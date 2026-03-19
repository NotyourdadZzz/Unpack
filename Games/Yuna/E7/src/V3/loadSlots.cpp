__int64 __fastcall spine::v3::SkeletonDataLoader::loadSlots(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        __int64 a3,
        int a4)
{
  __int64 v6; // x8
  unsigned __int64 v7; // x23
  unsigned __int64 v8; // x8
  unsigned __int64 v9; // x22
  bool v10; // cf
  unsigned __int64 v11; // x8
  __int64 v12; // x21
  int n8; // w24
  __int64 Instance; // x0
  __int64 v15; // x0
  __int64 v16; // x21
  __int64 v17; // x27
  __int64 v18; // x9
  __int64 v19; // x8
  __int64 v20; // x10
  int v21; // w24
  __int64 v22; // x9
  __int64 v23; // x10
  spine::v3::SkeletonDataLoader *v24; // x11
  char *v25; // x23
  size_t v26; // x0
  __int64 v27; // x8
  spine::v3::BoneData *v28; // x25
  __int64 v29; // x23
  spine::SpineExtension *v30; // x0
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
  __int64 v43; // x9
  __int64 v44; // x8
  __int64 v45; // x8
  __int64 v46; // x10
  __int64 v47; // x9
  __int64 v48; // x8
  char *v49; // x9
  const char *s; // x24
  const char *s_1; // x25
  __int64 InstanceEv; // x0
  __int64 v53; // x9
  char *v54; // x24
  int v55; // w8
  __int64 InstanceEv_1; // x0
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+8h] [xbp-28h] BYREF
  size_t v59; // [xsp+10h] [xbp-20h]
  char *v60; // [xsp+18h] [xbp-18h]
  char v61; // [xsp+20h] [xbp-10h]
  __int64 v62; // [xsp+28h] [xbp-8h]

  v62 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v6 = *((_QWORD *)this + 14);
  v7 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  v9 = *((_QWORD *)a2 + 10);
  v8 = *((_QWORD *)a2 + 11);
  *((_QWORD *)a2 + 10) = v7;
  v10 = v8 >= v7;
  v11 = v7;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 12);
    if ( (unsigned int)(int)(float)((float)(unsigned int)v7 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v7 * 1.75);
    *((_QWORD *)a2 + 11) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    v11 = *((_QWORD *)a2 + 10);
    *((_QWORD *)a2 + 12) = v15;
  }
  while ( v9 < v11 )
  {
    *(_QWORD *)(*((_QWORD *)a2 + 12) + 8 * v9++) = 0;
    v11 = *((_QWORD *)a2 + 10);
  }
  if ( (_DWORD)v7 )
  {
    v16 = 8 * v7;
    v17 = 0;
    do
    {
      v18 = *((_QWORD *)this + 14);
      v19 = *((_QWORD *)this + 11);
      v20 = v18 + 2;
      v21 = *(__int16 *)(v19 + v18);
      endptr = endptr;
      v59 = 0;
      v60 = 0;
      v22 = v18 + 6;
      *((_QWORD *)this + 14) = v20;
      v61 = 0;
      v23 = *(unsigned int *)(v19 + v20);
      *((_QWORD *)this + 14) = v22;
      if ( (_DWORD)v23 != -1 )
      {
        v24 = (*((_BYTE *)this + 120) & 1) != 0
            ? (spine::v3::SkeletonDataLoader *)*((_QWORD *)this + 17)
            : (spine::v3::SkeletonDataLoader *)((char *)this + 121);
        if ( v24 )
        {
          v25 = (char *)v24 + v23;
          v26 = strlen((const char *)v24 + v23);
          v19 = *((_QWORD *)this + 11);
          v22 = *((_QWORD *)this + 14);
          v59 = v26;
          v60 = v25;
          v61 = 1;
        }
      }
      v27 = *(__int16 *)(v19 + v22);
      *((_QWORD *)this + 14) = v22 + 2;
      v28 = *(spine::v3::BoneData **)(*((_QWORD *)a2 + 8) + 8 * v27);
      v29 = spine::SpineObject::operator new(
              (spine::SpineObject *)&qword_98,
              (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3"
                                "/SCSLoader_v3.cpp",
              (const char *)&qword_E0 + 2,
              a4);
      v30 = (spine::SpineExtension *)spine::v3::SlotData::SlotData(
                                       (spine::v3::SlotData *)v29,
                                       v21,
                                       (const spine::String *)&endptr,
                                       v28);
      *(_QWORD *)(*((_QWORD *)a2 + 12) + v17) = v29;
      *(_DWORD *)(v29 + 64) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
      v31 = *((_QWORD *)this + 11);
      v32 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v32;
      *(_DWORD *)(v29 + 68) = *(_DWORD *)(v31 + v32);
      v33 = *((_QWORD *)this + 11);
      v34 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v34;
      *(_DWORD *)(v29 + 72) = *(_DWORD *)(v33 + v34);
      v35 = *((_QWORD *)this + 11);
      v36 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v36;
      *(_DWORD *)(v29 + 76) = *(_DWORD *)(v35 + v36);
      v37 = *((_QWORD *)this + 11);
      v38 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v38;
      *(_DWORD *)(v29 + 88) = *(_DWORD *)(v37 + v38);
      v39 = *((_QWORD *)this + 11);
      v40 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v40;
      *(_DWORD *)(v29 + 92) = *(_DWORD *)(v39 + v40);
      v41 = *((_QWORD *)this + 11);
      v42 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v42;
      *(_DWORD *)(v29 + 96) = *(_DWORD *)(v41 + v42);
      v43 = *((_QWORD *)this + 11);
      v44 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v44;
      *(_DWORD *)(v29 + 100) = *(_DWORD *)(v43 + v44);
      v45 = *((_QWORD *)this + 14);
      v46 = *((_QWORD *)this + 11);
      *((_QWORD *)this + 14) = v45 + 4;
      LODWORD(v43) = *(unsigned __int8 *)(v46 + v45 + 4);
      *((_QWORD *)this + 14) = v45 + 5;
      *(_BYTE *)(v29 + 104) = (_DWORD)v43 != 0;
      v47 = *((_QWORD *)this + 14);
      v48 = *(unsigned int *)(*((_QWORD *)this + 11) + v47);
      *((_QWORD *)this + 14) = v47 + 4;
      if ( (_DWORD)v48 == -1 )
      {
        s = 0;
      }
      else
      {
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v49 = (char *)*((_QWORD *)this + 17);
        else
          v49 = (char *)this + 121;
        s = &v49[v48];
      }
      s_1 = *(const char **)(v29 + 128);
      if ( s_1 != s )
      {
        if ( s_1 && (*(_BYTE *)(v29 + 136) & 1) == 0 )
        {
          InstanceEv = spine::SpineExtension::getInstance(v30);
          v30 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv + 40LL))(
                                           InstanceEv,
                                           s_1,
                                           "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.andro"
                                           "idstudio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/sp"
                                           "ine/cpp/SpineString.h",
                                           129);
        }
        if ( s )
        {
          v30 = (spine::SpineExtension *)strlen(s);
          *(_QWORD *)(v29 + 120) = v30;
          *(_QWORD *)(v29 + 128) = s;
          *(_BYTE *)(v29 + 136) = 1;
        }
        else
        {
          *(_QWORD *)(v29 + 120) = 0;
          *(_QWORD *)(v29 + 128) = 0;
          *(_BYTE *)(v29 + 136) = 0;
        }
      }
      v53 = *((_QWORD *)this + 14);
      v54 = v60;
      v55 = *(__int16 *)(*((_QWORD *)this + 11) + v53);
      *((_QWORD *)this + 14) = v53 + 2;
      *(_DWORD *)(v29 + 144) = v55;
      endptr = endptr;
      if ( v54 && (v61 & 1) == 0 )
      {
        InstanceEv_1 = spine::SpineExtension::getInstance(v30);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
          InstanceEv_1,
          v54,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
      v17 += 8;
    }
    while ( v16 != v17 );
  }
  return 1;
}