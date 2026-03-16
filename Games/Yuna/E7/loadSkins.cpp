spine::v3::Skin *__fastcall spine::v3::SkeletonDataLoader::loadSkins(
        spine::v3::SkeletonDataLoader *this,
        spine::v3::SkeletonData *a2,
        __int64 a3,
        int a4)
{
  spine::v3::SkeletonData *v4; // x26
  __int64 v6; // x8
  unsigned __int64 v7; // x9
  unsigned __int64 v8; // x8
  unsigned __int64 v9; // x20
  bool v10; // cf
  unsigned __int64 v11; // x8
  __int64 v12; // x21
  int n8; // w22
  __int64 Instance; // x0
  __int64 v15; // x0
  __int64 v16; // x9
  __int64 v17; // x8
  __int64 v18; // x8
  char *v19; // x9
  const char *s1_8; // x22
  _QWORD *v21; // x25
  spine::SpineExtension *v22; // x0
  __int64 v23; // x8
  __int64 v24; // x9
  __int64 v25; // x23
  __int64 v26; // x9
  __int64 v27; // x12
  __int64 v28; // x8
  __int64 v29; // x10
  __int64 v30; // x8
  unsigned __int64 v31; // x10
  __int64 v32; // x9
  __int64 v33; // x20
  __int64 v34; // x22
  int n8_1; // w10
  __int64 n8_2; // x21
  __int64 InstanceEv; // x0
  __int64 v38; // x8
  __int64 v39; // x23
  __int64 v40; // x9
  __int64 v41; // x9
  __int64 v42; // x8
  __int64 v43; // x8
  char *v44; // x9
  char *s1_2; // x22
  spine::SpineExtension *PathConstraint; // x0
  unsigned __int64 v47; // x8
  spine::SpineExtension *PathConstraint_1; // x26
  __int64 v49; // x22
  int n8_3; // w8
  __int64 n8_4; // x20
  __int64 InstanceEv_1; // x0
  __int64 v53; // x8
  __int64 v54; // x9
  char *s1_3; // x22
  __int64 InstanceEv_2; // x0
  __int64 v57; // x10
  __int64 v58; // x24
  __int64 v59; // x8
  unsigned __int64 v60; // x22
  const spine::String *Name; // x0
  int v62; // w3
  __int64 v63; // x8
  __int64 v64; // x9
  __int64 v65; // x10
  __int64 v66; // x9
  char *v67; // x11
  char *v68; // x22
  size_t v69; // x0
  int n3; // w23
  __int64 v71; // x8
  char *v72; // x9
  char *v73; // x22
  __int64 lpsrc; // x27
  __int64 v75; // x0
  __int64 v76; // x8
  __int64 v77; // x10
  __int64 v78; // x8
  spine::SpineExtension *v79; // x0
  __int64 v80; // x9
  __int64 v81; // x8
  __int64 v82; // x9
  __int64 v83; // x8
  __int64 v84; // x9
  __int64 v85; // x8
  __int64 v86; // x9
  __int64 v87; // x8
  __int64 v88; // x9
  __int64 v89; // x8
  __int64 v90; // x8
  __int64 v91; // x10
  unsigned __int64 v92; // x28
  unsigned __int64 v93; // x8
  __int64 v94; // x21
  __int64 v95; // x20
  __int64 v96; // x22
  int n8_5; // w8
  __int64 n8_6; // x26
  __int64 InstanceEv_4; // x0
  __int64 v100; // x0
  __int64 v101; // x8
  spine::SpineExtension *v102; // x0
  __int64 v103; // x8
  unsigned __int64 v104; // x23
  unsigned __int64 v105; // x8
  __int64 v106; // x28
  __int64 v107; // x21
  __int64 v108; // x22
  int n8_17; // w8
  __int64 n8_18; // x20
  __int64 InstanceEv_23; // x0
  __int64 v112; // x0
  __int64 v113; // x8
  spine::SpineExtension *v114; // x0
  __int64 v115; // x9
  __int64 v116; // x8
  __int64 v117; // x9
  __int64 v118; // x8
  __int64 v119; // x9
  __int64 v120; // x8
  __int64 v121; // x9
  __int64 v122; // x8
  __int64 v123; // x9
  __int64 v124; // x8
  __int64 v125; // x9
  __int64 v126; // x8
  __int64 v127; // x9
  __int64 v128; // x8
  __int64 v129; // x9
  __int64 v130; // x8
  __int64 v131; // x9
  __int64 v132; // x8
  __int64 v133; // x9
  __int64 v134; // x8
  __int64 v135; // x9
  __int64 v136; // x8
  __int64 v137; // x9
  __int64 v138; // x8
  __int64 v139; // x8
  __int64 v140; // x10
  unsigned __int64 v141; // x23
  unsigned __int64 v142; // x8
  __int64 v143; // x21
  __int64 v144; // x20
  __int64 v145; // x22
  int n8_13; // w8
  __int64 n8_14; // x26
  __int64 InstanceEv_17; // x0
  __int64 v149; // x0
  __int64 v150; // x8
  __int64 v151; // x9
  __int64 v152; // x8
  __int64 v153; // x9
  __int64 v154; // x8
  spine::SpineExtension *v155; // x0
  __int64 v156; // x9
  __int64 v157; // x8
  unsigned __int64 v158; // x28
  unsigned __int64 v159; // x8
  __int64 v160; // x21
  __int64 v161; // x20
  __int64 v162; // x22
  int n8_7; // w8
  __int64 n8_8; // x26
  __int64 InstanceEv_5; // x0
  __int64 v166; // x0
  __int64 v167; // x8
  spine::SpineExtension *v168; // x0
  __int64 v169; // x9
  __int64 v170; // x8
  unsigned __int64 v171; // x28
  unsigned __int64 v172; // x8
  __int64 v173; // x21
  __int64 v174; // x20
  __int64 v175; // x22
  int n8_9; // w8
  __int64 n8_10; // x26
  __int64 InstanceEv_6; // x0
  __int64 v179; // x0
  __int64 v180; // x8
  spine::SpineExtension *v181; // x0
  __int64 v182; // x9
  __int64 v183; // x8
  unsigned __int64 v184; // x28
  unsigned __int64 v185; // x8
  __int64 v186; // x21
  __int64 v187; // x20
  __int64 v188; // x22
  int n8_11; // w8
  __int64 n8_12; // x26
  __int64 InstanceEv_7; // x0
  __int64 v192; // x0
  __int64 v193; // x8
  spine::SpineExtension *v194; // x0
  __int64 v195; // x9
  __int64 v196; // x8
  __int64 v197; // x8
  char *v198; // x9
  const char *s; // x28
  const char *s_1; // x22
  __int64 InstanceEv_8; // x0
  spine::SpineExtension *v202; // x0
  __int64 v203; // x9
  __int64 v204; // x8
  unsigned __int64 v205; // x23
  unsigned __int64 v206; // x8
  __int64 v207; // x21
  __int64 v208; // x20
  __int64 v209; // x22
  int n8_15; // w8
  __int64 n8_16; // x26
  __int64 InstanceEv_18; // x0
  __int64 v213; // x0
  __int64 v214; // x8
  __int64 v215; // x9
  __int64 v216; // x8
  __int64 v217; // x9
  spine::SpineExtension *v218; // x0
  __int64 v219; // x9
  __int64 v220; // x8
  __int64 v221; // x8
  char *v222; // x9
  const char *s_2; // x28
  __int64 v224; // x9
  __int64 v225; // x8
  __int64 v226; // x9
  __int64 v227; // x8
  __int64 v228; // x9
  __int64 v229; // x8
  __int64 v230; // x9
  __int64 v231; // x8
  __int64 v232; // x9
  __int64 v233; // x8
  __int64 v234; // x9
  __int64 v235; // x8
  __int64 v236; // x9
  __int64 v237; // x8
  __int64 v238; // x9
  __int64 v239; // x8
  __int64 v240; // x9
  __int64 v241; // x8
  __int64 v242; // x8
  __int64 v243; // x9
  __int64 v244; // x9
  __int64 v245; // x9
  __int64 v246; // x8
  __int64 v247; // x9
  __int64 v248; // x10
  __int64 v249; // x9
  char *v250; // x11
  char *src_2; // x22
  size_t v252; // x0
  unsigned int n0x7530; // w11
  unsigned int v254; // w20
  __int64 v255; // x10
  __int64 v256; // x8
  char *v257; // x9
  char *s1_5; // x22
  size_t v259; // x0
  __int64 v260; // x22
  __int64 v261; // x9
  spine::SpineExtension *v262; // x22
  __int64 InstanceEv_9; // x0
  spine::SpineExtension *v264; // x0
  char *dest_1; // x22
  __int64 InstanceEv_10; // x0
  __int64 NameEv; // x0
  char *s1_6; // x28
  char *s1_7; // x1
  const char *s_3; // x22
  __int64 InstanceEv_19; // x0
  __int64 InstanceEv_11; // x0
  int v275; // w8
  spine::v3::AtlasAttachmentLoader *Region; // x0
  bool v277; // w28
  spine::SpineExtension *v278; // x0
  size_t v279; // x20
  __int64 InstanceEv_12; // x0
  unsigned __int64 v281; // x8
  unsigned __int64 v282; // x22
  __int128 endptr_6; // q0
  spine::SpineExtension *v284; // x0
  __int64 v285; // x9
  __int64 v286; // x8
  __int64 v287; // x9
  __int64 v288; // x8
  __int64 v289; // x9
  __int64 v290; // x8
  spine::v3::AtlasAttachmentLoader *v291; // x0
  size_t v292; // x20
  __int64 InstanceEv_13; // x0
  void *dest_3; // x0
  char *dest_4; // x22
  __int64 InstanceEv_14; // x0
  char *src_1; // x22
  __int64 InstanceEv_15; // x0
  spine::SpineExtension *v299; // x0
  __int64 v300; // x22
  __int64 InstanceEv_16; // x0
  spine::SpineExtension *v302; // x0
  char *v303; // x22
  __int64 InstanceEv_20; // x0
  spine::SpineExtension *v305; // x0
  char *v306; // x22
  __int64 InstanceEv_21; // x0
  spine::SpineExtension *v308; // x0
  __int64 v309; // x22
  __int64 InstanceEv_22; // x0
  const char *s1_4; // x22
  __int64 InstanceEv_3; // x0
  spine::v3::MeshAttachment **v313; // x20
  spine::v3::MeshAttachment **v314; // x21
  spine::v3::Skin *AttachmentEmRKNS_6StringE; // x0
  spine::v3::Skin *AttachmentEmRKNS_6StringE_1; // x8
  __int64 v317; // x0
  unsigned __int64 v318; // [xsp+18h] [xbp-168h]
  __int64 v319; // [xsp+20h] [xbp-160h]
  __int64 v320; // [xsp+28h] [xbp-158h]
  spine::v3::SkeletonData *v321; // [xsp+30h] [xbp-150h]
  unsigned __int64 v322; // [xsp+38h] [xbp-148h]
  __int128 p_endptr; // [xsp+48h] [xbp-138h] BYREF
  char *s1; // [xsp+58h] [xbp-128h] BYREF
  size_t v325; // [xsp+60h] [xbp-120h]
  char *dest_2; // [xsp+68h] [xbp-118h]
  char v327; // [xsp+70h] [xbp-110h]
  bool v328; // [xsp+78h] [xbp-108h]
  void (__fastcall **endptr_5)(spine::String *__hidden); // [xsp+80h] [xbp-100h] BYREF
  size_t v330; // [xsp+88h] [xbp-F8h]
  char *dest; // [xsp+90h] [xbp-F0h]
  char v332; // [xsp+98h] [xbp-E8h]
  void (__fastcall **endptr_4)(spine::String *__hidden); // [xsp+A0h] [xbp-E0h] BYREF
  size_t v334; // [xsp+A8h] [xbp-D8h]
  char *src; // [xsp+B0h] [xbp-D0h]
  char v336; // [xsp+B8h] [xbp-C8h]
  _QWORD v337[2]; // [xsp+C0h] [xbp-C0h] BYREF
  __int64 v338; // [xsp+D0h] [xbp-B0h]
  char v339; // [xsp+D8h] [xbp-A8h]
  void (__fastcall **endptr_3)(spine::String *__hidden); // [xsp+E0h] [xbp-A0h] BYREF
  size_t v341; // [xsp+E8h] [xbp-98h]
  char *v342; // [xsp+F0h] [xbp-90h]
  char v343; // [xsp+F8h] [xbp-88h]
  void (__fastcall **endptr_2)(spine::String *__hidden); // [xsp+100h] [xbp-80h] BYREF
  size_t v345; // [xsp+108h] [xbp-78h]
  char *v346; // [xsp+110h] [xbp-70h]
  char v347; // [xsp+118h] [xbp-68h]
  _QWORD v348[2]; // [xsp+120h] [xbp-60h] BYREF
  __int64 v349; // [xsp+130h] [xbp-50h]
  char v350; // [xsp+138h] [xbp-48h]
  void (__fastcall **endptr)(spine::String *__hidden); // [xsp+140h] [xbp-40h] BYREF
  size_t v352; // [xsp+148h] [xbp-38h]
  const char *s1_1; // [xsp+150h] [xbp-30h]
  char v354; // [xsp+158h] [xbp-28h]
  __int64 v355; // [xsp+160h] [xbp-20h]

  v4 = a2;
  v355 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  *((_QWORD *)a2 + 17) = 0;
  v6 = *((_QWORD *)this + 14);
// Read the number of skins
  v7 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v6);
  *((_QWORD *)this + 14) = v6 + 2;
  v9 = *((_QWORD *)a2 + 14);
  v8 = *((_QWORD *)a2 + 15);
  *((_QWORD *)a2 + 14) = v7;
  v318 = v7;
  v10 = v8 >= v7;
  v11 = v7;
  if ( !v10 )
  {
    v12 = *((_QWORD *)a2 + 16);
    if ( (unsigned int)(int)(float)((float)(unsigned int)v7 * 1.75) <= 8 )
      n8 = 8;
    else
      n8 = (int)(float)((float)(unsigned int)v7 * 1.75);
    *((_QWORD *)a2 + 15) = n8;
    Instance = spine::SpineExtension::getInstance(this);
    v15 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)Instance + 32LL))(
            Instance,
            v12,
            8LL * n8,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
            85);
    v11 = *((_QWORD *)v4 + 14);
    *((_QWORD *)v4 + 16) = v15;
  }
  while ( v9 < v11 )
  {
    *(_QWORD *)(*((_QWORD *)v4 + 16) + 8 * v9++) = 0;
    v11 = *((_QWORD *)v4 + 14);
  }
// -----

  if ( (_DWORD)v318 )
  {
    v319 = 0;
    v321 = v4;

    while ( 1 )
    {
      v16 = *((_QWORD *)this + 14);
      v352 = 0;
      s1_1 = 0;
      endptr = endptr;
      v17 = *((_QWORD *)this + 11);
      v354 = 0;
      v18 = *(unsigned int *)(v17 + v16);
      *((_QWORD *)this + 14) = v16 + 4;
      if ( (_DWORD)v18 != -1 )
      {
        v19 = (char *)this + 121;
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v19 = (char *)*((_QWORD *)this + 17);
        if ( v19 )
        {
          s1_8 = &v19[v18];
          v352 = strlen(&v19[v18]);
          s1_1 = s1_8;
          v354 = 1;
        }
      }
      v21 = (_QWORD *)spine::SpineObject::operator new(
                        (spine::SpineObject *)&qword_90,
                        (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d"
                                          "/spinex/v3/SCSLoader_v3.cpp",
                        (const char *)off_168 + 5,
                        a4);
      spine::v3::Skin::Skin((spine::v3::Skin *)v21, (const spine::String *)&endptr);
      *(_QWORD *)(*((_QWORD *)v4 + 16) + 8 * v319) = v21;
      v22 = (spine::SpineExtension *)strcmp(s1_1, "default");
      if ( !(_DWORD)v22 )
        *((_QWORD *)v4 + 17) = v21;
      v23 = *((_QWORD *)this + 11);
      v24 = *((_QWORD *)this + 14);
      v25 = *(unsigned __int16 *)(v23 + v24);
      v26 = v24 + 2;
      *((_QWORD *)this + 14) = v26;
      if ( v25 )
      {
        do
        {
          v28 = *((_QWORD *)this + 14);
          v29 = v28 + 2;
          v30 = *(__int16 *)(*((_QWORD *)this + 11) + v28);
          *((_QWORD *)this + 14) = v29;
          v31 = v21[11];
          v32 = *((_QWORD *)v4 + 8);
          if ( v31 == v21[12] )
          {
            v33 = *(_QWORD *)(v32 + 8 * v30);
            v34 = v21[13];
            n8_1 = (int)(float)((float)v31 * 1.75);
            if ( (unsigned int)n8_1 <= 8 )
              n8_1 = 8;
            n8_2 = n8_1;
            v21[12] = n8_1;
            InstanceEv = spine::SpineExtension::getInstance(v22);
            v22 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv + 32LL))(
                                             InstanceEv,
                                             v34,
                                             8 * n8_2,
                                             "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.and"
                                             "roidstudio/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-suppor"
                                             "t/spine/cpp/Vector.h",
                                             109);
            v38 = v21[11];
            v21[13] = v22;
            v21[11] = v38 + 1;
            *((_QWORD *)v22 + v38) = v33;
          }
          else
          {
            v27 = v21[13];
            v21[11] = v31 + 1;
            *(_QWORD *)(v27 + 8 * v31) = *(_QWORD *)(v32 + 8 * v30);
          }
          --v25;
        }
        while ( v25 );
        v23 = *((_QWORD *)this + 11);
        v26 = *((_QWORD *)this + 14);
      }
      v39 = *(unsigned __int16 *)(v23 + v26);
      v40 = v26 + 2;
      *((_QWORD *)this + 14) = v40;
      if ( v39 )
      {
        do
        {
          v41 = *((_QWORD *)this + 14);
          *((_QWORD *)&p_endptr + 1) = 0;
          s1 = 0;
          *(_QWORD *)&p_endptr = endptr;
          v42 = *((_QWORD *)this + 11);
          LOBYTE(v325) = 0;
          v43 = *(unsigned int *)(v42 + v41);
          *((_QWORD *)this + 14) = v41 + 4;
          if ( (_DWORD)v43 != -1 )
          {
            v44 = (char *)this + 121;
            if ( (*((_BYTE *)this + 120) & 1) != 0 )
              v44 = (char *)*((_QWORD *)this + 17);
            if ( v44 )
            {
              s1_2 = &v44[v43];
              *((_QWORD *)&p_endptr + 1) = strlen(&v44[v43]);
              s1 = s1_2;
              LOBYTE(v325) = 1;
            }
          }
          PathConstraint = (spine::SpineExtension *)spine::v3::SkeletonData::findPathConstraint(
                                                      v4,
                                                      (const spine::String *)&p_endptr);
          v47 = v21[15];
          PathConstraint_1 = PathConstraint;
          if ( v47 == v21[16] )
          {
            v49 = v21[17];
            n8_3 = (int)(float)((float)v47 * 1.75);
            if ( (unsigned int)n8_3 <= 8 )
              n8_3 = 8;
            n8_4 = n8_3;
            v21[16] = n8_3;
            InstanceEv_1 = spine::SpineExtension::getInstance(PathConstraint);
            PathConstraint = (spine::SpineExtension *)(*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_1 + 32LL))(
                                                        InstanceEv_1,
                                                        v49,
                                                        8 * n8_4,
                                                        "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/"
                                                        "ur/proj.androidstudio/app/src/main/cpp/../../../../../yuna/cocos"
                                                        "2d/cocos/editor-support/spine/cpp/Vector.h",
                                                        109);
            v53 = v21[15];
            v21[17] = PathConstraint;
            v21[15] = v53 + 1;
            *((_QWORD *)PathConstraint + v53) = PathConstraint_1;
          }
          else
          {
            v54 = v21[17];
            v21[15] = v47 + 1;
            *(_QWORD *)(v54 + 8 * v47) = PathConstraint;
          }
          s1_3 = s1;
          v4 = v321;
          *(_QWORD *)&p_endptr = endptr;
          if ( s1 && (v325 & 1) == 0 )
          {
            InstanceEv_2 = spine::SpineExtension::getInstance(PathConstraint);
            (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_2 + 40LL))(
              InstanceEv_2,
              s1_3,
              "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../"
              "../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
              252);
          }
          spine::SpineObject::~SpineObject((spine::SpineObject *)&p_endptr);
          --v39;
        }
        while ( v39 );
        v23 = *((_QWORD *)this + 11);
        v40 = *((_QWORD *)this + 14);
      }
      v57 = *(unsigned __int16 *)(v23 + v40);
      *((_QWORD *)this + 14) = v40 + 2;
      v320 = v57;
      if ( v57 )
        break;
LABEL_209:
      s1_4 = s1_1;
      endptr = endptr;
      if ( s1_1 && (v354 & 1) == 0 )
      {
        InstanceEv_3 = spine::SpineExtension::getInstance(v22);
        (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_3 + 40LL))(
          InstanceEv_3,
          s1_4,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr);
      if ( ++v319 == v318 )
        goto LABEL_212;
    }
    v58 = 0;

//----- slot index
    while ( 1 )
    {
      v59 = *((_QWORD *)this + 14);
      v60 = *(__int16 *)(*((_QWORD *)this + 11) + v59);
      *((_QWORD *)this + 14) = v59 + 2;
      Name = (const spine::String *)spine::v3::SlotData::getName(*(spine::v3::SlotData **)(*((_QWORD *)v4 + 12) + 8 * v60));
      spine::String::String((spine::String *)v348, Name);
      v63 = *((_QWORD *)this + 11);
      v64 = *((_QWORD *)this + 14);
      endptr_2 = endptr;
      v345 = 0;
      v346 = 0;
      v347 = 0;
      v65 = *(unsigned int *)(v63 + v64);
      v66 = v64 + 4;
      v322 = v60;
      *((_QWORD *)this + 14) = v66;

// if offset is not -1, read string
      if ( (_DWORD)v65 != -1 )
      {
        v67 = (char *)this + 121;
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v67 = (char *)*((_QWORD *)this + 17);
        if ( v67 )
        {
          v68 = &v67[v65];
          v69 = strlen(&v67[v65]);
          v63 = *((_QWORD *)this + 11);
          v66 = *((_QWORD *)this + 14);
          v345 = v69;
          v346 = v68;
          v347 = 1;
        }
      }


//----- type
      n3 = *(unsigned __int16 *)(v63 + v66);
      endptr_3 = endptr;
      *((_QWORD *)this + 14) = v66 + 2;
      v341 = 0;
      v342 = 0;
      v343 = 0;
//----- path_name_offset
      v71 = *(unsigned int *)(v63 + v66 + 2);
      *((_QWORD *)this + 14) = v66 + 6;
      if ( (_DWORD)v71 != -1 )
      {
        v72 = (char *)this + 121;
        if ( (*((_BYTE *)this + 120) & 1) != 0 )
          v72 = (char *)*((_QWORD *)this + 17);
        if ( v72 )
        {
          v73 = &v72[v71];
          v341 = strlen(&v72[v71]);
          v342 = v73;
          v343 = 1;
        }
      }
      lpsrc = 0;
      if ( n3 > 3 )
        break;

// for 2 MeshAttachment and 3 linkedMeshAttachment
// 2 MeshAttachment
      if ( (unsigned int)(n3 - 2) < 2 )
      {
        lpsrc = spine::SpineObject::operator new(
                  (spine::SpineObject *)&off_1A0,
                  (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spine"
                                    "x/v3/SCSLoader_v3.cpp",
                  (const char *)&dword_1C8 + 1,
                  v62);
        spine::v3::MeshAttachment::MeshAttachment((spine::v3::MeshAttachment *)lpsrc, (const spine::String *)&endptr_3);
        v337[0] = endptr;
        v337[1] = 0;
        v338 = 0;
        v339 = 0;
//mesh _read_vertex_attachment
        v79 = (spine::SpineExtension *)spine::v3::SkeletonDataLoader::assignVertexAttachment(
                                         this,
                                         (spine::v3::Attachment *)lpsrc,
                                         (spine::String *)v337);
//floats6
        *(_DWORD *)(lpsrc + 160) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
        v80 = *((_QWORD *)this + 11);
        v81 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v81;
        *(_DWORD *)(lpsrc + 164) = *(_DWORD *)(v80 + v81);
        v82 = *((_QWORD *)this + 11);
        v83 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v83;
        *(_DWORD *)(lpsrc + 168) = *(_DWORD *)(v82 + v83);
        v84 = *((_QWORD *)this + 11);
        v85 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v85;
        *(_DWORD *)(lpsrc + 172) = *(_DWORD *)(v84 + v85);
        v86 = *((_QWORD *)this + 11);
        v87 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v87;
        *(_DWORD *)(lpsrc + 176) = *(_DWORD *)(v86 + v87);
        v88 = *((_QWORD *)this + 11);
        v89 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v89;
        *(_DWORD *)(lpsrc + 180) = *(_DWORD *)(v88 + v89);
        v90 = *((_QWORD *)this + 14);
        v91 = *((_QWORD *)this + 11);
        *((_QWORD *)this + 14) = v90 + 4;

// uv_count
        v92 = *(unsigned __int16 *)(v91 + v90 + 4);
        *((_QWORD *)this + 14) = v90 + 6;
        v93 = *(_QWORD *)(lpsrc + 208);
        *(_QWORD *)(lpsrc + 200) = 0;
        v94 = *((_QWORD *)this + 11);
        v95 = *((_QWORD *)this + 14);
        if ( v93 >= v92 )
        {
          v100 = *(_QWORD *)(lpsrc + 216);
          v101 = 0;
        }
        else
        {
          v96 = *(_QWORD *)(lpsrc + 216);
          n8_5 = (int)(float)((float)(unsigned int)v92 * 1.75);
          if ( (unsigned int)n8_5 <= 8 )
            n8_5 = 8;
          n8_6 = n8_5;
          *(_QWORD *)(lpsrc + 208) = n8_5;
          InstanceEv_4 = spine::SpineExtension::getInstance(v79);
          v100 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_4
                                                                                             + 32LL))(
                   InstanceEv_4,
                   v96,
                   4 * n8_6,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v101 = *(_QWORD *)(lpsrc + 200);
          *(_QWORD *)(lpsrc + 216) = v100;
        }
        v155 = (spine::SpineExtension *)memcpy((void *)(v100 + 4 * v101), (const void *)(v94 + v95), 4 * v92);
        *(_QWORD *)(lpsrc + 200) = v92;
        v156 = *((_QWORD *)this + 11);
        v157 = *((_QWORD *)this + 14) + 4 * v92;
        *((_QWORD *)this + 14) = v157;
// region-space verts
        v158 = *(unsigned __int16 *)(v156 + v157);
        *((_QWORD *)this + 14) = v157 + 2;
        v159 = *(_QWORD *)(lpsrc + 240);
        *(_QWORD *)(lpsrc + 232) = 0;
        v160 = *((_QWORD *)this + 11);
        v161 = *((_QWORD *)this + 14);
        if ( v159 >= v158 )
        {
          v166 = *(_QWORD *)(lpsrc + 248);
          v167 = 0;
        }
        else
        {
          v162 = *(_QWORD *)(lpsrc + 248);
          n8_7 = (int)(float)((float)(unsigned int)v158 * 1.75);
          if ( (unsigned int)n8_7 <= 8 )
            n8_7 = 8;
          n8_8 = n8_7;
          *(_QWORD *)(lpsrc + 240) = n8_7;
          InstanceEv_5 = spine::SpineExtension::getInstance(v155);
          v166 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_5
                                                                                             + 32LL))(
                   InstanceEv_5,
                   v162,
                   4 * n8_8,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v167 = *(_QWORD *)(lpsrc + 232);
          *(_QWORD *)(lpsrc + 248) = v166;
        }
        v168 = (spine::SpineExtension *)memcpy((void *)(v166 + 4 * v167), (const void *)(v160 + v161), 4 * v158);
        *(_QWORD *)(lpsrc + 232) = v158;
        v169 = *((_QWORD *)this + 11);
        v170 = *((_QWORD *)this + 14) + 4 * v158;
        *((_QWORD *)this + 14) = v170;


// triangles
        v171 = *(unsigned __int16 *)(v169 + v170);
        *((_QWORD *)this + 14) = v170 + 2;
        v172 = *(_QWORD *)(lpsrc + 272);
        *(_QWORD *)(lpsrc + 264) = 0;
        v173 = *((_QWORD *)this + 11);
        v174 = *((_QWORD *)this + 14);
        if ( v172 >= v171 )
        {
          v179 = *(_QWORD *)(lpsrc + 280);
          v180 = 0;
        }
        else
        {
          v175 = *(_QWORD *)(lpsrc + 280);
          n8_9 = (int)(float)((float)(unsigned int)v171 * 1.75);
          if ( (unsigned int)n8_9 <= 8 )
            n8_9 = 8;
          n8_10 = n8_9;
          *(_QWORD *)(lpsrc + 272) = n8_9;
          InstanceEv_6 = spine::SpineExtension::getInstance(v168);
          v179 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_6
                                                                                             + 32LL))(
                   InstanceEv_6,
                   v175,
                   2 * n8_10,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v180 = *(_QWORD *)(lpsrc + 264);
          *(_QWORD *)(lpsrc + 280) = v179;
        }
        v181 = (spine::SpineExtension *)memcpy((void *)(v179 + 2 * v180), (const void *)(v173 + v174), 2 * v171);
        *(_QWORD *)(lpsrc + 264) = v171;
        v182 = *((_QWORD *)this + 11);
        v183 = *((_QWORD *)this + 14) + 2 * v171;
        *((_QWORD *)this + 14) = v183;

// edges
        v184 = *(unsigned __int16 *)(v182 + v183);
        *((_QWORD *)this + 14) = v183 + 2;
        v185 = *(_QWORD *)(lpsrc + 304);
        *(_QWORD *)(lpsrc + 296) = 0;
        v186 = *((_QWORD *)this + 11);
        v187 = *((_QWORD *)this + 14);
        if ( v185 >= v184 )
        {
          v192 = *(_QWORD *)(lpsrc + 312);
          v193 = 0;
        }
        else
        {
          v188 = *(_QWORD *)(lpsrc + 312);
          n8_11 = (int)(float)((float)(unsigned int)v184 * 1.75);
          if ( (unsigned int)n8_11 <= 8 )
            n8_11 = 8;
          n8_12 = n8_11;
          *(_QWORD *)(lpsrc + 304) = n8_11;
          InstanceEv_7 = spine::SpineExtension::getInstance(v181);
          v192 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_7
                                                                                             + 32LL))(
                   InstanceEv_7,
                   v188,
                   2 * n8_12,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v193 = *(_QWORD *)(lpsrc + 296);
          *(_QWORD *)(lpsrc + 312) = v192;
        }
        v194 = (spine::SpineExtension *)memcpy((void *)(v192 + 2 * v193), (const void *)(v186 + v187), 2 * v184);
        *(_QWORD *)(lpsrc + 296) = v184;
        v195 = *((_QWORD *)this + 14) + 2 * v184;
        v196 = *((_QWORD *)this + 11);
        *((_QWORD *)this + 14) = v195;

// atlas region path
        v197 = *(unsigned int *)(v196 + v195);
        *((_QWORD *)this + 14) = v195 + 4;
        if ( (_DWORD)v197 == -1 )
        {
          s = 0;
        }
        else
        {
          v198 = (char *)this + 121;
          if ( (*((_BYTE *)this + 120) & 1) != 0 )
            v198 = (char *)*((_QWORD *)this + 17);
          s = &v198[v197];
        }
        s_1 = *(const char **)(lpsrc + 336);
        v4 = v321;
        if ( s_1 != s )
        {
          if ( s_1 && (*(_BYTE *)(lpsrc + 344) & 1) == 0 )
          {
            InstanceEv_8 = spine::SpineExtension::getInstance(v194);
            (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_8 + 40LL))(
              InstanceEv_8,
              s_1,
              "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../"
              "../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
              129);
          }
          if ( s )
          {
            *(_QWORD *)(lpsrc + 328) = strlen(s);
            *(_QWORD *)(lpsrc + 336) = s;
            *(_BYTE *)(lpsrc + 344) = 1;
          }
          else
          {
            *(_QWORD *)(lpsrc + 328) = 0;
            *(_QWORD *)(lpsrc + 336) = 0;
            *(_BYTE *)(lpsrc + 344) = 0;
          }
          v4 = v321;
        }

// floats10
        *(_DWORD *)(lpsrc + 352) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
        v224 = *((_QWORD *)this + 11);
        v225 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v225;
        *(_DWORD *)(lpsrc + 356) = *(_DWORD *)(v224 + v225);
        v226 = *((_QWORD *)this + 11);
        v227 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v227;
        *(_DWORD *)(lpsrc + 360) = *(_DWORD *)(v226 + v227);
        v228 = *((_QWORD *)this + 11);
        v229 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v229;
        *(_DWORD *)(lpsrc + 364) = *(_DWORD *)(v228 + v229);
        v230 = *((_QWORD *)this + 11);
        v231 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v231;
        *(_DWORD *)(lpsrc + 368) = *(_DWORD *)(v230 + v231);
        v232 = *((_QWORD *)this + 11);
        v233 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v233;
        *(_DWORD *)(lpsrc + 372) = *(_DWORD *)(v232 + v233);
        v234 = *((_QWORD *)this + 11);
        v235 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v235;
        *(_DWORD *)(lpsrc + 384) = *(_DWORD *)(v234 + v235);
        v236 = *((_QWORD *)this + 11);
        v237 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v237;
        *(_DWORD *)(lpsrc + 388) = *(_DWORD *)(v236 + v237);
        v238 = *((_QWORD *)this + 11);
        v239 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v239;
        *(_DWORD *)(lpsrc + 392) = *(_DWORD *)(v238 + v239);
        v240 = *((_QWORD *)this + 11);
        v241 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v241;
        *(_DWORD *)(lpsrc + 396) = *(_DWORD *)(v240 + v241);
        v242 = *((_QWORD *)this + 14);
        v243 = *((_QWORD *)this + 11);
        *((_QWORD *)this + 14) = v242 + 4;

// read int32 v243???  maybe hull length
        LODWORD(v243) = *(_DWORD *)(v243 + v242 + 4);
        *((_QWORD *)this + 14) = v242 + 8;
        *(_DWORD *)(lpsrc + 400) = v243;

// read bool v244??? flag
        v244 = *((_QWORD *)this + 14);
        LODWORD(v242) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v244);
        *((_QWORD *)this + 14) = v244 + 1;
        *(_BYTE *)(lpsrc + 404) = (_DWORD)v242 != 0;

// read int32 v245???
        v245 = *((_QWORD *)this + 14);
        LODWORD(v242) = *(_DWORD *)(*((_QWORD *)this + 11) + v245);
        endptr_4 = endptr;
        *((_QWORD *)this + 14) = v245 + 4;
        *(_DWORD *)(lpsrc + 408) = v242;
        //clean
        v246 = *((_QWORD *)this + 11);
        v247 = *((_QWORD *)this + 14);
        v334 = 0;
        src = 0;
        v336 = 0;

// read string_offset  v248???
        v248 = *(unsigned int *)(v246 + v247);
        v249 = v247 + 4;
        *((_QWORD *)this + 14) = v249;
        if ( (_DWORD)v248 != -1 )
        {
          v250 = (char *)this + 121;
          if ( (*((_BYTE *)this + 120) & 1) != 0 )
            v250 = (char *)*((_QWORD *)this + 17);
          if ( v250 )
          {
            src_2 = &v250[v248];
            v252 = strlen(&v250[v248]);
            v246 = *((_QWORD *)this + 11);
            v249 = *((_QWORD *)this + 14);
            v334 = v252;
            src = src_2;
            v336 = 1;
          }
        }
        n0x7530 = *((_DWORD *)this + 3);
// read int16  v254???
        v254 = *(__int16 *)(v246 + v249);
        v255 = v249 + 2;
        *((_QWORD *)this + 14) = v249 + 2;
    // check version (30001)  0x7530 = 30000
    // if V3
    // read int16
        if ( n0x7530 > 0x7530 )
        {
          LODWORD(v260) = *(__int16 *)(v246 + v255);
          v261 = v249 + 4;
          *((_QWORD *)this + 14) = v261;
        }
    // if V2 begin
    // read skin_name_offset if -1 use "default"
        else
        {
          p_endptr = (unsigned __int64)endptr;
          s1 = 0;
          LOBYTE(v325) = 0;

          v256 = *(unsigned int *)(v246 + v255);
          *((_QWORD *)this + 14) = v249 + 6;
          if ( (_DWORD)v256 == -1 )
            goto LABEL_137;
          v257 = (char *)this + 121;
          if ( (*((_BYTE *)this + 120) & 1) != 0 )
            v257 = (char *)*((_QWORD *)this + 17);

          if ( v257
            && (s1_5 = &v257[v256],
                v259 = strlen(&v257[v256]),
                *((_QWORD *)&p_endptr + 1) = v259,
                s1 = s1_5,
                LOBYTE(v325) = 1,
                v259) )
          {
            dest = s1_5;
            endptr_5 = endptr;
            v330 = v259;
            v332 = 1;
          }
          else
          {
LABEL_137:
            endptr_5 = endptr;
            v262 = (spine::SpineExtension *)strlen("default");
            v332 = 0;
            v330 = (size_t)v262;
            InstanceEv_9 = spine::SpineExtension::getInstance(v262);
            dest = (char *)(*(__int64 (__fastcall **)(__int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_9
                                                                                              + 24LL))(
                             InstanceEv_9,
                             (__int64)v262 + 1,
                             "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/s"
                             "rc/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                             68);
            memcpy(dest, "default", v330 + 1);
          }
          v264 = (spine::SpineExtension *)spine::String::operator=(&p_endptr, &endptr_5);
          dest_1 = dest;
          endptr_5 = endptr;
          if ( dest && (v332 & 1) == 0 )
          {
            InstanceEv_10 = spine::SpineExtension::getInstance(v264);
            (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_10 + 40LL))(
              InstanceEv_10,
              dest_1,
              "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../"
              "../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
              252);
          }
          spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr_5);
          //check skin number
          if ( *((_QWORD *)v4 + 14) )
          {
            v260 = 0;
            while ( 1 )
            {
              NameEv = spine::v3::Skin::getName(*(spine::v3::Skin **)(*((_QWORD *)v4 + 16) + 8 * v260));
              s1_6 = s1;
              s1_7 = *(char **)(NameEv + 16);
              if ( s1 == s1_7 )
                break;
              if ( *((_QWORD *)&p_endptr + 1) == *(_QWORD *)(NameEv + 8) && s1 != 0 && s1_7 != 0 )
              {
                NameEv = strcmp(s1, s1_7);
                if ( !(_DWORD)NameEv )
                {
                  *(_QWORD *)&p_endptr = endptr;
                  goto LABEL_164;
                }
              }
              if ( *((_QWORD *)v4 + 14) <= (unsigned __int64)++v260 )
                goto LABEL_162;
            }
          }
          else
          {
            s1_6 = s1;
LABEL_162:
            LODWORD(v260) = 0;
          }
          *(_QWORD *)&p_endptr = endptr;
          if ( s1_6 )
          {
          //clean
LABEL_164:
            if ( (v325 & 1) == 0 )
            {
              InstanceEv_11 = spine::SpineExtension::getInstance((spine::SpineExtension *)NameEv);
              (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_11 + 40LL))(
                InstanceEv_11,
                s1_6,
                "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/."
                "./../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                252);
            }
          }
          spine::SpineObject::~SpineObject((spine::SpineObject *)&p_endptr);
          v246 = *((_QWORD *)this + 11);
          v261 = *((_QWORD *)this + 14);
        }
    //end V2

// read bool v277 maybe deform
        v275 = *(unsigned __int8 *)(v246 + v261);
        Region = (spine::v3::AtlasAttachmentLoader *)*((_QWORD *)this + 27);
        *((_QWORD *)this + 14) = v261 + 1;
        v277 = v275 != 0;
        if ( Region )
        {
          Region = (spine::v3::AtlasAttachmentLoader *)spine::v3::AtlasAttachmentLoader::findRegion(
                                                         Region,
                                                         (const spine::String *)(lpsrc + 320));
          *(_QWORD *)(lpsrc + 144) = Region;
          *(_QWORD *)(lpsrc + 152) = 0;
        }
//2 meshAttachment end

//3 linkedMeshAttachment
        if ( n3 == 3 ) // 3 LinkedMesh
        {
          *(_QWORD *)&p_endptr = lpsrc;
          *((_QWORD *)&p_endptr + 1) = __PAIR64__(v260, v254);
          s1 = (char *)endptr;
          if ( src )
          {
            if ( v336 == 1 )
            {
              v327 = v336;
              v325 = v334;
              dest_2 = src;
            }
            else
            {
              v279 = v334;
              v327 = 0;
              v325 = v334;
              InstanceEv_12 = spine::SpineExtension::getInstance(Region);
              dest_2 = (char *)(*(__int64 (__fastcall **)(__int64, size_t, const char *, __int64))(*(_QWORD *)InstanceEv_12
                                                                                                 + 24LL))(
                                 InstanceEv_12,
                                 v279 + 1,
                                 "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/a"
                                 "pp/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                                 96);
              Region = (spine::v3::AtlasAttachmentLoader *)memcpy(dest_2, src, v334 + 1);
            }
          }
          else
          {
            v325 = 0;
            dest_2 = 0;
            v327 = 0;
          }
          v282 = *((_QWORD *)this + 20);
          v281 = *((_QWORD *)this + 21);
          v328 = v277;
          if ( v282 >= v281 )
          {
            v284 = (spine::SpineExtension *)std::vector<spine::v3::SkeletonDataLoader::linked_mesh>::__emplace_back_slow_path<spine::v3::SkeletonDataLoader::linked_mesh>(
                                              (char *)this + 152,
                                              &p_endptr);
          }
          else
          {
            endptr_6 = p_endptr;
            *(_QWORD *)(v282 + 16) = endptr;
            *(_OWORD *)v282 = endptr_6;
            if ( dest_2 )
            {
              if ( v327 == 1 )
              {
                *(_QWORD *)(v282 + 24) = v325;
                *(_QWORD *)(v282 + 32) = dest_2;
                *(_BYTE *)(v282 + 40) = v327;
              }
              else
              {
                v292 = v325;
                *(_BYTE *)(v282 + 40) = 0;
                *(_QWORD *)(v282 + 24) = v292;
                InstanceEv_13 = spine::SpineExtension::getInstance(Region);
                dest_3 = (void *)(*(__int64 (__fastcall **)(__int64, size_t, const char *, __int64))(*(_QWORD *)InstanceEv_13 + 24LL))(
                                   InstanceEv_13,
                                   v292 + 1,
                                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio"
                                   "/app/src/main/cpp/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
                                   96);
                *(_QWORD *)(v282 + 32) = dest_3;
                memcpy(dest_3, dest_2, v325 + 1);
              }
            }
            else
            {
              *(_QWORD *)(v282 + 24) = 0;
              *(_QWORD *)(v282 + 32) = 0;
              *(_BYTE *)(v282 + 40) = 0;
            }
            v284 = (spine::SpineExtension *)(v282 + 56);
            *(_BYTE *)(v282 + 48) = v328;
            *((_QWORD *)this + 20) = v282 + 56;
          }
          dest_4 = dest_2;
          *((_QWORD *)this + 20) = v284;
          s1 = (char *)endptr;
          if ( dest_4 && (v327 & 1) == 0 )
          {
            InstanceEv_14 = spine::SpineExtension::getInstance(v284);
            (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_14 + 40LL))(
              InstanceEv_14,
              dest_4,
              "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../"
              "../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
              252);
          }
          spine::SpineObject::~SpineObject((spine::SpineObject *)&s1);
        }
        else
        {
          v278 = (spine::SpineExtension *)*((_QWORD *)this + 27);
          if ( v278 )
            v278 = (spine::SpineExtension *)(*(__int64 (__fastcall **)(spine::SpineExtension *, __int64))(*(_QWORD *)v278 + 72LL))(
                                              v278,
                                              lpsrc);
        }
        src_1 = src;
        endptr_4 = endptr;
        if ( src && (v336 & 1) == 0 )
        {
          InstanceEv_15 = spine::SpineExtension::getInstance(v278);
          (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_15 + 40LL))(
            InstanceEv_15,
            src_1,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
            252);
        }
        spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr_4);
        v300 = v338;
        v337[0] = endptr;
        if ( v338 && (v339 & 1) == 0 )
        {
          InstanceEv_16 = spine::SpineExtension::getInstance(v299);
          (*(void (__fastcall **)(__int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_16 + 40LL))(
            InstanceEv_16,
            v300,
            "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../.."
            "/../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
            252);
        }
        spine::SpineObject::~SpineObject((spine::SpineObject *)v337);
        goto LABEL_200;
      }
//end 3 linkedMeshAttachment

//0 RegionAttachment begin
      if ( !n3 )
      {
        lpsrc = spine::SpineObject::operator new(
                  (spine::SpineObject *)off_F8,
                  (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spine"
                                    "x/v3/SCSLoader_v3.cpp",
                  (const char *)&qword_198 + 1,
                  v62);
        v114 = (spine::SpineExtension *)spine::v3::RegionAttachment::RegionAttachment(
                                          (spine::v3::RegionAttachment *)lpsrc,
                                          (const spine::String *)&endptr_3);
        *(_DWORD *)(lpsrc + 72) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
        v115 = *((_QWORD *)this + 11);
        v116 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v116;
        *(_DWORD *)(lpsrc + 76) = *(_DWORD *)(v115 + v116);
        v117 = *((_QWORD *)this + 11);
        v118 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v118;
        *(_DWORD *)(lpsrc + 80) = *(_DWORD *)(v117 + v118);
        v119 = *((_QWORD *)this + 11);
        v120 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v120;
        *(_DWORD *)(lpsrc + 84) = *(_DWORD *)(v119 + v120);
        v121 = *((_QWORD *)this + 11);
        v122 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v122;
        *(_DWORD *)(lpsrc + 88) = *(_DWORD *)(v121 + v122);
        v123 = *((_QWORD *)this + 11);
        v124 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v124;
        *(_DWORD *)(lpsrc + 92) = *(_DWORD *)(v123 + v124);
        v125 = *((_QWORD *)this + 11);
        v126 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v126;
        *(_DWORD *)(lpsrc + 96) = *(_DWORD *)(v125 + v126);
        v127 = *((_QWORD *)this + 11);
        v128 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v128;
        *(_DWORD *)(lpsrc + 100) = *(_DWORD *)(v127 + v128);
        v129 = *((_QWORD *)this + 11);
        v130 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v130;
        *(_DWORD *)(lpsrc + 104) = *(_DWORD *)(v129 + v130);
        v131 = *((_QWORD *)this + 11);
        v132 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v132;
        *(_DWORD *)(lpsrc + 108) = *(_DWORD *)(v131 + v132);
        v133 = *((_QWORD *)this + 11);
        v134 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v134;
        *(_DWORD *)(lpsrc + 112) = *(_DWORD *)(v133 + v134);
        v135 = *((_QWORD *)this + 11);
        v136 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v136;
        *(_DWORD *)(lpsrc + 116) = *(_DWORD *)(v135 + v136);
        v137 = *((_QWORD *)this + 11);
        v138 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v138;
        *(_DWORD *)(lpsrc + 120) = *(_DWORD *)(v137 + v138);
        v139 = *((_QWORD *)this + 14);
        v140 = *((_QWORD *)this + 11);
        *((_QWORD *)this + 14) = v139 + 4;
        v141 = *(unsigned __int16 *)(v140 + v139 + 4);
        *((_QWORD *)this + 14) = v139 + 6;
        v142 = *(_QWORD *)(lpsrc + 144);
        *(_QWORD *)(lpsrc + 136) = 0;
        v143 = *((_QWORD *)this + 11);
        v144 = *((_QWORD *)this + 14);
        if ( v142 >= v141 )
        {
          v149 = *(_QWORD *)(lpsrc + 152);
          v150 = 0;
        }
        else
        {
          v145 = *(_QWORD *)(lpsrc + 152);
          n8_13 = (int)(float)((float)(unsigned int)v141 * 1.75);
          if ( (unsigned int)n8_13 <= 8 )
            n8_13 = 8;
          n8_14 = n8_13;
          *(_QWORD *)(lpsrc + 144) = n8_13;
          InstanceEv_17 = spine::SpineExtension::getInstance(v114);
          v149 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_17
                                                                                             + 32LL))(
                   InstanceEv_17,
                   v145,
                   4 * n8_14,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v150 = *(_QWORD *)(lpsrc + 136);
          *(_QWORD *)(lpsrc + 152) = v149;
        }
        v202 = (spine::SpineExtension *)memcpy((void *)(v149 + 4 * v150), (const void *)(v143 + v144), 4 * v141);
        *(_QWORD *)(lpsrc + 136) = v141;
        v203 = *((_QWORD *)this + 11);
        v204 = *((_QWORD *)this + 14) + 4 * v141;
        *((_QWORD *)this + 14) = v204;
        v205 = *(unsigned __int16 *)(v203 + v204);
        *((_QWORD *)this + 14) = v204 + 2;
        v206 = *(_QWORD *)(lpsrc + 176);
        *(_QWORD *)(lpsrc + 168) = 0;
        v207 = *((_QWORD *)this + 11);
        v208 = *((_QWORD *)this + 14);
        if ( v206 >= v205 )
        {
          v213 = *(_QWORD *)(lpsrc + 184);
          v214 = 0;
        }
        else
        {
          v209 = *(_QWORD *)(lpsrc + 184);
          n8_15 = (int)(float)((float)(unsigned int)v205 * 1.75);
          if ( (unsigned int)n8_15 <= 8 )
            n8_15 = 8;
          n8_16 = n8_15;
          *(_QWORD *)(lpsrc + 176) = n8_15;
          InstanceEv_18 = spine::SpineExtension::getInstance(v202);
          v213 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_18
                                                                                             + 32LL))(
                   InstanceEv_18,
                   v209,
                   4 * n8_16,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v214 = *(_QWORD *)(lpsrc + 168);
          *(_QWORD *)(lpsrc + 184) = v213;
        }
        v218 = (spine::SpineExtension *)memcpy((void *)(v213 + 4 * v214), (const void *)(v207 + v208), 4 * v205);
        *(_QWORD *)(lpsrc + 168) = v205;
        v219 = *((_QWORD *)this + 14) + 4 * v205;
        v220 = *((_QWORD *)this + 11);
        *((_QWORD *)this + 14) = v219;
        v221 = *(unsigned int *)(v220 + v219);
        *((_QWORD *)this + 14) = v219 + 4;
        if ( (_DWORD)v221 == -1 )
        {
          s_2 = 0;
        }
        else
        {
          v222 = (char *)this + 121;
          if ( (*((_BYTE *)this + 120) & 1) != 0 )
            v222 = (char *)*((_QWORD *)this + 17);
          s_2 = &v222[v221];
        }
        s_3 = *(const char **)(lpsrc + 208);
        v4 = v321;
        if ( s_3 != s_2 )
        {
          if ( s_3 && (*(_BYTE *)(lpsrc + 216) & 1) == 0 )
          {
            InstanceEv_19 = spine::SpineExtension::getInstance(v218);
            (*(void (__fastcall **)(__int64, const char *, const char *, __int64))(*(_QWORD *)InstanceEv_19 + 40LL))(
              InstanceEv_19,
              s_3,
              "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../"
              "../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
              129);
          }
          if ( s_2 )
          {
            *(_QWORD *)(lpsrc + 200) = strlen(s_2);
            *(_QWORD *)(lpsrc + 208) = s_2;
            *(_BYTE *)(lpsrc + 216) = 1;
          }
          else
          {
            *(_QWORD *)(lpsrc + 200) = 0;
            *(_QWORD *)(lpsrc + 208) = 0;
            *(_BYTE *)(lpsrc + 216) = 0;
          }
          v4 = v321;
        }
        *(_DWORD *)(lpsrc + 232) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
        v285 = *((_QWORD *)this + 11);
        v286 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v286;
        *(_DWORD *)(lpsrc + 236) = *(_DWORD *)(v285 + v286);
        v287 = *((_QWORD *)this + 11);
        v288 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v288;
        *(_DWORD *)(lpsrc + 240) = *(_DWORD *)(v287 + v288);
        v289 = *((_QWORD *)this + 11);
        v290 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v290;
        *(_DWORD *)(lpsrc + 244) = *(_DWORD *)(v289 + v290);
        v291 = (spine::v3::AtlasAttachmentLoader *)*((_QWORD *)this + 27);
        *((_QWORD *)this + 14) += 4LL;
        if ( v291 )
        {
          *(_QWORD *)(lpsrc + 56) = spine::v3::AtlasAttachmentLoader::findRegion(
                                      v291,
                                      (const spine::String *)(lpsrc + 192));
          *(_QWORD *)(lpsrc + 64) = 0;
          (*(void (__fastcall **)(_QWORD, __int64))(**((_QWORD **)this + 27) + 72LL))(*((_QWORD *)this + 27), lpsrc);
        }
        goto LABEL_200;
      }
//0 RegionAttachment end

//1 BoundingBoxAttachment
      if ( n3 == 1 )
      {
        lpsrc = spine::SpineObject::operator new(
                  (spine::SpineObject *)&qword_88,
                  (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spine"
                                    "x/v3/SCSLoader_v3.cpp",
                  (const char *)&qword_1B8 + 6,
                  v62);
        spine::v3::BoundingBoxAttachment::BoundingBoxAttachment(
          (spine::v3::BoundingBoxAttachment *)lpsrc,
          (const spine::String *)&endptr_3);
        spine::v3::SkeletonDataLoader::assignVertexAttachment(this, (spine::v3::Attachment *)lpsrc, 0);
        v75 = *((_QWORD *)this + 27);
        if ( v75 )
          goto LABEL_116;
      }
LABEL_200:
      v302 = (spine::SpineExtension *)spine::v3::Skin::AttachmentMap::put(
                                        (spine::v3::Skin::AttachmentMap *)(v21 + 5),
                                        v322,
                                        (const spine::String *)&endptr_2,
                                        (spine::v3::Attachment *)lpsrc);
      v303 = v342;
      endptr_3 = endptr;
      if ( v342 && (v343 & 1) == 0 )
      {
        InstanceEv_20 = spine::SpineExtension::getInstance(v302);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_20 + 40LL))(
          InstanceEv_20,
          v303,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr_3);
      v306 = v346;
      endptr_2 = endptr;
      if ( v346 && (v347 & 1) == 0 )
      {
        InstanceEv_21 = spine::SpineExtension::getInstance(v305);
        (*(void (__fastcall **)(__int64, char *, const char *, __int64))(*(_QWORD *)InstanceEv_21 + 40LL))(
          InstanceEv_21,
          v306,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)&endptr_2);
      v309 = v349;
      v348[0] = endptr;
      if ( v349 && (v350 & 1) == 0 )
      {
        InstanceEv_22 = spine::SpineExtension::getInstance(v308);
        (*(void (__fastcall **)(__int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_22 + 40LL))(
          InstanceEv_22,
          v309,
          "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cpp/../../."
          "./../../yuna/cocos2d/cocos/editor-support/spine/cpp/SpineString.h",
          252);
      }
      spine::SpineObject::~SpineObject((spine::SpineObject *)v348);
      if ( ++v58 == v320 )
        goto LABEL_209;
    }
//4 5 6
    switch ( n3 ) //4 5 6 
    {
      case 4:
        lpsrc = spine::SpineObject::operator new(
                  (spine::SpineObject *)&dword_B0,
                  (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spine"
                                    "x/v3/SCSLoader_v3.cpp",
                  (const char *)&qword_220 + 1,
                  v62);
        spine::v3::PathAttachment::PathAttachment((spine::v3::PathAttachment *)lpsrc, (const spine::String *)&endptr_3);
        v102 = (spine::SpineExtension *)spine::v3::SkeletonDataLoader::assignVertexAttachment(
                                          this,
                                          (spine::v3::Attachment *)lpsrc,
                                          0);
        v103 = *((_QWORD *)this + 14);
        v104 = *(unsigned __int16 *)(*((_QWORD *)this + 11) + v103);
        *((_QWORD *)this + 14) = v103 + 2;
        v105 = *(_QWORD *)(lpsrc + 152);
        *(_QWORD *)(lpsrc + 144) = 0;
        v106 = *((_QWORD *)this + 11);
        v107 = *((_QWORD *)this + 14);
        if ( v105 >= v104 )
        {
          v112 = *(_QWORD *)(lpsrc + 160);
          v113 = 0;
        }
        else
        {
          v108 = *(_QWORD *)(lpsrc + 160);
          n8_17 = (int)(float)((float)(unsigned int)v104 * 1.75);
          if ( (unsigned int)n8_17 <= 8 )
            n8_17 = 8;
          n8_18 = n8_17;
          *(_QWORD *)(lpsrc + 152) = n8_17;
          InstanceEv_23 = spine::SpineExtension::getInstance(v102);
          v112 = (*(__int64 (__fastcall **)(__int64, __int64, __int64, const char *, __int64))(*(_QWORD *)InstanceEv_23
                                                                                             + 32LL))(
                   InstanceEv_23,
                   v108,
                   4 * n8_18,
                   "/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/proj.androidstudio/app/src/main/cp"
                   "p/../../../../../yuna/cocos2d/cocos/editor-support/spine/cpp/Vector.h",
                   126);
          v113 = *(_QWORD *)(lpsrc + 144);
          *(_QWORD *)(lpsrc + 160) = v112;
        }
        memcpy((void *)(v112 + 4 * v113), (const void *)(v106 + v107), 4 * v104);
        *(_QWORD *)(lpsrc + 144) = v104;
        v215 = *((_QWORD *)this + 11);
        v216 = *((_QWORD *)this + 14) + 4 * v104;
        *((_QWORD *)this + 14) = v216;
        LODWORD(v215) = *(unsigned __int8 *)(v215 + v216);
        *((_QWORD *)this + 14) = v216 + 1;
        *(_BYTE *)(lpsrc + 168) = (_DWORD)v215 != 0;
        v217 = *((_QWORD *)this + 14);
        LODWORD(v216) = *(unsigned __int8 *)(*((_QWORD *)this + 11) + v217);
        *((_QWORD *)this + 14) = v217 + 1;
        *(_BYTE *)(lpsrc + 169) = (_DWORD)v216 != 0;
        v75 = *((_QWORD *)this + 27);
        if ( !v75 )
          goto LABEL_200;
        break;
      case 5:
        lpsrc = spine::SpineObject::operator new(
                  (spine::SpineObject *)&word_38,
                  (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spine"
                                    "x/v3/SCSLoader_v3.cpp",
                  (const char *)&qword_228 + 3,
                  v62);
        spine::v3::PointAttachment::PointAttachment(
          (spine::v3::PointAttachment *)lpsrc,
          (const spine::String *)&endptr_3);
        spine::v3::SkeletonDataLoader::assignVertexAttachment(this, (spine::v3::Attachment *)lpsrc, 0);
        *(_DWORD *)(lpsrc + 44) = *(_DWORD *)(*((_QWORD *)this + 11) + *((_QWORD *)this + 14));
        v151 = *((_QWORD *)this + 11);
        v152 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v152;
        *(_DWORD *)(lpsrc + 48) = *(_DWORD *)(v151 + v152);
        v153 = *((_QWORD *)this + 11);
        v154 = *((_QWORD *)this + 14) + 4LL;
        *((_QWORD *)this + 14) = v154;
        *(_DWORD *)(lpsrc + 52) = *(_DWORD *)(v153 + v154);
        v75 = *((_QWORD *)this + 27);
        *((_QWORD *)this + 14) += 4LL;
        if ( !v75 )
          goto LABEL_200;
        break;
      case 6:
        lpsrc = spine::SpineObject::operator new(
                  (spine::SpineObject *)&qword_90,
                  (unsigned __int64)"/Users/dev/.jenkins/workspace/App-Epic7-Stove-Live/epic7/client/ur/yuna/yuna2d/spine"
                                    "x/v3/SCSLoader_v3.cpp",
                  (const char *)&qword_230 + 5,
                  v62);
        spine::v3::ClippingAttachment::ClippingAttachment(
          (spine::v3::ClippingAttachment *)lpsrc,
          (const spine::String *)&endptr_3);
        spine::v3::SkeletonDataLoader::assignVertexAttachment(this, (spine::v3::Attachment *)lpsrc, 0);
        v76 = *((_QWORD *)this + 14);
        v77 = v76 + 2;
        v78 = *(__int16 *)(*((_QWORD *)this + 11) + v76);
        *((_QWORD *)this + 14) = v77;
        *(_QWORD *)(lpsrc + 136) = *(_QWORD *)(*((_QWORD *)v4 + 12) + 8 * v78);
        v75 = *((_QWORD *)this + 27);
        if ( !v75 )
          goto LABEL_200;
        break;
      default:
        goto LABEL_200;
    }

LABEL_116:
    (*(void (__fastcall **)(__int64, __int64))(*(_QWORD *)v75 + 72LL))(v75, lpsrc);
    goto LABEL_200;
  }
LABEL_212:
  v313 = (spine::v3::MeshAttachment **)*((_QWORD *)this + 19);
  v314 = (spine::v3::MeshAttachment **)*((_QWORD *)this + 20);
  while ( v313 != v314 )
  {
    AttachmentEmRKNS_6StringE = *(spine::v3::Skin **)(*((_QWORD *)v4 + 16) + 8LL * *((int *)v313 + 3));
    if ( !AttachmentEmRKNS_6StringE )
      return AttachmentEmRKNS_6StringE;
    AttachmentEmRKNS_6StringE = (spine::v3::Skin *)spine::v3::Skin::getAttachment(
                                                     AttachmentEmRKNS_6StringE,
                                                     *((int *)v313 + 2),
                                                     (const spine::String *)(v313 + 2));
    if ( !AttachmentEmRKNS_6StringE )
      return AttachmentEmRKNS_6StringE;
    if ( *((_BYTE *)v313 + 48) )
      AttachmentEmRKNS_6StringE_1 = AttachmentEmRKNS_6StringE;
    else
      AttachmentEmRKNS_6StringE_1 = *v313;
    *((_QWORD *)*v313 + 15) = AttachmentEmRKNS_6StringE_1;
    spine::v3::MeshAttachment::setParentMesh(*v313, AttachmentEmRKNS_6StringE);
    spine::v3::MeshAttachment::updateUVs(*v313);
    v317 = *((_QWORD *)this + 27);
    if ( v317 )
      (*(void (__fastcall **)(__int64, spine::v3::MeshAttachment *))(*(_QWORD *)v317 + 72LL))(v317, *v313);
    v313 += 7;
  }
  return (spine::v3::Skin *)(&dword_0 + 1);
}