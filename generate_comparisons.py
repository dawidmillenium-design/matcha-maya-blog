import os
import html
import itertools
from batch_generator import CITY_ENTITIES

print("--- STARTING COMPARISON PAGE GENERATOR ---")

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"

featured_cities = [
    "bangkok", "lisbon", "medellin", "bali", "chiang-mai", 
    "mexico-city", "tokyo", "barcelona", "berlin", "tbilisi"
]

city_pairs = list(itertools.combinations(featured_cities, 2))
generated_count = 0

for city_a_slug, city_b_slug in city_pairs:
    data_a = CITY_ENTITIES.get(city_a_slug)
    data_b = CITY_ENTITIES.get(city_b_slug)
    
    if not data_a or not data_b:
        continue

    name_a = city_a_slug.replace("-", " ").title()
    name_b = city_b_slug.replace("-", " ").title()
    
    comp_slug = f"{city_a_slug}-vs-{city_b_slug}-digital-nomad"
    filename = f"{comp_slug}.html"
    page_url = f"{domain}/{filename}"
    title = f"{name_a} vs {name_b}: Digital Nomad Comparison Guide | Matcha Maya"
    description = f"Detailed remote work comparison: {name_a} vs {name_b}. Compare internet speeds ({data_a['wifi_speed']} vs {data_b['wifi_speed']}), monthly costs ({data_a['avg_cost']} vs {data_b['avg_cost']}), coworking spaces, and lifestyle."

    schema_json = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ItemPage",
  "headline": "{html.escape(title)}",
  "description": "{html.escape(description)}",
  "author": {{
    "@type": "Organization",
    "name": "Matcha Maya Blog",
    "url": "{domain}/"
  }},
  "mainEntity": {{
    "@type": "ItemList",
    "name": "{name_a} vs {name_b} Digital Nomad Comparison",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{name_a}",
        "url": "{domain}/{city_a_slug}-coworking-guide.html"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{name_b}",
        "url": "{domain}/{city_b_slug}-coworking-guide.html"
      }}
    ]
  }}
}}
</script>"""

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(title)}</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="canonical" href="{page_url}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:site_name" content="Matcha Maya Blog">
    
    {schema_json}
    
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; }}
        header {{ background: #2d5a27; color: white; padding: 2rem; border-radius: 8px; margin-bottom: 2rem; text-align: center; }}
        header h1 {{ margin: 0; font-size: 2rem; }}
        header a {{ color: #eef5ee; text-decoration: underline; }}
        .summary-box {{ background: #eef5ee; border-left: 4px solid #2d5a27; padding: 1.2rem; border-radius: 4px; margin-bottom: 2rem; }}
        table {{ width: 100%; border-collapse: collapse; margin: 2rem 0; font-size: 1rem; }}
        th, td {{ padding: 12px 15px; border: 1px solid #ddd; text-align: left; }}
        th {{ background-color: #2d5a27; color: white; }}
        tr:nth-child(even) {{ background-color: #f9fbf9; }}
        .btn {{ display: inline-block; padding: 0.6rem 1.2rem; background: #2d5a27; color: white; text-decoration: none; border-radius: 4px; font-weight: 500; margin-top: 0.5rem; }}
        .btn:hover {{ background: #1b3617; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0; }}
        .card {{ background: #ffffff; border: 1px solid #e0ebe0; border-radius: 8px; padding: 1.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
        footer {{ text-align: center; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid #ddd; color: #666; }}
    </style>
</head>
<body>

    <header>
        <h1>{name_a} vs {name_b}</h1>
        <p>Head-to-Head Digital Nomad & Remote Work Comparison</p>
        <p><a href="{domain}/index.html">← Home</a> | <a href="{domain}/hub.html">Global Hub Directory</a> | <a href="{domain}/compare.html">City Comparisons</a></p>
    </header>

    <div class="summary-box">
        <strong>🤖 AI Executive Summary:</strong> Choosing between <strong>{name_a}</strong> ({data_a['country']}) and <strong>{name_b}</strong> ({data_b['country']}) depends on budget and speed priorities. {name_a} offers average WiFi speeds of <strong>{data_a['wifi_speed']}</strong> with estimated living expenses around <strong>{data_a['avg_cost']}</strong>. In comparison, {name_b} provides <strong>{data_b['wifi_speed']}</strong> internet for roughly <strong>{data_b['avg_cost']}</strong> per month.
    </div>

    <h2>Head-to-Head Metric Comparison</h2>
    <table>
        <thead>
            <tr>
                <th>Data Point / Metric</th>
                <th>{name_a}</th>
                <th>{name_b}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Country & Region</strong></td>
                <td>{data_a['country']} ({data_a['region']})</td>
                <td>{data_b['country']} ({data_b['region']})</td>
            </tr>
            <tr>
                <td><strong>Average WiFi Speed</strong></td>
                <td>{data_a['wifi_speed']}</td>
                <td>{data_b['wifi_speed']}</td>
            </tr>
            <tr>
                <td><strong>Estimated Living Cost</strong></td>
                <td>{data_a['avg_cost']}</td>
                <td>{data_b['avg_cost']}</td>
            </tr>
            <tr>
                <td><strong>Recommended Coworking Spot</strong></td>
                <td>{data_a['top_spot']}</td>
                <td>{data_b['top_spot']}</td>
            </tr>
            <tr>
                <td><strong>Specialty Cafe / Matcha</strong></td>
                <td>{data_a['matcha_spot']}</td>
                <td>{data_b['matcha_spot']}</td>
            </tr>
            <tr>
                <td><strong>Primary Transit / Mobility App</strong></td>
                <td>{data_a['app']}</td>
                <td>{data_b['app']}</td>
            </tr>
        </tbody>
    </table>

    <div class="grid">
        <div class="card">
            <h3>Explore {name_a}</h3>
            <p>Get full insights, neighborhood breakdowns, visa specifics, and community hubs in {name_a}.</p>
            <a href="{domain}/{city_a_slug}-coworking-guide.html" class="btn">Read Full {name_a} Guide →</a>
        </div>
        <div class="card">
            <h3>Explore {name_b}</h3>
            <p>Get full insights, neighborhood breakdowns, visa specifics, and community hubs in {name_b}.</p>
            <a href="{domain}/{city_b_slug}-coworking-guide.html" class="btn">Read Full {name_b} Guide →</a>
        </div>
    </div>

    <footer>
        <p>© Matcha Maya Blog — Digital Nomad Research Index</p>
    </footer>

</body>
</html>
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    generated_count += 1

print(f"✔ Successfully re-generated {generated_count} comparison pages with absolute URLs!")