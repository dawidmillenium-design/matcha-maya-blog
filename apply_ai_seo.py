import os
import glob
import datetime

print("--- STARTING ADVANCED AI SEO UPGRADE ---")

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"

# 1. Update robots.txt
robots_content = f"""User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {domain}/sitemap.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

print("✔ 1. Updated robots.txt with AI Crawler Allow rules")

# 2. Update sitemap.xml
all_html_files = sorted(glob.glob("*.html"))
now_iso = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for html_file in all_html_files:
    sitemap_xml += f"""  <url>
    <loc>{domain}/{html_file}</loc>
    <lastmod>{now_iso}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""

sitemap_xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print(f"✔ 2. Generated sitemap.xml covering {len(all_html_files)} HTML pages")

# 3. Inject Speakable Schema into Spoke Guides
speakable_injected_count = 0
speakable_snippet = """
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": [".summary-box", ".ai-atomic-summary", "h1"]
      }
    }
    </script>
"""

for html_file in all_html_files:
    if html_file.endswith("-coworking-guide.html"):
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()

        if '"SpeakableSpecification"' not in content and "</head>" in content:
            updated_content = content.replace("</head>", f"{speakable_snippet}\n</head>")
            with open(html_file, "w", encoding="utf-8") as f:
                f.write(updated_content)
            speakable_injected_count += 1

print(f"✔ 3. Injected SpeakableSpecification Schema into {speakable_injected_count} spoke pages!")
print("--- ADVANCED AI SEO UPGRADES COMPLETE ---")