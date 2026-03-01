"""
CDN 版本号爆破脚本
目标：检测 {BASE_URL}/{PREFIX}.{VERSION}/hot_file_list.dat 是否存在
"""
import asyncio
import aiohttp
import os
from datetime import datetime

# ========== 配置区 ==========
BASE_URL    = "http://kanojo-jp-cdncf.y2sgames.com/kanojo-jp"
CHECK_FILE  = "hot_file_list.dat"
OUTPUT_DIR  = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\Games\SuperDimensionGF\Data"
OUTPUT_LOG  = os.path.join(OUTPUT_DIR, "VERSION.log")

# 起始版本（用于确定前缀段）
START_VERSION = "1.0.1520"

# 爆破模式：
#   1 = 只爆破最后一段         e.g. 1.0.XXXX  (4位, 0000~9999)
#   2 = 爆破后两段             e.g. 1.XXX.XXXX (3位+4位)
#   3 = 爆破后三段             e.g. X.XXX.XXXX (1位+3位+4位)
BRUTE_MODE  = 1

# 各段的爆破范围 [min, max]（含）
RANGE_SEG1  = (0, 9)       # 模式3：第一段
RANGE_SEG2  = (0, 9)       # 模式2/3：第二段
RANGE_SEG3  = (1000, 1700) # 模式1/2/3：最后一段（最主要的爆破段）

# 并发数
CONCURRENCY = 50
# 超时（秒）
TIMEOUT     = 8
# ========== 配置区结束 ==========


def gen_versions() -> list[str]:
    """根据 BRUTE_MODE 和 START_VERSION 生成待测版本列表"""
    parts = START_VERSION.split('.')
    versions = []

    if BRUTE_MODE == 1:
        # 固定前两段，爆破最后一段
        prefix = '.'.join(parts[:2])  # "1.0"
        for v in range(RANGE_SEG3[0], RANGE_SEG3[1] + 1):
            versions.append(f"{prefix}.{v}")

    elif BRUTE_MODE == 2:
        # 固定第一段，爆破后两段
        prefix = parts[0]  # "1"
        for s2 in range(RANGE_SEG2[0], RANGE_SEG2[1] + 1):
            for s3 in range(RANGE_SEG3[0], RANGE_SEG3[1] + 1):
                versions.append(f"{prefix}.{s2}.{s3}")

    elif BRUTE_MODE == 3:
        # 三段全爆破
        for s1 in range(RANGE_SEG1[0], RANGE_SEG1[1] + 1):
            for s2 in range(RANGE_SEG2[0], RANGE_SEG2[1] + 1):
                for s3 in range(RANGE_SEG3[0], RANGE_SEG3[1] + 1):
                    versions.append(f"{s1}.{s2}.{s3}")

    return versions


async def check_version(session: aiohttp.ClientSession,
                         sem: asyncio.Semaphore,
                         version: str) -> str | None:
    url = f"{BASE_URL}/{version}/{CHECK_FILE}"
    async with sem:
        try:
            async with session.head(url, timeout=aiohttp.ClientTimeout(total=TIMEOUT),
                                    allow_redirects=True) as resp:
                if resp.status == 200:
                    print(f"  [FOUND] {version}")
                    return version
                return None
        except Exception:
            return None


async def main():
    versions = gen_versions()
    print(f"爆破模式: {BRUTE_MODE}  |  待测版本数: {len(versions)}")
    print(f"基准URL: {BASE_URL}/{{version}}/{CHECK_FILE}\n")

    sem = asyncio.Semaphore(CONCURRENCY)
    found = []

    connector = aiohttp.TCPConnector(limit=CONCURRENCY)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [check_version(session, sem, v) for v in versions]
        results = await asyncio.gather(*tasks)

    found = sorted([r for r in results if r], key=lambda v: list(map(int, v.split('.'))))

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_LOG, 'w', encoding='utf-8') as f:
        f.write(f"# 爆破时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"# 基准URL:  {BASE_URL}\n")
        f.write(f"# 检测文件: {CHECK_FILE}\n")
        f.write(f"# 有效版本数: {len(found)}\n\n")
        for v in found:
            f.write(v + '\n')

    print(f"\n爆破完成，找到 {len(found)} 个有效版本")
    print(f"结果已保存到: {OUTPUT_LOG}")


if __name__ == "__main__":
    asyncio.run(main())