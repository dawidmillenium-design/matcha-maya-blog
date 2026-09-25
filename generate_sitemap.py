"""Publish editorial hubs and city guides in the discovery sitemap.

Generated proposals and comparison matrices remain available through site
navigation while they await editorial review. Sitemap omission is not noindex.
"""

from pathlib import Path
from urllib.parse import quote
from xml.etree.ElementTree import Element, SubElement, ElementTree, register_namespace

BASE = "https://dawidmillenium-design.github.io/matcha-maya-blog/"
ROOT = Path(__file__).resolve().parent
HUBS = {
    "index.html", "index2.html", "about.html", "hub.html", "compare.html",
    "comparison.html", "podcasts.html",
}


def selected_pages():
    for name in sorted(HUBS):
        if (ROOT / name).is_file():
            yield name
    for page in sorted((ROOT / "regions").glob("*.html")):
        yield page.relative_to(ROOT).as_posix()
    for page in sorted(ROOT.glob("*-coworking-guide.html")):
        yield page.name


def main():
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    register_namespace("", namespace)
    root = Element(f"{{{namespace}}}urlset")
    pages = list(selected_pages())
    for name in pages:
        entry = SubElement(root, f"{{{namespace}}}url")
        SubElement(entry, f"{{{namespace}}}loc").text = BASE + quote(name)
    ElementTree(root).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Wrote {len(pages)} editorial pages to sitemap.xml")


if __name__ == "__main__":
    main()
