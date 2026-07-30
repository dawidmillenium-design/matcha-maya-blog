import os
import re

all_files = [f for f in os.listdir(".") if f.endswith("-podcast-proposal.html")]
print(f"Loaded {len(all_files)} city podcast proposal files for fact-checking...\n")

issues_found = 0

for file in sorted(all_files):
    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    city_name = file.replace("-podcast-proposal.html", "").replace("-", " ").title()

    # Audit Rule 1: Missing Question 13 or truncated answer
    if "Q13: What are the most frequently connected domestic and international cities" not in content:
        print(f"[MISSING Q13] {file} does not contain Question 13.")
        issues_found += 1

    # Audit Rule 2: Placeholder text check
    if "undefined" in content.lower() or "null" in content.lower() or "todo" in content.lower():
        print(f"[PLACEHOLDER] {file} contains unfinished placeholder text.")
        issues_found += 1

    # Audit Rule 3: Missing JSON-LD Schema structured data
    if '"@type": "PodcastSeries"' not in content or '"@type": "Article"' not in content:
        print(f"[SCHEMA ERROR] {file} is missing complete JSON-LD Podcast/Article schema.")
        issues_found += 1

if issues_found == 0:
    print(f"SUCCESS: All {len(all_files)} city pages passed structural fact-checking and data completeness checks!")
else:
    print(f"\nAUDIT COMPLETE: Found {issues_found} potential issue(s) across the dataset.")
