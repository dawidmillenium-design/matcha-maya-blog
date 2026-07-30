import os

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"
files = [f for f in os.listdir(".") if f.endswith(".html")]
files.sort()

# Build Sitemap XML
xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for f in files:
    url = f"{domain}/{f}" if f != "index.html" else f"{domain}/"
    priority = "1.0" if f == "index.html" else ("0.8" if "region" in f or "hub" in f else "0.6")
    xml += f'  <url>\n    <loc>{url}</loc>\n    <priority>{priority}</priority>\n  </url>\n'

xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as s:
    s.write(xml)

# Build Robots.txt
robots = f"User-agent: *\nAllow: /\n\nSitemap: {domain}/sitemap.xml\n"
with open("robots.txt", "w", encoding="utf-8") as r:
    r.write(robots)

print(f"SUCCESS: Generated sitemap.xml ({len(files)} URLs) and robots.txt!")
