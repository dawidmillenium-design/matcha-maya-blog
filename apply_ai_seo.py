import os
import glob
import datetime
from xml.etree import ElementTree as ET

print("--- STARTING ADVANCED AI SEO UPGRADE ---")

# 1. GENERATE ROBOTS.TXT FOR AI CRAWLERS
robots_content = """User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

Sitemap: https://dawidmillenium-design.github.io/matcha-maya-blog/sitemap.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)
print("✔ 1. Created robots.txt with AI Crawler Allow rules")


# 2. GENERATE XML SITEMAP WITH DYNAMIC LASTMOD TIMESTAMPS
domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"
html_files = glob.glob("*.html")

urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for page in sorted(html_files):
    url_elem = ET.SubElement(urlset, "url")
    
    # Location
    loc = ET.SubElement(url_elem, "loc")
    loc.text = f"{domain}/{page}"
    
    # Dynamic Last Modified Timestamp
    mtime = os.path.getmtime(page)
    lastmod_date = datetime.datetime.fromtimestamp(mtime, tz=datetime.timezone.utc).strftime('%Y-%m-%d')
    lastmod = ET.SubElement(url_elem, "lastmod")
    lastmod.text = lastmod_date
    
    # Priority tuning
    priority = ET.SubElement(url_elem, "priority")
    if page == "index.html":
        priority.text = "1.0"
    elif "hub" in page or "guide" in page:
        priority.text = "0.8"
    else:
        priority.text = "0.6"

tree = ET.ElementTree(urlset)
ET.indent(tree, space="  ", level=0)
tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
print(f"✔ 2. Generated sitemap.xml with dynamic <lastmod> timestamps covering {len(html_files)} HTML pages")


# 3. GENERATE HUB DATASET SCHEMA
dataset_schema = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Global Digital Nomad & Coworking City Metrics Index",
  "description": "Structured repository containing internet connectivity speeds, cost of living estimates, and remote work infrastructure data across 525+ global nomad hubs.",
  "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/hub.html",
  "keywords": ["Digital Nomad", "Coworking", "WiFi Speeds", "Cost of Living", "Remote Work Cities"],
  "creator": {
    "@type": "Organization",
    "name": "Matcha Maya Blog",
    "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/"
  },
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "isAccessibleForFree": true
}
</script>"""

with open("hub_dataset_schema.jsonld", "w", encoding="utf-8") as f:
    f.write(dataset_schema)
print("✔ 3. Created Dataset schema for AI Research Engine Indexing")

print("--- ADVANCED AI SEO UPGRADES COMPLETE ---")