import re
import os

print("Injecting multi-section sentence rotation into batch_generator.py...")

with open("batch_generator.py", "r", encoding="utf-8") as f:
    code = f.read()

# Section-level sentence pools for combinatorial uniqueness
rotation_logic = """
import hashlib

def get_combinatorial_content(city, region):
    h = int(hashlib.md5(city.encode('utf-8')).hexdigest(), 16)
    
    # 1. Randomized Intro Hook
    intros = [
        f"Navigating {city}'s evolving remote work scene requires a balance of local neighborhood strategy and reliable infrastructure.",
        f"For global nomads targeting {city}, establishing a productive daily workflow hinges on choosing the right district hub.",
        f"As digital nomad interest in {city} continues to climb, understanding real-world living costs and internet stability is essential.",
        f"{city} has rapidly emerged as a notable destination for remote professionals seeking strong connectivity and high quality of life.",
        f"Setting up a temporary base in {city} offers a unique blend of regional culture and modern co-working amenities."
    ]
    
    # 2. Randomized Infrastructure Lead-in
    infra_leads = [
        f"When evaluating {city}'s suitability for long-term stays, internet speed and workspace accessibility take top priority.",
        f"Remote professionals in {city} typically rely on dedicated co-working hubs and work-friendly cafes equipped with high-speed fiber.",
        f"Ensuring uninterrupted productivity in {city} depends on identifying key neighborhoods with dependable Wi-Fi and generator backups.",
        f"Connectivity across {city} varies by district, making strategic accommodation choices critical for digital nomads."
    ]

    # 3. Randomized District Context
    districts = [
        f"Central business zones and creative quarters offer the highest concentration of high-speed hubs in {city}.",
        f"Emerging residential enclaves in {city} are increasingly catering to remote workers with modern cafe culture.",
        f"The primary nomad cluster in {city} is centered around accessible transit lines and walkable commercial strips.",
        f"Selecting a residential base near major coworking nodes drastically reduces daily transit time in {city}."
    ]

    intro_text = intros[h % len(intros)]
    infra_text = infra_leads[(h >> 2) % len(infra_leads)]
    district_text = districts[(h >> 4) % len(districts)]
    
    return {
        'intro': intro_text,
        'infra': infra_text,
        'district': district_text
    }
"""

if "get_combinatorial_content" not in code:
    code = rotation_logic + "\n" + code

    # Inject dynamic text blocks inside page construction logic
    injection_snippet = """
        cc = get_combinatorial_content(c['city'], c['region_slug'])
        unique_paragraph_block = f'''
        <div class="my-6 p-6 bg-white rounded-2xl border border-stone-200 shadow-sm font-sans text-xs leading-relaxed text-stone-600">
          <p class="mb-3 font-medium text-stone-800">{cc['intro']}</p>
          <p class="mb-3">{cc['infra']}</p>
          <p class="text-stone-500 italic">{cc['district']}</p>
        </div>
        '''
    """
    
    if "def build_city_post" in code:
        code = code.replace("def build_city_post(", injection_snippet + "\ndef build_city_post(", 1)

    with open("batch_generator.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("SUCCESS: Injected section-level sentence rotation into batch_generator.py!")
else:
    print("INFO: Combinatorial rotation function already present.")

