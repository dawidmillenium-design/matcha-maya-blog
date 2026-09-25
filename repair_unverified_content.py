"""Remove broken or misleading generated claims from legacy page families.

No source research is implied by these mechanical repairs. The proposal and
city-pair templates remain noindex until editorial verification is complete.
"""

import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://dawidmillenium-design.github.io/matcha-maya-blog/"
SCHEMA = re.compile(r'<script\b[^>]*type="application/ld\+json"[^>]*>.*?</script>', re.I | re.S)
FAQ_BLOCK = re.compile(r',\s*\{\s*"@context": "https://schema.org",\s*"@type": "FAQPage",.*?(?=,\s*\{\s*"@context": "https://schema.org",\s*"@type": "BreadcrumbList")', re.S)


def set_robots(s):
    if re.search(r'<meta\s+name="robots"', s, re.I):
        return re.sub(r'<meta\s+name="robots"[^>]*>', '<meta name="robots" content="noindex,follow">', s, count=1, flags=re.I)
    return s.replace('</head>', '  <meta name="robots" content="noindex,follow">\n</head>', 1)


def repair_guide(s):
    blocks = SCHEMA.findall(s)
    candidates = [block for block in blocks if '"@type": "FAQPage"' in block]
    if not candidates:
        return s
    assert len(candidates) == 1, len(candidates)
    repaired, n = FAQ_BLOCK.subn('', candidates[0], count=1)
    assert n == 1, 'Expected one unsupported FAQ schema block'
    return s.replace(candidates[0], repaired, 1)


def repair_proposal(s, name):
    if 'Podcast proposal:</strong> This is a planning draft.' in s:
        return s
    s = set_robots(s)
    if not re.search(r'<link\b[^>]*rel="canonical"', s, re.I):
        s = s.replace('</head>', f'  <link rel="canonical" href="{BASE}{name}">\n</head>', 1)
    # Remove fabricated editorial endorsements and the completed-interview label.
    replacements = {
        'Verified &bull; Reviewed July 2026': 'Proposal draft · Details require independent verification',
        'Fact-checked and verified by the Matcha Maya Global Research Team.': 'Planning draft. Interviews and local claims have not been independently verified.',
        'E-E-A-T Compliant': 'Research pending',
        'Podcast Interview: 13 Key Local Questions Answered': 'Proposed interview questions and draft research notes',
        'Verified Ride-Hailing & Local Transit': 'Ride-Hailing & Local Transit to Check',
        'Verified Rent & Accommodation Benchmarks': 'Rent & Accommodation Figures to Check',
        'Verified rental ranges across': 'Unconfirmed rental ranges across',
        '(Verified 2026)': '(figures require confirmation)',
        'Verified independent blogs': 'Suggested independent blogs',
        'Verified digital nomad visas': 'Possible digital nomad visas to check',
        '<strong>Answer:</strong>': '<strong>Draft research note (unverified):</strong>',
        '220 Interviews': 'City guides and proposals',
    }
    for before, after in replacements.items():
        s = s.replace(before, after)
    # The older 90-page template claimed a recorded interview with a generated
    # persona. Its content remains visible as a clearly labeled draft.
    s = re.sub(r'\bMATCHA MAYA Interviews\b', 'MATCHA MAYA proposes an interview with', s, flags=re.I)
    s = re.sub(r'\bVideo Call Interview\b', 'Interview concept (not recorded)', s, flags=re.I)
    s = re.sub(r'\bIn this video call interview, she connects with\b', 'The proposed interview would connect with', s, flags=re.I)
    s = re.sub(r'\bIn this Interview concept \(not recorded\), she connects with\b', 'The proposed interview would connect with', s, flags=re.I)
    s = re.sub(r'\bPublished: July 2026\b', 'Draft proposal', s)
    s = SCHEMA.sub(lambda m: '' if '"@type": "VideoObject"' in m.group() else m.group(), s)
    # A VIDEO_ID_* embed is a placeholder, not a published episode.
    s = re.sub(r'<div class="video-container"[^>]*>.*?VIDEO_ID_[A-Z_]+.*?</div>\s*', '', s, flags=re.S)
    s = s.replace('not been independently verified', 'not been independently checked')
    s = re.sub(r'\bVerified\b', 'Unconfirmed', s)
    notice = '<aside role="note" style="padding:16px;margin:20px auto;max-width:920px;border-left:4px solid #0f6b4d;background:#ecfdf5;color:#173b2a"><strong>Podcast proposal:</strong> This is a planning draft. No interview or venue visit is confirmed. Prices, visa details, safety information, and quoted local claims need verification before use.</aside>\n'
    assert '<body' in s
    s = re.sub(r'(<body\b[^>]*>)', r'\1\n' + notice, s, count=1, flags=re.I)
    return s


def repair_pair(s, name):
    if '<h1' in s.lower() and 'noindex,follow' in s:
        return s
    s = set_robots(s)
    assert '<h1' not in s.lower()
    city = escape(name.removesuffix('-digital-nomad.html').replace('-vs-', ' vs ').replace('-', ' ').title())
    intro = f'<div style="max-width:900px;margin:20px auto;padding:0 20px"><h1>{city}: remote work comparison</h1><p role="note">Planning draft: quoted prices, internet speeds and venue recommendations are unverified estimates. Confirm them with current primary sources before making a decision.</p></div>\n'
    return s.replace('</header>', '</header>\n' + intro, 1)


def main():
    groups = [('*-coworking-guide.html', repair_guide), ('*-podcast-proposal.html', repair_proposal), ('*-vs-*-digital-nomad.html', repair_pair)]
    for pattern, fn in groups:
        pages = sorted(ROOT.glob(pattern))
        for page in pages:
            s = page.read_text(encoding='utf-8-sig')
            changed = fn(s) if fn is repair_guide else fn(s, page.name)
            if changed != s:
                page.write_text(changed, encoding='utf-8')
        print(pattern, len(pages))


if __name__ == '__main__':
    main()
