# coding=utf-8
import json
import shutil
from pathlib import Path

INPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\res")
OUTPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Spine")

# 所有的骨骼和纹理集被绑定在了 import 里面的json
# 搜索所有的json 找到 type 为sp.SkeletonData 的json "__type__": "sp.SkeletonData"
# 然后 "_name": "arm_spine_ene10005_v2",是模型名称
# "skeletonJsonStr" 键的值是骨骼数据的json字符串,  "{\"skeleton\":{\"hash\"... 其中 \ 是转义字符. 直接删除就可以
# "_atlasText" 键的值是纹理集数据的字符串, "\narm_spine_ene10005_v2.png\nsize:... 其中 \n 是换行符, 直接替换成换行就可以
# "textures": [{ "__uuid__": "15alocojdEuoPKrUvUhTSQ" }], 这里的uuid是 22位的, 展开为36位就是对应贴图名称
# "textureNames": ["arm_spine_ene10005_v2.png"] 贴图的名称, 直接从这里获取就可以了
COMPRESS_JSON = True
BASE64_KEYS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
BASE64_MAP = {c: i for i, c in enumerate(BASE64_KEYS)}
def decompress_uuid22(base64_str):
    """
    解压: 将 22位 Cocos 压缩 ID 转换为标准 36位 UUID
    """
    if len(base64_str) != 22:
        return base64_str
    uuid_chars = [base64_str[:2]]
    for i in range(2, 22, 2):
        lhs = BASE64_MAP[base64_str[i]]
        rhs = BASE64_MAP[base64_str[i + 1]]
        val = (lhs << 6) | rhs
        uuid_chars.append(f"{val:03x}")
    hex_str = "".join(uuid_chars)
    return f"{hex_str[:8]}-{hex_str[8:12]}-{hex_str[12:16]}-{hex_str[16:20]}-{hex_str[20:]}"

def compress_json(json_str: str) -> str:
    if not COMPRESS_JSON:
        return json_str
    data = json.loads(json_str)
    return json.dumps(data,separators=(",",":"))

def build_texture_index(root: Path):
    index = {}
    for p in root.rglob("*"):
        if p.suffix.lower() not in (".png", ".jpg", ".webp", ".pkm"):
            continue
        name = p.stem.lower()
        index[name] = p
    return index

texture_index = build_texture_index(INPUT_PATH)

def find_texture(uuid36: str):
    return texture_index.get(uuid36.lower())

def process_json(json_path: Path):
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except OSError:
        return
    if not isinstance(data, dict):
        return
    if data.get("__type__") != "sp.SkeletonData":
        return

    spine_name = data.get("_name", json_path.stem)
    print(f"[FOUND] {spine_name}")

    out_dir = OUTPUT_PATH / spine_name
    out_dir.mkdir(parents=True, exist_ok=True)

    # ===== 1. skeleton json =====
    skel_str = data.get("skeletonJsonStr")
    if skel_str:
        skel_json = skel_str.replace('\\"', '"')
        skel_json = skel_json.replace("\\n", "\n")

        try:
            # 格式化
            obj = json.loads(skel_json)
            skel_json = json.dumps(obj, ensure_ascii=False, indent=2)
        except OSError:
            pass

        skel_json = compress_json(skel_json)
        (out_dir / f"{spine_name}.json").write_text(skel_json, encoding="utf-8")


    # ===== 2. atlas =====
    atlas_text = data.get("_atlasText")
    if atlas_text:
        atlas_text = atlas_text.replace("\\n", "\n")
        (out_dir / f"{spine_name}.atlas").write_text(atlas_text, encoding="utf-8")


    # ===== 3. 贴图 =====
    texture_names = data.get("textureNames", [])
    textures = data.get("textures", [])

    for i, tex in enumerate(textures):
        uuid22 = tex.get("__uuid__")
        if not uuid22:
            continue

        uuid36 = decompress_uuid22(uuid22)

        tex_path = find_texture(uuid36)

        if not tex_path:
            print(f"  [MISS] texture uuid: {uuid36}")
            continue

        if i < len(texture_names):
            real_suffix = tex_path.suffix.lower()
            tex_name = texture_names[i]
            name_suffix = Path(tex_name).suffix.lower()

            if name_suffix and name_suffix == real_suffix:
                out_name = tex_name
            else:
                base = Path(tex_name).stem
                out_name = base + real_suffix
        else:
            out_name = tex_path.name

        dst = out_dir / out_name
        shutil.copy2(tex_path, dst)

        print(f"  [OK] texture -> {dst}")


def main():
    # 递归搜索所有json文件, 找到type为sp.SkeletonData的json, 解析出骨骼数据和纹理集数据, 重命名为"_name"的值, 拓展名分别为.json 和 .atlas 保存到输出目录
    # 然后通过 "textures" 的uuid22 解压为uuid36 在输入目录下找到对应的贴图, 同样重命名, 移动到输出目录
    json_files = list(INPUT_PATH.rglob("*.json"))

    for jp in json_files:
        process_json(jp)

    print("Done.")


if __name__ == "__main__":
    main()