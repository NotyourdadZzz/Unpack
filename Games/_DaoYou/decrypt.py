import struct

HEX_TABLE = [0xFF] * 256
for i, ch in enumerate(range(ord('0'), ord('9') + 1)):
    HEX_TABLE[ch] = i
for i, ch in enumerate(range(ord('A'), ord('F') + 1)):
    HEX_TABLE[ch] = 0xA + i
for i, ch in enumerate(range(ord('a'), ord('f') + 1)):
    HEX_TABLE[ch] = 0xA + i


def hex_string_to_key(hex_str: str) -> bytearray:
    if len(hex_str) != 32:
        raise ValueError("Key must be 32 hex characters")
    key = bytearray()
    for i in range(0, 32, 2):
        hi = HEX_TABLE[ord(hex_str[i])]
        lo = HEX_TABLE[ord(hex_str[i+1])]
        if hi == 0xFF or lo == 0xFF:
            raise ValueError(f"Invalid hex char at {i}")
        key.append((hi << 4) | (lo & 0xF))
    return key


def decrypt_data(data: bytearray, filename: str, max_len: int = 16) -> int:
    if '.' in filename or len(filename) != 32:
        return 0

    key = hex_string_to_key(filename)

    # 解密前 max_len 字节（引擎固定最多 16）
    n = min(len(data), max_len, 16)
    for i in range(n):
        data[i] ^= key[i]
    return n


if __name__ == "__main__":

    fname = "ff46fd2c5a406d1c00e758663a37c251"

    encrypted = bytearray([0xFE, 0x64, 0xFD, 0x0E, 0x5A, 0x40, 0x6D, 0x1C,
                           0x01, 0xE7, 0x58, 0x66, 0x3A, 0x4F, 0x5E, 0x32])

    n_decrypted = decrypt_data(encrypted, fname)
    print(f"Decrypted {n_decrypted} bytes")
    print(encrypted.hex())