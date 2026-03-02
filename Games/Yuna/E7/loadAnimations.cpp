__int64 __fastcall spine::v3::SkeletonDataLoader::loadAnimations(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        spine::SkeletonDataV3 *a3)
{
  spine::v3::SkeletonDataLoader *this_1; // x20
  __int64 v5; // x8
  __int64 v6; // x21
  __int64 v7; // x22
  unsigned __int64 v8; // x10
  _QWORD *v9; // x27
  __int64 v10; // x9
  _QWORD *v11; // x28
  unsigned __int64 v12; // x22
  unsigned __int64 v13; // x8
  _BOOL4 v14; // w23
  unsigned __int64 v15; // x21
  __int64 v16; // x9
  __int64 v17; // x24
  __int64 Instance; // x0
  __int64 v19; // x21
  char v20; // w8
  __int64 v21; // x9
  __int64 v22; // x8
  __int64 v23; // x10
  __int64 v24; // x9
  char *v25; // x11
  char *s_1; // x24
  size_t v27; // x0
  int v28; // w3
  char *s_2; // x25
  size_t n0x17; // x0
  size_t n; // x24
  char *dest; // x26
  __int64 v33; // x24
  __int64 v34; // x0
  unsigned __int64 v35; // x8
  __int64 v36; // x25
  int n8; // w8
  __int64 n8_1; // x26
  __int64 InstanceEv; // x0
  __int64 v40; // x8
  spine::v3::SkeletonData *v41; // x21
  spine::v3::SkeletonDataLoader *this_2; // x19
  _QWORD *v43; // x20
  _BOOL4 v44; // w28
  unsigned __int64 v45; // x23
  _QWORD *v46; // x22
  unsigned __int64 n26; // x27
  char *dest_1; // x0
  __int64 v49; // x8
  int v50; // w3
  __int64 v51; // x24
  __int64 v52; // x25
  __int64 v53; // x24
  unsigned __int64 v54; // x8
  __int64 v55; // x25
  int n8_2; // w8
  __int64 n8_3; // x26
  __int64 InstanceEv_1; // x0
  __int64 v59; // x8
  __int64 v60; // x9
  unsigned __int64 v61; // x8
  signed __int64 v62; // x25
  __int64 v63; // x24
  bool v64; // cc
  __int64 v65; // x9
  unsigned __int64 v66; // x10
  __int64 v67; // x9
  char v68; // w25
  __int64 v69; // x24
  __int64 InstanceEv_2; // x0
  spine::SpineExtension *v71; // x0
  char *s_3; // x24
  __int64 InstanceEv_3; // x0
  void **v74; // x19
  void *v75; // x0
  void **v77; // x20
  __int64 v78; // [xsp+18h] [xbp-D8h]
  char *v79; // [xsp+20h] [xbp-D0h]
  _QWORD v80[2]; // [xsp+38h] [xbp-B8h] BYREF
  void *dest_2; // [xsp+48h] [xbp-A8h]
  __int64 (__fastcall **v82)(spine::SpineObject *); // [xsp+50h] [xbp-A0h] BYREF
  unsigned __int64 v83; // [xsp+58h] [xbp-98h]
  __int64 v84; // [xsp+60h] [xbp-90h]
  __int64 v85; // [xsp+68h] [xbp-88h]
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+70h] [xbp-80h] BYREF
  size_t v87; // [xsp+78h] [xbp-78h]
  char *s; // [xsp+80h] [xbp-70h]
  char v89; // [xsp+88h] [xbp-68h]
  __int128 v90; // [xsp+90h] [xbp-60h] BYREF
  __int128 v91; // [xsp+A0h] [xbp-50h]
  int n1065353216; // [xsp+B0h] [xbp-40h]
  __int64 v93; // [xsp+B8h] [xbp-38h] BYREF
  char v94; // [xsp+C8h] [xbp-28h]
  __int64 v95; // [xsp+D0h] [xbp-20h]

  this_1 = this;
  v95 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v90 = 0u;
  v91 = 0u;
  n1065353216 = 1065353216;
  if ( !a3 || (v5 = *((_QWORD *)a3 + 10), v6 = *(_QWORD *)(v5 + 136), v7 = *(_QWORD *)(v5 + 144), v6 == v7) )
  {
    v14 = 0;
    v9 = (_QWORD *)((char *)this + 88);
    v11 = (_QWORD *)((char *)this + 112);
    v16 = *((_QWORD *)this + 14);
    v12 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v16);
    *((_QWORD *)this + 14) = v16 + 2;
    v15 = v12;
  }
  else
  {
    do
    {
      this = (spine::v3::SkeletonDataLoader *)std::__hash_table<std::string,std::hash<std::string>,std::equal_to<std::string>,std::allocator<std::string>>::__emplace_unique_key_args<std::string,std::string const&>(
                                                &v90,
                                                v6,
                                                v6);
      v6 += 24;
    }
    while ( v6 != v7 );
    v8 = *((_QWORD *)&v91 + 1);
    v9 = (_QWORD *)((char *)this_1 + 88);
    v11 = (_QWORD *)((char *)this_1 + 112);
    v10 = *((_QWORD *)this_1 + 14);
    v12 = *(unsigned __int16 *)(*((_QWORD *)this_1 + 11) + v10);
    *((_QWORD *)this_1 + 14) = v10 + 2;
    if ( v8 >= v12 )
      v13 = v12;
    else
      v13 = v8;
    v14 = v8 != 0;
    if ( v8 )
      v15 = v13;
    else
      v15 = v12;
  }
  if ( *((_QWORD *)a2 + 24) < v15 )
  {
    v17 = *((_QWORD *)a2 + 25);
    *((_QWORD *)a2 + 24) = v15;
    Instance = spine::SpineExtension::getInstance(this);
    *((_QWORD *)a2 + 25) = (*(__int64 (__fastcall **)(__int64, __int64, unsigned __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
                             Instance,
                             v17,
                             8 * v15,
                             "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/s"
                             "rc/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                             97);
  }
  if ( v12 )
  {
    v79 = (char *)this_1 + 121;
    v19 = 0;
    do
    {
      v21 = *v11;
      v87 = 0;
      s = 0;
      endptr = endptr;
      v22 = *v9;
      v89 = 0;
      v23 = *(unsigned int *)(v22 + v21);
      v24 = v21 + 4;
      *v11 = v24;
      if ( (_DWORD)v23 != -1 )
      {
        v25 = v79;
        if ( (*((_BYTE *)this_1 + 120) & 1) != 0 )
          v25 = (char *)*((_QWORD *)this_1 + 17);
        if ( v25 )
        {
          s_1 = &v25[v23];
          v27 = strlen(&v25[v23]);
          v24 = *v11;
          v87 = v27;
          s = s_1;
          v89 = 1;
        }
      }
      *((_QWORD *)this_1 + 14) = v24 + 4;
      v82 = off_163C2D8;
      v84 = 0;
      v85 = 0;
      v83 = 0;
      spine::v3::SkeletonDataLoader::loadTimeline(this_1, a2, &v82);
      if ( !v14 )
      {
        v33 = spine::SpineObject::operator new(
                (spine::SpineObject *)off_50,
                (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/"
                                  "v3/SCSLoader_v3.cpp",
                (const char *)&stru_370.st_value + 2,
                v28);
        v34 = spine::v3::Animation::Animation(v33, (spine::String *)&endptr);
        v35 = *((_QWORD *)a2 + 23);
        if ( v35 == *((_QWORD *)a2 + 24) )
        {
          v36 = *((_QWORD *)a2 + 25);
          n8 = (int)(float)((float)v35 * 1.75);
          if ( (unsigned int)n8 <= 8 )
            n8 = 8;
          n8_1 = n8;
          *((_QWORD *)a2 + 24) = n8;
          InstanceEv = spine::SpineExtension::getInstance((spine::SpineExtension *)v34);
          v34 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv
                                                                                            + 32LL))(
                  InstanceEv,
                  v36,
                  8 * n8_1,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  109);
          v40 = *((_QWORD *)a2 + 23);
          *((_QWORD *)a2 + 25) = v34;
          *((_QWORD *)a2 + 23) = v40 + 1;
          *(_QWORD *)(v34 + 8 * v40) = v33;
        }
        else
        {
          v60 = *((_QWORD *)a2 + 25);
          *((_QWORD *)a2 + 23) = v35 + 1;
          *(_QWORD *)(v60 + 8 * v35) = v33;
        }
        goto LABEL_63;
      }
      s_2 = s;
      n0x17 = strlen(s);
      if ( n0x17 >= 0xFFFFFFFFFFFFFFF8LL )
        sub_A0F02C();
      n = n0x17;
      if ( n0x17 >= 0x17 )
      {
        v78 = v19;
        v41 = a2;
        this_2 = this_1;
        v43 = v11;
        v44 = v14;
        v45 = v12;
        v46 = v9;
        if ( (n0x17 | 7) == 0x17 )
          n26 = 26;
        else
          n26 = (n0x17 | 7) + 1;
        dest_1 = (char *)operator new(n26);
        v49 = n26 | 1;
        v9 = v46;
        v12 = v45;
        v14 = v44;
        v11 = v43;
        this_1 = this_2;
        a2 = v41;
        v19 = v78;
        dest = dest_1;
        v80[1] = n;
        dest_2 = dest_1;
        v80[0] = v49;
      }
      else
      {
        dest = (char *)v80 + 1;
        LOBYTE(v80[0]) = 2 * n0x17;
        if ( !n0x17 )
          goto LABEL_38;
      }
      memmove(dest, s_2, n);
LABEL_38:
      dest[n] = 0;
      v34 = std::__hash_table<std::string,std::hash<std::string>,std::equal_to<std::string>,std::allocator<std::string>>::find<std::string>(
              &v90,
              v80);
      v51 = v34;
      if ( v34 )
      {
        sub_A3FDF4(&v93, &v90, v34);
        v34 = v93;
        v93 = 0;
        if ( v34 )
        {
          if ( v94 == 1 && (*(_BYTE *)(v34 + 16) & 1) != 0 )
          {
            v52 = v34;
            operator delete(*(void **)(v34 + 32), *(_QWORD *)(v34 + 16) & 0xFFFFFFFFFFFFFFFELL);
            v34 = v52;
          }
          operator delete((void *)v34, 0x28u);
        }
      }
      if ( (v80[0] & 1) != 0 )
        operator delete(dest_2, v80[0] & 0xFFFFFFFFFFFFFFFELL);
      if ( v51 )
      {
        v53 = spine::SpineObject::operator new(
                (spine::SpineObject *)off_50,
                (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/"
                                  "v3/SCSLoader_v3.cpp",
                (const char *)&stru_370,
                v50);
        v34 = spine::v3::Animation::Animation(v53, (spine::String *)&endptr);
        v54 = *((_QWORD *)a2 + 23);
        if ( v54 == *((_QWORD *)a2 + 24) )
        {
          v55 = *((_QWORD *)a2 + 25);
          n8_2 = (int)(float)((float)v54 * 1.75);
          if ( (unsigned int)n8_2 <= 8 )
            n8_2 = 8;
          n8_3 = n8_2;
          *((_QWORD *)a2 + 24) = n8_2;
          InstanceEv_1 = spine::SpineExtension::getInstance((spine::SpineExtension *)v34);
          v34 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_1
                                                                                            + 32LL))(
                  InstanceEv_1,
                  v55,
                  8 * n8_3,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  109);
          v59 = *((_QWORD *)a2 + 23);
          *((_QWORD *)a2 + 25) = v34;
          *((_QWORD *)a2 + 23) = v59 + 1;
          *(_QWORD *)(v34 + 8 * v59) = v53;
          if ( !*((_QWORD *)&v91 + 1) )
          {
LABEL_69:
            v68 = 1;
            goto LABEL_64;
          }
        }
        else
        {
          v67 = *((_QWORD *)a2 + 25);
          *((_QWORD *)a2 + 23) = v54 + 1;
          *(_QWORD *)(v67 + 8 * v54) = v53;
          if ( !*((_QWORD *)&v91 + 1) )
            goto LABEL_69;
        }
      }
      else
      {
        v61 = v83;
        if ( (int)v83 >= 1 )
        {
          v62 = v83 & 0x7FFFFFFF;
          v63 = 8 * v62 - 8;
          do
          {
            v34 = *(_QWORD *)(v85 + 8 * (v62 - 1));
            if ( v34 )
            {
              v34 = (*(__int64 (__fastcall **)(__int64))(*(_QWORD *)v34 + 8LL))(v34);
              v61 = v83;
            }
            v83 = --v61;
            if ( v61 > v62 - 1 )
            {
              v65 = v63;
              v66 = v62 - 1;
              do
              {
                ++v66;
                *(int8x16_t *)(v85 + v65) = vextq_s8(*(int8x16_t *)(v85 + v65), *(int8x16_t *)(v85 + v65), 8u);
                v65 += 8;
                v61 = v83;
              }
              while ( v66 < v83 );
            }
            v64 = v62 <= 1;
            v63 -= 8;
            --v62;
          }
          while ( !v64 );
        }
      }
LABEL_63:
      v68 = 0;
LABEL_64:
      v69 = v85;
      v82 = off_163C2D8;
      v83 = 0;
      if ( v85 )
      {
        InstanceEv_2 = spine::SpineExtension::getInstance((spine::SpineExtension *)v34);
        (*(void (__fastcall **)(__int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_2 + 40LL))(
          InstanceEv_2,
          v69,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
          226);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&v82);
      s_3 = s;
      endptr = endptr;
      if ( s && (v89 & 1) == 0 )
      {
        InstanceEv_3 = spine::SpineExtension::getInstance(v71);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_3 + 40LL))(
          InstanceEv_3,
          s_3,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
      if ( ++v19 == v12 )
        v20 = 1;
      else
        v20 = v68;
    }
    while ( (v20 & 1) == 0 );
  }
  v74 = (void **)v91;
  if ( (_QWORD)v91 )
  {
    do
    {
      v77 = (void **)*v74;
      if ( ((_BYTE)v74[2] & 1) != 0 )
        operator delete(v74[4], (unsigned __int64)v74[2] & 0xFFFFFFFFFFFFFFFELL);
      operator delete(v74, 0x28u);
      v74 = v77;
    }
    while ( v77 );
  }
  v75 = (void *)v90;
  *(_QWORD *)&v90 = 0;
  if ( v75 )
    operator delete(v75, 8LL * *((_QWORD *)&v90 + 1));
  return 1;
}