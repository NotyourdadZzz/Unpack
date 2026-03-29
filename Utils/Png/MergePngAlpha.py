import os
from PIL import Image

# ===== 常量配置 =====
TARGET_DIR = r"D:\Tools\UsefulTools\MuMu\Shared\Download\1\base\guider"          # 目标目录，改成你的路径
BASE_EXTENSIONS = [".png", ".jpg", ".jpeg", ".webp"]
ALPHA_SUFFIXES = [
    "_alpha.png",
    "_a.png"
]

# ===================

def merge_alpha_images(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:

            matched_suffix = None
            for suffix in ALPHA_SUFFIXES:
                if filename.endswith(suffix):
                    matched_suffix = suffix
                    break

            if not matched_suffix:
                continue

            alpha_path = os.path.join(dirpath, filename)
            pure_name = filename[:-len(matched_suffix)]

            # 找主图
            base_path = None
            for ext in BASE_EXTENSIONS:
                temp = os.path.join(dirpath, pure_name + ext)
                if os.path.exists(temp):
                    base_path = temp
                    break

            if not base_path:
                print(f"缺少主图: {pure_name}")
                continue

            target_png = os.path.join(dirpath, pure_name + ".png")

            if os.path.exists(target_png):
                print(f"已存在，跳过: {pure_name}")
                continue

            try:
                with Image.open(base_path) as base_img, Image.open(alpha_path) as alpha_img:
                    base_img = base_img.convert("RGB")
                    alpha_img = alpha_img.convert("L")

                    if base_img.size != alpha_img.size:
                        alpha_img = alpha_img.resize(base_img.size, resample=Image.Resampling.BILINEAR)

                    r, g, b = base_img.split()
                    merged = Image.merge("RGBA", (r, g, b, alpha_img))

                    merged.save(target_png, "PNG")
                    print(f"合并成功 -> {target_png}")

                # 删除旧文件
                if base_path != target_png:
                    os.remove(base_path)

                os.remove(alpha_path)

            except Exception as e:
                print(f"失败: {filename} -> {e}")

merge_alpha_images(TARGET_DIR)
