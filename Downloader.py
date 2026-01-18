import os
import time
import random
import requests
import threading
from ddgs import DDGS
from concurrent.futures import ThreadPoolExecutor, as_completed


# ------------------------
# Download a single image
# ------------------------

def download_image(url, filepath, index):
    try:
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"[{index+1}] ✅ Saved: {filepath}")
        else:
            print(f"[{index+1}] ❌ Failed: HTTP {response.status_code}")
    except Exception as e:
        print(f"[{index+1}] ❌ Error: {e}")


# ------------------------
# Safe image search with retries
# ------------------------

def safe_ddg_images(ddgs, query, max_results):
    for attempt in range(5):  # retry up to 5 times
        try:
            return list(ddgs.images(
                query,
                max_results=max_results,
                safesearch="off",
                region="wt-wt"
            ))
        except Exception as e:
            wait = 2 ** attempt + random.random()
            print(f"⚠️ Rate limited, retrying in {wait:.1f} sec... ({e})")
            time.sleep(wait)
    return []


# ------------------------
# Main download function
# ------------------------
def download_images_fast(query, max_results=30, save_dir="Default"):
    os.makedirs(save_dir, exist_ok=True)
    print(f"\n🔍 Searching images for: {query} ...")

    with DDGS() as ddgs:
        results = list(ddgs.images(
            query,
            max_results=max_results,
            safesearch="off",   # ✅ disables safe search
            region="wt-wt"
        ))

    if not results:
        print("❌ No results found or blocked by rate limit.")
        return

    # Use a thread pool for faster parallel downloading
    with ThreadPoolExecutor(max_workers=10) as executor:  # adjust max_workers as needed
        futures = []
        for i, result in enumerate(results):
            url = result.get("image")
            if not url:
                continue

            ext = url.split(".")[-1].split("?")[0].lower()
            if len(ext) > 5 or "/" in ext:
                ext = "jpg"

            filename = f"{query.replace(' ', '_')}_{i}.{ext}"
            filepath = os.path.join(save_dir, filename)

            futures.append(executor.submit(download_image, url, filepath, i))

        # Wait for all threads to finish
        for future in as_completed(futures):
            pass

    print(f"\n✅ Finished downloading {len(results)} images into '{save_dir}/'.")


# ------------------------
# Run as script
# ------------------------
if __name__ == "__main__":
    while True:
        keyword = input("\nPrompt: ")
        count = input("Number: ")

        try:
            count = int(count)
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        download_images_fast(keyword, max_results=count, save_dir=keyword)
