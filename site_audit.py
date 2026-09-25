#!/usr/bin/env python3
"""Full-site HTML audit: on-page SEO, E-E-A-T, internal linking, fact-check flags, HTML validity."""
import os, re, json, html
from collections import Counter, defaultdict
from bs4 import BeautifulSoup

ROOT = "/workspace"
SITE = "https://dawidmillenium-design.github.io/matcha-maya-blog/"

def find_html_files():
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if ".git" in dirpath: continue
        for fn in filenames:
            if fn.lower().endswith((".html", ".htm")):
                files.append(os.path.join(dirpath, fn))
    return sorted(files)

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

def tag_balance_errors(raw):
    """Lightweight well-formedness check on raw markup (bs4 hides errors)."""
    errs = []
    stack = []
    # strip comments, doctype, script/style content
    txt = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    txt = re.sub(r"<!DOCTYPE[^>]*>", "", txt, flags=re.I)
    txt = re.sub(r"<script\b[^>]*>.*?</script\s*>", "<script></script>", txt, flags=re.S|re.I)
    txt = re.sub(r"<style\b[^>]*>.*?</style\s*>", "<style></style>", txt, flags=re.S|re.I)
    for m in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)((?:\"[^\"]*\"|'[^']*'|[^>\"'])*)>", txt):
        closing, name, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if name in VOID or attrs.rstrip().endswith("/"):
            continue
        if not closing:
            stack.append((name, m.start()))
        else:
            if stack and stack[-1][0] == name:
                stack.pop()
            else:
                # look for matching open further up
                names = [s[0] for s in stack]
                if name in names:
                    while stack and stack[-1][0] != name:
                        errs.append(f"unclosed <{stack[-1][0]}> before </{name}>")
                        stack.pop()
                    if stack: stack.pop()
                else:
                    errs.append(f"stray </{name}>")
    for name, _ in stack:
        errs.append(f"unclosed <{name}> at EOF")
    return errs

def visible_text_len(soup):
    for t in soup(["script", "style", "noscript"]): t.decompose()
    return len(soup.get_text(" ", strip=True).split())

def classify(fn):
    b = fn.lower()
    if "podcast-proposal" in b: return "podcast-proposal"
    if "coworking-guide" in b: return "city-guide"
    if "-comparison.html" in b: return "comparison-short"
    if "digital-nomad" in b: return "city-pair-comparison"
    if b.endswith("index.html"): return "index/hub"
    return "other"

results = []
files = find_html_files()
inbound = Counter()
outgoing = defaultdict(set)
targets_exist = {}

# first pass parse
parsed = {}
for f in files:
    raw = open(f, encoding="utf-8", errors="replace").read()
    soup = BeautifulSoup(raw, "html.parser")
    parsed[f] = (raw, soup)

# collect all basenames that can be link targets
all_names = {os.path.basename(f).lower() for f in files} | {os.path.basename(f).lower() for f in files}

for f, (raw, soup) in parsed.items():
    r = {"file": os.path.relpath(f, ROOT)}
    head = soup.head or soup
    title = head.title.get_text(strip=True) if head.title else ""
    md = head.find("meta", attrs={"name": re.compile("^description$", re.I)})
    desc = md["content"].strip() if md and md.has_attr("content") else ""
    kw = head.find("meta", attrs={"name": re.compile("^keywords$", re.I)})
    canon = head.find("link", attrs={"rel": lambda v: v and "canonical" in v})
    robots = head.find("meta", attrs={"name": "robots"})
    lang = (soup.html.get("lang") if soup.html else None)
    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")]
    h2s = soup.find_all("h2"); h3s = soup.find_all("h3")
    words = visible_text_len(soup)
    imgs = soup.find_all("img")
    imgs_noalt = [i for i in imgs if not (i.get("alt") or "").strip()]
    og = {m.get("property") or m.get("name") for m in soup.find_all("meta") if (m.get("property") or "").startswith("og:")}
    tw = any((m.get("name") or "").startswith("twitter") for m in soup.find_all("meta"))
    schemas = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
            items = data if isinstance(data, list) else [data]
            for it in items:
                st = it.get("@type", "?")
                schemas.append(st if isinstance(st, str) else ",".join(st))
                # author/date presence for EEAT
        except Exception as e:
            schemas.append(f"INVALID_JSON")
    text_all = soup.get_text(" ", strip=True)
    dates = re.findall(r"(?:Reviewed|Updated|Last updated|Fact-checked)\s*(?:\w+\s+)?(?:on\s+)?([A-Z][a-z]+ \d{1,2},?\s*\d{4}|\d{4})", text_all)
    datepub = head.find("meta", attrs={"property": "article:published_time"})
    authorm = head.find("meta", attrs={"name": "author"})
    has_author_block = bool(re.search(r"(?i)(written by|about the author|our team|editorial team|matcha maya)", text_all))
    external_links = []
    internal_links = []
    anchors = soup.find_all("a", href=True)
    for a in anchors:
        href = a["href"].strip()
        if href.startswith(("mailto:", "tel:", "#", "javascript:")): continue
        if href.startswith("http"):
            if "dawidmillenium-design.github.io" in href:
                tgt = href.split("/")[-1].lower().split("#")[0]
                internal_links.append(tgt)
            else:
                external_links.append(href)
        else:
            internal_links.append(href.split("#")[0].lower())
    for tgt in set(internal_links):
        if tgt: inbound[tgt] += 1
    outgoing[os.path.relpath(f, ROOT)] = {t for t in internal_links if t}
    nofollow_ext = sum(1 for a in anchors if "nofollow" in (a.get("rel") or []))
    urls_in_text = re.findall(r"https?://[\w./%-]+", text_all)

    # unverified claims (fact-check flags)
    claim_words = len(re.findall(r"(?i)\b(verified|fact[- ]checked|reviewed \d{4}|tested|confirmed|we visited|we interviewed|our research shows|according to)\b", text_all))
    cites = len(re.findall(r"(?i)\b(numbeo|expatistan|speedtest|nomadlist|world bank|un ?hcr|who\.int|gov|official|source|study|survey|data from)\b", text_all)) + len(set(external_links))

    r.update(dict(cat=classify(os.path.basename(f)), title=title, tlen=len(title),
                  desc=desc, dlen=len(desc), keywords=bool(kw), canonical=canon["href"] if canon else "",
                  robots=robots["content"] if robots and robots.has_attr("content") else "",
                  lang=lang or "", h1=len(h1s), h2=len(h2s), h3=len(h3s), words=words,
                  imgs=len(imgs), imgs_noalt=len(imgs_noalt), og=len(og), twitter=tw,
                  schema=schemas, dates=dates, article_date=bool(datepub), meta_author=bool(authorm),
                  author_block=has_author_block, int_links=len(internal_links), ext_links=len(external_links),
                  ext_domains=sorted({re.sub(r"^www\.", "", u.split("/")[2]) for u in external_links if "://" in u}),
                  nofollow_ext=nofollow_ext, claims=claim_words, citations=cites))

    # --- scoring ---
    seo = 0; seo_max = 0
    def add(cond, pts):
        global seo
        nonlocal_pts = pts
    score = 0
    checks = {}
    checks["title_30_60"] = 3 <= r["tlen"] <= 6 or True  # placeholder
    seo_items = [
        (15, 10 <= r["tlen"] <= 65),
        (15, 50 <= r["dlen"] <= 160),
        (10, bool(canon)),
        (5, bool(lang)),
        (10, r["h1"] == 1),
        (5, r["h2"] >= 2),
        (10, 300 <= r["words"]),
        (5, r["imgs_noalt"] == 0),
        (5, r["og"] >= 4),
        (5, r["twitter"]),
        (10, len([s for s in schemas if "INVALID" not in s]) >= 1),
        (5, r["int_links"] >= 3),
    ]
    r["seo_score"] = sum(p for p, ok in seo_items if ok)
    eeat_items = [
        (20, r["author_block"] or r["meta_author"] or any("Person" in s or "Organization" in s for s in schemas)),
        (15, bool(r["dates"]) or r["article_date"] or any("DatePublished" in raw for _ in [0])),
        (20, r["citations"] >= 3),
        (15, r["ext_links"] >= 2),
        (15, r["words"] >= 600),
        (15, any("About" in s or "Author" in s or "Organization" in s for s in schemas) or bool(re.search(r"(?i)experience|visited|interview|firsthand|lived", text_all))),
    ]
    r["eeat_score"] = sum(p for p, ok in eeat_items if ok)
    val_items = tag_balance_errors(raw)
    r["valid_issues"] = val_items[:6]
    r["valid_count"] = len(val_items)
    missing_targets = [t for t in set(internal_links) if t and os.path.basename(t).lower() not in all_names and not t.startswith(("http", "//"))]
    r["broken_int"] = missing_targets[:8]
    results.append(r)

# inbound counts
for r in results:
    r["inbound"] = inbound.get(os.path.basename(r["file"]).lower(), 0)

json.dump(results, open("/workspace/audit_results.json", "w"), indent=1)

# ---------- summary ----------
def avg(xs): return sum(xs)/len(xs) if xs else 0
cats = defaultdict(list)
for r in results: cats[r["cat"]].append(r)

print(f"TOTAL HTML FILES: {len(results)}")
print(f"Avg on-page SEO: {avg([r['seo_score'] for r in results]):.1f}/100 | Avg EEAT: {avg([r['eeat_score'] for r in results]):.1f}/100")
orphans = [r for r in results if r["inbound"] == 0]
print(f"Orphan pages (0 inbound internal links): {len(orphans)}")
tot_broken = sum(len(r["broken_int"]) for r in results)
print(f"Broken internal link references (total unique per page): {tot_broken}")
inv = sum(1 for r in results if "INVALID_JSON" in r["schema"])
print(f"Pages with invalid JSON-LD: {inv}")
pages_invalid = sum(1 for r in results if r["valid_count"] > 0)
print(f"Pages with HTML balance issues: {pages_invalid}")
nocanon = [r for r in results if not r["canonical"]]
print(f"Pages missing canonical: {len(nocanon)}")
noh1 = [r for r in results if r["h1"] != 1]
print(f"Pages without exactly one H1: {len(noh1)}")
shor = [r for r in results if r["words"] < 300]
print(f"Thin pages (<300 words): {len(shor)}")
noverify_claims = [r for r in results if r["claims"] >= 2 and r["citations"] < 2]
print(f"Pages with verification claims but <2 citations: {len(noverify_claims)}")
print("\nBY CATEGORY:")
for c, rs in sorted(cats.items()):
    print(f"  {c:22s} n={len(rs):4d}  SEO={avg([x['seo_score'] for x in rs]):5.1f}  EEAT={avg([x['eeat_score'] for x in rs]):5.1f}  words={avg([x['words'] for x in rs]):6.0f}  inbound={avg([x['inbound'] for x in rs]):5.1f}  brokenHTML%={100*sum(1 for x in rs if x['valid_count'])/len(rs):.0f}")
print("\nTOP 10 BY INBOUND LINKS:")
for r in sorted(results, key=lambda x: -x["inbound"])[:10]:
    print(f"  {r['inbound']:5d}  {r['file']}")
print("\nWORST 10 EEAT:")
for r in sorted(results, key=lambda x: x["eeat_score"])[:10]:
    print(f"  EEAT={r['eeat_score']:3d} SEO={r['seo_score']:3d} claims={r['claims']} cites={r['citations']}  {r['file']}")
print("\nSAMPLE ORPHANS:", [r["file"] for r in orphans][:15])
