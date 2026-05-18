import hashlib
from pathlib import Path

FILE1 = r"C:\Users\86182\Downloads\test\Output\Wendy_3\Wendy_3.moc3"
FILE2 = r"D:\Games\GameUnpackAssets\mymodel\Live2D\PathToNowhere (WuQiMiTu)\Models\live2d\characters\char2d_wendy_3\char2d_wendy_3.moc3"

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

md5_1 = md5(FILE1)
md5_2 = md5(FILE2)

print("FILE1:", md5_1)
print("FILE2:", md5_2)

if md5_1 == md5_2:
    print("两个文件完全相同")
else:
    print("两个文件不同")