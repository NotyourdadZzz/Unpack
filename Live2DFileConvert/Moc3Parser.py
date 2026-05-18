import ctypes
from pathlib import Path
import os


INPUT_MOC3 = r"C:\Users\86182\Downloads\test\Output\Atlant_3\Atlant_3.moc3"

os.add_dll_directory(
    r"D:\SteamLibrary\steamapps\common\Live2DViewerEX\bin\lw\lw_Data\Plugins\x86_64"
)# Live2DCubismCore.dll 的路径 根据实际情况修改
core = ctypes.cdll.LoadLibrary("Live2DCubismCore.dll")
# core.csmGetVersion.restype = ctypes.c_uint32
# version = core.csmGetVersion()
# print(hex(version))
def init_live2d_core():
    # initialize function signatures
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

def extract_param_ids(moc3_path) -> list[str]:
    if not Path(moc3_path).exists():
        raise FileNotFoundError(f"文件不存在: {moc3_path}")

    data = Path(moc3_path).read_bytes()
    size = len(data)
    # 多分配 64 字节以确保有足够的空间进行地址平移
    moc_raw_buf = ctypes.create_string_buffer(size + 64)
    moc_raw_addr = ctypes.addressof(moc_raw_buf)

    # 位运算：计算出下一个满足 64 字节对齐的绝对地址
    moc_aligned_addr = (moc_raw_addr + 63) & ~63

    # 将文件数据精准复制到对齐后的安全内存区域中
    ctypes.memmove(moc_aligned_addr, data, size)
    moc_ptr = ctypes.cast(moc_aligned_addr, ctypes.POINTER(ctypes.c_ubyte))

    moc = core.csmReviveMocInPlace(
        moc_ptr,
        ctypes.c_uint32(size)
    )

    if not moc:
        raise RuntimeError(f"=== Invalid moc3 (内存未对齐或文件损坏)")

    model_size = core.csmGetSizeofModel(moc)
    # 多分配 16 字节用于平移对齐
    model_raw_buf = ctypes.create_string_buffer(model_size + 16)
    model_raw_addr = ctypes.addressof(model_raw_buf)

    # 位运算
    model_aligned_addr = (model_raw_addr + 15) & ~15
    model_ptr = ctypes.c_void_p(model_aligned_addr)

    model = core.csmInitializeModelInPlace(moc, model_ptr, model_size)
    if not model:
        raise RuntimeError("Model init failed")

    count = core.csmGetParameterCount(model)
    ids_ptr = core.csmGetParameterIds(model)

    params = []
    for i in range(count):
        params.append(
            ctypes.string_at(ids_ptr[i]).decode("utf-8")
        )
    return params

def main():
    init_live2d_core()
    ids = extract_param_ids(INPUT_MOC3)
    print(f"参数数量: {len(ids)}")
    print(ids)

if __name__ == "__main__":
    main()

