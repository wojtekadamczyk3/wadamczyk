# Michelson Interferometer

A Michelson interferometer measures the intensity $I(x)$ at the detector as a function of the optical path difference $x = 2d$, where $d$ is how far the moving mirror has been displaced. For two monochromatic lines, each one contributes its own cosine fringe, and together they beat with period $1/\Delta\sigma$ (with $\sigma = 1/\lambda$). The spectrum is the Fourier transform of the measured part of $I(x)$. Scanning a length $L$ gives a resolution of about $\delta\sigma \approx 1/L$, i.e. $\delta\lambda \approx \lambda^2/L$. To separate the two lines you therefore have to scan at least one beat period.

<style>
  .mi-app {
    --mi-accent: #2f6bd8;
    --mi-l1: #d9822b;
    --mi-l2: #8a4fd8;
    --mi-mark: #e4572e;
    --mi-good: #1d8a4a;
    --mi-bad: #c62f2f;
    --mi-border: color-mix(in srgb, var(--md-default-fg-color, #000) 14%, transparent);
    --mi-soft: color-mix(in srgb, var(--md-default-fg-color, #000) 5%, transparent);
    border: 1px solid var(--mi-border);
    border-radius: 14px;
    padding: 18px;
    margin: 12px 0 20px;
    background: var(--md-default-bg-color, #fff);
    box-shadow: 0 10px 26px -18px rgba(0, 0, 0, 0.45);
  }
  .mi-head {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    gap: 6px 12px;
    margin-bottom: 12px;
  }
  .mi-head strong { font-size: 1rem; }
  .mi-head span { font-size: 0.8rem; opacity: 0.7; }
  .mi-groups { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
  .mi-group { border: 1px solid var(--mi-border); border-radius: 10px; padding: 4px 12px 10px; margin: 0; min-width: 0; }
  .mi-group legend { font-size: 0.8rem; font-weight: 700; padding: 0 6px; display: inline-flex; align-items: center; gap: 6px; }
  .mi-swatch { display: inline-block; width: 12px; height: 4px; border-radius: 2px; }
  .mi-row { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; font-size: 0.8rem; margin-top: 7px; }
  .mi-row output, .mi-num {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.76rem;
    font-weight: 600;
    white-space: nowrap;
  }
  .mi-num {
    width: 5.2em;
    padding: 1px 4px;
    border: 1px solid var(--mi-border);
    border-radius: 6px;
    background: transparent;
    color: inherit;
    text-align: right;
  }
  .mi-group input[type="range"] { width: 100%; margin: 3px 0 0; accent-color: var(--mi-accent); }
  .mi-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 10px; margin-top: 14px; }
  .mi-actions button {
    font: inherit;
    font-size: 0.8rem;
    font-weight: 600;
    border: 1px solid color-mix(in srgb, var(--mi-accent) 35%, transparent);
    border-radius: 10px;
    padding: 6px 12px;
    cursor: pointer;
    background: color-mix(in srgb, var(--mi-accent) 10%, var(--md-default-bg-color, #fff));
    color: var(--md-default-fg-color, #111);
  }
  .mi-actions button:active { transform: translateY(1px); }
  .mi-actions button.mi-primary { background: var(--mi-accent); color: #fff; min-width: 92px; }
  .mi-actions label { font-size: 0.8rem; display: inline-flex; align-items: center; gap: 5px; cursor: pointer; }
  .mi-actions input[type="checkbox"] { accent-color: var(--mi-accent); }
  .mi-actions select {
    font: inherit;
    font-size: 0.8rem;
    padding: 3px 6px;
    border-radius: 8px;
    border: 1px solid var(--mi-border);
    background: var(--md-default-bg-color, #fff);
    color: var(--md-default-fg-color, #111);
  }
  .mi-panels { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 14px; margin-top: 14px; }
  .mi-app figure { display: block; width: auto; max-width: none; margin: 0; min-width: 0; }
  .mi-app .mi-wide { margin-top: 14px; }
  .mi-app canvas {
    display: block;
    width: 100%;
    border: 1px solid var(--mi-border);
    border-radius: 10px;
    background: var(--md-default-bg-color, #fff);
  }
  #mi-setup, #mi-fringe { aspect-ratio: 4 / 3; }
  #mi-ifg { aspect-ratio: 16 / 6; cursor: ew-resize; touch-action: none; }
  #mi-spec { aspect-ratio: 16 / 7; }
  .mi-app figcaption { font-size: 0.75rem; opacity: 0.7; margin-top: 4px; text-align: center; }
  .mi-readout {
    margin-top: 12px;
    padding: 8px 10px;
    border-radius: 10px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.78rem;
    line-height: 1.65;
    background: var(--mi-soft);
    border: 1px solid var(--mi-border);
  }
  .mi-ok { color: var(--mi-good); font-weight: 700; }
  .mi-no { color: var(--mi-bad); font-weight: 700; }
  @media (max-width: 760px) {
    .mi-app { padding: 12px; }
    .mi-groups, .mi-panels { grid-template-columns: 1fr; }
    #mi-ifg { aspect-ratio: 4 / 2.4; }
    #mi-spec { aspect-ratio: 4 / 3; }
  }
</style>

<div class="mi-app" id="mi-app">
  <div class="mi-head">
    <strong>Michelson interferometer: from I(x) to the spectrum</strong>
    <span>Press Scan, or click and drag on I(x) to move the mirror</span>
  </div>
  <div class="mi-groups">
    <fieldset class="mi-group">
      <legend><span class="mi-swatch" style="background: var(--mi-l1)"></span>Beam 1</legend>
      <div class="mi-row"><label for="mi-l1">Wavelength λ₁</label><output id="mi-l1-v"></output></div>
      <input id="mi-l1" type="range" min="400" max="800" step="0.1" value="589" />
      <div class="mi-row"><label for="mi-a1">Intensity I₁</label><output id="mi-a1-v"></output></div>
      <input id="mi-a1" type="range" min="0" max="1" step="0.01" value="1" />
      <div class="mi-row"><label for="mi-n1">Intensity noise</label><output id="mi-n1-v"></output></div>
      <input id="mi-n1" type="range" min="0" max="100" step="1" value="0" />
    </fieldset>
    <fieldset class="mi-group">
      <legend><span class="mi-swatch" style="background: var(--mi-l2)"></span>Beam 2</legend>
      <div class="mi-row"><label for="mi-dl">Separation Δλ = λ₂ − λ₁</label><span><input id="mi-dl-box" class="mi-num" type="number" min="0.05" max="200" step="0.01" value="0.6" /> nm</span></div>
      <input id="mi-dl" type="range" min="0" max="1000" step="1" value="300" />
      <div class="mi-row"><label for="mi-a2">Intensity I₂</label><output id="mi-a2-v"></output></div>
      <input id="mi-a2" type="range" min="0" max="1" step="0.01" value="1" />
      <div class="mi-row"><label for="mi-n2">Intensity noise</label><output id="mi-n2-v"></output></div>
      <input id="mi-n2" type="range" min="0" max="100" step="1" value="0" />
    </fieldset>
    <fieldset class="mi-group">
      <legend>Measurement</legend>
      <div class="mi-row"><label for="mi-x0">Scan start (OPD)</label><output id="mi-x0-v"></output></div>
      <input id="mi-x0" type="range" min="0" max="4" step="0.001" value="0" />
      <div class="mi-row"><label for="mi-x1">Scan end (OPD)</label><output id="mi-x1-v"></output></div>
      <input id="mi-x1" type="range" min="0" max="4" step="0.001" value="1.2" />
      <div class="mi-row"><label for="mi-dx">Sampling step Δx</label><output id="mi-dx-v"></output></div>
      <input id="mi-dx" type="range" min="100" max="600" step="5" value="150" />
      <div class="mi-row"><label for="mi-nd">Detector noise</label><output id="mi-nd-v"></output></div>
      <input id="mi-nd" type="range" min="0" max="100" step="1" value="0" />
      <div class="mi-row"><label for="mi-T">Scan duration</label><output id="mi-T-v"></output></div>
      <input id="mi-T" type="range" min="2" max="30" step="1" value="8" />
    </fieldset>
  </div>
  <div class="mi-actions">
    <button id="mi-play" class="mi-primary">▶ Scan</button>
    <button id="mi-all">Measure whole range</button>
    <button id="mi-seed">New noise</button>
    <label><input id="mi-apod" type="checkbox" /> Apodise (Hann window)</label>
    <label><input id="mi-log" type="checkbox" /> Log spectrum</label>
    <select id="mi-view">
      <option value="zoom">Spectrum: zoom on the lines</option>
      <option value="full">Spectrum: full range (shows aliasing)</option>
    </select>
  </div>
  <div class="mi-panels">
    <figure>
      <canvas id="mi-setup"></canvas>
      <figcaption>(a) The interferometer. Mirror M₂ moves by d = x/2 (displacement exaggerated).</figcaption>
    </figure>
    <figure>
      <canvas id="mi-fringe"></canvas>
      <figcaption>(b) I(x) around the mirror position: beam 1, beam 2, their sum, and the measured samples (dots)</figcaption>
    </figure>
  </div>
  <figure class="mi-wide">
    <canvas id="mi-ifg"></canvas>
    <figcaption>(c) The interferogram I(x) over the measurement range. Click or drag to move the mirror.</figcaption>
  </figure>
  <figure class="mi-wide">
    <canvas id="mi-spec"></canvas>
    <figcaption>(d) Spectrum = |Fourier transform| of the measured part of I(x). The dashed lines mark the true wavelengths.</figcaption>
  </figure>
  <div class="mi-readout" id="mi-readout"></div>
</div>

<script>
(() => {
  const el = (id) => document.getElementById(id);
  const TAU = 2 * Math.PI;
  const X_SLIDER_MAX = 4000;   // µm of OPD
  const DL_MIN = 0.05, DL_MAX = 200;   // nm, log slider for Δλ

  const ui = {
    l1: el("mi-l1"), a1: el("mi-a1"), n1: el("mi-n1"),
    dl: el("mi-dl"), dlBox: el("mi-dl-box"), a2: el("mi-a2"), n2: el("mi-n2"),
    x0: el("mi-x0"), x1: el("mi-x1"), dx: el("mi-dx"), nd: el("mi-nd"), T: el("mi-T"),
    play: el("mi-play"), all: el("mi-all"), seed: el("mi-seed"),
    apod: el("mi-apod"), log: el("mi-log"), view: el("mi-view"),
    setup: el("mi-setup"), fringe: el("mi-fringe"), ifg: el("mi-ifg"), spec: el("mi-spec"), readout: el("mi-readout")
  };
  // lengths in µm throughout
  const state = {
    l1: 0.589, dl: 0.0006, a1: 1, a2: 1, n1: 0, n2: 0, nd: 0,
    x0: 0, x1: 1200, dx: 0.15, T: 8,
    pos: 1200, seed: 1, playing: false, lastTime: null,
    xs: new Float64Array(0), ys: new Float64Array(0), iStart: 0, ymin: 0, ymax: 1, genId: 0,
    spec: null, specKey: "", lastSpec: 0, bufs: {}
  };
  const l2 = () => state.l1 + state.dl;

  function css(name, fallback) {
    const v = getComputedStyle(ui.setup).getPropertyValue(name).trim();
    return v || fallback;
  }
  function wlColour(nm) {
    nm = Math.max(380, Math.min(780, nm));
    let r = 0, g = 0, b = 0;
    if (nm < 440) { r = (440 - nm) / 60; b = 1; }
    else if (nm < 490) { g = (nm - 440) / 50; b = 1; }
    else if (nm < 510) { g = 1; b = (510 - nm) / 20; }
    else if (nm < 580) { r = (nm - 510) / 70; g = 1; }
    else if (nm < 645) { r = 1; g = (645 - nm) / 65; }
    else r = 1;
    const f = nm < 420 ? 0.3 + 0.7 * (nm - 380) / 40 : nm > 700 ? 0.3 + 0.7 * (780 - nm) / 80 : 1;
    const c = (v) => Math.round(225 * Math.pow(Math.max(0, Math.min(1, v * f)), 0.8));
    return "rgb(" + c(r) + "," + c(g) + "," + c(b) + ")";
  }

  // ---------- reproducible noise: each sample position gets its own random numbers ----------
  function hash32(x) {
    x ^= x >>> 16; x = Math.imul(x, 0x7feb352d);
    x ^= x >>> 15; x = Math.imul(x, 0x846ca68b);
    x ^= x >>> 16;
    return x >>> 0;
  }
  function gauss(i, ch) {
    const h1 = hash32((i * 4 + ch) ^ hash32(state.seed * 7919 + ch * 104729));
    const h2 = hash32(h1 ^ 0x9e3779b9);
    const u1 = (h1 + 1) / 4294967297, u2 = h2 / 4294967296;
    return Math.sqrt(-2 * Math.log(u1)) * Math.cos(TAU * u2);
  }

  // ---------- measured interferogram on the grid x_i = i·Δx ----------
  function generate() {
    const { dx, a1, a2, n1, n2, nd } = state, lam1 = state.l1, lam2 = l2();
    const iStart = Math.ceil(state.x0 / dx - 1e-9), iEnd = Math.floor(state.x1 / dx + 1e-9);
    const N = Math.max(0, iEnd - iStart + 1);
    const xs = new Float64Array(N), ys = new Float64Array(N);
    const mean = (a1 + a2) / 2;
    let lo = 0, hi = 0.05;
    for (let n = 0; n < N; n++) {
      const i = iStart + n, x = i * dx;
      const e1 = n1 ? 1 + n1 * gauss(i, 0) : 1, e2 = n2 ? 1 + n2 * gauss(i, 1) : 1;
      let y = a1 * e1 * 0.5 * (1 + Math.cos(TAU * x / lam1)) + a2 * e2 * 0.5 * (1 + Math.cos(TAU * x / lam2));
      if (nd) y += nd * mean * gauss(i, 2);
      xs[n] = x; ys[n] = y;
      if (y < lo) lo = y;
      if (y > hi) hi = y;
    }
    const pad = 0.06 * (hi - lo);
    Object.assign(state, { xs, ys, iStart, ymin: lo < 0 ? lo - pad : 0, ymax: hi + pad, genId: state.genId + 1 });
  }
  function nAcq() {
    const N = state.xs.length;
    return Math.max(0, Math.min(N, Math.floor(state.pos / state.dx + 1e-9) - state.iStart + 1));
  }

  // ---------- spectrum: zero-padded FFT of the measured samples ----------
  function fft(re, im) {
    const n = re.length;
    for (let i = 1, j = 0; i < n; i++) {
      let bit = n >> 1;
      for (; j & bit; bit >>= 1) j ^= bit;
      j ^= bit;
      if (i < j) {
        let t = re[i]; re[i] = re[j]; re[j] = t;
        t = im[i]; im[i] = im[j]; im[j] = t;
      }
    }
    for (let len = 2; len <= n; len <<= 1) {
      const half = len >> 1, ang = -TAU / len, wr = Math.cos(ang), wi = Math.sin(ang);
      for (let i = 0; i < n; i += len) {
        let cr = 1, ci = 0;
        for (let k = 0; k < half; k++) {
          const a = i + k, b = a + half;
          const br = re[b] * cr - im[b] * ci, bi = re[b] * ci + im[b] * cr;
          re[b] = re[a] - br; im[b] = im[a] - bi;
          re[a] += br; im[a] += bi;
          const t = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = t;
        }
      }
    }
  }
  function computeSpectrum() {
    const n = nAcq(), apod = ui.apod.checked;
    const key = state.genId + "|" + n + "|" + apod;
    if (key === state.specKey) return;
    state.specKey = key;
    if (n < 4) { state.spec = null; return; }
    let nfft = 8192;
    while (nfft < 16 * n && nfft < 262144) nfft *= 2;
    if (!state.bufs[nfft]) state.bufs[nfft] = { re: new Float64Array(nfft), im: new Float64Array(nfft), mag: new Float64Array(nfft) };
    const { re, im, mag } = state.bufs[nfft];
    re.fill(0); im.fill(0);
    let mean = 0;
    for (let i = 0; i < n; i++) mean += state.ys[i];
    mean /= n;
    for (let i = 0; i < n; i++) re[i] = (state.ys[i] - mean) * (apod ? 0.5 * (1 - Math.cos(TAU * i / (n - 1))) : 1);
    fft(re, im);
    let mx = 0;
    for (let k = 0; k < nfft; k++) {
      mag[k] = Math.hypot(re[k], im[k]);
      if (k > 0 && k <= nfft / 2 && mag[k] > mx) mx = mag[k];
    }
    state.spec = { mag, nfft, max: mx || 1 };
  }
  // value shown in one pixel column covering FFT bins kA..kB (max if several bins, interpolated otherwise)
  function specColumn(kA, kB) {
    const { mag, nfft } = state.spec;
    const at = (k) => mag[((k % nfft) + nfft) % nfft];
    const lo = Math.min(kA, kB), hi = Math.max(kA, kB);
    if (hi - lo >= 1) {
      let v = 0;
      for (let k = Math.ceil(lo); k <= Math.floor(hi); k++) v = Math.max(v, at(k));
      return v;
    }
    const kc = (lo + hi) / 2, k0 = Math.floor(kc), f = kc - k0;
    return at(k0) * (1 - f) + at(k0 + 1) * f;
  }

  // ---------- drawing helpers ----------
  function fitCanvas(canvas) {
    const dpr = window.devicePixelRatio || 1;
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr); canvas.height = Math.round(h * dpr);
    }
    const ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    return { ctx, w, h };
  }
  function niceStep(span, target) {
    const raw = span / target, p = Math.pow(10, Math.floor(Math.log10(raw))), m = raw / p;
    return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p;
  }
  // grid, tick labels and axis titles; xs/ys map data → pixels, xFmt formats an x tick value
  function axes(ctx, P, pw, ph, h, xa, xb, ya, yb, xFmt, yTicks, yFmt, xLabel, yLabel) {
    const fg = css("--md-default-fg-color", "#222");
    const X = (v) => P.l + (v - xa) / (xb - xa) * pw, Y = (v) => P.t + ph * (1 - (v - ya) / (yb - ya));
    ctx.font = "11px sans-serif"; ctx.strokeStyle = fg; ctx.fillStyle = fg; ctx.lineWidth = 1;
    ctx.textAlign = "center";
    const step = niceStep(xb - xa, Math.max(3, Math.floor(pw / 85)));
    for (let v = Math.ceil(xa / step - 1e-9) * step; v <= xb + 1e-9 * step; v += step) {
      ctx.globalAlpha = 0.12; ctx.beginPath(); ctx.moveTo(X(v), P.t); ctx.lineTo(X(v), P.t + ph); ctx.stroke();
      ctx.globalAlpha = 0.7; ctx.fillText(xFmt(v, step), X(v), P.t + ph + 15);
    }
    ctx.textAlign = "right";
    for (const v of yTicks) {
      ctx.globalAlpha = 0.12; ctx.beginPath(); ctx.moveTo(P.l, Y(v)); ctx.lineTo(P.l + pw, Y(v)); ctx.stroke();
      ctx.globalAlpha = 0.7; ctx.fillText(yFmt(v), P.l - 6, Y(v) + 4);
    }
    ctx.globalAlpha = 0.3; ctx.strokeRect(P.l, P.t, pw, ph);
    ctx.globalAlpha = 0.85; ctx.textAlign = "center";
    ctx.fillText(xLabel, P.l + pw / 2, h - 4);
    ctx.save(); ctx.translate(12, P.t + ph / 2); ctx.rotate(-Math.PI / 2); ctx.fillText(yLabel, 0, 0); ctx.restore();
    ctx.globalAlpha = 1; ctx.textAlign = "left";
    return { X, Y };
  }
  const fmtStep = (v, step) => v.toFixed(Math.max(0, -Math.floor(Math.log10(step) + 1e-9)));
  function intensityTicks() {
    const step = niceStep(state.ymax - state.ymin, 4), t = [];
    for (let v = Math.ceil(state.ymin / step) * step; v <= state.ymax + 1e-9; v += step) t.push(v);
    return t;
  }

  // ---------- (a) set-up ----------
  function drawSetup() {
    const { ctx, w, h } = fitCanvas(ui.setup);
    const fg = css("--md-default-fg-color", "#222");
    const s = Math.min(w, h / 0.75);
    const cx = 0.40 * s, cy = 0.56 * h, arm = 0.22 * s;
    const off = 0.5 * arm * state.pos / X_SLIDER_MAX;
    const mx = cx + arm + off;
    const beam = wlColour(1000 * (state.l1 + l2()) / 2);
    const line = (x0, y0, x1, y1, col, wd, a) => {
      ctx.strokeStyle = col; ctx.lineWidth = wd; ctx.globalAlpha = a == null ? 1 : a;
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x1, y1); ctx.stroke(); ctx.globalAlpha = 1;
    };
    // beams (drawn with a dark outline so yellow stays visible)
    const beams = [[0.04 * s + 46, cy, cx, cy], [cx, cy, cx, cy - arm], [cx, cy, mx, cy], [cx, cy, cx, cy + 0.82 * arm]];
    for (const b of beams) line(b[0], b[1], b[2], b[3], fg, 5, 0.25);
    for (const b of beams) line(b[0], b[1], b[2], b[3], beam, 3, 1);
    // source
    ctx.fillStyle = fg; ctx.globalAlpha = 0.85;
    ctx.fillRect(0.04 * s, cy - 13, 46, 26);
    ctx.globalAlpha = 1; ctx.fillStyle = css("--md-default-bg-color", "#fff");
    ctx.font = "11px sans-serif"; ctx.textAlign = "center";
    ctx.fillText("source", 0.04 * s + 23, cy + 4);
    // beam splitter and mirrors
    line(cx - 15, cy + 15, cx + 15, cy - 15, fg, 3, 0.6);
    line(cx - 20, cy - arm, cx + 20, cy - arm, fg, 5, 0.9);
    line(mx, cy - 20, mx, cy + 20, css("--mi-mark", "#e4572e"), 5, 1);
    ctx.fillStyle = fg; ctx.font = "11px sans-serif";
    ctx.fillText("beam splitter", cx - 48, cy + 26);
    ctx.fillText("M₁ (fixed)", cx, cy - arm - 9);
    ctx.fillText("M₂ (moving)", mx, cy - 26);
    // travel range of M2 and displacement
    const r0 = cx + arm, r1 = cx + 1.5 * arm;
    line(r0, cy + 32, r1, cy + 32, fg, 1, 0.35);
    line(r0, cy + 28, r0, cy + 36, fg, 1, 0.35);
    line(cx + arm + 0.5 * arm * state.x0 / X_SLIDER_MAX, cy + 27, cx + arm + 0.5 * arm * state.x0 / X_SLIDER_MAX, cy + 37, css("--mi-accent", "#2f6bd8"), 2, 1);
    line(cx + arm + 0.5 * arm * state.x1 / X_SLIDER_MAX, cy + 27, cx + arm + 0.5 * arm * state.x1 / X_SLIDER_MAX, cy + 37, css("--mi-accent", "#2f6bd8"), 2, 1);
    ctx.fillStyle = css("--mi-mark", "#e4572e");
    ctx.beginPath(); ctx.moveTo(mx, cy + 32); ctx.lineTo(mx - 5, cy + 41); ctx.lineTo(mx + 5, cy + 41); ctx.closePath(); ctx.fill();
    ctx.fillStyle = fg; ctx.textAlign = "left";
    ctx.fillText("d = x/2 = " + (state.pos / 2000).toFixed(4) + " mm", r0 - 10, cy + 56);
    // detector and its reading
    const dy = cy + 0.82 * arm;
    ctx.fillStyle = fg; ctx.globalAlpha = 0.85; ctx.fillRect(cx - 18, dy, 36, 14); ctx.globalAlpha = 1;
    ctx.textAlign = "center"; ctx.fillText("detector", cx, dy + 28);
    const n = nAcq();
    const yv = n ? state.ys[n - 1] : 0;
    const frac = Math.max(0, Math.min(1, (yv - state.ymin) / (state.ymax - state.ymin)));
    const bx = cx + 30, bh = 0.7 * arm;
    ctx.strokeStyle = fg; ctx.globalAlpha = 0.4; ctx.strokeRect(bx, dy + 14 - bh, 10, bh); ctx.globalAlpha = 1;
    ctx.fillStyle = css("--mi-accent", "#2f6bd8"); ctx.fillRect(bx, dy + 14 - bh * frac, 10, bh * frac);
    ctx.fillStyle = fg; ctx.textAlign = "left"; ctx.fillText("I(x)", bx + 14, dy + 14 - bh * frac + 4);
    ctx.globalAlpha = 0.7; ctx.fillText("OPD x = 2d", 8, 16); ctx.globalAlpha = 1;
  }

  // ---------- (b) fringes near the mirror ----------
  function drawFringe() {
    const { ctx, w, h } = fitCanvas(ui.fringe);
    const P = { l: 44, r: 10, t: 10, b: 34 }, pw = w - P.l - P.r, ph = h - P.t - P.b;
    const W = 1.5;
    const { X, Y } = axes(ctx, P, pw, ph, h, -W, W, state.ymin, state.ymax, fmtStep,
      intensityTicks(), (v) => v.toFixed(1), "x − x_mirror  (µm)", "I(x)");
    const curve = (fn, col, wd, a) => {
      ctx.strokeStyle = col; ctx.lineWidth = wd; ctx.globalAlpha = a;
      ctx.beginPath();
      for (let p = 0; p <= pw; p++) {
        const u = -W + 2 * W * p / pw, v = fn(state.pos + u);
        if (p === 0) ctx.moveTo(X(u), Y(v)); else ctx.lineTo(X(u), Y(v));
      }
      ctx.stroke(); ctx.globalAlpha = 1;
    };
    const f1 = (x) => state.a1 * 0.5 * (1 + Math.cos(TAU * x / state.l1));
    const f2 = (x) => state.a2 * 0.5 * (1 + Math.cos(TAU * x / l2()));
    ctx.save(); ctx.beginPath(); ctx.rect(P.l, P.t, pw, ph); ctx.clip();
    curve(f1, css("--mi-l1", "#d9822b"), 1.4, 0.75);
    curve(f2, css("--mi-l2", "#8a4fd8"), 1.4, 0.75);
    curve((x) => f1(x) + f2(x), css("--md-default-fg-color", "#222"), 1.4, 0.55);
    ctx.strokeStyle = css("--mi-mark", "#e4572e"); ctx.globalAlpha = 0.6;
    ctx.beginPath(); ctx.moveTo(X(0), P.t); ctx.lineTo(X(0), P.t + ph); ctx.stroke(); ctx.globalAlpha = 1;
    const n = nAcq(), dx = state.dx;
    const iLo = Math.max(0, Math.ceil((state.pos - W) / dx) - state.iStart), iHi = Math.min(n - 1, Math.floor((state.pos + W) / dx) - state.iStart);
    ctx.fillStyle = css("--mi-accent", "#2f6bd8");
    for (let i = iLo; i <= iHi; i++) {
      ctx.beginPath(); ctx.arc(X(state.xs[i] - state.pos), Y(state.ys[i]), 3.2, 0, TAU); ctx.fill();
    }
    ctx.restore();
    ctx.font = "10.5px sans-serif"; ctx.globalAlpha = 0.85;
    ctx.fillStyle = css("--mi-l1", "#d9822b"); ctx.fillText("beam 1", P.l + 6, P.t + 12);
    ctx.fillStyle = css("--mi-l2", "#8a4fd8"); ctx.fillText("beam 2", P.l + 52, P.t + 12);
    ctx.fillStyle = css("--md-default-fg-color", "#222"); ctx.fillText("sum", P.l + 98, P.t + 12);
    ctx.fillStyle = css("--mi-accent", "#2f6bd8"); ctx.fillText("● measured", P.l + 126, P.t + 12);
    ctx.globalAlpha = 1;
  }

  // ---------- (c) interferogram ----------
  const IFG_PAD = { l: 44, r: 12, t: 10, b: 34 };
  function drawIfg() {
    const { ctx, w, h } = fitCanvas(ui.ifg);
    const P = IFG_PAD, pw = w - P.l - P.r, ph = h - P.t - P.b;
    const xa = state.x0, xb = Math.max(state.x1, state.x0 + 1e-3);
    const { X, Y } = axes(ctx, P, pw, ph, h, xa / 1000, xb / 1000, state.ymin, state.ymax, fmtStep,
      intensityTicks(), (v) => v.toFixed(1), "optical path difference x  (mm)", "I(x)");
    const Xu = (x) => X(x / 1000);
    const n = nAcq(), N = state.xs.length;
    ctx.save(); ctx.beginPath(); ctx.rect(P.l, P.t, pw, ph); ctx.clip();
    // not yet measured
    ctx.fillStyle = css("--md-default-fg-color", "#222"); ctx.globalAlpha = 0.05;
    ctx.fillRect(Xu(state.pos), P.t, P.l + pw - Xu(state.pos), ph);
    ctx.globalAlpha = 1;
    ctx.strokeStyle = css("--mi-accent", "#2f6bd8"); ctx.fillStyle = ctx.strokeStyle;
    if (N / pw < 2) {
      ctx.lineWidth = 1.2; ctx.beginPath();
      for (let i = 0; i < n; i++) { if (i === 0) ctx.moveTo(Xu(state.xs[i]), Y(state.ys[i])); else ctx.lineTo(Xu(state.xs[i]), Y(state.ys[i])); }
      ctx.stroke();
    } else {
      // many fringes per pixel: draw the min–max band, which shows the beat envelope
      const cols = Math.ceil(pw), mn = new Float64Array(cols).fill(Infinity), mxv = new Float64Array(cols).fill(-Infinity);
      for (let i = 0; i < n; i++) {
        const c = Math.min(cols - 1, Math.floor((state.xs[i] - xa) / (xb - xa) * pw));
        if (state.ys[i] < mn[c]) mn[c] = state.ys[i];
        if (state.ys[i] > mxv[c]) mxv[c] = state.ys[i];
      }
      for (let c = 0; c < cols; c++) {
        if (mn[c] === Infinity) continue;
        ctx.fillRect(P.l + c, Y(mxv[c]), 1, Math.max(1, Y(mn[c]) - Y(mxv[c])));
      }
    }
    ctx.strokeStyle = css("--mi-mark", "#e4572e"); ctx.lineWidth = 1.5;
    ctx.beginPath(); ctx.moveTo(Xu(state.pos), P.t); ctx.lineTo(Xu(state.pos), P.t + ph); ctx.stroke();
    ctx.restore();
    if (state.pos < xb - 1e-6) {
      ctx.fillStyle = css("--md-default-fg-color", "#222"); ctx.globalAlpha = 0.55; ctx.font = "11px sans-serif";
      ctx.textAlign = "right"; ctx.fillText("not measured yet", P.l + pw - 6, P.t + 14); ctx.textAlign = "left";
      ctx.globalAlpha = 1;
    }
  }

  // ---------- (d) spectrum ----------
  function zoomWindow() {
    const lc = (state.l1 + l2()) / 2, L = Math.max(state.x1 - state.x0, 4 * state.dx);
    let half = Math.max(0.6 * state.dl + 6 * lc * lc / L, 0.0005);
    half = Math.min(half, 0.2, lc - 0.1);
    return [lc - half, lc + half];
  }
  function drawSpec() {
    const { ctx, w, h } = fitCanvas(ui.spec);
    const fg = css("--md-default-fg-color", "#222");
    const P = { l: 44, r: 12, t: 22, b: 34 }, pw = w - P.l - P.r, ph = h - P.t - P.b;
    const full = ui.view.value === "full", logy = ui.log.checked;
    const lam1 = state.l1, lam2 = l2(), dx = state.dx;
    let xa, xb, kOf, toX, xFmt, xLabel;
    if (full) {
      xa = 0; xb = Math.max(1 / dx, 1.12 / lam1);
      xFmt = fmtStep; xLabel = "wavenumber σ = 1/λ  (µm⁻¹)";
      toX = (sigma) => sigma;
    } else {
      [xa, xb] = zoomWindow();
      xa *= 1000; xb *= 1000;
      xFmt = fmtStep; xLabel = "wavelength λ  (nm)";
      toX = (sigma) => 1000 / sigma;
    }
    const yTicks = logy ? [1e-4, 1e-3, 1e-2, 1e-1, 1] : [0, 0.25, 0.5, 0.75, 1];
    const yv = (v) => logy ? Math.max(-4, Math.log10(Math.max(v, 1e-6))) : v;
    const { X, Y } = axes(ctx, P, pw, ph, h, xa, xb, logy ? -4 : 0, logy ? 0.15 : 1.08, xFmt,
      yTicks.map(yv), (v) => logy ? "1e" + Math.round(v) : v.toFixed(2), xLabel, logy ? "|S| (log)" : "|S| (norm.)");
    ctx.save(); ctx.beginPath(); ctx.rect(P.l, P.t, pw, ph); ctx.clip();

    if (full) {
      const sN = 1 / (2 * dx);
      ctx.fillStyle = fg; ctx.globalAlpha = 0.05;
      ctx.fillRect(X(sN), P.t, P.l + pw - X(sN), ph);
      ctx.globalAlpha = 0.6; ctx.strokeStyle = fg; ctx.setLineDash([2, 3]);
      ctx.beginPath(); ctx.moveTo(X(sN), P.t); ctx.lineTo(X(sN), P.t + ph); ctx.stroke(); ctx.setLineDash([]);
      ctx.font = "10.5px sans-serif"; ctx.fillStyle = fg;
      ctx.fillText("Nyquist 1/(2Δx)", X(sN) + 4, P.t + ph - 6);
      ctx.globalAlpha = 1;
    }
    // true lines
    [[lam1, "--mi-l1", "#d9822b", "λ₁"], [lam2, "--mi-l2", "#8a4fd8", "λ₂"]].forEach(([lam, v, fb, lab], j) => {
      const xp = X(toX(1 / lam));
      ctx.strokeStyle = css(v, fb); ctx.globalAlpha = 0.85; ctx.lineWidth = 1.3; ctx.setLineDash([5, 4]);
      ctx.beginPath(); ctx.moveTo(xp, P.t); ctx.lineTo(xp, P.t + ph); ctx.stroke(); ctx.setLineDash([]);
      ctx.fillStyle = css(v, fb); ctx.font = "11px sans-serif"; ctx.globalAlpha = 1;
      ctx.textAlign = j === 0 ? "right" : "left";
      ctx.fillText(lab, xp + (j === 0 ? -4 : 4), P.t + 12);
    });
    ctx.textAlign = "left";

    if (state.spec) {
      const K = state.spec.nfft * dx;   // FFT bin index per unit σ
      const kAt = (px) => {
        const xv = xa + (xb - xa) * px / pw;
        return (full ? xv : 1000 / xv) * K;
      };
      const accent = css("--mi-accent", "#2f6bd8");
      ctx.beginPath();
      for (let p = 0; p < pw; p++) {
        const v = specColumn(kAt(p), kAt(p + 1)) / state.spec.max;
        const yy = Y(yv(v));
        if (p === 0) ctx.moveTo(P.l + p + 0.5, yy); else ctx.lineTo(P.l + p + 0.5, yy);
      }
      ctx.lineTo(P.l + pw, P.t + ph); ctx.lineTo(P.l, P.t + ph); ctx.closePath();
      ctx.fillStyle = accent; ctx.globalAlpha = 0.14; ctx.fill();
      ctx.globalAlpha = 1; ctx.strokeStyle = accent; ctx.lineWidth = 1.6; ctx.stroke();

      if (!full) {
        // resolution bar δλ ≈ λ²/L (twice that with the Hann window)
        const L = (nAcq() - 1) * dx, fac = ui.apod.checked ? 2 : 1;
        const dlam = 1000 * fac * lam1 * lam1 / L, xc = 1000 * (lam1 + lam2) / 2;
        const xA = X(xc - dlam / 2), xB = X(xc + dlam / 2), yb = P.t + ph - 14;
        ctx.strokeStyle = css("--mi-mark", "#e4572e"); ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(xA, yb - 5); ctx.lineTo(xA, yb + 5); ctx.moveTo(xA, yb); ctx.lineTo(xB, yb);
        ctx.moveTo(xB, yb - 5); ctx.lineTo(xB, yb + 5); ctx.stroke();
        ctx.fillStyle = css("--mi-mark", "#e4572e"); ctx.font = "11px sans-serif"; ctx.textAlign = "center";
        ctx.fillText("resolution δλ ≈ " + (fac > 1 ? "2" : "") + "λ²/L", Math.max(P.l + 70, Math.min(P.l + pw - 70, (xA + xB) / 2)), yb - 8);
        ctx.textAlign = "left";
      }
    } else {
      ctx.fillStyle = fg; ctx.globalAlpha = 0.6; ctx.font = "13px sans-serif"; ctx.textAlign = "center";
      ctx.fillText("Not enough data yet: scan further", P.l + pw / 2, P.t + ph / 2);
      ctx.textAlign = "left"; ctx.globalAlpha = 1;
    }
    ctx.restore();
  }

  // ---------- readout ----------
  function updateLabels() {
    el("mi-l1-v").textContent = (1000 * state.l1).toFixed(1) + " nm";
    el("mi-a1-v").textContent = state.a1.toFixed(2);
    el("mi-n1-v").textContent = Math.round(100 * state.n1) + " %";
    el("mi-a2-v").textContent = state.a2.toFixed(2);
    el("mi-n2-v").textContent = Math.round(100 * state.n2) + " %";
    el("mi-x0-v").textContent = (state.x0 / 1000).toFixed(3) + " mm";
    el("mi-x1-v").textContent = (state.x1 / 1000).toFixed(3) + " mm";
    el("mi-dx-v").textContent = Math.round(1000 * state.dx) + " nm";
    el("mi-nd-v").textContent = Math.round(100 * state.nd) + " %";
    el("mi-T-v").textContent = state.T + " s";
  }
  function updateReadout() {
    const lam1 = state.l1, lam2 = l2(), dx = state.dx, n = nAcq();
    const dsig = Math.abs(1 / lam1 - 1 / lam2);                 // µm⁻¹
    const L = Math.max(0, (n - 1) * dx), fac = ui.apod.checked ? 2 : 1;
    const res = L > 0 ? fac / L : Infinity;
    const ok = dsig >= res, nyqOk = Math.min(lam1, lam2) > 2 * dx;
    const yes = (b, t, f) => '<span class="' + (b ? "mi-ok" : "mi-no") + '">' + (b ? "✓ " + t : "✗ " + f) + "</span>";
    ui.readout.innerHTML =
      "λ₁ = " + (1000 * lam1).toFixed(2) + " nm, λ₂ = " + (1000 * lam2).toFixed(2) + " nm → Δσ = " + (1e4 * dsig).toFixed(2) + " cm⁻¹, " +
      "beat period in I(x): 1/Δσ = " + (1 / dsig / 1000).toFixed(3) + " mm<br>" +
      "measured L = " + (L / 1000).toFixed(3) + " mm (" + n + " samples) → δσ ≈ " + fac + "/L = " +
      (L > 0 ? (1e4 * res).toFixed(2) + " cm⁻¹, δλ ≈ " + (1000 * fac * lam1 * lam1 / L).toFixed(3) + " nm" : "—") + " &nbsp; " +
      yes(ok, "lines resolved", "not resolved: need L ≥ " + fac + "/Δσ = " + (fac / dsig / 1000).toFixed(3) + " mm") + "<br>" +
      "sampling Δx = " + Math.round(1000 * dx) + " nm → Nyquist: only λ > 2Δx = " + Math.round(2000 * dx) + " nm are measured correctly &nbsp; " +
      yes(nyqOk, "no aliasing", "aliased: λ = " + Math.round(1000 * Math.min(lam1, lam2)) + " nm is too short for this step");
  }

  function render(now) {
    if (!state.playing || !now || now - state.lastSpec > 90) {
      computeSpectrum();
      state.lastSpec = now || 0;
    }
    drawSetup(); drawFringe(); drawIfg(); drawSpec(); updateReadout();
  }
  function regenerate() { generate(); updateLabels(); render(); }

  // ---------- controls ----------
  const dlFromSlider = (p) => DL_MIN * Math.pow(DL_MAX / DL_MIN, p / 1000);
  const sliderFromDl = (d) => Math.round(1000 * Math.log(d / DL_MIN) / Math.log(DL_MAX / DL_MIN));
  function setDl(nm) {
    if (!Number.isFinite(nm)) return;
    nm = Math.max(DL_MIN, Math.min(DL_MAX, nm));
    state.dl = nm / 1000;
    regenerate();
  }
  ui.dl.addEventListener("input", () => {
    const nm = dlFromSlider(Number(ui.dl.value));
    ui.dlBox.value = nm < 1 ? nm.toFixed(3) : nm.toFixed(2);
    setDl(nm);
  });
  ui.dlBox.addEventListener("input", () => {
    setDl(Number(ui.dlBox.value));
    ui.dl.value = sliderFromDl(state.dl * 1000);
  });
  ui.dlBox.addEventListener("change", () => { ui.dlBox.value = Number((state.dl * 1000).toFixed(3)); });

  const bind = (input, key, scale) => input.addEventListener("input", () => { state[key] = Number(input.value) * scale; regenerate(); });
  bind(ui.l1, "l1", 1e-3); bind(ui.a1, "a1", 1); bind(ui.n1, "n1", 0.01);
  bind(ui.a2, "a2", 1); bind(ui.n2, "n2", 0.01); bind(ui.nd, "nd", 0.01); bind(ui.dx, "dx", 1e-3);
  ui.T.addEventListener("input", () => { state.T = Number(ui.T.value); updateLabels(); });

  function setRange(which) {
    const wasComplete = state.pos >= state.x1 - 1e-9;
    let x0 = Number(ui.x0.value) * 1000, x1 = Number(ui.x1.value) * 1000;
    if (x1 - x0 < 1) {
      if (which === "x0") x1 = Math.min(X_SLIDER_MAX, x0 + 1); else x0 = Math.max(0, x1 - 1);
      if (x1 - x0 < 1) x0 = x1 - 1;
      ui.x0.value = x0 / 1000; ui.x1.value = x1 / 1000;
    }
    state.x0 = x0; state.x1 = x1;
    state.pos = wasComplete ? x1 : Math.min(x1, Math.max(x0, state.pos));
    regenerate();
  }
  ui.x0.addEventListener("input", () => setRange("x0"));
  ui.x1.addEventListener("input", () => setRange("x1"));

  function setPlaying(on) {
    state.playing = on; state.lastTime = null;
    ui.play.textContent = on ? "❚❚ Pause" : "▶ Scan";
    if (on) requestAnimationFrame(tick); else render();
  }
  function tick(now) {
    if (!state.playing) return;
    if (state.lastTime !== null) {
      const dt = Math.min(0.1, (now - state.lastTime) / 1000);
      state.pos += (state.x1 - state.x0) * dt / state.T;
      if (state.pos >= state.x1) { state.pos = state.x1; setPlaying(false); return; }
      render(now);
    }
    state.lastTime = now;
    requestAnimationFrame(tick);
  }
  ui.play.addEventListener("click", () => {
    if (!state.playing && state.pos >= state.x1 - 1e-9) state.pos = state.x0;
    setPlaying(!state.playing);
  });
  ui.all.addEventListener("click", () => { state.pos = state.x1; setPlaying(false); });
  ui.seed.addEventListener("click", () => { state.seed += 1; regenerate(); });
  ui.apod.addEventListener("change", () => render());
  ui.log.addEventListener("change", () => render());
  ui.view.addEventListener("change", () => render());

  let dragging = false;
  function ifgPointer(e) {
    const rect = ui.ifg.getBoundingClientRect(), pw = rect.width - IFG_PAD.l - IFG_PAD.r;
    const f = (e.clientX - rect.left - IFG_PAD.l) / pw;
    state.pos = Math.min(state.x1, Math.max(state.x0, state.x0 + f * (state.x1 - state.x0)));
    render();
  }
  ui.ifg.addEventListener("pointerdown", (e) => {
    dragging = true; if (state.playing) { state.playing = false; ui.play.textContent = "▶ Scan"; }
    ui.ifg.setPointerCapture(e.pointerId); ifgPointer(e);
  });
  ui.ifg.addEventListener("pointermove", (e) => { if (dragging) ifgPointer(e); });
  ui.ifg.addEventListener("pointerup", () => { dragging = false; });
  ui.ifg.addEventListener("pointercancel", () => { dragging = false; });

  if (window.ResizeObserver) new ResizeObserver(() => render()).observe(ui.spec);
  window.addEventListener("resize", () => render());

  regenerate();
})();
</script>

## Things to try

1. **Watch the resolution build up.** With the sodium doublet (589.0 / 589.6 nm), press *Scan*. At first the spectrum is a single broad peak. The two lines separate once the scan has covered about one beat period of $I(x)$, $L \approx 1/\Delta\sigma \approx 0.58$ mm. Click on $I(x)$ to rewind and step through it.
2. **Closer lines need longer scans.** Make $\Delta\lambda$ smaller. The beats in $I(x)$ get longer, and you need a longer scan before the readout turns green. With the full 4 mm the limit is $\delta\lambda \approx \lambda^2/L \approx 0.09$ nm.
3. **Only the scan length matters.** Move the scan start away from zero. The resolution depends on $L = x_{\text{end}} - x_{\text{start}}$, not on where you measure.
4. **Noise.** Increase the intensity noise on one beam or the detector noise. The fringes in (b) scatter and the spectrum gets a noise floor (turn on *Log spectrum*). Scanning longer helps: the line height grows with the number of samples $N$, the noise only with $\sqrt N$.
5. **A weak line next to a strong one.** Set $I_2 = 0.1$ and choose $\Delta\lambda$ so the lines are just resolved. The weak line hides in the side lobes of the strong one. *Apodise* suppresses the side lobes, but each line becomes twice as broad.
6. **Sampling and aliasing.** Switch to *full range* and increase $\Delta x$ beyond $\lambda/2 \approx 295$ nm. Panel (b) shows fewer than two samples per fringe, and the lines jump below the Nyquist frequency to the wrong wavelength.
