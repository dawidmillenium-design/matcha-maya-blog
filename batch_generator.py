import html

CITY_ENTITIES = {
    "bangkok": {"wifi_speed": "120 Mbps", "avg_cost": "$1,400/mo", "country": "Thailand", "top_spot": "HUBBA Ekkamai", "matcha_spot": "Peace Oriental Teahouse"},
    "bali": {"wifi_speed": "85 Mbps", "avg_cost": "$1,300/mo", "country": "Indonesia", "top_spot": "Dojo Bali", "matcha_spot": "Matcha Cafe Bali"}
}

def get_city_data(city_slug):
    return CITY_ENTITIES.get(city_slug.lower(), {
        "wifi_speed": "100 Mbps",
        "avg_cost": "$1,500/mo",
        "country": "Global Destination",
        "top_spot": "Local Hub",
        "matcha_spot": "Organic Matcha Bar"
    })

def generate_intent_pillars_html(city_slug, city_name, custom_data=None):
    city_info = custom_data if custom_data else get_city_data(city_slug)
    return f"""<!-- INTENT_PILLARS_START -->
<section class="intent-pillars-container">
    <h2>Essential Digital Nomad Guide: {html.escape(city_name)}</h2>
    <div>
        <p><strong>Avg Speed:</strong> {city_info.get('wifi_speed', '100 Mbps')}</p>
        <p><strong>Monthly Est:</strong> {city_info.get('avg_cost', '$1,500/mo')}</p>
        <p><strong>Top Spot:</strong> {html.escape(str(city_info.get('top_spot', 'Co-working Center')))}</p>
    </div>
</section>
<!-- INTENT_PILLARS_END -->"""

def generate_city_schema(city_slug, city_name, wifi_speed=100, avg_cost=1500, country="Global"):
    entities = CITY_ENTITIES.get(city_slug.lower(), {})
    country_name = entities.get("country", country)
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Digital Nomad Guide to {html.escape(city_name)}, {html.escape(country_name)}"
}}
</script>"""
