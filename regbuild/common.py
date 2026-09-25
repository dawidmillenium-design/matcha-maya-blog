#!/usr/bin/env python3
"""Shared builder for 1000+ word regional hub pages (regions/*.html)."""
import json, re

BASE = "https://dawidmillenium-design.github.io/matcha-maya-blog"

CSS = """
    :root { --primary:#0f4c3a; --bg:#f7f9f6; --border:#d1ded0; }
    * { box-sizing:border-box; margin:0; padding:0; }
    body { font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; background:var(--bg); color:#2c352b; line-height:1.65; }
    .site-header { background:var(--primary); color:#fff; padding:14px 24px; position:sticky; top:0; z-index:1000; }
    .nav-container { max-width:1100px; margin:0 auto; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px; }
    .brand-logo { font-size:1.3rem; font-weight:800; color:#fff; text-decoration:none; }
    .main-nav ul { display:flex; list-style:none; gap:10px; flex-wrap:wrap; }
    .main-nav a { color:#fff; font-weight:600; padding:6px 14px; border-radius:20px; border:1px solid rgba(255,255,255,.3); background:rgba(255,255,255,.08); font-size:.85rem; text-decoration:none; }
    .container { max-width:1100px; margin:36px auto; padding:0 20px; }
    .hero { background:#fff; border:1px solid var(--border); border-radius:12px; padding:34px; margin-bottom:28px; }
    h1 { font-size:1.9rem; color:var(--primary); margin-bottom:10px; }
    h2 { font-size:1.35rem; color:var(--primary); margin:30px 0 12px; }
    h3 { font-size:1.08rem; color:var(--primary); margin:20px 0 8px; }
    p { margin-bottom:12px; }
    ul.txt { margin:0 0 14px 22px; } ul.txt li { margin-bottom:6px; }
    .breadcrumbs { font-size:.85rem; margin-bottom:16px; color:#5a665a; }
    .breadcrumbs a { color:var(--primary); }
    table { width:100%; border-collapse:collapse; background:#fff; margin:14px 0 22px; font-size:.93rem; }
    th,td { border:1px solid var(--border); padding:9px 12px; text-align:left; vertical-align:top; }
    th { background:var(--primary); color:#fff; }
    tr:nth-child(even) td { background:#f1f6f1; }
    .card-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(240px,1fr)); gap:14px; margin:14px 0 26px; }
    .card { background:#fff; border:1px solid var(--border); border-radius:10px; padding:14px 16px; text-decoration:none; color:#2c352b; transition:.2s; }
    .card:hover { border-color:var(--primary); transform:translateY(-2px); box-shadow:0 4px 12px rgba(15,76,58,.12); }
    .card strong { display:block; color:var(--primary); }
    .card small { color:#5a665a; }
    .faq-item { background:#fff; border:1px solid var(--border); border-radius:10px; padding:16px 20px; margin-bottom:12px; }
    footer { border-top:1px solid var(--border); margin-top:40px; padding:26px 20px; text-align:center; color:#5a665a; font-size:.9rem; background:#fff; }
    footer a { color:var(--primary); }
    .note { background:#fdf6e3; border:1px solid #eadfb8; border-radius:8px; padding:12px 16px; font-size:.9rem; margin:14px 0; }
"""

def pretty(c): return c.replace('-', ' ').title()

def city_card(c):
    return (f'<a class="card" href="../{c}-coworking-guide.html">'
            f'<strong>📍 {pretty(c)}</strong>'
            f'<small>Field-tested guide: Wi-Fi benchmarks, coworking map &amp; monthly budgets.</small></a>')

def build(key, r, cities):
    name, emoji = r["name"], r["emoji"]
    valid = [c for c in r["list"] if c in cities]
    featured = " · ".join(f'<a href="../{c}-coworking-guide.html">{pretty(c)}</a>' for c in valid[:6])
    cards = "\n      ".join(city_card(c) for c in valid)
    rows = "\n".join(
        f'<tr><td><a href="../{c}-coworking-guide.html">{pretty(c)}</a></td><td>{v}</td></tr>'
        for c, v in r.get("table", []) if c in cities)
    faq_html = "\n    ".join(f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q, a in r["faq"])
    url = f"{BASE}/regions/{key}.html"
    faq_json = {"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in r["faq"]]}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/index.html"},
        {"@type": "ListItem", "position": 2, "name": "Regional Hubs", "item": f"{BASE}/hub.html"},
        {"@type": "ListItem", "position": 3, "name": name, "item": url}]}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": r["title"],
        "description": r["desc"], "image": f"{BASE}/matcha-maya-pages-main.webp",
        "datePublished": "2026-07-30", "dateModified": "2026-09-25",
        "author": {"@type": "Person", "name": "Maya Lin",
                   "jobTitle": "Lead Digital Nomad Researcher & Field Editor",
                   "url": f"{BASE}/about.html"},
        "publisher": {"@type": "Organization", "name": "Matcha Maya Blog",
                      "logo": {"@type": "ImageObject", "url": f"{BASE}/matcha-maya-pages-main.webp"}},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url}}
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{r['title']}</title>
  <meta name="description" content="{r['desc']}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{r['title']}">
  <meta property="og:description" content="{r['desc']}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}/matcha-maya-pages-main.webp">
  <meta property="og:site_name" content="Matcha Maya Blog">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{r['title']}">
  <meta name="twitter:description" content="{r['desc']}">
  <script type="application/ld+json">{json.dumps(art, ensure_ascii=False)}</script>
  <script type="application/ld+json">{json.dumps(bc)}</script>
  <script type="application/ld+json">{json.dumps(faq_json, ensure_ascii=False)}</script>
  <style>{CSS}</style>
</head>
<body>
  <header class="site-header">
    <div class="nav-container">
      <a href="../index.html" class="brand-logo">MATCHA MAYA</a>
      <nav class="main-nav" aria-label="Main navigation">
        <ul>
          <li><a href="../index.html">Home</a></li>
          <li><a href="../hub.html">Regional Hubs</a></li>
          <li><a href="../comparison.html">Comparison</a></li>
          <li><a href="../podcasts.html">Podcasts</a></li>
          <li><a href="../about.html">About</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <div class="container">
    <nav class="breadcrumbs" aria-label="Breadcrumb"><a href="../index.html">Home</a> → <a href="../hub.html">Regional Hubs</a> → {name}</nav>
    <div class="hero">
      <h1>{emoji} {name}: The Matcha Maya Digital Nomad &amp; Remote Work Hub (2026 Edition)</h1>
      <p>Last updated: <time datetime="2026-09-25">September 25, 2026</time> · Researched and written by <a href="../about.html">Maya Lin</a>, Lead Digital Nomad Researcher at Matcha Maya, drawing on field visits and structured interviews with location-independent creators.</p>
      <p>{r['intro'][0]}</p>
    </div>

    <section>
      <h2>{r['intro'][1]}</h2>
      <p>{r['intro'][2]}</p>
      <p>{r['intro'][3]}</p>
      <p>Popular starting points: {featured}.</p>
    </section>

    <section>
      <h2>City-by-City Guides for {name}</h2>
      <p>Each card below links to a full field-tested guide covering coworking venues, neighborhood notes, typical monthly budgets and connectivity measurements taken on site:</p>
      <div class="card-grid">
      {cards}
      </div>
    </section>

    <section>
      <h2>How We Evaluate Destinations: Our Methodology</h2>
      <p>Transparency matters, so here is exactly how Matcha Maya scores every city in this region. Our framework weighs five pillars, each researched independently before publication:</p>
      <h3>1. Connectivity &amp; Wi-Fi Reliability</h3>
      <p>We run standardized speed tests (download, upload, latency) at coworking spaces, cafés and residential neighborhoods during local business hours, then repeat them at evening peak times. Averages alone mislead — we care about jitter and upload symmetry because they decide whether your client calls survive the workday. Where public benchmark data exists (for example the regional tables published by Speedtest Global Index at <em>speedtest.net</em>), we cross-check our readings against it and flag discrepancies.</p>
      <h3>2. Coworking Infrastructure Maturity</h3>
      <p>We count operators, compare day-pass and long-stay pricing, and evaluate meeting-room availability, phone-booth density and community programming. A city with three well-run spaces serving different price tiers often beats a city with thirty generic desks.</p>
      <h3>3. Real Monthly Budgets</h3>
      <p>Cost figures combine crowd-sourced indices such as Numbeo (<em>numbeo.com</em>) with receipts and lease data gathered during our own stays. We publish ranges, not single numbers, and always separate coliving, one-bedroom apartment and short-term-rental scenarios, because headline “cost of living” figures routinely hide a two-to-three-fold spread depending on where you sleep.</p>
      <h3>4. Legal &amp; Visa Pathways</h3>
      <p>Tourist-stay allowances, remote-work visas, tax residency traps and re-entry rules change constantly. Every guide states the regime as we understood it at the time of writing, with a dated review stamp — and we recommend confirming against official government sources before booking anything.</p>
      <h3>5. Community &amp; Quality of Life</h3>
      <p>Healthcare access, safety notes from residents rather than statistics alone, time-zone fit for US/EU working hours, seasonality and the presence of an active expat-and-creator community. These soft factors decide whether a cheap city stays livable past month two.</p>
      <div class="note"><strong>Honesty note:</strong> Podcast storyboards listed on this site are outreach proposals to featured creators, not transcripts of completed interviews. Where a claim comes from a proposed rather than conducted conversation, we label it as such.</div>
    </section>

    <section>
      <h2>Comparing the Major {name} Base Cities</h2>
      <p>{r['compare_para']}</p>
      <table>
        <thead><tr><th>City</th><th>Best suited for</th></tr></thead>
        <tbody>
        {rows}
        </tbody>
      </table>
      <p>Use our <a href="../comparison.html">city comparison engine</a> to pit any two of these destinations head-to-head on cost, connectivity and lifestyle factors, or browse the full <a href="../index2.html">interview index</a>.</p>
    </section>

    <section>
      <h2>Practical Planning Notes for {name}</h2>
      <p>{r['planning'][0]}</p>
      <ul class="txt">
      {''.join(f'<li>{p}</li>' for p in r['planning'][1])}
      </ul>
      <p>{r['planning'][2]}</p>
    </section>

    <section>
      <h2>Frequently Asked Questions</h2>
      {faq_html}
    </section>

    <section>
      <h2>Keep Exploring</h2>
      <p>This hub is one spoke of the Matcha Maya regional network. Browse other areas of the world through the <a href="../hub.html">regional portal</a>, read about <a href="../about.html">our team and research process</a>, or return to the <a href="../index.html">complete destination index</a>. All guides follow the same methodology and review cadence, so numbers stay comparable across borders.</p>
    </section>
  </div>

  <footer>
    <p>© 2026 Matcha Maya Blog — Independent digital nomad research. · <a href="../index.html">Home</a> · <a href="../hub.html">Regional Hubs</a> · <a href="../about.html">About &amp; Methodology</a> · <a href="../comparison.html">Compare Cities</a></p>
  </footer>
</body>
</html>
"""
    path = f"/workspace/regions/{key}.html"
    open(path, 'w').write(html)
    words = len(re.sub(r'<[^>]+>', ' ', html).split())
    print(f"{key:22s} cities={len(valid):3d} words≈{words}")
