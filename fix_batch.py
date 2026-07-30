code = '''import html

CITY_ENTITIES = {
    # Asia-Pacific
    "bangkok": {"wifi_speed": "120 Mbps", "avg_cost": "$1,400/mo", "country": "Thailand", "top_spot": "HUBBA Ekkamai", "matcha_spot": "Peace Oriental Teahouse", "app": "Grab / Bolt"},
    "chiang-mai": {"wifi_speed": "95 Mbps", "avg_cost": "$1,100/mo", "country": "Thailand", "top_spot": "Punspace Tha Phae", "matcha_spot": "Ristr8to", "app": "Grab / Bolt"},
    "bali": {"wifi_speed": "85 Mbps", "avg_cost": "$1,300/mo", "country": "Indonesia", "top_spot": "Dojo Bali", "matcha_spot": "Matcha Cafe Bali", "app": "Gojek / Grab"},
    "tokyo": {"wifi_speed": "210 Mbps", "avg_cost": "$2,800/mo", "country": "Japan", "top_spot": "Biolab Tokyo", "matcha_spot": "Ippodo Tea Marunouchi", "app": "GO App / Suica"},
    "da-nang": {"wifi_speed": "80 Mbps", "avg_cost": "$900/mo", "country": "Vietnam", "top_spot": "Enouvo Space", "matcha_spot": "43 Factory Coffee", "app": "Grab"},

    # Europe
    "lisbon": {"wifi_speed": "150 Mbps", "avg_cost": "$2,100/mo", "country": "Portugal", "top_spot": "LACS Conde d'Óbidos", "matcha_spot": "Matcha Mama Lisbon", "app": "Bolt / Uber"},
    "barcelona": {"wifi_speed": "180 Mbps", "avg_cost": "$2,600/mo", "country": "Spain", "top_spot": "Aticco Urquinaona", "matcha_spot": "HanSo Cafe", "app": "Cabify / Uber"},
    "berlin": {"wifi_speed": "130 Mbps", "avg_cost": "$2,400/mo", "country": "Germany", "top_spot": "Factory Berlin", "matcha_spot": "The Barn Roastery", "app": "FreeNow / Uber"},
    "tbilisi": {"wifi_speed": "90 Mbps", "avg_cost": "$1,200/mo", "country": "Georgia", "top_spot": "Impact Hub Tbilisi", "matcha_spot": "Coffee LAB", "app": "Yandex Go / Bolt"},

    # Americas
    "medellin": {"wifi_speed": "90 Mbps", "avg_cost": "$1,100/mo", "country": "Colombia", "top_spot": "Selah Coworking", "matcha_spot": "Teahouse El Poblado", "app": "Uber / InDrive"},
    "new-york": {"wifi_speed": "250 Mbps", "avg_cost": "$4,200/mo", "country": "United States", "top_spot": "WeWork 450 Lexington", "matcha_spot": "Cha Cha Matcha", "app": "Uber / Lyft / UberEats"},
    "mexico-city": {"wifi_speed": "110 Mbps", "avg_cost": "$1,600/mo", "country": "Mexico", "top_spot": "Público Condesa", "matcha_spot": "Matcha Kaori", "app": "Uber / DiDi"}
}

def get_city_data(city_slug):
    clean_slug = city_slug.lower().strip().replace("-coworking-guide", "")
    return CITY_ENTITIES.get(clean_slug, {
        "wifi_speed": "100 Mbps",
        "avg_cost": "$1,500/mo",
        "country": "Global Destination",
        "top_spot": "Central Coworking Hub",
        "matcha_spot": "Local Artisanal Cafe",
        "app": "Uber / Local Transit"
    })

def generate_intent_pillars_html(city_slug, city_name, custom_data=None):
    city_info = custom_data if custom_data else get_city_data(city_slug)
    
    return f"""<!-- INTENT_PILLARS_START -->
<section class="intent-pillars-container" style="margin: 2rem 0; padding: 1.5rem; background-color: #f9fbf9; border-radius: 8px; border: 1px solid #e0ebe0;">
    <h2 style="color: #2d5a27;">Essential Digital Nomad Guide: {html.escape(city_name)}</h2>
    
    <!-- ATOMIC ANSWER BLOCK FOR AI EXTRACTION -->
    <div class="ai-atomic-summary" style="background: #eef5ee; border-left: 4px solid #2d5a27; padding: 1rem; margin-bottom: 1.5rem; border-radius: 4px;">
        <p style="margin: 0; font-weight: 500; color: #1b3617;">
            <strong>Quick Nomad Summary for {html.escape(city_name)}:</strong> {html.escape(city_name)}, {html.escape(city_info.get('country', 'Global'))} offers average internet speeds of {city_info.get('wifi_speed', '100 Mbps')} and an estimated monthly living expense of {city_info.get('avg_cost', '$1,500/mo')}. Primary transportation relies on {city_info.get('app', 'Uber')}, while top laptop-friendly locations include {html.escape(str(city_info.get('top_spot', 'Central Coworking')))} and {html.escape(str(city_info.get('matcha_spot', 'Local Matcha Bar')))}.
        </p>
    </div>

    <div class="pillars-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; margin-top: 1rem;">
        
        <div class="pillar-card" style="background: #fff; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h3 style="font-size: 1.1rem; color: #1b3617;">📶 1. Connectivity & Infrastructure</h3>
            <p><strong>Avg Speed:</strong> {city_info.get('wifi_speed', '100 Mbps')}</p>
            <p>High-speed fiber connectivity with accessible remote working spaces throughout the central districts.</p>
        </div>

        <div class="pillar-card" style="background: #fff; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h3 style="font-size: 1.1rem; color: #1b3617;">💰 2. Cost of Living & Expenses</h3>
            <p><strong>Monthly Est:</strong> {city_info.get('avg_cost', '$1,500/mo')}</p>
            <p>Estimated budgets covering mid-range accommodation, workspace day-passes, and daily living costs.</p>
        </div>

        <div class="pillar-card" style="background: #fff; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h3 style="font-size: 1.1rem; color: #1b3617;">🛂 3. Visas & Mobility</h3>
            <p><strong>Mobility & Apps:</strong> {city_info.get('app', 'Uber / Public Transit')}</p>
            <p>Flexible entry options and established ride-hailing app networks for smooth navigation across town.</p>
        </div>

        <div class="pillar-card" style="background: #fff; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h3 style="font-size: 1.1rem; color: #1b3617;">🛡️ 4. Work-Life Balance</h3>
            <p><strong>Recommended Cafe:</strong> {html.escape(str(city_info.get('matcha_spot', 'Local Cafe')))}</p>
            <p>Great coffee & tea culture with quiet spots suitable for long focus sessions and calls.</p>
        </div>

        <div class="pillar-card" style="background: #fff; padding: 1rem; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
            <h3 style="font-size: 1.1rem; color: #1b3617;">🤝 5. Community Hubs</h3>
            <p><strong>Top Coworking:</strong> {html.escape(str(city_info.get('top_spot', 'Co-working Hub')))}</p>
            <p>Active expat communities, regular tech meetups, and dedicated collaborative workspaces.</p>
        </div>

    </div>
</section>
<!-- INTENT_PILLARS_END -->"""

def generate_city_schema(city_slug, city_name, wifi_speed=100, avg_cost=1500, country="Global"):
    city_info = get_city_data(city_slug)
    country_name = city_info.get("country", country)
    
    schema_json = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ItemPage",
  "headline": "Digital Nomad & Coworking Guide to {html.escape(city_name)}, {html.escape(country_name)}",
  "description": "Comprehensive guide covering connectivity, WiFi speeds, living costs, and top work cafes in {html.escape(city_name)}.",
  "about": {{
    "@type": "City",
    "name": "{html.escape(city_name)}",
    "containedInPlace": {{
      "@type": "Country",
      "name": "{html.escape(country_name)}"
    }}
  }},
  "author": {{
    "@type": "Organization",
    "name": "Matcha Maya Blog"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "Matcha Maya Blog"
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://dawidmillenium-design.github.io/matcha-maya-blog/{city_slug}-coworking-guide.html"
  }}
}}
</script>"""
    return schema_json
'''

with open('batch_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated batch_generator.py with Atomic Answers & City Place Schema!")