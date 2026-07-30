import glob
import html

print("--- STARTING COMPARISON HUB GENERATOR ---")

comparison_files = sorted(glob.glob("*-vs-*-digital-nomad.html"))

links_html = ""
for file in comparison_files:
    # Format 'bangkok-vs-lisbon-digital-nomad.html' -> 'Bangkok Vs Lisbon'
    clean_name = file.replace("-digital-nomad.html", "").replace("-vs-", " vs ").title()
    links_html += f"""
    <div style="background: #ffffff; border: 1px solid #e0ebe0; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <h3 style="margin: 0 0 0.5rem 0; font-size: 1.1rem; color: #2d5a27;">⚖️ {html.escape(clean_name)}</h3>
        <p style="margin: 0 0 0.8rem 0; font-size: 0.9rem; color: #555;">Head-to-head breakdown of WiFi speeds, monthly budgets, coworking hubs, and lifestyle metrics.</p>
        <a href="{file}" style="color: #2d5a27; font-weight: bold; text-decoration: none;">View Comparison Guide →</a>
    </div>
    """

hub_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Nomad City Comparisons Index | Matcha Maya Blog</title>
    <meta name="description" content="Compare top digital nomad destinations side-by-side. Analyze WiFi speeds, cost of living, top cafes, and coworking spaces across global cities.">
    <link rel="canonical" href="https://dawidmillenium-design.github.io/matcha-maya-blog/compare.html">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Digital Nomad City Comparisons Index | Matcha Maya Blog">
    <meta property="og:description" content="Compare top digital nomad destinations side-by-side across internet speeds, living costs, and coworking spaces.">
    <meta property="og:url" content="https://dawidmillenium-design.github.io/matcha-maya-blog/compare.html">
    <meta property="og:site_name" content="Matcha Maya Blog">
    
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 1000px; margin: 0 auto; padding: 20px; }}
        header {{ background: #2d5a27; color: white; padding: 2rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        header h1 {{ margin: 0; font-size: 2.2rem; }}
        header a {{ color: #eef5ee; text-decoration: underline; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; margin: 2rem 0; }}
        footer {{ text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #666; }}
    </style>
</head>
<body>

    <header>
        <h1>⚖️ Digital Nomad City Comparison Directory</h1>
        <p>Data-Driven Head-to-Head Comparisons for Remote Workers</p>
        <p><a href="index.html">← Home</a> | <a href="hub.html">Global Regional Hub</a></p>
    </header>

    <main>
        <h2>Available City Comparisons ({len(comparison_files)} Guides)</h2>
        <div class="grid">
            {links_html}
        </div>
    </main>

    <footer>
        <p>© Matcha Maya Blog — Digital Nomad Research Index</p>
    </footer>

</body>
</html>
"""

with open("compare.html", "w", encoding="utf-8") as f:
    f.write(hub_content)

print(f"✔ Generated compare.html with links to {len(comparison_files)} comparison guides!")