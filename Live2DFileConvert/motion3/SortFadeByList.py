# 导出fade文件时，确保File name format 是 asset name@pathlD的形式
# 例如导出了 【表情】默认.fade @4106.json 通过Fade2Motion.py 转为motion3
# 得到【表情】默认 @4106.motion3.json 
# 每个模型都有一个 .fadeMotionList文件，通过 
# "CubismFadeMotionObjects" > "m_PathID" 来区分该fade动作属于哪个模型
# 根据经验来看这个键 "CubismFadeMotionObjects" 不是固定的, 还见过 "motionsData"
import os
import json
import re
import shutil
# 使用前需要先把 .fade 文件转为 .motion3.json 文件, 通过 Fade2Motion.py 转换
INPUT_PATH = r"C:\Users\86182\Downloads\SKETCHY MASSAGE-2.0\Photo\Motion"
OUTPUT_PATH = r"C:\Users\86182\Downloads\SKETCHY MASSAGE-2.0\Photo\Moc3_Output"
FADE_KEY = "CubismFadeMotionObjects" # 根据实际情况修改为正确的键名(motionsList中记录所有动作信息pathId的键)


DRY_RUN = False
os.makedirs(OUTPUT_PATH, exist_ok=True)

def extract_model_name(filename):
    """从 fadeMotionList 文件名中提取模型名称"""
    # 匹配 "模型名.fadeMotionList @xxxx.json" 或 "模型名.fadeMotionList.json"
    match = re.match(r'(.+?)\.fadeMotionList(?:\s*@\d+)?\.json$', filename)
    if match:
        return match.group(1)
    return None

def extract_motion_name_and_pathid(filename):
    """从 motion3 文件名中提取动作名称和 pathID"""
    # 匹配 "动作名 @xxxx.motion3.json"
    match = re.match(r'(.+?)\s*@(\d+)\.motion3\.json$', filename)
    if match:
        return match.group(1), match.group(2)
    return None, None

def process_fade_motion_lists():
    """处理所有 fadeMotionList 文件"""
    # 查找所有包含 fadeMotionList 的文件
    fade_list_files = []
    for file in os.listdir(INPUT_PATH):
        if 'fadeMotionList' in file and file.endswith('.json'):
            fade_list_files.append(file)
    
    if not fade_list_files:
        print("未找到 fadeMotionList 文件")
        return
    
    # 预先扫描所有 motion3 文件
    motion3_files = {}
    for file in os.listdir(INPUT_PATH):
        if 'motion3' in file and file.endswith('.json'):
            motion_name, path_id = extract_motion_name_and_pathid(file)
            if path_id:
                motion3_files[path_id] = file
    
    # 处理每个 fadeMotionList 文件
    for fade_file in fade_list_files:
        model_name = extract_model_name(fade_file)
        if not model_name:
            print(f"跳过: {fade_file}")
            continue
        
        print(f"\n处理: {model_name}")
        
        # 读取 fadeMotionList 文件
        fade_file_path = os.path.join(INPUT_PATH, fade_file)
        print(f"读取: {fade_file_path}")
        try:
            with open(fade_file_path, 'r', encoding='utf-8') as f:
                fade_data = json.load(f)
        except Exception as e:
            print(f"读取失败: {e}")
            continue
        
        # 提取所有 m_PathID
        fade_objects = fade_data.get(FADE_KEY, [])
        if not fade_objects:
            print(f"未找到 {FADE_KEY} 键或列表为空")
            continue
        
        path_ids = [str(obj.get("m_PathID")) for obj in fade_objects if obj.get("m_PathID")]
        print(f"找到 {len(path_ids)} 个 PathID")
        # 创建目标目录
        target_dir = os.path.join(OUTPUT_PATH, model_name, "motions")
        if not DRY_RUN:
            os.makedirs(target_dir, exist_ok=True)
        
        # 处理每个 PathID 对应的 motion3 文件
        moved_count = 0
        for path_id in path_ids:
            if path_id in motion3_files:
                source_file = motion3_files[path_id]
                source_path = os.path.join(INPUT_PATH, source_file)
                
                # 提取动作名称并生成新文件名
                motion_name, _ = extract_motion_name_and_pathid(source_file)
                new_filename = f"{motion_name}.motion3.json"
                target_path = os.path.join(target_dir, new_filename)
                
                if DRY_RUN:
                    print(f"  [模拟] {new_filename}")
                else:
                    try:
                        shutil.move(source_path, target_path)
                        print(f"  {new_filename}")
                        moved_count += 1
                    except Exception as e:
                        print(f"  移动失败: {e}")
        
        if not DRY_RUN:
            print(f"完成: {moved_count}/{len(path_ids)}")

if __name__ == "__main__":
    print(f"输入: {INPUT_PATH}")
    print(f"输出: {OUTPUT_PATH}")
    print(f"{'[模拟模式]' if DRY_RUN else '[执行模式]'}\n")
    
    process_fade_motion_lists()
    
    print("\n完成")
