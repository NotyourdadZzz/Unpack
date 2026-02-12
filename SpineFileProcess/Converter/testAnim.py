import os, glob, json, struct
from SkelToJson import (
    read_binary_skeleton,
    write_json_data,
    Color,
    TimelineFrame,
    Animation,
    INPUT_PATH,
    OUTPUT_PATH,
)

ANIM_PATH = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\SpineFileProcess\Converter\Data"

class AnimationReader:
    def __init__(self, data: bytes):
        self.data = data
        self.pos = 0
    def _read(self, n):
        if self.pos + n > len(self.data): raise EOFError
        b = self.data[self.pos:self.pos+n]
        self.pos += n
        return b
    def u8(self): return self._read(1)[0]
    def i32(self): return struct.unpack(">i", self._read(4))[0]
    def f32(self): return struct.unpack(">f", self._read(4))[0]
    def varint(self):
        res = 0
        shift = 0
        while True:
            b = self.u8()
            res |= (b & 0x7F) << shift
            if b < 0x80:
                break
            shift += 7
        return res
    def str_varint(self):
        n = self.varint()
        if n == 0:
            return ""
        if n == 1:
            return ""
        length = n - 1
        return "" if length <= 0 else self._read(length).decode("utf-8", errors="replace")

    def read_float_array(self):
        cnt = self.varint()
        if cnt < 0: raise EOFError("negative float array length")
        return [self.f32() for _ in range(cnt)]

def read_curve_be(r: AnimationReader, f: TimelineFrame):
    try: c = r.u8()
    except EOFError: return
    if c == 1: f.curveType = f.curveType.STEPPED
    elif c == 2:
        f.curveType = f.curveType.BEZIER
        try: f.curve = [r.f32(), r.f32(), r.f32(), r.f32()]
        except EOFError: f.curve = []

def parse_spineani(data: bytes, sk) -> Animation:
    r = AnimationReader(data)
    name = r.str_varint().rstrip("@")
    duration = r.f32()
    tcount = r.i32()
    print(f"[ANI] name={name}, duration={duration}, tcount={tcount}, size={len(data)}")

    anim = Animation(name=name)
    bname = lambda i: sk.bones[i].name if 0 <= i < len(sk.bones) else f"bone_{i}"
    sname = lambda i: sk.slots[i].name if 0 <= i < len(sk.slots) else f"slot_{i}"

    for ti in range(max(tcount, 0)):
        try:
            ttype = r.i32()  # 时间线类型固定 4 字节大端
        except EOFError:
            print(f"[ANI] EOF when reading timeline type #{ti}")
            break
        # print(f"  [TL] idx={ti}, type={ttype}, pos={r.pos}")

        # 0 Rotate: curves(float[]), boneIndex(int32), frames(float[] => time,angle)
        if ttype == 0:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    bone={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 2):
                    if i + 1 >= len(fa): break
                    f = TimelineFrame(); f.time = fa[i]; f.value1 = fa[i+1]
                    tl.append(f)
                anim.bones.setdefault(bname(idx), {})["rotate"] = tl
            except EOFError:
                break

        # 1 Translate: curves, boneIndex, frames(time,x,y)
        elif ttype == 1:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    bone={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 3):
                    if i + 2 >= len(fa): break
                    f = TimelineFrame(); f.time = fa[i]; f.value1 = fa[i+1]; f.value2 = fa[i+2]
                    tl.append(f)
                anim.bones.setdefault(bname(idx), {})["translate"] = tl
            except EOFError:
                break

        # 2 Scale: curves, boneIndex, frames(time,x,y)
        elif ttype == 2:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    bone={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 3):
                    if i + 2 >= len(fa): break
                    f = TimelineFrame(); f.time = fa[i]; f.value1 = fa[i+1]; f.value2 = fa[i+2]
                    tl.append(f)
                anim.bones.setdefault(bname(idx), {})["scale"] = tl
            except EOFError:
                break

        # 3 Shear: curves, boneIndex, frames(time,x,y)
        elif ttype == 3:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    bone={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 3):
                    if i + 2 >= len(fa): break
                    f = TimelineFrame(); f.time = fa[i]; f.value1 = fa[i+1]; f.value2 = fa[i+2]
                    tl.append(f)
                anim.bones.setdefault(bname(idx), {})["shear"] = tl
            except EOFError:
                break

        # 4 Attachment（保留原逻辑）
        elif ttype == 4:
            try:
                idx = r.varint()
                fcount = r.varint()
                print(f"    slot={idx}, fcount={fcount}")
                tl = []
                for _ in range(fcount):
                    f = TimelineFrame(); f.time = 0.0; f.str1 = r.str_varint(); tl.append(f)
                anim.slots.setdefault(sname(idx), {})["attachment"] = tl
            except EOFError:
                break

        # 5 Color: curves, slotIndex(int32), frames(time,r,g,b,a)
        elif ttype == 5:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    slot={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 5):
                    if i + 4 >= len(fa): break
                    f = TimelineFrame()
                    f.time = fa[i]
                    f.color1 = Color(int(fa[i+1]*255), int(fa[i+2]*255), int(fa[i+3]*255), int(fa[i+4]*255))
                    tl.append(f)
                anim.slots.setdefault(sname(idx), {})["rgba"] = tl
            except EOFError:
                break

        # 6 Deform（暂保留旧逻辑）
        elif ttype == 6:
            try:
                idx = r.varint()
                att = r.str_varint()
                skin_idx = r.varint()
                fcount = r.varint()
                print(f"    slot={idx}, skin={skin_idx}, att={att}, fcount={fcount}")
                skin_name = sk.skins[skin_idx].name if 0 <= skin_idx < len(sk.skins) else "default"
                tl = []
                for _ in range(fcount):
                    f = TimelineFrame(); f.time = r.f32(); vcount = r.varint()
                    if vcount > 0:
                        vcount = min(vcount, 100000)
                        for _ in range(vcount):
                            f.vertices.append(r.f32())
                    tl.append(f)
                anim.attachments.setdefault(skin_name, {}).setdefault(sname(idx), {}).setdefault(att, {})["deform"] = tl
            except EOFError:
                break

        # 7 Event（保留）
        elif ttype == 7:
            try:
                fcount = r.varint()
                print(f"    events fcount={fcount}")
                tl = []
                for _ in range(fcount):
                    f = TimelineFrame()
                    f.time = r.f32()
                    f.str1 = r.str_varint()
                    f.int1 = r.i32()
                    f.value1 = r.f32()
                    f.str2 = r.str_varint()
                    tl.append(f)
                anim.events = tl
            except EOFError:
                break

        # 8 DrawOrder（保留）
        elif ttype == 8:
            try:
                fcount = r.varint()
                print(f"    draworder fcount={fcount}")
                tl = []
                for _ in range(fcount):
                    f = TimelineFrame(); f.time = r.f32(); oc = r.varint()
                    for _ in range(oc):
                        sid = r.varint(); off = r.i32()
                        f.offsets.append((sname(sid), off))
                    tl.append(f)
                anim.drawOrder = tl
            except EOFError:
                break

        # 9 IK（暂保留旧帧读取，但前置 curves+idx）
        elif ttype == 9:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fcount = r.varint()
                print(f"    ik={idx}, fcount={fcount}, curves={len(curves)}")
                tl = []
                for fi in range(fcount):
                    f = TimelineFrame()
                    f.time = r.f32()
                    f.value1 = r.f32()
                    f.value2 = r.f32()
                    f.bendPositive = r.i32() > 0
                    f.compress = r.u8() != 0
                    f.stretch = r.u8() != 0
                    tl.append(f)
                anim.ik[bname(idx)] = tl
            except EOFError:
                break

        # 10 TransformConstraint（前置 curves+idx，frames float[] 粗解析）
        elif ttype == 10:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    tf={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 4):
                    if i + 3 >= len(fa): break
                    f = TimelineFrame()
                    f.time = fa[i]; f.value1 = fa[i+1]; f.value2 = fa[i+2]; f.value4 = fa[i+3]
                    tl.append(f)
                anim.transform.setdefault(bname(idx), []).extend(tl)
            except EOFError:
                break

        # 11 Path Position（前置 curves+idx，frames float[]）
        elif ttype == 11:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    pathpos={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 2):
                    if i + 1 >= len(fa): break
                    f = TimelineFrame()
                    f.time = fa[i]; f.value1 = fa[i+1]
                    tl.append(f)
                anim.path.setdefault(bname(idx), {})["position"] = tl
            except EOFError:
                break

        # 12 Path Spacing
        elif ttype == 12:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    pathspace={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 2):
                    if i + 1 >= len(fa): break
                    f = TimelineFrame()
                    f.time = fa[i]; f.value1 = fa[i+1]
                    tl.append(f)
                anim.path.setdefault(bname(idx), {})["spacing"] = tl
            except EOFError:
                break

        # 13 Path Mix
        elif ttype == 13:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    pathmix={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 3):
                    if i + 2 >= len(fa): break
                    f = TimelineFrame()
                    f.time = fa[i]; f.value1 = fa[i+1]; f.value2 = fa[i+2]
                    tl.append(f)
                anim.path.setdefault(bname(idx), {})["mix"] = tl
            except EOFError:
                break

        # 14 TwoColor
        elif ttype == 14:
            try:
                curves = r.read_float_array()
                idx = r.i32()
                fa = r.read_float_array()
                print(f"    twocolor slot={idx}, floats={len(fa)}, curves={len(curves)}")
                tl = []
                for i in range(0, len(fa), 7):  # time, lr,lg,lb,la, dr,dg （db 可能缺，按 7 取）
                    if i + 6 >= len(fa): break
                    f = TimelineFrame()
                    f.time = fa[i]
                    lr, lg, lb, la = fa[i+1], fa[i+2], fa[i+3], fa[i+4]
                    dr, dg, db = fa[i+5], fa[i+6], fa[i+6]
                    f.color1 = Color(int(lr*255), int(lg*255), int(lb*255), int(la*255))
                    f.color2 = Color(int(dr*255), int(dg*255), int(db*255), 0xFF)
                    tl.append(f)
                anim.slots.setdefault(sname(idx), {})["rgba2"] = tl
            except EOFError:
                break

        else:
            print(f"  [UNKNOWN] type={ttype}, break")
            break
    return anim

def load_spineani_animations(sk, anim_dir):
    base = os.path.splitext(os.path.basename(INPUT_PATH))[0]
    pattern = os.path.join(anim_dir, f"{base.lower()}__*.spineani")
    added = 0
    for fp in glob.glob(pattern):
        try:
            with open(fp, "rb") as f: data = f.read()
            sk.animations.append(parse_spineani(data, sk))
            added += 1
        except Exception as e:
            print(f"[WARN] 读取 {fp} 失败：{e}")
    return added

def main():
    with open(INPUT_PATH, "rb") as f: skel_bytes = f.read()
    sk = read_binary_skeleton(skel_bytes)
    if not sk.animations:
        added = load_spineani_animations(sk, ANIM_PATH)
        print(f"[INFO] 外部动画补充 {added} 个")
    root = write_json_data(sk)
    out = OUTPUT_PATH
    with open(out, "w", encoding="utf-8") as f: json.dump(root, f, ensure_ascii=False, indent=4)
    print(f"[OK] 写出：{out}")

if __name__ == "__main__":
    main()