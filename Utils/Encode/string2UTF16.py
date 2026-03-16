def string_to_utf16_hex(input_str):
    # 'utf-16le' 表示小端序（Little Endian），这是 Windows/Android 内存中标准的存储方式
    # 不带 BOM (Byte Order Mark) 头
    utf16_bytes = input_str.encode('utf-16le')

    print(f"原始字符串: {input_str}")
    print(f"UTF-16LE 字节流 (Hex): {utf16_bytes.hex()}")
    # 去掉多余 00
    print(f"去掉多余 00 后的 Hex: {utf16_bytes.hex().replace('00', '')}")

    print(f"字节长度: {len(utf16_bytes)} bytes")

    return utf16_bytes


# 你的 Key
key_str = "514/wedsjjhfb#0v"
key_bytes = string_to_utf16_hex(key_str)
