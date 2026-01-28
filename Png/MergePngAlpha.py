import os
from PIL import Image

# ===== 常量配置 =====
TARGET_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\new\assets\_wizardresources2\resources\jpn"          # 目标目录，改成你的路径
ALPHA_SUFFIXES = [
    "_alpha.png",
    "_A.png",
    "_a.png"
]

# ===================

def merge_alpha_images(root):
    for dirpath, _, filenames in os.walk(root):

        for filename in filenames:
            # 判断是否是 alpha 通道图
            matched_suffix = None
            for suffix in ALPHA_SUFFIXES:
                if filename.endswith(suffix):
                    matched_suffix = suffix
                    break

            if not matched_suffix:
                continue

            alpha_path = os.path.join(dirpath, filename)
            base_name = filename.replace(matched_suffix, ".png")
            base_path = os.path.join(dirpath, base_name)

            if not os.path.exists(base_path):
                print(f"缺少对应主图: {base_path}")
                continue

            try:
                base_img = Image.open(base_path).convert("RGBA")
                alpha_img = Image.open(alpha_path).convert("L")

                if base_img.size != alpha_img.size:
                    print(f"尺寸不一致，跳过: {base_path}")
                    continue

                r, g, b, _ = base_img.split()
                merged = Image.merge("RGBA", (r, g, b, alpha_img))

                merged.save(base_path)
                print(f"合并完成 -> {base_path}")

                os.remove(alpha_path)
                print(f"删除 alpha 图片 -> {alpha_path}")

            except Exception as e:
                print(f"失败: {alpha_path} -> {e}")

# 调用
merge_alpha_images(TARGET_DIR)
