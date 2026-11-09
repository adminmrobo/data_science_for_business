#!/usr/bin/env python3
"""이미지 제작 명세서(IMG_*)와 글 표지 지시문(COVER_*)을 docs/에 쓴다. SKILL 18장·부록 D 틀."""
import os, json
from build import REPO, SERIES

DOC = '*chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie*'
ASST = '*girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans*'
FLY = '*anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings*'
ROBO = '*boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus*'
STYLE = '16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights, consistent with the reference images'
SEASON = 'cozy night laboratory mood, purple light, soft magenta and green fluorescent accents'
NO = 'no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands'
s = lambda t: t.strip('*')

PAGES = {
 'index': dict(title='비즈니스를 위한 데이터 과학 연구실 (목차)', key='index', anchor='B 연구실: 밤의 연구실 복도',
   place='a long night laboratory corridor with a row of doors, each door leaking a different colored light (one door per week)',
   meta='the doors themselves stand for the weeks of the course; a glowing open doorway in the middle',
   pose=('standing at the back center, pointing at the open glowing door', 'holding a blank clipboard, smiling toward the viewer', 'on the left facing right, peering at the nearest door with a magnifier', 'on the right facing left, rolling forward eagerly with the abacus raised'),
   alt='밤의 연구실 복도. 주차마다 다른 색 빛이 새는 문들 앞에 네 캐릭터가 서 있는 표지', duel=None, prev='(시리즈 첫 표지)'),
 '01': dict(title='1주차 · 데이터는 많은데, 결정은 왜 틀릴까', key='w01', anchor='B 연구실 + D 일상(우산 판매, 돌아온 비행기)',
   place='wide night laboratory with a large monitor showing a blank bar chart and four glowing stair blocks rising beside it',
   meta='four stacked steps of increasing brightness (data to wisdom) and a small toy airplane model with scattered white dots on its wings and body but none on its engines',
   pose=('at the back center with a hand on his chin, looking up the four steps', 'beside the monitor holding a striped blank ledger', 'on the left facing right, examining the toy airplane with a magnifier', 'on the right facing left, proudly pushing a cart piled with blank data cards'),
   alt='네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 밤의 연구실 표지', duel='F(초파리 승, 91.7% 대 56.8%)', prev='목차: 복도와 문들'),
 '02': dict(title='2주차 · 데이터는 어디서 오는가', key='w02', anchor='D 현장: 데이터 출처 → 연구실 서버',
   place='the night lab opened up like a map: a tiny bank counter, a factory sensor pole, a convenience store checkout and a smartphone, each sending streams of small glowing dots into a server rack',
   meta='streams of colored light dots flowing from four sources into one server rack, one stream fast and one slow',
   pose=('at the back center gesturing toward the server rack', 'kneeling by the checkout, labeling blank cards', 'on the left facing right, covering some dots with a translucent privacy sheet', 'on the right facing left, opening a big funnel to catch the fastest stream'),
   alt='네 캐릭터가 은행 창구, 공장 센서, 편의점 계산대, 스마트폰에서 서버로 흘러드는 빛줄기를 지켜보는 표지', duel='C(조건부: 사기 감시는 스트림, 월간 보고는 배치)', prev='1주차: 계단과 비행기 모형'),
 '03': dict(title='3주차 · 분석 전에 데이터를 손보다', key='w03', anchor='B 연구실: 데이터 손질 작업대',
   place='a big workbench in the night lab with a huge paper table spread out, some cells blank, some cells glowing red, a few duplicate cards stacked',
   meta='a giant table with holes being filled with green light, one oddly tall bar sticking out of the table, and a broom sweeping duplicate cards',
   pose=('at the back center pointing at a red cell with a pointer finger', 'filling a blank cell with a glowing green block', 'on the left facing right, holding scissors over a row with a blank cell, hesitating', 'on the right facing left, carrying a basket of glowing filler blocks'),
   alt='네 캐릭터가 빈칸과 튀는 값, 겹친 카드가 섞인 큰 표를 작업대 위에서 함께 손질하는 표지', duel='R(주판봇 승, 오차 28만 원 대 280만 원)', prev='2주차: 데이터 출처와 빛줄기'),
 '04': dict(title='4주차 · 도구와 알고리즘의 지도', key='w04', anchor='B 연구실: 도구 선반과 지도 탁자',
   place='a night lab with a tall tool shelf of glowing instruments and a large map table showing a scatter of red and green dots split by a curved line, a shopping basket on the corner',
   meta='a hand-drawn treasure map whose paths branch to different tools, and a straight ruler laid next to a curved glowing boundary between dots',
   pose=('at the back center unrolling the big map', 'checking items off a blank clipboard beside the shelf', 'on the left facing right, drawing a curved boundary with a glowing pen', 'on the right facing left, laying a straight ruler across the dots'),
   alt='네 캐릭터가 도구 선반과 점이 흩어진 지도 탁자 앞에서 직선 자와 곡선 경계를 견주는 표지', duel='R(주판봇 승, 대출 시험 정확도 88.5% 대 75.8%)', prev='3주차: 데이터 손질 작업대'),
 '05': dict(title='5주차 · 도미와 빙어', key='w05', anchor='B 연구실: 생선 계측대',
   place='a night lab workbench with a ruler, a kitchen scale, two buckets of fish (large silvery bream and small slim smelt) and a laptop showing a blank scatter plot',
   meta='fish being measured and turned into glowing dots that fly into the scatter plot on the laptop screen',
   pose=('at the back center holding up a large bream to look at it', 'writing blank labels and sticking them on small cards', 'on the left facing right, measuring a small smelt with a ruler', 'on the right facing left, placing a bream on the scale'),
   alt='네 캐릭터가 작업대 위 도미와 빙어를 자와 저울로 재며 노트북 산점도에 점을 찍는 표지', duel='D(무승부, 한 마리씩 빼고 채점: 둘 다 100%)', prev='4주차: 도구 선반과 지도'),
 '06': dict(title='6주차 · 농어가 끼어들자', key='w06', anchor='B 연구실: 수조와 두 바구니',
   place='a night lab with a glowing aquarium of three kinds of fish (big, medium, tiny), two baskets labeled only by color (one blue, one orange) and a long ruler and a scale side by side',
   meta='a stretched rubber ruler being pulled to the same length as a scale dial, showing two different units brought to one common scale',
   pose=('at the back center tapping the aquarium glass', 'sorting fish into the blue and orange baskets', 'on the left facing right, stretching the rubber ruler to match the scale dial', 'on the right facing left, weighing a fish and squinting at the big number'),
   alt='네 캐릭터가 도미·농어·빙어가 든 수조 앞에서 자의 눈금을 맞추고 생선을 훈련·시험 두 바구니로 나누는 표지', duel='F(초파리 승, 새 생선 30마리: 표준화 100% 대 원자료 83.3%)', prev='5주차: 생선 계측대'),
 '07': dict(title='7주차 · 정확도 95%의 함정', key='w07', anchor='B 연구실: 2×2 성적표와 저울',
   place='a night lab with a huge 2x2 grid board on the wall, each cell glowing a different color (green, red, amber, blue), a balance scale on the desk with two different weights',
   meta='a balance scale weighing two kinds of mistakes, one heavy coin and one light coin, in front of the four-cell board',
   pose=('at the back center pointing at the top-right cell of the board', 'counting tally marks on a blank clipboard', 'on the left facing right, holding a magnifier up to the biggest cell', 'on the right facing left, putting coins on the balance scale'),
   alt='네 캐릭터가 2×2 칸의 커다란 성적표 앞에서 저울로 두 종류의 오류 무게를 다는 표지', duel='R(주판봇 승, 고객 1,000명당 순이익 639만 원 대 198만 원)', prev='6주차: 수조와 두 바구니'),
 '09': dict(title='9주차 · 숫자를 맞히는 선', key='w09', anchor='B 연구실: 과녁과 저울',
   place='a night lab with an archery target on the wall, a kitchen scale with a medium fish on it, and a chalkboard full of dots with a smooth curve drawn through them',
   meta='arrows stuck around the bullseye at different distances, with faint lines measuring how far each one missed',
   pose=('at the back center drawing a smooth curve through dots on the chalkboard', 'reading the scale and writing a number on a blank card', 'on the left facing right, measuring a fish with a long ruler', 'on the right facing left, averaging five small fish cards with the abacus'),
   alt='네 캐릭터가 양궁 과녁 앞에서 농어를 저울에 올리고 칠판의 점들 위로 곡선을 긋는 표지', duel='C(조건부: 범위 안 KNN 27g 대 곡선 47g, 범위 밖 KNN 485g 대 곡선 209g)', prev='8주차 연습: 문제지 책상과 채점표'),
 '10': dict(title='10주차 · S자 곡선과 스무고개', key='w10', anchor='B 연구실: S자 칠판과 질문 나무',
   place='a night lab with a chalkboard showing a smooth S-shaped curve, a small potted tree whose branches end in colored marble jars, and a spice rack on the side',
   meta='a tree whose every branch split sorts marbles by color, next to a spice rack where some jars are almost empty',
   pose=('at the back center trimming a branch of the tree with small scissors', 'sorting colored marbles into two jars', 'on the left facing right, holding a spice jar and pouring just a pinch', 'on the right facing left, dumping a whole armful of spice jars into a pot'),
   alt='네 캐릭터가 S자 곡선이 그려진 칠판과 가지를 뻗은 질문 나무 앞에서 가위와 양념통을 든 표지', duel='F(초파리 승, 시험 RMSE 53g 대 1,431g)', prev='9주차: 과녁과 저울'),
 '11': dict(title='11주차 · 시간이 기억하는 숫자', key='w11', anchor='B 연구실: 긴 달력과 물결 그래프',
   place='a night lab with a very long wall calendar spanning six years and a glowing wavy sales line above it that peaks every December',
   meta='the same month in consecutive years connected by thin glowing threads, showing that this December remembers last December',
   pose=('at the back center tracing the wavy line with a pointer', 'cutting the long calendar strip into a training part and a test part', 'on the left facing right, studying a bar chart of correlations with a magnifier', 'on the right facing left, flipping open last year\'s ledger to the December page'),
   alt='네 캐릭터가 벽에 걸린 긴 달력과 물결치는 매출 그래프 앞에서 작년 같은 달을 손가락으로 짚는 표지', duel='R(주판봇 승, 시험 12개월 MAPE 2.76% 대 4.47%)', prev='10주차: S자 칠판과 질문 나무'),
 '12': dict(title='12주차 · 숫자의 얼굴', key='w12', anchor='B 연구실: 꼬리 긴 막대그래프와 시소',
   place='a night lab with a big histogram on the wall whose right tail stretches far, and a seesaw on the desk with two weights labeled only by color',
   meta='a seesaw tipped by one heavy weight far out on the right, while a small flag stands at the middle of the line of people',
   pose=('at the back center pointing at the long right tail of the histogram', 'lining up small figurines in order of height', 'on the left facing right, standing next to the middle figurine with arms open', 'on the right facing left, pushing the heavy weight further out on the seesaw'),
   alt='네 캐릭터가 한쪽으로 길게 늘어진 막대그래프와 시소 위의 평균·중앙값 추를 바라보는 표지', duel='F(초파리 승, 결제액 MAE 중앙값이 평균보다 작음)', prev='11주차: 긴 달력과 물결 그래프'),
 '13': dict(title='13주차 · 계기판을 설계하다', key='w13', anchor='B 연구실: 조종석 계기판',
   place='a night lab arranged like an airplane cockpit, with three round gauges, a glowing funnel diagram and a small warehouse shelf with boxes',
   meta='three gauge needles pulling against each other, and a funnel narrowing from many dots at the top to a few coins at the bottom',
   pose=('at the back center in the pilot seat looking at the gauges', 'plugging three different cables into one hub', 'on the left facing right, scattering many small light dots into the top of the funnel', 'on the right facing left, catching coins at the bottom of the funnel with the abacus'),
   alt='네 캐릭터가 항공기 조종석 같은 계기판 앞에서 깔때기 모양 광고 퍼널과 창고 선반을 살피는 표지', duel='C(조건부: 도달은 CPM, ROAS는 CPC)', prev='12주차: 꼬리 긴 막대그래프와 시소'),
 '14': dict(title='14주차 · 정답 없이, 글 속에서, 층을 쌓아', key='w14', anchor='B 연구실: 구슬 무리와 말풍선과 신경망 탑',
   place='a night lab with three clusters of glowing marbles on a table, a pile of speech-bubble cards on the floor, and a tower of connected glowing circles in layers',
   meta='marbles gathering by themselves into colored groups, speech bubbles sorted into a green tray and a red tray, and a layered tower of circles drawing a round boundary',
   pose=('at the back center looking up at the layered tower', 'sorting speech-bubble cards into green and red trays', 'on the left facing right, stacking one more layer of glowing circles on the tower', 'on the right facing left, drawing one straight line with a ruler across a sheet'),
   alt='네 캐릭터가 색깔별로 모인 구슬 무리, 말풍선 리뷰 더미, 층층이 쌓인 신경망 탑을 둘러보는 표지', duel='D(무승부, 직선 문제: 신경망 89.75% 대 로지스틱 89.50%)', prev='13주차: 조종석 계기판'),
 '08': dict(title='8주차 · 연습 ① 1~7주차 문제풀이', key='w08', anchor='B 연구실: 시험 전날 밤의 문제풀이 책상',
   place='a cozy night study corner of the laboratory with a long desk covered in blank answer sheets, seven small glowing folders stacked in a row, a desk lamp and a big wall chalkboard left blank',
   meta='seven small glowing folders lined up like a staircase (one per week reviewed), a red pencil and a stack of blank answer sheets with tick boxes',
   pose=('standing at the chalkboard holding a piece of chalk, looking back at the desk', 'holding a blank score sheet and a red pencil, cheerful', 'on the left facing right, scratching his helmet over an answer sheet with a pencil', 'on the right facing left, working fast on a wooden abacus beside a stack of sheets'),
   alt='밤의 연구실 공부 책상에서 네 캐릭터가 일곱 개의 빛나는 폴더와 빈 답안지를 앞에 두고 문제를 푸는 표지', duel=None, prev='7주차: 2×2 성적표와 저울'),
 '15': dict(title='15주차 · 연습 ② 9~14주차 문제풀이', key='w15', anchor='B 연구실: 마지막 밤의 복습 테이블',
   place='a round review table in the night laboratory at the end of the season, six glowing folders arranged in a circle, a calculator-like wooden abacus, colorful sticky notes on a corkboard behind, a window showing a winter night',
   meta='six glowing folders in a circle (one per week reviewed) around a single lit candle-like lamp, sticky notes without writing, a finished stack of answer sheets tied with ribbon',
   pose=('at the back center holding up a blank finished answer sheet proudly', 'pinning a blank sticky note on the corkboard', 'on the left facing right, flipping through a glowing folder with a magnifying glass', 'on the right facing left, tapping the abacus with one arm raised'),
   alt='한 시즌의 마지막 밤, 둥근 복습 테이블에 놓인 여섯 개의 빛나는 폴더를 네 캐릭터가 둘러싸고 마무리하는 표지', duel=None, prev='14주차: 구슬 무리와 신경망 탑'),
}

def prompt(p):
    d, a, f, r = p['pose']
    return ('Website top cover illustration, wide 16:9.\nMatch the art style, proportions and colors of the attached reference images exactly\n  (if there are no reference images: %s).\n%s.\nScene: %s.\n'
            'All four characters together:\n  %s, %s;\n  %s, %s;\n  %s, on the left facing right, %s;\n  %s, on the right facing left, %s.\n'
            'Visual metaphor of the topic: %s.\nComposition: keep every face and hand inside the central safe area (12%% margin left and right, 10%% top, 18%% bottom);\n'
            '  keep the bottom-left corner dark and simple; the light falls on the main prop.\nMood: curious, friendly rivalry, the moment before the result.\n%s.') % (
            STYLE.split(', consistent')[0], SEASON, p['place'], s(DOC), d, s(ASST), a, s(FLY), f, s(ROBO), r, p['meta'], NO.capitalize())

def cover_md(k, p):
    key = 'cover_' + p['key']
    return '''# 표지 지시문 — {t}

| 항목 | 내용 |
|---|---|
| 키 · 판 | {key} · L (16:9, 가로 1920 이상) |
| 장소 (앵커) | {anc} |
| 주제 은유 | {meta} |
| 네 캐릭터 포즈 | 박사: {p0} / 조수: {p1} / 초파리 연구원: {p2} / 주판봇: {p3} |
| 대체 글 (alt) | {alt} |
| 앞 표지와 다른 점 | 앞 표지: {prev}. 장소·소품·포즈를 겹치지 않게 함 |
| 결과 암시 | 없음 (대결 전 장면){duel} |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions`).

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

{pr}
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {{고칠 점}}. Still no text.`

**받은 뒤:** 그림을 돌려주면 SKILL 18-15 절차(비율·글자·네 캐릭터 확인 → WebP 1600×900·960×540 → 390·768·1280 폭 점검)로 `{key}` 자리에 넣습니다. 페이지는 그림이 없어도 대체 표지(CSS + 캐릭터 넷)로 완성 상태입니다.
'''.format(t=p['title'], key=key, anc=p['anchor'], meta=p['meta'], p0=p['pose'][0], p1=p['pose'][1], p2=p['pose'][2], p3=p['pose'][3], alt=p['alt'], prev=p['prev'],
           duel=(' · 이 페이지 대결 결과: ' + p['duel'] + ' — 표지에는 드러내지 않음') if p['duel'] else '', pr=prompt(p))

OUTRO = {'01': ('fly_arms', 'robo_sigh', 'a relaxed fruit fly researcher with arms crossed in quiet satisfaction on the left, a sheepish robot with a sweat drop on the right, the scientist giving a thumbs-up, the girl smiling with a striped ledger', '대결 후 팔짱 낀 초파리 연구원과 식은땀 흘리는 주판봇, 엄지를 세운 박사와 웃는 조수'),
         '02': ('fly_coffee', 'robo_calc', 'two task cards on a table between them, the fruit fly researcher holding a coffee cup calmly, the robot tapping its abacus, the scientist with a hand on his chin, the girl pointing at both cards', '두 업무 카드를 사이에 두고 커피를 든 초파리 연구원과 주판을 튕기는 주판봇, 턱을 괸 박사와 설명하는 조수'),
         '03': ('fly_coffee', 'robo_happy', 'a big table whose blank cells are now filled with green light, the robot cheering in front, the fruit fly researcher sipping coffee and nodding, the scientist giving a thumbs-up, the girl smiling', '빈칸이 채워진 표 앞에서 기뻐하는 주판봇과 커피를 든 초파리 연구원, 엄지를 세운 박사와 웃는 조수'),
         '04': ('fly_cry', 'robo_happy', 'the map table with a curved glowing boundary, the robot cheering beside it, the fruit fly researcher with teary eyes holding his straight ruler, the scientist giving a thumbs-up, the girl smiling', '곡선 경계 앞에서 기뻐하는 주판봇과 직선 자를 든 채 눈물 맺힌 초파리 연구원, 엄지를 세운 박사와 웃는 조수'),
         '05': ('fly_coffee', 'robo_meh', 'two identical score cards on the bench between the fish buckets, the fruit fly researcher sipping coffee, the robot shrugging, the scientist nodding, the girl holding up both cards', '같은 점수 카드 두 장을 사이에 두고 커피를 든 초파리 연구원과 어깨를 으쓱하는 주판봇, 고개를 끄덕이는 박사와 두 카드를 든 조수'),
         '06': ('fly_arms', 'robo_sigh', 'the aquarium glowing behind, the fruit fly researcher with arms crossed holding the matched rubber ruler, the robot sighing over its scale, the scientist giving a thumbs-up, the girl smiling', '수조 앞에서 팔짱 낀 초파리 연구원과 저울 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수'),
         '07': ('fly_coffee', 'robo_happy', 'the robot cheering with a stack of coins in front of the 2x2 board, the fruit fly researcher sipping coffee and nodding, the scientist giving a thumbs-up, the girl smiling', '동전 더미 앞에서 기뻐하는 주판봇과 커피를 든 초파리 연구원, 엄지를 세운 박사와 웃는 조수'),
         '09': ('fly_coffee', 'robo_calc', 'two archery targets side by side, one for small fish and one for big fish, the fruit fly researcher with a coffee cup, the robot tapping its abacus, the scientist with a hand on his chin, the girl pointing at both targets', '두 과녁을 사이에 두고 커피를 든 초파리 연구원과 주판을 튕기는 주판봇, 턱을 괸 박사와 설명하는 조수'),
         '10': ('fly_arms', 'robo_sigh', 'a calm curve on the chalkboard behind the fruit fly researcher with arms crossed, a wildly spiking curve behind the sighing robot, the scientist giving a thumbs-up, the girl smiling', '차분한 곡선 앞에서 팔짱 낀 초파리 연구원과 튀어 오른 곡선 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수'),
         '11': ('fly_coffee', 'robo_happy', 'the robot cheering with last year\'s ledger open, the fruit fly researcher sipping coffee and looking at the calendar, the scientist giving a thumbs-up, the girl smiling', '작년 장부를 펼친 주판봇이 기뻐하고 커피를 든 초파리 연구원이 달력을 보며, 엄지를 세운 박사와 웃는 조수'),
         '12': ('fly_arms', 'robo_sigh', 'the fruit fly researcher with arms crossed beside the middle figurine, the robot sighing as the seesaw tips under the heavy weight, the scientist giving a thumbs-up, the girl smiling', '가운데 인형 옆에서 팔짱 낀 초파리 연구원과 기운 시소 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수'),
         '13': ('fly_coffee', 'robo_calc', 'two dashboards side by side, one showing reach and one showing coins, the fruit fly researcher with a coffee cup, the robot tapping its abacus, the scientist with a hand on his chin, the girl pointing at both', '두 계기판을 사이에 두고 커피를 든 초파리 연구원과 주판을 튕기는 주판봇, 턱을 괸 박사와 설명하는 조수'),
         '14': ('fly_coffee', 'robo_meh', 'two identical score cards side by side, one beside the layered tower and one beside a single ruler, the fruit fly researcher sipping coffee, the robot shrugging, the scientist nodding, the girl smiling', '같은 점수 카드 두 장 앞에서 커피를 든 초파리 연구원과 어깨를 으쓱하는 주판봇, 고개를 끄덕이는 박사와 웃는 조수')}

def img_md(k, p):
    n = p['key']; fo, ro, scene, alt = OUTRO[k]
    hero = '%s, %s, 3:2 landscape scene, medium brightness, %s, %s at the back center, %s on the left facing right, %s on the right facing left, %s at the side, %s' % (STYLE, SEASON, p['place'], s(DOC), s(FLY), s(ROBO), s(ASST), NO)
    outro = '%s, %s, 3:2 landscape scene, medium brightness, inside the same night lab, %s; %s; %s; %s; %s; %s' % (STYLE, SEASON, scene, s(DOC), s(ASST), s(FLY), s(ROBO), NO)
    rows = [('cover_' + n, 'L', '1920×1080', '새로 (COVER_%s)' % k, 'P1', '맨 위 글 표지', '대체 표지(CSS + 캐릭터 넷)'),
            ('sc_%s_hero' % n, 'E', '1200×800', '새로', 'P1', '히어로 무대', '캔버스 무대 + 캐릭터 그림'),
            ('sc_%s_outro' % n, 'E', '1200×800', '새로', 'P2', '아웃트로', '없음(장면 생략)'),
            ('thumb_' + n, 'I', '600×400', '새로 (표지 3:2 자르기)', 'P2', '목차 카드', '이모지 카드'),
            ('og_' + n, 'K', '1200×630', '새로 (표지 자르기)', 'P3', '공유 미리보기', '없음'),
            ('표정 키 전부', 'A~D', '96px', '재사용 (캐릭터 팩 @5269662)', '—', '말풍선·대결·등장인물', '픽셀 지도'),
            ('행동으로 보기·실험 그림', '—', '—', '코드', '—', '캔버스', '—')]
    tbl = '\n'.join('| %d | %s |' % (i + 1, ' | '.join(r)) for i, r in enumerate(rows))
    man = {'page': n, 'anchor': p['anchor'], 'season': 'default', 'duel': p['duel'], 'images': [
        {'key': 'cover_' + n, 'plate': 'L', 'size': [1920, 1080], 'status': 'new', 'priority': 'P1', 'slot': 'cover', 'fallback': 'css-pixel-four', 'alt': p['alt']},
        {'key': 'sc_%s_hero' % n, 'plate': 'E', 'size': [1200, 800], 'status': 'new', 'priority': 'P1', 'slot': 'hero-stage', 'fallback': 'canvas-stage', 'alt': p['alt']},
        {'key': 'sc_%s_outro' % n, 'plate': 'E', 'size': [1200, 800], 'status': 'new', 'priority': 'P2', 'slot': 'outro', 'fallback': 'none', 'alt': alt},
        {'key': 'thumb_' + n, 'plate': 'I', 'size': [600, 400], 'status': 'new', 'priority': 'P2', 'slot': 'index-card', 'fallback': 'emoji-card'},
        {'key': 'og_' + n, 'plate': 'K', 'size': [1200, 630], 'status': 'new', 'priority': 'P3', 'slot': 'og', 'fallback': 'none'}]}
    return '''# {t} — 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | 저장소 맨 위의 해당 주차 HTML |
| 모드 / 주 앵커 | 교과서 모드 / {anc} |
| 시즌 | 기본 |
| 대결 | {duel} |
| 새로 그릴 그림 | P1 2장 · P2 2장 · P3 1장 |
| 재사용 | 표정 전부 (캐릭터 팩) |
| 그림이 없을 때 | 페이지는 캔버스 무대·대체 표지로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: SKILL 18-3 (16비트 RPG 픽셀아트, 굵은 외곽선, 2~3단계 명암)
- 캐릭터 고정 외형: 캐릭터 팩 18-4 (박사 · 조수 · 초파리 연구원 · 주판봇)
- 장소 영어 묘사: *{place}*
- 생물 앵커가 아니므로 현미경·초파리 해부 소품은 넣지 않음

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
{tbl}

## 3. 새로 그릴 그림 상세

### 3-1. `cover_{n}` — 글 표지
`COVER_{k}.md`를 그대로 씁니다.

### 3-2. `sc_{n}_hero` — 히어로 무대 (결과 암시 없음)
대체 글: {alt0}
```
{hero}
```

### 3-3. `sc_{n}_outro` — 아웃트로 (대결 후)
표정 기준(캐릭터 팩 5-8): 초파리 `{fo}`, 주판봇 `{ro}`. 대체 글: {alt}
```
{outro}
```

## 4. 일관성 지침
- 참고 이미지: 네 캐릭터 기본 그림 4장 + 이 시리즈의 첫 표지
- 같은 캐릭터는 같은 세션에서 연달아 만들기
- 투명 배경이 안 되면 *solid flat #00ff00 background*

## 5. 넘겨받은 뒤 처리
1. 크기 확인 → WebP 압축(표지 1600 220 KB 이하)
2. 단일 파일 페이지에 base64로 `SPRITE`에 키를 채움(`Object.assign(SPRITE,{{...}})`) → `data-scene`·`data-img` 자리가 자동으로 켜짐
3. 페이지 그림 합계 표지 포함 600 KB 이하 확인

## 6. 매니페스트
```json
{man}
```
'''.format(t=p['title'], anc=p['anchor'], duel=p['duel'], place=p['place'], tbl=tbl, n=n, k=k, hero=hero, outro=outro, fo=fo, ro=ro, alt=alt, alt0=p['alt'],
           man=json.dumps(man, ensure_ascii=False, indent=1))

PRACTICE = ('08', '15')
FILES = {'index': 'index.html', '01': 'week01_business_data_science.html', '02': 'week02_data_collection.html', '03': 'week03_analysis_prep.html',
         '04': 'week04_analysis_concepts.html', '05': 'week05_classification_1.html', '06': 'week06_classification_2.html', '07': 'week07_model_evaluation.html',
         '08': 'week08_practice_1.html', '09': 'week09_regression_1.html', '10': 'week10_regression_2.html', '11': 'week11_time_series.html',
         '12': 'week12_visualization.html', '13': 'week13_bi_kpi.html', '14': 'week14_advanced_analytics.html', '15': 'week15_practice_2.html'}
ORDER = ['index', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']

def img_practice_md(k, p):
    n = p['key']
    return '''# {t} — 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | {f} |
| 모드 / 주 앵커 | 연습(문제풀이) / {anc} |
| 대결 | 없음 (연습 페이지) |
| 새로 그릴 그림 | P1 1장 (표지) |
| 재사용 | 표정 전부 (캐릭터 팩) |
| 그림이 없을 때 | 대체 표지(CSS + 캐릭터 넷)로 이미 완성 상태 |

## 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|
| 1 | cover_{n} | L | 1920×1080 | 새로 (COVER_{k}) | P1 | 맨 위 글 표지 | 대체 표지(CSS + 캐릭터 넷) |
| 2 | thumb_{n} | I | 600×400 | 새로 (표지 3:2 자르기) | P2 | 목차 카드 | 이모지 카드 |
| 3 | og_{n} | K | 1200×630 | 새로 (표지 자르기) | P3 | 공유 미리보기 | 없음 |
| 4 | 표정 키 전부 | A~D | 96px | 재사용 (캐릭터 팩 @5269662) | — | 등장인물·말풍선 | 픽셀 지도 |

연습 페이지에는 히어로 무대·아웃트로 장면 자리가 없습니다. 표지 한 장이면 됩니다.
'''.format(t=p['title'], f=FILES[k], anc=p['anchor'], n=n, k=k)

def page_imgs(k, p):
    """(키, 판, 크기, 우선, 종류, 명세서) 목록"""
    n = p['key'] if k != 'index' else 'index'
    cov = 'COVER_%s.md' % ('00_index' if k == 'index' else k)
    out = [('cover_' + n, 'L', '1920×1080', 'P1', '그림(새로)', cov)]
    if k not in PRACTICE and k != 'index':
        out += [('sc_%s_hero' % n, 'E', '1200×800', 'P1', '그림(새로)', 'IMG_%s.md 3-2' % k),
                ('sc_%s_outro' % n, 'E', '1200×800', 'P2', '그림(새로)', 'IMG_%s.md 3-3' % k)]
    if k != 'index':
        out.append(('thumb_' + n, 'I', '600×400', 'P2', '표지 자르기', '—'))
    out.append(('og_' + n, 'K', '1200×630', 'P3', '표지 자르기', '—'))
    return out

def index_md():
    import re
    rows, total, faces, done = [], {'그림(새로)': 0, '표지 자르기': 0}, {}, 0
    for k in ORDER:
        p = PAGES[k]; f = FILES[k]
        try:
            h = open(os.path.join(REPO, f), encoding='utf-8').read()
        except OSError:
            h = ''
        have = set(re.findall(r'"([a-z0-9_]+)":"data:image', h))
        fs = sorted(set(re.findall(r'data-(?:img|mood)="((?:doc|asst|fly|robo)_[a-z]+)"', h)) | {w + '_' + m for w, m in re.findall(r'data-who="(doc|asst|fly|robo)" data-mood="([a-z]+)"', h)})
        faces[k] = fs
        for key, plate, size, pr, kind, spec in page_imgs(k, p):
            ok = key in have
            done += ok
            total[kind] += 1
            name = '목차' if k == 'index' else ('%d주차' % int(k))
            rows.append('| %s | `%s` | %s | %s | %s | %s | %s | %s |' % (name, key, kind, plate, size, pr, spec, '✅ 들어감' if ok else '☐ 없음'))
    allfaces = sorted(set(x for v in faces.values() for x in v))
    face_rows = '\n'.join('| %s | %s |' % ('목차' if k == 'index' else '%d주차' % int(k), ' · '.join('`%s`' % x for x in faces[k])) for k in ORDER)
    n_new, n_crop = total['그림(새로)'], total['표지 자르기']
    return '''# 이미지 전체 목록 (IMG_INDEX)

{series}에 들어가는 그림을 한곳에 모은 목록입니다. 주차별 상세 프롬프트는 각 명세서(`COVER_NN.md`, `IMG_NN.md`)에 있습니다.
이 파일은 `tools/build_docs.py`가 페이지 HTML을 읽어 만들므로, 그림을 넣은 뒤 다시 돌리면 상태 칸이 갱신됩니다.

## 1. 한눈에 보기

| 구분 | 장수 | 설명 |
|---|---|---|
| 새로 그릴 그림 | **{n_new}장** | 표지 16(목차 + 15주차) · 히어로 무대 13 · 아웃트로 13 |
| 표지에서 자르는 그림 | {n_crop}장 | 목차 카드(thumb, 3:2) 15 · 공유 미리보기(og, 1200×630) 16 — 따로 그리지 않음 |
| 재사용(캐릭터 팩) | 표정 {nf}종 | 이미 모든 페이지에 들어 있음. 새로 그리지 않음 |
| 지금 들어간 그림 | {done}장 | 나머지 페이지는 대체 표지·캔버스 무대로 이미 완성 상태 |

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
{rows}

## 4. 페이지별 재사용 표정 (캐릭터 팩 @5269662)

| 페이지 | 표정 키 |
|---|---|
{face_rows}

## 5. 넘겨주실 때
- 파일 이름을 키와 같게 해 주세요. 예: `cover_w07.png`, `sc_w07_hero.png`
- 받은 뒤 처리: 비율·글자·네 캐릭터 확인 → WebP(표지 1600×900, 220 KB 이하) → 페이지 `SPRITE`에 넣기 → 390·768·1280 폭 점검 → 이 목록 다시 생성
- 페이지 한 편의 그림 합계는 표지 포함 600 KB 이하로 둡니다.
'''.format(series=SERIES, n_new=n_new, n_crop=n_crop, nf=len(allfaces), done=done, rows='\n'.join(rows), face_rows=face_rows)

def main():
    d = os.path.join(REPO, 'docs'); os.makedirs(d, exist_ok=True)
    for k, p in PAGES.items():
        open(os.path.join(d, 'COVER_%s.md' % ('00_index' if k == 'index' else k)), 'w', encoding='utf-8').write(cover_md(k, p))
        if k in PRACTICE:
            open(os.path.join(d, 'IMG_%s.md' % k), 'w', encoding='utf-8').write(img_practice_md(k, p))
        elif k != 'index':
            open(os.path.join(d, 'IMG_%s.md' % k), 'w', encoding='utf-8').write(img_md(k, p))
    open(os.path.join(d, 'IMG_INDEX.md'), 'w', encoding='utf-8').write(index_md())
    print('docs written')

if __name__ == '__main__':
    main()
