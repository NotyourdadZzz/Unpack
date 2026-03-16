import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== 常量配置 =====
INPUT_TXT = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\File\diff.txt"  # 输入 URL 列表
OUTPUT_DIR = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\File\output" # 输出目录
THREADS = 16                                        # 线程数
TIMEOUT = 15
# ==================

session = requests.Session()


def download_one(url: str) -> str:
    url = url.strip()
    if not url:
        return "SKIP"

    name = url.rstrip("/").split("/")[-1]
    path = os.path.join(OUTPUT_DIR, name)

    # 已存在直接跳过
    if os.path.exists(path):
        return f"SKIP: {name}"

    try:
        r = session.get(url, timeout=TIMEOUT)
        r.raise_for_status()

        with open(path, "wb") as f:
            f.write(r.content)

        return f"OK: {name}"
    except Exception as e:
        return f"FAIL: {name}  {e}"


def main():
    if not os.path.exists(INPUT_TXT):
        print(f"输入文件不存在: {INPUT_TXT}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(INPUT_TXT, "r", encoding="utf-8") as f:
        urls = [x.strip() for x in f if x.strip()]

    print(f"总计 {len(urls)} 条，线程数 {THREADS}，开始下载…")

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = [executor.submit(download_one, url) for url in urls]

        for future in as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    main()
