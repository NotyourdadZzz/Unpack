// https://games-popularity.com/overview/732032/sketchy-massage
// metadata
char __fastcall sub_7FFFFC4A1B80(_DWORD *a1, _DWORD *a2)
{
  __m128i si128; // xmm3
  __int64 v5; // rax
  __int64 v6; // rax
  __int128 *v7; // rcx
  __int64 v8; // r8
  __int64 v9; // rdx
  __int64 n3; // rax
  __int128 v11; // xmm0
  unsigned __int16 *v12; // r11
  __m128i v13; // xmm2
  __m128 v14; // xmm3
  unsigned int v15; // ebx
  __int64 v16; // rcx
  __m128i v17; // xmm0
  __m128i v18; // xmm0
  __m128i v19; // xmm0
  __m128i v20; // xmm0
  __m128i v21; // xmm0
  __m128i v22; // xmm0
  __m128i v23; // xmm0
  __m128i v24; // xmm0
  __m128i v25; // xmm0
  unsigned int v26; // eax
  __m128i v27; // xmm0
  __m128i v28; // xmm0
  __m128i v29; // xmm0
  __m128i v30; // xmm0
  __int64 v31; // rcx
  __int64 v32; // rax
  __int64 v33; // rbx
  __int64 v34; // rdi
  unsigned __int64 i; // rcx
  __int64 v36; // rax
  __int64 v37; // rbx
  __int64 v38; // rdi
  unsigned __int64 j; // rcx
  __int64 v40; // rax
  __int64 v41; // rbx
  __int64 v42; // rdi
  unsigned __int64 k; // rcx
  __int64 v44; // rax
  __int64 v45; // rbx
  __int64 v46; // rdi
  unsigned __int64 m; // rcx
  __int64 v48; // rax
  __int64 v49; // rbx
  __int64 v50; // rdi
  unsigned __int64 n; // rcx
  __int64 v52; // rax
  __int64 v53; // rbx
  __int64 v54; // rdi
  unsigned __int64 ii; // rcx
  __int64 v56; // rax
  __int64 v57; // rbx
  __int64 v58; // rdi
  unsigned __int64 jj; // rcx
  unsigned __int64 v60; // rdx
  unsigned __int64 v61; // rax
  __int64 v62; // rax
  _QWORD *v63; // r10
  int v64; // r8d
  __int64 v65; // rbx
  __int64 v66; // rdi
  __int64 v67; // rdx
  int *v68; // r9
  __int64 v69; // r11
  __int64 v70; // r11
  int v71; // eax
  __int64 v72; // r11
  __int64 v73; // r11
  unsigned int YQSY_; // [rsp+30h] [rbp-20h] BYREF
  __int128 v76; // [rsp+34h] [rbp-1Ch]

  si128 = _mm_load_si128((const __m128i *)&xmmword_7FFFFDB9B740);
  *(_DWORD *)((char *)&v76 + 1) = 1398412629;
  *(_DWORD *)((char *)&v76 + 5) = 1398232385;
  *(_DWORD *)((char *)&v76 + 10) = 1279918417;
  qmemcpy(&YQSY_, "YQSY", sizeof(YQSY_));
  YQSY_ = _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                       (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(dword_7FFFFDB9B6E0)),
                                       (__m128)_mm_cvtsi32_si128(YQSY_)));
  BYTE9(v76) = 69;
  HIWORD(v76) = 11096;
  *(_QWORD *)&v76 = __PAIR64__(
                      _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                   (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(dword_7FFFFDB9B700)),
                                                   (__m128)_mm_cvtsi32_si128(DWORD1(v76)))),
                      _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                   (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(dword_7FFFFDB9B6F0)),
                                                   (__m128)_mm_cvtsi32_si128(v76))));
  *((_QWORD *)&v76 + 1) = __PAIR64__(
                            _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                         (__m128)_mm_sub_epi8(
                                                                   si128,
                                                                   _mm_cvtsi32_si128(dword_7FFFFDB9B720)),
                                                         (__m128)_mm_cvtsi32_si128(HIDWORD(v76)))),
                            _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                         (__m128)_mm_sub_epi8(
                                                                   si128,
                                                                   _mm_cvtsi32_si128(dword_7FFFFDB9B710)),
                                                         (__m128)_mm_cvtsi32_si128(DWORD2(v76)))));
  v5 = sub_7FFFFC44DDC0((__int64)&YQSY_);
  qword_7FFFFDEBF3B8 = v5;
  if ( v5 )
  {
    v6 = sub_7FFFFC513760(384);
    v7 = (__int128 *)qword_7FFFFDEBF3B8;
    v8 = v6;
    qword_7FFFFDEBF4C8 = v6;
    v9 = v6;
    n3 = 3;
    do
    {
      v9 += 128;
      v11 = *v7;
      v7 += 8;
      *(_OWORD *)(v9 - 128) = v11;
      *(_OWORD *)(v9 - 112) = *(v7 - 7);
      *(_OWORD *)(v9 - 96) = *(v7 - 6);
      *(_OWORD *)(v9 - 80) = *(v7 - 5);
      *(_OWORD *)(v9 - 64) = *(v7 - 4);
      *(_OWORD *)(v9 - 48) = *(v7 - 3);
      *(_OWORD *)(v9 - 32) = *(v7 - 2);
      *(_OWORD *)(v9 - 16) = *(v7 - 1);
      --n3;
    }
    while ( n3 );
    v12 = (unsigned __int16 *)(v8 + 4);
    v13 = _mm_load_si128((const __m128i *)&xmmword_7FFFFD8C8C90);
    v14 = (__m128)_mm_load_si128((const __m128i *)&xmmword_7FFFFDB9B730);
    v15 = _mm_load_si128((const __m128i *)&xmmword_7FFFFDB9B750).m128i_u16[0];
    v16 = -4 - v8;
    do
    {
      v17 = (__m128i)_mm_and_ps(
                       (__m128)_mm_add_epi64(
                                 _mm_unpacklo_epi64(
                                   (__m128i)((unsigned __int64)v12 + v16),
                                   (__m128i)((unsigned __int64)v12 + v16)),
                                 v13),
                       v14);
      v18 = _mm_packus_epi16(v17, v17);
      v19 = _mm_packus_epi16(v18, v18);
      *(v12 - 2) = _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                (__m128)_mm_sub_epi8(_mm_cvtsi32_si128(v15), _mm_packus_epi16(v19, v19)),
                                                (__m128)_mm_cvtsi32_si128(*(v12 - 2))));
      v20 = (__m128i)_mm_and_ps(
                       (__m128)_mm_add_epi64(
                                 _mm_unpacklo_epi64(
                                   (__m128i)((unsigned __int64)v12 - 2 - v8),
                                   (__m128i)((unsigned __int64)v12 - 2 - v8)),
                                 v13),
                       v14);
      v21 = _mm_packus_epi16(v20, v20);
      v22 = _mm_packus_epi16(v21, v21);
      *(v12 - 1) = _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                (__m128)_mm_sub_epi8(_mm_cvtsi32_si128(v15), _mm_packus_epi16(v22, v22)),
                                                (__m128)_mm_cvtsi32_si128(*(v12 - 1))));
      v23 = (__m128i)_mm_and_ps(
                       (__m128)_mm_add_epi64(
                                 _mm_unpacklo_epi64(
                                   (__m128i)((unsigned __int64)v12 - v8),
                                   (__m128i)((unsigned __int64)v12 - v8)),
                                 v13),
                       v14);
      v24 = _mm_packus_epi16(v23, v23);
      v25 = _mm_packus_epi16(v24, v24);
      *v12 = _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                          (__m128)_mm_sub_epi8(_mm_cvtsi32_si128(v15), _mm_packus_epi16(v25, v25)),
                                          (__m128)_mm_cvtsi32_si128(*v12)));
      v26 = v12[1];
      v27 = _mm_unpacklo_epi64((__m128i)((unsigned __int64)v12 + 2 - v8), (__m128i)((unsigned __int64)v12 + 2 - v8));
      v12 += 4;
      v28 = (__m128i)_mm_and_ps((__m128)_mm_add_epi64(v27, v13), v14);
      v29 = _mm_packus_epi16(v28, v28);
      v30 = _mm_packus_epi16(v29, v29);
      *(v12 - 3) = _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                (__m128)_mm_sub_epi8(_mm_cvtsi32_si128(v15), _mm_packus_epi16(v30, v30)),
                                                (__m128)_mm_cvtsi32_si128(v26)));
    }
    while ( (unsigned __int64)v12 + v16 < 0x180 );
    v31 = *(int *)(v8 + 376);
    qword_7FFFFDEBF4E0 = v8;
    v32 = sub_7FFFFC513760(v31);
    v33 = qword_7FFFFDEBF4E0;
    v34 = v32;
    qword_7FFFFDEBF4A0 = v32;
    sub_7FFFFC539500(
      v32,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 40) - 52,
      *(int *)(qword_7FFFFDEBF4E0 + 376));
    for ( i = 0; i < *(int *)(v33 + 376); ++i )
      *(_BYTE *)(i + v34) ^= *(_BYTE *)(v33 + 376) + i - 89;
    v36 = sub_7FFFFC513760(*(int *)(v33 + 156));
    v37 = qword_7FFFFDEBF4E0;
    v38 = v36;
    qword_7FFFFDEBF4A8 = v36;
    sub_7FFFFC539500(
      v36,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 112) - 56,
      *(int *)(qword_7FFFFDEBF4E0 + 156));
    for ( j = 0; j < *(int *)(v37 + 156); ++j )
      *(_BYTE *)(j + v38) ^= j - *(_BYTE *)(v37 + 156) + 89;
    v40 = sub_7FFFFC513760(*(int *)(v37 + 88));
    v41 = qword_7FFFFDEBF4E0;
    v42 = v40;
    qword_7FFFFDEBF4B0 = v40;
    sub_7FFFFC539500(
      v40,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 260) - 40,
      *(int *)(qword_7FFFFDEBF4E0 + 88));
    for ( k = 0; k < *(int *)(v41 + 88); ++k )
      *(_BYTE *)(k + v42) ^= k - *(_BYTE *)(v41 + 88) + 89;
    v44 = sub_7FFFFC513760(*(int *)(v41 + 228));
    v45 = qword_7FFFFDEBF4E0;
    v46 = v44;
    qword_7FFFFDEBF4B8 = v44;
    sub_7FFFFC539500(
      v44,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 316) + 48,
      *(int *)(qword_7FFFFDEBF4E0 + 228));
    for ( m = 0; m < *(int *)(v45 + 228); ++m )
      *(_BYTE *)(m + v46) ^= *(_BYTE *)(v45 + 228) + m - 89;
    v48 = sub_7FFFFC513760(*(int *)(v45 + 340));
    v49 = qword_7FFFFDEBF4E0;
    v50 = v48;
    qword_7FFFFDEBF4C0 = v48;
    sub_7FFFFC539500(
      v48,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 28) - 28,
      *(int *)(qword_7FFFFDEBF4E0 + 340));
    for ( n = 0; n < *(int *)(v49 + 340); ++n )
      *(_BYTE *)(n + v50) ^= *(_BYTE *)(v49 + 340) + n - 89;
    v52 = sub_7FFFFC513760(*(int *)(v49 + 92));
    v53 = qword_7FFFFDEBF4E0;
    v54 = v52;
    qword_7FFFFDEBF4D0 = v52;
    sub_7FFFFC539500(
      v52,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 100) - 56,
      *(int *)(qword_7FFFFDEBF4E0 + 92));
    for ( ii = 0; ii < *(int *)(v53 + 92); ++ii )
      *(_BYTE *)(ii + v54) ^= ii - *(_BYTE *)(v53 + 92) + 89;
    v56 = sub_7FFFFC513760(*(int *)(v53 + 284));
    v57 = qword_7FFFFDEBF4E0;
    v58 = v56;
    qword_7FFFFDEBF4D8 = v56;
    sub_7FFFFC539500(
      v56,
      qword_7FFFFDEBF3B8 + *(_DWORD *)(qword_7FFFFDEBF4E0 + 24) - 24,
      *(int *)(qword_7FFFFDEBF4E0 + 284));
    for ( jj = 0; jj < *(int *)(v57 + 284); ++jj )
      *(_BYTE *)(jj + v58) ^= jj - *(_BYTE *)(v57 + 284) + 89;
    v60 = *(int *)(v57 + 144) / 0x28uLL;
    *a1 = v60;
    v61 = (unsigned __int64)*(int *)(v57 + 156) >> 6;
    dword_7FFFFDEBF2B8 = v60;
    *a2 = v61;
    qword_7FFFFDEBF2C0 = sub_7FFFFC433170((int)v60, 24);
    qword_7FFFFDEBF2E0 = sub_7FFFFC433170(*((int *)off_7FFFFDEBF4F8 + 12), 8);
    qword_7FFFFDEBF2E8 = sub_7FFFFC433170(*(int *)(qword_7FFFFDEBF4E0 + 292) / 0x58uLL, 8);
    qword_7FFFFDEBF2D0 = sub_7FFFFC433170(*(int *)(qword_7FFFFDEBF4E0 + 88) / 0x24uLL, 8);
    v62 = sub_7FFFFC433170(*((int *)off_7FFFFDEBF4F8 + 16), 8);
    v63 = off_7FFFFDEBF4F8;
    v64 = 0;
    qword_7FFFFDEBF2C8 = v62;
    if ( *((int *)off_7FFFFDEBF4F8 + 12) > 0 )
    {
      v65 = qword_7FFFFDEBF3B8;
      v66 = qword_7FFFFDEBF4E0;
      v67 = 0;
      do
      {
        v68 = *(int **)(v67 + v63[7]);
        switch ( *((_BYTE *)v68 + 10) )
        {
          case 1:
          case 2:
          case 3:
          case 4:
          case 5:
          case 6:
          case 7:
          case 8:
          case 9:
          case 0xA:
          case 0xB:
          case 0xC:
          case 0xD:
          case 0xE:
          case 0x11:
          case 0x12:
          case 0x16:
          case 0x18:
          case 0x19:
          case 0x1C:
            v69 = *v68;
            if ( (_DWORD)v69 == -1 )
            {
              v70 = 0;
              goto LABEL_30;
            }
            v71 = *(_DWORD *)(v66 + 300) - 40;
            v72 = 88 * v69;
            goto LABEL_29;
          case 0x13:
          case 0x1E:
            v73 = *v68;
            if ( (_DWORD)v73 == -1 )
            {
              v70 = 0;
            }
            else
            {
              v71 = *(_DWORD *)(v66 + 48) + 44;
              v72 = 16 * v73;
LABEL_29:
              v70 = v65 + v71 + v72;
            }
LABEL_30:
            *(_QWORD *)v68 = v70;
            break;
          default:
            break;
        }
        ++v64;
        v67 += 8;
      }
      while ( v64 < *((_DWORD *)v63 + 12) );
    }
    LOBYTE(v5) = 1;
  }
  return v5;
}