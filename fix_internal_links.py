import os
import glob

print("--- REBUILDING REGIONAL HUBS WITH CITY GUIDES & TOP MENU ---")

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"

# Mapping cities to regional hubs and their spoke guide filenames
regional_mapping = {
    "southeast-asia": {
        "title": "Southeast Asia Digital Nomad Hub",
        "cities": [
            ("Bangkok", "bangkok-podcast-proposal.html"),
            ("Chiang Mai", "chiang-mai-podcast-proposal.html"),
            ("Bali", "bali-podcast-proposal.html")
        ],
        "comparisons": [
            ("Bangkok vs Chiang Mai", "bangkok-vs-chiang-mai-digital-nomad.html"),
            ("Bangkok vs Bali", "bangkok-vs-bali-digital-nomad.html"),
            ("Chiang Mai vs Bali", "chiang-mai-vs-bali-digital-nomad.html")
        ]
    },
    "europe": {
        "title": "Europe Digital Nomad Hub",
        "cities": [
            ("Lisbon", "lisbon-podcast-proposal.html"),
            ("Barcelona", "barcelona-podcast-proposal.html"),
            ("Berlin", "berlin-podcast-proposal.html"),
            ("Tbilisi", "tbilisi-podcast-proposal.html")
        ],
        "comparisons": [
            ("Lisbon vs Barcelona", "lisbon-vs-barcelona-digital-nomad.html"),
            ("Lisbon vs Berlin", "lisbon-vs-berlin-digital-nomad.html"),
            ("Barcelona vs Berlin", "barcelona-vs-berlin-digital-nomad.html")
        ]
    },
    "latin-america": {
        "title": "Latin America Digital Nomad Hub",
        "cities": [
            ("Medellin", "medellin-podcast-proposal.html"),
            ("Mexico City", "mexico-city-podcast-proposal.html")
        ],
        "comparisons": [
            ("Medellin vs Mexico City", "medellin-vs-mexico-city-digital-nomad.html")
        ]
    }
}

os.makedirs("regions", exist_ok=True)

for region_slug, data in regional_mapping.items():
    filename = f"regions/{region_slug}.html"
    
    city_links_html = "".join([
        f'<li><a href="../{file}"><strong>{name}</strong> Digital Nomad & Workation Guide →</a></li>'
        for name, file in data["cities"]
    ])
    
    comp_links_html = "".join([
        f'<li><a href="../{file}"><strong>{name}</strong> Comparison Breakdown →</a></li>'
        for name, file in data["comparisons"]
    ])

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']} | Matcha Maya Blog</title>
    <meta name="description" content="Explore top remote work cities, living costs, wifi speeds, and city comparisons across {data['title']}.">
    <link rel="canonical" href="{domain}/{filename}">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 950px; margin: 0 auto; padding: 20px; }}
        nav.top-menu {{ background: #1b3617; padding: 12px 20px; border-radius: 6px; margin-bottom: 20px; display: flex; gap: 15px; flex-wrap: wrap; align-items: center; }}
        nav.top-menu a {{ color: #ffffff; text-decoration: none; font-weight: 600; font-size: 0.95rem; }}
        nav.top-menu a:hover {{ text-decoration: underline; }}
        .top-menu .brand {{ font-weight: bold; color: #a3e09d; margin-right:auto; }}
        header {{ background: #2d5a27; color: white; padding: 2rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        header h1 {{ margin: 0; font-size: 2.2rem; }}
        .section-box {{ background: #ffffff; border: 1px solid #e0ebe0; border-radius: 8px; padding: 1.8rem; margin-bottom: 2rem; box-shadow: 0 2px 4px rgba(0,0,0,0.04); }}
        .section-box h2 {{ color: #2d5a27; margin-top: 0; font-size: 1.4rem; border-bottom: 2px solid #e0ebe0; padding-bottom: 0.5rem; }}
        ul.link-list {{ list-style: none; padding: 0; margin: 0; }}
        ul.link-list li {{ padding: 10px 0; border-bottom: 1px solid #f0f0f0; }}
        ul.link-list li:last-child {{ border-bottom: none; }}
        ul.link-list a {{ color: #2d5a27; text-decoration: none; font-size: 1.05rem; }}
        ul.link-list a:hover {{ text-decoration: underline; }}
        footer {{ text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #666; }}
    </style>
</head>
<body>

    <nav class="top-menu">
        <span class="brand">🍵 Matcha Maya</span>
        <a href="../index.html">Home</a>
        <a href="../hub.html">Regional Hubs</a>
        <a href="../compare.html">City Comparisons</a>
    </nav>

    <header>
        <h1>{data['title']}</h1>
        <p>Comprehensive Remote Work Hub & Destination Directory</p>
    </header>

    <div class="section-box">
        <h2>🏙️ Primary City Guides & Workation Reports</h2>
        <p>In-depth breakdowns on accommodation, digital nomad visas, coworking spaces, and daily living logistics:</p>
        <ul class="link-list">
            {city_links_html}
        </ul>
    </div>

    <div class="section-box">
        <h2>⚖️ Head-to-Head City Comparisons</h2>
        <p>Direct metric comparisons covering internet speeds, monthly expenses, and community vibes:</p>
        <ul class="link-list">
            {comp_links_html}
        </ul>
    </div>

    <footer>
        <p>© Matcha Maya Blog — Digital Nomad Research Index</p>
    </footer>

</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

print("✔ Regional hubs updated with dual-section navigation (City Pages + Comparisons) and Top Navigation Menu!")