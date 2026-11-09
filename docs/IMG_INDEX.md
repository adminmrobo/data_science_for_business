# 이미지 전체 목록 (IMG_INDEX)

비즈니스를 위한 데이터 과학 연구실에 들어가는 그림을 한곳에 모은 목록입니다. **42장 프롬프트는 만드는 순서대로 `IMG_PROMPTS.md`에 모두 모아 두었습니다**(주차별 명세서 `COVER_NN.md`·`IMG_NN.md`에도 같은 내용).
이 파일은 `tools/build_docs.py`가 페이지 HTML을 읽어 만들므로, 그림을 넣은 뒤 다시 돌리면 상태 칸이 갱신됩니다.

## 1. 한눈에 보기

| 구분 | 장수 | 설명 |
|---|---|---|
| 새로 그릴 그림 | **42장** | 표지 16(목차 + 15주차) · 히어로 무대 13 · 아웃트로 13 |
| 표지에서 자르는 그림 | 31장 | 목차 카드(thumb, 3:2) 15 · 공유 미리보기(og, 1200×630) 16 — 따로 그리지 않음 |
| 재사용(캐릭터 팩) | 표정 19종 | 이미 모든 페이지에 들어 있음. 새로 그리지 않음 |
| 지금 들어간 그림 | 0장 | 나머지 페이지는 대체 표지·캔버스 무대로 이미 완성 상태 |

연습 페이지(8·15주차)는 대결이 없어서 히어로 무대·아웃트로 자리가 없고 표지만 필요합니다.

## 2. 만드는 순서 (권장)

| 단계 | 그림 | 장수 | 이유 |
|---|---|---|---|
| 1 | 목차 표지 `cover_index` | 1 | 시리즈의 첫 기준 그림. 이후 모든 그림의 참고 이미지로 함께 올림 |
| 2 | 주차 표지 `cover_w01` ~ `cover_w15` | 15 | 페이지 맨 위에 바로 보이고, thumb·og를 여기서 잘라 냄 |
| 3 | 히어로 무대 `sc_wNN_hero` | 13 | 결과를 암시하지 않는 대결 전 장면 |
| 4 | 아웃트로 `sc_wNN_outro` | 13 | 대결 결과(표정 기준)가 드러나는 장면 |
| 5 | thumb·og 자르기 | 31 | 표지에서 잘라 WebP로 저장 |

## 3. 전체 목록

| 페이지 | 키 | 종류 | 판 | 크기 | 우선 | 프롬프트 위치 | 상태 |
|---|---|---|---|---|---|---|---|
| 목차 | `cover_index` | 그림(새로) | L | 1920×1080 | P1 | COVER_00_index.md | ☐ 없음 |
| 목차 | `og_index` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 1주차 | `cover_w01` | 그림(새로) | L | 1920×1080 | P1 | COVER_01.md | ☐ 없음 |
| 1주차 | `sc_w01_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_01.md 3-2 | ☐ 없음 |
| 1주차 | `sc_w01_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_01.md 3-3 | ☐ 없음 |
| 1주차 | `thumb_w01` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 1주차 | `og_w01` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 2주차 | `cover_w02` | 그림(새로) | L | 1920×1080 | P1 | COVER_02.md | ☐ 없음 |
| 2주차 | `sc_w02_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_02.md 3-2 | ☐ 없음 |
| 2주차 | `sc_w02_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_02.md 3-3 | ☐ 없음 |
| 2주차 | `thumb_w02` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 2주차 | `og_w02` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 3주차 | `cover_w03` | 그림(새로) | L | 1920×1080 | P1 | COVER_03.md | ☐ 없음 |
| 3주차 | `sc_w03_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_03.md 3-2 | ☐ 없음 |
| 3주차 | `sc_w03_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_03.md 3-3 | ☐ 없음 |
| 3주차 | `thumb_w03` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 3주차 | `og_w03` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 4주차 | `cover_w04` | 그림(새로) | L | 1920×1080 | P1 | COVER_04.md | ☐ 없음 |
| 4주차 | `sc_w04_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_04.md 3-2 | ☐ 없음 |
| 4주차 | `sc_w04_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_04.md 3-3 | ☐ 없음 |
| 4주차 | `thumb_w04` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 4주차 | `og_w04` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 5주차 | `cover_w05` | 그림(새로) | L | 1920×1080 | P1 | COVER_05.md | ☐ 없음 |
| 5주차 | `sc_w05_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_05.md 3-2 | ☐ 없음 |
| 5주차 | `sc_w05_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_05.md 3-3 | ☐ 없음 |
| 5주차 | `thumb_w05` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 5주차 | `og_w05` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 6주차 | `cover_w06` | 그림(새로) | L | 1920×1080 | P1 | COVER_06.md | ☐ 없음 |
| 6주차 | `sc_w06_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_06.md 3-2 | ☐ 없음 |
| 6주차 | `sc_w06_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_06.md 3-3 | ☐ 없음 |
| 6주차 | `thumb_w06` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 6주차 | `og_w06` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 7주차 | `cover_w07` | 그림(새로) | L | 1920×1080 | P1 | COVER_07.md | ☐ 없음 |
| 7주차 | `sc_w07_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_07.md 3-2 | ☐ 없음 |
| 7주차 | `sc_w07_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_07.md 3-3 | ☐ 없음 |
| 7주차 | `thumb_w07` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 7주차 | `og_w07` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 8주차 | `cover_w08` | 그림(새로) | L | 1920×1080 | P1 | COVER_08.md | ☐ 없음 |
| 8주차 | `thumb_w08` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 8주차 | `og_w08` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 9주차 | `cover_w09` | 그림(새로) | L | 1920×1080 | P1 | COVER_09.md | ☐ 없음 |
| 9주차 | `sc_w09_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_09.md 3-2 | ☐ 없음 |
| 9주차 | `sc_w09_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_09.md 3-3 | ☐ 없음 |
| 9주차 | `thumb_w09` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 9주차 | `og_w09` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 10주차 | `cover_w10` | 그림(새로) | L | 1920×1080 | P1 | COVER_10.md | ☐ 없음 |
| 10주차 | `sc_w10_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_10.md 3-2 | ☐ 없음 |
| 10주차 | `sc_w10_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_10.md 3-3 | ☐ 없음 |
| 10주차 | `thumb_w10` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 10주차 | `og_w10` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 11주차 | `cover_w11` | 그림(새로) | L | 1920×1080 | P1 | COVER_11.md | ☐ 없음 |
| 11주차 | `sc_w11_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_11.md 3-2 | ☐ 없음 |
| 11주차 | `sc_w11_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_11.md 3-3 | ☐ 없음 |
| 11주차 | `thumb_w11` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 11주차 | `og_w11` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 12주차 | `cover_w12` | 그림(새로) | L | 1920×1080 | P1 | COVER_12.md | ☐ 없음 |
| 12주차 | `sc_w12_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_12.md 3-2 | ☐ 없음 |
| 12주차 | `sc_w12_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_12.md 3-3 | ☐ 없음 |
| 12주차 | `thumb_w12` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 12주차 | `og_w12` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 13주차 | `cover_w13` | 그림(새로) | L | 1920×1080 | P1 | COVER_13.md | ☐ 없음 |
| 13주차 | `sc_w13_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_13.md 3-2 | ☐ 없음 |
| 13주차 | `sc_w13_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_13.md 3-3 | ☐ 없음 |
| 13주차 | `thumb_w13` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 13주차 | `og_w13` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 14주차 | `cover_w14` | 그림(새로) | L | 1920×1080 | P1 | COVER_14.md | ☐ 없음 |
| 14주차 | `sc_w14_hero` | 그림(새로) | E | 1200×800 | P1 | IMG_14.md 3-2 | ☐ 없음 |
| 14주차 | `sc_w14_outro` | 그림(새로) | E | 1200×800 | P2 | IMG_14.md 3-3 | ☐ 없음 |
| 14주차 | `thumb_w14` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 14주차 | `og_w14` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |
| 15주차 | `cover_w15` | 그림(새로) | L | 1920×1080 | P1 | COVER_15.md | ☐ 없음 |
| 15주차 | `thumb_w15` | 표지 자르기 | I | 600×400 | P2 | — | ☐ 없음 |
| 15주차 | `og_w15` | 표지 자르기 | K | 1200×630 | P3 | — | ☐ 없음 |

## 4. 페이지별 재사용 표정 (캐릭터 팩 @5269662)

| 페이지 | 표정 키 |
|---|---|
| 목차 | `asst_smile` · `doc_front` · `fly_point` · `robo_coin` |
| 1주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_board` · `doc_front` · `doc_judge` · `doc_think` · `fly_arms` · `fly_clip` · `fly_magnify` · `fly_point` · `robo_coin` · `robo_sigh` · `robo_smile` |
| 2주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `fly_clip` · `fly_coffee` · `fly_magnify` · `fly_point` · `robo_calc` · `robo_coin` · `robo_smile` |
| 3주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_board` · `doc_front` · `doc_judge` · `fly_clip` · `fly_coffee` · `fly_magnify` · `fly_point` · `robo_coin` · `robo_happy` · `robo_smile` |
| 4주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_board` · `doc_front` · `doc_judge` · `fly_clip` · `fly_cry` · `fly_magnify` · `fly_point` · `robo_coin` · `robo_happy` · `robo_smile` |
| 5주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `fly_clip` · `fly_coffee` · `fly_magnify` · `fly_point` · `robo_coin` · `robo_meh` · `robo_smile` |
| 6주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_arms` · `fly_clip` · `fly_point` · `robo_calc` · `robo_coin` · `robo_sigh` · `robo_smile` |
| 7주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_clip` · `fly_coffee` · `fly_point` · `robo_coin` · `robo_happy` · `robo_smile` |
| 8주차 | `asst_report` · `asst_smile` · `doc_front` · `doc_think` · `fly_point` · `robo_calc` · `robo_coin` |
| 9주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_clip` · `fly_coffee` · `fly_point` · `robo_calc` · `robo_coin` · `robo_smile` |
| 10주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_arms` · `fly_clip` · `fly_point` · `robo_coin` · `robo_sigh` · `robo_smile` |
| 11주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_clip` · `fly_coffee` · `fly_point` · `robo_coin` · `robo_happy` · `robo_smile` |
| 12주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_arms` · `fly_clip` · `fly_point` · `robo_coin` · `robo_sigh` · `robo_smile` |
| 13주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_clip` · `fly_coffee` · `fly_point` · `robo_calc` · `robo_coin` · `robo_smile` |
| 14주차 | `asst_firm` · `asst_report` · `asst_smile` · `doc_front` · `doc_judge` · `doc_think` · `fly_clip` · `fly_coffee` · `fly_point` · `robo_coin` · `robo_meh` · `robo_smile` |
| 15주차 | `asst_report` · `asst_smile` · `doc_front` · `doc_think` · `fly_point` · `robo_calc` · `robo_coin` |

## 5. 넘겨주실 때
- 파일 이름을 키와 같게 해 주세요. 예: `cover_w07.png`, `sc_w07_hero.png`
- 받은 뒤 처리: 비율·글자·네 캐릭터 확인 → WebP(표지 1600×900, 220 KB 이하) → 페이지 `SPRITE`에 넣기 → 390·768·1280 폭 점검 → 이 목록 다시 생성
- 페이지 한 편의 그림 합계는 표지 포함 600 KB 이하로 둡니다.
