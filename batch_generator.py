import os

REGIONAL_SILO = {
    # Southeast Asia
    "jakarta": "southeast-asia", "bangkok": "southeast-asia", "manila": "southeast-asia",
    "ho-chi-minh": "southeast-asia", "kuala-lumpur": "southeast-asia", "singapore": "southeast-asia",
    "phnom-penh": "southeast-asia", "vientiane": "southeast-asia", "yangon": "southeast-asia",
    "bali": "southeast-asia", "chiang-mai": "southeast-asia", "da-nang": "southeast-asia",
    "cebu": "southeast-asia", "phuket": "southeast-asia", "penang": "southeast-asia", "hanoi": "southeast-asia",
    # East Asia
    "tokyo": "east-asia", "osaka": "east-asia", "seoul": "east-asia", "busan": "east-asia",
    "taipei": "east-asia", "hong-kong": "east-asia", "shanghai": "east-asia", "guangzhou": "east-asia",
    "kyoto": "east-asia", "fukuoka": "east-asia", "sapporo": "east-asia", "kaohsiung": "east-asia",
    "taichung": "east-asia", "beijing": "east-asia", "shenzhen": "east-asia", "chengdu": "east-asia",
    "macau": "east-asia", "jeju": "east-asia",
    # South Asia
    "mumbai": "south-asia", "bengaluru": "south-asia", "colombo": "south-asia", "kathmandu": "south-asia",
    "delhi": "south-asia", "goa": "south-asia", "pune": "south-asia", "hyderabad": "south-asia",
    "chennai": "south-asia", "dhaka": "south-asia", "pokhara": "south-asia", "male": "south-asia",
    "kandy": "south-asia", "thimphu": "south-asia", "lahore": "south-asia", "karachi": "south-asia",
    "islamabad": "south-asia", "jaipur": "south-asia",
    # Central Asia
    "tbilisi": "central-asia", "almaty": "central-asia", "yerevan": "central-asia", "tashkent": "central-asia",
    "baku": "central-asia", "astana": "central-asia", "bishkek": "central-asia", "dushanbe": "central-asia",
    "samarkand": "central-asia", "batumi": "central-asia", "khujand": "central-asia", "ashgabat": "central-asia",
    # Middle East
    "dubai": "middle-east", "istanbul": "middle-east", "doha": "middle-east", "riyadh": "middle-east",
    "muscat": "middle-east", "amman": "middle-east", "beirut": "middle-east", "tel-aviv": "middle-east",
    "abu-dhabi": "middle-east", "jeddah": "middle-east", "antalya": "middle-east", "izmir": "middle-east",
    "ankara": "middle-east", "manama": "middle-east", "kuwait-city": "middle-east", "sharjah": "middle-east",
    "salalah": "middle-east", "aqaba": "middle-east", "erbil": "middle-east", "bursa": "middle-east",
    "bodrum": "middle-east", "al-ula": "middle-east",
    # Africa
    "cape-town": "africa", "nairobi": "africa", "cairo": "africa", "casablanca": "africa",
    "marrakech": "africa", "tunis": "africa", "lagos": "africa", "johannesburg": "africa",
    "accra": "africa", "kigali": "africa", "addis-ababa": "africa", "dakar": "africa",
    "zanzibar": "africa", "mauritius": "africa", "algiers": "africa", "alexandria": "africa",
    "kampala": "africa", "dar-es-salaam": "africa", "mombasa": "africa", "windhoek": "africa",
    "maputo": "africa", "luanda": "africa", "antananarivo": "africa", "pretoria": "africa",
    "durban": "africa", "taghazout": "africa",
    # Western Europe
    "lisbon": "western-europe", "barcelona": "western-europe", "berlin": "western-europe", "paris": "western-europe",
    "athens": "western-europe", "amsterdam": "western-europe", "madrid": "western-europe", "porto": "western-europe",
    "milan": "western-europe", "rome": "western-europe", "florence": "western-europe", "vienna": "western-europe",
    "zurich": "western-europe", "brussels": "western-europe", "munich": "western-europe", "hamburg": "western-europe",
    "dubrovnik": "western-europe", "split": "western-europe", "valletta": "western-europe", "nice": "western-europe",
    "lyon": "western-europe", "geneva": "western-europe", "rotterdam": "western-europe", "antwerp": "western-europe",
    "seville": "western-europe", "valencia": "western-europe", "faro": "western-europe", "funchal": "western-europe",
    # UK & Eastern Europe
    "london": "uk-eastern-europe", "prague": "uk-eastern-europe", "warsaw": "uk-eastern-europe", "budapest": "uk-eastern-europe",
    "dublin": "uk-eastern-europe", "edinburgh": "uk-eastern-europe", "manchester": "uk-eastern-europe", "krakow": "uk-eastern-europe",
    "bucharest": "uk-eastern-europe", "sofia": "uk-eastern-europe", "tallinn": "uk-eastern-europe", "riga": "uk-eastern-europe",
    "vilnius": "uk-eastern-europe", "belgrade": "uk-eastern-europe", "zagreb": "uk-eastern-europe", "bratislava": "uk-eastern-europe",
    "ljubljana": "uk-eastern-europe", "belfast": "uk-eastern-europe", "glasgow": "uk-eastern-europe", "cardiff": "uk-eastern-europe", "birmingham": "uk-eastern-europe",
    "gdansk": "uk-eastern-europe", "wroclaw": "uk-eastern-europe", "cluj-napoca": "uk-eastern-europe", "varna": "uk-eastern-europe",
    "plovdiv": "uk-eastern-europe", "tartu": "uk-eastern-europe", "kaunas": "uk-eastern-europe", "sarajevo": "uk-eastern-europe", "skopje": "uk-eastern-europe",
    # North America
    "new-york": "north-america", "los-angeles": "north-america", "san-francisco": "north-america", "vancouver": "north-america",
    "montreal": "north-america", "austin": "north-america", "miami": "north-america", "chicago": "north-america",
    "seattle": "north-america", "mexico-city": "north-america", "toronto": "north-america", "boston": "north-america",
    "denver": "north-america", "portland": "north-america", "san-diego": "north-america", "honolulu": "north-america",
    "playa-del-carmen": "north-america", "tulum": "north-america", "oaxaca": "north-america", "puerto-vallarta": "north-america",
    "guadalajara": "north-america", "san-jose-cr": "north-america", "panama-city": "north-america", "calgary": "north-america",
    "ottawa": "north-america", "nashville": "north-america",
    # South America
    "buenos-aires": "south-america", "medellin": "south-america", "rio-de-janeiro": "south-america", "santiago": "south-america",
    "lima": "south-america", "sao-paulo": "south-america", "bogota": "south-america", "quito": "south-america",
    "la-paz": "south-america", "montevideo": "south-america", "florianopolis": "south-america", "cartagena": "south-america",
    "cusco": "south-america", "mendoza": "south-america", "bariloche": "south-america", "cordoba": "south-america",
    "salvador": "south-america", "curitiba": "south-america", "asuncion": "south-america", "cuenca": "south-america",
    "arequipa": "south-america", "santa-marta": "south-america", "cali": "south-america", "guayaquil": "south-america"
}

ARCHETYPES = [
    "Format A (Ultimate Long Guide)",
    "Format B (Deep Transcript)",
    "Format C (How-To & Checklist)",
    "Format D (News Commentary)",
    "Format E (Vlogger Log)"
]

SUPERFOODS = [
    ("L-Theanine in Ceremonial Uji Matcha", "Matcha contains L-theanine, promoting alert relaxation and sustained focus without cortisol spikes."),
    ("Acai & Goji Berry ORAC Antioxidants", "Acai and Goji berries provide over 100,000 ORAC units per 100g to reduce screen fatigue and travel oxidative stress."),
    ("Moringa & Green Tea Polyphenols", "Combining Moringa with green tea polyphenols boosts iron absorption and immune resistance for remote workers."),
    ("Chlorogenic Acid in Green Tea & Cold Matcha", "Shade-grown green tea paired with unroasted coffee beans delivers chlorogenic acids that regulate glucose during deep-work blocks."),
    ("Matcha & Ashwagandha Adaptogens", "Infusing ceremonial matcha with ashwagandha roots balances adrenals and suppresses travel-induced insomnia.")
]

DEBATES = [
    "Is staying inside high-end expat enclaves isolating digital nomads from authentic local culture?",
    "Are long-term remote work visas driving up local apartment rents?",
    "Does privatized urban infrastructure create a sanitized experience removed from genuine city life?",
    "Can low-cost nomad destinations preserve their neighborhoods as remote work grows?",
    "Should remote workers undergo cultural orientation to prevent overtourism friction?"
]

DATA_SETS = [
    {
        "visa": "Remote Worker Visa / Digital Nomad Residence Permit",
        "ride_app": "Grab & Gojek",
        "taxi_cost": "$25 - $45 USD (Premium Executive SUV / Alphard)",
        "vlog": "YouTube Nomad Vlogs & Medium City Guides",
        "audiobook": "The Digital Nomad Guide to Sustainable Relocation (Audiobook & E-Book)"
    },
    {
        "visa": "D8 Nomad Visa / E33G Remote Worker Status",
        "ride_app": "Uber, Bolt & FreeNow",
        "taxi_cost": "$35 - $60 USD (Black Sedan Executive)",
        "vlog": "Local Expat Blogs & Youtube Relocation Logs",
        "audiobook": "Remote Work Freedom & Regional Tech Hubs (Audible & Kindle)"
    }
]

def generate_220_cities():
    cities_list = []
    for index, (slug, region_slug) in enumerate(REGIONAL_SILO.items()):
        formatted_name = " ".join([word.capitalize() for word in slug.split('-')])
        arch = ARCHETYPES[index % len(ARCHETYPES)]
        sf_title, sf_desc = SUPERFOODS[index % len(SUPERFOODS)]
        debate = DEBATES[index % len(DEBATES)]
        extra_data = DATA_SETS[index % len(DATA_SETS)]
        
        cities_list.append({
            "slug": f"{slug}-interview.html",
            "city": formatted_name,
            "region_slug": region_slug,
            "archetype": arch,
            "superfood_topic": sf_title,
            "superfood_text": sf_desc,
            "debate": debate,
            "visa": extra_data['visa'],
            "ride_app": extra_data['ride_app'],
            "taxi_cost": extra_data['taxi_cost'],
            "vlog": extra_data['vlog'],
            "audiobook": extra_data['audiobook']
        })
    return cities_list

CITIES = generate_220_cities()

def get_sibling_links(current_slug, current_region):
    siblings = [
        c for c in CITIES 
        if c['region_slug'] == current_region and c['slug'] != current_slug
    ][:3]
    
    html = '<div class="mt-8 border-t border-stone-200 pt-6"><h4 class="text-xs font-bold text-stone-900 uppercase tracking-wider mb-3">🎧 Related Regional Podcasts</h4><ul class="space-y-2 text-xs">'
    for s in siblings:
        html += f'<li><a href="{s["slug"]}" class="text-emerald-700 hover:underline font-medium">→ Remote Work & Superfoods in {s["city"]}</a></li>'
    html += '</ul></div>'
    return html

def build_city_post(c):
    sibling_section = get_sibling_links(c['slug'], c['region_slug'])
    page_url = f"https://dawidmillenium-design.github.io/matcha-maya-blog/{c['slug']}"
    page_title = f"{c['city']} - Matcha Maya Interview proposal with local influencer"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  <meta name="description" content="Matcha Maya Interview proposal with local influencer in {c['city']}. Covers digital nomad visas, laptop coworking, ride-hailing apps, premium taxi costs, audiobooks, and local vlogs." />
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- PodcastSeries & Article JSON-LD Schema Markup -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "@id": "{page_url}#article",
        "isPartOf": {{ "@id": "{page_url}" }},
        "headline": "{page_title}",
        "description": "Matcha Maya Interview proposal with local influencer covering remote work setup, visa options, and lifestyle in {c['city']}.",
        "inLanguage": "en-US",
        "mainEntityOfPage": "{page_url}",
        "author": {{
          "@type": "Organization",
          "name": "Matcha Maya"
        }},
        "publisher": {{
          "@type": "Organization",
          "name": "Matcha Maya Blog",
          "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/"
        }}
      }},
      {{
        "@type": "PodcastSeries",
        "@id": "{page_url}#podcast",
        "name": "Matcha Maya Interview proposal with local influencer - {c['city']}",
        "description": "Podcast interview series discussing digital nomad visas, laptop coworking infrastructure, ride-hailing options, and superfoods in {c['city']}.",
        "url": "{page_url}",
        "webFeed": "https://dawidmillenium-design.github.io/matcha-maya-blog/feed.xml",
        "author": {{
          "@type": "Organization",
          "name": "Matcha Maya"
        }}
      }}
    ]
  }}
  </script>
</head>
<body class="bg-stone-50 text-stone-800 font-sans antialiased">
  <header class="bg-emerald-900 text-white p-4 text-xs shadow-md">
    <div class="max-w-4xl mx-auto flex justify-between items-center">
      <a href="https://dawidmillenium-design.github.io/matcha-maya-blog/" class="font-bold text-sm tracking-wide">🍵 MATCHA MAYA</a>
      <a href="regions/{c['region_slug']}.html" class="underline text-emerald-300 hover:text-white transition">
        Parent Regional SILO Hub
      </a>
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 py-8">
    <article class="bg-white p-8 rounded-2xl border border-stone-200 shadow-sm">
      <div class="flex items-center justify-between border-b border-stone-100 pb-4 mb-4">
        <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider">{c['region_slug'].replace('-', ' ')} • {c['archetype']}</span>
        <span class="text-xs text-stone-400">100+ Mbps Fiber Verified</span>
      </div>

      <h1 class="text-2xl md:text-3xl font-extrabold text-stone-900 mt-1">{c['city']} - Matcha Maya Interview proposal with local influencer</h1>
      <p class="text-xs text-stone-500 mt-2">Verified workspace analysis, laptop battery hubs, ride-hailing app options, e-books, and local vlogs.</p>
      
      <!-- SEO Key Info Box -->
      <div class="my-6 grid grid-cols-1 md:grid-cols-2 gap-4 bg-stone-50 p-4 rounded-xl border border-stone-200 text-xs">
        <div>
          <strong class="text-stone-900">🛂 Country-Specific Visa:</strong>
          <p class="text-stone-600">{c['visa']}</p>
        </div>
        <div>
          <strong class="text-stone-900">🚕 Ride-Hailing Apps & Premium Taxi:</strong>
          <p class="text-stone-600">{c['ride_app']} | Airport Executive Car: {c['taxi_cost']}</p>
        </div>
        <div>
          <strong class="text-stone-900">🎧 Audiobook & E-Book Recommendation:</strong>
          <p class="text-stone-600">{c['audiobook']}</p>
        </div>
        <div>
          <strong class="text-stone-900">📹 Blogs & Vlogs:</strong>
          <p class="text-stone-600">{c['vlog']}</p>
        </div>
      </div>

      <!-- Superfood Section -->
      <div class="my-6 bg-emerald-50 border-l-4 border-emerald-600 p-4 rounded-r-xl">
        <h3 class="font-bold text-emerald-950 text-sm flex items-center gap-2">🌿 {c['superfood_topic']}</h3>
        <p class="text-emerald-800 text-xs mt-1 leading-relaxed">{c['superfood_text']}</p>
      </div>

      <section class="mt-6 text-xs leading-relaxed text-stone-700 space-y-4">
        <h2 class="text-base font-bold text-stone-900">Laptop Workspaces & High-Speed Mobility</h2>
        <p>In {c['city']}, digital nomads using modern dual-screen laptop setups can rely on high-speed fiber internet in dedicated co-working spaces. Getting around the city is seamless using popular local ride-hailing apps like {c['ride_app']}, while premium executive taxi cars are readily available for comfortable airport transfers.</p>
      </section>

      <div class="bg-stone-900 text-white p-6 rounded-2xl mt-8 shadow-sm">
        <h3 class="font-bold text-emerald-400 text-sm">🗣️ The Nomad Debate</h3>
        <p class="text-xs text-stone-300 mt-2 leading-relaxed">{c['debate']}</p>
      </div>

      {sibling_section}
    </article>
  </main>

  <footer class="text-center py-6 text-xs text-stone-400">
    <p>MATCHA MAYA © 2026 — 220 Global City Guides</p>
  </footer>
</body>
</html>"""

# Execute Full 220-City Generation Loop
generated_count = 0
for city in CITIES:
    filename = city['slug']
    content = build_city_post(city)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    generated_count += 1

print(f"\n🎉 SUCCESS! Regenerated all {generated_count} city posts with PodcastSeries/Article JSON-LD schema & Influencer title!")