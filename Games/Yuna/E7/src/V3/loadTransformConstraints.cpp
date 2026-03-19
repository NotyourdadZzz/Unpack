__int64 __fastcall spine::v3::SkeletonDataLoader::loadTransformConstraints(
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
  __int64 v28; // x8
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
  __int64 v43; // x9
  __int64 v44; // x8
  __int64 v45; // x8
  __int64 v46; // x10
  __int64 v47; // x9
  __int64 v48; // x8
  __int64 v49; // x9
  __int64 v50; // x10
  __int64 v51; // x9
  __int64 v52; // x26
  char *v53; // x24
  __int64 InstanceEv_1; // x0
  __int64 v55; // x12
  __int64 v56; // x8
  __int64 v57; // x10
  __int64 v58; // x8
  unsigned __int64 v59; // x10
  __int64 v60; // x9
  __int64 v61; // x27
  __int64 v62; // x25
  int n8_1; // w10
  __int64 n8_2; // x22
  __int64 InstanceEv; // x0
  __int64 v66; // x8
  unsigned __int64 i_1; // [xsp+20h] [xbp-40h]
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+28h] [xbp-38h] BYREF
  size_t v70; // [xsp+30h] [xbp-30h]
  char *v71; // [xsp+38h] [xbp-28h]
  char v72; // [xsp+40h] [xbp-20h]
  __int64 v73; // [xsp+48h] [xbp-18h]

  v73 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v6 = *((_QWORD *)this + 14);
  i_2 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  i_5 = *((_QWORD *)a2 + 31);
  i_3 = *((_QWORD *)a2 + 32);
  *((_QWORD *)a2 + 31) = i_2;
  i_1 = i_2;
  v10 = i_3 >= i_2;
  i_4 = i_2;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 33);
    if ( (unsigned int)(int)(float)((float)(unsigned int)i_2 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)i_2 * 1.75);
    *((_QWORD *)a2 + 32) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    i_4 = *((_QWORD *)a2 + 31);
    *((_QWORD *)a2 + 33) = v15;
  }
  while ( i_5 < i_4 )
  {
    *(_QWORD *)(*((_QWORD *)a2 + 33) + 8 * i_5++) = 0;
    i_4 = *((_QWORD *)a2 + 31);
  }
  if ( (_DWORD)i_1 )
  {
    for ( i = 0; i != i_1; ++i )
    {
      v17 = *((_QWORD *)this + 14);
      v70 = 0;
      v71 = 0;
      endptr = endptr;
      v18 = *((_QWORD *)this + 11);
      v72 = 0;
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
          v70 = strlen(&v20[v19]);
          v71 = v21;
          v72 = 1;
        }
      }
      v22 = spine::SpineObject::operator new(
              (spine::SpineObject *)&qword_90,
              (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3"
                                "/SCSLoader_v3.cpp",
              (const char *)&qword_100,
              a4);
      v23 = (spine::SpineExtension *)spine::v3::TransformConstraintData::TransformConstraintData(
                                       (spine::v3::TransformConstraintData *)v22,
                                       (const spine::String *)&endptr);
      *(_QWORD *)(*((_QWORD *)a2 + 33) + 8 * i) = v22;
      v24 = *((_QWORD *)this + 14);
      v25 = *(unsigned int *)(*((_QWORD *)this + 11) + v24);
      *((_QWORD *)this + 14) = v24 + 4;
      *(_QWORD *)(v22 + 40) = v25;
      v26 = *((_QWORD *)this + 14);
      LODWORD(v25) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v26);
      *((_QWORD *)this + 14) = v26 + 1;
      *(_BYTE *)(v22 + 48) = (_DWORD)v25 != 0;
      *(_DWORD *)(v22 + 96) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
      v27 = *((_QWORD *)this + 11);
      v28 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v28;
      *(_DWORD *)(v22 + 100) = *(_DWORD *)(v27 + v28);
      v29 = *((_QWORD *)this + 11);
      v30 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v30;
      *(_DWORD *)(v22 + 104) = *(_DWORD *)(v29 + v30);
      v31 = *((_QWORD *)this + 11);
      v32 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v32;
      *(_DWORD *)(v22 + 108) = *(_DWORD *)(v31 + v32);
      v33 = *((_QWORD *)this + 11);
      v34 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v34;
      *(_DWORD *)(v22 + 112) = *(_DWORD *)(v33 + v34);
      v35 = *((_QWORD *)this + 11);
      v36 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v36;
      *(_DWORD *)(v22 + 116) = *(_DWORD *)(v35 + v36);
      v37 = *((_QWORD *)this + 11);
      v38 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v38;
      *(_DWORD *)(v22 + 120) = *(_DWORD *)(v37 + v38);
      v39 = *((_QWORD *)this + 11);
      v40 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v40;
      *(_DWORD *)(v22 + 124) = *(_DWORD *)(v39 + v40);
      v41 = *((_QWORD *)this + 11);
      v42 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v42;
      *(_DWORD *)(v22 + 128) = *(_DWORD *)(v41 + v42);
      v43 = *((_QWORD *)this + 11);
      v44 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v44;
      *(_DWORD *)(v22 + 132) = *(_DWORD *)(v43 + v44);
      v45 = *((_QWORD *)this + 14);
      v46 = *((_QWORD *)this + 11);
      *((_QWORD *)this + 14) = v45 + 4;
      LODWORD(v43) = *(unsigned __int8 *)(v46 + v45 + 4);
      *((_QWORD *)this + 14) = v45 + 5;
      *(_BYTE *)(v22 + 136) = (_DWORD)v43 != 0;
      v47 = *((_QWORD *)this + 14);
      LODWORD(v45) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v47);
      *((_QWORD *)this + 14) = v47 + 1;
      *(_BYTE *)(v22 + 137) = (_DWORD)v45 != 0;
      v48 = *((_QWORD *)this + 11);
      v49 = *((_QWORD *)this + 14);
      v50 = *(__int16 *)(v48 + v49);
      v51 = v49 + 2;
      *((_QWORD *)this + 14) = v51;
      if ( (v50 & 0x8000000000000000LL) == 0 )
      {
        *(_QWORD *)(v22 + 88) = *(_QWORD *)(*((_QWORD *)a2 + 8) + 8 * v50);
        v48 = *((_QWORD *)this + 11);
        v51 = *((_QWORD *)this + 14);
      }
      v52 = *(unsigned __int16 *)(v48 + v51);
      for ( *((_QWORD *)this + 14) = v51 + 2; v52; --v52 )
      {
        v56 = *((_QWORD *)this + 14);
        v57 = v56 + 2;
        v58 = *(__int16 *)(*((_QWORD *)this + 11) + v56);
        *((_QWORD *)this + 14) = v57;
        v59 = *(_QWORD *)(v22 + 64);
        v60 = *((_QWORD *)a2 + 8);
        if ( v59 == *(_QWORD *)(v22 + 72) )
        {
          v61 = *(_QWORD *)(v60 + 8 * v58);
          v62 = *(_QWORD *)(v22 + 80);
          n8_1 = (int)(float)((float)v59 * 1.75);
          if ( (unsigned int)n8_1 <= 8 )
            n8_1 = 8;
          n8_2 = n8_1;
          *(_QWORD *)(v22 + 72) = n8_1;
          InstanceEv = spine::SpineExtension::getInstance(v23);
          v23 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv + 32LL))(
                                           InstanceEv,
                                           v62,
                                           8 * n8_2,
                                           "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.andro"
                                           "idstudio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/sp"
                                           "ine/cpp/Vector.h",
                                           109);
          v66 = *(_QWORD *)(v22 + 64);
          *(_QWORD *)(v22 + 80) = v23;
          *(_QWORD *)(v22 + 64) = v66 + 1;
          *((_QWORD *)v23 + v66) = v61;
        }
        else
        {
          v55 = *(_QWORD *)(v22 + 80);
          *(_QWORD *)(v22 + 64) = v59 + 1;
          *(_QWORD *)(v55 + 8 * v59) = *(_QWORD *)(v60 + 8 * v58);
        }
      }
      v53 = v71;
      endptr = endptr;
      if ( v71 && (v72 & 1) == 0 )
      {
        InstanceEv_1 = spine::SpineExtension::getInstance(v23);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
          InstanceEv_1,
          v53,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
    }
  }
  return 1;
}