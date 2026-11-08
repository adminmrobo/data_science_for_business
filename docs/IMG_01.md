# 1주차 · 데이터는 많은데, 결정은 왜 틀릴까 — 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 저장소 맨 위의 해당 주차 HTML |
| 모드 / 주 앵커 | 교과서 모드 / B 연구실 + D 일상(우산 판매, 돌아온 비행기) |
| 시즌 | 기본 |
| 대결 | F(초파리 승, 91.7% 대 56.8%) |
| 새로 그릴 그림 | P1 2장 · P2 2장 · P3 1장 |
| 재사용 | 표정 전부 (캐릭터 팩) |
| 그림이 없을 때 | 페이지는 캔버스 무대·대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: SKILL 18-3 (16비트 RPG 픽셀아트, 굵은 외곽선, 2~3단계 명암)
- 캐릭터 고정 외형: 캐릭터 팩 18-4 (박사 · 조수 · 초파리 연구원 · 주판봇)
- 장소 영어 묘사: *wide night laboratory with a large monitor showing a blank bar chart and four glowing stair blocks rising beside it*
- 생물 앵커가 아니므로 현미경·초파리 해부 소품은 넣지 않음

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 1 | cover_w01 | L | 1920×1080 | 새로 (COVER_01) | P1 | 맨 위 글 표지 | 대체 표지(CSS + 캐릭터 넷) |
| 2 | sc_w01_hero | E | 1200×800 | 새로 | P1 | 히어로 무대 | 캔버스 무대 + 캐릭터 그림 |
| 3 | sc_w01_outro | E | 1200×800 | 새로 | P2 | 아웃트로 | 없음(장면 생략) |
| 4 | thumb_w01 | I | 600×400 | 새로 (표지 3:2 자르기) | P2 | 목차 카드 | 이모지 카드 |
| 5 | og_w01 | K | 1200×630 | 새로 (표지 자르기) | P3 | 공유 미리보기 | 없음 |
| 6 | 표정 키 전부 | A~D | 96px | 재사용 (캐릭터 팩 @5269662) | — | 말풍선·대결·등장인물 | 픽셀 지도 |
| 7 | 행동으로 보기·실험 그림 | — | — | 코드 | — | 캔버스 | — |

## 3. 새로 그릴 그림 상세

### 3-1. `cover_w01` — 글 표지
`COVER_01.md`를 그대로 씁니다.

### 3-2. `sc_w01_hero` — 히어로 무대 (결과 암시 없음)
대체 글: 네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 밤의 연구실 표지
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, wide night laboratory with a large monitor showing a blank bar chart and four glowing stair blocks rising beside it, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `sc_w01_outro` — 아웃트로 (대결 후)
표정 기준(캐릭터 팩 5-8): 초파리 `fly_arms`, 주판봇 `robo_sigh`. 대체 글: 대결 후 팔짱 낀 초파리 연구원과 식은땀 흘리는 주판봇, 엄지를 세운 박사와 웃는 조수
```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, a relaxed fruit fly researcher with arms crossed in quiet satisfaction on the left, a sheepish robot with a sweat drop on the right, the scientist giving a thumbs-up, the girl smiling with a striped ledger; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 4. 일관성 지침
- 참고 이미지: 네 캐릭터 기본 그림 4장 + 이 시리즈의 첫 표지
- 같은 캐릭터는 같은 세션에서 연달아 만들기
- 투명 배경이 안 되면 *solid flat #00ff00 background*

## 5. 넘겨받은 뒤 처리
1. 크기 확인 → WebP 압축(표지 1600 220 KB 이하)
2. 단일 파일 페이지에 base64로 `SPRITE`에 키를 채움(`Object.assign(SPRITE,{...})`) → `data-scene`·`data-img` 자리가 자동으로 켜짐
3. 페이지 그림 합계 표지 포함 600 KB 이하 확인

## 6. 매니페스트
```json
{
 "page": "w01",
 "anchor": "B 연구실 + D 일상(우산 판매, 돌아온 비행기)",
 "season": "default",
 "duel": "F(초파리 승, 91.7% 대 56.8%)",
 "images": [
  {
   "key": "cover_w01",
   "plate": "L",
   "size": [
    1920,
    1080
   ],
   "status": "new",
   "priority": "P1",
   "slot": "cover",
   "fallback": "css-pixel-four",
   "alt": "네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 밤의 연구실 표지"
  },
  {
   "key": "sc_w01_hero",
   "plate": "E",
   "size": [
    1200,
    800
   ],
   "status": "new",
   "priority": "P1",
   "slot": "hero-stage",
   "fallback": "canvas-stage",
   "alt": "네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 밤의 연구실 표지"
  },
  {
   "key": "sc_w01_outro",
   "plate": "E",
   "size": [
    1200,
    800
   ],
   "status": "new",
   "priority": "P2",
   "slot": "outro",
   "fallback": "none",
   "alt": "대결 후 팔짱 낀 초파리 연구원과 식은땀 흘리는 주판봇, 엄지를 세운 박사와 웃는 조수"
  },
  {
   "key": "thumb_w01",
   "plate": "I",
   "size": [
    600,
    400
   ],
   "status": "new",
   "priority": "P2",
   "slot": "index-card",
   "fallback": "emoji-card"
  },
  {
   "key": "og_w01",
   "plate": "K",
   "size": [
    1200,
    630
   ],
   "status": "new",
   "priority": "P3",
   "slot": "og",
   "fallback": "none"
  }
 ]
}
```
