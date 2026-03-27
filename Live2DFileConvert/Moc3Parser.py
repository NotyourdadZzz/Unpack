import ctypes
from pathlib import Path
import os


INPUT_MOC3 = r"D:\Games\GameUnpackAssets\mymodel\Live2D\Red PrideOfEden (YiDianDeJiaoAo)\Live2D\l2d_12030003\l2d_12030003.moc3"
os.add_dll_directory(
    r"D:\SteamLibrary\steamapps\common\Live2DViewerEX\bin\lw\lw_Data\Plugins\x86_64"
)# Live2DCubismCore.dll 的路径，根据实际情况修改
core = ctypes.cdll.LoadLibrary("Live2DCubismCore.dll")

class StandardParams:
    ParamAngleX = "ParamAngleX"
    ParamAngleY = "ParamAngleY"
    ParamAngleZ = "ParamAngleZ"
    ParamEyeLOpen = "ParamEyeLOpen"
    ParamEyeLSmile = "ParamEyeLSmile"
    ParamEyeROpen = "ParamEyeROpen"
    ParamEyeRSmile = "ParamEyeRSmile"
    ParamEyeBallX = "ParamEyeBallX"
    ParamEyeBallY = "ParamEyeBallY"
    ParamEyeBallForm = "ParamEyeBallForm"
    ParamBrowLY = "ParamBrowLY"
    ParamBrowRY = "ParamBrowRY"
    ParamBrowLX = "ParamBrowLX"
    ParamBrowRX = "ParamBrowRX"
    ParamBrowLAngle = "ParamBrowLAngle"
    ParamBrowRAngle = "ParamBrowRAngle"
    ParamBrowLForm = "ParamBrowLForm"
    ParamBrowRForm = "ParamBrowRForm"
    ParamMouthForm = "ParamMouthForm"
    ParamMouthOpenY = "ParamMouthOpenY"
    ParamCheek = "ParamCheek"
    ParamBodyAngleX = "ParamBodyAngleX"
    ParamBodyAngleY = "ParamBodyAngleY"
    ParamBodyAngleZ = "ParamBodyAngleZ"
    ParamBreath = "ParamBreath"
    ParamArmLA = "ParamArmLA"
    ParamArmRA = "ParamArmRA"
    ParamArmLB = "ParamArmLB"
    ParamArmRB = "ParamArmRB"
    ParamHandL = "ParamHandL"
    ParamHandR = "ParamHandR"
    ParamHairFront = "ParamHairFront"
    ParamHairSide = "ParamHairSide"
    ParamHairBack = "ParamHairBack"
    ParamHairFluffy = "ParamHairFluffy"
    ParamShoulderY = "ParamShoulderY"
    ParamBustX = "ParamBustX"
    ParamBustY = "ParamBustY"
    ParamBaseX = "ParamBaseX"
    ParamBaseY = "ParamBaseY"

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


def extract_param_ids(moc3_path: str) -> list[str]:
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

    return [ids_ptr[i].decode("utf-8") for i in range(count)]


if __name__ == "__main__":
    ids = extract_param_ids(INPUT_MOC3)
    print(ids)

