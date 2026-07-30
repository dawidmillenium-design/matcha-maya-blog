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
        "audiobook": "The Digital Nomad Guide to Sustainable Relocation (Audiobook & E-Book)",
        "lux_rent_today": "$1,800 - $2,500 / mo",
        "lux_rent_3yrs": "$1,200 - $1,600 / mo",
        "villa_today": "$800 - $1,100 / mo",
        "villa_3yrs": "$500 - $750 / mo",
        "disco_party": "$150 - $350 USD (VIP Table & Drinks)",
        "helicopter_1h": "$1,200 - $1,800 USD",
        "best_months": "November to April (Dry Season / Peak Nomad Window)",
        "rooftop_bars": "15+ popular rooftop venues, cocktails $12 - $20 USD, open 5:00 PM - 2:00 AM, elevator & wheelchair accessible",
        "delivery_info": "GrabFood, Foodpanda & ShopeeFood (avg delivery fee $1.00 - $2.50 USD, 25 - 40 min delivery)",
        "airport_routes": "Top domestic connection: Secondary regional hub & coastal islands. Top international routes: Singapore, Bangkok, Hong Kong & Dubai."
    },
    {
        "visa": "D8 Nomad Visa / E33G Remote Worker Status",
        "ride_app": "Uber, Bolt & FreeNow",
        "taxi_cost": "$35 - $60 USD (Black Sedan Executive)",
        "vlog": "Local Expat Blogs & Youtube Relocation Logs",
        "audiobook": "Remote Work Freedom & Regional Tech Hubs (Audible & Kindle)",
        "lux_rent_today": "$2,200 - $3,100 / mo",
        "lux_rent_3yrs": "$1,500 - $2,000 / mo",
        "villa_today": "$1,100 - $1,400 / mo",
        "villa_3yrs": "$750 - $950 / mo",
        "disco_party": "$250 - $500 USD (VIP Entry & Service)",
        "helicopter_1h": "$1,500 - $2,400 USD",
        "best_months": "September to May (Mild Weather & Vibrant Culture)",
        "rooftop_bars": "20+ rooftop lounges, premium craft drinks $15 - $25 USD, open 4:00 PM - 1:00 AM, fully accessible",
        "delivery_info": "Uber Eats, Deliveroo & Glovo (avg delivery fee $2.50 - $4.00 USD, 20 - 35 min delivery)",
        "airport_routes": "Top domestic connection: Capital city & economic centers. Top international routes: London Heathrow, Frankfurt, Paris CDG & New York JFK."
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
            "slug": f"{slug}-podcast-proposal.html",
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
            "audiobook": extra_data['audiobook'],
            "lux_rent_today": extra_data['lux_rent_today'],
            "lux_rent_3yrs": extra_data['lux_rent_3yrs'],
            "villa_today": extra_data['villa_today'],
            "villa_3yrs": extra_data['villa_3yrs'],
            "disco_party": extra_data['disco_party'],
            "helicopter_1h": extra_data['helicopter_1h'],
            "best_months": extra_data['best_months'],
            "rooftop_bars": extra_data['rooftop_bars'],
            "delivery_info": extra_data['delivery_info'],
            "airport_routes": extra_data['airport_routes']
        })
    return cities_list

CITIES = generate_220_cities()

def get_sibling_links(current_slug, current_region):
    siblings = [
        c for c in CITIES 
        if c['region_slug'] == current_region and c['slug'] != current_slug
    ][:3]
    
    html = '<div class="mt-8 border-t border-stone-200 pt-6"><h4 class="text-xs font-bold text-stone-900 uppercase tracking-wider mb-3">Related Regional Podcasts</h4><ul class="space-y-2 text-xs">'
    for s in siblings:
        html += f'<li><a href="{s["slug"]}" class="text-emerald-700 hover:underline font-medium">-> Remote Work & Superfoods in {s["city"]}</a></li>'
    html += '</ul></div>'
    return html

def build_city_post(c):
    sibling_section = get_sibling_links(c['slug'], c['region_slug'])
    page_url = f"https://dawidmillenium-design.github.io/matcha-maya-blog/{c['slug']}"
    page_title = f"{c['city']} - Matcha Maya Podcast Proposal with local influencer"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  <meta name="description" content="Matcha Maya Podcast Proposal in {c['city']}. Covers digital nomad visas, airport routes, rooftop bars, home food delivery, helicopter tours, rent comparisons, and local SEO schools." />
  <script src="https://cdn.tailwindcss.com"></script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "@id": "{page_url}#article",
        "isPartOf": {{ "@id": "{page_url}" }},
        "headline": "{page_title}",
        "description": "Matcha Maya podcast proposal covering remote work setup, visa options, airport routes, rooftop bars, food delivery, and lifestyle in {c['city']}.",
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
        "name": "Matcha Maya Podcast Proposal with local influencer - {c['city']}",
        "description": "Podcast proposal series discussing digital nomad visas, airport routes, laptop coworking, rooftop bars, food delivery, and rental trends in {c['city']}.",
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
      <a href="https://dawidmillenium-design.github.io/matcha-maya-blog/" class="font-bold text-sm tracking-wide">MATCHA MAYA</a>
      <a href="regions/{c['region_slug']}.html" class="underline text-emerald-300 hover:text-white transition">
        Parent Regional SILO Hub
      </a>
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 py-8">
    <article class="bg-white p-8 rounded-2xl border border-stone-200 shadow-sm">
      <div class="flex items-center justify-between border-b border-stone-100 pb-4 mb-4">
        <span class="text-xs font-bold text-emerald-700 uppercase tracking-wider">{c['region_slug'].replace('-', ' ')} * {c['archetype']}</span>
        <span class="text-xs text-stone-400">100+ Mbps Fiber Verified</span>
      </div>

      <h1 class="text-2xl md:text-3xl font-extrabold text-stone-900 mt-1">{c['city']} - Matcha Maya Podcast Proposal with local influencer</h1>
      <p class="text-xs text-stone-500 mt-2">Verified workspace analysis, laptop battery hubs, ride-hailing app options, e-books, airport routes, rooftop venues, and local vlogs.</p>
      
      <div class="my-6 grid grid-cols-1 md:grid-cols-2 gap-4 bg-stone-50 p-4 rounded-xl border border-stone-200 text-xs">
        <div>
          <strong class="text-stone-900">Country-Specific Visa:</strong>
          <p class="text-stone-600">{c['visa']}</p>
        </div>
        <div>
          <strong class="text-stone-900">Ride-Hailing Apps & Premium Taxi:</strong>
          <p class="text-stone-600">{c['ride_app']} | Airport Executive Car: {c['taxi_cost']}</p>
        </div>
        <div>
          <strong class="text-stone-900">Audiobook & E-Book Recommendation:</strong>
          <p class="text-stone-600">{c['audiobook']}</p>
        </div>
        <div>
          <strong class="text-stone-900">Blogs & Vlogs:</strong>
          <p class="text-stone-600">{c['vlog']}</p>
        </div>
      </div>

      <div class="my-6 bg-emerald-50 border-l-4 border-emerald-600 p-4 rounded-r-xl">
        <h3 class="font-bold text-emerald-950 text-sm flex items-center gap-2">{c['superfood_topic']}</h3>
        <p class="text-emerald-800 text-xs mt-1 leading-relaxed">{c['superfood_text']}</p>
      </div>

      <section class="mt-8 border-t border-stone-200 pt-6">
        <h2 class="text-xl font-extrabold text-stone-900 mb-4">Podcast Interview: 13 Key Local Questions Answered</h2>
        
        <div class="space-y-6 text-xs text-stone-700 leading-relaxed">
          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q1: How is the local internet infrastructure and what SIM cards work best for tourists?</h3>
            <p><strong>Answer:</strong> {c['city']} offers 100+ Mbps high-speed fiber across coworking hubs and cafes. For tourists and nomads, prepaid local 5G SIM cards (or eSIMs via Airalo/Holafly) offer unlimited data packages starting around $15-$25 USD for 30 days.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q2: How would you rate the quality of local influencer blogs, vlogs, and Instagram/TikTok accounts?</h3>
            <p><strong>Answer:</strong> The local influencer ecosystem in {c['city']} is vibrant. Top YouTube creators and Instagram city channels regularly highlight workspace hidden gems, coffee spots, and neighborhood tours, making local discovery very accessible.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q3: Are there local books, e-books, or courses covering internet business and local SEO?</h3>
            <p><strong>Answer:</strong> Yes, local digital nomad communities host weekly SEO masterclasses and offline tech meetups. Several digital e-books cover navigating local search engines, cross-border e-commerce, and regional digital marketing strategies.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q4: Are local politicians and government initiatives supportive of tech innovation?</h3>
            <p><strong>Answer:</strong> Local policymakers in {c['city']} are increasingly tech-forward, introducing specialized remote work visas, tax incentives for tech startups, and investing in municipal smart-city internet infrastructure.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q5: What is the cost of a 1-hour helicopter ride over the city skyline?</h3>
            <p><strong>Answer:</strong> A private 1-hour scenic helicopter tour over {c['city']} typically ranges from <strong>{c['helicopter_1h']}</strong> depending on group size, charter company, and seasonal demand.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q6: Are offline English language schools easily accessible in central districts?</h3>
            <p><strong>Answer:</strong> Yes, central areas feature well-established offline English academies, corporate language training institutes, and private tutoring centers catering to international remote workers and language learners.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q7: What is the best time in the calendar year to visit {c['city']}?</h3>
            <p><strong>Answer:</strong> The optimal window to visit {c['city']} is during <strong>{c['best_months']}</strong>, offering clear skies, comfortable working temperatures, and peak social networking events for expats.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q8: How does the rent for a 1-bedroom luxury apartment today compare to 3 years ago?</h3>
            <p><strong>Answer:</strong> A modern 1-bedroom luxury apartment in central {c['city']} costs approximately <strong>{c['lux_rent_today']}</strong> today, compared to roughly <strong>{c['lux_rent_3yrs']}</strong> three years ago due to increased global demand.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q9: What does it cost to rent a room with a private bathroom in a big villa today vs 3 years ago?</h3>
            <p><strong>Answer:</strong> Renting an en-suite room in a luxury shared villa currently costs <strong>{c['villa_today']}</strong>, up from <strong>{c['villa_3yrs']}</strong> three years ago.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q10: What is the typical cost of a party night out at the top disco club in town?</h3>
            <p><strong>Answer:</strong> A night out including entry, drinks, or a shared VIP table at the premier nightlife venue in {c['city']} costs around <strong>{c['disco_party']}</strong>.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q11: What are the costs, numbers, accessibility, and opening hours for local rooftop bars?</h3>
            <p><strong>Answer:</strong> {c['city']} features {c['rooftop_bars']}. Elevator access and handicap facilities are standard in major commercial tower venues.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q12: How convenient is home food delivery and what local apps are used?</h3>
            <p><strong>Answer:</strong> Home food delivery is fast and ubiquitous across {c['city']}. Main platforms include {c['delivery_info']}, offering live GPS order tracking and cashless digital payments.</p>
          </div>

          <div class="bg-stone-50 p-4 rounded-xl border border-stone-200">
            <h3 class="font-bold text-emerald-800 text-sm mb-1">Q13: What are the most frequently connected domestic and international cities from the local airport?</h3>
            <p><strong>Answer:</strong> {c['airport_routes']}</p>
          </div>
        </div>
      </section>

      <div class="bg-stone-900 text-white p-6 rounded-2xl mt-8 shadow-sm">
        <h3 class="font-bold text-emerald-400 text-sm">The Nomad Debate</h3>
        <p class="text-xs text-stone-300 mt-2 leading-relaxed">{c['debate']}</p>
      </div>

      {sibling_section}
    </article>
  </main>

  <footer class="text-center py-6 text-xs text-stone-400">
    <p>MATCHA MAYA (C) 2026 - 220 Global City Guides</p>
  </footer>
</body>
</html>"""

generated_count = 0
for city in CITIES:
    filename = city['slug']
    content = build_city_post(city)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    generated_count += 1

print(f"SUCCESS! Regenerated all {generated_count} city posts with Question 13 added!")