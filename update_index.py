import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Matcha Maya Blog - 220 Global Digital Nomad City Guides</title>
  <meta name="description" content="Explore 220 podcast proposals and digital nomad infrastructure guides across 10 global regions." />
  <link rel="canonical" href="https://dawidmillenium-design.github.io/matcha-maya-blog/index.html" />
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-stone-50 text-stone-800 font-sans antialiased min-h-screen flex flex-col">

  <!-- Header -->
  <header class="bg-emerald-900 text-white py-8 px-4 shadow-md">
    <div class="max-w-5xl mx-auto text-center">
      <h1 class="text-3xl md:text-4xl font-extrabold tracking-tight">MATCHA MAYA BLOG</h1>
      <p class="text-emerald-200 text-sm mt-2">220 Global Digital Nomad City Guides & Podcast Proposals</p>
    </div>
  </header>

  <!-- Main Content Area -->
  <main class="max-w-5xl mx-auto px-4 py-8 flex-grow w-full">
    
    <!-- Search & Filter Controls -->
    <section class="mb-8 bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="relative flex-grow">
          <input 
            type="text" 
            id="citySearchInput" 
            placeholder="Search 220 cities (e.g., Bangkok, Lisbon, Tokyo)..." 
            class="w-full px-4 py-3 pl-11 rounded-xl border border-stone-300 focus:outline-none focus:ring-2 focus:ring-emerald-600 focus:border-transparent text-sm shadow-inner transition"
            onkeyup="filterCities()"
          />
          <svg class="w-5 h-5 text-stone-400 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
        </div>
        <div class="flex items-center justify-between md:justify-end gap-3 text-xs text-stone-500 font-medium">
          <span id="cityCounter" class="bg-emerald-50 text-emerald-800 px-3 py-2 rounded-lg border border-emerald-200">
            Showing <strong id="visibleCount">220</strong> of 220 cities
          </span>
          <button 
            onclick="clearSearch()" 
            id="clearBtn"
            class="hidden text-stone-400 hover:text-stone-700 underline transition"
          >
            Clear filter
          </button>
        </div>
      </div>
    </section>

    <!-- Regional SILO Hub Navigation -->
    <section class="mb-10">
      <h2 class="text-xs font-bold text-stone-400 uppercase tracking-wider mb-4">Browse by Regional SILO Hubs</h2>
      <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-3 text-xs font-semibold">
        <a href="regions/southeast-asia.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">Southeast Asia</a>
        <a href="regions/east-asia.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">East Asia</a>
        <a href="regions/south-asia.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">South Asia</a>
        <a href="regions/central-asia.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">Central Asia</a>
        <a href="regions/middle-east.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">Middle East</a>
        <a href="regions/africa.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">Africa</a>
        <a href="regions/western-europe.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">Western Europe</a>
        <a href="regions/uk-eastern-europe.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">UK & Eastern Europe</a>
        <a href="regions/north-america.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">North America</a>
        <a href="regions/south-america.html" class="p-3 bg-stone-100 hover:bg-emerald-800 hover:text-white rounded-xl border border-stone-200 text-center transition">South America</a>
      </div>
    </section>

    <!-- 220 City Grid -->
    <section>
      <h2 class="text-xs font-bold text-stone-400 uppercase tracking-wider mb-4">All City Guides</h2>
      
      <!-- Container for JavaScript Filtering -->
      <div id="cityGridContainer" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
"""

# Append links dynamically for all 220 city files present in working directory
import os
files = [f for f in os.listdir(".") if f.endswith("-podcast-proposal.html")]
files.sort()

for f in files:
    city_name = f.replace("-podcast-proposal.html", "").replace("-", " ").title()
    html_content += f'        <a href="{f}" class="city-card p-3.5 bg-white hover:bg-emerald-50 rounded-xl border border-stone-200 text-xs font-medium text-stone-700 hover:text-emerald-900 hover:border-emerald-300 transition flex items-center justify-between" data-city="{city_name.lower()}">\n'
    html_content += f'          <span>{city_name}</span>\n'
    html_content += f'          <span class="text-stone-300 group-hover:text-emerald-600">&rarr;</span>\n'
    html_content += f'        </a>\n'

html_content += """      </div>

      <!-- No Results Feedback State -->
      <div id="noResultsState" class="hidden py-12 text-center bg-white rounded-2xl border border-stone-200 mt-4">
        <p class="text-stone-500 text-sm font-medium">No matching cities found.</p>
        <button onclick="clearSearch()" class="mt-2 text-xs text-emerald-700 underline font-semibold">Reset Filter</button>
      </div>
    </section>
  </main>

  <!-- Footer -->
  <footer class="bg-stone-900 text-stone-400 text-center py-6 text-xs mt-12">
    <p>MATCHA MAYA &copy; 2026 - 220 City Guides Index</p>
  </footer>

  <!-- Instant JavaScript Filter Logic -->
  <script>
    function filterCities() {
      const input = document.getElementById('citySearchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.city-card');
      const clearBtn = document.getElementById('clearBtn');
      const noResults = document.getElementById('noResultsState');
      let visibleCount = 0;

      cards.forEach(card => {
        const cityData = card.getAttribute('data-city');
        if (cityData.includes(input)) {
          card.classList.remove('hidden');
          card.classList.add('flex');
          visibleCount++;
        } else {
          card.classList.remove('flex');
          card.classList.add('hidden');
        }
      });

      // Update visible city count
      document.getElementById('visibleCount').textContent = visibleCount;

      // Show/hide clear button
      if (input.length > 0) {
        clearBtn.classList.remove('hidden');
      } else {
        clearBtn.classList.add('hidden');
      }

      // Show no results state if count is zero
      if (visibleCount === 0) {
        noResults.classList.remove('hidden');
      } else {
        noResults.classList.add('hidden');
      }
    }

    function clearSearch() {
      document.getElementById('citySearchInput').value = '';
      filterCities();
    }
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"SUCCESS: Updated index.html with interactive JS search bar across {len(files)} city guides!")
