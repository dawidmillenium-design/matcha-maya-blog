import os
import glob

print("--- STARTING INTERNAL LINK REPAIR ---")

# 1. Create 'regions' directory
os.makedirs("regions", exist_ok=True)

# 2. Define Regional Hub Data
regions_data = {
    "middle-east": "Middle East",
    "africa": "Africa",
    "central-asia": "Central Asia",
    "western-europe": "Western Europe",
    "south-america": "South America",
    "north-america": "North America",
    "southeast-asia": "Southeast Asia",
    "east-asia": "East Asia",
    "uk-eastern-europe": "UK & Eastern Europe",
    "south-asia": "South Asia"
}

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"

# 3. Generate individual Regional Hub HTML pages inside 'regions/'
for reg_slug, reg_name in regions_data.items():
    hub_filename = os.path.join("regions", f"{reg_slug}.html")
    
    hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{reg_name} Digital Nomad Hub | Matcha Maya Blog</title>
    <meta name="description" content="Digital nomad guides, coworking reviews, cost of living metrics, and WiFi speeds for cities across {reg_name}.">
    <link rel="canonical" href="{domain}/regions/{reg_slug}.html">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; }}
        header {{ background: #2d5a27; color: white; padding: 2rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        header a {{ color: #eef5ee; text-decoration: underline; }}
        .card {{ background: #ffffff; border: 1px solid #e0ebe0; border-radius: 6px; padding: 1rem; margin-bottom: 1rem; }}
        footer {{ text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #666; }}
    </style>
</head>
<body>
    <header>
        <h1>🌍 {reg_name} Nomad Directory</h1>
        <p>Regional Remote Work Hub & City Guides</p>
        <p><a href="../index.html">← Home</a> | <a href="../hub.html">All Regional Hubs</a> | <a href="../compare.html">City Comparisons</a></p>
    </header>
    <main>
        <h2>Explore Destinations in {reg_name}</h2>
        <div class="card">
            <p>Select a specific city spoke guide from the main index or comparison engine to view WiFi metrics, coworking options, and monthly living estimates.</p>
            <a href="../compare.html" style="color: #2d5a27; font-weight: bold;">Browse City Comparisons →</a>
        </div>
    </main>
    <footer>
        <p>© Matcha Maya Blog — Digital Nomad Research Index</p>
    </footer>
</body>
</html>
"""
    with open(hub_filename, "w", encoding="utf-8") as f:
        f.write(hub_html)

print(f"✔ Generated {len(regions_data)} regional hub files in 'regions/' folder")

# 4. Generate Root 'hub.html' Directory Page
hub_links_html = ""
for reg_slug, reg_name in regions_data.items():
    hub_links_html += f"""
    <div style="background: #ffffff; border: 1px solid #e0ebe0; padding: 1.2rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
        <h3 style="margin: 0 0 0.5rem 0; color: #2d5a27;">📍 {reg_name}</h3>
        <p style="margin: 0 0 0.8rem 0; font-size: 0.9rem; color: #555;">Browse nomad destinations and coworking hubs in {reg_name}.</p>
        <a href="regions/{reg_slug}.html" style="color: #2d5a27; font-weight: bold; text-decoration: none;">View {reg_name} Guides →</a>
    </div>
    """

root_hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Digital Nomad Hub Directory | Matcha Maya Blog</title>
    <meta name="description" content="Global index of regional digital nomad hubs covering Asia, Europe, Americas, Africa, and Middle East.">
    <link rel="canonical" href="{domain}/hub.html">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 1000px; margin: 0 auto; padding: 20px; }}
        header {{ background: #2d5a27; color: white; padding: 2rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        header a {{ color: #eef5ee; text-decoration: underline; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.2rem; margin: 2rem 0; }}
        footer {{ text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #666; }}
    </style>
</head>
<body>
    <header>
        <h1>🌐 Global Regional Hub Directory</h1>
        <p>Choose a Region to Discover Remote Work Destination Guides</p>
        <p><a href="index.html">← Home</a> | <a href="compare.html">City Comparisons Index</a></p>
    </header>
    <main>
        <div class="grid">
            {hub_links_html}
        </div>
    </main>
    <footer>
        <p>© Matcha Maya Blog — Digital Nomad Research Index</p>
    </footer>
</body>
</html>
"""

with open("hub.html", "w", encoding="utf-8") as f:
    f.write(root_hub_html)

print("✔ Generated root 'hub.html' directory")