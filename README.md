# Fast DuckDuckGo Image Downloader

A high-performance, multi-threaded Python script to scrape and download images from DuckDuckGo search results. It bypasses basic rate limits and uses parallel processing to maximize download speed.

## Features

* **Multi-threaded Downloading:** Uses `ThreadPoolExecutor` to download multiple images simultaneously.
* **Safe Search Toggle:** Configured to `safesearch="off"` by default for broader results.
* **Resilient:** Includes retry logic for rate limits and connection timeouts.
* **Simple CLI:** Interactive command-line interface for quick usage.
* **Organized:** Automatically creates folders based on your search query.

## Prerequisites

* Python 3.8 or higher
* Pip (Python Package Installer)

## Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/PaperCodeGithub/fast-ddg-images.git](https://github.com/PaperCodeGithub/fast-ddg-images.git)
    cd fast-ddg-images
    ```

2.  **Set up a Virtual Environment (Optional but Recommended)**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

    > **Note:** This script relies on the `duckduckgo-search` library. If you encounter import errors, ensure you have the latest version installed.

## Usage

Run the script using Python:

```
python main.py
```

### Steps:
1. Enter your search prompt when asked (e.g., "futuristic cyberpunk city").
2. Enter the number of images you want to download (e.g., 50).
3. The script will create a folder named after your prompt and save the images there.

## Code Overview
- ```safe_ddg_images ``` Wraps the search functionality with retry logic to handle potential HTTP 429 (Rate Limit) errors.
- ``` download_images_fast ``` The core function that fetches URLs and dispatches them to a thread pool.
- ``` ThreadPoolExecutor ``` Currently set to max_workers=10. You can increase this in the code if you have a high-bandwidth connection.
## Disclaimer
This script is for educational purposes only. Please respect copyright laws and the Terms of Service of the websites you scrape. Do not use this tool to overload servers or for malicious intent.

