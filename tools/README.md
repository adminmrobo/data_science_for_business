# 제작 도구 (다음 주차를 이어 만들 때)

주차 페이지는 `pages/wNN.py`(설정·지식 그래프·용어·퀴즈·문헌) + `pages/wNN.html`(본문) + `pages/wNN.js`(실험) 세 파일로 쓰고, 조립기가 공용 엔진·캐릭터 그림·데이터 블록을 넣어 저장소 맨 위에 **단일 HTML**로 만듭니다.

```bash
cd tools
python3 build.py 01 02 03      # 주차 페이지 조립 + data/KG_00_registry.json 갱신
python3 build_index.py         # 목차 (WEEKS 표의 ready를 True로 바꾸면 카드가 켜짐)
python3 build_docs.py          # docs/IMG_*.md, docs/COVER_*.md
node check.js ../week01_business_data_science.html   # 콘솔 오류·390px 넘침·대결 결과 점검 (Playwright)
```

- 캐릭터 그림: ai-lab-explainer 캐릭터 팩(`character_pack`, fruitfly-lab-expressions @ 5269662)에서 그 페이지에 쓰는 표정만 뽑습니다. 경로는 환경 변수 `PACK`으로 바꿀 수 있습니다.
- 공용 엔진: `engine.css`(디자인 토큰·구성 요소), `engine.js`(캐릭터·대결·용어 말풍선·퀴즈·지식 색인·꾸러미 ZIP).
- 조립기 점검: 끊긴 관계, 고립 노드, `relatedTo` 15% 초과면 멈춥니다.
