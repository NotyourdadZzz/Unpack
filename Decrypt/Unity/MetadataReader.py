dat = r"D:\Tools\UsefulTools\MuMu\Shared\Download\global-metadata.dat"
offset = 0x65D948
size = 0x100

with open(dat, "rb") as f:
    f.seek(offset)
    eval_b = f.read(size)
print(eval_b.hex())