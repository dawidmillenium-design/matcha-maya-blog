import os
import glob
import urllib.request
import json

print("--- STARTING INDEXNOW PING AUTOMATION ---")

DOMAIN = "dawidmillenium-design.github.io"
BASE_URL = f"https://{DOMAIN}/matcha-maya-blog"
API_KEY = "a4b8c1d2e3f4567890abcdef12345678"
KEY_LOCATION = f"{BASE_URL}/{API_KEY}.txt"

# 1. Ensure verification key file exists
key_filename = f"{API_KEY}.txt"
if not os.path.exists(key_filename):
    with open(key_filename, "w", encoding="utf-8") as f:
        f.write(API_KEY)
    print(f"✔ Generated IndexNow verification key file: {key_filename}")

# 2. Gather target URLs
target_files = ["compare.html", "llms.txt", "hub.html"] + sorted(glob.glob("*-vs-*-digital-nomad.html"))
url_list = [f"{BASE_URL}/{f}" for f in target_files]

print(f"Found {len(url_list)} priority URLs to submit to IndexNow.")

# 3. Construct Payload
payload = {
    "host": DOMAIN,
    "key": API_KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": url_list
}

data = json.dumps(payload).encode("utf-8")
indexnow_url = "https://api.indexnow.org/indexnow"

# Headers including User-Agent to prevent 403 Forbidden blocks
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) MatchaMayaBot/1.0"
}

req = urllib.request.Request(indexnow_url, data=data, headers=headers)

try:
    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        if status_code in (200, 202):
            print(f"✔ Successfully pinged IndexNow! Status Code: {status_code}")
            print(f"✔ Submitted {len(url_list)} URLs for immediate crawling.")
        else:
            print(f"⚠️ IndexNow returned status code: {status_code}")
except Exception as e:
    print(f"❌ Error pinging IndexNow: {e}")