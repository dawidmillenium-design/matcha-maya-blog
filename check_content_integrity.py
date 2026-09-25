"""Catch generated trust and metadata regressions before publishing."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMA = re.compile(r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', re.S | re.I)
BASE = 'https://dawidmillenium-design.github.io/matcha-maya-blog/'


def main():
    problems = []
    pages = sorted(ROOT.glob('*.html')) + sorted((ROOT / 'regions').glob('*.html'))
    for page in pages:
        s = page.read_text(encoding='utf-8-sig')
        for block in SCHEMA.findall(s):
            try:
                json.loads(block)
            except json.JSONDecodeError as exc:
                problems.append(f'{page.name}: invalid JSON-LD: {exc}')
        canonical = re.search(r'<link\b(?=[^>]*rel=["\']canonical["\'])[^>]*href=["\']([^"\']+)', s, re.I)
        og = re.search(r'<meta\b(?=[^>]*property=["\']og:url["\'])[^>]*content=["\']([^"\']+)', s, re.I)
        if canonical and og and canonical.group(1) != og.group(1):
            problems.append(f'{page.name}: canonical and og:url disagree')
        if page.name.endswith('-podcast-proposal.html'):
            if not canonical or canonical.group(1) != BASE + page.name:
                problems.append(f'{page.name}: missing or mismatched canonical')
            if 'noindex,follow' not in s or 'Podcast proposal:</strong> This is a planning draft.' not in s:
                problems.append(f'{page.name}: proposal lacks draft notice or noindex')
            if 'VIDEO_ID_' in s or '"@type": "VideoObject"' in s:
                problems.append(f'{page.name}: fake video placeholder or markup')
        if page.name.endswith('-digital-nomad.html') and '-vs-' in page.name:
            if len(re.findall(r'<h1\b', s, re.I)) != 1:
                problems.append(f'{page.name}: expected exactly one H1')
    if problems:
        raise SystemExit('\n'.join(problems[:30]) + f'\n{len(problems)} issues total')
    print(f'Checked {len(pages)} HTML pages: JSON-LD, URL identity and draft status passed')


if __name__ == '__main__':
    main()
