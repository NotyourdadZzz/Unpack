import os
import lz4.block
from pathlib import Path
from dataclasses import dataclass, field
import struct
from enum import IntEnum
from typing import List, Optional, Any, Tuple
# ==============================
# Config
# ==============================
INPUT_PATH = r"/SpineFileProcess/Converter/Data/V2"
OUTPUT_PATH = r"/SpineFileProcess/Converter/Data/test"
_EXT = ".scsp"
string_pool = b''


# ==============================
# Binary Reader
# ==============================
def _rd(fmt: str, data: bytes, pos: int):
    """读取单值，返回 (value, new_pos)"""
    size = struct.calcsize(fmt)
    if pos + size > len(data):
        raise struct.error(f"read overflow: fmt={fmt} pos={pos} need={size} len={len(data)}")
    return struct.unpack_from(fmt, data, pos)[0], pos + size

def _rd_n(code: str, count: int, data: bytes, pos: int):
    """读取 count 个同类型值，返回 (list, new_pos)"""
    if count <= 0:
        return [], pos
    fmt = f"<{count}{code}"
    size = struct.calcsize(fmt)
    if pos + size > len(data):
        raise struct.error(f"read overflow: fmt={fmt} pos={pos} need={size} len={len(data)}")
    return list(struct.unpack_from(fmt, data, pos)), pos + size

def read_u8 (data, pos): return _rd("<B", data, pos)
def read_i16(data, pos): return _rd("<h", data, pos)
def read_u16(data, pos): return _rd("<H", data, pos)
def read_i32(data, pos): return _rd("<i", data, pos)
def read_u32(data, pos): return _rd("<I", data, pos)
def read_f32(data, pos): return _rd("<f", data, pos)

def read_f32_n(data, pos, count): return _rd_n("f", count, data, pos)
def read_i16_n(data, pos, count): return _rd_n("h", count, data, pos)
def read_u16_n(data, pos, count): return _rd_n("H", count, data, pos)
def read_u32_n(data, pos, count): return _rd_n("I", count, data, pos)
def read_u8_n (data, pos, count): return _rd_n("B", count, data, pos)

def skip_bytes(data, pos, count):
    if pos + count > len(data):
        raise struct.error(f"skip overflow: pos={pos} skip={count} len={len(data)}")
    return pos + count

def peek_u16(data, pos):
    if pos + 2 > len(data):
        raise struct.error(f"peek_u16 overflow: pos={pos} len={len(data)}")
    return struct.unpack_from("<H", data, pos)[0]

def _read_vertex_attachment(data, pos, extra=None):
    """
    读取 VertexAttachment 公共头:
      u16 bones_count + u16[n] bones
      u16 vf_count + f32[vf_count] 顶点数据
      u32 worldVerticesLength
      u32 deform_name_offset  (0xFFFFFFFF = 无)
    """
    bones_count,        pos = read_u16(data, pos)
    bones,              pos = read_u16_n(data, pos, bones_count)
    vf_count,           pos = read_u16(data, pos)
    vertices,           pos = read_f32_n(data, pos, vf_count)
    world_len,          pos = read_u32(data, pos)
    deform_off,         pos = read_u32(data, pos)
    if extra is not None:
        extra['va_bones']             = bones
        extra['va_vertices']           = vertices
        extra['va_vertex_floats']     = vf_count
        extra['world_vertices_length']= world_len
        extra['deform_name_off']      = deform_off
    return pos
# ==============================
# Enums & helpers
# ==============================
class Inherit(IntEnum):
    Normal = 0
    OnlyTranslation = 1
    NoRotationOrReflection = 2
    NoScale = 3
    NoScaleOrReflection = 4
class BlendMode(IntEnum):
    Normal = 0
    Additive = 1
    Multiply = 2
    Screen = 3
class PositionMode(IntEnum):
    Fixed = 0
    Percent = 1
class SpacingMode(IntEnum):
    Length = 0
    Fixed = 1
    Percent = 2
    Proportional = 3
class RotateMode(IntEnum):
    Tangent = 0
    Chain = 1
    ChainScale = 2

class AttachmentType(IntEnum):
    Region = 0
    Boundingbox = 1
    Mesh = 2
    Linkedmesh = 3
    Path = 4
    Point = 5
    Clipping = 6

@dataclass
class Color:
    r: int = 0xFF
    g: int = 0xFF
    b: int = 0xFF
    a: int = 0xFF
def color_to_string(r, g, b, a, has_alpha: bool = True) -> str:
    if has_alpha:
        return f"{r:02X}{g:02X}{b:02X}{a:02X}"
    return f"{r:02X}{g:02X}{b:02X}"


def get_pool_string(offset: int) -> Optional[str]:
    """从字符串池按偏移取 null-terminated UTF-8 字符串; 0xFFFFFFFF 表示 None"""
    if offset == 0xFFFFFFFF:
        return None
    if offset >= len(string_pool):
        return f'<OOB:{offset:#x}>'
    try:
        end = string_pool.index(b'\x00', offset)
    except ValueError:
        end = len(string_pool)
    return string_pool[offset:end].decode('utf-8', errors='replace')






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

    inherit: int = Inherit.Normal
    skinRequired: bool = False

    def __repr__(self):
        return (
            f"Bone(index={self.index}, "
            f"parent={self.parent_index}, "
            f"length={self.length:.2f}, "
            f"x={self.x:.2f}, y={self.y:.2f}, "
            f"rot={self.rotation:.2f}, "
            f"scale=({self.scaleX:.2f},{self.scaleY:.2f})),"
            f"shear=({self.shearX:.2f},{self.shearY:.2f})"
            f"inherit={self.inherit})"
            f"skinRequired={self.skinRequired}"
        )
    @classmethod
    def parse_from(cls, data: bytes, pos: int):
        index,        pos = read_i16(data, pos)
        name_offset,  pos = read_u32(data, pos)
        parent_index, pos = read_i16(data, pos)  # -1 for root bones
        floats,       pos = read_f32_n(data, pos, 8)
        inherit,        pos = read_i16(data, pos)
        skin_required,      pos = read_u8 (data, pos)
        bone = cls(
            index=index,
            name_offset=name_offset,
            parent_index=parent_index,
            length=floats[0], x=floats[1], y=floats[2], rotation=floats[3],
            scaleX=floats[4], scaleY=floats[5], shearX=floats[6], shearY=floats[7],
            inherit=inherit,
            skinRequired=bool(skin_required)
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
    bone_indices: list = field(default_factory=list) # bone index 列表，顺序即链条顺序
    def __repr__(self):
        return (
            f"IkConstraint(name={get_pool_string(self.name_offset)}, "
            f"order={self.order}, skin_required={self.skin_required}, "
            f"bend_direction={self.bend_direction}, compress={self.compress}, "
            f"mix={self.mix:.2f}, softness={self.softness:.2f}, "
            f"stretch={self.stretch}, uniform={self.uniform}, "
            f"target_index={self.target_index}, bone_indices={self.bone_indices})"
        )

    @classmethod
    def parse_from(cls, data, pos):
        name_offset,   pos = read_u32(data, pos)
        order,         pos = read_u32(data, pos)
        skin_required, pos = read_u8 (data, pos)
        bend_direction,pos = read_i32(data, pos)
        compress,      pos = read_u8 (data, pos)
        mix,           pos = read_f32(data, pos)
        softness,      pos = read_f32(data, pos)
        stretch,       pos = read_u8 (data, pos)
        uniform,       pos = read_u8 (data, pos)
        target_index,  pos = read_i16(data, pos)
        bone_count,    pos = read_u16(data, pos)
        bone_indices,  pos = read_i16_n(data, pos, bone_count)
        return cls(
            name_offset, order, bool(skin_required),
            bend_direction, bool(compress),
            mix, softness, bool(stretch), bool(uniform),
            target_index, bone_indices
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
    blend_mode: BlendMode.Normal

    def __repr__(self):
        return (
            f"Slot(index={self.index}, bone={self.bone_index}, "
            f"color=({self.r:.2f},{self.g:.2f},{self.b:.2f},{self.a:.2f}), "
            f"has_dark_color={self.has_dark_color}, "
            f"dark=({self.dark_r:.2f},{self.dark_g:.2f},{self.dark_b:.2f},{self.dark_a:.2f}), "
            f"blend_mode={self.blend_mode})"
        )
    @classmethod
    def parse_from(cls, data, pos):
        index,                  pos = read_u16(data, pos)
        name_offset,            pos = read_u32(data, pos)
        bone_index,             pos = read_u16(data, pos)
        (r, g, b, a),           pos = read_f32_n(data, pos, 4)
        (dr, dg, db, da),       pos = read_f32_n(data, pos, 4)
        has_dark_color,         pos = read_u8 (data, pos)
        attachment_name_offset, pos = read_u32(data, pos)
        blend_mode,             pos = read_u16(data, pos)
        return cls(
            index, name_offset, bone_index,
            r, g, b, a, 
            dr, dg, db, da,
            bool(has_dark_color),
            attachment_name_offset, blend_mode
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

    def __repr__(self):
        return (
            f"TransformConstraint(name={get_pool_string(self.name_offset)}, "
            f"order={self.order}, skin_required={self.skin_required}, "
            f"rotate_mix={self.rotate_mix:.2f}, translate_mix={self.translate_mix:.2f}, "
            f"scale_mix={self.scale_mix:.2f}, shear_mix={self.shear_mix:.2f}, "
            f"offset_rotation={self.offset_rotation:.2f}, offset_x={self.offset_x:.2f}, "
            f"offset_y={self.offset_y:.2f}, offset_scale_x={self.offset_scale_x:.2f}, "
            f"offset_scale_y={self.offset_scale_y:.2f}, offset_shear_y={self.offset_shear_y:.2f}, "
            f"local={self.local}, relative={self.relative}, "
            f"target_index={self.target_index}, bone_indices={self.bone_indices})"
        )
    @classmethod
    def parse_from(cls, data, pos):
        name_offset,     pos = read_u32(data, pos)
        order,           pos = read_u32(data, pos)
        skin_required,   pos = read_u8 (data, pos)
        rotate_mix,      pos = read_f32(data, pos)
        translate_mix,   pos = read_f32(data, pos)
        scale_mix,       pos = read_f32(data, pos)
        shear_mix,       pos = read_f32(data, pos)
        offset_rotation, pos = read_f32(data, pos)
        offset_x,        pos = read_f32(data, pos)
        offset_y,        pos = read_f32(data, pos)
        offset_scale_x,  pos = read_f32(data, pos)
        offset_scale_y,  pos = read_f32(data, pos)
        offset_shear_y,  pos = read_f32(data, pos)
        local,           pos = read_u8 (data, pos)
        relative,        pos = read_u8 (data, pos)
        target_index,    pos = read_i16(data, pos)
        bone_count,      pos = read_u16(data, pos)
        bone_indices,    pos = read_i16_n(data, pos, bone_count)
        return cls(
            name_offset, order, bool(skin_required),
            rotate_mix, translate_mix, scale_mix, shear_mix,
            offset_rotation, offset_x, offset_y, offset_scale_x, offset_scale_y, offset_shear_y,
            bool(local), bool(relative),
            target_index, bone_indices
        ), pos


@dataclass
class PathConstraintData:
    name_offset: int
    order: int
    skin_required: bool
    position_mode: PositionMode
    spacing_mode: SpacingMode
    rotate_mode: RotateMode
    offset_rotation: float
    position: float
    spacing: float
    rotate_mix: float
    translate_mix: float
    target_index: int
    bone_indices: list = field(default_factory=list)
    def __repr__(self):
        return (
            f"PathConstraint(name={get_pool_string(self.name_offset)}, "
            f"order={self.order}, skin_required={self.skin_required}, "
            f"position_mode={self.position_mode}, spacing_mode={self.spacing_mode}, rotate_mode={self.rotate_mode}, "
            f"offset_rotation={self.offset_rotation:.2f}, position={self.position:.2f}, spacing={self.spacing:.2f}, "
            f"rotate_mix={self.rotate_mix:.2f}, translate_mix={self.translate_mix:.2f}, "
            f"target_index={self.target_index}, bone_indices={self.bone_indices})"
        )

    @classmethod
    def parse_from(cls, data, pos):
        name_offset,     pos = read_u32(data, pos)
        order,           pos = read_u32(data, pos)
        skin_required,   pos = read_u8 (data, pos)
        position_mode,   pos = read_i16(data, pos)
        spacing_mode,    pos = read_i16(data, pos)
        rotate_mode,     pos = read_i16(data, pos)
        offset_rotation, pos = read_f32(data, pos)
        position_val,    pos = read_f32(data, pos)
        spacing_val,     pos = read_f32(data, pos)
        rotate_mix,      pos = read_f32(data, pos)
        translate_mix,   pos = read_f32(data, pos)

        target_index,    pos = read_i16(data, pos)
        bone_count,      pos = read_u16(data, pos)
        bone_indices,    pos = read_i16_n(data, pos, bone_count)
        return cls(
            name_offset, order, bool(skin_required),
            position_mode, spacing_mode, rotate_mode,
            offset_rotation, position_val, spacing_val,
            rotate_mix, translate_mix,
            target_index, bone_indices
        ), pos


@dataclass
class EventData:
    name_offset: int
    int_value: int
    float_value: float
    string_offset: int
    audio_path_offset: int
    volume: float
    balance: float

    @classmethod
    def parse_from(cls, data, pos):
        name_offset,       pos = read_u32(data, pos)
        int_value,         pos = read_i32(data, pos)
        float_value,       pos = read_f32(data, pos)
        string_offset,     pos = read_u32(data, pos)
        audio_path_offset, pos = read_u32(data, pos)
        volume,            pos = read_f32(data, pos)
        balance,           pos = read_f32(data, pos)
        return cls(name_offset, int_value, float_value,
                   string_offset, audio_path_offset, volume, balance), pos



@dataclass
class RegionAttachment:
    rotation: float = 0.0
    x: float = 0.0
    y: float = 0.0
    scaleX: float = 1.0
    scaleY: float = 1.0
    width: float = 0.0
    height: float = 0.0
    color: Optional[Color] = None
    path_offset: int = 0xFFFFFFFF # custom

@dataclass
class MeshAttachment:
    uvs: List[float] = field(default_factory=list)
    triangles: List[int] = field(default_factory=list)
    vertices: List[float] = field(default_factory=list)
    hullLength: int = 0
    edges: List[int] = field(default_factory=list)
    width: float = 0.0
    height: float = 0.0
    color: Optional[Color] = None


@dataclass
class LinkedMeshAttachment:
    skin: Optional[str] = None
    parentMesh: str = ""
    timelines: int = 0
    width: float = 0.0
    height: float = 0.0
    color: Optional[Color] = None


@dataclass
class BoundingBoxAttachment:
    vertexCount: int = 0
    vertices: List[float] = field(default_factory=list)
    color: Optional[Color] = None


@dataclass
class PathAttachment:
    closed: bool = False
    constantSpeed: bool = False
    vertexCount: int = 0
    vertices: List[float] = field(default_factory=list)
    lengths: List[float] = field(default_factory=list)
    color: Optional[Color] = None


@dataclass
class PointAttachment:
    rotation: float = 0.0
    x: float = 0.0
    y: float = 0.0
    color: Optional[Color] = None


@dataclass
class ClippingAttachment:
    endSlot: Optional[str] = None
    vertexCount: int = 0
    vertices: List[float] = field(default_factory=list)
    color: Optional[Color] = None

@dataclass
class AttachmentData:
    slot_index: int = 0
    attach_name_offset: int = 0xFFFFFFFF
    type: AttachmentType = AttachmentType.Region
    # type:
    #   0 = RegionAttachment
    #   1 = BoundingBoxAttachment
    #   2 = MeshAttachment (完整数据)
    #   3 = LinkedMeshAttachment
    #   4 = PathAttachment
    #   5 = PointAttachment
    #   6 = ClippingAttachment
    template_name_offset: int = 0xFFFFFFFF
    data: Any = None
    
    @property
    def name(self) -> Optional[str]:
        return get_pool_string(self.attach_name_offset)

    @property
    def template_name(self) -> Optional[str]:
        return get_pool_string(self.template_name_offset)

    @property
    def path(self) -> Optional[str]:
        if hasattr(self.data, 'path_offset'):
            off = self.data.path_offset
            return self.name if off == 0xFFFFFFFF else get_pool_string(off)
        return self.name

    @classmethod
    def parse_from(cls, data, pos, scsp_version=30001):
        slot_index,        pos = read_i16(data, pos)
        attach_name_off,   pos = read_u32(data, pos)
        type_,             pos = read_u16(data, pos)
        template_name_off, pos = read_u32(data, pos)
        att_data = None
        extra = {}

        if type_ == 0:
            # ── RegionAttachment ─────────────────────────────────────
            # 13 × f32
            floats13,           pos = read_f32_n(data, pos, 13)
            
            # u16 count1 + count1×f32  uvs
            count1,             pos = read_u16(data, pos)
            _,                  pos = read_f32_n(data, pos, count1)

            # u16 count2 + count2×f32  vertices
            count2,             pos = read_u16(data, pos)
            _,                  pos = read_f32_n(data, pos, count2)

            # region name offset 
            path_off,  pos = read_u32(data, pos)
            # p = get_pool_string(path_off)

            # 4 × f32: r,g,b,a
            clr,                pos = read_f32_n(data, pos, 4)
            
            att_data = RegionAttachment(
                # 0-7 offset
                x=floats13[8], 
                y=floats13[9], 
                rotation=floats13[10], 
                scaleX=floats13[11], 
                scaleY=floats13[12],
                width=0.0, 
                height=0.0,
                color=Color(int(clr[0]*255), int(clr[1]*255), int(clr[2]*255), int(clr[3]*255)),
                path_offset=path_off 
            )


        elif type_ == 1:
            # ── BoundingBoxAttachment ────────────────────────────────
            pos = _read_vertex_attachment(data, pos, extra)
            att_data = BoundingBoxAttachment(
                vertexCount=extra.get('world_vertices_length', 0) // 2,
                vertices=extra.get('va_vertices', []),
            )

        elif type_ in (2, 3):
            # ── MeshAttachment / LinkedMeshAttachment ─────────────────
            pos = _read_vertex_attachment(data, pos, extra)

            floats6,  pos = read_f32_n(data, pos, 6)       # 6×f32

            count_uvs,         pos = read_u16(data, pos)             # uvs
            uvs_data,          pos = read_f32_n(data, pos, count_uvs)

            # region-space 顶点数据 可以忽略 数量会和 uv 一致
            count_verts,       pos = read_u16(data, pos)             # verts
            verts_data,        pos = read_f32_n(data, pos, count_verts)

            count_tris,        pos = read_u16(data, pos)             # tris
            tris_data,         pos = read_u16_n(data, pos, count_tris)

            count_edges,       pos = read_u16(data, pos)             # edges
            edges_data,        pos = read_u16_n(data, pos, count_edges)


            # atlas region path
            path_off,          pos = read_u32(data, pos)             # path name
            clr10,             pos = read_f32_n(data, pos, 10)       # 10×f32
            
            _u32_val,          pos = read_u32(data, pos)             # u32 ???
            _u8_val,           pos = read_u8(data, pos)              # u8 boolean 可能是flag
            _u32_val2,         pos = read_u32(data, pos)             # u32 if flag: _u32_val2 = 90 else: _u32_val2 = 0

            ref_name_off,      pos = read_u32(data, pos)
            ref_slot_idx,      pos = read_i16(data, pos)
            # print("ref_name_off", ref_name_off, "ref_slot_idx", ref_slot_idx)
            if scsp_version > 0x7530: #V3
                _,             pos = read_i16(data, pos)              # i16 v260

            else: #V2
                skin_name_off,   pos = read_u32(data, pos)
                skin_name = get_pool_string(skin_name_off) if skin_name_off != 0xFFFFFFFF else "default"

            inherit_deform,    pos = read_u8(data, pos)

            if type_ == 3:
                # LinkedMeshAttachment
                ref_name = get_pool_string(ref_name_off)
                skin_name = get_pool_string(ref_slot_idx) if ref_slot_idx >= 0 else None
                att_data = LinkedMeshAttachment(
                    skin=skin_name,
                    parentMesh=ref_name,
                    timelines=inherit_deform,
                    width=floats6[4] if len(floats6) > 4 else 0.0,
                    height=floats6[5] if len(floats6) > 5 else 0.0,
                    color=Color(int(clr10[0]*255) if len(clr10) > 0 else 255,
                                int(clr10[1]*255) if len(clr10) > 1 else 255,
                                int(clr10[2]*255) if len(clr10) > 2 else 255,
                                int(clr10[3]*255) if len(clr10) > 3 else 255),
                )
            else:
                hull = extra.get('world_vertices_length', 0)
                att_data = MeshAttachment(
                    uvs=uvs_data,
                    triangles=tris_data,
                    vertices=verts_data,
                    hullLength=hull,
                    edges=edges_data,
                    width=floats6[4] if len(floats6) > 4 else 0.0,
                    height=floats6[5] if len(floats6) > 5 else 0.0,
                    color=Color(int(clr10[0]*255) if len(clr10) > 0 else 255,
                                int(clr10[1]*255) if len(clr10) > 1 else 255,
                                int(clr10[2]*255) if len(clr10) > 2 else 255,
                                int(clr10[3]*255) if len(clr10) > 3 else 255),
                )
                att_data.path_offset = path_off

        elif type_ == 4:
            # ── PathAttachment ──────────────────────────────────────
            pos = _read_vertex_attachment(data, pos, extra)
            count1,                pos = read_u16(data, pos)
            lengths,               pos = read_f32_n(data, pos, count1)
            closed_val,            pos = read_u8(data, pos)
            constant_speed_val,    pos = read_u8(data, pos)
            att_data = PathAttachment(
                closed=bool(closed_val),
                constantSpeed=bool(constant_speed_val),
                vertexCount=extra.get('world_vertices_length', 0) // 2,
                vertices=extra.get('va_vertices', []),
                lengths=lengths,
            )

        elif type_ == 5:
            # ── PointAttachment ─────────────────────────────────────
            # pos = _read_vertex_attachment(data, pos, extra)
            point_floats, pos = read_f32_n(data, pos, 3)  # x, y, rotation
            att_data = PointAttachment(
                x=point_floats[0],
                y=point_floats[1],
                rotation=point_floats[2],
            )

        elif type_ == 6:
            # ── ClippingAttachment ──────────────────────────────────
            pos = _read_vertex_attachment(data, pos, extra)
            end_slot_index,  pos = read_i16(data, pos)
            att_data = ClippingAttachment(
                endSlot=str(end_slot_index),
                vertexCount=extra.get('world_vertices_length', 0) // 2,
                vertices=extra.get('va_vertices', []),
            )

        return cls(slot_index, attach_name_off, type_, template_name_off, att_data), pos


@dataclass
class SkinData:
    name_offset: int
    bone_indices: list[int]
    path_constraint_name_offsets: list[int]
    slots: List[Tuple[int, List["AttachmentData"]]] # slot_index → [AttachmentData]

    def __repr__(self):
        return (
            f"Skin(name={get_pool_string(self.name_offset)}, "
            f"bones={self.bone_indices}, "
            f"path_constraints={self.path_constraint_name_offsets}, "
            f"slots={[(k, len(v)) for k, v in self.slots]})"

        )
    @classmethod
    def parse_from(cls, data, pos, scsp_version=30001, debug=False):
        name_off,   pos = read_u32(data, pos)

        # 平坦列表：u32 name_off → u16 bone_count+i16[n] → u16 path_count+u32[n] → u16 total_att_count
        # 无嵌套 slot 分组，每个 attachment 自带 i16 slot_index
        bone_count,   pos = read_u16(data, pos)
        bone_indices, pos = read_i16_n(data, pos, bone_count)
        path_count,   pos = read_u16(data, pos)
        path_constraint_name_offsets, pos = read_u32_n(data, pos, path_count)

        total_att_count, pos = read_u16(data, pos)

        atts_by_slot = {}   # slot_index → [AttachmentData]

        for i in range(total_att_count):
            att, pos = AttachmentData.parse_from(data, pos, scsp_version)
            if att.slot_index not in atts_by_slot:
                atts_by_slot[att.slot_index] = []
            atts_by_slot[att.slot_index].append(att)

        slots = sorted([(k, v) for k, v in atts_by_slot.items()])
        return cls(name_off, bone_indices, path_constraint_name_offsets, slots), pos


@dataclass
class TimelineData:
    """
    单条 Timeline（loadTimeline switch-case 反编译）
      case 0  Rotate              → LABEL_36 → LABEL_55
      case 1  Translate           → LABEL_48 → LABEL_55
      case 2  Scale               → LABEL_48 → LABEL_55
      case 3  Shear               → LABEL_48 → LABEL_55
      case 4  Attachment          → 独立
      case 5  Color               → LABEL_36 → LABEL_55
      case 6  Deform              → 独立
      case 7  Event               → 独立
      case 8  DrawOrder           → 独立
      case 9  IkConstraint        → LABEL_48 → LABEL_55
      case 10 TransformConstraint → LABEL_48 → LABEL_55
      case 11 PathConstraintPos   → LABEL_48 → LABEL_55
      case 12 PathConstraintSpc   → LABEL_48 → LABEL_55
      case 13 PathConstraintMix   → LABEL_48 → LABEL_55
      case 14 TwoColor            → LABEL_48 → LABEL_55

    通用流格式（LABEL_36/48, case 0-3,5,9-14）：
      i16 index + u16 frames_n + f32[n] + u16 curves_n + f32[n]
    """
    type: int
    data: dict = field(default_factory=dict)

    @classmethod
    def parse_from(cls, data, pos, scsp_version):
        type_, pos = read_u16(data, pos)
        d = {}

        if type_ in (0, 1, 2, 3, 5, 9, 10, 11, 12, 13, 14):
            # i16 index + u16 frames_n + f32[n] + u16 curves_n + f32[n]
            d['index'],  pos = read_i16(data, pos)
            frames_n,    pos = read_u16(data, pos)
            d['frames'], pos = read_f32_n(data, pos, frames_n)
            curves_n,    pos = read_u16(data, pos)
            d['curves'], pos = read_f32_n(data, pos, curves_n)

        elif type_ == 4:
            # AttachmentTimeline
            # i16 slot + u16 times_n + f32[n] + u16 name_count + u32[n]
            d['slot_index'], pos = read_i16(data, pos)
            times_n,         pos = read_u16(data, pos)
            d['times'],      pos = read_f32_n(data, pos, times_n)
            name_count,      pos = read_u16(data, pos)
            d['names'],      pos = read_u32_n(data, pos, name_count)

        elif type_ == 6:
            # DeformTimeline
            # i16 slot + u16 frames_n + f32[n] + u16 curves_n + f32[n]
            # + u16 deform_count + (u16 vert_n + f32[vert_n]) × n
            # + u32 attach_name_off + [i16 skin_index if ver>0x7530]
            d['slot_index'], pos = read_i16(data, pos)
            frames_n,        pos = read_u16(data, pos)
            d['frames'],     pos = read_f32_n(data, pos, frames_n)
            curves_n,        pos = read_u16(data, pos)
            d['curves'],     pos = read_f32_n(data, pos, curves_n)
            deform_count,    pos = read_u16(data, pos)
            verts = []
            for _ in range(deform_count):
                vert_n, pos = read_u16(data, pos)
                vs,     pos = read_f32_n(data, pos, vert_n)
                verts.append(vs)
            d['deform_verts'] = verts
            d['attach_off'],  pos = read_u32(data, pos)
            if scsp_version > 0x7530:
                d['skin_index'], pos = read_i16(data, pos)

        elif type_ == 7:
            # EventTimeline: u16 times_n + f32[n] + u16 event_count + u32[n]
            times_n,       pos = read_u16(data, pos)
            d['times'],    pos = read_f32_n(data, pos, times_n)
            event_count,   pos = read_u16(data, pos)
            d['events'],   pos = read_u32_n(data, pos, event_count)

        elif type_ == 8:
            # DrawOrderTimeline: u16 times_n + f32[n]
            # + u16 do_count + (u16 slot_n + i32[slot_n]) × n
            times_n,       pos = read_u16(data, pos)
            d['times'],    pos = read_f32_n(data, pos, times_n)
            do_count,      pos = read_u16(data, pos)
            orders = []
            for _ in range(do_count):
                slot_n, pos = read_u16(data, pos)
                slots,  pos = _rd_n("i", slot_n, data, pos)
                orders.append(slots)
            d['draw_orders'] = orders

        else:
            ctx = data[max(0, pos - 16):pos + 8]
            hx  = ' '.join(f'{b:02X}' for b in ctx)
            raise struct.error(
                f"unknown timeline type={type_} (0x{type_:04X}) @{pos-2}  ctx={hx}")

        if type_ == 14:
            print(f"  Timeline type={type_} , frames={d.get('frames', [])}")
            # print(f"  curves={d.get('curves', [])}")
        return cls(type_, d), pos


@dataclass
class AnimationData:
    """
    单个 Animation 条目：u32 name_off + f32 duration + u16 tl_count + timelines
    """
    name_offset: int
    duration: float
    timelines: list = field(default_factory=list)

    @classmethod
    def parse_from(cls, data, pos, scsp_version):
        name_off, pos = read_u32(data, pos)
        duration, pos = read_f32(data, pos)
        tl_count, pos = read_u16(data, pos)
        timelines = []
        for _ in range(tl_count):
            tl, pos = TimelineData.parse_from(data, pos, scsp_version)
            timelines.append(tl)
        return cls(name_off, duration, timelines), pos

@dataclass
class SkeletonData:
    hash: int = 0
    hashString: Optional[str] = None
    version: Optional[str] = None
    x: float = 0.0
    y: float = 0.0
    width: float = 0.0
    height: float = 0.0
    nonessential: bool = False
    fps: float = 30.0
    imagesPath: Optional[str] = None
    audioPath: Optional[str] = None
    strings: List[str] = field(default_factory=list)
    bones: List[BoneData] = field(default_factory=list)
    slots: List[SlotData] = field(default_factory=list)
    ikConstraints: List[IkConstraintData] = field(default_factory=list)
    transformConstraints: List[TransformConstraintData] = field(default_factory=list)
    pathConstraints: List[PathConstraintData] = field(default_factory=list)
    skins: List[SkinData] = field(default_factory=list)
    events: List[EventData] = field(default_factory=list)
    animations: List[AnimationData] = field(default_factory=list)


# 脱壳 脱壳后是一个自定义的skel二进制骨骼, 难以转换为标准的二进制骨骼, 所以直接解析为 json 格式骨骼最好
def convert_scsp(input_file, output_file):
    """SCSP → .skel"""
    with open(input_file, 'rb') as f:
        data = f.read()

    try:
        uncompressed_size, _ = read_u32(data, 0)
        compressed_size,   _ = read_u32(data, 4)

        print(f"  解压大小: {uncompressed_size}, 压缩大小: {compressed_size}")

        # LZ4 解压 (从 offset 8 开始)
        compressed_data = data[8:8 + compressed_size]
        decompressed = lz4.block.decompress(
            compressed_data,
            uncompressed_size=uncompressed_size
        )

        data_size,   _ = read_u32(decompressed, 0)
        string_size, _ = read_u32(decompressed, 4)
        print(f">>> data_size={data_size}, string_size={string_size}, len_decompressed={len(decompressed)}")
        print(f"  binary section: skel_data[0..{data_size-1}], string pool: [{data_size}..{data_size+string_size-1}]")

        # 跳过前 8 字节，剩下的就是骨骼数据
        skel_data = decompressed[8:]

        # 提取字符串池 (位于 skel_data 末尾)
        global string_pool
        string_pool = skel_data[data_size: data_size + string_size]

        # 版本： uint32  (skel_data[0..3] = "scsp", [4..7] = version)
        # 1 -> V2
        # 30001 -> V3
        scsp_version = 0
        if skel_data[:4] == b"scsp":
            scsp_version, _ = read_u32(skel_data, 4)
            if scsp_version < 2:
                print("SCSP version = V2,", scsp_version)
                print("  Warning: V2 版本暂不支持解析")
                return False
            else:
                print("SCSP version = V3,", scsp_version)

        # v2
        # header_size , _ = read_u32(skel_data, 8)
        # 暴力枚举前 8-73 的 f32 数据
        # for i in range(8, 74):
        #     var = read_f32(skel_data, i)[0]
        #     print(f"  offset {i:02} = {var:.3f}")
        # for i in range(12, 12+6*4, 4):
        #     f32_var = read_f32(skel_data, i)[0]
        #     print(f"f32:  offset {i} = {f32_var}")
        #
        # for i in range(36, 36+7*4, 4):
        #     u32_var = read_u32(skel_data, i)[0]
        #     print(f"u32:  offset {i} = {u32_var}")
        #
        # for i in range(64, 64+4*2, 2):
        #     u16_var = read_u16(skel_data, i)[0]
        #     print(f"u16:  offset {i} = {u16_var}")
        #
        # for i in range(72, 72+7*4, 4):
        #     u32_var = read_u32(skel_data, i)[0]
        #     print(f"u32:  offset {i} = {u32_var}")
        #
        # return  False

        x = 0.0
        y = 0.0
        width = read_f32(skel_data, 14)[0]
        height = read_f32(skel_data, 18)[0]
        fps = read_f32(skel_data, 38)[0]
        print(f"width={width:.3f}, height={height:.3f}")
        print(f"  fps = {fps:.3f}")


        # ── 字符串偏移 (stream[74..97] = skel_data[74..97]) ─────────────────
        # [74..77] = hash_off   (u32)
        # [78..81] = ver_off    (u32)
        # [82..85] = 跳过
        # [86..89] = 跳过
        # [90..93] = images_off (u32)
        # [94..97] = audio_off  (u32)
        # for i in range(74, 98):
        #     var = read_u32(skel_data, i)[0]
        #     print(f"  offset {i:02} = {var} (0x{var:08X})")

        hash_off,   _ = read_u32(skel_data, 74)
        ver_off,    _ = read_u32(skel_data, 78)
        images_off, _ = read_u32(skel_data, 86)
        audio_off,  _ = read_u32(skel_data, 94)

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
        bone_count, pos = read_u16(skel_data, pos)
        print(f"Bone count = {bone_count}, pos_before_bones={pos}")
        bones = []
        for i in range(bone_count):
            bone, pos = BoneData.parse_from(skel_data, pos)
            bones.append(bone)
        for b in bones[:10]:
            print(b)

        # ── IKConstraints ────────────────
        ik_count, pos = read_u16(skel_data, pos)
        print(f"IK constraint count = {ik_count}, pos_before_ik={pos}")
        iks = []
        for _ in range(ik_count):
            ik, pos = IkConstraintData.parse_from(skel_data, pos)
            iks.append(ik)
        for i in iks[:5]:
            print(i)

        # ── Slots ────────────────
        slot_count, pos = read_u16(skel_data, pos)
        print(f"Slot count = {slot_count}, pos_before_slots={pos}")
        slots = []
        for _ in range(slot_count):
            slot, pos = SlotData.parse_from(skel_data, pos)
            slots.append(slot)
        for s in slots[:5]:
            print(s)

        # ── TransformConstraints ────────────────
        tc_count, pos = read_u16(skel_data, pos)
        print(f"TransformConstraint count = {tc_count}, pos_before_tc={pos}")
        tcs = []
        for _ in range(tc_count):
            tc, pos = TransformConstraintData.parse_from(skel_data, pos)
            tcs.append(tc)
        for i in tcs[:5]:
            print(i)

        # ── PathConstraints ──────────────── DEBUG
        pc_count, pos = read_u16(skel_data, pos)
        print(f"PathConstraint count = {pc_count}, pos_before_pc={pos}")
        pcs = []
        for _ in range(pc_count):
            pc, pos = PathConstraintData.parse_from(skel_data, pos)
            pcs.append(pc)
        for i in pcs[:5]:
            print(i)

        # ── Skins ────────────────
        skin_count, pos = read_u16(skel_data, pos)
        print(f"skin_count = {skin_count}, pos_before_skins={pos}")
        skins = []
        for si in range(skin_count):
            skin_pos_before = pos
            skin, pos = SkinData.parse_from(skel_data, pos, scsp_version, debug=(si == 0))
            # print(f"  Skin[{si}] name={get_pool_string(skin.name_offset)!r}, "
            #       f"consumed={pos - skin_pos_before}, pos_after={pos}")
            skins.append(skin)
        for s in skins[:5]:
            print(s)

        # ── Events ────────────────
        event_count, pos = read_u16(skel_data, pos)
        events = []
        for _ in range(event_count):
            ev, pos = EventData.parse_from(skel_data, pos)
            events.append(ev)
        print(f"Events parsed: {len(events)}, pos={pos}")
        for ev in events[:5]:
            print(f"  Event name={get_pool_string(ev.name_offset)!r} "
                  f"int={ev.int_value} float={ev.float_value:.3f} "
                  f"str={get_pool_string(ev.string_offset)!r}")

        # ── Animations ────────────────
        anim_count, pos = read_u16(skel_data, pos)
        animations = []
        for _ in range(anim_count):
            anim, pos = AnimationData.parse_from(skel_data, pos, scsp_version)
            animations.append(anim)
        print(f"Animations parsed: {len(animations)}, final pos={pos}, data_size={data_size}")
        for an in animations:
            print(f"  Anim name={get_pool_string(an.name_offset)!r} "
                  f"duration={an.duration:.3f}s timelines={len(an.timelines)}")


        # 保存为 .skel
        with open(output_file, 'wb') as f:
            f.write(skel_data)

        print(f"✓ {os.path.basename(input_file)} → {os.path.basename(output_file)} ({len(skel_data)} bytes)\n")
        return True

    except Exception as e:
        import traceback
        print(f"✗ {os.path.basename(input_file)} 失败: {e}")
        traceback.print_exc()
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