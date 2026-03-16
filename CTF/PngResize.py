import struct

src = r"C:\Users\86182\Downloads\CTF\A_MISC\1.png"
dst = r"C:\Users\86182\Downloads\CTF\A_MISC\1_big.png"

width = 948
height = 500

with open(src, "rb") as f:
    data = bytearray(f.read())

data[16:20] = struct.pack(">I", width)
data[20:24] = struct.pack(">I", height)

with open(dst, "wb") as f:
    f.write(data)

print("done")