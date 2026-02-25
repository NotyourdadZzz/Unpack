import os
import json
import re
from pathlib import Path

INPUT_PATH = r"C:\Users\86182\Downloads\TEMP"
OUTPUT_PATH = r"C:\Users\86182\Downloads\OUTPUT"

FADE_REGEX = re.compile(r'.*\.fade(\s*@-?\d+)?\.json$')  # 匹配 .fade.json 或 .fade @xxxx.json
IsHash = False
os.makedirs(OUTPUT_PATH, exist_ok=True)


def convert_to_bezier(curve):
    """
    将线性曲线点列表转换为贝塞尔形式
    curve: [{"time": ..., "value": ...}, ...]
    输出 segments: [time, value, inTangent, outTangent, time, value, ...]
    """
    segments = []
    n = len(curve)
    for i, pt in enumerate(curve):
        time = pt.get("time", 0)
        value = pt.get("value", 0)
        if n == 1:
            inT = outT = 0
        elif i == 0:
            next_pt = curve[i+1]
            outT = (next_pt["value"] - value) / max(next_pt["time"] - time, 1e-6)
            inT = 0
        elif i == n-1:
            prev_pt = curve[i-1]
            inT = (value - prev_pt["value"]) / max(time - prev_pt["time"], 1e-6)
            outT = 0
        else:
            prev_pt = curve[i-1]
            next_pt = curve[i+1]
            inT = (value - prev_pt["value"]) / max(time - prev_pt["time"], 1e-6)
            outT = (next_pt["value"] - value) / max(next_pt["time"] - time, 1e-6)
        segments.extend([time, value, inT, outT])
    return segments

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
                segments = convert_to_bezier(curve_obj.get("m_Curve", []))
                total_segment_count += len(curve_obj.get("m_Curve", []))
                if segments:
                    max_time = max(max_time, curve_obj.get("m_Curve", [])[-1].get("time", 0))
                motion3_json["Curves"].append({
                    "Target": "Parameter",
                    "Id": param_ids[i] if i < len(param_ids) else "",
                    "Segments": segments
                })

            motion3_json["Meta"]["CurveCount"] = len(param_ids)
            motion3_json["Meta"]["Duration"] = max_time
            motion3_json["Meta"]["TotalSegmentCount"] = total_segment_count
            motion3_json["Meta"]["TotalPointCount"] = len(param_ids) + total_segment_count

            out_path = os.path.join(Path(OUTPUT_PATH), f"{file_name}.motion3.json")

            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(motion3_json, f, ensure_ascii=False, indent=4)
            print(f"{out_path}")

process_fade_files(INPUT_PATH)