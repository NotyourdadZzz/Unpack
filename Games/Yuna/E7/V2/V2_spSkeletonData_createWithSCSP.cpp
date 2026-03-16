__int64 __fastcall spine::v2::spSkeletonData_createWithSCSP(
        unsigned int *a1,
        unsigned __int64 a2,
        __int64 a3,
        __int64 a4)
{
  __int64 v5; // x10
  __int64 v6; // x9
  int v7; // w11
  __int64 n88_1; // x19
  __int64 v9; // x20
  __int64 n88; // x2
  __int64 v11; // x26
  __int64 v12; // x23
  __int64 v13; // x24
  __int64 v14; // x28
  __int64 v15; // x25
  __int64 v16; // x27
  __int64 v17; // x21
  __int64 v18; // x22
  __int64 v19; // x8
  __int64 v20; // x19
  spine::v2::scsSkeletonData *v21; // x20
  __int64 v22; // x9
  __int64 v23; // x8
  __int64 v24; // x10
  char *v25; // x11
  char *v26; // x10
  __int64 v27; // x28
  __int64 v28; // x22
  __int64 v29; // x25
  __int64 v30; // x19
  __int64 v31; // x26
  __int64 v32; // x23
  unsigned __int16 *v33; // x11
  unsigned __int64 v34; // x27
  __int64 v35; // x24
  __int64 v36; // x21
  __int64 v37; // x10
  __int64 v38; // x8
  __int64 v39; // x9
  __int64 v40; // x11
  int v41; // w14
  __int64 v42; // x8
  __int64 v43; // x10
  char *v44; // x11
  char *v45; // x10
  __int64 v46; // x25
  __int64 v47; // x9
  char *v48; // x10
  char *v49; // x9
  __int64 v50; // x9
  char *v51; // x10
  char *v52; // x9
  __int64 v53; // kr00_8
  __int128 v54; // q1
  __int64 v55; // kr08_8
  int v56; // w10
  __int64 v57; // x9
  __int64 v58; // x10
  _QWORD *v59; // x23
  __int64 v60; // x1
  __int64 (__fastcall *v61)(char *, __int64); // x9
  __int64 v62; // x0
  int v63; // w8
  __int64 v64; // x19
  __int64 v65; // x8
  __int64 v66; // x0
  __int64 v67; // x8
  __int64 v68; // x9
  __int64 v69; // x8
  char *v70; // x9
  char *v71; // x8
  __int64 n0xFFFF; // x8
  __int64 v73; // x0
  int v74; // w8
  __int64 v75; // x19
  __int64 v76; // x8
  __int64 v77; // x10
  __int64 v78; // x11
  __int64 v79; // x9
  __int64 v80; // x8
  __int64 v81; // x9
  __int64 v82; // x0
  __int64 v83; // x24
  __int64 v84; // x8
  char *v85; // x9
  char *v86; // x8
  __int64 v87; // x9
  __int64 v88; // x0
  int v89; // w8
  __int64 v90; // x8
  __int64 v91; // x9
  __int64 v92; // x10
  __int64 v93; // x0
  int v94; // w8
  __int64 v95; // x19
  char *v96; // x10
  char *v97; // x9
  __int64 v98; // x9
  __int64 v99; // x8
  __int64 v100; // x9
  __int64 v101; // x0
  __int64 v102; // x8
  char *v103; // x9
  char *v104; // x8
  __int64 v105; // x8
  __int64 v106; // x11
  __int64 v107; // x10
  __int64 v108; // x9
  __int64 v109; // x9
  __int64 v110; // x10
  __int64 (__fastcall *v111)(char *, __int64); // x8
  __int64 v112; // x0
  __int64 v113; // x8
  __int64 v114; // x19
  unsigned int v115; // w28
  char **v116; // x0
  __int64 v117; // x8
  char *v118; // x9
  char *v119; // x8
  unsigned int v120; // w10
  __int64 v121; // x19
  unsigned int v122; // w22
  __int64 v123; // x0
  __int64 v124; // x25
  __int64 v125; // x8
  __int64 v126; // x9
  char *v127; // x10
  char *v128; // x9
  __int64 v129; // x9
  int n2; // w8
  __int64 v131; // x0
  __int64 v132; // x26
  __int64 v133; // x8
  char *v134; // x9
  char *v135; // x8
  __int64 v136; // x0
  __int64 v137; // x8
  char *v138; // x9
  char *v139; // x8
  __int64 v140; // x0
  __int64 v141; // x8
  char *v142; // x9
  char *v143; // x8
  __int64 v144; // x0
  __int64 v145; // x8
  char *v146; // x9
  char *v147; // x8
  __int64 v148; // x9
  size_t n_11; // x27
  void *dest_11; // x0
  __int64 v151; // x8
  __int64 v152; // x9
  __int64 v153; // x8
  __int64 v154; // x9
  char *v155; // x10
  char *v156; // x9
  __int64 v157; // x8
  size_t n_5; // x27
  void *dest_5; // x0
  __int64 v160; // x8
  __int64 v161; // x9
  __int64 v162; // x9
  size_t n_6; // x27
  void *dest_6; // x0
  __int64 v165; // x8
  __int64 v166; // x9
  __int64 v167; // x9
  size_t n_7; // x27
  void *dest_7; // x0
  __int64 v170; // x8
  __int64 v171; // x9
  __int64 v172; // x9
  size_t n_8; // x27
  void *dest_8; // x0
  __int64 v175; // x8
  __int64 v176; // x9
  __int64 v177; // x10
  size_t v178; // x8
  size_t n_9; // x27
  void *dest_9; // x0
  __int64 v181; // x8
  __int64 v182; // x9
  __int64 v183; // x9
  size_t v184; // x8
  __int128 v185; // q0
  int v186; // w10
  __int128 *v187; // x11
  __int128 v188; // q0
  __int128 v189; // q2
  __int128 v190; // q1
  __int64 v191; // x9
  size_t n_10; // x27
  void *dest_10; // x0
  __int64 v194; // x8
  __int64 v195; // x9
  __int64 v196; // x9
  __int64 v197; // x0
  float v198; // s0
  float v199; // s1
  float v200; // s2
  float v201; // s0
  float v202; // s3
  float v203; // s1
  int v204; // w9
  int v205; // w8
  __int64 v206; // x8
  __int64 v207; // x9
  __int64 v208; // x8
  __int64 v209; // x9
  char *v210; // x10
  char *v211; // x9
  __int64 v212; // x8
  __int64 v213; // x9
  char *v214; // x10
  char *v215; // x9
  __int64 v216; // x9
  __int128 v217; // q0
  __int128 v218; // q1
  __int128 v219; // q2
  __int128 *v220; // x10
  __int64 v221; // x11
  __int128 v222; // q0
  __int128 *v223; // x8
  __int128 v224; // q0
  __int128 v225; // q1
  __int128 v226; // q2
  __int128 v227; // q3
  __int64 v228; // x0
  _DWORD *v229; // x27
  __int64 v230; // x8
  size_t n; // x27
  void *dest; // x0
  __int64 v233; // x8
  __int64 v234; // x9
  int v235; // w9
  size_t n_1; // x27
  void *dest_1; // x0
  __int64 v238; // x8
  __int64 v239; // x9
  __int64 v240; // x10
  size_t v241; // x8
  size_t n_2; // x27
  void *dest_2; // x0
  __int64 v244; // x8
  __int64 v245; // x9
  __int64 v246; // x9
  size_t n_3; // x27
  void *dest_3; // x0
  __int64 v249; // x8
  __int64 v250; // x9
  __int64 v251; // x9
  size_t v252; // x8
  __int128 v253; // q0
  __int128 *v254; // x10
  __int128 v255; // q0
  __int128 v256; // q1
  __int128 v257; // q2
  __int64 v258; // x9
  size_t n_4; // x27
  void *dest_4; // x0
  __int64 v261; // x8
  __int64 v262; // x9
  __int64 v263; // x9
  __int64 Region; // x0
  float v265; // s0
  float v266; // s1
  float v267; // s2
  float v268; // s0
  float v269; // s3
  float v270; // s1
  int v271; // w9
  int v272; // w8
  __int64 v273; // x8
  __int64 v274; // x9
  __int64 v275; // x8
  __int64 *v276; // x24
  __int64 *v277; // x19
  unsigned int v278; // w8
  __int64 v279; // x0
  _QWORD *v280; // x27
  __int64 v281; // x8
  __int64 v282; // x9
  __int64 v283; // x8
  __int64 v284; // x9
  __int64 v285; // x9
  __int64 v286; // x8
  __int64 v287; // x0
  int v288; // w8
  __int64 v289; // x19
  char *v290; // x9
  char *v291; // x8
  char **v292; // x0
  __int64 v293; // x8
  char *v294; // x9
  char *v295; // x8
  __int64 v296; // x8
  __int64 v297; // x9
  __int64 v298; // x8
  __int128 v299; // q0
  __int64 v300; // x8
  __int64 v301; // x1
  __int64 v302; // x19
  unsigned int v304; // [xsp+8h] [xbp-158h]
  __int64 v305; // [xsp+10h] [xbp-150h]
  __int64 v306; // [xsp+18h] [xbp-148h]
  __int64 v307; // [xsp+20h] [xbp-140h]
  __int64 v308; // [xsp+20h] [xbp-140h]
  __int64 v309; // [xsp+28h] [xbp-138h]
  __int64 v310; // [xsp+28h] [xbp-138h]
  __int64 v311; // [xsp+30h] [xbp-130h]
  __int64 v312; // [xsp+30h] [xbp-130h]
  __int64 v313; // [xsp+38h] [xbp-128h]
  __int64 v314; // [xsp+38h] [xbp-128h]
  __int64 v315; // [xsp+40h] [xbp-120h]
  __int64 v316; // [xsp+40h] [xbp-120h]
  __int64 v317; // [xsp+48h] [xbp-118h]
  unsigned int v318; // [xsp+48h] [xbp-118h]
  unsigned int v319; // [xsp+50h] [xbp-110h]
  __int64 v320; // [xsp+50h] [xbp-110h]
  __int64 v321; // [xsp+58h] [xbp-108h]
  __int64 v322; // [xsp+68h] [xbp-F8h]
  __int64 v323; // [xsp+68h] [xbp-F8h]
  __int64 v324; // [xsp+68h] [xbp-F8h]
  __int64 v325; // [xsp+70h] [xbp-F0h]
  __int64 v326; // [xsp+70h] [xbp-F0h]
  __int64 v327; // [xsp+70h] [xbp-F0h]
  __int64 v328; // [xsp+78h] [xbp-E8h]
  __int64 v329; // [xsp+78h] [xbp-E8h]
  char **v330; // [xsp+78h] [xbp-E8h]
  __int64 v332; // [xsp+88h] [xbp-D8h]
  unsigned int v333; // [xsp+88h] [xbp-D8h]
  unsigned int v334; // [xsp+88h] [xbp-D8h]
  __int64 v335; // [xsp+90h] [xbp-D0h]
  __int64 v336; // [xsp+90h] [xbp-D0h]
  __int64 *v337; // [xsp+98h] [xbp-C8h] BYREF
  __int64 v338; // [xsp+A0h] [xbp-C0h] BYREF
  __int64 v339; // [xsp+A8h] [xbp-B8h]
  __int128 v340; // [xsp+B0h] [xbp-B0h] BYREF
  __int128 v341; // [xsp+C0h] [xbp-A0h]
  __int128 v342; // [xsp+D0h] [xbp-90h] BYREF
  __int128 v343; // [xsp+E0h] [xbp-80h]
  _OWORD v344[2]; // [xsp+F0h] [xbp-70h] BYREF
  __int128 v345; // [xsp+110h] [xbp-50h]
  __int128 v346; // [xsp+120h] [xbp-40h]
  __int128 v347; // [xsp+130h] [xbp-30h]
  __int64 v348; // [xsp+140h] [xbp-20h]
  __int64 v349; // [xsp+148h] [xbp-18h]

  v349 = *(_QWORD *)(_ReadStatusReg(TPIDR_EL0) + 40);
  v340 = 0u;
  v341 = 0u;
  v342 = 0u;
  v343 = 0u;
  sp_bin_stream::decode((__int64)&v340, a1, a2);


  v5 = *((_QWORD *)&v341 + 1);
  v321 = a4;
  v6 = *((_QWORD *)&v341 + 1);
  // signature "SCSP"
  if ( *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1)) == 1886610291
    && (*((_QWORD *)&v341 + 1) += 4LL,
        v7 = *(_DWORD *)(v340 + v5 + 4),
        v6 = v5 + 8,
        *((_QWORD *)&v341 + 1) = v5 + 8,
        v7 >= 1) )
  {
    n88_1 = *(int *)(v340 + v6);
    v9 = v5 + 12;
    v348 = 0;
    *((_QWORD *)&v341 + 1) = v5 + 12;
    v346 = 0u;
    v347 = 0u;
    // HeaderSize = min (size, 88)
    if ( (unsigned int)n88_1 >= 0x58 )
      n88 = 88;
    else
      n88 = (unsigned int)n88_1;

    v345 = 0u;
    memset(v344, 0, sizeof(v344));
    __memcpy_chk(v344, v340 + v5 + 12, n88, 88);
    v11 = WORD1(v346);
    v12 = DWORD1(v345);
    v13 = DWORD2(v345);
    v325 = WORD2(v346);
    v14 = WORD3(v346);
    v335 = DWORD2(v344[1]);
    v15 = HIDWORD(v345);
    v16 = WORD1(v347);
    v322 = (unsigned __int16)v346;
    v17 = WORD6(v347);
    v18 = (unsigned int)v345;
    v317 = (unsigned __int16)v347;
    v315 = HIWORD(v346);
    v332 = HIDWORD(v344[1]);
    v19 = v9 + n88_1;
    v20 = WORD5(v347);
    v313 = WORD2(v347);
    *((_QWORD *)&v341 + 1) = v19;
    v304 = WORD3(v347);
    v311 = WORD4(v347);
    v309 = WORD5(v346);
    v305 = WORD4(v346);
    v307 = WORD6(v346);
    v319 = HIWORD(v347);
    v306 = HIDWORD(v348);
    v328 = (unsigned int)v348;
    v21 = (spine::v2::scsSkeletonData *)operator new(120);
    spine::v2::scsSkeletonData::scsSkeletonData(
      v21,
      48LL * (unsigned int)v18
    + 56LL * (unsigned int)v335
    + 16 * v12
    + 40 * (v11 + v332)
    + 200LL * (unsigned int)v14
    + 32 * (v322 + v325 + v11 + v14)
    + 24LL * (unsigned int)v13
    + 176LL * (unsigned int)(v322 + v325)
    + 8 * (v332 + v335 + v18 + v12 + v13)
    + 144,
      40 * (v16 + v15 + v20 + v17)
    + 72LL * v304
    + 8 * v306
    + 48 * (v315 + v317 + v313 + v311 + v309 + v305 + v307)
    + 24LL * v319
    + v328);
    v22 = v340;
    v23 = *((_QWORD *)v21 + 9);
    v24 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
    *((_QWORD *)&v341 + 1) += 4LL;

    if ( (_DWORD)v24 == -1 )
    {
      v26 = 0;
    }
    else
    {
      if ( (v342 & 1) != 0 )
        v25 = (char *)v343;
      else
        v25 = (char *)&v342 + 1;
      v26 = &v25[v24];
    }

    *(_QWORD *)(v23 + 24) = v26;
    v46 = v23 + 16;
    v50 = *(unsigned int *)(v22 + *((_QWORD *)&v341 + 1));
    *((_QWORD *)&v341 + 1) += 4LL;
    if ( (_DWORD)v50 == -1 )
    {
      v52 = 0;
    }
    else
    {
      if ( (v342 & 1) != 0 )
        v51 = (char *)v343;
      else
        v51 = (char *)&v342 + 1;
      v52 = &v51[v50];
    }
    *(_QWORD *)(v23 + 16) = v52;
    v53 = *((_QWORD *)&v344[1] + 1);
    *(_QWORD *)(v23 + 32) = *(_QWORD *)&v344[0];
    v54 = *(_OWORD *)((char *)v344 + 8);
    *(_DWORD *)(v23 + 56) = v53;
    *(_DWORD *)(v23 + 144) = HIDWORD(v53);
    v55 = v345;
    *(_OWORD *)(v23 + 40) = v54;
    *(_DWORD *)(v23 + 72) = v55;
    *(_DWORD *)(v23 + 88) = HIDWORD(v55);
    v56 = HIDWORD(v345);
    *(_DWORD *)(v23 + 112) = DWORD2(v345);
    *(_DWORD *)(v23 + 128) = v56;
  }
  else
  {
    v27 = *(unsigned int *)(v340 + v6);
    *((_QWORD *)&v341 + 1) = v6 + 4;
    v28 = *(unsigned int *)(v340 + v6 + 4);
    *((_QWORD *)&v341 + 1) = v6 + 8;
    v29 = *(unsigned int *)(v340 + v6 + 8);
    *((_QWORD *)&v341 + 1) = v6 + 12;
    v30 = *(unsigned int *)(v340 + v6 + 12);
    *((_QWORD *)&v341 + 1) = v6 + 16;
    v31 = *(unsigned int *)(v340 + v6 + 16);
    *((_QWORD *)&v341 + 1) = v6 + 20;
    v32 = *(unsigned int *)(v340 + v6 + 20);
    *((_QWORD *)&v341 + 1) = v6 + 24;
    v33 = (unsigned __int16 *)(v340 + v6 + 32);
    v34 = *(_QWORD *)(v340 + v6 + 24);
    *((_QWORD *)&v341 + 1) = v6 + 32;
    v35 = v33[9];
    v36 = v33[10];
    v329 = *v33;
    v326 = v33[1];
    v323 = v33[2];
    v320 = v33[3];
    v316 = v33[4];
    v308 = v33[5];
    v314 = v33[6];
    v318 = v33[7];
    v312 = v33[8];
    *((_QWORD *)&v341 + 1) = v6 + 54;
    v37 = *(unsigned int *)(v340 + v6 + 54);
    *((_QWORD *)&v341 + 1) = v6 + 58;
    v336 = v37;
    LODWORD(v37) = *(unsigned __int16 *)(v340 + v6 + 58);
    *((_QWORD *)&v341 + 1) = v6 + 60;
    v38 = *(unsigned int *)(v340 + v6 + 60);
    v333 = v37;
    *((_QWORD *)&v341 + 1) = v6 + 64;
    v310 = v38;


    v21 = (spine::v2::scsSkeletonData *)operator new(120);
    spine::v2::scsSkeletonData::scsSkeletonData(
      v21,
      48LL * (unsigned int)v29
    + 56LL * (unsigned int)v27
    + 16 * v30
    + 40 * (WORD1(v34) + v28)
    + 200 * HIWORD(v34)
    + 32 * ((unsigned __int16)v34 + (unsigned __int64)WORD2(v34) + WORD1(v34) + HIWORD(v34))
    + 24LL * (unsigned int)v31
    + 176LL * ((unsigned __int16)v34 + (unsigned int)WORD2(v34))
    + 8 * (v28 + v27 + v29 + v30 + v31)
    + 144,
      40 * (v308 + v32 + v35 + v36)
    + 72LL * v318
    + 8 * v310
    + 48 * (v320 + v316 + v314 + v312 + v326 + v329 + v323)
    + 24LL * v333
    + v336);
    v39 = v340;
    v40 = *((_QWORD *)&v341 + 1);
    v41 = v29;
    v42 = *((_QWORD *)v21 + 9);
    *(_DWORD *)(v42 + 32) = *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1));
    *((_QWORD *)&v341 + 1) = v40 + 4;
    *(_DWORD *)(v42 + 36) = *(_DWORD *)(v39 + v40 + 4);
    *((_QWORD *)&v341 + 1) = v40 + 8;
    v43 = *(unsigned int *)(v39 + v40 + 8);
    *((_QWORD *)&v341 + 1) = v40 + 12;
    if ( (_DWORD)v43 == -1 )
    {
      v45 = 0;
    }
    else
    {
      if ( (v342 & 1) != 0 )
        v44 = (char *)v343;
      else
        v44 = (char *)&v342 + 1;
      v45 = &v44[v43];
    }
    *(_QWORD *)(v42 + 24) = v45;
    v46 = v42 + 16;
    v47 = *(unsigned int *)(v39 + *((_QWORD *)&v341 + 1));
    *((_QWORD *)&v341 + 1) += 4LL;
    if ( (_DWORD)v47 == -1 )
    {
      v49 = 0;
    }
    else
    {
      if ( (v342 & 1) != 0 )
        v48 = (char *)v343;
      else
        v48 = (char *)&v342 + 1;
      v49 = &v48[v47];
    }
    *(_QWORD *)(v42 + 16) = v49;
    *(_DWORD *)(v42 + 56) = v27;
    *(_DWORD *)(v42 + 144) = v28;
    *(_DWORD *)(v42 + 72) = v41;
    *(_DWORD *)(v42 + 88) = v30;
    *(_DWORD *)(v42 + 112) = v31;
    *(_DWORD *)(v42 + 128) = v32;
  }


  *(_QWORD *)(v46 + 8) = v21;
  v57 = *(int *)(v46 + 40);
  v59 = (_QWORD *)((char *)v21 + 48);
  v58 = *((_QWORD *)v21 + 6);
  *((_QWORD *)&v344[0] + 1) = 0;
  *(_QWORD *)&v344[1] = 0;
  v60 = 8 * v57;
  v61 = *(__int64 (__fastcall **)(char *, __int64))(v58 + 16);
  *(_QWORD *)&v344[0] = (char *)v344 + 8;
  v62 = v61((char *)v21 + 48, v60);
  v63 = *(_DWORD *)(v46 + 40);
  *(_QWORD *)(v46 + 48) = v62;

// bones
  if ( v63 >= 1 )
  {
    v64 = 0;
    do
    {
      v66 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 56);
      v67 = v340;
      *(_DWORD *)(v66 + 16) = *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      *(_DWORD *)(v66 + 20) = *(_DWORD *)(v67 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      *(_DWORD *)(v66 + 24) = *(_DWORD *)(v67 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      *(_DWORD *)(v66 + 28) = *(_DWORD *)(v67 + *((_QWORD *)&v341 + 1));
      v68 = *((_QWORD *)&v341 + 1);
      *((_QWORD *)&v341 + 1) += 4LL;
      *(_DWORD *)(v66 + 32) = *(_DWORD *)(v67 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) = v68 + 8;
      *(_DWORD *)(v66 + 36) = *(_DWORD *)(v67 + v68 + 8);
      *((_QWORD *)&v341 + 1) = v68 + 12;
      *(_DWORD *)(v66 + 40) = *(_DWORD *)(v67 + v68 + 12);
      *((_QWORD *)&v341 + 1) = v68 + 16;
      *(_DWORD *)(v66 + 44) = *(_DWORD *)(v67 + v68 + 16);
      *((_QWORD *)&v341 + 1) = v68 + 20;
      *(_DWORD *)(v66 + 48) = *(_DWORD *)(v67 + v68 + 20);
      *((_QWORD *)&v341 + 1) = v68 + 24;
      *(_DWORD *)(v66 + 52) = *(_DWORD *)(v67 + v68 + 24);
      *((_QWORD *)&v341 + 1) = v68 + 28;
      v69 = *(unsigned int *)(v67 + v68 + 28);
      *((_QWORD *)&v341 + 1) = v68 + 32;
      if ( (_DWORD)v69 == -1 )
      {
        v71 = 0;
      }
      else
      {
        if ( (v342 & 1) != 0 )
          v70 = (char *)v343;
        else
          v70 = (char *)&v342 + 1;
        v71 = &v70[v69];
      }
      *(_QWORD *)v66 = v71;
      n0xFFFF = *(unsigned __int16 *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 2LL;
      if ( n0xFFFF == 0xFFFF )
        v65 = 0;
      else
        v65 = *(_QWORD *)(*(_QWORD *)(v46 + 48) + 8 * n0xFFFF);
      *(_QWORD *)(v66 + 8) = v65;
      *(_QWORD *)(*(_QWORD *)(v46 + 48) + 8 * v64++) = v66;
    }
    while ( v64 < *(int *)(v46 + 40) );
  }
  v73 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 8LL * *(int *)(v46 + 128));
  v74 = *(_DWORD *)(v46 + 128);
  *(_QWORD *)(v46 + 136) = v73;

// slots
  if ( v74 >= 1 )
  {
    v75 = 0;
    do
    {
      v82 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 40);
      v83 = v82;
      v84 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      if ( (_DWORD)v84 == -1 )
      {
        v86 = 0;
      }
      else
      {
        if ( (v342 & 1) != 0 )
          v85 = (char *)v343;
        else
          v85 = (char *)&v342 + 1;
        v86 = &v85[v84];
      }
      *(_QWORD *)v82 = v86;
      *(_DWORD *)(v82 + 8) = *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1));
      v87 = *(_QWORD *)v21;
      *((_QWORD *)&v341 + 1) += 4LL;
      v88 = (*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(v87 + 16))(v21, 8LL * *(int *)(v82 + 8));
      v89 = *(_DWORD *)(v83 + 8);
      *(_QWORD *)(v83 + 16) = v88;
      if ( v89 >= 1 )
      {
        v90 = 0;
        do
        {
          v91 = *(unsigned __int16 *)(v340 + *((_QWORD *)&v341 + 1));
          v92 = *(_QWORD *)(v46 + 48);
          *((_QWORD *)&v341 + 1) += 2LL;
          *(_QWORD *)(*(_QWORD *)(v83 + 16) + 8 * v90++) = *(_QWORD *)(v92 + 8 * v91);
        }
        while ( v90 < *(int *)(v83 + 8) );
      }
      v76 = v340;
      v77 = *(_QWORD *)(v46 + 48);
      v78 = *(unsigned __int16 *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 2LL;
      *(_QWORD *)(v83 + 24) = *(_QWORD *)(v77 + 8 * v78);
      v79 = *((_QWORD *)&v341 + 1);
      *(_DWORD *)(v83 + 32) = *(_DWORD *)(v76 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) = v79 + 4;
      *(_DWORD *)(v83 + 36) = *(_DWORD *)(v76 + v79 + 4);
      v80 = v79 + 8;
      v81 = *(_QWORD *)(v46 + 136);
      *((_QWORD *)&v341 + 1) = v80;
      *(_QWORD *)(v81 + 8 * v75++) = v83;
    }
    while ( v75 < *(int *)(v46 + 128) );
  }


  v93 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 8LL * *(int *)(v46 + 56));
  v94 = *(_DWORD *)(v46 + 56);
  *(_QWORD *)(v46 + 64) = v93;

// skins
  if ( v94 >= 1 )
  {
    v95 = 0;
    do
    {
      v101 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 48);
      v102 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      if ( (_DWORD)v102 == -1 )
      {
        v104 = 0;
      }
      else
      {
        if ( (v342 & 1) != 0 )
          v103 = (char *)v343;
        else
          v103 = (char *)&v342 + 1;
        v104 = &v103[v102];
      }
      *(_QWORD *)v101 = v104;
      v105 = v340;
      v106 = *(_QWORD *)(v46 + 48);
      v107 = *(unsigned __int16 *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 2LL;
      *(_QWORD *)(v101 + 8) = *(_QWORD *)(v106 + 8 * v107);
      v108 = *(unsigned int *)(v105 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      if ( (_DWORD)v108 == -1 )
      {
        v97 = 0;
      }
      else
      {
        if ( (v342 & 1) != 0 )
          v96 = (char *)v343;
        else
          v96 = (char *)&v342 + 1;
        v97 = &v96[v108];
      }
      *(_QWORD *)(v101 + 16) = v97;
      *(_DWORD *)(v101 + 24) = *(_DWORD *)(v105 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      *(_DWORD *)(v101 + 28) = *(_DWORD *)(v105 + *((_QWORD *)&v341 + 1));
      v98 = *((_QWORD *)&v341 + 1);
      *((_QWORD *)&v341 + 1) += 4LL;
      *(_DWORD *)(v101 + 32) = *(_DWORD *)(v105 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) = v98 + 8;
      *(_DWORD *)(v101 + 36) = *(_DWORD *)(v105 + v98 + 8);
      *((_QWORD *)&v341 + 1) = v98 + 12;
      *(_DWORD *)(v101 + 40) = *(_DWORD *)(v105 + v98 + 12);
      v99 = v98 + 16;
      v100 = *(_QWORD *)(v46 + 64);
      *((_QWORD *)&v341 + 1) = v99;
      *(_QWORD *)(v100 + 8 * v95++) = v101;
    }
    while ( v95 < *(int *)(v46 + 56) );
  }
  v109 = *(int *)(v46 + 72);
  v110 = *v59;
  v338 = 0;
  v339 = 0;
  v111 = *(__int64 (__fastcall **)(char *, __int64))(v110 + 16);
  v337 = &v338;
  v112 = v111((char *)v21 + 48, 8 * v109);
  LODWORD(v113) = *(_DWORD *)(v46 + 72);
  *(_QWORD *)(v46 + 80) = v112;


  if ( (int)v113 >= 1 )
  {
    v114 = 0;
    v115 = 0;
    v324 = v46;
    while ( 1 )
    {
      v116 = (char **)(*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 16);
      *(_QWORD *)(*(_QWORD *)(v46 + 80) + 8 * v114) = v116;
      v117 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      if ( (_DWORD)v117 == -1 )
      {
        v119 = 0;
      }
      else
      {
        v118 = (char *)&v342 + 1;
        if ( (v342 & 1) != 0 )
          v118 = (char *)v343;
        v119 = &v118[v117];
      }
      *v116 = v119;
      v327 = v114;
      v120 = *(unsigned __int16 *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 2LL;
      v334 = v120;
      if ( v120 )
        break;
LABEL_74:
      v46 = v324;
      v113 = *(int *)(v324 + 72);
      v114 = v327 + 1;
      if ( v327 + 1 >= v113 )
        goto LABEL_173;
    }
    v121 = 0;
    v122 = 0;
    v330 = v116;
    while ( 1 )
    {
      v123 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 32);
      v124 = v123;
      *(_QWORD *)(v123 + 24) = 0;
      if ( v121 )
        *(_QWORD *)(v121 + 24) = v123;
      else
        v330[1] = (char *)v123;
      v125 = v340;
      v126 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      if ( (_DWORD)v126 == -1 )
      {
        v128 = 0;
      }
      else
      {
        v127 = (char *)&v342 + 1;
        if ( (v342 & 1) != 0 )
          v127 = (char *)v343;
        v128 = &v127[v126];
      }
      *(_QWORD *)(v123 + 8) = v128;
      *(_DWORD *)v123 = *(_DWORD *)(v125 + *((_QWORD *)&v341 + 1));
      v129 = *((_QWORD *)&v341 + 1) + 8LL;
      *((_QWORD *)&v341 + 1) += 4LL;
      n2 = *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) = v129;
      if ( n2 > 1 )
      {
        if ( n2 == 2 )
        {
          v144 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 176);
          v132 = v144;
          *(_DWORD *)(v144 + 8) = 2;
          v145 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v145 == -1 )
          {
            v147 = 0;
          }
          else
          {
            v146 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v146 = (char *)v343;
            v147 = &v146[v145];
          }
          *(_QWORD *)v144 = v147;
          v212 = v340;
          v213 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v213 == -1 )
          {
            v215 = 0;
          }
          else
          {
            v214 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v214 = (char *)v343;
            v215 = &v214[v213];
          }
          *(_QWORD *)(v144 + 24) = v215;
          v230 = *(int *)(v212 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v144 + 32) = v230;
          n = 4 * v230;
          dest = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                           v21,
                           4 * v230);
          v233 = v340;
          v234 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 40) = dest;
          memcpy(dest, (const void *)(v233 + v234), n);
          *((_QWORD *)&v341 + 1) += n;
          v235 = *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v132 + 48) = v235;
          n_1 = 4LL * *(int *)(v132 + 32);
          dest_1 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, size_t))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             n_1);
          v238 = v340;
          v239 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 64) = dest_1;
          memcpy(dest_1, (const void *)(v238 + v239), n_1);
          v240 = *(_QWORD *)v21;
          v241 = *((_QWORD *)&v341 + 1) + n_1;
          n_2 = 4LL * *(int *)(v132 + 32);
          *((_QWORD *)&v341 + 1) = v241;
          dest_2 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, size_t))(v240 + 16))(v21, n_2);
          v244 = v340;
          v245 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 56) = dest_2;
          memcpy(dest_2, (const void *)(v244 + v245), n_2);
          *((_QWORD *)&v341 + 1) += n_2;
          v246 = *(int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v132 + 72) = v246;
          n_3 = 4 * v246;
          dest_3 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             4 * v246);
          v249 = v340;
          v250 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 80) = dest_3;
          memcpy(dest_3, (const void *)(v249 + v250), n_3);
          v251 = v340;
          v252 = *((_QWORD *)&v341 + 1) + n_3;
          *((_QWORD *)&v341 + 1) = v252;
          v253 = *(_OWORD *)(v340 + v252);
          *((_QWORD *)&v341 + 1) = v252 + 16;
          v254 = (__int128 *)(v340 + v252 + 16);
          *(_OWORD *)(v132 + 88) = v253;
          v255 = *v254;
          v256 = v254[1];
          v257 = *(__int128 *)((char *)v254 + 28);
          *((_QWORD *)&v341 + 1) = v252 + 60;
          *(_OWORD *)(v132 + 112) = v255;
          *(_OWORD *)(v132 + 128) = v256;
          *(_OWORD *)(v132 + 140) = v257;
          v258 = *(int *)(v251 + v252 + 60);
          *((_QWORD *)&v341 + 1) = v252 + 64;
          *(_DWORD *)(v132 + 156) = v258;
          n_4 = 4 * v258;
          dest_4 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             4 * v258);
          v261 = v340;
          v262 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 160) = dest_4;
          memcpy(dest_4, (const void *)(v261 + v262), n_4);
          *((_QWORD *)&v341 + 1) += n_4;
          v263 = *(_QWORD *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 8LL;
          *(_QWORD *)(v132 + 168) = v263;
          if ( a3 && (Region = spine::v2::spAtlas_findRegion(*(_QWORD *)(a3 + 24), *(char **)(v132 + 24))) != 0 )
          {
            *(_QWORD *)(v132 + 104) = Region;
            v265 = *(float *)(Region + 24);
            *(float *)(v132 + 136) = v265;
            v266 = *(float *)(Region + 28);
            *(float *)(v132 + 140) = v266;
            v267 = *(float *)(Region + 32);
            *(float *)(v132 + 144) = v267;
            v268 = v267 - v265;
            v269 = *(float *)(Region + 36);
            *(float *)(v132 + 148) = v269;
            v270 = v269 - v266;
            v271 = *(_DWORD *)(Region + 60);
            *(_DWORD *)(v132 + 152) = v271;
            *(_DWORD *)(v132 + 112) = *(_DWORD *)(Region + 40);
            *(_DWORD *)(v132 + 116) = *(_DWORD *)(Region + 44);
            *(_DWORD *)(v132 + 120) = *(_DWORD *)(Region + 16);
            *(_DWORD *)(v132 + 124) = *(_DWORD *)(Region + 20);
            *(_DWORD *)(v132 + 128) = *(_DWORD *)(Region + 48);
            v272 = *(_DWORD *)(v132 + 32);
            *(_DWORD *)(v132 + 132) = *(_DWORD *)(Region + 52);
            if ( v271 )
            {
              if ( v272 >= 1 )
              {
                v273 = 0;
                do
                {
                  v274 = 4 * v273;
                  v273 += 2;
                  *(float *)(*(_QWORD *)(v132 + 64) + v274) = *(float *)(v132 + 136)
                                                            + (float)(*(float *)(*(_QWORD *)(v132 + 56) + v274 + 4)
                                                                    * v268);
                  *(float *)(*(_QWORD *)(v132 + 64) + v274 + 4) = (float)(v270 + *(float *)(v132 + 140))
                                                                - (float)(*(float *)(*(_QWORD *)(v132 + 56) + v274)
                                                                        * v270);
                }
                while ( v273 < *(int *)(v132 + 32) );
              }
            }
            else if ( v272 >= 1 )
            {
              v281 = 0;
              do
              {
                v282 = 4 * v281;
                v281 += 2;
                *(float *)(*(_QWORD *)(v132 + 64) + v282) = *(float *)(v132 + 136)
                                                          + (float)(*(float *)(*(_QWORD *)(v132 + 56) + v282) * v268);
                *(float *)(*(_QWORD *)(v132 + 64) + v282 + 4) = *(float *)(v132 + 140)
                                                              + (float)(*(float *)(*(_QWORD *)(v132 + 56) + v282 + 4)
                                                                      * v270);
              }
              while ( v281 < *(int *)(v132 + 32) );
            }
          }
          else
          {
            *(_QWORD *)(v132 + 104) = 0;
          }
          goto LABEL_154;
        }
        if ( n2 == 3 )
        {
          v136 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 200);
          *(_QWORD *)(v136 + 128) = 0;
          v132 = v136;
          *(_DWORD *)(v136 + 8) = 3;
          v137 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v137 == -1 )
          {
            v139 = 0;
          }
          else
          {
            v138 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v138 = (char *)v343;
            v139 = &v138[v137];
          }
          *(_QWORD *)v136 = v139;
          v153 = v340;
          v154 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v154 == -1 )
          {
            v156 = 0;
          }
          else
          {
            v155 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v155 = (char *)v343;
            v156 = &v155[v154];
          }
          *(_QWORD *)(v136 + 24) = v156;
          v157 = *(int *)(v153 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v136 + 32) = v157;
          n_5 = 4 * v157;
          dest_5 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             4 * v157);
          v160 = v340;
          v161 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 40) = dest_5;
          memcpy(dest_5, (const void *)(v160 + v161), n_5);
          *((_QWORD *)&v341 + 1) += n_5;
          v162 = *(int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v132 + 48) = v162;
          n_6 = 4 * v162;
          dest_6 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             4 * v162);
          v165 = v340;
          v166 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 56) = dest_6;
          memcpy(dest_6, (const void *)(v165 + v166), n_6);
          *((_QWORD *)&v341 + 1) += n_6;
          v167 = *(int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v132 + 64) = v167;
          n_7 = 4 * v167;
          dest_7 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             4 * v167);
          v170 = v340;
          v171 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 72) = dest_7;
          memcpy(dest_7, (const void *)(v170 + v171), n_7);
          *((_QWORD *)&v341 + 1) += n_7;
          v172 = *(int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          *(_DWORD *)(v132 + 80) = v172;
          n_8 = 4 * v172;
          dest_8 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                             v21,
                             4 * v172);
          v175 = v340;
          v176 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 88) = dest_8;
          memcpy(dest_8, (const void *)(v175 + v176), n_8);
          v177 = *(_QWORD *)v21;
          v178 = *((_QWORD *)&v341 + 1) + n_8;
          n_9 = 4LL * *(int *)(v132 + 80);
          *((_QWORD *)&v341 + 1) = v178;
          dest_9 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, size_t))(v177 + 16))(v21, n_9);
          v181 = v340;
          v182 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 96) = dest_9;
          memcpy(dest_9, (const void *)(v181 + v182), n_9);
          v183 = v340;
          v184 = *((_QWORD *)&v341 + 1) + n_9;
          *((_QWORD *)&v341 + 1) = v184;
          v185 = *(_OWORD *)(v340 + v184);
          v186 = *(_DWORD *)(v340 + v184 + 16);
          *((_QWORD *)&v341 + 1) = v184 + 20;
          v187 = (__int128 *)(v340 + v184 + 20);
          *(_OWORD *)(v132 + 104) = v185;
          *(_DWORD *)(v132 + 120) = v186;
          v189 = *v187;
          v188 = v187[1];
          v190 = *(__int128 *)((char *)v187 + 28);
          *((_QWORD *)&v341 + 1) = v184 + 64;
          *(_OWORD *)(v132 + 152) = v188;
          *(_OWORD *)(v132 + 164) = v190;
          *(_OWORD *)(v132 + 136) = v189;
          v191 = *(int *)(v183 + v184 + 64);
          *((_QWORD *)&v341 + 1) = v184 + 68;
          *(_DWORD *)(v132 + 180) = v191;
          n_10 = 4 * v191;
          dest_10 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, __int64))(*(_QWORD *)v21 + 16LL))(
                              v21,
                              4 * v191);
          v194 = v340;
          v195 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 184) = dest_10;
          memcpy(dest_10, (const void *)(v194 + v195), n_10);
          *((_QWORD *)&v341 + 1) += n_10;
          v196 = *(_QWORD *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 8LL;
          *(_QWORD *)(v132 + 192) = v196;
          if ( a3 && (v197 = spine::v2::spAtlas_findRegion(*(_QWORD *)(a3 + 24), *(char **)(v132 + 24))) != 0 )
          {
            *(_QWORD *)(v132 + 128) = v197;
            v198 = *(float *)(v197 + 24);
            *(float *)(v132 + 160) = v198;
            v199 = *(float *)(v197 + 28);
            *(float *)(v132 + 164) = v199;
            v200 = *(float *)(v197 + 32);
            *(float *)(v132 + 168) = v200;
            v201 = v200 - v198;
            v202 = *(float *)(v197 + 36);
            *(float *)(v132 + 172) = v202;
            v203 = v202 - v199;
            v204 = *(_DWORD *)(v197 + 60);
            *(_DWORD *)(v132 + 176) = v204;
            *(_DWORD *)(v132 + 136) = *(_DWORD *)(v197 + 40);
            *(_DWORD *)(v132 + 140) = *(_DWORD *)(v197 + 44);
            *(_DWORD *)(v132 + 144) = *(_DWORD *)(v197 + 16);
            *(_DWORD *)(v132 + 148) = *(_DWORD *)(v197 + 20);
            *(_DWORD *)(v132 + 152) = *(_DWORD *)(v197 + 48);
            v205 = *(_DWORD *)(v132 + 80);
            *(_DWORD *)(v132 + 156) = *(_DWORD *)(v197 + 52);
            if ( v204 )
            {
              if ( v205 >= 1 )
              {
                v206 = 0;
                do
                {
                  v207 = 4 * v206;
                  v206 += 2;
                  *(float *)(*(_QWORD *)(v132 + 96) + v207) = *(float *)(v132 + 160)
                                                            + (float)(*(float *)(*(_QWORD *)(v132 + 88) + v207 + 4)
                                                                    * v201);
                  *(float *)(*(_QWORD *)(v132 + 96) + v207 + 4) = (float)(v203 + *(float *)(v132 + 164))
                                                                - (float)(*(float *)(*(_QWORD *)(v132 + 88) + v207)
                                                                        * v203);
                }
                while ( v206 < *(int *)(v132 + 80) );
              }
            }
            else if ( v205 >= 1 )
            {
              v283 = 0;
              do
              {
                v284 = 4 * v283;
                v283 += 2;
                *(float *)(*(_QWORD *)(v132 + 96) + v284) = *(float *)(v132 + 160)
                                                          + (float)(*(float *)(*(_QWORD *)(v132 + 88) + v284) * v201);
                *(float *)(*(_QWORD *)(v132 + 96) + v284 + 4) = *(float *)(v132 + 164)
                                                              + (float)(*(float *)(*(_QWORD *)(v132 + 88) + v284 + 4)
                                                                      * v203);
              }
              while ( v283 < *(int *)(v132 + 80) );
            }
          }
          else
          {
            *(_QWORD *)(v132 + 128) = 0;
          }
          goto LABEL_154;
        }
      }
      else
      {
        if ( !n2 )
        {
          v140 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 176);
          *(_DWORD *)(v140 + 8) = 0;
          v132 = v140;
          v141 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v141 == -1 )
          {
            v143 = 0;
          }
          else
          {
            v142 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v142 = (char *)v343;
            v143 = &v142[v141];
          }
          *(_QWORD *)v140 = v143;
          v208 = v340;
          v209 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v209 == -1 )
          {
            v211 = 0;
          }
          else
          {
            v210 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v210 = (char *)v343;
            v211 = &v210[v209];
          }
          *(_QWORD *)(v140 + 24) = v211;
          v216 = *((_QWORD *)&v341 + 1);
          v217 = *(_OWORD *)(v208 + *((_QWORD *)&v341 + 1));
          v218 = *(_OWORD *)(v208 + *((_QWORD *)&v341 + 1) + 16);
          v219 = *(_OWORD *)(v208 + *((_QWORD *)&v341 + 1) + 28);
          *((_QWORD *)&v341 + 1) += 44LL;
          v220 = (__int128 *)(v208 + *((_QWORD *)&v341 + 1));
          *(_OWORD *)(v140 + 32) = v217;
          *(_OWORD *)(v140 + 48) = v218;
          *(_OWORD *)(v140 + 60) = v219;
          v221 = *((_QWORD *)v220 + 2);
          v222 = *v220;
          *((_QWORD *)&v341 + 1) = v216 + 68;
          v223 = (__int128 *)(v208 + v216 + 68);
          *(_QWORD *)(v140 + 104) = v221;
          *(_OWORD *)(v140 + 88) = v222;
          v225 = v223[2];
          v224 = v223[3];
          v226 = *v223;
          v227 = v223[1];
          *((_QWORD *)&v341 + 1) = v216 + 132;
          *(_OWORD *)(v140 + 144) = v225;
          *(_OWORD *)(v140 + 160) = v224;
          *(_OWORD *)(v140 + 112) = v226;
          *(_OWORD *)(v140 + 128) = v227;
          if ( a3
            && (v228 = spine::v2::spAtlas_findRegion(*(_QWORD *)(a3 + 24), *(char **)(v140 + 24)),
                (v229 = (_DWORD *)v228) != 0) )
          {
            *(_QWORD *)(v132 + 80) = v228;
            spine::v2::spRegionAttachment_setUVs(
              v132,
              *(unsigned int *)(v228 + 60),
              *(float *)(v228 + 24),
              *(float *)(v228 + 28),
              *(float *)(v228 + 32),
              *(float *)(v228 + 36));
            *(_DWORD *)(v132 + 88) = v229[10];
            *(_DWORD *)(v132 + 92) = v229[11];
            *(_DWORD *)(v132 + 96) = v229[4];
            *(_DWORD *)(v132 + 100) = v229[5];
            *(_DWORD *)(v132 + 104) = v229[12];
            *(_DWORD *)(v132 + 108) = v229[13];
          }
          else
          {
            *(_QWORD *)(v132 + 80) = 0;
          }
          goto LABEL_154;
        }
        if ( n2 == 1 )
        {
          v131 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 40);
          v132 = v131;
          *(_DWORD *)(v131 + 8) = 1;
          v133 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
          *((_QWORD *)&v341 + 1) += 4LL;
          if ( (_DWORD)v133 == -1 )
          {
            v135 = 0;
          }
          else
          {
            v134 = (char *)&v342 + 1;
            if ( (v342 & 1) != 0 )
              v134 = (char *)v343;
            v135 = &v134[v133];
          }
          *(_QWORD *)v131 = v135;
          *(_DWORD *)(v131 + 24) = *(_DWORD *)(v340 + *((_QWORD *)&v341 + 1));
          v148 = *(_QWORD *)v21;
          *((_QWORD *)&v341 + 1) += 4LL;
          n_11 = 4LL * *(int *)(v131 + 24);
          dest_11 = (void *)(*(__int64 (__fastcall **)(spine::v2::scsSkeletonData *, size_t))(v148 + 16))(v21, n_11);
          v151 = v340;
          v152 = *((_QWORD *)&v341 + 1);
          *(_QWORD *)(v132 + 32) = dest_11;
          memcpy(dest_11, (const void *)(v151 + v152), n_11);
          *((_QWORD *)&v341 + 1) += n_11;
LABEL_154:
          *(_QWORD *)(v132 + 16) = &spine::v2::_scsAttachmentVtable;
          *(_QWORD *)(v124 + 16) = v132;
          goto LABEL_155;
        }
      }
      v132 = *(_QWORD *)(v123 + 16);
LABEL_155:
      v275 = v338;
      v276 = &v338;
      v277 = &v338;
      if ( v338 )
      {
        while ( 1 )
        {
          while ( 1 )
          {
            v277 = (__int64 *)v275;
            v278 = *(_DWORD *)(v275 + 32);
            if ( v115 >= v278 )
              break;
            v275 = *v277;
            v276 = v277;
            if ( !*v277 )
              goto LABEL_162;
          }
          if ( v278 >= v115 )
            break;
          v275 = v277[1];
          if ( !v275 )
          {
            v276 = v277 + 1;
            goto LABEL_162;
          }
        }
        v280 = v277;
      }
      else
      {
LABEL_162:
        v279 = operator new(48);
        *(_DWORD *)(v279 + 32) = v115;
        v280 = (_QWORD *)v279;
        *(_QWORD *)(v279 + 40) = 0;
        *(_QWORD *)v279 = 0;
        *(_QWORD *)(v279 + 8) = 0;
        *(_QWORD *)(v279 + 16) = v277;
        *v276 = v279;
        if ( *v337 )
          v337 = (__int64 *)*v337;
        sub_A11B2C(v338);
        ++v339;
      }
      ++v122;
      ++v115;
      v121 = v124;
      v280[5] = v132;
      if ( v122 >= v334 )
        goto LABEL_74;
    }
  }
LABEL_173:
  v285 = *(int *)(v340 + *((_QWORD *)&v341 + 1));
  *((_QWORD *)&v341 + 1) += 4LL;
  if ( (_DWORD)v113 )
    v286 = *(_QWORD *)(*(_QWORD *)(v46 + 80) + 8 * v285);
  else
    v286 = 0;
  *(_QWORD *)(v46 + 88) = v286;
  v287 = (*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 8LL * *(int *)(v46 + 96));
  v288 = *(_DWORD *)(v46 + 96);
  *(_QWORD *)(v46 + 104) = v287;


  if ( v288 >= 1 )
  {
    v289 = 0;
    do
    {
      v292 = (char **)(*(__int64 (__fastcall **)(_QWORD *, __int64))(*v59 + 16LL))((_QWORD *)v21 + 6, 24);
      v293 = *(unsigned int *)(v340 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) += 4LL;
      if ( (_DWORD)v293 == -1 )
      {
        v295 = 0;
      }
      else
      {
        if ( (v342 & 1) != 0 )
          v294 = (char *)v343;
        else
          v294 = (char *)&v342 + 1;
        v295 = &v294[v293];
      }
      *v292 = v295;
      v296 = v340;
      v292[1] = *(char **)(v340 + *((_QWORD *)&v341 + 1));
      v297 = *((_QWORD *)&v341 + 1) + 12LL;
      *((_QWORD *)&v341 + 1) += 8LL;
      v298 = *(unsigned int *)(v296 + *((_QWORD *)&v341 + 1));
      *((_QWORD *)&v341 + 1) = v297;
      if ( (_DWORD)v298 == -1 )
      {
        v291 = 0;
      }
      else
      {
        if ( (v342 & 1) != 0 )
          v290 = (char *)v343;
        else
          v290 = (char *)&v342 + 1;
        v291 = &v290[v298];
      }
      v292[2] = v291;
      *(_QWORD *)(*(_QWORD *)(v46 + 104) + 8 * v289++) = v292;
    }
    while ( v289 < *(int *)(v46 + 96) );
  }

// readAnimation
  spine::v2::readAnimation(v46, &v340, v21, &v337, v321);

  if ( (*((_BYTE *)v21 + 96) & 1) != 0 )
    operator delete(*((_QWORD *)v21 + 14), *((_QWORD *)v21 + 12) & 0xFFFFFFFFFFFFFFFELL);
  v299 = v342;
  v300 = v343;
  v301 = v338;
  v302 = *((_QWORD *)v21 + 9);
  LOWORD(v342) = 0;
  *((_OWORD *)v21 + 6) = v299;
  *((_QWORD *)v21 + 14) = v300;
  sub_D74284(&v337, v301);
  sub_D74228(v344, *((_QWORD *)&v344[0] + 1));
  if ( (v342 & 1) != 0 )
    operator delete(v343, v342 & 0xFFFFFFFFFFFFFFFELL);
  if ( (_QWORD)v340 )
  {
    *((_QWORD *)&v340 + 1) = v340;
    operator delete(v340, v341 - v340);
  }
  return v302 + 16;
}