/* 오션마켓 글로벌 본사 3D — 목차(건물 전체)와 주차 페이지(이번 주의 층)를 같은 코드로 그린다.
   three.js는 CDN에서 읽는다. 읽지 못하면(오프라인·WebGL 없음) HTML 목록만 남는다. */
(function () {
  var raw = document.getElementById('bld-data');
  if (!raw) return;
  var DATA = JSON.parse(raw.textContent);
  var host = document.getElementById('tower3d') || document.getElementById('floor3d');
  if (!host) return;
  var MODE = host.id === 'tower3d' ? 'tower' : 'floor';
  var URL3 = 'https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js';
  var started = false;
  function start() {
    if (started) return; started = true;
    import(URL3).then(function (T) { try { (MODE === 'tower' ? tower : floor)(T); host.classList.add('on'); } catch (e) { console.warn('3D 건물을 그리지 못했습니다', e); } })
      .catch(function () { host.classList.add('off'); });
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { io.disconnect(); start(); } }); }, { rootMargin: '200px' });
    io.observe(host);
  } else start();

  /* ---------- 공통: 장면 · 카메라 · 끌어서 돌리기 · 라벨 ---------- */
  function stage(T, fit, opts) {
    var cv = document.createElement('canvas'); cv.className = 'bld-cv'; host.appendChild(cv);
    var lab = document.createElement('div'); lab.className = 'bld-labels'; host.appendChild(lab);
    var R = new T.WebGLRenderer({ canvas: cv, antialias: true, alpha: true });
    R.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
    R.shadowMap.enabled = true; R.shadowMap.type = T.PCFSoftShadowMap;
    var S = new T.Scene();
    var cam = new T.OrthographicCamera(-10, 10, 10, -10, 0.1, 400);
    S.add(new T.HemisphereLight('#dfe9ff', '#1b2330', 1.15));
    var sun = new T.DirectionalLight('#ffffff', 1.6); sun.position.set(18, 30, 12); sun.castShadow = true;
    sun.shadow.mapSize.set(1024, 1024); var sc = sun.shadow.camera; sc.left = -24; sc.right = 24; sc.top = 24; sc.bottom = -24; sc.far = 90; sun.shadow.bias = -0.0008;
    S.add(sun);
    var az = opts.az, el = opts.el, target = opts.target, dirty = true, labels = [];
    function place() {
      var d = 60; cam.position.set(target.x + d * Math.cos(el) * Math.sin(az), target.y + d * Math.sin(el), target.z + d * Math.cos(el) * Math.cos(az));
      cam.lookAt(target.x, target.y, target.z);
    }
    function size() {
      var w = host.clientWidth, h = host.clientHeight; if (!w || !h) return;
      R.setSize(w, h, false); var a = w / h, f = fit(a);
      cam.left = -f * a; cam.right = f * a; cam.top = f; cam.bottom = -f; cam.updateProjectionMatrix(); dirty = true;
    }
    function label(html, pos, cls, onclick) {
      var e = document.createElement(onclick ? 'button' : 'div'); e.className = 'bld-lb ' + (cls || ''); e.innerHTML = html;
      if (onclick) { e.type = 'button'; e.addEventListener('click', onclick); }
      lab.appendChild(e); var L = { el: e, pos: pos }; labels.push(L); return L;
    }
    var v = new T.Vector3();
    function drawLabels() {
      var w = host.clientWidth, h = host.clientHeight;
      labels.forEach(function (L) { v.copy(L.pos).project(cam); L.el.style.transform = 'translate(' + ((v.x + 1) / 2 * w).toFixed(1) + 'px,' + ((1 - v.y) / 2 * h).toFixed(1) + 'px)'; });
    }
    var anim = null;
    function loop() { requestAnimationFrame(loop); if (anim && anim()) dirty = true; if (!dirty) return; dirty = false; place(); R.render(S, cam); drawLabels(); }
    /* 끌기 = 돌리기, 짧게 누르기 = 고르기 */
    var down = null, ray = new T.Raycaster(), ndc = new T.Vector2();
    function pick(ev, list) {
      var r = cv.getBoundingClientRect(); ndc.set((ev.clientX - r.left) / r.width * 2 - 1, -(ev.clientY - r.top) / r.height * 2 + 1);
      ray.setFromCamera(ndc, cam); var hit = ray.intersectObjects(list, false)[0]; return hit ? hit.object : null;
    }
    cv.addEventListener('pointerdown', function (e) { down = { x: e.clientX, y: e.clientY, az: az, el: el, moved: false }; });
    window.addEventListener('pointerup', function () { setTimeout(function () { down = null; }, 0); });
    cv.addEventListener('pointermove', function (e) {
      if (down && (e.buttons & 1)) {
        var dx = e.clientX - down.x, dy = e.clientY - down.y;
        if (Math.abs(dx) + Math.abs(dy) > 5) { down.moved = true; az = down.az - dx * 0.008; el = Math.max(0.25, Math.min(1.1, down.el + dy * 0.005)); dirty = true; }
      }
    });
    cv.style.touchAction = 'pan-y';
    window.addEventListener('resize', size); size(); requestAnimationFrame(loop);
    return { T: T, S: S, R: R, cam: cam, cv: cv, label: label, pick: pick, dirtyNow: function () { dirty = true; }, wasDrag: function () { return down && down.moved; }, setAnim: function (f) { anim = f; }, reset: function () { az = opts.az; el = opts.el; dirty = true; } };
  }
  function kit(T, S) {
    var M = function (c, o) { return new T.MeshStandardMaterial(Object.assign({ color: c, roughness: .78, metalness: .05 }, o || {})); };
    function box(w, h, d, m, x, y, z, p) { var g = new T.Mesh(new T.BoxGeometry(w, h, d), typeof m === 'string' ? M(m) : m); g.position.set(x, y, z); g.castShadow = true; g.receiveShadow = true; (p || S).add(g); return g; }
    function cyl(r1, r2, h, m, x, y, z, p, seg) { var g = new T.Mesh(new T.CylinderGeometry(r1, r2, h, seg || 12), typeof m === 'string' ? M(m) : m); g.position.set(x, y, z); g.castShadow = true; (p || S).add(g); return g; }
    function tex(w, h, draw) { var c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); var t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t; }
    function tree(x, z, s) { s = s || 1; cyl(.08 * s, .1 * s, .5 * s, '#6b4f36', x, .25 * s, z); var c = new T.Mesh(new T.ConeGeometry(.45 * s, 1.1 * s, 8), M('#3f8f5f')); c.position.set(x, 1 * s, z); c.castShadow = true; S.add(c); }
    return { M: M, box: box, cyl: cyl, tex: tex, tree: tree };
  }
  function glow(T, hex) { return new T.Color(hex); }
  function narrow() { return host.clientWidth < 620; }

  /* ---------- 가구: 방의 성격을 한눈에 ---------- */
  function props(T, K, kind, g, w, d, color) {
    var dark = '#2c3640', light = '#e7ecef', wood = '#b08a63';
    function desk(x, z) { K.box(.9, .06, .5, wood, x, .42, z, g); K.box(.06, .4, .45, dark, x - .4, .2, z, g); K.box(.06, .4, .45, dark, x + .4, .2, z, g);
      K.box(.42, .28, .03, '#111a22', x, .62, z - .12, g); K.box(.38, .24, .01, K.M(color, { emissive: color, emissiveIntensity: .6 }), x, .62, z - .1, g);
      K.box(.3, .06, .3, '#46525e', x, .26, z + .45, g); K.box(.3, .3, .05, '#46525e', x, .45, z + .6, g); }
    if (kind === 'desk') { var n = w > 3 ? 3 : 2; for (var i = 0; i < n; i++) desk(-w / 2 + w / (n) * (i + .5), -.2); return; }
    if (kind === 'meet') { K.box(Math.min(2.4, w * .6), .07, .9, wood, 0, .42, 0, g); for (var j = -1; j <= 1; j++) { K.box(.3, .3, .3, '#46525e', j * .7, .2, .75, g); K.box(.3, .3, .3, '#46525e', j * .7, .2, -.75, g); }
      K.box(Math.min(1.6, w * .45), .9, .05, '#111a22', 0, 1.05, -d / 2 + .25, g); K.box(Math.min(1.5, w * .42), .8, .02, K.M(color, { emissive: color, emissiveIntensity: .5 }), 0, 1.05, -d / 2 + .28, g); return; }
    if (kind === 'server') { for (var s = 0; s < 4; s++) { var x = -w / 2 + .7 + s * .75; if (x > w / 2 - .4) break; K.box(.55, 1.5, .7, '#1d252d', x, .75, -.3, g);
      for (var l = 0; l < 5; l++) K.box(.5, .03, .02, K.M(l % 2 ? '#43e08a' : color, { emissive: l % 2 ? '#43e08a' : color, emissiveIntensity: 1 }), x, .3 + l * .25, .06, g); } return; }
    if (kind === 'lab') { K.box(Math.min(2.6, w * .7), .08, .8, light, 0, .48, -.1, g); K.box(Math.min(2.4, w * .65), .44, .7, '#8fa0ad', 0, .22, -.1, g);
      for (var c = 0; c < 3; c++) { K.box(.45, .25, .32, '#3a7fb8', -.6 + c * .6, .65, -.1, g); K.box(.36, .04, .26, '#cfe8ff', -.6 + c * .6, .79, -.1, g); }
      K.box(.5, .5, .5, '#d9a441', w / 2 - .6, .25, .7, g); return; }
    if (kind === 'screen') { var sw = Math.min(2.8, w * .75); K.box(sw, 1.2, .08, '#111a22', 0, 1.0, -d / 2 + .3, g);
      for (var r = 0; r < 2; r++) for (var q = 0; q < 3; q++) K.box(sw / 3 - .08, .5, .02, K.M(q === 1 && r === 0 ? '#f0b44c' : color, { emissive: q === 1 && r === 0 ? '#f0b44c' : color, emissiveIntensity: .7 }), -sw / 3 + q * sw / 3, .72 + r * .56, -d / 2 + .35, g);
      desk(0, .5); return; }
    if (kind === 'board') { K.box(Math.min(2, w * .55), 1, .05, '#f4f6f8', 0, 1.0, -d / 2 + .25, g); K.box(Math.min(2, w * .55), .06, .1, '#5a6570', 0, .48, -d / 2 + .27, g);
      for (var b = 0; b < 3; b++) K.box(.35, .04, .02, color, -.5 + b * .45, 1.1 - b * .18, -d / 2 + .28, g);
      K.cyl(.45, .45, .06, wood, 0, .42, .4, g, 20); K.cyl(.06, .06, .4, dark, 0, .2, .4, g); return; }
    if (kind === 'shelf') { for (var f = 0; f < 3; f++) { var sx = -w / 2 + .7 + f * .9; if (sx > w / 2 - .4) break; K.box(.75, 1.4, .35, '#6b4f36', sx, .7, -d / 2 + .35, g);
      for (var y = 0; y < 3; y++) K.box(.6, .3, .25, ['#5b8def', '#e07a5f', '#3fbf8f'][(f + y) % 3], sx, .3 + y * .42, -d / 2 + .38, g); } desk(0, .5); return; }
  }

  /* ---------- 목차: 건물 전체 ---------- */
  function tower(T) {
    var FL = DATA.floors, N = FL.length, W = 9, D = 6.4, H = 1.0, BASE = .7;
    var top = BASE + N * H;
    var st = stage(T, function (a) { return (a < .8 ? 12.6 : 11.6); }, { az: Math.PI / 4.6, el: .52, target: new T.Vector3(0, top / 2 + .4, 0) });
    var S = st.S, K = kit(T, S);
    /* 땅 · 광장 */
    var ground = new T.Mesh(new T.PlaneGeometry(60, 60), K.M('#16202a')); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; S.add(ground);
    var grid = new T.GridHelper(60, 60, '#24313d', '#1c2833'); grid.position.y = .005; S.add(grid);
    K.box(W + 5, .12, D + 5, '#33414d', 0, .06, 0);
    K.box(W + 1.2, BASE, D + 1.2, '#2a3540', 0, BASE / 2, 0);
    K.box(W * .5, BASE - .1, .05, K.M('#9fd8ff', { transparent: true, opacity: .55, emissive: '#3a8fd0', emissiveIntensity: .35 }), 0, BASE / 2, D / 2 + .62);
    [[-W / 2 - 1.8, D / 2 + 1.8], [W / 2 + 1.8, D / 2 + 1.8], [-W / 2 - 1.8, -D / 2 - 1.6], [W / 2 + 1.9, -.4], [-W / 2 - 1.9, .3]].forEach(function (p, i) { K.tree(p[0], p[1], .9 + (i % 2) * .2); });
    /* 광장의 지구본: 다국적 */
    var globe = new T.Mesh(new T.SphereGeometry(.75, 18, 12), new T.MeshStandardMaterial({ color: '#2fb5c4', wireframe: true, emissive: '#2fb5c4', emissiveIntensity: .6 }));
    globe.position.set(W / 2 + 1.2, 1.25, D / 2 + 2.2); S.add(globe); K.cyl(.35, .45, .4, '#46525e', W / 2 + 1.2, .2, D / 2 + 2.2);
    /* 옆 건물: 물류센터 · 데이터센터 */
    K.box(5, 2.2, 4, '#3b4752', -W / 2 - 5, 1.1, -3.5); K.box(4.6, .1, 3.6, '#56636e', -W / 2 - 5, 2.25, -3.5);
    K.box(4, 3.2, 3.4, '#2e3a46', W / 2 + 4.6, 1.6, -4.2);
    for (var r = 0; r < 4; r++) K.box(.08, .08, 3, K.M('#43e08a', { emissive: '#43e08a', emissiveIntensity: 1 }), W / 2 + 2.58, .7 + r * .6, -4.2);
    var bl = st.label('물류센터', new T.Vector3(-W / 2 - 5, 2.8, -3.5), 'mini'); var bl2 = st.label('데이터센터', new T.Vector3(W / 2 + 4.6, 3.6, -4.2), 'mini');
    /* 층 */
    var hits = [], floors = {};
    FL.forEach(function (f, i) {
      var g = new T.Group(); g.position.y = BASE + i * H; S.add(g);
      K.box(W, .12, D, '#d5dce2', 0, .06, 0, g);
      var col = glow(T, f.color);
      var glass = new T.Mesh(new T.BoxGeometry(W - .2, H - .12, D - .2), new T.MeshStandardMaterial({ color: col, transparent: true, opacity: .42, roughness: .15, metalness: .2, emissive: col, emissiveIntensity: .12 }));
      glass.position.y = .06 + (H - .12) / 2; g.add(glass); glass.userData.n = f.n; hits.push(glass);
      for (var k = 0; k <= 6; k++) { var x = -W / 2 + .1 + k * (W - .2) / 6; K.box(.06, H - .12, .06, '#1f2932', x, .06 + (H - .12) / 2, D / 2 - .08, g); }
      for (var k2 = 0; k2 <= 4; k2++) { var z = -D / 2 + .1 + k2 * (D - .2) / 4; K.box(.06, H - .12, .06, '#1f2932', W / 2 - .08, .06 + (H - .12) / 2, z, g); }
      for (var q = 0; q < 4; q++) K.box(.9, .32, .5, '#eef2f5', -W / 2 + 1.4 + q * 2.1, .28, -.6 + (q % 2) * 1.4, g);
      floors[f.n] = { g: g, glass: glass, base: g.position.y, f: f };
      var tx = f.n + 'F';
      floors[f.n].lb = st.label(tx, new T.Vector3(W / 2 + .1, BASE + i * H + H / 2, D / 2 + .1), 'fl', function () { location.href = f.file; });
      floors[f.n].lb.el.style.setProperty('--c', f.color); if (host.clientWidth < 480 && f.n % 2 === 0) floors[f.n].lb.el.style.display = 'none';
    });
    /* 옥상: 간판 · 헬리패드 · 안테나 */
    K.box(W, .2, D, '#c3cbd2', 0, top + .1, 0);
    K.box(2.2, .6, 1.6, '#7d8a95', -W / 2 + 1.8, top + .5, -D / 2 + 1.4); K.box(1.4, .5, 1.4, '#7d8a95', -W / 2 + 4, top + .45, -D / 2 + 1.2);
    var hp = new T.Mesh(new T.CylinderGeometry(1.25, 1.25, .06, 32), new T.MeshStandardMaterial({ map: K.tex(256, 256, function (c, w, h) { c.fillStyle = '#3b4752'; c.fillRect(0, 0, w, h); c.strokeStyle = '#f0b44c'; c.lineWidth = 14; c.beginPath(); c.arc(128, 128, 104, 0, 7); c.stroke(); c.fillStyle = '#ffffff'; c.font = 'bold 130px sans-serif'; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText('H', 128, 136); }) }));
    hp.position.set(W / 2 - 1.8, top + .23, .4); S.add(hp);
    K.cyl(.05, .05, 2.4, '#9aa6b0', -W / 2 + 1.2, top + 1.4, D / 2 - 1); var bk = K.box(.14, .14, .14, K.M('#ff5b5b', { emissive: '#ff5b5b', emissiveIntensity: 1.2 }), -W / 2 + 1.2, top + 2.65, D / 2 - 1);
    var sign = new T.Mesh(new T.PlaneGeometry(W - .6, 1.0), new T.MeshBasicMaterial({ transparent: true, map: K.tex(1024, 120, function (c, w, h) { c.fillStyle = 'rgba(16,22,30,.92)'; c.fillRect(0, 0, w, h); c.fillStyle = '#2fb5c4'; c.fillRect(0, h - 10, w, 10); c.fillStyle = '#ffffff'; c.font = 'bold 66px sans-serif'; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText(DATA.company.en, w / 2, h / 2 - 4); }) }));
    sign.position.set(0, top + .75, D / 2 - .02); S.add(sign); K.box(W - .4, .9, .08, '#10161e', 0, top + .7, D / 2 - .1);
    st.label('<b>' + DATA.company.name + '</b> 본사', new T.Vector3(0, top + 1.6, 0), 'co');
    /* 고르기 */
    var hover = 0, t0 = performance.now();
    function setHover(n) {
      if (hover === n) return; hover = n;
      Object.keys(floors).forEach(function (k) { var F = floors[k], on = +k === n; F.glass.material.opacity = on ? .85 : .42; F.glass.material.emissiveIntensity = on ? .6 : .12; F.lb.el.classList.toggle('hi', on); });
      document.querySelectorAll('[data-fl]').forEach(function (a) { a.classList.toggle('hi', +a.dataset.fl === n); });
      st.cv.style.cursor = n ? 'pointer' : 'grab'; st.dirtyNow();
    }
    st.setAnim(function () {
      var moved = false, now = performance.now();
      Object.keys(floors).forEach(function (k) { var F = floors[k], want = +k === hover ? .55 : 0, x = F.g.position.x; if (Math.abs(want - x) > .002) { F.g.position.x = x + (want - x) * .18; F.lb.pos.x = W / 2 + .1 + F.g.position.x; moved = true; } });
      globe.rotation.y = (now - t0) / 4000; bk.material.emissiveIntensity = (Math.sin(now / 400) > 0) ? 1.4 : .2;
      return true;
    });
    st.cv.addEventListener('pointermove', function (e) { if (st.wasDrag()) return; var o = st.pick(e, hits); setHover(o ? o.userData.n : 0); });
    st.cv.addEventListener('pointerleave', function () { setHover(0); });
    st.cv.addEventListener('click', function (e) { if (st.wasDrag()) return; var o = st.pick(e, hits); if (o) location.href = floors[o.userData.n].f.file; });
    document.querySelectorAll('[data-fl]').forEach(function (a) { a.addEventListener('mouseenter', function () { setHover(+a.dataset.fl); }); a.addEventListener('mouseleave', function () { setHover(0); }); });
    var rb = document.getElementById('bldReset'); if (rb) rb.addEventListener('click', st.reset);
  }

  /* ---------- 주차 페이지: 이번 주의 층 ---------- */
  function floor(T) {
    var cur = DATA.cur, F = DATA.floors[cur - 1], rooms = F.rooms.slice();
    var W = 16, D = 10, COR = 1.7;
    var slots = rooms.concat([{ id: '_core', name: '엘리베이터', prop: 'core' }]);
    var nTop = Math.ceil(slots.length / 2), nBot = slots.length - nTop, RD = (D - COR) / 2;
    var st = stage(T, function (a) { return a < 1.1 ? 11.2 : 7.0; }, { az: Math.PI / 5.2, el: .62, target: new T.Vector3(narrow() ? 1.4 : 0, .6, .4) });
    var S = st.S, K = kit(T, S), col = F.color;
    var ground = new T.Mesh(new T.PlaneGeometry(80, 80), K.M('#141c25')); ground.rotation.x = -Math.PI / 2; ground.position.y = -.4; ground.receiveShadow = true; S.add(ground);
    K.box(W + .6, .4, D + .6, '#cfd6dc', 0, -.2, 0);
    /* 뒤·왼쪽 바깥 유리벽(인형의 집처럼 앞은 열어 둔다) */
    var gm = new T.MeshStandardMaterial({ color: col, transparent: true, opacity: .16, roughness: .1 });
    var wb = new T.Mesh(new T.BoxGeometry(W + .6, 2.4, .08), gm); wb.position.set(0, 1.2, -D / 2 - .26); S.add(wb);
    var wl = new T.Mesh(new T.BoxGeometry(.08, 2.4, D + .6), gm); wl.position.set(-W / 2 - .26, 1.2, 0); S.add(wl);
    for (var c = 0; c <= 8; c++) K.box(.12, 2.4, .12, '#26313b', -W / 2 - .26 + c * (W + .52) / 8, 1.2, -D / 2 - .26);
    for (var c2 = 1; c2 <= 5; c2++) K.box(.12, 2.4, .12, '#26313b', -W / 2 - .26, 1.2, -D / 2 - .26 + c2 * (D + .52) / 5);
    /* 복도 */
    K.box(W, .05, COR, '#9aa6b0', 0, .025, 0);
    var hits = [], R = {}, nums = '①②③④⑤⑥';
    function room(s, i, row, n, gi) {
      var w = W / n, x = -W / 2 + w * (i + .5), z = row ? (COR / 2 + RD / 2) : -(COR / 2 + RD / 2);
      var g = new T.Group(); g.position.set(x, 0, z); S.add(g);
      if (s.prop === 'core') {
        K.box(w - .3, .06, RD - .3, '#3b4752', 0, .03, 0, g);
        K.box(Math.min(2.4, w * .6), 2.3, 1.4, '#2a333c', 0, 1.15, -RD / 2 + 1, g);
        for (var d = 0; d < 2; d++) { K.box(.7, 1.6, .04, '#b9c3cc', -.45 + d * .9, .82, -RD / 2 + 1.72, g); }
        var lbl = st.label('🛗 ' + cur + 'F · 엘리베이터', new T.Vector3(x, 2.7, z - RD / 2 + 1), 'core');
        return;
      }
      var isDuel = s.id === 'duel', tc = isDuel ? '#e07a5f' : col;
      var tile = new T.Mesh(new T.BoxGeometry(w - .25, .08, RD - .25), K.M(tc, { transparent: true, opacity: .32, emissive: tc, emissiveIntensity: .08 }));
      tile.position.y = .06; tile.receiveShadow = true; g.add(tile); tile.userData.id = s.id; hits.push(tile);
      var pm = new T.MeshStandardMaterial({ color: '#cfe6ff', transparent: true, opacity: .18, roughness: .05 });
      var side = new T.Mesh(new T.BoxGeometry(.05, 1.1, RD - .25), pm); side.position.set(w / 2 - .12, .6, 0); g.add(side);
      var back = new T.Mesh(new T.BoxGeometry(w - .25, 1.1, .05), pm); back.position.set(0, .6, row ? RD / 2 - .12 : -RD / 2 + .12); g.add(back);
      var inner = new T.Group(); g.add(inner); if (row) inner.rotation.y = Math.PI;
      props(T, K, s.prop, inner, w - .6, RD - .6, tc);
      if (isDuel) chars(T, g, w);
      var no = isDuel ? '⚔' : (s.id.indexOf('lv') === 0 ? nums[+s.id.slice(2) - 1] : nums[gi]);
      var L = st.label('<span class="no">' + no + '</span>' + (narrow() ? '' : '<span class="nm">' + s.name + '</span>'), new T.Vector3(x, 1.9, z), 'room' + (isDuel ? ' duel' : ''), function () { go(s.id); });
      R[s.id] = { tile: tile, L: L, g: g };
    }
    slots.slice(0, nTop).forEach(function (s, i) { room(s, i, 0, nTop, i); });
    slots.slice(nTop).forEach(function (s, i) { room(s, i, 1, nBot, nTop + i); });
    /* 대결 회의실의 네 캐릭터(그림이 있으면) */
    function chars(T, g, w) {
      var SP = window.SPRITE || {}, AL = window.SPRITE_ALIAS || {}, ks = ['fly_point', 'doc_front', 'asst_smile', 'robo_coin'], HR = [.41, 1.0, .9, .72]; /* 캐릭터 팩 C3 키 비율 */
      ks.forEach(function (k, i) { var src = SP[k] || SP[AL[k]]; if (!src) return; var t = new T.TextureLoader().load(src, function () { st.dirtyNow(); }); t.colorSpace = T.SRGBColorSpace;
        var sp = new T.Sprite(new T.SpriteMaterial({ map: t, transparent: true })); var h = 1.45 * HR[i]; sp.scale.set(h, h, 1); sp.center.set(.5, 0); sp.position.set(-w / 2 + .7 + i * (w - 1.4) / 3, .1, .9); g.add(sp); });
    }
    if (!narrow()) st.label('<b>' + cur + 'F</b> ' + F.dept, new T.Vector3(-W / 2 + .2, 3.0, -D / 2), 'flname');
    var hover = null;
    function setHover(id) {
      if (hover === id) return; hover = id;
      Object.keys(R).forEach(function (k) { var on = k === id; R[k].tile.material.opacity = on ? .75 : .32; R[k].tile.material.emissiveIntensity = on ? .5 : .08; R[k].L.el.classList.toggle('hi', on); });
      document.querySelectorAll('[data-room]').forEach(function (a) { a.classList.toggle('hi', a.dataset.room === id); });
      st.cv.style.cursor = id ? 'pointer' : 'grab'; st.dirtyNow();
    }
    function go(id) { var t = document.getElementById(id); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    st.cv.addEventListener('pointermove', function (e) { if (st.wasDrag()) return; var o = st.pick(e, hits); setHover(o ? o.userData.id : null); });
    st.cv.addEventListener('pointerleave', function () { setHover(null); });
    st.cv.addEventListener('click', function (e) { if (st.wasDrag()) return; var o = st.pick(e, hits); if (o) go(o.userData.id); });
    document.querySelectorAll('[data-room]').forEach(function (a) { a.addEventListener('mouseenter', function () { setHover(a.dataset.room); }); a.addEventListener('mouseleave', function () { setHover(null); }); });
    var rb = document.getElementById('bldReset'); if (rb) rb.addEventListener('click', st.reset);
  }
})();
