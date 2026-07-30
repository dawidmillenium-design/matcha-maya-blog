import os
import re
from batch_generator import generate_intent_pillars_html, generate_city_schema

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
updated_count = 0

for file_name in html_files:
    clean_name = file_name.replace('-coworking-guide.html', '').replace('-podcast-proposal.html', '').replace('.html', '')
    city_slug = clean_name
    city_name = clean_name.replace('-', ' ').title()

    with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_pillars = generate_intent_pillars_html(city_slug, city_name)
    new_schema = generate_city_schema(city_slug, city_name, 100, 1500)

    if '<!-- INTENT_PILLARS_START -->' in content and '<!-- INTENT_PILLARS_END -->' in content:
        content = re.sub(r'<!-- INTENT_PILLARS_START -->.*?<!-- INTENT_PILLARS_END -->', f'<!-- INTENT_PILLARS_START -->\n{new_pillars}\n<!-- INTENT_PILLARS_END -->', content, flags=re.DOTALL)
    else:
        if '</main>' in content:
            content = content.replace('</main>', f'{new_pillars}\n</main>')
        elif '</body>' in content:
            content = content.replace('</body>', f'{new_pillars}\n</body>')

    if '<script type="application/ld+json">' in content:
        content = re.sub(r'<script type="application/ld\+json">.*?</script>', new_schema, content, flags=re.DOTALL)
    else:
        content = content.replace('</head>', f'{new_schema}\n</head>')

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

    updated_count += 1

print(f"Successfully re-rendered and updated {updated_count} city HTML files on disk.")