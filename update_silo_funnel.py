import re
import os

print("Injecting PageRank Funnel into site generation pipeline...")

# Read batch_generator.py
with open("batch_generator.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update build_city_post template if not already modified
if "Upward PageRank Funnel Box" not in code:
    # Add Google verification tag to template head
    code = re.sub(
        r'(<head.*?>)',
        r'\1\n  <meta name="google-site-verification" content="ddryQTwrxDAxNvgfjcrTs2eW06UebOvdNums43rTfJc" />',
        code,
        count=1
    )

    # Inject Breadcrumb Navigation at top of body
    breadcrumb_nav = """
    <!-- Enhanced SILO Breadcrumb Header -->
    <nav class="bg-emerald-900 text-white py-3 px-4 text-xs shadow-md" aria-label="Breadcrumb">
      <div class="max-w-4xl mx-auto flex items-center justify-between">
        <div class="flex items-center space-x-2">
          <a href="https://dawidmillenium-design.github.io/matcha-maya-blog/index.html" class="font-bold text-emerald-200 hover:text-white transition">Home</a>
          <span class="text-emerald-400">&rsaquo;</span>
          <a href="regions/{c['region_slug']}.html" class="font-semibold text-emerald-200 hover:text-white underline transition">
            {c['region_slug'].replace('-', ' ').title()} Hub
          </a>
          <span class="text-emerald-400">&rsaquo;</span>
          <span class="text-stone-300 truncate">{c['city']}</span>
        </div>
        <span class="hidden sm:inline-block text-stone-400 text-[10px] uppercase font-mono">SILO Node</span>
      </div>
    </nav>
    """

    # Inject In-Content Upward Funnel Banner
    funnel_banner = """
    <!-- Upward PageRank Funnel Box -->
    <div class="my-8 bg-emerald-950 text-white p-6 rounded-2xl border border-emerald-800 shadow-md">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
        <div>
          <span class="text-[10px] font-bold text-emerald-400 uppercase tracking-widest">Regional Hub Directory</span>
          <h4 class="text-sm font-bold text-white mt-1">Explore All Nomad Guides in {c['region_slug'].replace('-', ' ').title()}</h4>
          <p class="text-xs text-stone-300 mt-1">Compare visa requirements, internet reliability, and living costs across neighboring regional cities.</p>
        </div>
        <a href="regions/{c['region_slug']}.html" class="inline-flex items-center justify-center px-4 py-2.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold rounded-xl transition whitespace-nowrap shadow-sm">
          View {c['region_slug'].replace('-', ' ').title()} Hub &rarr;
        </a>
      </div>
    </div>
    """

    # Target key locations for injection inside the python generator file
    if '<header' in code:
        code = code.replace('<header', breadcrumb_nav + '\n<header', 1)
    
    if '<!-- Nomad Debate Section -->' in code:
        code = code.replace('<!-- Nomad Debate Section -->', funnel_banner + '\n<!-- Nomad Debate Section -->', 1)

    with open("batch_generator.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("SUCCESS: Updated batch_generator.py with internal PageRank funnel elements!")
else:
    print("INFO: batch_generator.py already contains PageRank Funnel elements.")

