import subprocess
import sys

scripts = [
    ("1. Generating Comparison Pages", "generate_comparisons.py"),
    ("2. Repairing Regional Links & Hubs", "fix_internal_links.py"),
    ("3. Cleaning Dead Spoke References", "clean_dead_spokes.py"),
    ("4. Applying AI SEO & Sitemap", "apply_ai_seo.py"),
    ("5. Auditing Internal Links", "audit_links.py"),
    ("6. Pinging IndexNow", "ping_indexnow.py")
]

print("==================================================")
print("🚀 MATCHA MAYA — FULL SITE BUILD PIPELINE")
print("==================================================\n")

for title, script in scripts:
    print(f"\n▶ [{title}]...")
    try:
        result = subprocess.run([sys.executable, script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing {script}. Aborting pipeline.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"⚠️ Script {script} not found, skipping.")

print("\n==================================================")
print("✨ BUILD COMPLETE! All 570+ pages updated & synced.")
print("==================================================")