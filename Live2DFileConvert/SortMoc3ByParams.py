import ctypes
import shutil
from pathlib import Path
import os
import json

# 模型根目录, 每个模型目录结构为
# root
# ├─ model1
#     ├─ motions
#     │  └─ 1.motion3.json
#     │  └─ 2.motion3.json
#     ├─ textures
#     │  └─ texture_00.png
#     ├─ .moc3 #To be sorted
#     ├─ .model3.json
# ├─ model2
# ├─ ...
DRY_RUN = True
ROOT_DIR = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Live2D"
# .moc3 文件所在目录
MOC3_DIR = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Live2D\Moc3"

os.add_dll_directory(
    r"D:\SteamLibrary\steamapps\common\Live2DViewerEX\bin\lw\lw_Data\Plugins\x86_64"
)# Live2DCubismCore.dll 的路径，根据实际情况修改
core = ctypes.cdll.LoadLibrary("Live2DCubismCore.dll")

STANDARD_PARAMS = {
    "ParamAngleX","ParamAngleY","ParamAngleZ","ParamEyeLOpen","ParamEyeLSmile","ParamEyeROpen","ParamEyeRSmile","ParamEyeBallX","ParamEyeBallY","ParamEyeBallForm",
    "ParamBrowLY","ParamBrowRY","ParamBrowLX","ParamBrowRX","ParamBrowLAngle","ParamBrowRAngle","ParamBrowLForm","ParamBrowRForm","ParamMouthForm","ParamMouthOpenY",
    "ParamCheek","ParamBodyAngleX","ParamBodyAngleY","ParamBodyAngleZ","ParamBreath","ParamArmLA","ParamArmRA","ParamArmLB","ParamArmRB","ParamHandL","ParamHandR",
    "ParamHairFront","ParamHairSide","ParamHairBack","ParamHairFluffy","ParamShoulderY","ParamBustX","ParamBustY","ParamBaseX","ParamBaseY",
}
c_void_p = ctypes.c_void_p
c_int = ctypes.c_int
c_char_p = ctypes.c_char_p

core.csmReviveMocInPlace.argtypes = [ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint32]
core.csmReviveMocInPlace.restype = c_void_p

core.csmGetSizeofModel.argtypes = [c_void_p]
core.csmGetSizeofModel.restype = ctypes.c_uint32

core.csmInitializeModelInPlace.argtypes = [c_void_p, c_void_p, ctypes.c_uint32]
core.csmInitializeModelInPlace.restype = c_void_p

core.csmGetParameterCount.argtypes = [c_void_p]
core.csmGetParameterCount.restype = c_int

core.csmGetParameterIds.argtypes = [c_void_p]
core.csmGetParameterIds.restype = ctypes.POINTER(c_char_p)


def extract_moc3_param_ids(moc3_path: str) -> set[str]:
    data = Path(moc3_path).read_bytes()
    size = len(data)

    buf = (ctypes.c_ubyte * size).from_buffer_copy(data)

    moc = core.csmReviveMocInPlace(buf, size)
    if not moc:
        raise RuntimeError("Invalid moc3")

    model_size = core.csmGetSizeofModel(moc)
    model_buf = ctypes.create_string_buffer(model_size)

    model = core.csmInitializeModelInPlace(moc, model_buf, model_size)
    if not model:
        raise RuntimeError("Model init failed")

    count = core.csmGetParameterCount(model)
    ids_ptr = core.csmGetParameterIds(model)

    return set(ids_ptr[i].decode("utf-8") for i in range(count))

def extract_motion3_curve_ids(motion3_json_path: str) -> set[str]:
    data = json.loads(Path(motion3_json_path).read_text(encoding="utf-8"))
    curves = data.get("Curves", [])
    return set(curve.get("Id", "") for curve in curves)

def collect_model_motion_ids(root_dir: Path) -> dict[Path, set[str]]:
    model_ids: dict[Path, set[str]] = {}

    for model_json in root_dir.rglob("*.model3.json"):
        model_dir = model_json.parent

        ids = set()
        for motion in model_dir.rglob("*.motion3.json"):
            ids |= extract_motion3_curve_ids(motion)

        if ids:
            model_ids[model_dir] = ids

    return model_ids

def collect_moc3_ids(moc_dir: Path) -> dict[Path, set[str]]:
    moc_ids: dict[Path, set[str]] = {}

    for moc in moc_dir.rglob("*.moc3"):
        ids = extract_moc3_param_ids(moc)
        if ids:
            moc_ids[moc] = ids

    return moc_ids

def match_models(model_ids: dict[Path, set[str]], moc_ids: dict[Path, set[str]]) -> list[dict]:
    results = []

    for model_dir, m_ids in model_ids.items():
        best_score = 0
        best_mocs: list[Path] = []

        for moc_path, moc_param_ids in moc_ids.items():
            common = m_ids & moc_param_ids
            score = len(common)

            if score > best_score:
                best_score = score
                best_mocs = [moc_path]  # 重置
            elif score == best_score and score != 0:
                best_mocs.append(moc_path)  # 追加

        results.append({
            "model": str(model_dir),
            "moc3_path_list": [str(p) for p in best_mocs],
            "scoreRatio": best_score / len(m_ids) if m_ids else 0
        })

    return results



def move_moc3_files(results: list[dict]):
    for r in results:
        model_dir = Path(r["model"])
        moc_list = r.get("moc3_path_list", [])
        score_ratio = r["scoreRatio"]

        if not moc_list:
            continue

        model_name = model_dir.name

        for idx, moc_str in enumerate(moc_list):
            moc_path = Path(moc_str)

            if not moc_path.exists():
                continue

            if len(moc_list) > 1:
                dst = model_dir / moc_path.name
            else: # only one
                dst = model_dir / f"{model_name}.moc3"

            if dst.exists():
                print(f"[EXISTS] {dst}")
                continue

            print(f"[COPY] {moc_path} -> {dst} (scoreRatio={score_ratio})")

            if not DRY_RUN:
                shutil.copy2(str(moc_path), str(dst))  # 用 copy！


def main():
    model_ids = collect_model_motion_ids(Path(ROOT_DIR))
    moc_ids = collect_moc3_ids(Path(MOC3_DIR))
    results = match_models(model_ids, moc_ids)
    for r in results:
        print(f"[MODEL] {r['model']}")
        for moc in r["moc3_path_list"]:
            print(f"  -> MOC3: {moc}")
        print(f"  -> ScoreRatio: {r['scoreRatio']:.2f}")
    move_moc3_files(results)
    # 递归搜索 MOC3_DIR 下所有的 .moc3 文件，并提取参数 id 列表
    # 同时搜索 ROOT_DIR 下所有的 .model3.json 文件, 每个 model3 所在目录认为是一个模型目录
    # 模型目录下 motions 中每个 .motion3.json取出 "Curves" > "Id" 列表,
    # 然后同一个模型目录下的motion3 id取并集作为该模型的 id 列表
    # 每个模型的 id 列表和 MOC3_DIR下的.moc3 id进行比较, 匹配度最高的认为是该模型对应的.moc3文件, 输出匹配结果


if __name__ == "__main__":
    main()

