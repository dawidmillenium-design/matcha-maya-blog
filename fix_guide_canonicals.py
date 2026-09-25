"""Align city guide canonicals with their published GitHub Pages URLs."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
BASE = "https://dawidmillenium-design.github.io/matcha-maya-blog/"
CANONICAL = re.compile(r'<link\b(?=[^>]*\brel\s*=\s*["\']canonical["\'])[^>]*>', re.I)


def main():
    updated = 0
    for page in sorted(ROOT.glob("*-coworking-guide.html")):
        original = page.read_text(encoding="utf-8-sig")
        replacement = f'<link rel="canonical" href="{BASE}{page.name}" />'
        content, count = CANONICAL.subn(replacement, original)
        if count != 1:
            raise ValueError(f"Expected one canonical in {page.name}; found {count}")
        if content != original:
            page.write_text(content, encoding="utf-8-sig")
            updated += 1
    print(f"Corrected {updated} city guide canonicals")


if __name__ == "__main__":
    main()
