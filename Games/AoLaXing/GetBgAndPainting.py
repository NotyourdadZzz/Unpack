import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ================== 配置 ==================

INPUT_TXT = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\output.txt")
OUTPUT_LH_TXT = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\output-lh.txt")

OUTPUT_BG_TXT = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\output-bg.txt")
BG_START_NUM = 0

# 并发与停止条件
WORKERS = 8
BATCH_SIZE = 20        
MAX_MISS = 150          # 阈值
TIMEOUT = 5

# =========================================

session = requests.Session()

# -------------------------------------------------
# 功能一：petmovie → newlarge 映射
# -------------------------------------------------

LH_RE = re.compile(r"petmovie(\d+)/petmovie\1\.json$")

def map_to_newlarge(url: str) -> str | None:
    m = LH_RE.search(url)
    if not m:
        return None
    num = m.group(1)
    return (
        "https://aola.100bt.com/h5/"
        f"peticon/newlarge/type1/peticon{num}/peticon{num}_1.png"
    )


def generate_output_lh():
    lines = INPUT_TXT.read_text(encoding="utf-8").splitlines()
    results = set()

    for line in lines:
        new_url = map_to_newlarge(line.strip())
        if new_url:
            results.add(new_url)

    with OUTPUT_LH_TXT.open("w", encoding="utf-8") as f:
        for u in sorted(results):
            f.write(u + "\n")

    print(f"[LH DONE] {len(results)} 条 → {OUTPUT_LH_TXT}")


# -------------------------------------------------
# 功能二：background 并发向后扫描
# -------------------------------------------------

def bg_url(num: int) -> str:
    return (
        "https://aola.100bt.com/h5/"
        f"pet/petskin/background/bg/img_petskinbackground_{num}.png"
    )


def bg_exists(num: int) -> bool:
    try:
        r = session.head(bg_url(num), timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 200:
            return True
        r = session.get(bg_url(num), stream=True, timeout=TIMEOUT)
        return r.status_code == 200
    except requests.RequestException:
        return False


def scan_bg_forward_concurrent(start: int) -> list[int]:
    found = []
    cur = start
    miss = 0

    print(f"[BG SCAN] start from {start}")

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        while True:
            batch = list(range(cur, cur + BATCH_SIZE))
            futures = {pool.submit(bg_exists, n): n for n in batch}

            hit_in_batch = False

            for f in as_completed(futures):
                n = futures[f]
                if f.result():
                    found.append(n)
                    hit_in_batch = True
                    miss = 0
                    print(f"[BG FOUND] {n}")

            if hit_in_batch:
                cur += BATCH_SIZE
            else:
                miss += BATCH_SIZE
                if miss >= MAX_MISS:
                    break
                cur += BATCH_SIZE

    return sorted(found)


def generate_output_bg():
    nums = scan_bg_forward_concurrent(BG_START_NUM)

    with OUTPUT_BG_TXT.open("w", encoding="utf-8") as f:
        for n in nums:
            f.write(bg_url(n) + "\n")

    print(f"[BG DONE] {len(nums)} 条 → {OUTPUT_BG_TXT}")


# -------------------------------------------------
# main
# -------------------------------------------------

def main():
    generate_output_lh()
    generate_output_bg()


if __name__ == "__main__":
    main()
