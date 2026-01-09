import json
from pathlib import Path

def skel_merge(info_dir, bundles_dir, output_root):
    info_path = Path(info_dir)
    bundles_path = Path(bundles_dir)
    output_root_path = Path(output_root)

    # 遍历所有 JSON 索引文件
    for json_file in info_path.rglob("*_aniInfo.json"):
        try:
            with open(json_file, "r", encoding="utf8") as f:
                data = json.load(f)

            # 1. 确定名称（去掉后缀）
            # 例如: character_aniInfo -> character
            base_name = json_file.name.replace("_aniInfo.json", "")
            skel_filename = base_name + ".skel"
            
            # 2. 创建父级目录：output/character/
            # parents=True 确保多层级目录也能创建，exist_ok=True 防止目录已存在时报错
            file_parent_dir = output_root_path / base_name
            file_parent_dir.mkdir(parents=True, exist_ok=True)

            # 3. 解析 MD5 对应的碎片路径
            base_file_path = bundles_path / (data["_baseBytesMd5"] + ".u2d")
            ani_file_path = bundles_path / (data["_aniBytesMd5"] + ".u2d")

            # 4. 检查并合并
            if base_file_path.exists() and ani_file_path.exists():
                content = base_file_path.read_bytes() + ani_file_path.read_bytes()
                
                # 最终路径示例：output/character/character.skel
                target_path = file_parent_dir / skel_filename
                target_path.write_bytes(content)
                
                print(f"成功导出: {target_path}")
            else:
                print(f"跳过 {base_name}: 缺少 .u2d 数据碎片")

        except Exception as e:
            print(f"处理 {json_file.name} 时出错: {e}")

if __name__ == '__main__':
    # ================= 配置区域 =================
    INFO_DIR = r"D:\Games\GameUnpackAssets\mymodel\Spine\XiYou BiHuiXiXing\Spine\assets\objects\spine\hero_live"
    BUNDLES_DIR = r"C:\Users\86182\Downloads\bundles"
    OUTPUT_DIR = r"D:\Games\GameUnpackAssets\mymodel\Spine\XiYou BiHuiXiXing\Spine\assets\objects\spine\hero_live"
    # ============================================

    skel_merge(INFO_DIR, BUNDLES_DIR, OUTPUT_DIR)