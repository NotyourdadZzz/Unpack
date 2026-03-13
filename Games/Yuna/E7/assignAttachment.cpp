__int64 __fastcall spine::v3::SkeletonDataLoader::assignVertexAttachment(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::Attachment *lpsrc,
        spine::String *a3)
{
  _QWORD *v5; // x0
  _QWORD *v6; // x21
  spine::SpineExtension *v7; // x0
  __int64 v8; // x8
  unsigned __int64 v9; // x24
  unsigned __int64 v10; // x8
  __int64 v11; // x25
  __int64 v12; // x26
  __int64 v13; // x22
  int n8; // w27
  __int64 Instance; // x0
  __int64 v16; // x0
  __int64 v17; // x8
  spine::SpineExtension *v18; // x0
  __int64 v19; // x9
  __int64 v20; // x8
  __int64 v21; // x9
  __int64 v22; // x9
  __int64 v23; // x8
  char *v24; // x9
  char *v25; // x20
  __int64 InstanceEv; // x0
  void (__fastcall **s1)(spine::String *__hidden); // [xsp+8h] [xbp-28h] BYREF
  spine::SpineExtension *v29; // [xsp+10h] [xbp-20h]
  char *v30; // [xsp+18h] [xbp-18h]
  char v31; // [xsp+20h] [xbp-10h]
  __int64 v32; // [xsp+28h] [xbp-8h]

  v32 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  if ( !lpsrc )
    return 1;
  v5 = __dynamic_cast(
         lpsrc,
         (const struct __class_type_info *)&`typeinfo for'spine::v3::Attachment,
         (const struct __class_type_info *)&`typeinfo for'spine::v3::VertexAttachment,
         0);
  if ( !v5 )
    return 1;
  v6 = v5;
  v7 = (spine::SpineExtension *)sp_bin_stream::pop_vector<unsigned short,unsigned long>((char *)this + 88, v5 + 6);
  v8 = *((_QWORD *)this + 14);
  v9 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v8);
  *((_QWORD *)this + 14) = v8 + 2;
  v10 = v6[12];
  v6[11] = 0;
  v11 = *((_QWORD *)this + 11);
  v12 = *((_QWORD *)this + 14);
  if ( v10 >= v9 )
  {
    v16 = v6[13];
    v17 = 0;
  }
  else
  {
    v13 = v6[13];
    if ( (unsigned int)(int)(float)((float)(unsigned int)v9 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v9 * 1.75);
    v6[12] = n8;
    Instance = spine::SpineExtension::getInstance(v7);
    v16 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v13,
            4LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            126);
    v17 = v6[11];
    v6[13] = v16;
  }
  v18 = (spine::SpineExtension *)memcpy((void *)(v16 + 4 * v17), (const void *)(v11 + v12), 4 * v9);
  v6[11] = v9;
  v19 = *((_QWORD *)this + 11);
  v20 = *((_QWORD *)this + 14) + 4 * v9;
  *((_QWORD *)this + 14) = v20;
  v21 = *(unsigned int *)(v19 + v20);
  *((_QWORD *)this + 14) = v20 + 4;
  v6[14] = v21;
  v22 = *((_QWORD *)this + 14);
  v29 = 0;
  v30 = 0;
  v31 = 0;
  s1 = s1;
  v23 = *(unsigned int *)(*((_QWORD *)this + 11) + v22);
  *((_QWORD *)this + 14) = v22 + 4;
  if ( (_DWORD)v23 == -1
    || ((*((_BYTE *)this + 120) & 1) != 0 ? (v24 = (char *)*((_QWORD *)this + 17)) : (v24 = (char *)this + 121), !v24) )
  {
    v25 = 0;
    if ( !a3 )
      goto LABEL_18;
    goto LABEL_17;
  }
  v25 = &v24[v23];
  v18 = (spine::SpineExtension *)strlen(&v24[v23]);
  v29 = v18;
  v30 = v25;
  v31 = 1;
  if ( a3 )
  {
LABEL_17:
    v18 = (spine::SpineExtension *)spine::String::operator=(a3, &s1);
    v25 = v30;
  }
LABEL_18:
  s1 = s1;
  if ( v25 && (v31 & 1) == 0 )
  {
    InstanceEv = spine::SpineExtension::getInstance(v18);
    (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv + 40LL))(
      InstanceEv,
      v25,
      "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../../.."
      "/../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
      252);
  }
  spine::SpineObject::~SpineObject((spine::SpineObject *)&s1);
  return 1;
}