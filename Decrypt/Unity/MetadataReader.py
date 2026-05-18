dat = r"D:\Tools\UsefulTools\MuMu\Shared\Download\global-metadata.dat"
_offset = 0x65D948
_size = 0x100

with open(dat, "rb") as f:
    f.seek(_offset)
    eval_b = f.read(_size)
print(eval_b.hex())