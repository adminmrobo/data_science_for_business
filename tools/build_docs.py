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
         '06': ('fly_arms', 'robo_sigh', 'the aquarium glowing behind, the fruit fly researcher with arms crossed holding the matched rubber ruler, the robot sighing over its scale, the scientist giving a thumbs-up, the girl smiling', '수조 앞에서 팔짱 낀 초파리 연구원과 저울 앞에서 한숨 쉬는 주판봇, 엄지를 세운 박사와 웃는 조수')}

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

def main():
    d = os.path.join(REPO, 'docs'); os.makedirs(d, exist_ok=True)
    for k, p in PAGES.items():
        open(os.path.join(d, 'COVER_%s.md' % ('00_index' if k == 'index' else k)), 'w', encoding='utf-8').write(cover_md(k, p))
        if k != 'index':
            open(os.path.join(d, 'IMG_%s.md' % k), 'w', encoding='utf-8').write(img_md(k, p))
    print('docs written')

if __name__ == '__main__':
    main()
