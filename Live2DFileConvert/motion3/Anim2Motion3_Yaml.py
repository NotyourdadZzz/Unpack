import os
import json
from pathlib import Path
import yaml
try:
    from yaml import CLoader as Loader
except:
    from yaml import SafeLoader as Loader

# 需要能够导出 yaml 格式的 AnimationClip 数据
# path 需要以 Parameters/ 或 Parts/ 开头

def close(a, b):
    return abs(a - b) < 1e-5

def ignore_unknown(loader, tag_suffix, node):
    return loader.construct_mapping(node)

Loader.add_multi_constructor('', ignore_unknown)


class KeyFrame:
    def __init__(
        self,
        time,
        value,
        in_tangent=0,
        out_tangent=0
    ):
        self.time = time
        self.value = value
        self.in_tangent = in_tangent
        self.out_tangent = out_tangent


def load_anim(path: str) -> dict:
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"File not found: {path}"
        )
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=Loader)

def read_curves(anim: dict) -> list[tuple[str, list[KeyFrame]]]:
    curves: list[tuple[str, list[KeyFrame]]] = []
    for fc in anim["AnimationClip"]["m_FloatCurves"]:
        path = fc.get("path")
        if not path:
            continue
        frames = []

        for k in fc["curve"]["m_Curve"]:
            frames.append(
                KeyFrame(
                    k["time"],
                    k["value"],
                    k.get("inSlope", 0)
                    if isinstance(k.get("inSlope"), int | float) else 0,
                    k.get("outSlope", 0)
                    if isinstance(k.get("outSlope"), int | float) else 0
                )
            )
        curve = (path, frames)
        curves.append(curve)

    return curves

def curve_to_segments(frames):
    if not frames:
        return []

    result = [frames[0].time, frames[0].value]

    for i in range(1, len(frames)):

        prev = frames[i-1]
        cur = frames[i]
        dt = cur.time - prev.time

        # Linear
        if dt:
            slope = (cur.value - prev.value) / dt
            if close(prev.out_tangent, slope) and close(cur.in_tangent, slope):
                result += [0, cur.time, cur.value]
                continue

        # Bezier
        length = abs(dt) / 3
        c1x = prev.time + length
        c1y = prev.value + prev.out_tangent * length
        c2x = cur.time - length
        c2y = cur.value - cur.in_tangent * length
        result += [
            1,
            c1x, c1y,
            c2x, c2y,
            cur.time,
            cur.value
        ]
    return result

def convert(anim_file: str, out_dir: str):
    data = load_anim(anim_file)
    if "AnimationClip" not in data:
        raise ValueError(
            f"Invalid animation data: {anim_file}"
        )

    clip = data["AnimationClip"]
    stop = clip["m_AnimationClipSettings"]["m_StopTime"]
    start = clip["m_AnimationClipSettings"]["m_StartTime"]
    duration = stop - start

    curves = []
    for path, frames in read_curves(data):
        curve_id = path.split("/")[-1]
        if path.startswith("Parameters/"):
            curve_target = "Parameter"
        elif path.startswith("Parts/"):
            curve_target = "PartOpacity"
        else:
            print(f"[Warning] Unknown curve target: {path}")
        curves.append(
            {
                "Target": curve_target,
                "Id": curve_id,
                "Segments": curve_to_segments(frames)
            }
        )

    motion = {
        "Version": 3,
        "Meta": {
            "Duration": duration,
            "Fps": 30.0,
            "FadeInTime": 0.5,
            "FadeOutTime": 0.5,
            "Loop": True,
            "AreBeziersRestricted": True
        },
        "Curves": curves
    }

    name = clip["m_Name"]
    out = os.path.join(out_dir, name + ".motion3.json")

    with open(out, "w", encoding="utf-8") as f:
        json.dump(motion, f, indent=2, ensure_ascii=False)

    print("[OK]", out)

def main():
    # 获取脚本所在目录
    script_dir = Path(__file__).resolve().parent
    # 输入目录：脚本所在目录
    anim_path = script_dir
    # 输出目录：脚本同目录下的 motions 文件夹，不存在则创建
    output_dir = script_dir / "motions"
    output_dir.mkdir(parents=True, exist_ok=True)

    for file in anim_path.rglob("*.anim"):
        print(f"[+] converting {file}")
        convert(
            str(file),
            str(output_dir)
        )

if __name__ == "__main__":
    main()
