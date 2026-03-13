import re
from UnityPy.helpers.ArchiveStorageManager import brute_force_key
from UnityPy.streams.EndianBinaryReader import EndianBinaryReader

# ================== 配置 ==================
BUNDLE_FILE_PATH = r"C:\Users\86182\Downloads\momentris\file\portrait_middle_awaker_c01ex_af_ani.ab"
GLOBAL_METADATA_PATH = r"C:\Users\86182\Downloads\momentris\global-metadata.dat"
# ==========================================
PATTERN_1 = re.compile(rb"(?=([\x20-\x7E]{16}))")  # 16字节可打印ASCII
PATTERN_2 = re.compile(rb"(?=(\w{16}))")

def main():
    with open(GLOBAL_METADATA_PATH, "rb") as f:
        if f.read(4) != b"\xAF\x1B\xB1\xFA":
            print("global-metadata.dat 不是有效的 global-metadata 文件 或者 不是明文")
            return
        else:
            print("global-metadata.dat 文件验证通过")

    with open(BUNDLE_FILE_PATH, "rb") as f:
        data = f.read()
        reader = EndianBinaryReader(data)

    # === 解析 AssetBundle 头 ===
    signature = reader.read_string_to_null()  # signature
    version = reader.read_u_int()           # version
    unity_version = reader.read_string_to_null()  # unity version
    unity_reversion = reader.read_string_to_null()  # unity revision
    print(f"AssetBundle Signature: {signature}")
    print(f"AssetBundle Version: {version}")
    print(f"Unity Version: {unity_version}")
    print(f"Unity Revision: {unity_reversion}")

    possible_offsets = [56, 57, 60, 64]
    for offset in possible_offsets:
        print(f"[*] 正在测试偏移量: {offset}")

        reader.Position += offset

        # === 读取签名数据 ===
        signature_bytes = reader.read_bytes(0x10)
        signature_key   = reader.read_bytes(0x10)

        # === 暴力 key ===
        key = brute_force_key(
            GLOBAL_METADATA_PATH,
            signature_key,
            signature_bytes,
            PATTERN_1
        )

        print(key)

if __name__ == "__main__":
    main()
