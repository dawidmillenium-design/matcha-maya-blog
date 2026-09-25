"""Replace unsupported uniform metrics with an honest city research checklist.

The former 213 city matrices all contained the same cost, speed, and safety
figures. They remain accessible as navigation tools and outside the sitemap.
Re-run this script to rebuild the category pages in a consistent design.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://dawidmillenium-design.github.io/matcha-maya-blog/"


def card(city, slug):
    name = escape(city)
    guide = f"{slug}-coworking-guide.html"
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name} coworking research checklist | Matcha Maya</title>
<meta name="description" content="Research coworking options in {name}. Check current desk prices, internet, housing and venue access before choosing a workspace.">
<meta name="robots" content="noindex,follow">
<link rel="stylesheet" href="comparison-pages.css"></head><body>
<header class="site-header"><div class="nav-container"><a class="brand-logo" href="index.html">MATCHA <span>MAYA</span></a><nav class="main-nav" aria-label="Main navigation"><a href="index.html">Home</a><a href="index2.html">City guides</a><a href="comparison.html" aria-current="page">City research</a><a href="about.html">About</a></nav></div></header>
<section class="hero"><div class="hero-inner"><p class="eyebrow">Matcha Maya · City research</p><h1>{name}: coworking research checklist</h1><p>A practical starting point for comparing workspaces in {name}. Check current figures and availability with the venue before booking.</p><a href="comparison.html">← Browse all cities</a></div></section>
<main class="container"><div class="notice"><p><strong>Research note:</strong> This page does not publish a verified city average for rent, internet speed, safety or desk prices. Request quotes and test the connection you will actually use.</p></div>
<div class="check-grid"><section class="check-card"><h2>Desk access and price</h2><p>Ask for the current day pass and monthly rate, opening hours, deposit, and cancellation terms.</p></section><section class="check-card"><h2>Internet and calls</h2><p>Test upload and download speeds at the desk and ask about quiet rooms, power and backup connectivity.</p></section><section class="check-card"><h2>Housing and journey</h2><p>Compare a real apartment quote with the commute, transport options, and the workspace's location.</p></section><section class="check-card"><h2>Comfort and fit</h2><p>Check seating, noise, accessibility, and whether the space suits your work schedule.</p></section></div>
<div class="actions"><a href="{guide}">Read the {name} coworking guide →</a><a href="comparison.html">Choose another city</a></div></main>
<footer class="site-footer"><a href="index.html">Home</a> · <a href="comparison.html">City research directory</a> · <a href="about.html">About Matcha Maya</a></footer></body></html>
'''


def main():
    pages = sorted(ROOT.glob("*-comparison.html"))
    assert len(pages) == 213, f"Expected 213 city pages; found {len(pages)}"
    for page in pages:
        slug = page.name.removesuffix("-comparison.html")
        guide = ROOT / f"{slug}-coworking-guide.html"
        if not guide.is_file():
            raise FileNotFoundError(guide)
        city = slug.replace("-", " ").title()
        page.write_text(card(city, slug), encoding="utf-8")
    print(f"Updated {len(pages)} city research cards")


if __name__ == "__main__":
    main()
