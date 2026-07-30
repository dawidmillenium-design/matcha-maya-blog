import os
import re
import random
import difflib

# 1. Gather all HTML files
html_files = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

print("==================================================")
print("🚀 RUNNING MATCHA MAYA SEO AUDIT...")
print("==================================================\n")

# --- AUDIT 1: INTERNAL LINK INTEGRITY ---
print("--- 1. INTERNAL LINK & SILO INTEGRITY AUDIT ---")
broken_links = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Find all hrefs
    links = re.findall(r'href=["\']([^"\']+)["\']', content)
    for link in links:
        # Ignore external links, mailto, and anchor jumps
        if link.startswith("http") or link.startswith("#") or link.startswith("mailto:") or link == "/":
            continue
        
        # Resolve relative paths
        base_dir = os.path.dirname(file_path)
        target_path = os.path.normpath(os.path.join(base_dir, link))
        
        if not os.path.exists(target_path):
            print(f"[X] BROKEN LINK in {file_path}: {link}")
            broken_links += 1

if broken_links == 0:
    print("✅ SUCCESS: 0 broken internal links found! Your SILO PageRank funnel is fully intact.\n")
else:
    print(f"❌ WARNING: Found {broken_links} broken links. Fix these before indexing!\n")


# --- AUDIT 2: N-GRAM TEXT UNIQUENESS ---
print("--- 2. SCALED CONTENT ABUSE (UNIQUENESS) AUDIT ---")
city_files = [f for f in html_files if "-podcast-proposal.html" in f]

def get_clean_text(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
        # Strip all HTML tags to compare pure text
        text = re.sub(r'<[^>]+>', ' ', content)
        return " ".join(text.split())

if len(city_files) >= 2:
    # Randomly sample 5 city pages for comparison
    samples = random.sample(city_files, min(5, len(city_files)))
    total_ratio = 0
    comparisons = 0
    
    for i in range(len(samples)):
        for j in range(i + 1, len(samples)):
            text1 = get_clean_text(samples[i])
            text2 = get_clean_text(samples[j])
            # Calculate mathematical similarity between the two text strings
            ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
            total_ratio += ratio
            comparisons += 1
            city1 = os.path.basename(samples[i]).replace('-podcast-proposal.html', '')
            city2 = os.path.basename(samples[j]).replace('-podcast-proposal.html', '')
            print(f"Comparing {city1.title()} vs {city2.title()} -> Similarity: {ratio*100:.1f}%")
    
    avg_sim = (total_ratio / comparisons) * 100
    print(f"\n📊 AVERAGE CONTENT SIMILARITY: {avg_sim:.1f}%")
    
    if avg_sim > 45.0:
        print("⚠️ WARNING: Similarity is high. You risk Google's 'Scaled Content Abuse' penalty. Consider adding more randomized variables or unique district data to your batch generator.")
    else:
        print("✅ SUCCESS: Content uniqueness is excellent! Pages are mathematically distinct.")
else:
    print("Not enough city pages found to run uniqueness audit.")
print("\n==================================================")
