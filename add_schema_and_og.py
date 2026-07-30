import re
import os

print("Injecting FAQ Schema & Open Graph Meta Tags into batch_generator.py...")

# Read batch_generator.py
with open("batch_generator.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Inject Open Graph and FAQ Schema into template head if not present
if "schema.org" not in code or "og:title" not in code:
    og_and_schema_markup = """
  <!-- Open Graph Meta Tags -->
  <meta property="og:title" content="{page_title}" />
  <meta property="og:description" content="Explore digital nomad infrastructure, cost of living, and podcast proposals for {c['city']}." />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://dawidmillenium-design.github.io/matcha-maya-blog/{c['slug']}.html" />

  <!-- Google FAQ Schema (JSON-LD) for SERP Rich Snippets -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "Is {c['city']} a good destination for digital nomads?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{c['city']} offers high-speed remote work infrastructure, vibrant coworking communities, and diverse lifestyle options suited for global remote workers."
        }}
      }},
      {{
        "@type": "Question",
        "name": "What is the primary focus of the {c['city']} podcast proposal?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "The proposal highlights emerging district hubs, local nomad ecosystems, and actionable content strategies tailored for {c['city']}."
        }}
      }}
    ]
  }}
  </script>
    """

    # Inject inside the <head> tag of the generator
    if "<head>" in code:
        code = code.replace("<head>", "<head>\n" + og_and_schema_markup, 1)

    with open("batch_generator.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("SUCCESS: Updated batch_generator.py with FAQ JSON-LD Schema & Open Graph tags!")
else:
    print("INFO: batch_generator.py already contains Schema and OG tags.")

