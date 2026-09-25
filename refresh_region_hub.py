"""Build an honest regional directory from the available region pages."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = 'https://dawidmillenium-design.github.io/matcha-maya-blog/'


def main():
    regions = sorted((ROOT / 'regions').glob('*.html'))
    links = '\n'.join(
        f'<a class="grid-card" href="regions/{p.name}"><strong>{escape(p.stem.replace("-", " ").title())}</strong><span>Explore →</span></a>'
        for p in regions
    )
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Regional coworking guide directory | Matcha Maya</title><meta name="description" content="Browse Matcha Maya coworking guides by region, then review individual city pages and verify local details before booking.">
<link rel="canonical" href="{BASE}hub.html"><link rel="stylesheet" href="comparison-pages.css"></head><body>
<header class="site-header"><div class="nav-container"><a class="brand-logo" href="index.html">MATCHA <span>MAYA</span></a><nav class="main-nav" aria-label="Main navigation"><a href="index.html">Home</a><a href="index2.html">City guides</a><a href="hub.html" aria-current="page">Regions</a><a href="comparison.html">City research</a></nav></div></header>
<section class="hero"><div class="hero-inner"><p class="eyebrow">Explore by region</p><h1>Regional coworking guide directory</h1><p>Find city guides across {len(regions)} regions. These are planning resources; check current prices, workspace access and local rules before relying on a guide.</p></div></section>
<main class="container"><div class="link-grid">{links}</div><div class="actions"><a href="index2.html">Browse all city guides</a><a href="comparison.html">City research directory</a></div></main>
<footer class="site-footer"><a href="index.html">Home</a> · <a href="about.html">About Matcha Maya</a></footer></body></html>'''
    (ROOT / 'hub.html').write_text(html, encoding='utf-8')
    print(f'Updated region hub with {len(regions)} links')


if __name__ == '__main__':
    main()
