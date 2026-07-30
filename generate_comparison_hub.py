import os
import glob
from datetime import datetime

print("--- GENERATING COMPARISON HUB WITH INSTANT FILTER ---")

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"
current_date = datetime.now().strftime("%Y-%m-%d")

# Find all comparison HTML files
comp_files = sorted(glob.glob("*-vs-*-digital-nomad.html"))

cards_html = ""
for f in comp_files:
    # Format readable title from filename
    raw_name = f.replace("-digital-nomad.html", "").replace("-vs-", " vs ")
    title_display = raw_name.replace("-", " ").title()
    
    cards_html += f"""
    <div class="card" data-title="{title_display.lower()}">
        <h3 style="margin: 0 0 0.5rem 0; color: #2d5a27;">⚖️ {title_display}</h3>
        <p style="margin: 0 0 1rem 0; font-size: 0.9rem; color: #555;">Head-to-head analysis of internet speeds, living costs, and coworking hubs.</p>
        <a href="{f}" style="color: #2d5a27; font-weight: bold; text-decoration: none;">Compare Destinations →</a>
    </div>
    """

hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Nomad City Comparison Directory | Matcha Maya Blog</title>
    <meta name="description" content="Compare digital nomad destinations head-to-head. Compare internet speed, cost of living, visas, and coworking infrastructure across top remote work hubs.">
    <link rel="canonical" href="{domain}/compare.html">
    <meta property="article:modified_time" content="{current_date}">
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "Digital Nomad City Comparison Directory",
      "description": "Head-to-head remote work comparison index covering cost of living, internet speed, and lifestyle.",
      "url": "{domain}/compare.html",
      "dateModified": "{current_date}"
    }}
    </script>
    
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 1000px; margin: 0 auto; padding: 20px; }}
        header {{ background: #2d5a27; color: white; padding: 2rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        header a {{ color: #eef5ee; text-decoration: underline; }}
        .search-container {{ margin: 1.5rem 0 2rem 0; text-align: center; }}
        .search-input {{ width: 100%; max-width: 500px; padding: 12px 18px; font-size: 1rem; border: 2px solid #2d5a27; border-radius: 25px; outline: none; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; margin: 2rem 0; }}
        .card {{ background: #ffffff; border: 1px solid #e0ebe0; padding: 1.2rem; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); transition: transform 0.15s ease; }}
        .card:hover {{ transform: translateY(-2px); }}
        footer {{ text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #666; }}
    </style>
</head>
<body>

    <header>
        <h1>⚖️ Digital Nomad City Comparisons</h1>
        <p>Head-to-Head Remote Work & Cost Breakdown Engine</p>
        <p><a href="index.html">← Home</a> | <a href="hub.html">Global Regional Directory</a></p>
    </header>

    <div class="search-container">
        <input type="text" id="searchInput" class="search-input" placeholder="🔍 Search cities (e.g., Tokyo, Berlin, Lisbon)..." onkeyup="filterCards()">
        <p id="counter" style="margin-top: 0.5rem; font-size: 0.9rem; color: #666;">Showing {len(comp_files)} comparison guides</p>
    </div>

    <main class="grid" id="cardsGrid">
        {cards_html}
    </main>

    <footer>
        <p>© Matcha Maya Blog — Digital Nomad Research Index | Updated: {current_date}</p>
    </footer>

    <script>
        function filterCards() {{
            const input = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.querySelectorAll('.card');
            let visibleCount = 0;

            cards.forEach(card => {{
                const title = card.getAttribute('data-title');
                if (title.includes(input)) {{
                    card.style.display = "block";
                    visibleCount++;
                }} else {{
                    card.style.display = "none";
                }}
            }});

            document.getElementById('counter').innerText = `Showing ${{visibleCount}} comparison guides`;
        }}
    </script>

</body>
</html>
"""

with open("compare.html", "w", encoding="utf-8") as f:
    f.write(hub_html)

print(f"✔ Successfully generated 'compare.html' with instant search filtering for {len(comp_files)} comparisons!")