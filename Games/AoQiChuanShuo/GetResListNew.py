import requests

CONFIG_URL = "https://aoqi.100bt.com/h5/config/pet/petspineicon.json"
OUT_FILE = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\output.txt"

def main():
    # ID
    r = requests.get(CONFIG_URL, timeout=15)
    r.raise_for_status()
    ids = r.json()  # 期望是形如 [2872, 2947, ...] 的数组

    # 写入URL
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        for i in ids:
            url = f"https://aoqi.100bt.com/h5/peticon/spine/peticon{i}.mix"
            f.write(url + "\n")

    print(f"写入 {len(ids)} 条到 {OUT_FILE}")

if __name__ == "__main__":
    main()
