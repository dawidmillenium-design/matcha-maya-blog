import glob

print("--- STARTING LLMS.TXT GENERATOR ---")

domain = "https://dawidmillenium-design.github.io/matcha-maya-blog"

# Collect files
spoke_files = sorted(glob.glob("*-coworking-guide.html"))
comp_files = sorted(glob.glob("*-vs-*-digital-nomad.html"))

llms_content = f"""# Matcha Maya Blog — Digital Nomad & Coworking City Index

> Comprehensive database of global digital nomad destinations featuring internet connectivity speeds, living costs, top coworking hubs, and transit profiles.

## Core Directories & Navigation
- Global Regional Hub: {domain}/hub.html
- Head-to-Head City Comparison Directory: {domain}/compare.html
- XML Sitemap: {domain}/sitemap.xml

## City Destinations ({len(spoke_files)} Guides)
"""

for page in spoke_files:
    city_name = page.replace("-coworking-guide.html", "").replace("-", " ").title()
    llms_content += f"- [{city_name} Digital Nomad Guide]({domain}/{page})\n"

llms_content += f"\n## City Comparisons ({len(comp_files)} Guides)\n"

for page in comp_files:
    comp_name = page.replace("-digital-nomad.html", "").replace("-vs-", " vs ").title()
    llms_content += f"- [{comp_name} Comparison]({domain}/{page})\n"

with open("llms.txt", "w", encoding="utf-8") as f:
    f.write(llms_content)

print(f"✔ Successfully generated llms.txt with {len(spoke_files) + len(comp_files)} indexed links!")