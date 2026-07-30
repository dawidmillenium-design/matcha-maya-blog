code = '''import html

CITY_ENTITIES = {
    # Asia-Pacific
    "bangkok": {"wifi_speed": "120 Mbps", "avg_cost": "$1,400/mo", "country": "Thailand", "region": "Asia", "top_spot": "HUBBA Ekkamai", "matcha_spot": "Peace Oriental Teahouse", "app": "Grab / Bolt", "related": ["chiang-mai", "da-nang", "bali"]},
    "chiang-mai": {"wifi_speed": "95 Mbps", "avg_cost": "$1,100/mo", "country": "Thailand", "region": "Asia", "top_spot": "Punspace Tha Phae", "matcha_spot": "Ristr8to", "app": "Grab / Bolt", "related": ["bangkok", "da-nang", "bali"]},
    "bali": {"wifi_speed": "85 Mbps", "avg_cost": "$1,300/mo", "country": "Indonesia", "region": "Asia", "top_spot": "Dojo Bali", "matcha_spot": "Matcha Cafe Bali", "app": "Gojek / Grab", "related": ["bangkok", "chiang-mai", "da-nang"]},
    "tokyo": {"wifi_speed": "210 Mbps", "avg_cost": "$2,800/mo", "country": "Japan", "region": "Asia", "top_spot": "Biolab Tokyo", "matcha_spot": "Ippodo Tea Marunouchi", "app": "GO App / Suica", "related": ["bangkok", "lisbon", "berlin"]},
    "da-nang": {"wifi_speed": "80 Mbps", "avg_cost": "$900/mo", "country": "Vietnam", "region": "Asia", "top_spot": "Enouvo Space", "matcha_spot": "43 Factory Coffee", "app": "Grab", "related": ["bangkok", "chiang-mai", "bali"]},
    "kuala-lumpur": {"wifi_speed": "110 Mbps", "avg_cost": "$1,250/mo", "country": "Malaysia", "region": "Asia", "top_spot": "Colony Coworking", "matcha_spot": "Matcha Hero Kyoto", "app": "Grab", "related": ["bangkok", "bali", "singapore"]},
    "singapore": {"wifi_speed": "240 Mbps", "avg_cost": "$3,800/mo", "country": "Singapore", "region": "Asia", "top_spot": "The Working Capitol", "matcha_spot": "Hvala Craig Rd", "app": "Grab / MRT", "related": ["kuala-lumpur", "tokyo", "bangkok"]},

    # Europe
    "lisbon": {"wifi_speed": "150 Mbps", "avg_cost": "$2,100/mo", "country": "Portugal", "region": "Europe", "top_spot": "LACS Conde d'Óbidos", "matcha_spot": "Matcha Mama Lisbon", "app": "Bolt / Uber", "related": ["barcelona", "berlin", "tbilisi"]},
    "barcelona": {"wifi_speed": "180 Mbps", "avg_cost": "$2,600/mo", "country": "Spain", "region": "Europe", "top_spot": "Aticco Urquinaona", "matcha_spot": "HanSo Cafe", "app": "Cabify / Uber", "related": ["lisbon", "berlin", "medellin"]},
    "berlin": {"wifi_speed": "130 Mbps", "avg_cost": "$2,400/mo", "country": "Germany", "region": "Europe", "top_spot": "Factory Berlin", "matcha_spot": "The Barn Roastery", "app": "FreeNow / Uber", "related": ["lisbon", "barcelona", "tokyo"]},
    "tbilisi": {"wifi_speed": "90 Mbps", "avg_cost": "$1,200/mo", "country": "Georgia", "region": "Europe", "top_spot": "Impact Hub Tbilisi", "matcha_spot": "Coffee LAB", "app": "Yandex Go / Bolt", "related": ["lisbon", "chiang-mai", "medellin"]},
    "porto": {"wifi_speed": "140 Mbps", "avg_cost": "$1,800/mo", "country": "Portugal", "region": "Europe", "top_spot": "Porto i/o", "matcha_spot": "Epoca Cafe", "app": "Bolt / Uber", "related": ["lisbon", "barcelona", "madrid"]},
    "budapest": {"wifi_speed": "130 Mbps", "avg_cost": "$1,500/mo", "country": "Hungary", "region": "Europe", "top_spot": "KAPTÁR Coworking", "matcha_spot": "Kontakt Coffee", "app": "Bolt", "related": ["prague", "berlin", "tbilisi"]},

    # Americas
    "medellin": {"wifi_speed": "90 Mbps", "avg_cost": "$1,100/mo", "country": "Colombia", "region": "Americas", "top_spot": "Selah Coworking", "matcha_spot": "Teahouse El Poblado", "app": "Uber / InDrive", "related": ["mexico-city", "bali", "tbilisi"]},
    "new-york": {"wifi_speed": "250 Mbps", "avg_cost": "$4,200/mo", "country": "United States", "region": "Americas", "top_spot": "WeWork 450 Lexington", "matcha_spot": "Cha Cha Matcha", "app": "Uber / Lyft / UberEats", "related": ["tokyo", "london", "barcelona"]},
    "mexico-city": {"wifi_speed": "110 Mbps", "avg_cost": "$1,600/mo", "country": "Mexico", "region": "Americas", "top_spot": "Público Condesa", "matcha_spot": "Matcha Kaori", "app": "Uber / DiDi", "related": ["medellin", "barcelona", "lisbon"]},
    "buenos-aires": {"wifi_speed": "85 Mbps", "avg_cost": "$1,000/mo", "country": "Argentina", "region": "Americas", "top_spot": "AreaTres Soho", "matcha_spot": "Lattente", "app": "Cabify / Uber", "related": ["medellin", "mexico-city", "lima"]}
}

def get_city_data(city_slug):
    clean_slug = city_slug.lower().strip().replace("-coworking-guide", "")
    return CITY_ENTITIES.get(clean_slug, {
        "wifi_speed": "100 Mbps",
        "avg_cost": "$1,500/mo",
        "country": "Global Destination",
        "region": "Global",
        "top_spot": "Central Coworking Hub",
        "matcha_spot": "Local Artisanal Cafe",
        "app": "Uber / Local Transit",
        "related": ["bangkok", "lisbon", "medellin"]
    })

def generate_head_tags(city_slug, city_name):
    city_info = get_city_data(city_slug)
    country = city_info.get("country", "Global Destination")
    page_url = f"https://dawidmillenium-design.github.io/matcha-maya-blog/{city_slug}-coworking-guide.html"
    image_url = f"https://dawidmillenium-design.github.io/matcha-maya-blog/assets/covers/{city_slug}.jpg"
    title = f"{city_name} Digital Nomad & Coworking Guide | Matcha Maya"
    description = f"Complete remote work guide to {city_name}, {country}. Includes average WiFi speeds ({city_info.get('wifi_speed')}), living costs ({city_info.get('avg_cost')}), top work cafes, and coworking spaces."
    
    return f"""<!-- DYNAMIC AI SEO & OPEN GRAPH HEAD TAGS -->
    <title>{html.escape(title)}</title>
    <meta name="description" content="{html.escape(description)}">
    <link rel="canonical" href="{page_url}">
    
    <!-- Open Graph / Social Media -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(description)}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:site_name" content="Matcha Maya Blog">
    
    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{html.escape(title)}">
    <meta name="twitter:description" content="{html.escape(description)}">
    <meta name="twitter:image" content="{image_url}">
"""

def generate_intent_pillars_html(city_slug, city_name, custom_data=None):
    city_info = custom_data if custom_data else get_city_data(city_slug)
    related_cities = city_info.get("related", ["bangkok", "lisbon", "medellin"])
    
    related_links_html = "".join([
        f'<a href="{rel}-coworking-guide.html" style="display: inline-block; margin: 0.25rem 0.5rem 0.25rem 0; padding: 0.5rem 1rem; background: #eef5ee; color: #2d5a27; text-decoration: none; border-radius: 4px; font-weight: 500;">👉 {rel.replace("-", " ").title()} Guide</a>'
        for rel in related_cities
    ])
    
    return f"""<!-- INTENT_PILLARS_START -->
<section class="intent-pillars-container" style="margin: 2rem 0; padding: 1.5rem; background-color: #f9fbf9; border-radius: 8px; border: 1px solid #e0ebe0;">
    <h2 style="color: #2d5a27;">Essential Digital Nomad Guide: {html.escape(city_name)}</h2>
    
    <!-- ATOMIC ANSWER BLOCK FOR AI EXTRACTION -->
    <div class="ai-atomic-summary" style="background: #eef5ee; border-left: 4px solid #2d5a27; padding: 1rem; margin-bottom: 1.5rem; border-radius: 4px;">
        <p style="margin: 0; font-weight: 500; color: #1b3617;">
            <strong>Quick Nomad Summary for {html.escape(city_name)}:</strong> {html.escape(city_name)}, {html.escape(city_info.get('country', 'Global'))} offers average internet speeds of {city_info.get('wifi_speed', '100 Mbps')} and an estimated monthly living expense of {city_info.get('avg_cost', '$1,500/mo')}. Primary transportation relies on {city_info.get('app', 'Uber')}, while top laptop-friendly locations include {html.escape(str(city_info.get('top_spot', 'Central Coworking')))} and {html.escape(str(city_info.get('matcha_spot', 'Local Matcha Bar')))}.
        </p>
    </div>

    <!-- AI GEO COMPARISON TABLE -->
    <div class="geo-comparison-table-wrapper" style="margin-bottom: 1.5rem; overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; background: #ffffff; text-align: left; font-size: 0.95rem;">
            <thead>
                <tr style="background-color: #2d5a27; color: #ffffff;">
                    <th style="padding: 10px; border: 1px solid #ddd;">Metric</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Details for {html.escape(city_name)}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Average WiFi Speed</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{city_info.get('wifi_speed', '100 Mbps')}</td>
                </tr>
                <tr style="background-color: #f2f7f2;">
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Estimated Living Cost</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{city_info.get('avg_cost', '$1,500/mo')}</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Top Coworking Space</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{html.escape(str(city_info.get('top_spot', 'Central Coworking')))}</td>
                </tr>
                <tr style="background-color: #f2f7f2;">
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Recommended Cafe / Matcha</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{html.escape(str(city_info.get('matcha_spot', 'Local Cafe')))}</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Primary Transit App</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{city_info.get('app', 'Uber / Local Transit')}</td>
                </tr>
            </tbody>
        </table>
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

    <!-- INTERNAL LINK GRAPH / RELATED CITIES -->
    <div class="related-spokes-section" style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px dashed #c0d8c0;">
        <h4 style="margin: 0 0 0.5rem 0; color: #1b3617;">Explore Related Digital Nomad Destinations:</h4>
        {related_links_html}
    </div>
</section>
<!-- INTENT_PILLARS_END -->"""

def generate_city_schema(city_slug, city_name, wifi_speed=100, avg_cost=1500, country="Global"):
    city_info = get_city_data(city_slug)
    country_name = city_info.get("country", country)
    region_name = city_info.get("region", "Global")
    
    schema_json = f"""<script type="application/ld+json">
[
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
      "@type": "Person",
      "name": "Matcha Maya Editorial Team",
      "jobTitle": "Digital Nomad Destination Specialist",
      "worksFor": {{
        "@type": "Organization",
        "name": "Matcha Maya Blog",
        "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/"
      }}
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "Matcha Maya Blog",
      "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/assets/logo.png"
      }}
    }},
    "speakable": {{
      "@type": "SpeakableSpecification",
      "cssSelector": [".ai-atomic-summary"]
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://dawidmillenium-design.github.io/matcha-maya-blog/{city_slug}-coworking-guide.html"
    }}
  }},
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "What is the average WiFi speed for digital nomads in {html.escape(city_name)}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "The average WiFi speed in {html.escape(city_name)} is approximately {city_info.get('wifi_speed', '100 Mbps')}."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How much does it cost to live in {html.escape(city_name)} as a remote worker?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Estimated monthly living expenses in {html.escape(city_name)} average around {city_info.get('avg_cost', '$1,500/mo')}."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What is the best coworking space in {html.escape(city_name)}?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "A top-rated coworking venue in {html.escape(city_name)} is {html.escape(str(city_info.get('top_spot', 'Central Coworking')))}."
        }}
      }}
    ]
  }},
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://dawidmillenium-design.github.io/matcha-maya-blog/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{html.escape(region_name)} Hub",
        "item": "https://dawidmillenium-design.github.io/matcha-maya-blog/hub.html"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{html.escape(city_name)} Guide",
        "item": "https://dawidmillenium-design.github.io/matcha-maya-blog/{city_slug}-coworking-guide.html"
      }}
    ]
  }}
]
</script>"""
    return schema_json
'''

with open('batch_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully updated batch_generator.py with og:image and twitter:image meta tags!")