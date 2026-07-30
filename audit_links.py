import os
import glob
import re

print("--- STARTING INTERNAL LINK AUDIT ---")

# Scan both root files and files inside subdirectories
all_files = glob.glob("*.html") + glob.glob("regions/*.html")
# Store all relative paths using standard forward slashes
existing_files = set(f.replace("\\", "/") for f in all_files)
broken_links = []

for file in all_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        continue

    hrefs = re.findall(r'href=["\'](.*?)["\']', content)

    for href in hrefs:
        if href.startswith("http") or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("#") or href.startswith("javascript:") or href == "":
            continue

        target = href.split("?")[0].split("#")[0]

        if "matcha-maya-blog/" in target:
            target = target.split("matcha-maya-blog/")[-1]

        # Resolve relative directory targets cleanly using POSIX style
        file_dir = os.path.dirname(file)
        if file_dir:
            raw_path = os.path.join(file_dir, target)
        else:
            raw_path = target

        # Normalize without converting to Windows backslashes
        resolved_target = os.path.normpath(raw_path).replace("\\", "/")

        if resolved_target and resolved_target not in existing_files:
            broken_links.append((file, href, resolved_target))

print(f"Audit complete! Analyzed {len(all_files)} HTML files.")

if broken_links:
    print(f"\n❌ FOUND {len(broken_links)} BROKEN INTERNAL LINK(S):\n")
    missing_targets = {}
    for source, href, target in broken_links:
        if target not in missing_targets:
            missing_targets[target] = []
        missing_targets[target].append(source)

    for missing_file, sources in missing_targets.items():
        print(f"  • Missing File: '{missing_file}' (Referenced in {len(sources)} page(s), e.g., '{sources[0]}')")
else:
    print("\n✔ All internal links are valid and pointing to existing local files!")