import os
import glob
import re

print("--- STARTING INTERNAL LINK AUDIT ---")

html_files = glob.glob("*.html")
existing_files = set(html_files)
broken_links = []

for file in html_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        continue

    # Extract all href targets
    hrefs = re.findall(r'href=["\'](.*?)["\']', content)

    for href in hrefs:
        # Ignore external links, mailto, tel, javascript, or anchors
        if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#") or href.startswith("javascript:") or href == "":
            continue

        # Strip URL parameters and hash anchors
        target = href.split("?")[0].split("#")[0]

        # Handle full absolute domain paths pointing back to local repo
        if "matcha-maya-blog/" in target:
            target = target.split("matcha-maya-blog/")[-1]

        if target and target not in existing_files:
            broken_links.append((file, href, target))

print(f"Audit complete! Analyzed {len(html_files)} HTML files.")

if broken_links:
    print(f"\n❌ FOUND {len(broken_links)} BROKEN INTERNAL LINK(S):\n")
    # Group by missing target file to keep output clear
    missing_targets = {}
    for source, href, target in broken_links:
        if target not in missing_targets:
            missing_targets[target] = []
        missing_targets[target].append(source)

    for missing_file, sources in missing_targets.items():
        print(f"  • Missing File: '{missing_file}' (Referenced in {len(sources)} page(s), e.g., '{sources[0]}')")
else:
    print("\n✔ All internal links are valid and pointing to existing local files!")