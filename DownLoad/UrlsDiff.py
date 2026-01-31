from pathlib import Path

# ====== 配置 ========
FILE1 = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\File\output.txt"
FILE2 = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\File\outputOld.txt"
OUT_FILE = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\File\diff.txt"
# ====================

def read_lines(path):
    return {
        line.strip()
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    }

def main():
    s1 = read_lines(FILE1)
    s2 = read_lines(FILE2)

    only_in_1 = sorted(s1 - s2)
    only_in_2 = sorted(s2 - s1)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"只在 {FILE1} 中有 ({len(only_in_1)} 条):\n")
        for x in only_in_1:
            f.write(x + "\n")

        f.write(f"\n只在 {FILE2} 中有 ({len(only_in_2)} 条):\n")
        for x in only_in_2:
            f.write(x + "\n")

    print(f"已写入 {OUT_FILE}")

if __name__ == "__main__":
    main()
