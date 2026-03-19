unsigned __int64 __fastcall spine::SkeletoneSCSPLoader::load(
        spine::SkeletoneSCSPLoader *this,
        const cocos2d::Data *a2,
        spine::SkeletoneCacheData *a3)
{
  __int64 Bytes; // x19
  __int64 Size; // x0
  int v7; // w21
  unsigned __int64 v8; // x19
  unsigned __int8 *v9; // x23
  _BYTE *v10; // x8
  _BYTE *v11; // x8
  _BYTE *v12; // x9
  _BYTE *v13; // x8
  char *v14; // x8
  _BOOL4 v15; // w25
  unsigned __int8 *v16; // x1
  __int64 n32; // x8
  __int64 n32_2; // x8
  char v19; // w20
  _QWORD *v20; // x0
  __int64 n32_1; // x8
  __int64 v22; // x10
  _BYTE v24[16]; // [xsp+8h] [xbp-F8h] BYREF
  __int64 v25; // [xsp+18h] [xbp-E8h] BYREF
  unsigned __int64 v26; // [xsp+20h] [xbp-E0h] BYREF
  void *v27; // [xsp+28h] [xbp-D8h]
  _QWORD v28[4]; // [xsp+30h] [xbp-D0h] BYREF
  _QWORD *v29; // [xsp+50h] [xbp-B0h]
  _QWORD v30[4]; // [xsp+60h] [xbp-A0h] BYREF
  _QWORD *v31; // [xsp+80h] [xbp-80h]
  _QWORD v32[4]; // [xsp+90h] [xbp-70h] BYREF
  _QWORD *v33; // [xsp+B0h] [xbp-50h]
  _QWORD v34[4]; // [xsp+C0h] [xbp-40h] BYREF
  _QWORD *v35; // [xsp+E0h] [xbp-20h]
  __int64 v36; // [xsp+F8h] [xbp-8h]

  v36 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v25 = 0;
  v26 = 0;
  v27 = 0;
  Bytes = cocos2d::Data::getBytes(a2);
  Size = cocos2d::Data::getSize(a2);
  yuna::archive::lz4::uncompress(Bytes, Size, &v25);
  v7 = v25 & 1;
  if ( v7 )
    v8 = v26;
  else
    v8 = (unsigned __int64)(unsigned __int8)v25 >> 1;
  if ( !v8 )
    goto LABEL_44;
  v9 = (unsigned __int8 *)v27;
  v10 = (char *)&v26 + 1;
  if ( v7 )
    v10 = (char *)v27 + 8;
  if ( *v10 != 115 )
    goto LABEL_20;
  v11 = (char *)&v26 + 2;
  if ( v7 )
    v11 = (char *)v27 + 9;
  if ( *v11 != 99 )
    goto LABEL_20;
  v12 = (char *)&v26 + 3;
  if ( v7 )
    v12 = (char *)v27 + 10;
  if ( *v12 != 115 )
    goto LABEL_20;
  v13 = (char *)&v26 + 4;
  if ( v7 )
    v13 = (char *)v27 + 11;
  if ( *v13 == 112 )
  {
    v14 = (char *)&v26 + 5;
    if ( v7 )
      v14 = (char *)v27 + 12;
    v15 = *(_DWORD *)v14 > 2u;
  }
  else
  {
LABEL_20:
    v15 = 0;
  }
  cocos2d::Data::Data((cocos2d::Data *)v24);
  if ( v7 )
    v16 = v9;
  else
    v16 = (unsigned __int8 *)&v25 + 1;
  cocos2d::Data::fastSet((cocos2d::Data *)v24, v16, v8);
  if ( v15 )
  {
    v8 = operator new(0x60u);
    v34[0] = off_163BF68;
    v35 = v34;
    spine::SkeletonDataV3::SkeletonDataV3(v8, a3, v34);
    if ( v35 == v34 )
    {
      n32 = 32;
    }
    else
    {
      if ( !v35 )
        goto LABEL_33;
      n32 = 40;
    }
    (*(void (**)(void))(*v35 + n32))();
LABEL_33:
    v33 = v32;
    v32[0] = off_163BFF8;
    v32[1] = spine::v3::SkeletonData_readSkeletonSCSPData;
    v19 = spine::SkeletonDataV3::load(v8, v24, v32);
    v20 = v33;
    if ( v33 != v32 )
      goto LABEL_34;
LABEL_39:
    n32_1 = 32;
    goto LABEL_40;
  }
  v8 = operator new(0x60u);
  v30[0] = off_163C0A8;
  v31 = v30;
  spine::SkeletonDataV2::SkeletonDataV2(v8, a3, v30);
  if ( v31 == v30 )
  {
    n32_2 = 32;
  }
  else
  {
    if ( !v31 )
      goto LABEL_38;
    n32_2 = 40;
  }
  (*(void (**)(void))(*v31 + n32_2))();
LABEL_38:
  v22 = *(_QWORD *)v8;
  v29 = v28;
  v28[0] = off_163C138;
  v28[1] = spine::v2::spSkeletonJson_readSkeletonSCSPData;
  v19 = (*(__int64 (__fastcall **)(unsigned __int64, _BYTE *, _QWORD *))(v22 + 96))(v8, v24, v28);
  v20 = v29;
  if ( v29 == v28 )
    goto LABEL_39;
LABEL_34:
  if ( v20 )
  {
    n32_1 = 40;
LABEL_40:
    (*(void (**)(void))(*v20 + n32_1))();
  }
  if ( (v19 & 1) == 0 )
  {
    (*(void (__fastcall **)(unsigned __int64))(*(_QWORD *)v8 + 24LL))(v8);
    v8 = 0;
  }
  cocos2d::Data::fastSet((cocos2d::Data *)v24, 0, 0);
  cocos2d::Data::~Data((cocos2d::Data *)v24);
  v7 = v25 & 1;
LABEL_44:
  if ( v7 )
    operator delete(v27, v25 & 0xFFFFFFFFFFFFFFFELL);
  return v8;
}

__int64 __fastcall spine::v3::SkeletonDataLoader::load(
        spine::v3::SkeletonDataLoader *this,
        const void *a2,
        unsigned __int64 a3,
        spine::SkeletonDataV3 *a4)
{
  __int64 v8; // x20
  spine::SpineExtension *v9; // x0
  __int64 v10; // x8
  __int64 v11; // x9
  __int128 v12; // q1
  __int128 v13; // q3
  __int128 v14; // q2
  __int64 v15; // x8
  char *v16; // x9
  const char *s; // x22
  const char *s_1; // x23
  __int64 Instance; // x0
  __int64 v20; // x9
  __int64 v21; // x8
  char *v22; // x9
  const char *s_2; // x22
  const char *s_3; // x23
  __int64 InstanceEv; // x0
  const char *s_4; // x23
  __int64 InstanceEv_1; // x0
  __int64 v28; // x9
  __int64 v29; // x8
  __int64 v30; // x8
  char *v31; // x9
  const char *s_5; // x22
  const char *s_6; // x23
  __int64 InstanceEv_2; // x0
  __int64 v35; // x9
  __int64 v36; // x8
  char *v37; // x9
  const char *s_7; // x22
  const char *s_8; // x23
  __int64 InstanceEv_3; // x0
  __int128 v41; // q0
  __int64 result; // x0

  v8 = spine::SpineObject::operator new(
         (spine::SpineObject *)&dword_200,
         (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
         (const char *)&stru_370.st_size + 5,
         (int)a4);
  *(_OWORD *)v8 = 0u;
  *(_OWORD *)(v8 + 16) = 0u;
  *(_OWORD *)(v8 + 32) = 0u;
  *(_OWORD *)(v8 + 48) = 0u;
  *(_OWORD *)(v8 + 64) = 0u;
  *(_OWORD *)(v8 + 80) = 0u;
  *(_OWORD *)(v8 + 96) = 0u;
  *(_OWORD *)(v8 + 112) = 0u;
  *(_OWORD *)(v8 + 128) = 0u;
  *(_OWORD *)(v8 + 144) = 0u;
  *(_OWORD *)(v8 + 160) = 0u;
  *(_OWORD *)(v8 + 176) = 0u;
  *(_OWORD *)(v8 + 192) = 0u;
  *(_OWORD *)(v8 + 208) = 0u;
  *(_OWORD *)(v8 + 224) = 0u;
  *(_OWORD *)(v8 + 240) = 0u;
  *(_OWORD *)(v8 + 256) = 0u;
  *(_OWORD *)(v8 + 272) = 0u;
  *(_OWORD *)(v8 + 288) = 0u;
  *(_OWORD *)(v8 + 304) = 0u;
  *(_OWORD *)(v8 + 320) = 0u;
  *(_OWORD *)(v8 + 336) = 0u;
  *(_OWORD *)(v8 + 352) = 0u;
  *(_OWORD *)(v8 + 368) = 0u;
  *(_OWORD *)(v8 + 384) = 0u;
  *(_OWORD *)(v8 + 400) = 0u;
  *(_OWORD *)(v8 + 416) = 0u;
  *(_OWORD *)(v8 + 432) = 0u;
  *(_OWORD *)(v8 + 448) = 0u;
  *(_OWORD *)(v8 + 464) = 0u;
  *(_OWORD *)(v8 + 480) = 0u;
  *(_OWORD *)(v8 + 496) = 0u;
  spine::v3::SkeletonData::SkeletonData((spine::v3::SkeletonData *)v8);
  *(_QWORD *)(v8 + 496) = 0;
  *(_QWORD *)(v8 + 504) = 0;
  *(_QWORD *)(v8 + 488) = 0;
  *(_QWORD *)v8 = off_163C268;
  v9 = (spine::SpineExtension *)sp_bin_stream::decode((spine::v3::SkeletonDataLoader *)((char *)this + 88), a2, a3);
  v10 = *((_QWORD *)this + 11);
  v11 = *((_QWORD *)this + 14);
  *(_OWORD *)((char *)this + 8) = *(_OWORD *)(v10 + v11);
  v13 = *(_OWORD *)(v10 + v11 + 32);
  v12 = *(_OWORD *)(v10 + v11 + 48);
  v14 = *(_OWORD *)(v10 + v11 + 16);
  *(_OWORD *)((char *)this + 66) = *(_OWORD *)(v10 + v11 + 58);
  *(_OWORD *)((char *)this + 56) = v12;
  *(_OWORD *)((char *)this + 40) = v13;
  *(_OWORD *)((char *)this + 24) = v14;
  *((_QWORD *)this + 14) = v11 + 74;
  v15 = *(unsigned int *)(v10 + v11 + 74);
  *((_QWORD *)this + 14) = v11 + 78;
  if ( (_DWORD)v15 == -1 )
  {
    s = 0;
  }
  else
  {
    if ( (*((_BYTE *)this + 120) & 1) != 0 )
      v16 = (char *)*((_QWORD *)this + 17);
    else
      v16 = (char *)this + 121;
    s = &v16[v15];
  }
  s_1 = *(const char **)(v8 + 368);
  if ( s_1 != s )
  {
    if ( s_1 && (*(_BYTE *)(v8 + 376) & 1) == 0 )
    {
      Instance = spine::SpineExtension::getInstance(v9);
      v9 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)Instance + 40LL))(
                                      Instance,
                                      s_1,
                                      "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstu"
                                      "dio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                                      129);
    }
    if ( s )
    {
      v9 = (spine::SpineExtension *)strlen(s);
      *(_QWORD *)(v8 + 360) = v9;
      *(_QWORD *)(v8 + 368) = s;
      *(_BYTE *)(v8 + 376) = 1;
    }
    else
    {
      *(_QWORD *)(v8 + 360) = 0;
      *(_QWORD *)(v8 + 368) = 0;
      *(_BYTE *)(v8 + 376) = 0;
    }
  }
  v20 = *((_QWORD *)this + 14);
  v21 = *(unsigned int *)(*((_QWORD *)this + 11) + v20);
  *((_QWORD *)this + 14) = v20 + 4;
  if ( (_DWORD)v21 == -1 )
  {
    s_2 = 0;
  }
  else
  {
    if ( (*((_BYTE *)this + 120) & 1) != 0 )
      v22 = (char *)*((_QWORD *)this + 17);
    else
      v22 = (char *)this + 121;
    s_2 = &v22[v21];
  }
  s_3 = *(const char **)(v8 + 336);
  if ( s_3 != s_2 )
  {
    if ( s_3 && (*(_BYTE *)(v8 + 344) & 1) == 0 )
    {
      InstanceEv = spine::SpineExtension::getInstance(v9);
      v9 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv + 40LL))(
                                      InstanceEv,
                                      s_3,
                                      "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstu"
                                      "dio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                                      129);
    }
    if ( s_2 )
    {
      v9 = (spine::SpineExtension *)strlen(s_2);
      *(_QWORD *)(v8 + 328) = v9;
      *(_QWORD *)(v8 + 336) = s_2;
      *(_BYTE *)(v8 + 344) = 1;
    }
    else
    {
      *(_QWORD *)(v8 + 328) = 0;
      *(_QWORD *)(v8 + 336) = 0;
      *(_BYTE *)(v8 + 344) = 0;
    }
  }
  *((_QWORD *)this + 14) += 4LL;
  s_4 = *(const char **)(v8 + 24);
  if ( s_4 != s_2 )
  {
    if ( s_4 && (*(_BYTE *)(v8 + 32) & 1) == 0 )
    {
      InstanceEv_1 = spine::SpineExtension::getInstance(v9);
      v9 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
                                      InstanceEv_1,
                                      s_4,
                                      "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstu"
                                      "dio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                                      129);
    }
    if ( s_2 )
    {
      v9 = (spine::SpineExtension *)strlen(s_2);
      *(_QWORD *)(v8 + 16) = v9;
      *(_QWORD *)(v8 + 24) = s_2;
      *(_BYTE *)(v8 + 32) = 1;
    }
    else
    {
      *(_QWORD *)(v8 + 16) = 0;
      *(_QWORD *)(v8 + 24) = 0;
      *(_BYTE *)(v8 + 32) = 0;
    }
  }
  v28 = *((_QWORD *)this + 14);
  v29 = *((_QWORD *)this + 11);
  *((_QWORD *)this + 14) = v28 + 4;
  v30 = *(unsigned int *)(v29 + v28 + 4);
  *((_QWORD *)this + 14) = v28 + 8;
  if ( (_DWORD)v30 == -1 )
  {
    s_5 = 0;
  }
  else
  {
    if ( (*((_BYTE *)this + 120) & 1) != 0 )
      v31 = (char *)*((_QWORD *)this + 17);
    else
      v31 = (char *)this + 121;
    s_5 = &v31[v30];
  }
  s_6 = *(const char **)(v8 + 440);
  if ( s_6 != s_5 )
  {
    if ( s_6 && (*(_BYTE *)(v8 + 448) & 1) == 0 )
    {
      InstanceEv_2 = spine::SpineExtension::getInstance(v9);
      v9 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_2 + 40LL))(
                                      InstanceEv_2,
                                      s_6,
                                      "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstu"
                                      "dio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                                      129);
    }
    if ( s_5 )
    {
      v9 = (spine::SpineExtension *)strlen(s_5);
      *(_QWORD *)(v8 + 432) = v9;
      *(_QWORD *)(v8 + 440) = s_5;
      *(_BYTE *)(v8 + 448) = 1;
    }
    else
    {
      *(_QWORD *)(v8 + 432) = 0;
      *(_QWORD *)(v8 + 440) = 0;
      *(_BYTE *)(v8 + 448) = 0;
    }
  }
  v35 = *((_QWORD *)this + 14);
  v36 = *(unsigned int *)(*((_QWORD *)this + 11) + v35);
  *((_QWORD *)this + 14) = v35 + 4;
  if ( (_DWORD)v36 == -1 )
  {
    s_7 = 0;
  }
  else
  {
    if ( (*((_BYTE *)this + 120) & 1) != 0 )
      v37 = (char *)*((_QWORD *)this + 17);
    else
      v37 = (char *)this + 121;
    s_7 = &v37[v36];
  }
  s_8 = *(const char **)(v8 + 472);
  if ( s_8 != s_7 )
  {
    if ( s_8 && (*(_BYTE *)(v8 + 480) & 1) == 0 )
    {
      InstanceEv_3 = spine::SpineExtension::getInstance(v9);
      (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_3 + 40LL))(
        InstanceEv_3,
        s_8,
        "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../../"
        "../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
        129);
    }
    if ( s_7 )
    {
      *(_QWORD *)(v8 + 464) = strlen(s_7);
      *(_QWORD *)(v8 + 472) = s_7;
      *(_BYTE *)(v8 + 480) = 1;
    }
    else
    {
      *(_QWORD *)(v8 + 464) = 0;
      *(_QWORD *)(v8 + 472) = 0;
      *(_BYTE *)(v8 + 480) = 0;
    }
  }
  spine::v3::SkeletonDataLoader::loadBoneData(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadIkConstraints(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadSlots(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadTransformConstraints(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadPathConstraints(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadSkins(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadEvents(this, (spine::v3::SkeletonData *)v8);
  spine::v3::SkeletonDataLoader::loadAnimations(this, (spine::v3::SkeletonData *)v8, a4);
  if ( (*(_BYTE *)(v8 + 488) & 1) != 0 )
    operator delete(*(void **)(v8 + 504), *(_QWORD *)(v8 + 488) & 0xFFFFFFFFFFFFFFFELL);
  v41 = *(_OWORD *)((char *)this + 120);
  result = v8;
  *(_QWORD *)(v8 + 504) = *((_QWORD *)this + 17);
  *(_OWORD *)(v8 + 488) = v41;
  *((_WORD *)this + 60) = 0;
  return result;
}


__int64 __fastcall sp_bin_stream::decode(sp_bin_stream *this, unsigned int *a2)
{
  void *src; // x23
  __int64 v4; // x20
  unsigned __int64 v5; // x21
  unsigned __int64 v6; // x24
  size_t n; // x25
  char *dest; // x26
  unsigned int *src_1; // x2
  int v11; // w22
  int v12; // w5
  int v13; // w6
  int v14; // w7
  unsigned __int64 v15; // x8
  unsigned __int64 v16; // x11
  bool v17; // zf
  __int64 v18; // x8
  __int64 v19; // x9
  __int64 result; // x0
  __int64 vars0; // [xsp+0h] [xbp+0h]
  int vars8; // [xsp+8h] [xbp+8h]
  void *vars10; // [xsp+10h] [xbp+10h]

  src = *(void **)this;
  v5 = *a2;
  v4 = a2[1];
  v6 = *((_QWORD *)this + 2) - *(_QWORD *)this;
  if ( v6 < v5 )
  {
    n = *((_QWORD *)this + 1) - (_QWORD)src;
    dest = (char *)operator new(*a2);
    memcpy(dest, src, n);
    *(_QWORD *)this = dest;
    *((_QWORD *)this + 1) = &dest[n];
    *((_QWORD *)this + 2) = &dest[v5];
    if ( src )
      operator delete(src, v6);
  }
  src_1 = a2 + 2;
  v11 = (_DWORD)a2 + 8 + v5;
  std::vector<char>::__insert_with_size[abi:ne210000]<char const*,char const*>((int)this, *((void **)this + 1), src_1);
  std::string::reserve((char *)this + 32, v4);
  v15 = *((unsigned __int8 *)this + 32);
  v16 = v15 >> 1;
  v17 = (v15 & 1) == 0;
  if ( (v15 & 1) != 0 )
    v18 = *((_QWORD *)this + 6);
  else
    LODWORD(v18) = (_DWORD)this + 33;
  if ( v17 )
    LODWORD(v19) = v16;
  else
    v19 = *((_QWORD *)this + 5);
  result = std::string::__insert_with_size<char const*,char const*>(
             (int)this + 32,
             (int)v18 + (int)v19,
             v11,
             v11 + (int)v4,
             v4,
             v12,
             v13,
             v14,
             vars0,
             vars8,
             vars10);
  *((_QWORD *)this + 7) = 0;
  *((_QWORD *)this + 3) = 0;
  return result;
}