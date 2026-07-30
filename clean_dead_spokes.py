import glob
import os

print("--- CLEANING DEAD SPOKE REFERENCES ---")

# Map specific missing pages to active equivalents
REMAPS = {
    "bali-coworking-guide.html": "bali-podcast-proposal.html",
    "chiang-mai-coworking-guide.html": "chiang-mai-podcast-proposal.html",
    "da-nang-coworking-guide.html": "da-nang-podcast-proposal.html",
    "florianopolis-coworking-guide.html": "florianopolis-podcast-proposal.html",
    "porto-coworking-guide.html": "porto-podcast-proposal.html",
    "../index2.html": "index.html"
}

html_files = glob.glob("*.html")
updated_count = 0

for file in html_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        continue

    modified = False
    for dead_link, active_link in REMAPS.items():
        if dead_link in content:
            content = content.replace(dead_link, active_link)
            modified = True

    if modified:
        with open(file, "w", encoding="utf-8") as f:
            f.write(content)
        updated_count += 1

print(f"✔ Fixed dead spoke references across {updated_count} files!")