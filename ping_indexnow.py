import glob
import json
import urllib.request
import ssl

HOST = "dawidmillenium-design.github.io"
KEY = "matchamaya2026indexnowkey"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

# 1. Create verification key file
with open(f"{KEY}.txt", "w", encoding="utf-8") as f:
    f.write(KEY)

print(f"✔ Created IndexNow key verification file: {KEY}.txt")

# 2. Collect all HTML URLs
html_files = glob.glob("*.html")
url_list = [f"https://{HOST}/matcha-maya-blog/{page}" for page in html_files]

# 3. Payload structure for IndexNow API
payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": url_list
}

data = json.dumps(payload).encode("utf-8")

# Send request to Bing / IndexNow Endpoint
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=data,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST"
)

try:
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx) as response:
        if response.status in [200, 202]:
            print(f"✔ Successfully pinged IndexNow API for {len(url_list)} URLs! (Status Code: {response.status})")
        else:
            print(f"⚠ Response status: {response.status}")
except Exception as e:
    print(f"ℹ API Ping notice: Key file needs to be live on GitHub Pages first before API validation. Exception: {e}")

print("--- INDEXNOW SETUP COMPLETE ---")