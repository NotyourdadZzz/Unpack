import os
import struct
import lz4.block
from pathlib import Path
from dataclasses import dataclass, field
import struct
INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\SpineFileProcess\Converter\Data"
OUTPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\SpineFileProcess\Converter\Data\test"

_EXT = ".scsp"

@dataclass
class BoneData:
    index: int
    name_offset: int
    parent_index: int

    length: float
    x: float
    y: float
    rotation: float
    scaleX: float
    scaleY: float
    shearX: float
    shearY: float

    color: int
    inherit: bool

    SIZE = 43   # 实际读取字节数（无padding）

    def __repr__(self):
        return (
            f"Bone(index={self.index}, "
            f"parent={self.parent_index}, "
            f"x={self.x:.2f}, y={self.y:.2f}, "
            f"rot={self.rotation:.2f}, "
            f"scale=({self.scaleX:.2f},{self.scaleY:.2f}))"
        )
    @classmethod
    def parse_from(cls, data: bytes, pos: int):

        index = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        name_offset = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        parent_index = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        floats = struct.unpack_from('<8f', data, pos)
        pos += 32

        color = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        inherit = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        bone = cls(
            index=index,
            name_offset=name_offset,
            parent_index=parent_index,
            length=floats[0],
            x=floats[1],
            y=floats[2],
            rotation=floats[3],
            scaleX=floats[4],
            scaleY=floats[5],
            shearX=floats[6],
            shearY=floats[7],
            color=color,
            inherit=bool(inherit)
        )

        return bone, pos

@dataclass
class IkConstraintData:
    name_offset: int
    order: int
    skin_required: bool
    bend_direction: int
    compress: bool
    mix: float
    softness: float
    stretch: bool
    uniform: bool
    target_index: int
    bone_indices: list = field(default_factory=list)

    @classmethod
    def parse_from(cls, data, pos):

        name_offset = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        order = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        skin_required = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        bend_direction = struct.unpack_from('<i', data, pos)[0]
        pos += 4

        compress = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        mix = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        softness = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        stretch = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        uniform = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        target_index = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        bone_count = struct.unpack_from('<H', data, pos)[0]
        pos += 2

        bone_indices = []
        for _ in range(bone_count):
            idx = struct.unpack_from('<h', data, pos)[0]
            pos += 2
            bone_indices.append(idx)

        return cls(
            name_offset,
            order,
            bool(skin_required),
            bend_direction,
            bool(compress),
            mix,
            softness,
            bool(stretch),
            bool(uniform),
            target_index,
            bone_indices
        ), pos

@dataclass
class SlotData:
    index: int
    name_offset: int
    bone_index: int

    r: float
    g: float
    b: float
    a: float

    dark_r: float
    dark_g: float
    dark_b: float
    dark_a: float

    has_dark_color: bool

    attachment_name_offset: int
    blend_mode: int

    @classmethod
    def parse_from(cls, data, pos):

        index = struct.unpack_from('<H', data, pos)[0]
        pos += 2

        name_offset = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        bone_index = struct.unpack_from('<H', data, pos)[0]
        pos += 2

        r, g, b, a = struct.unpack_from('<4f', data, pos)
        pos += 16

        dark_r, dark_g, dark_b, dark_a = struct.unpack_from('<4f', data, pos)
        pos += 16

        has_dark_color = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        attachment_name_offset = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        blend_mode = struct.unpack_from('<H', data, pos)[0]
        pos += 2

        return cls(
            index,
            name_offset,
            bone_index,
            r, g, b, a,
            dark_r, dark_g, dark_b, dark_a,
            bool(has_dark_color),
            attachment_name_offset,
            blend_mode
        ), pos

@dataclass
class TransformConstraintData:
    name_offset: int
    order: int
    skin_required: bool

    rotate_mix: float
    translate_mix: float
    scale_mix: float
    shear_mix: float

    offset_rotation: float
    offset_x: float
    offset_y: float
    offset_scale_x: float
    offset_scale_y: float
    offset_shear_y: float

    local: bool
    relative: bool

    target_index: int
    bone_indices: list = field(default_factory=list)

    @classmethod
    def parse_from(cls, data, pos):

        name_offset = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        order = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        skin_required = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        rotate_mix = struct.unpack_from('<f', data, pos)[0]; pos += 4
        translate_mix = struct.unpack_from('<f', data, pos)[0]; pos += 4
        scale_mix = struct.unpack_from('<f', data, pos)[0]; pos += 4
        shear_mix = struct.unpack_from('<f', data, pos)[0]; pos += 4

        offset_rotation = struct.unpack_from('<f', data, pos)[0]; pos += 4
        offset_x = struct.unpack_from('<f', data, pos)[0]; pos += 4
        offset_y = struct.unpack_from('<f', data, pos)[0]; pos += 4
        offset_scale_x = struct.unpack_from('<f', data, pos)[0]; pos += 4
        offset_scale_y = struct.unpack_from('<f', data, pos)[0]; pos += 4
        offset_shear_y = struct.unpack_from('<f', data, pos)[0]; pos += 4

        local = struct.unpack_from('<B', data, pos)[0]; pos += 1
        relative = struct.unpack_from('<B', data, pos)[0]; pos += 1

        target_index = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        bone_count = struct.unpack_from('<H', data, pos)[0]
        pos += 2

        bone_indices = []
        for _ in range(bone_count):
            idx = struct.unpack_from('<h', data, pos)[0]
            pos += 2
            bone_indices.append(idx)

        return cls(
            name_offset,
            order,
            bool(skin_required),

            rotate_mix,
            translate_mix,
            scale_mix,
            shear_mix,

            offset_rotation,
            offset_x,
            offset_y,
            offset_scale_x,
            offset_scale_y,
            offset_shear_y,

            bool(local),
            bool(relative),

            target_index,
            bone_indices
        ), pos

@dataclass
class PathConstraintData:
    name_offset: int
    order: int
    skin_required: bool
    position_mode: int
    spacing_mode: int
    rotate_mode: int
    offset_rotation: float
    position: float
    spacing: float
    rotate_mix: float
    translate_mix: float
    target_index: int
    bone_indices: list = field(default_factory=list)

    @classmethod
    def parse_from(cls, data, pos):

        name_offset = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        order = struct.unpack_from('<I', data, pos)[0]
        pos += 4

        skin_required = struct.unpack_from('<B', data, pos)[0]
        pos += 1

        position_mode = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        spacing_mode = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        rotate_mode = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        offset_rotation = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        position_val = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        spacing_val = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        rotate_mix = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        translate_mix = struct.unpack_from('<f', data, pos)[0]
        pos += 4

        target_index = struct.unpack_from('<h', data, pos)[0]
        pos += 2

        bone_count = struct.unpack_from('<H', data, pos)[0]
        pos += 2

        bone_indices = []
        for _ in range(bone_count):
            idx = struct.unpack_from('<h', data, pos)[0]
            pos += 2
            bone_indices.append(idx)

        return cls(
            name_offset,
            order,
            bool(skin_required),
            position_mode,
            spacing_mode,
            rotate_mode,
            offset_rotation,
            position_val,
            spacing_val,
            rotate_mix,
            translate_mix,
            target_index,
            bone_indices
        ), pos



# 脱壳 脱壳后是一个自定义的skel二进制骨骼, 难以转换为标准的二进制骨骼, 所以直接解析为 json 格式骨骼最好
def convert_scsp(input_file, output_file):
    """SCSP → .skel"""
    with open(input_file, 'rb') as f:
        data = f.read()

    try:
        # 读取头部信息
        uncompressed_size = struct.unpack('<I', data[0:4])[0]
        compressed_size = struct.unpack('<I', data[4:8])[0]

        print(f"  解压大小: {uncompressed_size}, 压缩大小: {compressed_size}")

        # LZ4 解压 (从 offset 8 开始)
        compressed_data = data[8:8 + compressed_size]
        decompressed = lz4.block.decompress(
            compressed_data,
            uncompressed_size=uncompressed_size
        )

        data_size = struct.unpack("<I", decompressed[0:4])[0]
        print("data_size = ", data_size)
        string_size = struct.unpack("<I", decompressed[4:8])[0]
        print("string_size = ", string_size)

        # 跳过前 8 字节，剩下的就是骨骼数据
        skel_data = decompressed[8:]

        # 提取字符串池 (位于 skel_data 末尾)
        string_pool = skel_data[data_size: data_size + string_size]

        def get_pool_string(offset):
            """从字符串池按偏移取 null-terminated UTF-8 字符串; 0xFFFFFFFF 表示 None"""
            if offset == 0xFFFFFFFF:
                return None
            end = string_pool.index(b'\x00', offset)
            return string_pool[offset:end].decode('utf-8', errors='replace')

        # 版本： uint32  (skel_data[0..3] = "scsp", [4..7] = version)
        # 1 -> V2
        # 30001 -> V3
        if skel_data[:4] == b"scsp":
            version = struct.unpack("<I", skel_data[4:8])[0]
            if version < 2:
                print("SCSP version = V2,", version)
            else:
                print("SCSP version = V3,", version)

        # ── 字符串偏移 (stream[74..97] = skel_data[74..97]) ─────────────────
        # [74..77] = hash_off   (u32)
        # [78..81] = ver_off    (u32)
        # [82..85] = 跳过
        # [86..89] = 跳过
        # [90..93] = images_off (u32)
        # [94..97] = audio_off  (u32)
        hash_off   = struct.unpack_from('<I', skel_data, 74)[0]
        ver_off    = struct.unpack_from('<I', skel_data, 78)[0]
        images_off = struct.unpack_from('<I', skel_data, 90)[0]
        audio_off  = struct.unpack_from('<I', skel_data, 94)[0]

        hash_str   = get_pool_string(hash_off)
        ver_str    = get_pool_string(ver_off)
        images_str = get_pool_string(images_off)
        audio_str  = get_pool_string(audio_off)
        print(f"hash_off={hash_off}, ver_off={ver_off}, images_off={images_off}, audio_off={audio_off}")
        print(f"  hash={hash_str!r}, spine_ver={ver_str!r}")
        print(f"  images={images_str!r}, audio={audio_str!r}")

        # 后续 section 数据从 skel_data[98] 开始
        pos = 98

        # ── BoneData ────────────────
        bone_count = struct.unpack_from('<H', skel_data, pos)[0]
        pos += 2
        print(f"  bone_count = {bone_count}")
        bones = []
        for i in range(bone_count):
            bone, pos = BoneData.parse_from(skel_data, pos)
            bones.append(bone)
        # for b in bones[:10]:
        #     print(b)
        print(f"  section end pos = {pos}")

        # ── IKConstraints ────────────────
        ik_count = struct.unpack_from('<H', skel_data, pos)[0]
        pos += 2
        iks = []
        for _ in range(ik_count):
            ik, pos = IkConstraintData.parse_from(skel_data, pos)
            iks.append(ik)
        # for i in iks[:5]:
        #     print(i)
        print("IK parsed:", len(iks))

        # ── Slots ────────────────
        slot_count = struct.unpack_from('<H', skel_data, pos)[0]
        pos += 2
        slots = []
        for _ in range(slot_count):
            slot, pos = SlotData.parse_from(skel_data, pos)
            slots.append(slot)
        # for s in slots[:10]:
        #     print(s)
        print("Slots parsed:", len(slots))

        # ── TransformConstraints ────────────────
        tc_count = struct.unpack_from('<H', skel_data, pos)[0]
        pos += 2

        tcs = []
        for _ in range(tc_count):
            tc, pos = TransformConstraintData.parse_from(skel_data, pos)
            tcs.append(tc)
        # for i in tcs[:5]:
        #     print(i)
        print("TransformConstraints:", len(tcs))

        # ── PathConstraints ──────────────── DEBUG
        pc_count = struct.unpack_from('<H', skel_data, pos)[0]
        pos += 2

        pcs = []
        for _ in range(pc_count):
            pc, pos = PathConstraintData.parse_from(skel_data, pos)
            pcs.append(pc)
        for i in pcs[:5]:
            print(i)
        print("PathConstraints:", len(pcs))

        # ── Skins ────────────────

        # ── Events ────────────────

        # ── Animations ────────────────


        # 保存为 .skel
        with open(output_file, 'wb') as f:
            f.write(skel_data)

        print(f"✓ {os.path.basename(input_file)} → {os.path.basename(output_file)} ({len(skel_data)} bytes)\n")
        return True

    except Exception as e:
        print(f"✗ {os.path.basename(input_file)} 失败: {e}")
        return False


def batch_convert():
    """批量转换"""
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    scsp_files = list(Path(INPUT_PATH).rglob(f"*{_EXT}"))
    if not scsp_files:
        print(f"未找到 {_EXT} 文件")
        return

    print(f"找到 {len(scsp_files)} 个文件\n")

    success = 0
    for f in scsp_files:
        print(f"处理: {os.path.basename(f)}")
        if convert_scsp(str(f), os.path.join(OUTPUT_PATH, f.stem + ".skel")):
            success += 1

    print(f"\n完成! {success}/{len(scsp_files)}")


if __name__ == "__main__":
    batch_convert()