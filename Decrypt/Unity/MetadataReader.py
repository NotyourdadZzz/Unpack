dat = r"D:\Tools\UsefulTools\MuMu\Shared\Download\global-metadata.dat"
with open(dat, "rb") as f:
    f.seek(0x65D948)
    eval_b = f.read(0x100)
print(eval_b.hex())