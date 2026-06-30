import math
import struct
def get_mask_code(url: str, data_len: int) -> int:
    MAX_INT = 2147483647

    # 取最后一个 '/' 之后的部分
    filename = url.rsplit('/', 1)[-1] if '/' in url else url

    # 去掉扩展名
    if '.bin' in filename:
        filename = filename.replace('.bin', '')
    elif '.json' in filename:
        filename = filename.replace('.json', '')
    else:
        filename = filename.replace('.png', '').replace('.jpg', '').replace('.jpeg', '')

    parts = filename.split('-')
    if len(parts) > 1:
        try:
            ver = int(parts[1], 16)
        except ValueError:
            ver = MAX_INT
    else:
        ver = MAX_INT

    ver %= data_len
    while ver * 3 < MAX_INT:
        ver *= 3
    return ver

def codec(data: bytes, mask: int) -> bytes:
    length = len(data)
    s = math.floor(math.sqrt(length / 4))

    # 保证数据长度是 4 的倍数，并补齐到 s*s*4
    need = s * s * 4
    if length % 4 != 0 or length < need:
        padded = data + b'\x00' * (need - length) if need > length else data
        padded += b'\x00' * ((4 - (len(padded) % 4)) % 4)
    else:
        padded = data

    # 以小端 u32 读取
    ints = list(struct.unpack('<' + 'I' * (len(padded) // 4), padded))
    a = s
    o = s
    h = math.ceil(s / 2)

    for y in range(o):
        if (y // h) % 2 != 0:
            continue
        for x in range(a):
            new_y = y
            new_x = x
            skip = False

            if (x // h) % 2 == 0:
                if x + h < a:
                    new_x = x + h
            else:
                if skip:
                    continue
                new_x = x - h

            if y + h < o:
                new_y = y + h
            else:
                skip = True

            if skip and (x // h) % 2 != 0:
                continue

            idx1 = y * a + x
            idx2 = new_y * a + new_x
            tmp = ints[idx1]
            ints[idx1] = ints[idx2] ^ mask
            ints[idx2] = tmp ^ mask

    result = struct.pack('<' + 'I' * len(ints), *ints)
    return result[:length]   # 截回原始长度

def decrypt_asset(url: str, encrypted_data: bytes) -> bytes:
    mask = get_mask_code(url, len(encrypted_data))
    return codec(encrypted_data, mask)