import os

REGIONS_DATA = {
    "southeast-asia": {
        "title": "Southeast Asia Regional Hub",
        "cities": ["jakarta", "bangkok", "manila", "ho-chi-minh", "kuala-lumpur", "singapore", "phnom-penh", "vientiane", "yangon", "bali", "chiang-mai", "da-nang", "cebu", "phuket", "penang", "hanoi"]
    },
    "east-asia": {
        "title": "East Asia Regional Hub",
        "cities": ["tokyo", "osaka", "seoul", "busan", "taipei", "hong-kong", "shanghai", "guangzhou", "kyoto", "fukuoka", "sapporo", "kaohsiung", "taichung", "beijing", "shenzhen", "chengdu", "macau", "jeju"]
    },
    "south-asia": {
        "title": "South Asia Regional Hub",
        "cities": ["mumbai", "bengaluru", "colombo", "kathmandu", "delhi", "goa", "pune", "hyderabad", "chennai", "dhaka", "pokhara", "male", "kandy", "thimphu", "lahore", "karachi", "islamabad", "jaipur"]
    },
    "central-asia": {
        "title": "Central Asia Regional Hub",
        "cities": ["tbilisi", "almaty", "yerevan", "tashkent", "baku", "astana", "bishkek", "dushanbe", "samarkand", "batumi", "khujand", "ashgabat"]
    },
    "middle-east": {
        "title": "Middle East Regional Hub",
        "cities": ["dubai", "istanbul", "doha", "riyadh", "muscat", "amman", "beirut", "tel-aviv", "abu-dhabi", "jeddah", "antalya", "izmir", "ankara", "manama", "kuwait-city", "sharjah", "salalah", "aqaba", "erbil", "bursa", "bodrum", "al-ula"]
    },
    "africa": {
        "title": "Africa Regional Hub",
        "cities": ["cape-town", "nairobi", "cairo", "casablanca", "marrakech", "tunis", "lagos", "johannesburg", "accra", "kigali", "addis-ababa", "dakar", "zanzibar", "mauritius", "algiers", "alexandria", "kampala", "dar-es-salaam", "mombasa", "windhoek", "maputo", "luanda", "antananarivo", "pretoria", "durban", "taghazout"]
    },
    "western-europe": {
        "title": "Western Europe Regional Hub",
        "cities": ["lisbon", "barcelona", "berlin", "paris", "athens", "amsterdam", "madrid", "porto", "milan", "rome", "florence", "vienna", "zurich", "brussels", "munich", "hamburg", "dubrovnik", "split", "valletta", "nice", "lyon", "geneva", "rotterdam", "antwerp", "seville", "valencia", "faro", "funchal"]
    },
    "uk-eastern-europe": {
        "title": "UK & Eastern Europe Regional Hub",
        "cities": ["london", "prague", "warsaw", "budapest", "dublin", "edinburgh", "manchester", "krakow", "bucharest", "sofia", "tallinn", "riga", "vilnius", "belgrade", "zagreb", "bratislava", "ljubljana", "belfast", "glasgow", "cardiff", "birmingham", "gdansk", "wroclaw", "cluj-napoca", "varna", "plovdiv", "tartu", "kaunas", "sarajevo", "skopje"]
    },
    "north-america": {
        "title": "North America Regional Hub",
        "cities": ["new-york", "los-angeles", "san-francisco", "vancouver", "montreal", "austin", "miami", "chicago", "seattle", "mexico-city", "toronto", "boston", "denver", "portland", "san-diego", "honolulu", "playa-del-carmen", "tulum", "oaxaca", "puerto-vallarta", "guadalajara", "san-jose-cr", "panama-city", "calgary", "ottawa", "nashville"]
    },
    "south-america": {
        "title": "South America Regional Hub",
        "cities": ["buenos-aires", "medellin", "rio-de-janeiro", "santiago", "lima", "sao-paulo", "bogota", "quito", "la-paz", "montevideo", "florianopolis", "cartagena", "cusco", "mendoza", "bariloche", "cordoba", "salvador", "curitiba", "asuncion", "cuenca", "arequipa", "santa-marta", "cali", "guayaquil"]
    }
}

os.makedirs("regions", exist_ok=True)

for slug, data in REGIONS_DATA.items():
    city_links = ""
    for city_slug in data["cities"]:
        formatted_name = " ".join([word.capitalize() for word in city_slug.split('-')])
        city_links += f"""
        <a href="../{city_slug}-podcast-proposal.html" class="block p-4 bg-white rounded-xl border border-stone-200 hover:border-emerald-500 hover:shadow-sm transition">
          <h3 class="font-bold text-stone-900 text-sm">{formatted_name}</h3>
          <p class="text-xs text-stone-500 mt-1">13-Point Podcast Proposal & Nomad Guide</p>
          <span class="inline-block mt-2 text-xs font-semibold text-emerald-700">View Proposal -></span>
        </a>"""

    hub_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{data['title']} - Matcha Maya</title>
  <meta name="description" content="{data['title']} listing all city podcast proposals, digital nomad infrastructure, rent comparisons, and workspace guides." />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-stone-50 text-stone-800 font-sans antialiased">
  <header class="bg-emerald-900 text-white p-4 text-xs shadow-md">
    <div class="max-w-5xl mx-auto flex justify-between items-center">
      <a href="../index.html" class="font-bold text-sm tracking-wide">MATCHA MAYA</a>
      <a href="../index.html" class="underline text-emerald-300 hover:text-white transition"><- Back to Main Index</a>
    </div>
  </header>

  <main class="max-w-5xl mx-auto px-4 py-8">
    <div class="border-b border-stone-200 pb-4 mb-6">
      <h1 class="text-2xl md:text-3xl font-extrabold text-stone-900">{data['title']}</h1>
      <p class="text-xs text-stone-500 mt-1">Explore all city podcast proposals and digital nomad infrastructure across this region.</p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      {city_links}
    </div>
  </main>

  <footer class="text-center py-6 text-xs text-stone-400 mt-8 border-t border-stone-200">
    <p>MATCHA MAYA (C) 2026 - Regional SILO Hub</p>
  </footer>
</body>
</html>"""

    filepath = os.path.join("regions", f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(hub_html)

print("Created all 10 regional SILO hub HTML pages in /regions/!")
