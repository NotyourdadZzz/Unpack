import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

INPUT_FILE = r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\output-bg.txt"
MAX_WORKERS = 32
TIMEOUT = 5
REPORT_EVERY = 200

headers = {
    "User-Agent": "Mozilla/5.0"
}

def is_url_valid(url: str) -> tuple[str, bool, str]:
    """
    返回 (url, 是否有效, 错误原因)
    """
    try:
        r = requests.head(url, timeout=TIMEOUT, allow_redirects=True, headers=headers)
        if r.status_code < 400:
            return url, True, ""
        return url, False, f"HTTP {r.status_code}"
    except Exception:
        try:
            r = requests.get(url, timeout=TIMEOUT, stream=True, headers=headers)
            if r.status_code < 400:
                return url, True, ""
            return url, False, f"HTTP {r.status_code}"
        except Exception as e:
            return url, False, str(e)

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    total = len(urls)
    checked = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(is_url_valid, url): url for url in urls}

        for future in as_completed(futures):
            url, ok, reason = future.result()
            checked += 1

            if not ok:
                print(f"[INVALID] {url}  -> {reason}")

            if checked % REPORT_EVERY == 0 or checked == total:
                print(f"[PROGRESS] Checked {checked}/{total} URLs")

if __name__ == "__main__":
    main()
