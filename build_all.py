import subprocess
import sys

scripts = [
    ("1. Generating Comparison Pages", "generate_comparisons.py"),
    ("2. Repairing Regional Links & Hubs", "fix_internal_links.py"),
    ("3. Cleaning Dead Spoke References", "clean_dead_spokes.py"),
    ("4. Generating XML Sitemap", "generate_sitemap.py"),
    ("5. Applying AI SEO & Metadata", "apply_ai_seo.py"),
    ("6. Auditing Internal Links", "audit_links.py"),
    ("7. Pinging IndexNow Engine", "ping_indexnow.py")
]

print("=== STARTING MASTER SITE BUILD PIPELINE ===")

for description, script in scripts:
    print(f"\n--- Running: {description} ({script}) ---")
    result = subprocess.run([sys.executable, script])
    if result.returncode != 0:
        print(f"❌ Error encountered in {script}. Stopping build.")
        sys.exit(1)

print("\n=== MASTER BUILD COMPLETE: ALL STAGES PASSED SUCCESSFULLY ===")