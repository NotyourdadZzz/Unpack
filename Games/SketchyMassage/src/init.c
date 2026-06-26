// https://games-popularity.com/overview/732032/sketchy-massage
// metadata
char __fastcall sub_1801C1B80(_DWORD *a1, _DWORD *a2)
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
  __m128i *_RCX; // rax
  __int64 v33; // rbx
  __m128i *_RCX_7; // rdi
  unsigned __int64 i; // rcx
  __m128i *_RCX_1; // rax
  __int64 v37; // rbx
  __m128i *_RCX_8; // rdi
  unsigned __int64 j; // rcx
  __m128i *_RCX_2; // rax
  __int64 v41; // rbx
  __m128i *_RCX_9; // rdi
  unsigned __int64 k; // rcx
  __m128i *_RCX_3; // rax
  __int64 v45; // rbx
  __m128i *_RCX_10; // rdi
  unsigned __int64 m; // rcx
  __m128i *_RCX_4; // rax
  __int64 v49; // rbx
  __m128i *_RCX_11; // rdi
  unsigned __int64 n; // rcx
  __m128i *_RCX_5; // rax
  __int64 v53; // rbx
  __m128i *_RCX_12; // rdi
  unsigned __int64 ii; // rcx
  __m128i *_RCX_6; // rax
  __int64 v57; // rbx
  __m128i *_RCX_13; // rdi
  unsigned __int64 jj; // rcx
  unsigned __int64 v60; // rdx
  unsigned __int64 v61; // rax
  __int64 v62; // rax
  __int64 v63; // r10
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
  unsigned int YQSY; // [rsp+30h] [rbp-20h] BYREF
  __int128 v76; // [rsp+34h] [rbp-1Ch]

  si128 = _mm_load_si128((const __m128i *)&xmmword_1818BB740);
  *(_DWORD *)((char *)&v76 + 1) = 1398412629;
  *(_DWORD *)((char *)&v76 + 5) = 1398232385;
  *(_DWORD *)((char *)&v76 + 10) = 1279918417;
  qmemcpy(&YQSY, "YQSY", sizeof(YQSY));
  YQSY = _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                      (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(0x3020100u)),
                                      (__m128)_mm_cvtsi32_si128(YQSY)));
  BYTE9(v76) = 69;
  HIWORD(v76) = 11096;
  *(_QWORD *)&v76 = __PAIR64__(
                      _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                   (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(0xB0A0908u)),
                                                   (__m128)_mm_cvtsi32_si128(DWORD1(v76)))),
                      _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                   (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(0x7060504u)),
                                                   (__m128)_mm_cvtsi32_si128(v76))));
  *((_QWORD *)&v76 + 1) = __PAIR64__(
                            _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                         (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(0x13121110u)),
                                                         (__m128)_mm_cvtsi32_si128(HIDWORD(v76)))),
                            _mm_cvtsi128_si32((__m128i)_mm_xor_ps(
                                                         (__m128)_mm_sub_epi8(si128, _mm_cvtsi32_si128(0xF0E0D0Cu)),
                                                         (__m128)_mm_cvtsi32_si128(DWORD2(v76)))));
  v5 = sub_18016DDC0(&YQSY);
  qword_181BDF3B8 = v5;
  if ( v5 )
  {
    v6 = sub_180233760(384);
    v7 = (__int128 *)qword_181BDF3B8;
    v8 = v6;
    qword_181BDF4C8 = v6;
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
    v13 = _mm_load_si128((const __m128i *)&xmmword_1815E8C90);
    v14 = (__m128)_mm_load_si128((const __m128i *)&xmmword_1818BB730);
    v15 = _mm_load_si128((const __m128i *)&xmmword_1818BB750).m128i_u16[0];
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
    qword_181BDF4E0 = v8;
    _RCX = (__m128i *)sub_180233760(v31);
    v33 = qword_181BDF4E0;
    _RCX_7 = _RCX;
    RCX = (__int64)_RCX;
    sub_180259500(
      _RCX,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 40) - 52),
      *(int *)(qword_181BDF4E0 + 376));
    for ( i = 0; i < *(int *)(v33 + 376); ++i )
      _RCX_7->m128i_i8[i] ^= *(_BYTE *)(v33 + 376) + i - 89;
    _RCX_1 = (__m128i *)sub_180233760(*(int *)(v33 + 156));
    v37 = qword_181BDF4E0;
    _RCX_8 = _RCX_1;
    RCX_0 = (__int64)_RCX_1;
    sub_180259500(
      _RCX_1,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 112) - 56),
      *(int *)(qword_181BDF4E0 + 156));
    for ( j = 0; j < *(int *)(v37 + 156); ++j )
      _RCX_8->m128i_i8[j] ^= j - *(_BYTE *)(v37 + 156) + 89;
    _RCX_2 = (__m128i *)sub_180233760(*(int *)(v37 + 88));
    v41 = qword_181BDF4E0;
    _RCX_9 = _RCX_2;
    RCX_1 = (__int64)_RCX_2;
    sub_180259500(
      _RCX_2,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 260) - 40),
      *(int *)(qword_181BDF4E0 + 88));
    for ( k = 0; k < *(int *)(v41 + 88); ++k )
      _RCX_9->m128i_i8[k] ^= k - *(_BYTE *)(v41 + 88) + 89;
    _RCX_3 = (__m128i *)sub_180233760(*(int *)(v41 + 228));
    v45 = qword_181BDF4E0;
    _RCX_10 = _RCX_3;
    RCX_2 = (__int64)_RCX_3;
    sub_180259500(
      _RCX_3,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 316) + 48),
      *(int *)(qword_181BDF4E0 + 228));
    for ( m = 0; m < *(int *)(v45 + 228); ++m )
      _RCX_10->m128i_i8[m] ^= *(_BYTE *)(v45 + 228) + m - 89;
    _RCX_4 = (__m128i *)sub_180233760(*(int *)(v45 + 340));
    v49 = qword_181BDF4E0;
    _RCX_11 = _RCX_4;
    RCX_3 = (__int64)_RCX_4;
    sub_180259500(
      _RCX_4,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 28) - 28),
      *(int *)(qword_181BDF4E0 + 340));
    for ( n = 0; n < *(int *)(v49 + 340); ++n )
      _RCX_11->m128i_i8[n] ^= *(_BYTE *)(v49 + 340) + n - 89;
    _RCX_5 = (__m128i *)sub_180233760(*(int *)(v49 + 92));
    v53 = qword_181BDF4E0;
    _RCX_12 = _RCX_5;
    RCX_4 = (__int64)_RCX_5;
    sub_180259500(
      _RCX_5,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 100) - 56),
      *(int *)(qword_181BDF4E0 + 92));
    for ( ii = 0; ii < *(int *)(v53 + 92); ++ii )
      _RCX_12->m128i_i8[ii] ^= ii - *(_BYTE *)(v53 + 92) + 89;
    _RCX_6 = (__m128i *)sub_180233760(*(int *)(v53 + 284));
    v57 = qword_181BDF4E0;
    _RCX_13 = _RCX_6;
    RCX_5 = (__int64)_RCX_6;
    sub_180259500(
      _RCX_6,
      (const __m128i *)(qword_181BDF3B8 + *(_DWORD *)(qword_181BDF4E0 + 24) - 24),
      *(int *)(qword_181BDF4E0 + 284));
    for ( jj = 0; jj < *(int *)(v57 + 284); ++jj )
      _RCX_13->m128i_i8[jj] ^= jj - *(_BYTE *)(v57 + 284) + 89;
    v60 = *(int *)(v57 + 144) / 0x28uLL;
    *a1 = v60;
    v61 = (unsigned __int64)*(int *)(v57 + 156) >> 6;
    dword_181BDF2B8 = v60;
    *a2 = v61;
    qword_181BDF2C0 = sub_180153170((int)v60, 24);
    qword_181BDF2E0 = sub_180153170(*(int *)(qword_181BDF4F8 + 48), 8);
    qword_181BDF2E8 = sub_180153170(*(int *)(qword_181BDF4E0 + 292) / 0x58uLL, 8);
    qword_181BDF2D0 = sub_180153170(*(int *)(qword_181BDF4E0 + 88) / 0x24uLL, 8);
    v62 = sub_180153170(*(int *)(qword_181BDF4F8 + 64), 8);
    v63 = qword_181BDF4F8;
    v64 = 0;
    qword_181BDF2C8 = v62;
    if ( *(int *)(qword_181BDF4F8 + 48) > 0 )
    {
      v65 = qword_181BDF3B8;
      v66 = qword_181BDF4E0;
      v67 = 0;
      do
      {
        v68 = *(int **)(v67 + *(_QWORD *)(v63 + 56));
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
      while ( v64 < *(_DWORD *)(v63 + 48) );
    }
    LOBYTE(v5) = 1;
  }
  return v5;
}