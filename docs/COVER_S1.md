# 표지 지시문 — 특강 ① · 평소와 다른 한 건 찾기 (이상 탐지)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_wS1 · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | D 생활·현장: 밤의 연구실에 펼쳐진 점의 들판 |
| 주제 은유 | 수백 개의 초록 점 사이에서 홀로 떨어진 붉은 점 하나, 가지를 뻗은 빛의 나무 모형(고립 숲), 방을 가로지르는 호박색 레이저 선(문턱값) |
| 네 캐릭터 포즈 | 박사: at the back center pointing up at the horizontal amber laser line / 조수: kneeling and counting green dots on a clipboard / 초파리 연구원: on the left facing right, peering at the lone red dot through a big magnifying glass / 주판봇: on the right facing left, holding up a small glowing tree model in one arm and an abacus in the other |
| 대체 글 (alt) | 네 캐릭터가 밤의 연구실에서 수많은 초록 점 사이에 홀로 붉게 빛나는 점 하나를 돋보기와 주판으로 살피는 표지 |
| 앞 표지와 다른 점 | 14주차(구슬 무리·말풍선·신경망 탑), 7주차(성적표) 와 겹치지 않게 점의 들판·빛의 나무·레이저 선으로 함 |
| 결과 암시 | 없음 (대결 전 장면) · 이 페이지 대결 결과: R(주판봇 승, 경보 15건 중 진짜 이상: 고립 숲 8건 대 Z 점수 3건) — 표지에는 드러내지 않음 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions`).

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab where hundreds of small glowing green dots float above a long table like a starry field, with one lone red-glowing dot drifting apart from them, a small tree-shaped model made of branching glowing lines on a stand, and a horizontal amber laser line stretched across the room.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center pointing up at the horizontal amber laser line;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, kneeling and counting green dots on a clipboard;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, peering at the lone red dot through a big magnifying glass;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, holding up a small glowing tree model made of branching lines.
Visual metaphor of the topic: one lone red dot drifting apart from a field of green dots, a branching tree of light that splits the field, and a single amber line that separates "check" from "pass".
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the lone red dot.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

**받은 뒤:** 그림을 돌려주면 SKILL 18-15 절차(비율·글자·네 캐릭터 확인 → WebP 1600×900·960×540 → 390·768·1280 폭 점검)로 `cover_wS1` 자리에 넣습니다(`tools/art/cover_wS1.webp`로 두고 `python3 build.py S1`). 페이지는 그림이 없어도 대체 표지(CSS + 캐릭터 넷)로 완성 상태입니다.
