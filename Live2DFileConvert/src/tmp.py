def fnv1a_64(s: str) -> int:
    """
    计算字符串的 FNV-1a 64-bit 哈希，返回 unsigned 64-bit 整数
    """
    FNV_offset_basis = 0xcbf29ce484222325
    FNV_prime = 0x100000001b3

    h = FNV_offset_basis
    for c in s.encode('utf-8'):
        h ^= c
        h = (h * FNV_prime) & 0xFFFFFFFFFFFFFFFF  # 保持 64-bit
    return h

# 示例
parameter_name = "char2d_vautour_4/Parameters/ParamEyeLOpen"
hash64 = fnv1a_64(parameter_name)
print(f"{parameter_name} -> {hash64} (0x{hash64:016X})")
