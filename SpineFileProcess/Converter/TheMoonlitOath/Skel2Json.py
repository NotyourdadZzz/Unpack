#!/usr/bin/env python3

#花亦山心之月 Convert skel 3.8 to json 
from __future__ import annotations

import base64
import json
import struct
import sys
from typing import cast
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, Dict, List, Optional, Tuple

# ==============================
# Config
# ==============================
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\花亦山\output\test\Hero_Alaiye.skel"
OUTPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\花亦山\output\test\Hero_Alaiye.json"
ENDIAN = ">"



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


class PathTimelineType(IntEnum):
    POSITION = 0
    SPACING = 1
    MIX = 2


class CurveType(IntEnum):
    LINEAR = 0
    STEPPED = 1
    BEZIER = 2


def color_to_string(color: "Color", has_alpha: bool = True) -> str:
    if has_alpha:
        return f"{color.r:02X}{color.g:02X}{color.b:02X}{color.a:02X}"
    return f"{color.r:02X}{color.g:02X}{color.b:02X}"


def uint64_to_base64(v: int) -> str:
    return base64.b64encode(struct.pack("<Q", v)).decode("ascii").rstrip("=")


def base64_to_uint64(s: str) -> int:
    # pad to valid length
    padding = "=" * ((4 - len(s) % 4) % 4)
    data = base64.b64decode(s + padding)
    # tolerate malformed/short hashes by interpreting whatever bytes we get
    # as a little-endian unsigned integer (C++ implementation accumulates byte-wise)
    return int.from_bytes(data, byteorder="little", signed=False)


# ==============================
# Data classes
# ==============================


@dataclass
class Color:
    r: int = 0xFF
    g: int = 0xFF
    b: int = 0xFF
    a: int = 0xFF


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


AttachmentData = Any


@dataclass
class Attachment:
    name: str
    path: str
    type: AttachmentType
    data: AttachmentData


@dataclass
class TimelineFrame:
    time: float = 0.0
    str1: Optional[str] = None
    str2: Optional[str] = None
    int1: int = 0
    value1: float = 0.0
    value2: float = 0.0
    value3: float = 0.0
    value4: float = 0.0
    value5: float = 0.0
    value6: float = 0.0
    color1: Optional[Color] = None
    color2: Optional[Color] = None
    curveType: CurveType = CurveType.LINEAR
    curve: List[float] = field(default_factory=list)
    bendPositive: bool = True
    compress: bool = False
    stretch: bool = False
    vertices: List[float] = field(default_factory=list)
    offsets: List[Tuple[str, int]] = field(default_factory=list)


Timeline = List[TimelineFrame]
MultiTimeline = Dict[str, Timeline]


@dataclass
class BoneData:
    name: Optional[str] = None
    parent: Optional[str] = None
    rotation: float = 0.0
    x: float = 0.0
    y: float = 0.0
    scaleX: float = 1.0
    scaleY: float = 1.0
    shearX: float = 0.0
    shearY: float = 0.0
    length: float = 0.0
    inherit: Inherit = Inherit.Normal
    skinRequired: bool = False
    color: Optional[Color] = None


@dataclass
class SlotData:
    name: Optional[str] = None
    bone: Optional[str] = None
    color: Optional[Color] = None
    darkColor: Optional[Color] = None
    attachmentName: Optional[str] = None
    blendMode: BlendMode = BlendMode.Normal


@dataclass
class IKConstraintData:
    name: Optional[str] = None
    order: int = 0
    skinRequired: bool = False
    bones: List[str] = field(default_factory=list)
    target: Optional[str] = None
    mix: float = 1.0
    softness: float = 0.0
    bendPositive: bool = True
    compress: bool = False
    stretch: bool = False
    uniform: bool = False


@dataclass
class TransformConstraintData:
    name: Optional[str] = None
    order: int = 0
    skinRequired: bool = False
    bones: List[str] = field(default_factory=list)
    target: Optional[str] = None
    local: bool = False
    relative: bool = False
    offsetRotation: float = 0.0
    offsetX: float = 0.0
    offsetY: float = 0.0
    offsetScaleX: float = 0.0
    offsetScaleY: float = 0.0
    offsetShearY: float = 0.0
    mixRotate: float = 1.0
    mixX: float = 1.0
    mixY: float = 1.0
    mixScaleX: float = 1.0
    mixScaleY: float = 1.0
    mixShearY: float = 1.0


@dataclass
class PathConstraintData:
    name: Optional[str] = None
    order: int = 0
    skinRequired: bool = False
    bones: List[str] = field(default_factory=list)
    target: Optional[str] = None
    positionMode: PositionMode = PositionMode.Percent
    spacingMode: SpacingMode = SpacingMode.Length
    rotateMode: RotateMode = RotateMode.Tangent
    offsetRotation: float = 0.0
    position: float = 0.0
    spacing: float = 0.0
    mixRotate: float = 1.0
    mixX: float = 1.0
    mixY: float = 1.0


@dataclass
class Skin:
    name: str = ""
    attachments: Dict[str, Dict[str, Attachment]] = field(default_factory=dict)
    bones: List[str] = field(default_factory=list)
    ik: List[str] = field(default_factory=list)
    transform: List[str] = field(default_factory=list)
    path: List[str] = field(default_factory=list)


@dataclass
class EventData:
    name: str = ""
    intValue: int = 0
    floatValue: float = 0.0
    stringValue: Optional[str] = None
    audioPath: Optional[str] = None
    volume: float = 1.0
    balance: float = 0.0


@dataclass
class Animation:
    name: str = ""
    slots: Dict[str, MultiTimeline] = field(default_factory=dict)
    bones: Dict[str, MultiTimeline] = field(default_factory=dict)
    ik: Dict[str, Timeline] = field(default_factory=dict)
    transform: Dict[str, Timeline] = field(default_factory=dict)
    path: Dict[str, MultiTimeline] = field(default_factory=dict)
    attachments: Dict[str, Dict[str, Dict[str, MultiTimeline]]] = field(default_factory=dict)
    drawOrder: Timeline = field(default_factory=list)
    events: Timeline = field(default_factory=list)


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
    ikConstraints: List[IKConstraintData] = field(default_factory=list)
    transformConstraints: List[TransformConstraintData] = field(default_factory=list)
    pathConstraints: List[PathConstraintData] = field(default_factory=list)
    skins: List[Skin] = field(default_factory=list)
    events: List[EventData] = field(default_factory=list)
    animations: List[Animation] = field(default_factory=list)


# ==============================
# Binary Reader (Spine 3.8)
# ==============================


class SpineBinaryReader:
    def __init__(self, data: bytes, endian: str = ENDIAN):
        self.data = data
        self.pos = 0
        self.endian = endian

    def _read(self, size: int) -> bytes:
        if self.pos + size > len(self.data):
            raise EOFError("Unexpected end of file")
        chunk = self.data[self.pos : self.pos + size]
        self.pos += size
        return chunk

    def read_byte(self) -> int:
        return self._read(1)[0]

    def read_sbyte(self) -> int:
        return struct.unpack(f"{self.endian}b", self._read(1))[0]

    def read_int(self) -> int:
        return struct.unpack(f"{self.endian}i", self._read(4))[0]

    def read_float(self) -> float:
        return struct.unpack(f"{self.endian}f", self._read(4))[0]

    def read_ushort(self) -> int:
        return struct.unpack(f"{self.endian}H", self._read(2))[0]

    def read_boolean(self) -> bool:
        return self.read_byte() != 0


    def read_color(self, has_alpha: bool = True) -> Color:
        r = self.read_byte()
        g = self.read_byte()
        b = self.read_byte()
        a = self.read_byte() if has_alpha else 0xFF
        return Color(r, g, b, a)

    def read_varint(self, optimize_positive: bool) -> int:
        result = 0
        shift = 0
        while True:
            b = self.read_byte()
            result |= (b & 0x7F) << shift
            if (b & 0x80) == 0:
                break
            shift += 7
        if not optimize_positive:
            result = (result >> 1) ^ -(result & 1)
        return result

    def read_string(self, strings: Optional[List[str]] = None) -> Optional[str]:
        length = self.read_varint(True)
        if length == 0:
            return None
        if length == 1:
            return ""
        length -= 1
        raw = self._read(length)
        s = raw.decode("utf-8", errors="replace")
        if strings is not None:
            strings.append(s)
        return s

    def read_string_ref(self, strings: List[str]) -> Optional[str]:
        index = self.read_varint(True)
        if index == 0:
            return None
        index -= 1
        if index >= len(strings):
            strings.append(self.read_string())
        return strings[index]


# ==============================
# Binary -> SkeletonData
# ==============================


def read_float_array(reader: SpineBinaryReader, n: int) -> List[float]:
    return [reader.read_float() for _ in range(n)]


def read_short_array(reader: SpineBinaryReader) -> List[int]:
    n = reader.read_varint(True)
    return [reader.read_ushort() for _ in range(n)]


def read_vertices(reader: SpineBinaryReader, vertex_count: int) -> List[float]:
    vertices: List[float] = []
    if not reader.read_boolean():
        vertices.extend(read_float_array(reader, vertex_count << 1))
    else:
        for _ in range(vertex_count):
            bone_count = reader.read_varint(True)
            vertices.append(float(bone_count))
            for _ in range(bone_count):
                vertices.append(float(reader.read_varint(True)))
                vertices.append(reader.read_float())
                vertices.append(reader.read_float())
                vertices.append(reader.read_float())
    return vertices


def read_curve(reader: SpineBinaryReader, frame: TimelineFrame) -> None:
    curve_type = reader.read_byte()
    if curve_type == CurveType.STEPPED.value:
        frame.curveType = CurveType.STEPPED
    elif curve_type == CurveType.BEZIER.value:
        frame.curveType = CurveType.BEZIER
        frame.curve = [reader.read_float() for _ in range(4)]


def read_timeline(reader: SpineBinaryReader, frame_count: int, value_num: int) -> Timeline:
    timeline: Timeline = []
    for frame_index in range(frame_count):
        frame = TimelineFrame()
        frame.time = reader.read_float()
        frame.value1 = reader.read_float()
        if value_num > 1:
            frame.value2 = reader.read_float()
        if frame_index < frame_count - 1:
            read_curve(reader, frame)
        timeline.append(frame)
    return timeline


def read_skin(reader: SpineBinaryReader, default_skin: bool, skeleton: SkeletonData) -> Skin:
    skin = Skin()
    if default_skin:
        slot_count = reader.read_varint(True)
        skin.name = "default"
    else:
        skin.name = reader.read_string_ref(skeleton.strings) or ""
        for _ in range(reader.read_varint(True)):
            skin.bones.append(skeleton.bones[reader.read_varint(True)].name or "")
        for _ in range(reader.read_varint(True)):
            skin.ik.append(skeleton.ikConstraints[reader.read_varint(True)].name or "")
        for _ in range(reader.read_varint(True)):
            skin.transform.append(skeleton.transformConstraints[reader.read_varint(True)].name or "")
        for _ in range(reader.read_varint(True)):
            skin.path.append(skeleton.pathConstraints[reader.read_varint(True)].name or "")
        slot_count = reader.read_varint(True)

    for _ in range(slot_count):
        slot_name = skeleton.slots[reader.read_varint(True)].name or ""
        for _ in range(reader.read_varint(True)):
            attachment_name = reader.read_string_ref(skeleton.strings) or ""
            name_opt = reader.read_string_ref(skeleton.strings)
            attachment_actual_name = name_opt if name_opt not in (None, "") else attachment_name
            att_type = AttachmentType(reader.read_byte())

            def _push(att: Attachment):
                skin.attachments.setdefault(slot_name, {})[attachment_name] = att

            if att_type == AttachmentType.Region:
                region = RegionAttachment()
                path_opt = reader.read_string_ref(skeleton.strings)
                path = path_opt if path_opt not in (None, "") else attachment_actual_name
                region.rotation = reader.read_float()
                region.x = reader.read_float()
                region.y = reader.read_float()
                region.scaleX = reader.read_float()
                region.scaleY = reader.read_float()
                region.width = reader.read_float()
                region.height = reader.read_float()
                color = reader.read_color()
                if color != Color():
                    region.color = color
                _push(Attachment(attachment_actual_name, path, att_type, region))
            elif att_type == AttachmentType.Boundingbox:
                box = BoundingBoxAttachment()
                box.vertexCount = reader.read_varint(True)
                box.vertices = read_vertices(reader, box.vertexCount)
                if skeleton.nonessential:
                    color = reader.read_color()
                    if color != Color():
                        box.color = color
                _push(Attachment(attachment_actual_name, attachment_actual_name, att_type, box))
            elif att_type == AttachmentType.Mesh:
                mesh = MeshAttachment()
                path_opt = reader.read_string_ref(skeleton.strings)
                path = path_opt if path_opt not in (None, "") else attachment_actual_name
                color = reader.read_color()
                if color != Color():
                    mesh.color = color
                vertex_count = reader.read_varint(True)
                mesh.uvs = read_float_array(reader, vertex_count << 1)
                mesh.triangles = read_short_array(reader)
                mesh.vertices = read_vertices(reader, vertex_count)
                mesh.hullLength = reader.read_varint(True)
                if skeleton.nonessential:
                    mesh.edges = read_short_array(reader)
                    mesh.width = reader.read_float()
                    mesh.height = reader.read_float()
                _push(Attachment(attachment_actual_name, path, att_type, mesh))
            elif att_type == AttachmentType.Linkedmesh:
                lmesh = LinkedMeshAttachment()
                path_opt = reader.read_string_ref(skeleton.strings)
                path = path_opt if path_opt not in (None, "") else attachment_actual_name
                color = reader.read_color()
                if color != Color():
                    lmesh.color = color
                lmesh.skin = reader.read_string_ref(skeleton.strings)
                lmesh.parentMesh = reader.read_string_ref(skeleton.strings) or ""
                lmesh.timelines = 1 if reader.read_boolean() else 0
                if skeleton.nonessential:
                    lmesh.width = reader.read_float()
                    lmesh.height = reader.read_float()
                _push(Attachment(attachment_actual_name, path, att_type, lmesh))
            elif att_type == AttachmentType.Path:
                path_att = PathAttachment()
                path_att.closed = reader.read_boolean()
                path_att.constantSpeed = reader.read_boolean()
                path_att.vertexCount = reader.read_varint(True)
                path_att.vertices = read_vertices(reader, path_att.vertexCount)
                path_att.lengths = read_float_array(reader, path_att.vertexCount // 3)
                if skeleton.nonessential:
                    color = reader.read_color()
                    if color != Color():
                        path_att.color = color
                _push(Attachment(attachment_actual_name, attachment_actual_name, att_type, path_att))
            elif att_type == AttachmentType.Point:
                point_att = PointAttachment()
                point_att.rotation = reader.read_float()
                point_att.x = reader.read_float()
                point_att.y = reader.read_float()
                if skeleton.nonessential:
                    color = reader.read_color()
                    if color != Color():
                        point_att.color = color
                _push(Attachment(attachment_actual_name, attachment_actual_name, att_type, point_att))
            elif att_type == AttachmentType.Clipping:
                clipping_att = ClippingAttachment()
                clipping_att.endSlot = skeleton.slots[reader.read_varint(True)].name
                clipping_att.vertexCount = reader.read_varint(True)
                clipping_att.vertices = read_vertices(reader, clipping_att.vertexCount)
                if skeleton.nonessential:
                    color = reader.read_color()
                    if color != Color():
                        clipping_att.color = color
                _push(Attachment(attachment_actual_name, attachment_actual_name, att_type, clipping_att))
    return skin


def read_animation(reader: SpineBinaryReader, skeleton: SkeletonData) -> Animation:
    animation = Animation()
    animation.name = reader.read_string() or ""

    # slots timelines
    for _ in range(reader.read_varint(True)):
        slot_name = skeleton.slots[reader.read_varint(True)].name or ""
        slot_timeline: MultiTimeline = {}
        for _ in range(reader.read_varint(True)):
            timeline_type = reader.read_byte()
            frame_count = reader.read_varint(True)
            if timeline_type == 0:  # attachment
                timeline: Timeline = []
                for _ in range(frame_count):
                    frame = TimelineFrame()
                    frame.time = reader.read_float()
                    frame.str1 = reader.read_string_ref(skeleton.strings)
                    timeline.append(frame)
                slot_timeline["attachment"] = timeline
            elif timeline_type == 1:  # color
                timeline = []
                for frame_index in range(frame_count):
                    frame = TimelineFrame()
                    frame.time = reader.read_float()
                    frame.color1 = reader.read_color()
                    if frame_index < frame_count - 1:
                        read_curve(reader, frame)
                    timeline.append(frame)
                slot_timeline["rgba"] = timeline
            elif timeline_type == 2:  # two color
                timeline = []
                for frame_index in range(frame_count):
                    frame = TimelineFrame()
                    frame.time = reader.read_float()
                    frame.color1 = reader.read_color()
                    a = reader.read_byte()
                    r = reader.read_byte()
                    g = reader.read_byte()
                    b = reader.read_byte()
                    frame.color2 = Color(r, g, b, a)
                    if frame_index < frame_count - 1:
                        read_curve(reader, frame)
                    timeline.append(frame)
                slot_timeline["rgba2"] = timeline
        animation.slots[slot_name] = slot_timeline

    # bones timelines
    for _ in range(reader.read_varint(True)):
        bone_name = skeleton.bones[reader.read_varint(True)].name or ""
        bone_timeline: MultiTimeline = {}
        for _ in range(reader.read_varint(True)):
            timeline_type = reader.read_byte()
            frame_count = reader.read_varint(True)
            if timeline_type == 0:
                bone_timeline["rotate"] = read_timeline(reader, frame_count, 1)
            elif timeline_type == 1:
                bone_timeline["translate"] = read_timeline(reader, frame_count, 2)
            elif timeline_type == 2:
                bone_timeline["scale"] = read_timeline(reader, frame_count, 2)
            elif timeline_type == 3:
                bone_timeline["shear"] = read_timeline(reader, frame_count, 2)
        animation.bones[bone_name] = bone_timeline

    # ik
    for _ in range(reader.read_varint(True)):
        ik_name = skeleton.ikConstraints[reader.read_varint(True)].name or ""
        frame_count = reader.read_varint(True)
        timeline: Timeline = []
        for frame_index in range(frame_count):
            frame = TimelineFrame()
            frame.time = reader.read_float()
            frame.value1 = reader.read_float()
            frame.value2 = reader.read_float()
            frame.bendPositive = reader.read_sbyte() > 0
            frame.compress = reader.read_boolean()
            frame.stretch = reader.read_boolean()
            if frame_index < frame_count - 1:
                read_curve(reader, frame)
            timeline.append(frame)
        animation.ik[ik_name] = timeline

    # transform constraints
    for _ in range(reader.read_varint(True)):
        tf_name = skeleton.transformConstraints[reader.read_varint(True)].name or ""
        frame_count = reader.read_varint(True)
        timeline: Timeline = []
        for frame_index in range(frame_count):
            frame = TimelineFrame()
            frame.time = reader.read_float()
            frame.value1 = reader.read_float()
            frame.value2 = reader.read_float()
            frame.value3 = frame.value2
            frame.value4 = reader.read_float()
            frame.value5 = frame.value4
            frame.value6 = reader.read_float()
            if frame_index < frame_count - 1:
                read_curve(reader, frame)
            timeline.append(frame)
        animation.transform[tf_name] = timeline

    # path constraints
    for _ in range(reader.read_varint(True)):
        path_name = skeleton.pathConstraints[reader.read_varint(True)].name or ""
        path_timeline: MultiTimeline = {}
        for _ in range(reader.read_varint(True)):
            timeline_type = PathTimelineType(reader.read_sbyte())
            frame_count = reader.read_varint(True)
            if timeline_type == PathTimelineType.POSITION:
                path_timeline["position"] = read_timeline(reader, frame_count, 1)
            elif timeline_type == PathTimelineType.SPACING:
                path_timeline["spacing"] = read_timeline(reader, frame_count, 1)
            elif timeline_type == PathTimelineType.MIX:
                timeline: Timeline = []
                for frame_index in range(frame_count):
                    frame = TimelineFrame()
                    frame.time = reader.read_float()
                    frame.value1 = reader.read_float()
                    frame.value2 = reader.read_float()
                    frame.value3 = frame.value2
                    if frame_index < frame_count - 1:
                        read_curve(reader, frame)
                    timeline.append(frame)
                path_timeline["mix"] = timeline
        animation.path[path_name] = path_timeline

    # deform / attachments
    for _ in range(reader.read_varint(True)):
        skin_name = skeleton.skins[reader.read_varint(True)].name
        for _ in range(reader.read_varint(True)):
            slot_name = skeleton.slots[reader.read_varint(True)].name or ""
            for _ in range(reader.read_varint(True)):
                attachment_name = reader.read_string_ref(skeleton.strings) or ""
                frame_count = reader.read_varint(True)
                timeline: Timeline = []
                for frame_index in range(frame_count):
                    frame = TimelineFrame()
                    frame.time = reader.read_float()
                    end = reader.read_varint(True)
                    if end != 0:
                        start = reader.read_varint(True)
                        frame.int1 = start
                        end += start
                        for _ in range(start, end):
                            frame.vertices.append(reader.read_float())
                    if frame_index < frame_count - 1:
                        read_curve(reader, frame)
                    timeline.append(frame)
                animation.attachments.setdefault(skin_name, {}).setdefault(slot_name, {}).setdefault(attachment_name, {})[
                    "deform"
                ] = timeline

    # draw order
    draw_order_count = reader.read_varint(True)
    for _ in range(draw_order_count):
        frame = TimelineFrame()
        frame.time = reader.read_float()
        offset_count = reader.read_varint(True)
        for _ in range(offset_count):
            slot = skeleton.slots[reader.read_varint(True)].name or ""
            offset = reader.read_varint(True)
            frame.offsets.append((slot, offset))
        animation.drawOrder.append(frame)

    # events
    event_count = reader.read_varint(True)
    for _ in range(event_count):
        frame = TimelineFrame()
        frame.time = reader.read_float()
        event_index = reader.read_varint(True)
        event_data = skeleton.events[event_index]
        frame.str1 = event_data.name
        frame.int1 = reader.read_varint(False)
        frame.value1 = reader.read_float()
        free_string = reader.read_boolean()
        frame.str2 = reader.read_string() if free_string else event_data.stringValue
        if event_data.audioPath and len(event_data.audioPath) > 0:
            frame.value2 = reader.read_float()
            frame.value3 = reader.read_float()
        animation.events.append(frame)

    return animation


def read_binary_skeleton(data: bytes) -> SkeletonData:
    r = SpineBinaryReader(data)
    sk = SkeletonData()

    sk.hashString = r.read_string()
    if sk.hashString:
        sk.hash = base64_to_uint64(sk.hashString)
    sk.version = r.read_string()
    sk.x = r.read_float()
    sk.y = r.read_float()
    sk.width = r.read_float()
    sk.height = r.read_float()
    sk.nonessential = r.read_boolean()
    if sk.nonessential:
        sk.fps = r.read_float()
        sk.imagesPath = r.read_string()
        sk.audioPath = r.read_string()

    for _ in range(r.read_varint(True)):
        sk.strings.append(r.read_string() or "")

    # bones
    for i in range(r.read_varint(True)):
        bone = BoneData()
        bone.name = r.read_string()
        if i != 0:
            bone.parent = sk.bones[r.read_varint(True)].name
        bone.rotation = r.read_float()
        bone.x = r.read_float()
        bone.y = r.read_float()
        bone.scaleX = r.read_float()
        bone.scaleY = r.read_float()
        bone.shearX = r.read_float()
        bone.shearY = r.read_float()
        bone.length = r.read_float()
        bone.inherit = Inherit(r.read_varint(True))
        bone.skinRequired = r.read_boolean()
        if sk.nonessential:
            color = r.read_color()
            if color != Color(0x9B, 0x9B, 0x9B, 0xFF):
                bone.color = color
        sk.bones.append(bone)

    # slots
    for _ in range(r.read_varint(True)):
        slot = SlotData()
        slot.name = r.read_string()
        slot.bone = sk.bones[r.read_varint(True)].name
        color = r.read_color()
        if color != Color():
            slot.color = color
        r_dark = r.read_byte()
        g_dark = r.read_byte()
        b_dark = r.read_byte()
        a_dark = r.read_byte()
        if not (r_dark == 0xFF and g_dark == 0xFF and b_dark == 0xFF and a_dark == 0xFF):
            slot.darkColor = Color(r_dark, g_dark, b_dark, a_dark)
        slot.attachmentName = r.read_string_ref(sk.strings)
        slot.blendMode = BlendMode(r.read_varint(True))
        sk.slots.append(slot)

    # ik constraints
    for _ in range(r.read_varint(True)):
        ik = IKConstraintData()
        ik.name = r.read_string()
        ik.order = r.read_varint(True)
        ik.skinRequired = r.read_boolean()
        for _ in range(r.read_varint(True)):
            ik.bones.append(sk.bones[r.read_varint(True)].name or "")
        ik.target = sk.bones[r.read_varint(True)].name
        ik.mix = r.read_float()
        ik.softness = r.read_float()
        ik.bendPositive = r.read_sbyte() > 0
        ik.compress = r.read_boolean()
        ik.stretch = r.read_boolean()
        ik.uniform = r.read_boolean()
        sk.ikConstraints.append(ik)

    # transform constraints
    for _ in range(r.read_varint(True)):
        tf = TransformConstraintData()
        tf.name = r.read_string()
        tf.order = r.read_varint(True)
        tf.skinRequired = r.read_boolean()
        for _ in range(r.read_varint(True)):
            tf.bones.append(sk.bones[r.read_varint(True)].name or "")
        tf.target = sk.bones[r.read_varint(True)].name
        tf.local = r.read_boolean()
        tf.relative = r.read_boolean()
        tf.offsetRotation = r.read_float()
        tf.offsetX = r.read_float()
        tf.offsetY = r.read_float()
        tf.offsetScaleX = r.read_float()
        tf.offsetScaleY = r.read_float()
        tf.offsetShearY = r.read_float()
        tf.mixRotate = r.read_float()
        tf.mixX = r.read_float()
        tf.mixY = tf.mixX
        tf.mixScaleX = r.read_float()
        tf.mixScaleY = tf.mixScaleX
        tf.mixShearY = r.read_float()
        sk.transformConstraints.append(tf)

    # path constraints
    for _ in range(r.read_varint(True)):
        path = PathConstraintData()
        path.name = r.read_string()
        path.order = r.read_varint(True)
        path.skinRequired = r.read_boolean()
        for _ in range(r.read_varint(True)):
            path.bones.append(sk.bones[r.read_varint(True)].name or "")
        path.target = sk.slots[r.read_varint(True)].name
        path.positionMode = PositionMode(r.read_varint(True))
        path.spacingMode = SpacingMode(r.read_varint(True))
        path.rotateMode = RotateMode(r.read_varint(True))
        path.offsetRotation = r.read_float()
        path.position = r.read_float()
        path.spacing = r.read_float()
        path.mixRotate = r.read_float()
        path.mixX = r.read_float()
        path.mixY = path.mixX
        sk.pathConstraints.append(path)

    # skins
    sk.skins.append(read_skin(r, True, sk))
    for _ in range(r.read_varint(True)):
        sk.skins.append(read_skin(r, False, sk))

    # events
    for _ in range(r.read_varint(True)):
        ev = EventData()
        ev.name = r.read_string_ref(sk.strings) or ""
        ev.intValue = r.read_varint(False)
        ev.floatValue = r.read_float()
        ev.stringValue = r.read_string()
        ev.audioPath = r.read_string()
        if ev.audioPath and len(ev.audioPath) > 0:
            ev.volume = r.read_float()
            ev.balance = r.read_float()
        sk.events.append(ev)

    if r.pos < len(r.data):
        for _ in range(r.read_varint(True)):
            sk.animations.append(read_animation(r, sk))

    return sk


# ==============================
# JSON Writer (Spine 3.8)
# ==============================


def write_curve(frame: TimelineFrame) -> Dict[str, Any]:
    j: Dict[str, Any] = {}
    if frame.curveType == CurveType.STEPPED:
        j["curve"] = "stepped"
    elif frame.curveType == CurveType.BEZIER:
        if frame.curve:
            j["curve"] = frame.curve[0]
            if frame.curve[1] != 0.0:
                j["c2"] = frame.curve[1]
            if frame.curve[2] != 1.0:
                j["c3"] = frame.curve[2]
            if frame.curve[3] != 1.0:
                j["c4"] = frame.curve[3]
    return j


def write_timeline(timeline: Timeline, value_num: int, key1: str, key2: str, default: float) -> List[Dict[str, Any]]:
    arr: List[Dict[str, Any]] = []
    for f in timeline:
        item: Dict[str, Any] = {}
        if f.time != 0.0:
            item["time"] = f.time
        if f.value1 != default:
            item[key1] = f.value1
        if value_num > 1 and f.value2 != default:
            item[key2] = f.value2
        item.update(write_curve(f))
        arr.append(item)
    return arr


def write_json_data(sk: SkeletonData) -> Dict[str, Any]:
    j: Dict[str, Any] = {}

    skeleton = {
        "x": sk.x,
        "y": sk.y,
        "width": sk.width,
        "height": sk.height,
    }
    if sk.hashString:
        skeleton["hash"] = sk.hashString
    elif sk.hash != 0:
        skeleton["hash"] = uint64_to_base64(sk.hash)
    if sk.version:
        skeleton["spine"] = sk.version
    if sk.nonessential:
        if sk.fps != 30.0:
            skeleton["fps"] = sk.fps
        if sk.imagesPath:
            skeleton["images"] = sk.imagesPath
        if sk.audioPath:
            skeleton["audio"] = sk.audioPath
    j["skeleton"] = skeleton

    # bones
    j["bones"] = []
    for b in sk.bones:
        obj: Dict[str, Any] = {}
        if b.name is not None:
            obj["name"] = b.name
        if b.parent is not None:
            obj["parent"] = b.parent
        if b.length != 0.0:
            obj["length"] = b.length
        if b.x != 0.0:
            obj["x"] = b.x
        if b.y != 0.0:
            obj["y"] = b.y
        if b.rotation != 0.0:
            obj["rotation"] = b.rotation
        if b.scaleX != 1.0:
            obj["scaleX"] = b.scaleX
        if b.scaleY != 1.0:
            obj["scaleY"] = b.scaleY
        if b.shearX != 0.0:
            obj["shearX"] = b.shearX
        if b.shearY != 0.0:
            obj["shearY"] = b.shearY
        if b.inherit != Inherit.Normal:
            obj["transform"] = {
                Inherit.Normal: "normal",
                Inherit.OnlyTranslation: "onlyTranslation",
                Inherit.NoRotationOrReflection: "noRotationOrReflection",
                Inherit.NoScale: "noScale",
                Inherit.NoScaleOrReflection: "noScaleOrReflection",
            }[b.inherit]
        if b.skinRequired:
            obj["skin"] = True
        if b.color:
            obj["color"] = color_to_string(b.color, True)
        j["bones"].append(obj)

    # slots
    j["slots"] = []
    for s in sk.slots:
        obj: Dict[str, Any] = {}
        if s.name:
            obj["name"] = s.name
        if s.bone:
            obj["bone"] = s.bone
        if s.color:
            obj["color"] = color_to_string(s.color, True)
        if s.darkColor:
            obj["dark"] = color_to_string(s.darkColor, False)
        if s.attachmentName is not None:
            obj["attachment"] = s.attachmentName
        if s.blendMode != BlendMode.Normal:
            obj["blend"] = {
                BlendMode.Normal: "normal",
                BlendMode.Additive: "additive",
                BlendMode.Multiply: "multiply",
                BlendMode.Screen: "screen",
            }[s.blendMode]
        j["slots"].append(obj)

    # ik
    if sk.ikConstraints:
        j["ik"] = []
        for ik in sk.ikConstraints:
            obj: Dict[str, Any] = {}
            if ik.name:
                obj["name"] = ik.name
            if ik.order != 0:
                obj["order"] = ik.order
            if ik.skinRequired:
                obj["skin"] = True
            if ik.bones:
                obj["bones"] = ik.bones
            if ik.target:
                obj["target"] = ik.target
            if ik.mix != 1.0:
                obj["mix"] = ik.mix
            if ik.softness != 0.0:
                obj["softness"] = ik.softness
            if not ik.bendPositive:
                obj["bendPositive"] = False
            if ik.compress:
                obj["compress"] = True
            if ik.stretch:
                obj["stretch"] = True
            if ik.uniform:
                obj["uniform"] = True
            j["ik"].append(obj)

    # transform
    if sk.transformConstraints:
        j["transform"] = []
        for tf in sk.transformConstraints:
            obj: Dict[str, Any] = {}
            if tf.name:
                obj["name"] = tf.name
            if tf.order != 0:
                obj["order"] = tf.order
            if tf.skinRequired:
                obj["skin"] = True
            if tf.bones:
                obj["bones"] = tf.bones
            if tf.target:
                obj["target"] = tf.target
            if tf.mixRotate != 1.0:
                obj["rotateMix"] = tf.mixRotate
            if tf.mixX != 1.0:
                obj["translateMix"] = tf.mixX
            if tf.mixScaleX != 1.0:
                obj["scaleMix"] = tf.mixScaleX
            if tf.mixShearY != 1.0:
                obj["shearMix"] = tf.mixShearY
            if tf.offsetRotation != 0.0:
                obj["rotation"] = tf.offsetRotation
            if tf.offsetX != 0.0:
                obj["x"] = tf.offsetX
            if tf.offsetY != 0.0:
                obj["y"] = tf.offsetY
            if tf.offsetScaleX != 0.0:
                obj["scaleX"] = tf.offsetScaleX
            if tf.offsetScaleY != 0.0:
                obj["scaleY"] = tf.offsetScaleY
            if tf.offsetShearY != 0.0:
                obj["shearY"] = tf.offsetShearY
            if tf.relative:
                obj["relative"] = True
            if tf.local:
                obj["local"] = True
            j["transform"].append(obj)

    # path constraints
    if sk.pathConstraints:
        j["path"] = []
        for p in sk.pathConstraints:
            obj: Dict[str, Any] = {}
            if p.name:
                obj["name"] = p.name
            if p.order != 0:
                obj["order"] = p.order
            if p.skinRequired:
                obj["skin"] = True
            if p.bones:
                obj["bones"] = p.bones
            if p.target:
                obj["target"] = p.target
            if p.positionMode != PositionMode.Percent:
                obj["positionMode"] = {PositionMode.Fixed: "fixed", PositionMode.Percent: "percent"}[p.positionMode]
            if p.spacingMode != SpacingMode.Length:
                obj["spacingMode"] = {
                    SpacingMode.Length: "length",
                    SpacingMode.Fixed: "fixed",
                    SpacingMode.Percent: "percent",
                    SpacingMode.Proportional: "proportional",
                }[p.spacingMode]
            if p.rotateMode != RotateMode.Tangent:
                obj["rotateMode"] = {
                    RotateMode.Tangent: "tangent",
                    RotateMode.Chain: "chain",
                    RotateMode.ChainScale: "chainScale",
                }[p.rotateMode]
            if p.offsetRotation != 0.0:
                obj["rotation"] = p.offsetRotation
            if p.position != 0.0:
                obj["position"] = p.position
            if p.spacing != 0.0:
                obj["spacing"] = p.spacing
            if p.mixRotate != 1.0:
                obj["rotateMix"] = p.mixRotate
            if p.mixX != 1.0:
                obj["translateMix"] = p.mixX
            j["path"].append(obj)

    # skins
    j["skins"] = []
    for skin in sk.skins:
        s_obj: Dict[str, Any] = {"name": skin.name}
        if skin.bones:
            s_obj["bones"] = skin.bones
        if skin.ik:
            s_obj["ik"] = skin.ik
        if skin.transform:
            s_obj["transform"] = skin.transform
        if skin.path:
            s_obj["path"] = skin.path
        for slot_name, slot_map in skin.attachments.items():
            for att_name, att in slot_map.items():
                a_obj: Dict[str, Any] = {}
                if att.name != att_name:
                    a_obj["name"] = att.name
                if att.path != att.name:
                    a_obj["path"] = att.path
                if att.type != AttachmentType.Region:
                    a_obj["type"] = {
                        AttachmentType.Region: "region",
                        AttachmentType.Boundingbox: "boundingbox",
                        AttachmentType.Mesh: "mesh",
                        AttachmentType.Linkedmesh: "linkedmesh",
                        AttachmentType.Path: "path",
                        AttachmentType.Point: "point",
                        AttachmentType.Clipping: "clipping",
                    }[att.type]

                if att.type == AttachmentType.Region:
                    region: RegionAttachment = att.data
                    if region.x != 0.0:
                        a_obj["x"] = region.x
                    if region.y != 0.0:
                        a_obj["y"] = region.y
                    if region.rotation != 0.0:
                        a_obj["rotation"] = region.rotation
                    if region.scaleX != 1.0:
                        a_obj["scaleX"] = region.scaleX
                    if region.scaleY != 1.0:
                        a_obj["scaleY"] = region.scaleY
                    a_obj["width"] = region.width
                    a_obj["height"] = region.height
                    if region.color:
                        a_obj["color"] = color_to_string(region.color, True)
                elif att.type == AttachmentType.Mesh:
                    mesh: MeshAttachment = att.data
                    a_obj["width"] = mesh.width
                    a_obj["height"] = mesh.height
                    if mesh.color:
                        a_obj["color"] = color_to_string(mesh.color, True)
                    if mesh.hullLength != 0:
                        a_obj["hull"] = mesh.hullLength
                    if mesh.triangles:
                        a_obj["triangles"] = mesh.triangles
                    if mesh.edges:
                        a_obj["edges"] = mesh.edges
                    if mesh.uvs:
                        a_obj["uvs"] = mesh.uvs
                    if mesh.vertices:
                        a_obj["vertices"] = mesh.vertices
                elif att.type == AttachmentType.Linkedmesh:
                    lmesh: LinkedMeshAttachment = att.data
                    a_obj["width"] = lmesh.width
                    a_obj["height"] = lmesh.height
                    if lmesh.color:
                        a_obj["color"] = color_to_string(lmesh.color, True)
                    a_obj["parent"] = lmesh.parentMesh
                    if lmesh.timelines != 1:
                        a_obj["deform"] = lmesh.timelines
                    if lmesh.skin:
                        a_obj["skin"] = lmesh.skin
                elif att.type == AttachmentType.Boundingbox:
                    box: BoundingBoxAttachment = att.data
                    if box.vertexCount != 0:
                        a_obj["vertexCount"] = box.vertexCount
                    if box.color:
                        a_obj["color"] = color_to_string(box.color, True)
                    if box.vertices:
                        a_obj["vertices"] = box.vertices
                elif att.type == AttachmentType.Path:
                    path_att: PathAttachment = att.data
                    if path_att.vertexCount != 0:
                        a_obj["vertexCount"] = path_att.vertexCount
                    if path_att.closed:
                        a_obj["closed"] = True
                    if not path_att.constantSpeed:
                        a_obj["constantSpeed"] = path_att.constantSpeed
                    if path_att.color:
                        a_obj["color"] = color_to_string(path_att.color, True)
                    if path_att.vertices:
                        a_obj["vertices"] = path_att.vertices
                    if path_att.lengths:
                        a_obj["lengths"] = path_att.lengths
                elif att.type == AttachmentType.Point:
                    point: PointAttachment = att.data
                    if point.x != 0.0:
                        a_obj["x"] = point.x
                    if point.y != 0.0:
                        a_obj["y"] = point.y
                    if point.rotation != 0.0:
                        a_obj["rotation"] = point.rotation
                    if point.color:
                        a_obj["color"] = color_to_string(point.color, True)
                elif att.type == AttachmentType.Clipping:
                    clip: ClippingAttachment = att.data
                    if clip.vertexCount != 0:
                        a_obj["vertexCount"] = clip.vertexCount
                    if clip.endSlot:
                        a_obj["end"] = clip.endSlot
                    if clip.color:
                        a_obj["color"] = color_to_string(clip.color, True)
                    if clip.vertices:
                        a_obj["vertices"] = clip.vertices

                s_obj.setdefault("attachments", {}).setdefault(slot_name, {})[att_name] = a_obj
        j["skins"].append(s_obj)

    # events
    if sk.events:
        ev_obj: Dict[str, Any] = {}
        for e in sk.events:
            item: Dict[str, Any] = {}
            if e.intValue != 0:
                item["int"] = e.intValue
            if e.floatValue != 0.0:
                item["float"] = e.floatValue
            if e.stringValue is not None:
                item["string"] = e.stringValue
            if e.audioPath:
                item["audio"] = e.audioPath
                if e.volume != 1.0:
                    item["volume"] = e.volume
                if e.balance != 0.0:
                    item["balance"] = e.balance
            ev_obj[e.name] = item
        j["events"] = ev_obj

    # animations
    if sk.animations:
        anims: Dict[str, Any] = {}
        for anim in sk.animations:
            a_obj: Dict[str, Any] = {}
            if anim.slots:
                slots_obj: Dict[str, Any] = {}
                for slot_name, slot_map in anim.slots.items():
                    s_obj2: Dict[str, Any] = {}
                    if "attachment" in slot_map:
                        s_obj2["attachment"] = []
                        for f in slot_map["attachment"]:
                            item = {}
                            if f.time != 0.0:
                                item["time"] = f.time
                            item["name"] = f.str1 if f.str1 is not None else None
                            s_obj2["attachment"].append(item)
                    if "rgba" in slot_map or "rgb" in slot_map:
                        s_obj2["color"] = []
                        for f in slot_map.get("rgba") or slot_map.get("rgb"):
                            item = {}
                            if f.time != 0.0:
                                item["time"] = f.time
                            if f.color1:
                                item["color"] = color_to_string(f.color1, True)
                            item.update(write_curve(f))
                            s_obj2["color"].append(item)
                    if "rgba2" in slot_map or "rgb2" in slot_map:
                        s_obj2["twoColor"] = []
                        for f in slot_map.get("rgba2") or slot_map.get("rgb2"):
                            item = {}
                            if f.time != 0.0:
                                item["time"] = f.time
                            if f.color1:
                                item["light"] = color_to_string(f.color1, True)
                            if f.color2:
                                item["dark"] = color_to_string(f.color2, False)
                            item.update(write_curve(f))
                            s_obj2["twoColor"].append(item)
                    slots_obj[slot_name] = s_obj2
                a_obj["slots"] = slots_obj

            if anim.bones:
                bones_obj: Dict[str, Any] = {}
                for bone_name, bone_map in anim.bones.items():
                    b_obj: Dict[str, Any] = {}
                    if "rotate" in bone_map:
                        b_obj["rotate"] = write_timeline(bone_map["rotate"], 1, "angle", "", 0.0)
                    if "translate" in bone_map:
                        b_obj["translate"] = write_timeline(bone_map["translate"], 2, "x", "y", 0.0)
                    if "scale" in bone_map:
                        b_obj["scale"] = write_timeline(bone_map["scale"], 2, "x", "y", 1.0)
                    if "shear" in bone_map:
                        b_obj["shear"] = write_timeline(bone_map["shear"], 2, "x", "y", 0.0)
                    bones_obj[bone_name] = b_obj
                a_obj["bones"] = bones_obj

            if anim.ik:
                ik_obj: Dict[str, Any] = {}
                for ik_name, timeline in cast(Dict[str, Timeline], anim.ik).items():
                    frames: List[Dict[str, Any]] = []
                    for f in timeline:
                        item = {}
                        if f.time != 0.0:
                            item["time"] = f.time
                        if f.value1 != 1.0:
                            item["mix"] = f.value1
                        if f.value2 != 0.0:
                            item["softness"] = f.value2
                        if not f.bendPositive:
                            item["bendPositive"] = False
                        if f.compress:
                            item["compress"] = True
                        if f.stretch:
                            item["stretch"] = True
                        item.update(write_curve(f))
                        frames.append(item)
                    ik_obj[ik_name] = frames
                a_obj["ik"] = ik_obj

            if anim.transform:
                tf_obj: Dict[str, Any] = {}
                for tf_name, timeline in anim.transform.items():
                    frames = []
                    for f in timeline:
                        item = {}
                        if f.time != 0.0:
                            item["time"] = f.time
                        if f.value1 != 1.0:
                            item["rotateMix"] = f.value1
                        if f.value2 != 1.0:
                            item["translateMix"] = f.value2
                        if f.value4 != 1.0:
                            item["scaleMix"] = f.value4
                        if f.value6 != 1.0:
                            item["shearMix"] = f.value6
                        item.update(write_curve(f))
                        frames.append(item)
                    tf_obj[tf_name] = frames
                a_obj["transform"] = tf_obj

            if anim.path:
                path_obj: Dict[str, Any] = {}
                for path_name, path_map in anim.path.items():
                    p_obj: Dict[str, Any] = {}
                    if "position" in path_map:
                        p_obj["position"] = write_timeline(path_map["position"], 1, "position", "", 0.0)
                    if "spacing" in path_map:
                        p_obj["spacing"] = write_timeline(path_map["spacing"], 1, "spacing", "", 0.0)
                    if "mix" in path_map:
                        mix_frames = []
                        for f in path_map["mix"]:
                            item = {}
                            if f.time != 0.0:
                                item["time"] = f.time
                            if f.value1 != 1.0:
                                item["rotateMix"] = f.value1
                            if f.value2 != 1.0:
                                item["translateMix"] = f.value2
                            item.update(write_curve(f))
                            mix_frames.append(item)
                        p_obj["mix"] = mix_frames
                    path_obj[path_name] = p_obj
                a_obj["path"] = path_obj

            if anim.attachments:
                deform_obj: Dict[str, Any] = {}
                for skin_name, skin_map in anim.attachments.items():
                    for slot_name, slot_map in skin_map.items():
                        for att_name, att_map in slot_map.items():
                            if "deform" not in att_map:
                                continue
                            frames = []
                            for f in att_map["deform"]:
                                item = {}
                                if f.time != 0.0:
                                    item["time"] = f.time
                                if f.vertices:
                                    if f.int1 != 0:
                                        item["offset"] = f.int1
                                    item["vertices"] = f.vertices
                                item.update(write_curve(f))
                                frames.append(item)
                            deform_obj.setdefault(skin_name, {}).setdefault(slot_name, {})[att_name] = frames
                if deform_obj:
                    a_obj["deform"] = deform_obj

            if anim.drawOrder:
                frames = []
                for f in anim.drawOrder:
                    item = {}
                    if f.time != 0.0:
                        item["time"] = f.time
                    if f.offsets:
                        offs = []
                        for slot, offset in f.offsets:
                            offs.append({"slot": slot, "offset": offset})
                        item["offsets"] = offs
                    frames.append(item)
                a_obj["drawOrder"] = frames

            if anim.events:
                frames = []
                for f in anim.events:
                    item = {}
                    if f.time != 0.0:
                        item["time"] = f.time
                    if f.str1:
                        item["name"] = f.str1
                    # find default event values
                    event_data = next((e for e in sk.events if e.name == f.str1), None)
                    if event_data:
                        if f.int1 != event_data.intValue:
                            item["int"] = f.int1
                        if f.value1 != event_data.floatValue:
                            item["float"] = f.value1
                        if f.str2 is not None:
                            item["string"] = f.str2
                        if event_data.audioPath:
                            if f.value2 != 1.0:
                                item["volume"] = f.value2
                            if f.value3 != 0.0:
                                item["balance"] = f.value3
                    frames.append(item)
                a_obj["events"] = frames

            anims[anim.name] = a_obj
        j["animations"] = anims

    return j


# ==============================
# Converter
# ==============================


def convert_skel_to_json(input_path: str, output_path: str) -> None:
    with open(input_path, "rb") as f:
        data = f.read()

    skeleton = read_binary_skeleton(data)
    root = write_json_data(skeleton)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(root, f, ensure_ascii=False, indent=4)


# ==============================
# Entry
# ==============================


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        convert_skel_to_json(sys.argv[1], sys.argv[2])
    else:
        convert_skel_to_json(INPUT_PATH, OUTPUT_PATH)