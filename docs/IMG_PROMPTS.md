# 이미지 제작 프롬프트 모음 (42장)

비즈니스를 위한 데이터 과학 연구실의 새로 그릴 그림 42장 프롬프트를 만드는 순서대로 모았습니다. 같은 내용이 주차별 `COVER_NN.md`·`IMG_NN.md`에도 있습니다. 전체 목록과 상태는 `IMG_INDEX.md`를 보세요.

## 쓰는 법 (Genspark 기준)

1. 새 대화마다 **참고 이미지**를 함께 올립니다: 네 캐릭터 기본 그림 4장(GitHub `adminmrobo/fruitfly-lab-expressions`). 1단계가 끝나면 `cover_index`도 함께 올립니다.
2. 아래 한국어 안내 다음 줄에 해당 영어 프롬프트를 붙여 넣습니다.

```
웹페이지에 넣을 그림 1장을 만들어 줘.
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 비율: 표지는 16:9(가로 1920px 이상), 무대·아웃트로는 3:2(1200×800)
아래 영어 프롬프트를 그대로 써 줘.
```

3. 고칠 때(같은 대화에서): `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`
4. 받은 그림은 **키와 같은 파일 이름**으로 저장해 주세요(예: `cover_w07.png`, `sc_w07_hero.png`).
5. 같은 캐릭터가 나오는 그림은 같은 대화에서 연달아 만드는 편이 외형이 덜 흔들립니다.

## 1단계 · 목차 표지 (1장)

### 1. `cover_index` — 목차 표지 · 16:9, 가로 1920 이상

대체 글: 밤의 연구실 복도. 주차마다 다른 색 빛이 새는 문들 앞에 네 캐릭터가 서 있는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a long night laboratory corridor with a row of doors, each door leaking a different colored light (one door per week).
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center, pointing at the open glowing door;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, holding a blank clipboard, smiling toward the viewer;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, peering at the nearest door with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, rolling forward eagerly with the abacus raised.
Visual metaphor of the topic: the doors themselves stand for the weeks of the course; a glowing open doorway in the middle.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 2단계 · 주차 표지 (15장)

1단계에서 만든 `cover_index`를 참고 이미지로 함께 올리면 그림체가 맞습니다.

### 2. `cover_w01` — 1주차 · 데이터는 많은데, 결정은 왜 틀릴까 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 밤의 연구실 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: wide night laboratory with a large monitor showing a blank bar chart and four glowing stair blocks rising beside it.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center with a hand on his chin, looking up the four steps;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, beside the monitor holding a striped blank ledger;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, examining the toy airplane with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, proudly pushing a cart piled with blank data cards.
Visual metaphor of the topic: four stacked steps of increasing brightness (data to wisdom) and a small toy airplane model with scattered white dots on its wings and body but none on its engines.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 3. `cover_w02` — 2주차 · 데이터는 어디서 오는가 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 은행 창구, 공장 센서, 편의점 계산대, 스마트폰에서 서버로 흘러드는 빛줄기를 지켜보는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: the night lab opened up like a map: a tiny bank counter, a factory sensor pole, a convenience store checkout and a smartphone, each sending streams of small glowing dots into a server rack.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center gesturing toward the server rack;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, kneeling by the checkout, labeling blank cards;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, covering some dots with a translucent privacy sheet;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, opening a big funnel to catch the fastest stream.
Visual metaphor of the topic: streams of colored light dots flowing from four sources into one server rack, one stream fast and one slow.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 4. `cover_w03` — 3주차 · 분석 전에 데이터를 손보다 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 빈칸과 튀는 값, 겹친 카드가 섞인 큰 표를 작업대 위에서 함께 손질하는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a big workbench in the night lab with a huge paper table spread out, some cells blank, some cells glowing red, a few duplicate cards stacked.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center pointing at a red cell with a pointer finger;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, filling a blank cell with a glowing green block;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, holding scissors over a row with a blank cell, hesitating;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, carrying a basket of glowing filler blocks.
Visual metaphor of the topic: a giant table with holes being filled with green light, one oddly tall bar sticking out of the table, and a broom sweeping duplicate cards.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 5. `cover_w04` — 4주차 · 도구와 알고리즘의 지도 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 도구 선반과 점이 흩어진 지도 탁자 앞에서 직선 자와 곡선 경계를 견주는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with a tall tool shelf of glowing instruments and a large map table showing a scatter of red and green dots split by a curved line, a shopping basket on the corner.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center unrolling the big map;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, checking items off a blank clipboard beside the shelf;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, drawing a curved boundary with a glowing pen;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, laying a straight ruler across the dots.
Visual metaphor of the topic: a hand-drawn treasure map whose paths branch to different tools, and a straight ruler laid next to a curved glowing boundary between dots.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 6. `cover_w05` — 5주차 · 도미와 빙어 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 작업대 위 도미와 빙어를 자와 저울로 재며 노트북 산점도에 점을 찍는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab workbench with a ruler, a kitchen scale, two buckets of fish (large silvery bream and small slim smelt) and a laptop showing a blank scatter plot.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center holding up a large bream to look at it;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, writing blank labels and sticking them on small cards;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, measuring a small smelt with a ruler;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, placing a bream on the scale.
Visual metaphor of the topic: fish being measured and turned into glowing dots that fly into the scatter plot on the laptop screen.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 7. `cover_w06` — 6주차 · 농어가 끼어들자 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 도미·농어·빙어가 든 수조 앞에서 자의 눈금을 맞추고 생선을 훈련·시험 두 바구니로 나누는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with a glowing aquarium of three kinds of fish (big, medium, tiny), two baskets labeled only by color (one blue, one orange) and a long ruler and a scale side by side.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center tapping the aquarium glass;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, sorting fish into the blue and orange baskets;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, stretching the rubber ruler to match the scale dial;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, weighing a fish and squinting at the big number.
Visual metaphor of the topic: a stretched rubber ruler being pulled to the same length as a scale dial, showing two different units brought to one common scale.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 8. `cover_w07` — 7주차 · 정확도 95%의 함정 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 2×2 칸의 커다란 성적표 앞에서 저울로 두 종류의 오류 무게를 다는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with a huge 2x2 grid board on the wall, each cell glowing a different color (green, red, amber, blue), a balance scale on the desk with two different weights.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center pointing at the top-right cell of the board;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, counting tally marks on a blank clipboard;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, holding a magnifier up to the biggest cell;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, putting coins on the balance scale.
Visual metaphor of the topic: a balance scale weighing two kinds of mistakes, one heavy coin and one light coin, in front of the four-cell board.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 9. `cover_w08` — 8주차 · 연습 ① 1~7주차 문제풀이 · 16:9, 가로 1920 이상

대체 글: 밤의 연구실 공부 책상에서 네 캐릭터가 일곱 개의 빛나는 폴더와 빈 답안지를 앞에 두고 문제를 푸는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a cozy night study corner of the laboratory with a long desk covered in blank answer sheets, seven small glowing folders stacked in a row, a desk lamp and a big wall chalkboard left blank.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the chalkboard holding a piece of chalk, looking back at the desk;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, holding a blank score sheet and a red pencil, cheerful;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, scratching his helmet over an answer sheet with a pencil;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, working fast on a wooden abacus beside a stack of sheets.
Visual metaphor of the topic: seven small glowing folders lined up like a staircase (one per week reviewed), a red pencil and a stack of blank answer sheets with tick boxes.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 10. `cover_w09` — 9주차 · 숫자를 맞히는 선 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 양궁 과녁 앞에서 농어를 저울에 올리고 칠판의 점들 위로 곡선을 긋는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with an archery target on the wall, a kitchen scale with a medium fish on it, and a chalkboard full of dots with a smooth curve drawn through them.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center drawing a smooth curve through dots on the chalkboard;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, reading the scale and writing a number on a blank card;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, measuring a fish with a long ruler;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, averaging five small fish cards with the abacus.
Visual metaphor of the topic: arrows stuck around the bullseye at different distances, with faint lines measuring how far each one missed.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 11. `cover_w10` — 10주차 · S자 곡선과 스무고개 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 S자 곡선이 그려진 칠판과 가지를 뻗은 질문 나무 앞에서 가위와 양념통을 든 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with a chalkboard showing a smooth S-shaped curve, a small potted tree whose branches end in colored marble jars, and a spice rack on the side.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center trimming a branch of the tree with small scissors;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, sorting colored marbles into two jars;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, holding a spice jar and pouring just a pinch;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, dumping a whole armful of spice jars into a pot.
Visual metaphor of the topic: a tree whose every branch split sorts marbles by color, next to a spice rack where some jars are almost empty.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 12. `cover_w11` — 11주차 · 시간이 기억하는 숫자 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 벽에 걸린 긴 달력과 물결치는 매출 그래프 앞에서 작년 같은 달을 손가락으로 짚는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with a very long wall calendar spanning six years and a glowing wavy sales line above it that peaks every December.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center tracing the wavy line with a pointer;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, cutting the long calendar strip into a training part and a test part;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, studying a bar chart of correlations with a magnifier;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, flipping open last year's ledger to the December page.
Visual metaphor of the topic: the same month in consecutive years connected by thin glowing threads, showing that this December remembers last December.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 13. `cover_w12` — 12주차 · 숫자의 얼굴 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 한쪽으로 길게 늘어진 막대그래프와 시소 위의 평균·중앙값 추를 바라보는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with a big histogram on the wall whose right tail stretches far, and a seesaw on the desk with two weights labeled only by color.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center pointing at the long right tail of the histogram;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, lining up small figurines in order of height;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, standing next to the middle figurine with arms open;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, pushing the heavy weight further out on the seesaw.
Visual metaphor of the topic: a seesaw tipped by one heavy weight far out on the right, while a small flag stands at the middle of the line of people.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 14. `cover_w13` — 13주차 · 계기판을 설계하다 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 항공기 조종석 같은 계기판 앞에서 깔때기 모양 광고 퍼널과 창고 선반을 살피는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab arranged like an airplane cockpit, with three round gauges, a glowing funnel diagram and a small warehouse shelf with boxes.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center in the pilot seat looking at the gauges;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, plugging three different cables into one hub;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, scattering many small light dots into the top of the funnel;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, catching coins at the bottom of the funnel with the abacus.
Visual metaphor of the topic: three gauge needles pulling against each other, and a funnel narrowing from many dots at the top to a few coins at the bottom.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 15. `cover_w14` — 14주차 · 정답 없이, 글 속에서, 층을 쌓아 · 16:9, 가로 1920 이상

대체 글: 네 캐릭터가 색깔별로 모인 구슬 무리, 말풍선 리뷰 더미, 층층이 쌓인 신경망 탑을 둘러보는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a night lab with three clusters of glowing marbles on a table, a pile of speech-bubble cards on the floor, and a tower of connected glowing circles in layers.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center looking up at the layered tower;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, sorting speech-bubble cards into green and red trays;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, stacking one more layer of glowing circles on the tower;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, drawing one straight line with a ruler across a sheet.
Visual metaphor of the topic: marbles gathering by themselves into colored groups, speech bubbles sorted into a green tray and a red tray, and a layered tower of circles drawing a round boundary.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

### 16. `cover_w15` — 15주차 · 연습 ② 9~14주차 문제풀이 · 16:9, 가로 1920 이상

대체 글: 한 시즌의 마지막 밤, 둥근 복습 테이블에 놓인 여섯 개의 빛나는 폴더를 네 캐릭터가 둘러싸고 마무리하는 표지

```
Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
  (if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a round review table in the night laboratory at the end of the season, six glowing folders arranged in a circle, a calculator-like wooden abacus, colorful sticky notes on a corkboard behind, a window showing a winter night.
All four characters together:
  chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center holding up a blank finished answer sheet proudly;
  girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, pinning a blank sticky note on the corkboard;
  anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, on the left facing right, flipping through a glowing folder with a magnifying glass;
  boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus, on the right facing left, on the right facing left, tapping the abacus with one arm raised.
Visual metaphor of the topic: six glowing folders in a circle (one per week reviewed) around a single lit candle-like lamp, sticky notes without writing, a finished stack of answer sheets tied with ribbon.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner dark and simple; the light falls on the main prop.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

## 3단계 · 히어로 무대 (13장)

대결 전 장면입니다. 결과를 암시하지 않습니다.

### 17. `sc_w01_hero` — 1주차 · 데이터는 많은데, 결정은 왜 틀릴까 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 밤의 연구실 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, wide night laboratory with a large monitor showing a blank bar chart and four glowing stair blocks rising beside it, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 18. `sc_w02_hero` — 2주차 · 데이터는 어디서 오는가 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 은행 창구, 공장 센서, 편의점 계산대, 스마트폰에서 서버로 흘러드는 빛줄기를 지켜보는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, the night lab opened up like a map: a tiny bank counter, a factory sensor pole, a convenience store checkout and a smartphone, each sending streams of small glowing dots into a server rack, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 19. `sc_w03_hero` — 3주차 · 분석 전에 데이터를 손보다 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 빈칸과 튀는 값, 겹친 카드가 섞인 큰 표를 작업대 위에서 함께 손질하는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a big workbench in the night lab with a huge paper table spread out, some cells blank, some cells glowing red, a few duplicate cards stacked, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 20. `sc_w04_hero` — 4주차 · 도구와 알고리즘의 지도 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 도구 선반과 점이 흩어진 지도 탁자 앞에서 직선 자와 곡선 경계를 견주는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with a tall tool shelf of glowing instruments and a large map table showing a scatter of red and green dots split by a curved line, a shopping basket on the corner, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 21. `sc_w05_hero` — 5주차 · 도미와 빙어 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 작업대 위 도미와 빙어를 자와 저울로 재며 노트북 산점도에 점을 찍는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab workbench with a ruler, a kitchen scale, two buckets of fish (large silvery bream and small slim smelt) and a laptop showing a blank scatter plot, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 22. `sc_w06_hero` — 6주차 · 농어가 끼어들자 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 도미·농어·빙어가 든 수조 앞에서 자의 눈금을 맞추고 생선을 훈련·시험 두 바구니로 나누는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with a glowing aquarium of three kinds of fish (big, medium, tiny), two baskets labeled only by color (one blue, one orange) and a long ruler and a scale side by side, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 23. `sc_w07_hero` — 7주차 · 정확도 95%의 함정 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 2×2 칸의 커다란 성적표 앞에서 저울로 두 종류의 오류 무게를 다는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with a huge 2x2 grid board on the wall, each cell glowing a different color (green, red, amber, blue), a balance scale on the desk with two different weights, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 24. `sc_w09_hero` — 9주차 · 숫자를 맞히는 선 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 양궁 과녁 앞에서 농어를 저울에 올리고 칠판의 점들 위로 곡선을 긋는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with an archery target on the wall, a kitchen scale with a medium fish on it, and a chalkboard full of dots with a smooth curve drawn through them, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 25. `sc_w10_hero` — 10주차 · S자 곡선과 스무고개 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 S자 곡선이 그려진 칠판과 가지를 뻗은 질문 나무 앞에서 가위와 양념통을 든 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with a chalkboard showing a smooth S-shaped curve, a small potted tree whose branches end in colored marble jars, and a spice rack on the side, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 26. `sc_w11_hero` — 11주차 · 시간이 기억하는 숫자 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 벽에 걸린 긴 달력과 물결치는 매출 그래프 앞에서 작년 같은 달을 손가락으로 짚는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with a very long wall calendar spanning six years and a glowing wavy sales line above it that peaks every December, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 27. `sc_w12_hero` — 12주차 · 숫자의 얼굴 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 한쪽으로 길게 늘어진 막대그래프와 시소 위의 평균·중앙값 추를 바라보는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with a big histogram on the wall whose right tail stretches far, and a seesaw on the desk with two weights labeled only by color, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 28. `sc_w13_hero` — 13주차 · 계기판을 설계하다 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 항공기 조종석 같은 계기판 앞에서 깔때기 모양 광고 퍼널과 창고 선반을 살피는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab arranged like an airplane cockpit, with three round gauges, a glowing funnel diagram and a small warehouse shelf with boxes, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 29. `sc_w14_hero` — 14주차 · 정답 없이, 글 속에서, 층을 쌓아 히어로 · 3:2, 1200×800

대체 글: 네 캐릭터가 색깔별로 모인 구슬 무리, 말풍선 리뷰 더미, 층층이 쌓인 신경망 탑을 둘러보는 표지

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a night lab with three clusters of glowing marbles on a table, a pile of speech-bubble cards on the floor, and a tower of connected glowing circles in layers, chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie at the back center, anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings on the left facing right, boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus on the right facing left, girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans at the side, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

## 4단계 · 아웃트로 (13장)

대결 뒤 장면입니다. 표정은 각 주차 대결 결과를 따릅니다.

### 30. `sc_w01_outro` — 1주차 · 데이터는 많은데, 결정은 왜 틀릴까 아웃트로 · 3:2, 1200×800

대결: F(초파리 승, 91.7% 대 56.8%) · 표정 기준: 초파리 `fly_arms`, 주판봇 `robo_sigh`

대체 글: 대결 후 팔짱 낀 초파리 연구원과 식은땀 흘리는 주판봇, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, a relaxed fruit fly researcher with arms crossed in quiet satisfaction on the left, a sheepish robot with a sweat drop on the right, the scientist giving a thumbs-up, the girl smiling with a striped ledger; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 31. `sc_w02_outro` — 2주차 · 데이터는 어디서 오는가 아웃트로 · 3:2, 1200×800

대결: C(조건부: 사기 감시는 스트림, 월간 보고는 배치) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_calc`

대체 글: 두 업무 카드를 사이에 두고 커피를 든 초파리 연구원과 주판을 튕기는 주판봇, 턱을 괸 박사와 설명하는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, two task cards on a table between them, the fruit fly researcher holding a coffee cup calmly, the robot tapping its abacus, the scientist with a hand on his chin, the girl pointing at both cards; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 32. `sc_w03_outro` — 3주차 · 분석 전에 데이터를 손보다 아웃트로 · 3:2, 1200×800

대결: R(주판봇 승, 오차 28만 원 대 280만 원) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_happy`

대체 글: 빈칸이 채워진 표 앞에서 기뻐하는 주판봇과 커피를 든 초파리 연구원, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, a big table whose blank cells are now filled with green light, the robot cheering in front, the fruit fly researcher sipping coffee and nodding, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 33. `sc_w04_outro` — 4주차 · 도구와 알고리즘의 지도 아웃트로 · 3:2, 1200×800

대결: R(주판봇 승, 대출 시험 정확도 88.5% 대 75.8%) · 표정 기준: 초파리 `fly_cry`, 주판봇 `robo_happy`

대체 글: 곡선 경계 앞에서 기뻐하는 주판봇과 직선 자를 든 채 눈물 맺힌 초파리 연구원, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, the map table with a curved glowing boundary, the robot cheering beside it, the fruit fly researcher with teary eyes holding his straight ruler, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 34. `sc_w05_outro` — 5주차 · 도미와 빙어 아웃트로 · 3:2, 1200×800

대결: D(무승부, 한 마리씩 빼고 채점: 둘 다 100%) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_meh`

대체 글: 같은 점수 카드 두 장을 사이에 두고 커피를 든 초파리 연구원과 어깨를 으쓱하는 주판봇, 고개를 끄덕이는 박사와 두 카드를 든 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, two identical score cards on the bench between the fish buckets, the fruit fly researcher sipping coffee, the robot shrugging, the scientist nodding, the girl holding up both cards; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 35. `sc_w06_outro` — 6주차 · 농어가 끼어들자 아웃트로 · 3:2, 1200×800

대결: F(초파리 승, 새 생선 30마리: 표준화 100% 대 원자료 83.3%) · 표정 기준: 초파리 `fly_arms`, 주판봇 `robo_sigh`

대체 글: 수조 앞에서 팔짱 낀 초파리 연구원과 저울 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, the aquarium glowing behind, the fruit fly researcher with arms crossed holding the matched rubber ruler, the robot sighing over its scale, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 36. `sc_w07_outro` — 7주차 · 정확도 95%의 함정 아웃트로 · 3:2, 1200×800

대결: R(주판봇 승, 고객 1,000명당 순이익 639만 원 대 198만 원) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_happy`

대체 글: 동전 더미 앞에서 기뻐하는 주판봇과 커피를 든 초파리 연구원, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, the robot cheering with a stack of coins in front of the 2x2 board, the fruit fly researcher sipping coffee and nodding, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 37. `sc_w09_outro` — 9주차 · 숫자를 맞히는 선 아웃트로 · 3:2, 1200×800

대결: C(조건부: 범위 안 KNN 27g 대 곡선 47g, 범위 밖 KNN 485g 대 곡선 209g) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_calc`

대체 글: 두 과녁을 사이에 두고 커피를 든 초파리 연구원과 주판을 튕기는 주판봇, 턱을 괸 박사와 설명하는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, two archery targets side by side, one for small fish and one for big fish, the fruit fly researcher with a coffee cup, the robot tapping its abacus, the scientist with a hand on his chin, the girl pointing at both targets; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 38. `sc_w10_outro` — 10주차 · S자 곡선과 스무고개 아웃트로 · 3:2, 1200×800

대결: F(초파리 승, 시험 RMSE 53g 대 1,431g) · 표정 기준: 초파리 `fly_arms`, 주판봇 `robo_sigh`

대체 글: 차분한 곡선 앞에서 팔짱 낀 초파리 연구원과 튀어 오른 곡선 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, a calm curve on the chalkboard behind the fruit fly researcher with arms crossed, a wildly spiking curve behind the sighing robot, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 39. `sc_w11_outro` — 11주차 · 시간이 기억하는 숫자 아웃트로 · 3:2, 1200×800

대결: R(주판봇 승, 시험 12개월 MAPE 2.76% 대 4.47%) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_happy`

대체 글: 작년 장부를 펼친 주판봇이 기뻐하고 커피를 든 초파리 연구원이 달력을 보며, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, the robot cheering with last year's ledger open, the fruit fly researcher sipping coffee and looking at the calendar, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 40. `sc_w12_outro` — 12주차 · 숫자의 얼굴 아웃트로 · 3:2, 1200×800

대결: F(초파리 승, 결제액 MAE 중앙값이 평균보다 작음) · 표정 기준: 초파리 `fly_arms`, 주판봇 `robo_sigh`

대체 글: 가운데 인형 옆에서 팔짱 낀 초파리 연구원과 기운 시소 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, the fruit fly researcher with arms crossed beside the middle figurine, the robot sighing as the seesaw tips under the heavy weight, the scientist giving a thumbs-up, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 41. `sc_w13_outro` — 13주차 · 계기판을 설계하다 아웃트로 · 3:2, 1200×800

대결: C(조건부: 도달은 CPM, ROAS는 CPC) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_calc`

대체 글: 두 계기판을 사이에 두고 커피를 든 초파리 연구원과 주판을 튕기는 주판봇, 턱을 괸 박사와 설명하는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, two dashboards side by side, one showing reach and one showing coins, the fruit fly researcher with a coffee cup, the robot tapping its abacus, the scientist with a hand on his chin, the girl pointing at both; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 42. `sc_w14_outro` — 14주차 · 정답 없이, 글 속에서, 층을 쌓아 아웃트로 · 3:2, 1200×800

대결: D(무승부, 직선 문제: 신경망 89.75% 대 로지스틱 89.50%) · 표정 기준: 초파리 `fly_coffee`, 주판봇 `robo_meh`

대체 글: 같은 점수 카드 두 장 앞에서 커피를 든 초파리 연구원과 어깨를 으쓱하는 주판봇, 고개를 끄덕이는 박사와 웃는 조수

```
16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, inside the same night lab, two identical score cards side by side, one beside the layered tower and one beside a single ruler, the fruit fly researcher sipping coffee, the robot shrugging, the scientist nodding, the girl smiling; chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```
