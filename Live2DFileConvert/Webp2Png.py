import json
from pathlib import Path
from PIL import Image

INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Live2D"

def webp_to_png(root: Path):
    """
    递归查找所有 webp 文件并转为 png
    """
    for webp_path in root.rglob("*.webp"):
        png_path = webp_path.with_suffix(".png")

        try:
            with Image.open(webp_path) as img:
                img = img.convert("RGBA")  # 保证透明通道
                img.save(png_path, "PNG")

                if png_path.exists():
                    webp_path.unlink()
                    print(f"[OK] {webp_path} -> {png_path}")
                else:
                    print(f"[WARN] PNG未生成: {png_path}")

        except Exception as e:
            print(f"[ERR] {webp_path}: {e}")

def fix_model3_json(root: Path):
    """
    修改 .model3.json 中 FileReferences.Textures
    把 .webp 改为 .png
    """
    for json_path in root.rglob("*.model3.json"):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            file_refs = data.get("FileReferences", {})
            textures = file_refs.get("Textures")

            if not textures:
                continue

            modified = False

            for i, tex in enumerate(textures):
                if tex.lower().endswith(".webp"):
                    new_tex = tex[:-5] + ".png"
                    textures[i] = new_tex
                    modified = True

            if modified:
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

                print(f"[FIXED] {json_path}")

        except Exception as e:
            print(f"[ERR] {json_path}: {e}")


def main():
    root = Path(INPUT_PATH)

    if not root.exists():
        print("路径不存在")
        return

    webp_to_png(root)
    fix_model3_json(root)


if __name__ == '__main__':
    main()