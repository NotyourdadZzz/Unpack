__int64 __fastcall spine::v3::SkeletonDataLoader::loadBoneData(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        __int64 a3,
        int a4)
{
  __int64 v6; // x8
  unsigned __int64 v7; // x26
  unsigned __int64 v8; // x8
  unsigned __int64 v9; // x22
  bool v10; // cf
  unsigned __int64 v11; // x8
  __int64 v12; // x21
  int n8; // w23
  __int64 Instance; // x0
  __int64 v15; // x0
  __int64 v16; // x9
  __int64 v17; // x8
  int v18; // w24
  __int64 v19; // x8
  spine::v3::SkeletonDataLoader *v20; // x9
  char *v21; // x23
  __int64 v22; // x23
  spine::SpineExtension *v23; // x0
  __int64 v24; // x8
  __int64 v25; // x9
  __int64 v26; // x10
  __int64 v27; // x9
  char *v28; // x24
  __int64 v29; // x9
  __int64 v30; // x8
  __int64 v31; // x9
  __int64 v32; // x8
  __int64 v33; // x9
  __int64 v34; // x8
  __int64 v35; // x9
  __int64 v36; // x8
  __int64 v37; // x9
  __int64 v38; // x8
  __int64 v39; // x9
  __int64 v40; // x8
  __int64 v41; // x9
  __int64 v42; // x8
  __int64 v43; // x8
  __int64 v44; // x9
  __int64 v45; // x9
  __int64 InstanceEv; // x0
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+8h] [xbp-28h] BYREF
  size_t v49; // [xsp+10h] [xbp-20h]
  char *v50; // [xsp+18h] [xbp-18h]
  char v51; // [xsp+20h] [xbp-10h]
  __int64 v52; // [xsp+28h] [xbp-8h]

  v52 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v6 = *((_QWORD *)this + 14);
  v7 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  v9 = *((_QWORD *)a2 + 6);
  v8 = *((_QWORD *)a2 + 7);
  *((_QWORD *)a2 + 6) = v7;
  v10 = v8 >= v7;
  v11 = v7;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 8);
    if ( (unsigned int)(int)(float)((float)(unsigned int)v7 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v7 * 1.75);
    *((_QWORD *)a2 + 7) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    v11 = *((_QWORD *)a2 + 6);
    *((_QWORD *)a2 + 8) = v15;
  }
  while ( v9 < v11 )
  {
    *(_QWORD *)(*((_QWORD *)a2 + 8) + 8 * v9++) = 0;
    v11 = *((_QWORD *)a2 + 6);
  }
  if ( (_DWORD)v7 )
  {
    do
    {
      v16 = *((_QWORD *)this + 14);
      v17 = *((_QWORD *)this + 11);
      v18 = *(__int16 *)(v17 + v16);
      endptr = endptr;
      v49 = 0;
      v50 = 0;
      *((_QWORD *)this + 14) = v16 + 2;
      v51 = 0;
      v19 = *(unsigned int *)(v17 + v16 + 2);
      *((_QWORD *)this + 14) = v16 + 6;
      if ( (_DWORD)v19 != -1 )
      {
        v20 = (*((_BYTE *)this + 120) & 1) != 0
            ? (spine::v3::SkeletonDataLoader *)*((_QWORD *)this + 17)
            : (spine::v3::SkeletonDataLoader *)((char *)this + 121);
        if ( v20 )
        {
          v21 = (char *)v20 + v19;
          v49 = strlen((const char *)v20 + v19);
          v50 = v21;
          v51 = 1;
        }
      }
      v22 = spine::SpineObject::operator new(
              (spine::SpineObject *)&qword_60,
              (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3"
                                "/SCSLoader_v3.cpp",
              (const char *)&qword_88,
              a4);
      v23 = (spine::SpineExtension *)spine::v3::BoneData::BoneData(
                                       (spine::v3::BoneData *)v22,
                                       v18,
                                       (const spine::String *)&endptr,
                                       0);
      *(_QWORD *)(*((_QWORD *)a2 + 8) + 8LL * v18) = v22;
      v24 = *((_QWORD *)this + 11);
      v25 = *((_QWORD *)this + 14);
      v26 = *(__int16 *)(v24 + v25);
      v27 = v25 + 2;
      *((_QWORD *)this + 14) = v27;
      if ( (v26 & 0x8000000000000000LL) == 0 )
      {
        *(_QWORD *)(v22 + 48) = *(_QWORD *)(*((_QWORD *)a2 + 8) + 8 * v26);
        v24 = *((_QWORD *)this + 11);
        v27 = *((_QWORD *)this + 14);
      }
      v28 = v50;
      *(_DWORD *)(v22 + 56) = *(_DWORD *)(v24 + v27);
      v29 = *((_QWORD *)this + 11);
      v30 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v30;
      *(_DWORD *)(v22 + 60) = *(_DWORD *)(v29 + v30);
      v31 = *((_QWORD *)this + 11);
      v32 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v32;
      *(_DWORD *)(v22 + 64) = *(_DWORD *)(v31 + v32);
      v33 = *((_QWORD *)this + 11);
      v34 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v34;
      *(_DWORD *)(v22 + 68) = *(_DWORD *)(v33 + v34);
      v35 = *((_QWORD *)this + 11);
      v36 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v36;
      *(_DWORD *)(v22 + 72) = *(_DWORD *)(v35 + v36);
      v37 = *((_QWORD *)this + 11);
      v38 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v38;
      *(_DWORD *)(v22 + 76) = *(_DWORD *)(v37 + v38);
      v39 = *((_QWORD *)this + 11);
      v40 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v40;
      *(_DWORD *)(v22 + 80) = *(_DWORD *)(v39 + v40);
      v41 = *((_QWORD *)this + 11);
      v42 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v42;
      *(_DWORD *)(v22 + 84) = *(_DWORD *)(v41 + v42);
      v43 = *((_QWORD *)this + 14);
      v44 = *((_QWORD *)this + 11);
      *((_QWORD *)this + 14) = v43 + 4;
      LODWORD(v44) = *(__int16 *)(v44 + v43 + 4);
      *((_QWORD *)this + 14) = v43 + 6;
      *(_DWORD *)(v22 + 88) = v44;
      v45 = *((_QWORD *)this + 14);
      LODWORD(v43) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v45);
      *((_QWORD *)this + 14) = v45 + 1;
      endptr = endptr;
      *(_BYTE *)(v22 + 92) = (_DWORD)v43 != 0;
      if ( v28 && (v51 & 1) == 0 )
      {
        InstanceEv = spine::SpineExtension::getInstance(v23);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv + 40LL))(
          InstanceEv,
          v28,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
      --v7;
    }
    while ( v7 );
  }
  return 1;
}
