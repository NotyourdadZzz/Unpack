
old_file = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\PathToNoWhere\ptn_old.txt"
new_file = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\PathToNoWhere\ptn.txt"
def load_set(path):
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())

old_set = load_set(old_file)
new_set = load_set(new_file)

new = sorted(new_set - old_set)
common = sorted(old_set & new_set)

print(f"new: {len(new)}")
print(f"common: {len(common)}")

with open("diff_only_in_new.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(new))

with open("diff_common.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(common))
