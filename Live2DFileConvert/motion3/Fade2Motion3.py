import math
import os
import json
import re
from pathlib import Path
# 尚处于测试阶段, 备份数据, 自行测试 2026.6.15
# // https://live2dhub.com/t/topic/2636/54
INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Live2D\SteamGame\MorningMist\Live2D\Test"
OUTPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Live2D\SteamGame\MorningMist\Live2D\Output"


FADE_REGEX = re.compile(r'.*\.fade(\s*[#@]-?\d+)?\.json$')  # 匹配 .fade.json 或 .fade @xxxx.json 或 .fade #xxxx.json
os.makedirs(OUTPUT_PATH, exist_ok=True)
def convert_segments(curve, force_bezier=True):
    """
    Unity Keyframe -> Live2D motion3 Segments
    """
    if not curve:
        return []

    segments = []

    # 第一个点直接写入
    first = curve[0]
    segments.append(first.get("time", 0.0))
    segments.append(first.get("value", 0.0))

    j = 1

    while j < len(curve):
        cur = curve[j]
        prev = curve[j - 1]
        next_curve = curve[j + 1] if j + 1 < len(curve) else None

        cur_time = float(cur.get("time", 0.0))
        cur_value = float(cur.get("value", 0.0))

        prev_time = float(prev.get("time", 0.0))
        prev_value = float(prev.get("value", 0.0))

        in_slope = cur.get("inSlope", 0.0)
        out_slope = prev.get("outSlope", 0.0)

        # 字符串 Infinity -> float
        if isinstance(in_slope, str):
            if in_slope == "Infinity":
                in_slope = math.inf
            else:
                in_slope = float(in_slope)

        if isinstance(out_slope, str):
            if out_slope == "Infinity":
                out_slope = math.inf
            else:
                out_slope = float(out_slope)

        in_slope = float(in_slope)
        out_slope = float(out_slope)

        # --------------------------------------------------
        # InverseStepped
        # --------------------------------------------------

        if (
            abs(cur_time - prev_time - 0.01) < 0.0001
            and next_curve is not None
            and float(next_curve.get("value", 0.0)) == cur_value
        ):
            segments.append(3)

            segments.append(float(next_curve.get("time", 0.0)))
            segments.append(float(next_curve.get("value", 0.0)))

            j += 2
            continue

        # --------------------------------------------------
        # Stepped
        # --------------------------------------------------

        if math.isinf(in_slope) and in_slope > 0:
            segments.append(2)

            segments.append(cur_time)
            segments.append(cur_value)

            j += 1
            continue

        # --------------------------------------------------
        # Linear
        # --------------------------------------------------

        if (
            out_slope == 0.0
            and abs(in_slope) < 0.0001
            and not force_bezier
        ):
            segments.append(0)

            segments.append(cur_time)
            segments.append(cur_value)

            j += 1
            continue

        # --------------------------------------------------
        # Bezier
        # --------------------------------------------------

        tangent_length = (cur_time - prev_time) / 3.0

        cx1 = prev_time + tangent_length
        cy1 = out_slope * tangent_length + prev_value

        cx2 = cur_time - tangent_length
        cy2 = cur_value - in_slope * tangent_length

        segments.append(1)

        segments.append(cx1)
        segments.append(cy1)

        segments.append(cx2)
        segments.append(cy2)

        segments.append(cur_time)
        segments.append(cur_value)

        j += 1

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
            param_ids = obj.get("ParameterIds", [])

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