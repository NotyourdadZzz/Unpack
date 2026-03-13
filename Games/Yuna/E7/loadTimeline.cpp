__int64 __fastcall spine::v3::SkeletonDataLoader::loadTimeline(
        spine::v3::SkeletonDataLoader *this,
        __int64 a2,
        _QWORD *a3)
{
  __int64 v5; // x8
  unsigned __int64 v6; // x9
  unsigned __int64 v7; // x8
  unsigned __int64 v8; // x19
  bool v9; // cf
  unsigned __int64 v10; // x8
  __int64 v11; // x22
  int n8; // w20
  __int64 Instance; // x0
  __int64 v14; // x0
  __int64 v15; // x22
  __int64 v16; // x24
  int n8_16; // w27
  __int64 InstanceEv_14; // x0
  __int64 v19; // x0
  __int64 v20; // x8
  __int64 v21; // x9
  int v22; // w8
  __int64 v23; // x26
  spine::SpineExtension *v24; // x0
  spine::SpineExtension *v25; // x0
  spine::v3::AttachmentTimeline *v26; // x26
  spine::SpineExtension *v27; // x0
  __int64 v28; // x9
  __int64 v29; // x8
  __int64 v30; // x8
  unsigned __int64 v31; // x19
  unsigned __int64 v32; // x8
  __int64 v33; // x23
  __int64 v34; // x25
  __int64 v35; // x24
  int n8_1; // w27
  __int64 InstanceEv; // x0
  __int64 v38; // x0
  __int64 v39; // x8
  spine::v3::EventTimeline *v40; // x26
  spine::SpineExtension *v41; // x0
  __int64 v42; // x8
  unsigned __int64 v43; // x19
  unsigned __int64 v44; // x8
  __int64 v45; // x23
  __int64 v46; // x25
  __int64 v47; // x24
  int n8_10; // w27
  __int64 InstanceEv_8; // x0
  __int64 v50; // x0
  __int64 v51; // x8
  __int64 v52; // x9
  int v53; // w8
  __int64 v54; // x8
  unsigned __int64 v55; // x19
  unsigned __int64 v56; // x8
  __int64 v57; // x23
  __int64 v58; // x25
  __int64 v59; // x24
  int n8_2; // w27
  __int64 InstanceEv_2; // x0
  __int64 v62; // x0
  __int64 v63; // x8
  __int64 v64; // x26
  spine::SpineExtension *v65; // x0
  __int64 v66; // x9
  int v67; // w8
  __int64 v68; // x8
  unsigned __int64 v69; // x19
  unsigned __int64 v70; // x8
  __int64 v71; // x23
  __int64 v72; // x25
  __int64 v73; // x24
  int n8_3; // w27
  __int64 InstanceEv_3; // x0
  __int64 v76; // x0
  __int64 v77; // x8
  __int64 v78; // x9
  int v79; // w8
  __int64 v80; // x8
  unsigned __int64 v81; // x19
  unsigned __int64 v82; // x8
  __int64 v83; // x23
  __int64 v84; // x25
  __int64 v85; // x24
  int n8_15; // w27
  __int64 InstanceEv_13; // x0
  __int64 v88; // x0
  __int64 v89; // x8
  __int64 v90; // x24
  spine::SpineExtension *v91; // x0
  __int64 v92; // x9
  __int64 v93; // x8
  unsigned __int64 v94; // x19
  unsigned __int64 v95; // x8
  __int64 v96; // x23
  __int64 v97; // x25
  spine::v3::DrawOrderTimeline *v98; // x26
  spine::SpineExtension *v99; // x0
  __int64 v100; // x8
  unsigned __int64 v101; // x19
  unsigned __int64 v102; // x8
  __int64 v103; // x23
  __int64 v104; // x25
  __int64 v105; // x24
  int n8_12; // w27
  __int64 InstanceEv_10; // x0
  __int64 v108; // x0
  __int64 v109; // x8
  unsigned __int64 v110; // x8
  unsigned __int64 v111; // x19
  __int64 v112; // x23
  void (__fastcall ***v113)(_QWORD); // x0
  __int64 v114; // x9
  __int64 v115; // x19
  __int64 v116; // x9
  __int64 v117; // x8
  char *v118; // x9
  char *n8_19; // x24
  spine::SpineExtension *v120; // x0
  const char *n8_20; // x24
  __int64 InstanceEv_1; // x0
  spine::SpineExtension *v123; // x0
  __int64 v124; // x9
  __int64 v125; // x8
  unsigned __int64 v126; // x23
  unsigned __int64 v127; // x8
  unsigned __int64 v128; // x19
  unsigned __int64 v129; // x8
  __int64 v130; // x24
  int n8_11; // w25
  __int64 InstanceEv_9; // x0
  __int64 v133; // x0
  __int64 v134; // x19
  __int64 v135; // x9
  __int64 v136; // x8
  char *v137; // x9
  const char *n8_17; // x27
  size_t n0x17; // x0
  size_t n; // x28
  char *dest; // x24
  __int64 n26; // x25
  const spine::v3::EventData *v143; // x27
  float v144; // s8
  spine::v3::Event *v145; // x24
  spine::SpineExtension *v146; // x0
  const char *n8_18; // x24
  __int64 InstanceEv_15; // x0
  spine::SpineExtension *v149; // x0
  __int64 v150; // x9
  __int64 v151; // x8
  unsigned __int64 v152; // x19
  unsigned __int64 v153; // x8
  __int64 v154; // x23
  __int64 v155; // x25
  __int64 v156; // x24
  int n8_4; // w27
  __int64 InstanceEv_4; // x0
  __int64 v159; // x0
  __int64 v160; // x8
  spine::SpineExtension *Attachment; // x0
  unsigned __int64 v162; // x8
  unsigned __int64 v163; // x19
  __int64 v164; // x23
  __int64 (__fastcall ***v165)(_QWORD); // x0
  __int64 v166; // x8
  __int64 v167; // x19
  unsigned __int64 v168; // x8
  unsigned __int64 v169; // x23
  __int64 v170; // x24
  __int64 (__fastcall ***v171)(_QWORD); // x0
  __int64 v172; // x9
  __int64 v173; // x8
  char *v174; // x9
  char *n8_8; // x24
  unsigned __int64 v176; // x19
  __int64 v177; // x25
  __int64 v178; // x8
  size_t Attachment_5; // x23
  __int64 v180; // x27
  int n8_5; // w8
  __int64 n8_6; // x24
  __int64 InstanceEv_5; // x0
  __int64 v184; // x0
  size_t Attachment_4; // x8
  __int64 v186; // x8
  spine::SpineExtension *v187; // x0
  __int64 v188; // x24
  __int64 InstanceEv_6; // x0
  spine::SpineExtension *v190; // x0
  __int64 v191; // x9
  __int64 v192; // x8
  __int64 v193; // x19
  unsigned __int64 v194; // x8
  unsigned __int64 v195; // x23
  __int64 v196; // x24
  __int64 (__fastcall ***v197)(_QWORD); // x0
  __int64 v198; // x25
  __int64 v199; // x8
  size_t Attachment_3; // x23
  __int64 v201; // x27
  int n8_13; // w8
  __int64 n8_14; // x24
  __int64 InstanceEv_11; // x0
  __int64 v205; // x0
  size_t Attachment_2; // x8
  __int64 v207; // x8
  spine::SpineExtension *v208; // x0
  __int64 v209; // x24
  __int64 InstanceEv_12; // x0
  __int64 v211; // x8
  __int64 v212; // x10
  __int64 v213; // x8
  const char *n8_9; // x24
  __int64 InstanceEv_7; // x0
  _QWORD *v218; // [xsp+18h] [xbp-98h]
  unsigned __int64 v219; // [xsp+20h] [xbp-90h]
  _QWORD v220[2]; // [xsp+48h] [xbp-68h] BYREF
  char *dest_1; // [xsp+58h] [xbp-58h]
  char v222; // [xsp+67h] [xbp-49h] BYREF
  _QWORD *v223; // [xsp+68h] [xbp-48h] BYREF
  __int64 (__fastcall **p_s1)(); // [xsp+70h] [xbp-40h] BYREF
  size_t Attachment_1; // [xsp+78h] [xbp-38h]
  const char *n8_7; // [xsp+80h] [xbp-30h]
  __int64 v227; // [xsp+88h] [xbp-28h]
  __int64 v228; // [xsp+90h] [xbp-20h]

  v228 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v5 = *((_QWORD *)this + 14);
  v6 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v5);
  *((_QWORD *)this + 14) = v5 + 2;
  v8 = a3[1];
  v7 = a3[2];
  a3[1] = v6;
  v219 = v6;
  v9 = v7 >= v6;
  v10 = v6;
  if ( !v9 )
  {
    v11 = a3[3];
    if ( (unsigned int)(int)(float)((float)(unsigned int)v6 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v6 * 1.75);
    a3[2] = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v14 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v11,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    v10 = a3[1];
    a3[3] = v14;
  }
  while ( v8 < v10 )
  {
    *(_QWORD *)(a3[3] + 8 * v8++) = 0;
    v10 = a3[1];
  }
  v218 = a3;
  if ( !(_DWORD)v219 )
    return 1;
  v15 = 0;
  while ( 2 )
  {
    v21 = *((_QWORD *)this + 14);
    v22 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v21);
    *((_QWORD *)this + 14) = v21 + 2;
    switch ( v22 )
    {
      case 0:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                649);
        v24 = (spine::SpineExtension *)spine::v3::RotateTimeline::RotateTimeline((spine::v3::RotateTimeline *)v23, 1);
        goto LABEL_36;
      case 1:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                659);
        v25 = (spine::SpineExtension *)spine::v3::TranslateTimeline::TranslateTimeline(
                                         (spine::v3::TranslateTimeline *)v23,
                                         1);
        goto LABEL_48;
      case 2:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                669);
        v25 = (spine::SpineExtension *)spine::v3::ScaleTimeline::ScaleTimeline((spine::v3::ScaleTimeline *)v23, 1);
        goto LABEL_48;
      case 3:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                678);
        v25 = (spine::SpineExtension *)spine::v3::ShearTimeline::ShearTimeline((spine::v3::ShearTimeline *)v23, 1);
        goto LABEL_48;
      case 4:
        v26 = (spine::v3::AttachmentTimeline *)spine::SpineObject::operator new(
                                                 80,
                                                 "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna"
                                                 "/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                                                 687);
        v27 = (spine::SpineExtension *)spine::v3::AttachmentTimeline::AttachmentTimeline(v26, 1);
        *(_QWORD *)(v218[3] + 8 * v15) = v26;
        v28 = *((_QWORD *)this + 14);
        v29 = *(__int16 *)(*((_QWORD *)this + 11) + v28);
        *((_QWORD *)this + 14) = v28 + 2;
        *((_QWORD *)v26 + 1) = v29;
        v30 = *((_QWORD *)this + 14);
        v31 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v30);
        *((_QWORD *)this + 14) = v30 + 2;
        v32 = *((_QWORD *)v26 + 4);
        *((_QWORD *)v26 + 3) = 0;
        v33 = *((_QWORD *)this + 11);
        v34 = *((_QWORD *)this + 14);
        if ( v32 >= v31 )
        {
          v38 = *((_QWORD *)v26 + 5);
          v39 = 0;
        }
        else
        {
          v35 = *((_QWORD *)v26 + 5);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v31 * 1.75) <= 8 )
            n8_1 = 8;
          else
            n8_1 = (int)(float)((float)(unsigned int)v31 * 1.75);
          *((_QWORD *)v26 + 4) = n8_1;
          InstanceEv = spine::SpineExtension::getInstance(v27);
          v38 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv
                                                                                            + 32LL))(
                  InstanceEv,
                  v35,
                  4LL * n8_1,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  126);
          v39 = *((_QWORD *)v26 + 3);
          *((_QWORD *)v26 + 5) = v38;
        }
        memcpy((void *)(v38 + 4 * v39), (const void *)(v33 + v34), 4 * v31);
        *((_QWORD *)v26 + 3) = v31;
        *((_QWORD *)this + 14) += 4 * v31;
        v110 = *((_QWORD *)v26 + 7);
        if ( v110 )
        {
          v111 = 0;
          v112 = -32;
          do
          {
            v113 = (void (__fastcall ***)(_QWORD))(*((_QWORD *)v26 + 9) + 32 * v110 + v112);
            (**v113)(v113);
            v110 = *((_QWORD *)v26 + 7);
            ++v111;
            v112 -= 32;
          }
          while ( v111 < v110 );
        }
        *((_QWORD *)v26 + 7) = 0;
        v114 = *((_QWORD *)this + 14);
        v115 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v114);
        for ( *((_QWORD *)this + 14) = v114 + 2; v115; --v115 )
        {
          v116 = *((_QWORD *)this + 14);
          Attachment_1 = 0;
          n8_7 = 0;
          LOBYTE(v227) = 0;
          p_s1 = (__int64 (__fastcall **)())s1;
          v117 = *(unsigned int *)(*((_QWORD *)this + 11) + v116);
          *((_QWORD *)this + 14) = v116 + 4;
          if ( (_DWORD)v117 != -1 )
          {
            v118 = (char *)this + 121;
            if ( (*((_BYTE *)this + 120) & 1) != 0 )
              v118 = (char *)*((_QWORD *)this + 17);
            if ( v118 )
            {
              n8_19 = &v118[v117];
              Attachment_1 = strlen(&v118[v117]);
              n8_7 = n8_19;
              LOBYTE(v227) = 1;
            }
          }
          v120 = (spine::SpineExtension *)spine::Vector<spine::String>::add((char *)v26 + 48, &p_s1);
          n8_20 = n8_7;
          p_s1 = (__int64 (__fastcall **)())s1;
          if ( n8_7 && (v227 & 1) == 0 )
          {
            InstanceEv_1 = spine::SpineExtension::getInstance(v120);
            (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 40LL))(
              InstanceEv_1,
              n8_20,
              "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../"
              "../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
              252);
          }
          spine::SpineObject::~SpineObject((spine::SpineObject *)&p_s1);
        }
        goto LABEL_15;
      case 5:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                703);
        v24 = (spine::SpineExtension *)spine::v3::ColorTimeline::ColorTimeline((spine::v3::ColorTimeline *)v23, 1);
LABEL_36:
        *(_QWORD *)(v218[3] + 8 * v15) = v23;
        v52 = *((_QWORD *)this + 14);
        v53 = *(__int16 *)(*((_QWORD *)this + 11) + v52);
        *((_QWORD *)this + 14) = v52 + 2;
        *(_DWORD *)(v23 + 40) = v53;
        v54 = *((_QWORD *)this + 14);
        v55 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v54);
        *((_QWORD *)this + 14) = v54 + 2;
        v56 = *(_QWORD *)(v23 + 64);
        *(_QWORD *)(v23 + 56) = 0;
        v57 = *((_QWORD *)this + 11);
        v58 = *((_QWORD *)this + 14);
        if ( v56 >= v55 )
        {
          v62 = *(_QWORD *)(v23 + 72);
          v63 = 0;
        }
        else
        {
          v59 = *(_QWORD *)(v23 + 72);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v55 * 1.75) <= 8 )
            n8_2 = 8;
          else
            n8_2 = (int)(float)((float)(unsigned int)v55 * 1.75);
          *(_QWORD *)(v23 + 64) = n8_2;
          InstanceEv_2 = spine::SpineExtension::getInstance(v24);
          v62 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_2
                                                                                            + 32LL))(
                  InstanceEv_2,
                  v59,
                  4LL * n8_2,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  126);
          v63 = *(_QWORD *)(v23 + 56);
          *(_QWORD *)(v23 + 72) = v62;
        }
        v90 = 4 * v55;
        v91 = (spine::SpineExtension *)memcpy((void *)(v62 + 4 * v63), (const void *)(v57 + v58), 4 * v55);
        *(_QWORD *)(v23 + 56) = v55;
        goto LABEL_55;
      case 6:
        v64 = spine::SpineObject::operator new(
                120,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                713);
        v65 = (spine::SpineExtension *)spine::v3::DeformTimeline::DeformTimeline((spine::v3::DeformTimeline *)v64, 1);
        *(_QWORD *)(v218[3] + 8 * v15) = v64;
        v66 = *((_QWORD *)this + 14);
        v67 = *(__int16 *)(*((_QWORD *)this + 11) + v66);
        *((_QWORD *)this + 14) = v66 + 2;
        *(_DWORD *)(v64 + 40) = v67;
        v68 = *((_QWORD *)this + 14);
        v69 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v68);
        *((_QWORD *)this + 14) = v68 + 2;
        v70 = *(_QWORD *)(v64 + 64);
        *(_QWORD *)(v64 + 56) = 0;
        v71 = *((_QWORD *)this + 11);
        v72 = *((_QWORD *)this + 14);
        if ( v70 >= v69 )
        {
          v76 = *(_QWORD *)(v64 + 72);
          v77 = 0;
        }
        else
        {
          v73 = *(_QWORD *)(v64 + 72);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v69 * 1.75) <= 8 )
            n8_3 = 8;
          else
            n8_3 = (int)(float)((float)(unsigned int)v69 * 1.75);
          *(_QWORD *)(v64 + 64) = n8_3;
          InstanceEv_3 = spine::SpineExtension::getInstance(v65);
          v76 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_3
                                                                                            + 32LL))(
                  InstanceEv_3,
                  v73,
                  4LL * n8_3,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  126);
          v77 = *(_QWORD *)(v64 + 56);
          *(_QWORD *)(v64 + 72) = v76;
        }
        v149 = (spine::SpineExtension *)memcpy((void *)(v76 + 4 * v77), (const void *)(v71 + v72), 4 * v69);
        *(_QWORD *)(v64 + 56) = v69;
        v150 = *((_QWORD *)this + 11);
        v151 = *((_QWORD *)this + 14) + 4 * v69;
        *((_QWORD *)this + 14) = v151;
        v152 = *(unsigned __int16 *)(v150 + v151);
        *((_QWORD *)this + 14) = v151 + 2;
        v153 = *(_QWORD *)(v64 + 24);
        *(_QWORD *)(v64 + 16) = 0;
        v154 = *((_QWORD *)this + 11);
        v155 = *((_QWORD *)this + 14);
        if ( v153 >= v152 )
        {
          v159 = *(_QWORD *)(v64 + 32);
          v160 = 0;
        }
        else
        {
          v156 = *(_QWORD *)(v64 + 32);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v152 * 1.75) <= 8 )
            n8_4 = 8;
          else
            n8_4 = (int)(float)((float)(unsigned int)v152 * 1.75);
          *(_QWORD *)(v64 + 24) = n8_4;
          InstanceEv_4 = spine::SpineExtension::getInstance(v149);
          v159 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_4
                                                                                             + 32LL))(
                   InstanceEv_4,
                   v156,
                   4LL * n8_4,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v160 = *(_QWORD *)(v64 + 16);
          *(_QWORD *)(v64 + 32) = v159;
        }
        Attachment = (spine::SpineExtension *)memcpy((void *)(v159 + 4 * v160), (const void *)(v154 + v155), 4 * v152);
        *(_QWORD *)(v64 + 16) = v152;
        *((_QWORD *)this + 14) += 4 * v152;
        v162 = *(_QWORD *)(v64 + 88);
        if ( v162 )
        {
          v163 = 0;
          v164 = -32;
          do
          {
            v165 = (__int64 (__fastcall ***)(_QWORD))(*(_QWORD *)(v64 + 104) + 32 * v162 + v164);
            Attachment = (spine::SpineExtension *)(**v165)(v165);
            v162 = *(_QWORD *)(v64 + 88);
            ++v163;
            v164 -= 32;
          }
          while ( v163 < v162 );
        }
        *(_QWORD *)(v64 + 88) = 0;
        v166 = *((_QWORD *)this + 14);
        v167 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v166);
        *((_QWORD *)this + 14) = v166 + 2;
        v168 = *(_QWORD *)(v64 + 88);
        if ( v168 )
        {
          v169 = 0;
          v170 = -32;
          do
          {
            v171 = (__int64 (__fastcall ***)(_QWORD))(*(_QWORD *)(v64 + 104) + 32 * v168 + v170);
            Attachment = (spine::SpineExtension *)(**v171)(v171);
            v168 = *(_QWORD *)(v64 + 88);
            ++v169;
            v170 -= 32;
          }
          while ( v169 < v168 );
        }
        *(_QWORD *)(v64 + 88) = 0;
        if ( (_DWORD)v167 )
        {
          do
          {
            v177 = *((_QWORD *)this + 11);
            n8_7 = 0;
            v227 = 0;
            Attachment_1 = 0;
            p_s1 = s1_0;
            v178 = *((_QWORD *)this + 14);
            Attachment_5 = *(unsigned __int16 *)(v177 + v178);
            v180 = v178 + 2;
            Attachment_1 = 0;
            *((_QWORD *)this + 14) = v178 + 2;
            if ( Attachment_5 )
            {
              n8_5 = (int)(float)((float)(unsigned int)Attachment_5 * 1.75);
              if ( (unsigned int)n8_5 <= 8 )
                n8_5 = 8;
              n8_6 = n8_5;
              n8_7 = (const char *)n8_5;
              InstanceEv_5 = spine::SpineExtension::getInstance(Attachment);
              v184 = (*(__int64 (__fastcall **)(__int64, _QWORD, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_5
                                                                                                + 32LL))(
                       InstanceEv_5,
                       0,
                       4 * n8_6,
                       "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/mai"
                       "n/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                       126);
              Attachment_4 = Attachment_1;
              v227 = v184;
            }
            else
            {
              Attachment_4 = 0;
              v184 = 0;
            }
            memcpy((void *)(v184 + 4 * Attachment_4), (const void *)(v177 + v180), 4 * Attachment_5);
            v186 = *((_QWORD *)this + 14);
            Attachment_1 = Attachment_5;
            *((_QWORD *)this + 14) = v186 + 4 * Attachment_5;
            v187 = (spine::SpineExtension *)spine::Vector<spine::Vector<float>>::add(v64 + 80, &p_s1);
            v188 = v227;
            p_s1 = s1_0;
            Attachment_1 = 0;
            if ( v227 )
            {
              InstanceEv_6 = spine::SpineExtension::getInstance(v187);
              (*(void (__fastcall **)(__int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_6 + 40LL))(
                InstanceEv_6,
                v188,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/."
                "./../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                226);
            }
            spine::SpineObject::~SpineObject((spine::SpineObject *)&p_s1);
            --v167;
          }
          while ( v167 );
        }
        v172 = *((_QWORD *)this + 14);
        Attachment_1 = 0;
        n8_7 = 0;
        LOBYTE(v227) = 0;
        p_s1 = (__int64 (__fastcall **)())s1;
        v173 = *(unsigned int *)(*((_QWORD *)this + 11) + v172);
        *((_QWORD *)this + 14) = v172 + 4;
        if ( (_DWORD)v173 != -1 )
        {
          v174 = (char *)this + 121;
          if ( (*((_BYTE *)this + 120) & 1) != 0 )
            v174 = (char *)*((_QWORD *)this + 17);
          if ( v174 )
          {
            n8_8 = &v174[v173];
            Attachment = (spine::SpineExtension *)strlen(&v174[v173]);
            Attachment_1 = (size_t)Attachment;
            n8_7 = n8_8;
            LOBYTE(v227) = 1;
          }
        }
        if ( *((_DWORD *)this + 3) > 0x7530u )
        {
          v211 = *((_QWORD *)this + 14);
          v212 = v211 + 2;
          v213 = *(__int16 *)(*((_QWORD *)this + 11) + v211);
          *((_QWORD *)this + 14) = v212;
          Attachment = (spine::SpineExtension *)spine::v3::Skin::getAttachment(
                                                  *(spine::v3::Skin **)(*(_QWORD *)(a2 + 128) + 8 * v213),
                                                  *(int *)(v64 + 40),
                                                  (const spine::String *)&p_s1);
          *(_QWORD *)(v64 + 112) = Attachment;
        }
        else if ( *(_QWORD *)(a2 + 112) )
        {
          v176 = 0;
          do
          {
            Attachment = (spine::SpineExtension *)spine::v3::Skin::getAttachment(
                                                    *(spine::v3::Skin **)(*(_QWORD *)(a2 + 128) + 8 * v176),
                                                    *(int *)(v64 + 40),
                                                    (const spine::String *)&p_s1);
            *(_QWORD *)(v64 + 112) = Attachment;
            if ( Attachment )
              break;
            ++v176;
          }
          while ( *(_QWORD *)(a2 + 112) > v176 );
        }
        n8_9 = n8_7;
        p_s1 = (__int64 (__fastcall **)())s1;
        if ( n8_7 && (v227 & 1) == 0 )
        {
          InstanceEv_7 = spine::SpineExtension::getInstance(Attachment);
          (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_7 + 40LL))(
            InstanceEv_7,
            n8_9,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
            252);
        }
        spine::SpineObject::~SpineObject((spine::SpineObject *)&p_s1);
        goto LABEL_15;
      case 7:
        v40 = (spine::v3::EventTimeline *)spine::SpineObject::operator new(
                                            72,
                                            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna"
                                            "2d/spinex/v3/SCSLoader_v3.cpp",
                                            750);
        v41 = (spine::SpineExtension *)spine::v3::EventTimeline::EventTimeline(v40, 1);
        *(_QWORD *)(v218[3] + 8 * v15) = v40;
        v42 = *((_QWORD *)this + 14);
        v43 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v42);
        *((_QWORD *)this + 14) = v42 + 2;
        v44 = *((_QWORD *)v40 + 3);
        *((_QWORD *)v40 + 2) = 0;
        v45 = *((_QWORD *)this + 11);
        v46 = *((_QWORD *)this + 14);
        if ( v44 >= v43 )
        {
          v50 = *((_QWORD *)v40 + 4);
          v51 = 0;
        }
        else
        {
          v47 = *((_QWORD *)v40 + 4);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v43 * 1.75) <= 8 )
            n8_10 = 8;
          else
            n8_10 = (int)(float)((float)(unsigned int)v43 * 1.75);
          *((_QWORD *)v40 + 3) = n8_10;
          InstanceEv_8 = spine::SpineExtension::getInstance(v41);
          v50 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_8
                                                                                            + 32LL))(
                  InstanceEv_8,
                  v47,
                  4LL * n8_10,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  126);
          v51 = *((_QWORD *)v40 + 2);
          *((_QWORD *)v40 + 4) = v50;
        }
        v123 = (spine::SpineExtension *)memcpy((void *)(v50 + 4 * v51), (const void *)(v45 + v46), 4 * v43);
        *((_QWORD *)v40 + 2) = v43;
        v124 = *((_QWORD *)this + 11);
        v125 = *((_QWORD *)this + 14) + 4 * v43;
        *((_QWORD *)this + 14) = v125;
        v126 = *(unsigned __int16 *)(v124 + v125);
        *((_QWORD *)this + 14) = v125 + 2;
        v128 = *((_QWORD *)v40 + 6);
        v127 = *((_QWORD *)v40 + 7);
        *((_QWORD *)v40 + 6) = v126;
        v9 = v127 >= v126;
        v129 = v126;
        if ( !v9 )
        {
          v130 = *((_QWORD *)v40 + 8);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v126 * 1.75) <= 8 )
            n8_11 = 8;
          else
            n8_11 = (int)(float)((float)(unsigned int)v126 * 1.75);
          *((_QWORD *)v40 + 7) = n8_11;
          InstanceEv_9 = spine::SpineExtension::getInstance(v123);
          v133 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_9
                                                                                             + 32LL))(
                   InstanceEv_9,
                   v130,
                   8LL * n8_11,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   85);
          v129 = *((_QWORD *)v40 + 6);
          *((_QWORD *)v40 + 8) = v133;
        }
        while ( v128 < v129 )
        {
          *(_QWORD *)(*((_QWORD *)v40 + 8) + 8 * v128++) = 0;
          v129 = *((_QWORD *)v40 + 6);
        }
        if ( !(_DWORD)v126 )
          goto LABEL_15;
        v134 = 0;
        break;
      case 8:
        v98 = (spine::v3::DrawOrderTimeline *)spine::SpineObject::operator new(
                                                72,
                                                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/"
                                                "yuna2d/spinex/v3/SCSLoader_v3.cpp",
                                                769);
        v99 = (spine::SpineExtension *)spine::v3::DrawOrderTimeline::DrawOrderTimeline(v98, 1);
        *(_QWORD *)(v218[3] + 8 * v15) = v98;
        v100 = *((_QWORD *)this + 14);
        v101 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v100);
        *((_QWORD *)this + 14) = v100 + 2;
        v102 = *((_QWORD *)v98 + 3);
        *((_QWORD *)v98 + 2) = 0;
        v103 = *((_QWORD *)this + 11);
        v104 = *((_QWORD *)this + 14);
        if ( v102 >= v101 )
        {
          v108 = *((_QWORD *)v98 + 4);
          v109 = 0;
        }
        else
        {
          v105 = *((_QWORD *)v98 + 4);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v101 * 1.75) <= 8 )
            n8_12 = 8;
          else
            n8_12 = (int)(float)((float)(unsigned int)v101 * 1.75);
          *((_QWORD *)v98 + 3) = n8_12;
          InstanceEv_10 = spine::SpineExtension::getInstance(v99);
          v108 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_10
                                                                                             + 32LL))(
                   InstanceEv_10,
                   v105,
                   4LL * n8_12,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v109 = *((_QWORD *)v98 + 2);
          *((_QWORD *)v98 + 4) = v108;
        }
        v190 = (spine::SpineExtension *)memcpy((void *)(v108 + 4 * v109), (const void *)(v103 + v104), 4 * v101);
        *((_QWORD *)v98 + 2) = v101;
        v191 = *((_QWORD *)this + 11);
        v192 = *((_QWORD *)this + 14) + 4 * v101;
        *((_QWORD *)this + 14) = v192;
        v193 = *(unsigned __int16 *)(v191 + v192);
        *((_QWORD *)this + 14) = v192 + 2;
        v194 = *((_QWORD *)v98 + 6);
        if ( v194 )
        {
          v195 = 0;
          v196 = -32;
          do
          {
            v197 = (__int64 (__fastcall ***)(_QWORD))(*((_QWORD *)v98 + 8) + 32 * v194 + v196);
            v190 = (spine::SpineExtension *)(**v197)(v197);
            v194 = *((_QWORD *)v98 + 6);
            ++v195;
            v196 -= 32;
          }
          while ( v195 < v194 );
        }
        *((_QWORD *)v98 + 6) = 0;
        if ( (_DWORD)v193 )
        {
          do
          {
            v198 = *((_QWORD *)this + 11);
            n8_7 = 0;
            v227 = 0;
            Attachment_1 = 0;
            p_s1 = s1_1;
            v199 = *((_QWORD *)this + 14);

            Attachment_3 = *(unsigned __int16 *)(v198 + v199);
            v201 = v199 + 2;
            Attachment_1 = 0;
            *((_QWORD *)this + 14) = v199 + 2;
            if ( Attachment_3 )
            {
              n8_13 = (int)(float)((float)(unsigned int)Attachment_3 * 1.75);
              if ( (unsigned int)n8_13 <= 8 )
                n8_13 = 8;
              n8_14 = n8_13;
              n8_7 = (const char *)n8_13;
              InstanceEv_11 = spine::SpineExtension::getInstance(v190);
              v205 = (*(__int64 (__fastcall **)(__int64, _QWORD, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_11
                                                                                                + 32LL))(
                       InstanceEv_11,
                       0,
                       4 * n8_14,
                       "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/mai"
                       "n/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                       126);
              Attachment_2 = Attachment_1;
              v227 = v205;
            }
            else
            {
              Attachment_2 = 0;
              v205 = 0;
            }
            memcpy((void *)(v205 + 4 * Attachment_2), (const void *)(v198 + v201), 4 * Attachment_3);
            v207 = *((_QWORD *)this + 14);
            Attachment_1 = Attachment_3;
            *((_QWORD *)this + 14) = v207 + 4 * Attachment_3;
            v208 = (spine::SpineExtension *)spine::Vector<spine::Vector<int>>::add((char *)v98 + 40, &p_s1);
            v209 = v227;
            p_s1 = s1_1;
            Attachment_1 = 0;
            if ( v227 )
            {
              InstanceEv_12 = spine::SpineExtension::getInstance(v208);
              (*(void (__fastcall **)(__int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_12 + 40LL))(
                InstanceEv_12,
                v209,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/."
                "./../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                226);
            }
            spine::SpineObject::~SpineObject((spine::SpineObject *)&p_s1);
            --v193;
          }
          while ( v193 );
        }
        goto LABEL_15;
      case 9:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                785);
        v25 = (spine::SpineExtension *)spine::v3::IkConstraintTimeline::IkConstraintTimeline(
                                         (spine::v3::IkConstraintTimeline *)v23,
                                         1);
        goto LABEL_48;
      case 10:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                794);
        v25 = (spine::SpineExtension *)spine::v3::TransformConstraintTimeline::TransformConstraintTimeline(
                                         (spine::v3::TransformConstraintTimeline *)v23,
                                         1);
        goto LABEL_48;
      case 11:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                803);
        v25 = (spine::SpineExtension *)spine::v3::PathConstraintPositionTimeline::PathConstraintPositionTimeline(
                                         (spine::v3::PathConstraintPositionTimeline *)v23,
                                         1);
        goto LABEL_48;
      case 12:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                812);
        v25 = (spine::SpineExtension *)spine::v3::PathConstraintSpacingTimeline::PathConstraintSpacingTimeline(
                                         (spine::v3::PathConstraintSpacingTimeline *)v23,
                                         1);
        goto LABEL_48;
      case 13:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                821);
        v25 = (spine::SpineExtension *)spine::v3::PathConstraintMixTimeline::PathConstraintMixTimeline(
                                         (spine::v3::PathConstraintMixTimeline *)v23,
                                         1);
        goto LABEL_48;
      case 14:
        v23 = spine::SpineObject::operator new(
                80,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex/v3/SCSLoader_v3.cpp",
                830);
        v25 = (spine::SpineExtension *)spine::v3::TwoColorTimeline::TwoColorTimeline(
                                         (spine::v3::TwoColorTimeline *)v23,
                                         1);
LABEL_48:
        *(_QWORD *)(v218[3] + 8 * v15) = v23;
        v78 = *((_QWORD *)this + 14);
        v79 = *(__int16 *)(*((_QWORD *)this + 11) + v78);
        *((_QWORD *)this + 14) = v78 + 2;
        *(_DWORD *)(v23 + 72) = v79;
        v80 = *((_QWORD *)this + 14);
        v81 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v80);
        *((_QWORD *)this + 14) = v80 + 2;
        v82 = *(_QWORD *)(v23 + 56);
        *(_QWORD *)(v23 + 48) = 0;
        v83 = *((_QWORD *)this + 11);
        v84 = *((_QWORD *)this + 14);
        if ( v82 >= v81 )
        {
          v88 = *(_QWORD *)(v23 + 64);
          v89 = 0;
        }
        else
        {
          v85 = *(_QWORD *)(v23 + 64);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v81 * 1.75) <= 8 )
            n8_15 = 8;
          else
            n8_15 = (int)(float)((float)(unsigned int)v81 * 1.75);
          *(_QWORD *)(v23 + 56) = n8_15;
          InstanceEv_13 = spine::SpineExtension::getInstance(v25);
          v88 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_13
                                                                                            + 32LL))(
                  InstanceEv_13,
                  v85,
                  4LL * n8_15,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  126);
          v89 = *(_QWORD *)(v23 + 48);
          *(_QWORD *)(v23 + 64) = v88;
        }
        v90 = 4 * v81;
        v91 = (spine::SpineExtension *)memcpy((void *)(v88 + 4 * v89), (const void *)(v83 + v84), 4 * v81);
        *(_QWORD *)(v23 + 48) = v81;
LABEL_55:
        v92 = *((_QWORD *)this + 11);
        v93 = *((_QWORD *)this + 14) + v90;
        *((_QWORD *)this + 14) = v93;
        v94 = *(unsigned __int16 *)(v92 + v93);
        *((_QWORD *)this + 14) = v93 + 2;
        v95 = *(_QWORD *)(v23 + 24);
        *(_QWORD *)(v23 + 16) = 0;
        v96 = *((_QWORD *)this + 11);
        v97 = *((_QWORD *)this + 14);
        if ( v95 < v94 )
        {
          v16 = *(_QWORD *)(v23 + 32);
          if ( (unsigned int)(int)(float)((float)(unsigned int)v94 * 1.75) <= 8 )
            n8_16 = 8;
          else
            n8_16 = (int)(float)((float)(unsigned int)v94 * 1.75);
          *(_QWORD *)(v23 + 24) = n8_16;
          InstanceEv_14 = spine::SpineExtension::getInstance(v91);
          v19 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_14
                                                                                            + 32LL))(
                  InstanceEv_14,
                  v16,
                  4LL * n8_16,
                  "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp"
                  "/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                  126);
          v20 = *(_QWORD *)(v23 + 16);
          *(_QWORD *)(v23 + 32) = v19;
        }
        else
        {
          v19 = *(_QWORD *)(v23 + 32);
          v20 = 0;
        }
        memcpy((void *)(v19 + 4 * v20), (const void *)(v96 + v97), 4 * v94);
        *(_QWORD *)(v23 + 16) = v94;
        *((_QWORD *)this + 14) += 4 * v94;
        goto LABEL_15;
      default:
        goto LABEL_15;
    }
    do
    {
      v135 = *((_QWORD *)this + 14);
      Attachment_1 = 0;
      n8_7 = 0;
      LOBYTE(v227) = 0;
      p_s1 = (__int64 (__fastcall **)())s1;
      v136 = *(unsigned int *)(*((_QWORD *)this + 11) + v135);
      *((_QWORD *)this + 14) = v135 + 4;
      if ( (_DWORD)v136 == -1 )
        goto LABEL_95;
      v137 = (char *)this + 121;
      if ( (*((_BYTE *)this + 120) & 1) != 0 )
        v137 = (char *)*((_QWORD *)this + 17);
      if ( !v137 )
      {
LABEL_95:
        n8_17 = 0;
      }
      else
      {
        n8_17 = &v137[v136];
        Attachment_1 = strlen(&v137[v136]);
        n8_7 = n8_17;
        LOBYTE(v227) = 1;
      }
      n0x17 = strlen(n8_17);
      if ( n0x17 >= 0xFFFFFFFFFFFFFFF8LL )
        sub_A0F02C();
      n = n0x17;
      if ( n0x17 >= 0x17 )
      {
        if ( (n0x17 | 7) == 0x17 )
          n26 = 26;
        else
          n26 = (n0x17 | 7) + 1;
        dest = (char *)operator new(n26);
        v220[1] = n;
        dest_1 = dest;
        v220[0] = n26 | 1;
LABEL_104:
        memmove(dest, n8_17, n);
        goto LABEL_105;
      }
      dest = (char *)v220 + 1;
      LOBYTE(v220[0]) = 2 * n0x17;
      if ( n0x17 )
        goto LABEL_104;
LABEL_105:
      dest[n] = 0;
      v223 = v220;
      v143 = *(const spine::v3::EventData **)(std::__hash_table<std::__hash_value_type<std::string,spine::v3::EventData *>,std::__unordered_map_hasher<std::string,std::__hash_value_type<std::string,spine::v3::EventData *>,std::hash<std::string>,std::equal_to<std::string>,true>,std::__unordered_map_equal<std::string,std::__hash_value_type<std::string,spine::v3::EventData *>,std::equal_to<std::string>,std::hash<std::string>,true>,std::allocator<std::__hash_value_type<std::string,spine::v3::EventData *>>>::__emplace_unique_key_args<std::string,std::piecewise_construct_t const&,std::tuple<std::string&&>,std::tuple<>>(
                                                (char *)this + 176,
                                                v220,
                                                &std::piecewise_construct,
                                                &v223,
                                                &v222)
                                            + 40);
      if ( (v220[0] & 1) != 0 )
        operator delete(dest_1, v220[0] & 0xFFFFFFFFFFFFFFFELL);
      v144 = *(float *)(*((_QWORD *)v40 + 4) + 4 * v134);
      v145 = (spine::v3::Event *)spine::SpineObject::operator new(
                                   72,
                                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spinex"
                                   "/v3/SCSLoader_v3.cpp",
                                   762);
      v146 = (spine::SpineExtension *)spine::v3::Event::Event(v145, v144, v143);
      *(_QWORD *)(*((_QWORD *)v40 + 8) + 8 * v134) = v145;
      n8_18 = n8_7;
      p_s1 = (__int64 (__fastcall **)())s1;
      if ( n8_7 && (v227 & 1) == 0 )
      {
        InstanceEv_15 = spine::SpineExtension::getInstance(v146);
        (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_15 + 40LL))(
          InstanceEv_15,
          n8_18,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&p_s1);
      ++v134;
    }
    while ( v126 != v134 );
LABEL_15:
    if ( ++v15 != v219 )
      continue;
    return 1;
  }
}