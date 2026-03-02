__int64 __fastcall spine::v3::SkeletonDataLoader::loadPathConstraints(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        __int64 a3,
        int a4)
{
  __int64 v6; // x8
  unsigned __int64 i_2; // x9
  unsigned __int64 i_3; // x8
  unsigned __int64 i_5; // x22
  bool v10; // cf
  unsigned __int64 i_4; // x8
  __int64 v12; // x21
  int n8; // w23
  __int64 Instance; // x0
  __int64 v15; // x0
  __int64 i; // x28
  __int64 v17; // x9
  __int64 v18; // x8
  __int64 v19; // x8
  char *v20; // x9
  char *v21; // x24
  __int64 v22; // x24
  spine::SpineExtension *v23; // x0
  __int64 v24; // x9
  __int64 v25; // x8
  __int64 v26; // x9
  __int64 v27; // x9
  __int64 v28; // x9
  __int64 v29; // x9
  __int64 v30; // x9
  __int64 v31; // x8
  __int64 v32; // x9
  __int64 v33; // x8
  __int64 v34; // x9
  __int64 v35; // x8
  __int64 v36; // x9
  __int64 v37; // x8
  __int64 v38; // x9
  __int64 v39; // x8
  __int64 v40; // x10
  __int64 v41; // x9
  __int64 v42; // x10
  __int64 v43; // x27
  char *v44; // x24
  __int64 InstanceEv_1; // x0
  __int64 v46; // x12
  __int64 v47; // x8
  __int64 v48; // x10
  __int64 v49; // x8
  unsigned __int64 v50; // x10
  __int64 v51; // x9
  __int64 v52; // x26
  __int64 v53; // x25
  int n8_1; // w10
  __int64 n8_2; // x22
  __int64 InstanceEv; // x0
  __int64 v57; // x8
  unsigned __int64 i_1; // [xsp+20h] [xbp-40h]
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+28h] [xbp-38h] BYREF
  size_t v61; // [xsp+30h] [xbp-30h]
  char *v62; // [xsp+38h] [xbp-28h]
  char v63; // [xsp+40h] [xbp-20h]
  __int64 v64; // [xsp+48h] [xbp-18h]

  v64 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v6 = *((_QWORD *)this + 14);
  i_2 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  i_5 = *((_QWORD *)a2 + 35);
  i_3 = *((_QWORD *)a2 + 36);
  *((_QWORD *)a2 + 35) = i_2;
  i_1 = i_2;
  v10 = i_3 >= i_2;
  i_4 = i_2;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 37);
    if ( (unsigned int)(int)(float)((float)(unsigned int)i_2 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)i_2 * 1.75);
    *((_QWORD *)a2 + 36) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    i_4 = *((_QWORD *)a2 + 35);
    *((_QWORD *)a2 + 37) = v15;
  }
  while ( i_5 < i_4 )
  {
    *(_QWORD *)(*((_QWORD *)a2 + 37) + 8 * i_5++) = 0;
    i_4 = *((_QWORD *)a2 + 35);
  }
  if ( (_DWORD)i_1 )
  {
    for ( i = 0; i != i_1; ++i )
    {
      v17 = *((_QWORD *)this + 14);
      v61 = 0;
      v62 = 0;
      endptr = endptr;
      v18 = *((_QWORD *)this + 11);
      v63 = 0;
      v19 = *(unsigned int *)(v18 + v17);
      *((_QWORD *)this + 14) = v17 + 4;
      if ( (_DWORD)v19 != -1 )
      {
        v20 = (char *)this + 121;
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v20 = (char *)*((_QWORD *)this + 17);
        if ( v20 )
        {
          v21 = &v20[v19];
          v61 = strlen(&v20[v19]);
          v62 = v21;
          v63 = 1;
        }
      }
      v22 = spine::SpineObject::operator new(
              (spine::SpineObject *)&qword_80,
              (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3"
                                "/SCSLoader_v3.cpp",
              (const char *)off_130,
              a4);
      v23 = (spine::SpineExtension *)spine::v3::PathConstraintData::PathConstraintData(
                                       (spine::v3::PathConstraintData *)v22,
                                       (const spine::String *)&endptr);
      *(_QWORD *)(*((_QWORD *)a2 + 37) + 8 * i) = v22;
      v24 = *((_QWORD *)this + 14);
      v25 = *(unsigned int *)(*((_QWORD *)this + 11) + v24);
      *((_QWORD *)this + 14) = v24 + 4;
      *(_QWORD *)(v22 + 40) = v25;
      v26 = *((_QWORD *)this + 14);
      LODWORD(v25) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v26);
      *((_QWORD *)this + 14) = v26 + 1;
      *(_BYTE *)(v22 + 48) = (_DWORD)v25 != 0;
      v27 = *((_QWORD *)this + 14);
      LODWORD(v25) = *(__int16 *)(*((_QWORD *)this + 11) + v27);
      *((_QWORD *)this + 14) = v27 + 2;
      *(_DWORD *)(v22 + 96) = v25;
      v28 = *((_QWORD *)this + 14);
      LODWORD(v25) = *(__int16 *)(*((_QWORD *)this + 11) + v28);
      *((_QWORD *)this + 14) = v28 + 2;
      *(_DWORD *)(v22 + 100) = v25;
      v29 = *((_QWORD *)this + 14);
      LODWORD(v25) = *(__int16 *)(*((_QWORD *)this + 11) + v29);
      *((_QWORD *)this + 14) = v29 + 2;
      *(_DWORD *)(v22 + 104) = v25;
      *(_DWORD *)(v22 + 108) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
      v30 = *((_QWORD *)this + 11);
      v31 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v31;
      *(_DWORD *)(v22 + 112) = *(_DWORD *)(v30 + v31);
      v32 = *((_QWORD *)this + 11);
      v33 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v33;
      *(_DWORD *)(v22 + 116) = *(_DWORD *)(v32 + v33);
      v34 = *((_QWORD *)this + 11);
      v35 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v35;
      *(_DWORD *)(v22 + 120) = *(_DWORD *)(v34 + v35);
      v36 = *((_QWORD *)this + 11);
      v37 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v37;
      *(_DWORD *)(v22 + 124) = *(_DWORD *)(v36 + v37);
      v38 = *((_QWORD *)this + 14);
      v39 = *((_QWORD *)this + 11);
      v40 = v38 + 4;
      v41 = v38 + 6;
      *((_QWORD *)this + 14) = v40;
      v42 = *(__int16 *)(v39 + v40);
      *((_QWORD *)this + 14) = v41;
      if ( (v42 & 0x8000000000000000LL) == 0 )
      {
        *(_QWORD *)(v22 + 88) = *(_QWORD *)(*((_QWORD *)a2 + 12) + 8 * v42);
        v39 = *((_QWORD *)this + 11);
        v41 = *((_QWORD *)this + 14);
      }
      v43 = *(unsigned __int16 *)(v39 + v41);
      for ( *((_QWORD *)this + 14) = v41 + 2; v43; --v43 )
      {
        v47 = *((_QWORD *)this + 14);
        v48 = v47 + 2;
        v49 = *(__int16 *)(*((_QWORD *)this + 11) + v47);
        *((_QWORD *)this + 14) = v48;
        v50 = *(_QWORD *)(v22 + 64);
        v51 = *((_QWORD *)a2 + 8);
        if ( v50 == *(_QWORD *)(v22 + 72) )
        {
          v52 = *(_QWORD *)(v51 + 8 * v49);
          v53 = *(_QWORD *)(v22 + 80);
          n8_1 = (int)(float)((float)v50 * 1.75);
          if ( (unsigned int)n8_1 <= 8 )
            n8_1 = 8;
          n8_2 = n8_1;
          *(_QWORD *)(v22 + 72) = n8_1;
          InstanceEv = spine::SpineExtension::getInstance(v23);
          v23 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv + 32LL))(
                                           InstanceEv,
                                           v53,
                                           8 * n8_2,
                                           "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.andro"
                                           "idstudio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/sp"
                                           "ine/cpp/Vector.h",
                                           109);
          v57 = *(_QWORD *)(v22 + 64);
          *(_QWORD *)(v22 + 80) = v23;
          *(_QWORD *)(v22 + 64) = v57 + 1;
          *((_QWORD *)v23 + v57) = v52;
        }
        else
        {
          v46 = *(_QWORD *)(v22 + 80);
          *(_QWORD *)(v22 + 64) = v50 + 1;
          *(_QWORD *)(v46 + 8 * v50) = *(_QWORD *)(v51 + 8 * v49);
        }
      }
      v44 = v62;
      endptr = endptr;
      if ( v62 && (v63 & 1) == 0 )
      {
        InstanceEv_1 = spine::SpineExtension::getInstance(v23);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
          InstanceEv_1,
          v44,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
    }
  }
  return 1;
}