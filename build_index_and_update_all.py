import os

REGIONS = {
    "southeast-asia": "Southeast Asia",
    "east-asia": "East Asia",
    "south-asia": "South Asia",
    "central-asia": "Central Asia",
    "middle-east": "Middle East",
    "africa": "Africa",
    "western-europe": "Western Europe",
    "uk-eastern-europe": "UK & Eastern Europe",
    "north-america": "North America",
    "south-america": "South America"
}

def build_root_index():
    region_cards = ""
    for r_slug, r_name in REGIONS.items():
        region_cards += f"""
        <a href="regions/{r_slug}.html" class="block p-6 bg-white rounded-xl border border-stone-200 hover:border-emerald-500 hover:shadow-md transition">
          <h2 class="text-lg font-bold text-stone-900">{r_name} Hub</h2>
          <p class="text-xs text-stone-500 mt-1">Explore podcast proposals, remote work infrastructure, and lifestyle insights for {r_name} destinations.</p>
          <span class="inline-block mt-3 text-xs font-semibold text-emerald-700">Browse {r_name} Cities -></span>
        </a>"""

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Matcha Maya Blog - Global Remote Work & Podcast Proposals</title>
  <meta name="description" content="Matcha Maya global blog platform covering digital nomad lifestyle, high-speed workspace analysis, visa requirements, and city podcast proposals across 220 global destinations." />
  <script src="https://cdn.tailwindcss.com"></script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Matcha Maya Blog",
    "url": "https://dawidmillenium-design.github.io/matcha-maya-blog/",
    "description": "Global hub for remote work podcasts, workspace infrastructure, and digital nomad lifestyle insights."
  }}
  </script>
</head>
<body class="bg-stone-50 text-stone-800 font-sans antialiased">
  <header class="bg-emerald-900 text-white p-6 shadow-md">
    <div class="max-w-5xl mx-auto flex justify-between items-center">
      <a href="index.html" class="font-bold text-lg tracking-wide">MATCHA MAYA</a>
      <span class="text-xs text-emerald-300">220 Global City Destinations</span>
    </div>
  </header>

  <main class="max-w-5xl mx-auto px-4 py-12">
    <section class="text-center mb-12">
      <h1 class="text-3xl md:text-4xl font-extrabold text-stone-900">Global Podcast Proposals & Nomad Guides</h1>
      <p class="text-sm text-stone-600 max-w-2xl mx-auto mt-3">
        Comprehensive 12-point city analysis covering internet speeds, SIM cards, influencer media, rooftop venues, luxury rents, and local tech innovation. Select a continent or region below to browse city proposals.
      </p>
    </section>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      {region_cards}
    </div>
  </main>

  <footer class="bg-stone-900 text-stone-400 py-8 text-center text-xs border-t border-stone-800 mt-12">
    <p>MATCHA MAYA (C) 2026 - Global Digital Nomad SILO Platform</p>
  </footer>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
    print("Created root index.html with regional hub SILO links.")

def rename_and_update_links():
    renamed_count = 0
    updated_files = 0

    for file in os.listdir("."):
        if file.endswith("-interview.html"):
            old_path = file
            new_path = file.replace("-interview.html", "-podcast-proposal.html")
            os.rename(old_path, new_path)
            renamed_count += 1

    print(f"Renamed {renamed_count} city files to *-podcast-proposal.html")

    all_html_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                all_html_files.append(os.path.join(root, file))

    for filepath in all_html_files:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        new_content = content.replace("-interview.html", "-podcast-proposal.html")

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_files += 1

    print(f"Updated internal link references in {updated_files} HTML files.")

if __name__ == "__main__":
    build_root_index()
    rename_and_update_links()
