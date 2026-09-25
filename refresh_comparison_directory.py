"""Build the city research directory from its 213 published card files."""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = "https://dawidmillenium-design.github.io/matcha-maya-blog/"


def main():
    pages = sorted(ROOT.glob("*-comparison.html"))
    cards = "\n".join(
        f'<a class="grid-card" href="{page.name}"><strong>{escape(page.name.removesuffix("-comparison.html").replace("-", " ").title())}</strong><span>Research checklist →</span></a>'
        for page in pages
    )
    document = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>City coworking research directory | Matcha Maya</title>
<meta name="description" content="Browse 213 city coworking research checklists and guides. Learn what to verify about workspace prices, connectivity, housing and access.">
<link rel="canonical" href="{BASE}comparison.html"><link rel="stylesheet" href="comparison-pages.css"></head><body>
<header class="site-header"><div class="nav-container"><a class="brand-logo" href="index.html">MATCHA <span>MAYA</span></a><nav class="main-nav" aria-label="Main navigation"><a href="index.html">Home</a><a href="index2.html">City guides</a><a href="comparison.html" aria-current="page">City research</a><a href="about.html">About</a></nav></div></header>
<section class="hero"><div class="hero-inner"><p class="eyebrow">Matcha Maya · Explore by city</p><h1>City coworking research directory</h1><p>Find a city, then check the questions that matter before you commit to a desk or apartment. Current prices, speeds and availability should be confirmed directly.</p></div></section>
<main class="container"><div class="notice"><p><strong>How to use this directory:</strong> These 213 cards are research checklists, not verified price tables. Open a city card for practical checks and a link to its full coworking guide.</p></div>
<div class="search-filter-box"><label for="compSearch">Find a city</label><input type="search" id="compSearch" placeholder="For example: Tbilisi or Bangkok" autocomplete="off" aria-controls="comparisonGrid"><p id="resultCount" role="status" aria-live="polite">Showing {len(pages)} cities</p></div>
<div class="link-grid" id="comparisonGrid">{cards}</div><p id="noResults" hidden>No city matches your search. Try a shorter name.</p></main>
<footer class="site-footer"><a href="index.html">Home</a> · <a href="index2.html">Coworking guides</a> · <a href="about.html">About Matcha Maya</a></footer>
<script>const search=document.getElementById('compSearch'),cards=[...document.querySelectorAll('#comparisonGrid a')],count=document.getElementById('resultCount'),empty=document.getElementById('noResults');search.addEventListener('input',()=>{{const q=search.value.trim().toLocaleLowerCase();let n=0;for(const card of cards){{const show=card.textContent.toLocaleLowerCase().includes(q);card.hidden=!show;if(show)n++}}count.textContent=`Showing ${{n}} cities`;empty.hidden=n!==0}});</script>
</body></html>'''
    (ROOT / "comparison.html").write_text(document, encoding="utf-8")
    print(f"Built directory with {len(pages)} city links")


if __name__ == "__main__":
    main()
