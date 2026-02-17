import requests

# ================== 基础配置 ==================
PATCHLIST_URL = "https://api.shziyi.com:12101/v1/gameconfig/patchlist"
CDN_BASE = "https://xonecn-hotupdatecdn.shziyi.com"
PLATFORM_PATH = "release-cn/android/tags/major"

BLOCKSIZE = 5
START_VERSION = 0   # <<< 起始版本

headers = {
    "User-Agent": "UnityPlayer/2019.4.40f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cache-Control": "max-age=0, no-cache, no-store",
    "X-Unity-Version": "2019.4.40f1",
}

data = {
    "region": 3,
    "channel": 2,
    "role": 1,
    "env": 3,
    "timestamp": 1768314246,
    "clientid": 1030,
    "sig": "bc157a80d03aa0df0b82eb2a219e756f",
    "lang": "zh",
}

# ================== Step 1: patchlist ==================
resp = requests.post(PATCHLIST_URL, headers=headers, data=data, timeout=10)
patchlist = resp.json()

hotfix_version = patchlist["game_config_patch"]["extra"]["hotfix_version"]
parts = hotfix_version.split(".")
major_version = ".".join(parts[:2])   # 2.3
minor_version = parts[2]              # 48
apk_url = patchlist["game_config_apk"]["apk_url"]

print(f"major_version: {major_version}")
print(f"minor_version: {minor_version}")
print(f"[APK] {apk_url}\n")

# ================== Step 2: res_releases.json ==================
releases_url = f"{CDN_BASE}/{PLATFORM_PATH}/{major_version}/latest/res_releases.json"
releases = requests.get(releases_url, timeout=10).json()

AssetsVersion = releases["Merges"][-1]["Version"]

print(f"[AssetsVersion] {AssetsVersion}\n")

# ================== Step 3: 生成 Patch URLs ==================
patch_urls = []

current = START_VERSION
while current < AssetsVersion:
    end = min(current + BLOCKSIZE, AssetsVersion)
    patch_urls.append(
        f"{CDN_BASE}/{PLATFORM_PATH}/{major_version}/patches/{current}_{end}.patch"
    )
    current = end

with open("PatchURLs.txt", "w", encoding="utf-8") as f:
    for url in patch_urls:
        f.write(url + "\n")

print(f"[PatchURLs] 生成 {len(patch_urls)} 条\n")

# ================== Step 4: 请求 patch.txt 并统计 ==================
total_file_count = 0
total_file_size = 0

print("Patch Detail:")
print("-" * 60)

for url in patch_urls:
    txt_url = url + ".txt"

    r = requests.get(txt_url, timeout=10)
    if r.status_code != 200 or r.text.strip() == "404":
        print(f"[SKIP] {txt_url}")
        continue

    info = r.json()
    file_count = info["FileCount"]
    file_size = info["FileSize"]

    total_file_count += file_count
    total_file_size += file_size

    print(
        f"{info['Filename']:12} | "
        f"FileCount: {file_count:5} | "
        f"FileSize: {file_size / 1024 / 1024:8.2f} MB"
    )

print("-" * 60)
print(f"[TOTAL] FileCount = {total_file_count}")
print(f"[TOTAL] FileSize  = {total_file_size / 1024 / 1024:.2f} MB")
