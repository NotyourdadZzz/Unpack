import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== 配置 =====
TXT_PATH = Path("C:/Users/86182/Downloads/output.txt")
BASE_URL = "https://aoqi.100bt.com/h5/peticon/spine/"
PREFIX = "peticon"
SUFFIX = ".mix"

STEP = 150          # 每次扩张步长
TIMEOUT = 5
WORKERS = 6         # 并发线程数
# ==================

session = requests.Session()


def extract_num(url: str) -> int:
    m = re.search(r'peticon(\d+)\.mix$', url)
    return int(m.group(1)) if m else -1


def make_url(num: int) -> str:
    return f"{BASE_URL}{PREFIX}{num}{SUFFIX}"


def resource_exists(num: int) -> int | None:
    """
    存在返回 num，不存在返回 None
    """
    try:
        r = session.head(make_url(num), timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 200:
            return num
        r = session.get(make_url(num), stream=True, timeout=TIMEOUT)
        if r.status_code == 200:
            return num
    except requests.RequestException:
        pass
    return None


def scan_up(start_max: int, existing: set[int]) -> list[int]:
    """
    向上扩张扫描（并发）
    """
    found_all = []
    offset = STEP

    while True:
        seg_start = start_max + offset - STEP + 1
        seg_end = start_max + offset

        print(f"[SCAN ↑] {seg_start} ~ {seg_end}")

        block = [
            i for i in range(seg_start, seg_end + 1)
            if i not in existing
        ]

        found = []

        with ThreadPoolExecutor(max_workers=WORKERS) as pool:
            futures = [pool.submit(resource_exists, i) for i in block]

            for f in as_completed(futures):
                res = f.result()
                if res is not None:
                    existing.add(res)
                    found.append(res)
                    found_all.append(res)
                    print(f"[INSERT ↑] peticon{res}")

        if not found:
            break

        offset += STEP

    return found_all


def main():
    lines = TXT_PATH.read_text(encoding="utf-8").splitlines()
    nums = sorted(extract_num(line) for line in lines)
    nums = [n for n in nums if n != -1]

    if not nums:
        print("txt 无有效数据")
        return

    existing = set(nums)
    MIN = nums[0]
    MAX = nums[-1]

    print(f"MIN = {MIN}, MAX = {MAX}")

    new_nums = scan_up(MAX, existing)

    if not new_nums:
        print("未发现新增资源")
        return

    # ===== 写回 txt（完全按序号）=====
    all_nums = sorted(existing)
    with TXT_PATH.open("w", encoding="utf-8") as f:
        for n in all_nums:
            f.write(make_url(n) + "\n")

    print(f"\n新增 {len(new_nums)} 个资源，txt 已更新")
    print(f"新区间：{all_nums[0]} ~ {all_nums[-1]}")


if __name__ == "__main__":
    main()
