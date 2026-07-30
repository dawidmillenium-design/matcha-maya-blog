import os
import glob
import urllib.request
import json

print("--- STARTING INDEXNOW PING AUTOMATION ---")

DOMAIN = "dawidmillenium-design.github.io"
BASE_URL = f"https://{DOMAIN}/matcha-maya-blog"
API_KEY = "a4b8c1d2e3f4567890abcdef12345678"  # 32-character hex key
KEY_LOCATION = f"{BASE_URL}/{API_KEY}.txt"

# 1. Ensure IndexNow key file exists locally
key_filename = f"{API_KEY}.txt"
if not os.path.exists(key_filename):
    with open(key_filename, "w", encoding="utf-8") as f:
        f.write(API_KEY)
    print(f"✔ Generated IndexNow verification key file: {key_filename}")

# 2. Gather target URLs (compare.html + all comparison guides)
target_files = ["compare.html", "llms.txt", "hub.html"] + sorted(glob.glob("*-vs-*-digital-nomad.html"))
url_list = [f"{BASE_URL}/{f}" for f in target_files]

print(f"Found {len(url_list)} priority URLs to submit to IndexNow.")

# 3. Construct IndexNow Payload
payload = {
    "host": DOMAIN,
    "key": API_KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": url_list
}

data = json.dumps(payload).encode("utf-8")

# 4. Send POST request to Bing/IndexNow Endpoint
indexnow_url = "https://api.indexnow.org/indexnow"

req = urllib.request.Request(
    indexnow_url,
    data=data,
    headers={"Content-Type": "application/json; charset=utf-8"}
)

try:
    with urllib.request.urlopen(req) as response:
        status_code = response.getcode()
        if status_code in (200, 202):
            print(f"✔ Successfully pinged IndexNow! Status Code: {status_code}")
            print(f"✔ Submitted {len(url_list)} URLs for immediate crawling across Bing & participating search engines.")
        else:
            print(f"⚠️ IndexNow returned status code: {status_code}")
except Exception as e:
    print(f"❌ Error pinging IndexNow: {e}")