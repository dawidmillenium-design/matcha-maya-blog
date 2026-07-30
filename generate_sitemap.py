import os
import glob
from datetime import datetime

print("--- GENERATING DYNAMIC XML SITEMAP ---")

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"
current_date = datetime.now().strftime("%Y-%m-%d")

# Collect all HTML files
root_html_files = glob.glob("*.html")
region_html_files = glob.glob("regions/*.html")

all_files = root_html_files + region_html_files

url_entries = []

for file in all_files:
    # Normalize path separator for web URLs
    clean_path = file.replace("\\", "/")
    
    # Exclude 404 pages or test drafts if present
    if "404" in clean_path or "test" in clean_path:
        continue

    # Assign URL priorities based on SILO tier
    if clean_path in ["index.html", "hub.html", "compare.html"]:
        priority = "1.0"
        changefreq = "daily"
    elif clean_path.startswith("regions/"):
        priority = "0.8"
        changefreq = "weekly"
    else:
        priority = "0.7"
        changefreq = "monthly"

    url_entries.append(f"""  <url>
    <loc>{domain}/{clean_path}</loc>
    <lastmod>{current_date}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\n".join(url_entries)}
</urlset>
"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"✔ Successfully generated 'sitemap.xml' containing {len(url_entries)} indexable URLs!")