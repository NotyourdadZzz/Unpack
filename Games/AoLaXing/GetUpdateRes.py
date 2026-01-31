import re
import requests
from pathlib import Path

# ===== 配置 =====
TXT_PATH = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\output.txt")

BASE = "https://aola.100bt.com/h5"
DIR_FMT = "peticon/newbreath/petmovie{n}"
FILE_FMT = "petmovie{n}.{ext}"

EXTS = ("json", "atlas", "png")

TIMEOUT = 5
MAX_MISS = 50   # 连续不存在多少个才停止扩张
# ==================

session = requests.Session()

# ---------- URL 构造 ----------
def make_url(num: int, ext: str) -> str:
    return f"{BASE}/{DIR_FMT.format(n=num)}/{FILE_FMT.format(n=num, ext=ext)}"


# ---------- num 提取 ----------
NUM_RE = re.compile(r"petmovie(\d+)/petmovie\1\.(json|atlas|png)$")

def extract_num(url: str) -> int | None:
    m = NUM_RE.search(url)
    return int(m.group(1)) if m else None


# ---------- json 存在检测 ----------
def json_exists(num: int) -> bool:
    url = make_url(num, "json")
    try:
        r = session.head(url, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code == 200:
            return True
        r = session.get(url, stream=True, timeout=TIMEOUT)
        return r.status_code == 200
    except requests.RequestException:
        return False


# ---------- 补全已有编号的缺失文件 ----------
def fill_missing_files(nums: set[int]) -> set[str]:
    urls = set()
    for n in nums:
        for ext in EXTS:
            urls.add(make_url(n, ext))
    return urls


# ---------- 区间内部补洞 ----------
def fill_gaps(nums: set[int]) -> set[int]:
    found = set()
    lo, hi = min(nums), max(nums)

    print(f"[GAP SCAN] {lo} ~ {hi}")

    for n in range(lo, hi + 1):
        if n in nums:
            continue
        if json_exists(n):
            nums.add(n)
            found.add(n)
            print(f"[GAP FOUND] petmovie{n}")

    return found


# ---------- 向单方向扩张 ----------
def scan_linear(start: int, direction: int, nums: set[int]) -> set[int]:
    found = set()
    miss = 0
    cur = start + direction

    arrow = "↑" if direction > 0 else "↓"

    while cur > 0:
        if cur in nums:
            cur += direction
            continue

        if json_exists(cur):
            nums.add(cur)
            found.add(cur)
            miss = 0
            print(f"[EXT {arrow}] petmovie{cur}")
        else:
            miss += 1
            if miss >= MAX_MISS:
                break

        cur += direction

    return found


# ---------- main ----------
def main():
    lines = TXT_PATH.read_text(encoding="utf-8").splitlines()
    nums = {n for n in (extract_num(l) for l in lines) if n is not None}

    if not nums:
        print("output.txt 中无有效 petmovie")
        return

    print(f"[INIT] {min(nums)} ~ {max(nums)}")

    # 补全已有编号文件
    all_urls = fill_missing_files(nums)

    # 区间内部补洞
    fill_gaps(nums)

    # 向两端扩张
    scan_linear(max(nums), +1, nums)
    scan_linear(min(nums), -1, nums)

    # 重新生成完整 URL
    for n in nums:
        for ext in EXTS:
            all_urls.add(make_url(n, ext))

    # 写回 txt
    with TXT_PATH.open("w", encoding="utf-8") as f:
        for url in sorted(all_urls):
            f.write(url + "\n")

    print(f"[DONE] 共 {len(nums)} 个 petmovie，output.txt 已更新")


if __name__ == "__main__":
    main()
