__int64 __fastcall spine::v3::SkeletonDataLoader::loadIkConstraints(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        __int64 a3,
        int a4)
{
  __int64 v6; // x8
  unsigned __int64 v7; // x25
  unsigned __int64 v8; // x8
  unsigned __int64 v9; // x22
  bool v10; // cf
  unsigned __int64 v11; // x8
  __int64 v12; // x21
  int n8; // w23
  __int64 Instance; // x0
  __int64 v15; // x0
  __int64 *p__ZTVN5spine6StringE; // x21
  __int64 v17; // x28
  const char *_Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client; // x27
  __int64 v19; // x9
  __int64 v20; // x8
  char *v21; // x9
  char *v22; // x24
  __int64 v23; // x24
  spine::SpineExtension *v24; // x0
  __int64 v25; // x9
  __int64 v26; // x8
  __int64 v27; // x9
  __int64 v28; // x9
  __int64 v29; // x9
  __int64 v30; // x9
  __int64 v31; // x8
  __int64 v32; // x8
  __int64 v33; // x10
  __int64 v34; // x9
  __int64 v35; // x8
  __int64 v36; // x9
  __int64 v37; // x10
  __int64 v38; // x9
  unsigned __int64 v39; // x26
  unsigned __int64 v40; // x8
  unsigned __int64 v41; // x22
  unsigned __int64 v42; // x8
  const char *_Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client_1; // x28
  __int64 *p__ZTVN5spine6StringE_1; // x23
  unsigned __int64 v45; // x21
  __int64 v46; // x25
  int n8_1; // w8
  __int64 n8_2; // x27
  __int64 InstanceEv; // x0
  __int64 v50; // x9
  __int64 v51; // x11
  __int64 v52; // x10
  char *v53; // x24
  __int64 InstanceEv_1; // x0
  __int64 v56; // [xsp+18h] [xbp-48h]
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+28h] [xbp-38h] BYREF
  size_t v58; // [xsp+30h] [xbp-30h]
  char *v59; // [xsp+38h] [xbp-28h]
  char v60; // [xsp+40h] [xbp-20h]
  __int64 v61; // [xsp+48h] [xbp-18h]

  v61 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v6 = *((_QWORD *)this + 14);
  v7 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  v9 = *((_QWORD *)a2 + 27);
  v8 = *((_QWORD *)a2 + 28);
  *((_QWORD *)a2 + 27) = v7;
  v10 = v8 >= v7;
  v11 = v7;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 29);
    if ( (unsigned int)(int)(float)((float)(unsigned int)v7 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v7 * 1.75);
    *((_QWORD *)a2 + 28) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    v11 = *((_QWORD *)a2 + 27);
    *((_QWORD *)a2 + 29) = v15;
  }
  while ( v9 < v11 )
  {
    *(_QWORD *)(*((_QWORD *)a2 + 29) + 8 * v9++) = 0;
    v11 = *((_QWORD *)a2 + 27);
  }
  if ( (_DWORD)v7 )
  {
    p__ZTVN5spine6StringE = &vtable for spine::String;
    v17 = 0;
    _Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client = "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live"
                                                                      "/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp";
    do
    {
      v19 = *((_QWORD *)this + 14);
      v58 = 0;
      v59 = 0;
      v60 = 0;
      endptr = endptr;
      v20 = *(unsigned int *)(*((_QWORD *)this + 11) + v19);
      *((_QWORD *)this + 14) = v19 + 4;
      if ( (_DWORD)v20 != -1 )
      {
        v21 = (char *)this + 121;
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v21 = (char *)*((_QWORD *)this + 17);
        if ( v21 )
        {
          v22 = &v21[v20];
          v58 = strlen(&v21[v20]);
          v59 = v22;
          v60 = 1;
        }
      }
      v23 = spine::SpineObject::operator new(
              (spine::SpineObject *)&qword_70,
              (unsigned __int64)_Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client,
              (const char *)&dword_B0,
              a4);
      v24 = (spine::SpineExtension *)spine::v3::IkConstraintData::IkConstraintData(
                                       (spine::v3::IkConstraintData *)v23,
                                       (const spine::String *)&endptr);
      *(_QWORD *)(*((_QWORD *)a2 + 29) + 8 * v17) = v23;
      v25 = *((_QWORD *)this + 14);
      v26 = *(unsigned int *)(*((_QWORD *)this + 11) + v25);
      *((_QWORD *)this + 14) = v25 + 4;
      *(_QWORD *)(v23 + 40) = v26;
      v27 = *((_QWORD *)this + 14);
      LODWORD(v26) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v27);
      *((_QWORD *)this + 14) = v27 + 1;
      *(_BYTE *)(v23 + 48) = (_DWORD)v26 != 0;
      v28 = *((_QWORD *)this + 14);
      LODWORD(v26) = *(_DWORD *)(*((_QWORD *)this + 11) + v28);
      *((_QWORD *)this + 14) = v28 + 4;
      *(_DWORD *)(v23 + 96) = v26;
      v29 = *((_QWORD *)this + 14);
      LODWORD(v26) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v29);
      *((_QWORD *)this + 14) = v29 + 1;
      *(_BYTE *)(v23 + 100) = (_DWORD)v26 != 0;
      *(_DWORD *)(v23 + 104) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
      v30 = *((_QWORD *)this + 11);
      v31 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v31;
      *(_DWORD *)(v23 + 108) = *(_DWORD *)(v30 + v31);
      v32 = *((_QWORD *)this + 14);
      v33 = *((_QWORD *)this + 11);
      *((_QWORD *)this + 14) = v32 + 4;
      LODWORD(v30) = *(unsigned __int8 *)(v33 + v32 + 4);
      *((_QWORD *)this + 14) = v32 + 5;
      *(_BYTE *)(v23 + 101) = (_DWORD)v30 != 0;
      v34 = *((_QWORD *)this + 14);
      LODWORD(v32) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v34);
      *((_QWORD *)this + 14) = v34 + 1;
      *(_BYTE *)(v23 + 102) = (_DWORD)v32 != 0;
      v35 = *((_QWORD *)this + 11);
      v36 = *((_QWORD *)this + 14);
      v37 = *(__int16 *)(v35 + v36);
      v38 = v36 + 2;
      *((_QWORD *)this + 14) = v38;
      if ( (v37 & 0x8000000000000000LL) == 0 )
      {
        *(_QWORD *)(v23 + 88) = *(_QWORD *)(*((_QWORD *)a2 + 8) + 8 * v37);
        v35 = *((_QWORD *)this + 11);
        v38 = *((_QWORD *)this + 14);
      }
      v39 = *(unsigned __int16 *)(v35 + v38);
      *((_QWORD *)this + 14) = v38 + 2;
      v41 = *(_QWORD *)(v23 + 64);
      v40 = *(_QWORD *)(v23 + 72);
      *(_QWORD *)(v23 + 64) = v39;
      v10 = v40 >= v39;
      v42 = v39;
      if ( !v10 )
      {
        v56 = v17;
        _Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client_1 = _Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client;
        p__ZTVN5spine6StringE_1 = p__ZTVN5spine6StringE;
        v45 = v7;
        v46 = *(_QWORD *)(v23 + 80);
        n8_1 = (int)(float)((float)(unsigned int)v39 * 1.75);
        if ( (unsigned int)n8_1 <= 8 )
          n8_1 = 8;
        n8_2 = n8_1;
        *(_QWORD *)(v23 + 72) = n8_1;
        InstanceEv = spine::SpineExtension::getInstance(v24);
        v24 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv + 32LL))(
                                         InstanceEv,
                                         v46,
                                         8 * n8_2,
                                         "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.android"
                                         "studio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                                         85);
        v42 = *(_QWORD *)(v23 + 64);
        _Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client = _Users_dev_.jenkins_workspace_App_Epic7_Stove_Live_epic7_client_1;
        v17 = v56;
        *(_QWORD *)(v23 + 80) = v24;
        v7 = v45;
        p__ZTVN5spine6StringE = p__ZTVN5spine6StringE_1;
      }
      while ( v41 < v42 )
      {
        *(_QWORD *)(*(_QWORD *)(v23 + 80) + 8 * v41++) = 0;
        v42 = *(_QWORD *)(v23 + 64);
      }
      if ( (_DWORD)v39 )
      {
        v50 = 0;
        do
        {
          v51 = *((_QWORD *)this + 14);
          v52 = *(__int16 *)(*((_QWORD *)this + 11) + v51);
          *((_QWORD *)this + 14) = v51 + 2;
          if ( (v52 & 0x8000000000000000LL) == 0 )
            *(_QWORD *)(*(_QWORD *)(v23 + 80) + v50) = *(_QWORD *)(*((_QWORD *)a2 + 8) + 8 * v52);
          v50 += 8;
        }
        while ( 8 * v39 != v50 );
      }
      v53 = v59;
      endptr = (void (__fastcall **)(spine::String *__hidden))(p__ZTVN5spine6StringE + 2);
      if ( v59 && (v60 & 1) == 0 )
      {
        InstanceEv_1 = spine::SpineExtension::getInstance(v24);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
          InstanceEv_1,
          v53,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
      ++v17;
    }
    while ( v17 != v7 );
  }
  return 1;
}
