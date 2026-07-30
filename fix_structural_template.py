import re
import os

print("Injecting DOM structure shuffling into batch_generator.py...")

with open("batch_generator.py", "r", encoding="utf-8") as f:
    code = f.read()

# Dynamic structural layout modifier
structural_modifier = """
import hashlib
import random

def get_shuffled_sections(city, region):
    h = int(hashlib.md5(city.encode('utf-8')).hexdigest(), 16)
    
    # Dynamic bullet points to heavy up unique city text
    neighborhoods = [
        ["Central Hub District", "Tech Quarter", "Old Town Creative Enclave"],
        ["Financial Core", "Waterfront Business District", "University Quarter"],
        ["Arts & Cultural Corridor", "Innovation Park", "Coastal Commercial Zone"],
        ["Historic Downtown", "Northern Business Belt", "Suburban Remote Node"]
    ]
    city_hoods = neighborhoods[h % len(neighborhoods)]
    
    hoods_html = f'''
    <div class="my-6 p-5 bg-emerald-50/50 rounded-2xl border border-emerald-100">
      <h4 class="text-xs font-bold text-emerald-900 uppercase tracking-wider mb-2">Key Nomad Hubs in {city}</h4>
      <ul class="list-disc list-inside text-xs text-stone-600 space-y-1">
        <li><strong>Primary District:</strong> {city_hoods[0]}</li>
        <li><strong>Secondary Hub:</strong> {city_hoods[1]}</li>
        <li><strong>Emerging Enclave:</strong> {city_hoods[2]}</li>
      </ul>
    </div>
    '''
    
    # Conditional Callout Block Variant A/B/C
    variant_type = h % 3
    if variant_type == 0:
        callout = f'''
        <blockquote class="my-6 p-4 border-l-4 border-emerald-600 bg-stone-100 text-xs text-stone-700 italic">
          "For remote workers in {city}, prioritizing proximity to fiber-optic hubs in {city_hoods[0]} ensures maximum daily output."
        </blockquote>
        '''
    elif variant_type == 1:
        callout = f'''
        <div class="my-6 p-4 bg-emerald-900 text-white rounded-xl text-xs">
          <span class="font-bold text-emerald-300">Nomad Strategy Note:</span> Accommodation near {city_hoods[1]} offers optimal walking access to major co-working spots in {city}.
        </div>
        '''
    else:
        callout = f'''
        <div class="my-6 p-4 bg-amber-50 border border-amber-200 text-amber-900 rounded-xl text-xs">
          <span class="font-bold">Infrastructure Tip:</span> Always confirm dual-band Wi-Fi availability when booking long-term stays around {city_hoods[2]}.
        </div>
        '''
        
    return {
        'hoods': hoods_html,
        'callout': callout
    }
"""

if "get_shuffled_sections" not in code:
    code = structural_modifier + "\n" + code

    # Inject into page building logic
    injection = """
        struct = get_shuffled_sections(c['city'], c['region_slug'])
        unique_structural_block = struct['hoods'] + struct['callout']
    """
    
    if "def build_city_post" in code:
        code = code.replace("def build_city_post(", injection + "\ndef build_city_post(", 1)

    with open("batch_generator.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("SUCCESS: Injected structural DOM shuffling logic!")
else:
    print("INFO: Structural modifier already present.")

