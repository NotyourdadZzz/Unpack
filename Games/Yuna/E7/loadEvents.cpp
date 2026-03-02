__int64 __fastcall spine::v3::SkeletonDataLoader::loadEvents(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        __int64 a3,
        int a4)
{
  __int64 v6; // x8
  unsigned __int64 v7; // x24
  unsigned __int64 v8; // x8
  unsigned __int64 v9; // x22
  bool v10; // cf
  unsigned __int64 v11; // x8
  __int64 v12; // x21
  int n8; // w23
  __int64 Instance; // x0
  __int64 v15; // x0
  __int64 v16; // x23
  __int64 *p__ZTVN5spine6StringE; // x28
  __int64 v18; // x9
  __int64 v19; // x8
  spine::v3::SkeletonDataLoader *v20; // x9
  const char *s_6; // x24
  spine::v3::EventData *v22; // x24
  const char *src; // x26
  size_t n0x17; // x0
  size_t n; // x25
  char *dest; // x27
  __int64 *p__ZTVN5spine6StringE_1; // x21
  unsigned __int64 n26; // x28
  spine::SpineExtension *v29; // x0
  char v30; // w8
  __int64 v31; // x9
  int v32; // w8
  __int64 v33; // x9
  __int64 v34; // x10
  __int64 v35; // x8
  char *v36; // x9
  const char *s_1; // x25
  const char *s_2; // x26
  __int64 InstanceEv; // x0
  __int64 v40; // x9
  __int64 v41; // x8
  char *v42; // x9
  const char *s_3; // x25
  const char *s_4; // x26
  __int64 InstanceEv_1; // x0
  __int64 v46; // x9
  __int64 v47; // x8
  const char *s_5; // x24
  __int64 InstanceEv_2; // x0
  __int64 v51; // [xsp+10h] [xbp-60h]
  _QWORD v52[2]; // [xsp+20h] [xbp-50h] BYREF
  void *dest_1; // [xsp+30h] [xbp-40h]
  char v54; // [xsp+3Fh] [xbp-31h] BYREF
  _QWORD *v55; // [xsp+40h] [xbp-30h] BYREF
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+48h] [xbp-28h] BYREF
  size_t v57; // [xsp+50h] [xbp-20h]
  const char *s; // [xsp+58h] [xbp-18h]
  char v59; // [xsp+60h] [xbp-10h]
  __int64 v60; // [xsp+68h] [xbp-8h]

  v60 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v6 = *((_QWORD *)this + 14);
  v7 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  v9 = *((_QWORD *)a2 + 19);
  v8 = *((_QWORD *)a2 + 20);
  *((_QWORD *)a2 + 19) = v7;
  v10 = v8 >= v7;
  v11 = v7;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 21);
    if ( (unsigned int)(int)(float)((float)(unsigned int)v7 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v7 * 1.75);
    *((_QWORD *)a2 + 20) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    v11 = *((_QWORD *)a2 + 19);
    *((_QWORD *)a2 + 21) = v15;
  }
  while ( v9 < v11 )
  {
    *(_QWORD *)(*((_QWORD *)a2 + 21) + 8 * v9++) = 0;
    v11 = *((_QWORD *)a2 + 19);
  }
  if ( (_DWORD)v7 )
  {
    v16 = 0;
    p__ZTVN5spine6StringE = &vtable for spine::String;
    v51 = 8 * v7;
    do
    {
      v18 = *((_QWORD *)this + 14);
      v57 = 0;
      s = 0;
      v59 = 0;
      endptr = endptr;
      v19 = *(unsigned int *)(*((_QWORD *)this + 11) + v18);
      *((_QWORD *)this + 14) = v18 + 4;
      if ( (_DWORD)v19 != -1 )
      {
        v20 = (*((_BYTE *)this + 120) & 1) != 0
            ? (spine::v3::SkeletonDataLoader *)*((_QWORD *)this + 17)
            : (spine::v3::SkeletonDataLoader *)((char *)this + 121);
        if ( v20 )
        {
          s_6 = (char *)v20 + v19;
          v57 = strlen((const char *)v20 + v19);
          s = s_6;
          v59 = 1;
        }
      }
      v22 = (spine::v3::EventData *)spine::SpineObject::operator new(
                                      (spine::SpineObject *)&dword_78,
                                      (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/"
                                                        "ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                                      &byte_24C[27],
                                      a4);
      spine::v3::EventData::EventData(v22, (const spine::String *)&endptr);
      src = s;
      n0x17 = strlen(s);
      if ( n0x17 >= 0xFFFFFFFFFFFFFFF8LL )
        sub_A0F02C();
      n = n0x17;
      if ( n0x17 >= 0x17 )
      {
        p__ZTVN5spine6StringE_1 = p__ZTVN5spine6StringE;
        if ( (n0x17 | 7) == 0x17 )
          n26 = 26;
        else
          n26 = (n0x17 | 7) + 1;
        dest = (char *)operator new(n26);
        v52[1] = n;
        dest_1 = dest;
        v52[0] = n26 | 1;
        p__ZTVN5spine6StringE = p__ZTVN5spine6StringE_1;
      }
      else
      {
        dest = (char *)v52 + 1;
        LOBYTE(v52[0]) = 2 * n0x17;
        if ( !n0x17 )
          goto LABEL_26;
      }
      memmove(dest, src, n);
LABEL_26:
      dest[n] = 0;
      v55 = v52;
      v29 = (spine::SpineExtension *)std::__hash_table<std::__hash_value_type<std::string,spine::v3::EventData *>,std::__unordered_map_hasher<std::string,std::__hash_value_type<std::string,spine::v3::EventData *>,std::hash<std::string>,std::equal_to<std::string>,true>,std::__unordered_map_equal<std::string,std::__hash_value_type<std::string,spine::v3::EventData *>,std::equal_to<std::string>,std::hash<std::string>,true>,std::allocator<std::__hash_value_type<std::string,spine::v3::EventData *>>>::__emplace_unique_key_args<std::string,std::piecewise_construct_t const&,std::tuple<std::string&&>,std::tuple<>>(
                                       (char *)this + 176,
                                       v52,
                                       &std::piecewise_construct,
                                       &v55,
                                       &v54);
      v30 = v52[0];
      *((_QWORD *)v29 + 5) = v22;
      if ( (v30 & 1) != 0 )
        operator delete(dest_1, v52[0] & 0xFFFFFFFFFFFFFFFELL);
      *(_QWORD *)(*((_QWORD *)a2 + 21) + v16) = v22;
      v31 = *((_QWORD *)this + 14);
      v32 = *(_DWORD *)(*((_QWORD *)this + 11) + v31);
      *((_QWORD *)this + 14) = v31 + 4;
      *((_DWORD *)v22 + 10) = v32;
      *((_DWORD *)v22 + 11) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
      v33 = *((_QWORD *)this + 14);
      v34 = *((_QWORD *)this + 11);
      *((_QWORD *)this + 14) = v33 + 4;
      v35 = *(unsigned int *)(v34 + v33 + 4);
      *((_QWORD *)this + 14) = v33 + 8;
      if ( (_DWORD)v35 == -1 )
      {
        s_1 = 0;
      }
      else
      {
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v36 = (char *)*((_QWORD *)this + 17);
        else
          v36 = (char *)this + 121;
        s_1 = &v36[v35];
      }
      s_2 = (const char *)*((_QWORD *)v22 + 8);
      if ( s_2 != s_1 )
      {
        if ( s_2 && (*((_BYTE *)v22 + 72) & 1) == 0 )
        {
          InstanceEv = spine::SpineExtension::getInstance(v29);
          v29 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv + 40LL))(
                                           InstanceEv,
                                           s_2,
                                           "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.andro"
                                           "idstudio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/sp"
                                           "ine/cpp/SpineString.h",
                                           129);
        }
        if ( s_1 )
        {
          v29 = (spine::SpineExtension *)strlen(s_1);
          *((_QWORD *)v22 + 7) = v29;
          *((_QWORD *)v22 + 8) = s_1;
          *((_BYTE *)v22 + 72) = 1;
        }
        else
        {
          *((_QWORD *)v22 + 7) = 0;
          *((_QWORD *)v22 + 8) = 0;
          *((_BYTE *)v22 + 72) = 0;
        }
      }
      v40 = *((_QWORD *)this + 14);
      v41 = *(unsigned int *)(*((_QWORD *)this + 11) + v40);
      *((_QWORD *)this + 14) = v40 + 4;
      if ( (_DWORD)v41 == -1 )
      {
        s_3 = 0;
      }
      else
      {
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v42 = (char *)*((_QWORD *)this + 17);
        else
          v42 = (char *)this + 121;
        s_3 = &v42[v41];
      }
      s_4 = (const char *)*((_QWORD *)v22 + 12);
      if ( s_4 != s_3 )
      {
        if ( s_4 && (*((_BYTE *)v22 + 104) & 1) == 0 )
        {
          InstanceEv_1 = spine::SpineExtension::getInstance(v29);
          v29 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
                                           InstanceEv_1,
                                           s_4,
                                           "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.andro"
                                           "idstudio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/sp"
                                           "ine/cpp/SpineString.h",
                                           129);
        }
        if ( s_3 )
        {
          v29 = (spine::SpineExtension *)strlen(s_3);
          *((_QWORD *)v22 + 11) = v29;
          *((_QWORD *)v22 + 12) = s_3;
          *((_BYTE *)v22 + 104) = 1;
        }
        else
        {
          *((_QWORD *)v22 + 11) = 0;
          *((_QWORD *)v22 + 12) = 0;
          *((_BYTE *)v22 + 104) = 0;
        }
      }
      *((_DWORD *)v22 + 28) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
      v46 = *((_QWORD *)this + 11);
      v47 = *((_QWORD *)this + 14) + 4LL;
      *((_QWORD *)this + 14) = v47;
      LODWORD(v47) = *(_DWORD *)(v46 + v47);
      endptr = (void (__fastcall **)(spine::String *__hidden))(p__ZTVN5spine6StringE + 2);
      *((_DWORD *)v22 + 29) = v47;
      s_5 = s;
      *((_QWORD *)this + 14) += 4LL;
      if ( s_5 && (v59 & 1) == 0 )
      {
        InstanceEv_2 = spine::SpineExtension::getInstance(v29);
        (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_2 + 40LL))(
          InstanceEv_2,
          s_5,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
      v16 += 8;
    }
    while ( v51 != v16 );
  }
  return 1;
}