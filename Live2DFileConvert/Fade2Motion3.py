import os
import json
import re
from pathlib import Path

INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Live2D\SteamGame\MorningMist\Live2D\Test"
OUTPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Live2D\SteamGame\MorningMist\Live2D\Output"

FADE_REGEX = re.compile(r'.*\.fade(\s*[#@]-?\d+)?\.json$')  # 匹配 .fade.json 或 .fade @xxxx.json 或 .fade #xxxx.json
IsHash = False
os.makedirs(OUTPUT_PATH, exist_ok=True)


def convert_segments(curve):
    """
    每个点依次写入 [time, value, weightedMode]，最后移除末尾 weightedMode。
    输出长度为 3*n-1（n>=1），空曲线输出空列表。
    """
    segments = []
    for pt in curve:
        segments.append(pt.get("time", 0))
        segments.append(pt.get("value", 0))
        segments.append(pt.get("weightedMode", 0))

    if segments:
        segments.pop()

    return segments


def build_output_path(output_root, obj, fallback_file_name):
    motion_name = str(obj.get("MotionName", "")).strip()
    if motion_name:
        motion_name = motion_name.replace("\\", "/").lstrip("/")
        normalized = os.path.normpath(motion_name)
        if not os.path.isabs(normalized) and not normalized.startswith(".."):
            return Path(output_root) / normalized

    return Path(output_root) / f"{fallback_file_name}.motion3.json"

def process_fade_files(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not FADE_REGEX.match(file):
                continue
            file_name = os.path.splitext(file)[0]  # 去掉 .json
            file_name = re.sub(r'\.fade', '', file_name)  # 去掉 .fade
            with open(file_path, 'r', encoding='utf-8') as f:
                obj = json.load(f)

            motion3_json = {
                "Version": 3,
                "Meta": {
                    "Duration": 0.0,
                    "Fps": 60.0,
                    "Loop": True,
                    "AreBeziersRestricted": True,
                    "CurveCount": 0,
                    "TotalSegmentCount": 0,
                    "TotalPointCount": 0,
                    "UserDataCount": 1,
                    "TotalUserDataSize": 0
                },
                "Curves": [],
                "UserData": [{"Time": 0.0, "Value": ""}]
            }

            total_segment_count = 0
            max_time = 0.0
            param_ids = obj.get("ParameterIdHashes") if IsHash else obj.get("ParameterIds", [])

            for i, curve_obj in enumerate(obj.get("ParameterCurves", [])):
                curve = curve_obj.get("m_Curve", [])
                segments = convert_segments(curve)
                total_segment_count += len(curve_obj.get("m_Curve", []))
                if curve:
                    max_time = max(max_time, curve[-1].get("time", 0))
                motion3_json["Curves"].append({
                    "Target": "Parameter",
                    "Id": param_ids[i] if i < len(param_ids) else "",
                    "Segments": segments
                })

            motion3_json["Meta"]["CurveCount"] = len(param_ids)
            motion3_json["Meta"]["Duration"] = max_time
            motion3_json["Meta"]["TotalSegmentCount"] = total_segment_count
            motion3_json["Meta"]["TotalPointCount"] = len(param_ids) + total_segment_count

            out_path = build_output_path(OUTPUT_PATH, obj, file_name)
            out_path.parent.mkdir(parents=True, exist_ok=True)

            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(motion3_json, f, ensure_ascii=False, indent=4)
            print(f"{out_path}")

process_fade_files(INPUT_PATH)