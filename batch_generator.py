
# ====================================================
# 5 INTENT-BASED LSI SUB-TOPIC CLUSTERS GENERATOR
# ====================================================
DEFAULT_PILLAR_DATA = {
    "connectivity": {
        "wifi_speed": "120 Mbps",
        "esim_options": "Airalo / Maya Mobile (Instant Local 5G)",
        "backup_power": "High grid stability; key coworking hubs feature UPS/generator back-ups"
    },
    "cost_of_living": {
        "budget_range": ",200 - ,200 USD / month",
        "avg_rent": " - ,100 USD (1BR City Center)",
        "meal_price": " -  USD (Local to Mid-range meal)"
    },
    "logistics_visas": {
        "visa_status": "Digital Nomad Visa / 30 to 90-day Tourist Visa on Arrival",
        "stay_limit": "90 Days (extendable locally)",
        "tax_threshold": "183-day fiscal residence rule applies"
    },
    "lifestyle_safety": {
        "walkability": "78/100 (Pedestrian-friendly core)",
        "safety_report": "Moderate to High Safety Index; standard urban vigilance advised",
        "healthcare": "International private hospitals & English-speaking clinics available"
    },
    "community_nodes": {
        "neighborhoods": "Downtown Hub & Arts District",
        "coliving": "Selina, Outsite, and local boutique co-living spaces",
        "meetups": "Weekly Nomad Meetups & Tech/Startup Coffee Hours"
    }
}

def generate_intent_pillars_html(city_slug, city_name, custom_data=None):
    # Seed dynamic pseudo-random values using the city name string to keep generation deterministic
    seed_val = sum(ord(c) for c in city_name)
    
    wifi = 80 + (seed_val % 140)  # Speed between 80 - 220 Mbps
    budget_low = 800 + ((seed_val * 3) % 1200) # Budget between  - 
    budget_high = budget_low + 600 + (seed_val % 500)
    rent_low = int(budget_low * 0.45)
    rent_high = int(budget_high * 0.55)
    meal_low = 3 + (seed_val % 7)
    meal_high = meal_low + 6 + (seed_val % 8)
    walkability = 65 + (seed_val % 30)

    dynamic_defaults = {
        "connectivity": {
            "wifi_speed": f"{wifi} Mbps Fiber",
            "esim_options": f"Airalo / Maya Mobile ({city_name} 5G eSIM)",
            "backup_power": "High grid stability; key coworking hubs feature UPS back-ups"
        },
        "cost_of_living": {
            "budget_range": f" -  USD / month",
            "avg_rent": f" -  USD (1BR City Center)",
            "meal_price": f" -  USD (Local to Mid-range meal)"
        },
        "logistics_visas": {
            "visa_status": f"Digital Nomad Visa / Tourist Visa on Arrival ({city_name})",
            "stay_limit": "30 to 90 Days (extendable locally)",
            "tax_threshold": "183-day fiscal residence rule applies"
        },
        "lifestyle_safety": {
            "walkability": f"{walkability}/100 (Pedestrian-friendly core)",
            "safety_report": f"Moderate-to-High Safety Index in {city_name} central districts",
            "healthcare": "International private hospitals & English-speaking clinics available"
        },
        "community_nodes": {
            "neighborhoods": f"Central {city_name} Hub & Arts District",
            "coliving": f"Selina, Outsite, and local boutique co-living spaces in {city_name}",
            "meetups": f"Weekly {city_name} Nomad Meetups & Tech/Startup Coffee Hours"
        }
    }

    if custom_data:
        for k, v in custom_data.items():
            if k in dynamic_defaults and isinstance(v, dict):
                dynamic_defaults[k].update(v)

    data = dynamic_defaults

    html = f"""
    <section class="intent-pillars-cluster container my-5">
      <h2 class="section-title mb-4">Essential Remote Work Infrastructure in {city_name}</h2>
      <div class="row g-4">
        
        <!-- 1. Connectivity -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100 pillar-card shadow-sm border-0 p-3">
            <h3 class="h5 text-primary">?? Connectivity & Tech</h3>
            <ul class="list-unstyled mb-0">
              <li><strong>Avg Fiber Wi-Fi:</strong> {data['connectivity']['wifi_speed']}</li>
              <li><strong>eSIM / SIM:</strong> {data['connectivity']['esim_options']}</li>
              <li><strong>Power Grid:</strong> {data['connectivity']['backup_power']}</li>
            </ul>
          </div>
        </div>

        <!-- 2. Cost of Living -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100 pillar-card shadow-sm border-0 p-3">
            <h3 class="h5 text-primary">?? Cost of Living</h3>
            <ul class="list-unstyled mb-0">
              <li><strong>Nomad Budget:</strong> {data['cost_of_living']['budget_range']}</li>
              <li><strong>1BR Apartment:</strong> {data['cost_of_living']['avg_rent']}</li>
              <li><strong>Average Meal:</strong> {data['cost_of_living']['meal_price']}</li>
            </ul>
          </div>
        </div>

        <!-- 3. Logistics & Visas -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100 pillar-card shadow-sm border-0 p-3">
            <h3 class="h5 text-primary">?? Logistics & Visas</h3>
            <ul class="list-unstyled mb-0">
              <li><strong>Nomad Visa:</strong> {data['logistics_visas']['visa_status']}</li>
              <li><strong>Entry Stay Limit:</strong> {data['logistics_visas']['stay_limit']}</li>
              <li><strong>Tax Residency:</strong> {data['logistics_visas']['tax_threshold']}</li>
            </ul>
          </div>
        </div>

        <!-- 4. Lifestyle & Safety -->
        <div class="col-md-6 col-lg-4">
          <div class="card h-100 pillar-card shadow-sm border-0 p-3">
            <h3 class="h5 text-primary">??? Lifestyle & Safety</h3>
            <ul class="list-unstyled mb-0">
              <li><strong>Walkability:</strong> {data['lifestyle_safety']['walkability']}</li>
              <li><strong>Safety Index:</strong> {data['lifestyle_safety']['safety_report']}</li>
              <li><strong>Healthcare:</strong> {data['lifestyle_safety']['healthcare']}</li>
            </ul>
          </div>
        </div>

        <!-- 5. Community Nodes -->
        <div class="col-md-6 col-lg-8">
          <div class="card h-100 pillar-card shadow-sm border-0 p-3">
            <h3 class="h5 text-primary">?? Community Nodes</h3>
            <ul class="list-unstyled mb-0">
              <li><strong>Top Neighborhoods:</strong> {data['community_nodes']['neighborhoods']}</li>
              <li><strong>Co-Living Hubs:</strong> {data['community_nodes']['coliving']}</li>
              <li><strong>Events:</strong> {data['community_nodes']['meetups']}</li>
            </ul>
          </div>
        </div>

      </div>
    </section>
    """
    return html
def generate_city_schema(city_slug, city_name, wifi_speed, avg_cost, country="Global"):
    import json
    entities = CITY_ENTITIES.get(city_slug, [])
    schema_data = [
        {
            "@context": "https://schema.org",
            "@type": "City",
            "name": city_name,
            "containedInPlace": {"@type": "Country", "name": country},
            "sameAs": entities
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": f"Is {city_name} good for digital nomads?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"{city_name} offers a strong ecosystem for remote workers, featuring average Wi-Fi speeds of {wifi_speed} Mbps and a typical monthly living cost around  USD."
                    }
                },
                {
                    "@type": "Question",
                    "name": f"What is the average internet speed in {city_name}?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"The average internet speed in coworking spaces and nomad-friendly cafes across {city_name} is approximately {wifi_speed} Mbps."
                    }
                },
                {
                    "@type": "Question",
                    "name": f"How much does it cost to live in {city_name} as a remote worker?",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": f"On average, a digital nomad can expect to spend around  USD per month in {city_name}, covering housing, coworking access, and basic living expenses."
                    }
                }
            ]
        }
    ]
    return f'<script type="application/ld+json">\n{json.dumps(schema_data, indent=2)}\n</script>'


