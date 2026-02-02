import re
from UnityPy.helpers.ArchiveStorageManager import brute_force_key
from UnityPy.streams.EndianBinaryReader import EndianBinaryReader

# ================== 配置 ==================
BUNDLEFILE_PATH = r"C:\Users\86182\Downloads\assetbundles\000f5831daaa36ba34237edd63a6e3c6.ab"
GLOBAL_METADATA_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\global-metadata.dat"
# ==========================================

def main():
    with open(BUNDLEFILE_PATH, "rb") as f:
        data = f.read()
        reader = EndianBinaryReader(data)

    # === 解析 AssetBundle 头 ===
    _ = reader.read_string_to_null()  # signature
    _ = reader.read_u_int()           # version
    _ = reader.read_string_to_null()  # unity version
    _ = reader.read_string_to_null()  # unity revision

    reader.Position += 57  # ⚠ 如失败，优先调整这里：56 / 60 / 64

    # === 读取签名数据 ===
    signatureBytes = reader.read_bytes(0x10)
    signatureKey   = reader.read_bytes(0x10)

    # === 暴力 key ===
    key = brute_force_key(
        GLOBAL_METADATA_PATH,
        signatureKey,
        signatureBytes,
        re.compile(rb"(?=([\x20-\x7E]{16}))")  # 16字节可打印ASCII
    )

    print(key)

if __name__ == "__main__":
    main()
