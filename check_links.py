import os
import re

all_html_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            all_html_files.append(rel_path)

print(f"?? Found {len(all_html_files)} total HTML files to scan.\n")

broken_links = []
scanned_links = 0
href_pattern = re.compile(r'href=["\'](.*?)["\']', re.IGNORECASE)

for html_file in all_html_files:
    with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    links = href_pattern.findall(content)
    file_dir = os.path.dirname(html_file)

    for link in links:
        if link.startswith("http://") or link.startswith("https://") or link.startswith("#") or link.startswith("mailto:"):
            continue

        scanned_links += 1

        if file_dir:
            target_path = os.path.normpath(os.path.join(file_dir, link)).replace("\\", "/")
        else:
            target_path = os.path.normpath(link).replace("\\", "/")

        if not os.path.exists(target_path):
            broken_links.append({
                "source": html_file,
                "target": link,
                "resolved": target_path
            })

print(f"? Total internal links scanned: {scanned_links}")

if broken_links:
    print(f"\n? FOUND {len(broken_links)} BROKEN INTERNAL LINKS:\n")
    for b in broken_links:
        print(f"• In '{b['source']}' --> Broken link: '{b['target']}' (Missing at: '{b['resolved']}')")
else:
    print("\n?? PERFECT! 0 broken internal links found across all files!")
