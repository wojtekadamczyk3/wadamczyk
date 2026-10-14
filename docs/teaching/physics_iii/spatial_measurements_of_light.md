# Spatial measurements of light

## Interactive phasor simulation

By default every curve is divided by its own peak value $(1-R^N)^2$, so you compare line *shapes*. Untick *Normalise each curve to its peak* to see the absolute transmission. For a few phasors and high $R$ that number is tiny, because most of the light is still bouncing inside the etalon.

<style>
  .fp-app {
    --fp-accent: #2f6bd8;
    --fp-resultant: #e4572e;
    --fp-border: color-mix(in srgb, var(--md-default-fg-color, #000) 14%, transparent);
    --fp-soft: color-mix(in srgb, var(--md-default-fg-color, #000) 5%, transparent);
    border: 1px solid var(--fp-border);
    border-radius: 14px;
    padding: 18px;
    margin: 12px 0 20px;
    background: var(--md-default-bg-color, #fff);
    box-shadow: 0 10px 26px -18px rgba(0, 0, 0, 0.45);
  }
  .fp-head {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    justify-content: space-between;
    gap: 6px 12px;
    margin-bottom: 12px;
  }
  .fp-head strong { font-size: 1rem; }
  .fp-head span { font-size: 0.8rem; opacity: 0.7; }
  .fp-grid {
    display: grid;
    grid-template-columns: 210px 1fr 110px;
    gap: 10px 14px;
    align-items: center;
  }
  .fp-label { font-size: 0.85rem; }
  .fp-grid input[type="range"] { width: 100%; accent-color: var(--fp-accent); }
  .fp-grid select {
    font: inherit;
    font-size: 0.82rem;
    padding: 3px 6px;
    border-radius: 8px;
    border: 1px solid var(--fp-border);
    background: var(--md-default-bg-color, #fff);
    color: var(--md-default-fg-color, #111);
  }
  .fp-value {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.8rem;
    font-weight: 600;
    text-align: right;
    background: var(--fp-soft);
    border: 1px solid var(--fp-border);
    border-radius: 8px;
    padding: 3px 8px;
    white-space: nowrap;
  }
  .fp-num {
    width: 100%;
    box-sizing: border-box;
    color: inherit;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  }
  .fp-actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px 10px;
    margin-top: 14px;
  }
  .fp-actions button {
    font: inherit;
    font-size: 0.8rem;
    font-weight: 600;
    border: 1px solid color-mix(in srgb, var(--fp-accent) 35%, transparent);
    border-radius: 10px;
    padding: 6px 12px;
    cursor: pointer;
    background: color-mix(in srgb, var(--fp-accent) 10%, var(--md-default-bg-color, #fff));
    color: var(--md-default-fg-color, #111);
  }
  .fp-actions button:hover { filter: brightness(0.97); }
  .fp-actions button:active { transform: translateY(1px); }
  .fp-actions button.fp-primary { background: var(--fp-accent); color: #fff; min-width: 92px; }
  .fp-actions label { font-size: 0.8rem; display: inline-flex; align-items: center; gap: 5px; cursor: pointer; }
  .fp-actions input[type="checkbox"] { accent-color: var(--fp-accent); }
  .fp-panels {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1.7fr);
    gap: 14px;
    margin-top: 14px;
  }
  .fp-app .fp-panels figure { display: block; width: auto; max-width: none; margin: 0; min-width: 0; }
  .fp-panels canvas {
    display: block;
    width: 100%;
    border: 1px solid var(--fp-border);
    border-radius: 10px;
    background: var(--md-default-bg-color, #fff);
  }
  #fp-phasor { aspect-ratio: 1 / 1; }
  #fp-spectrum { aspect-ratio: 16 / 10; cursor: crosshair; touch-action: none; }
  .fp-panels figcaption { font-size: 0.75rem; opacity: 0.7; margin-top: 4px; text-align: center; }
  .fp-readout {
    margin-top: 12px;
    padding: 8px 10px;
    border-radius: 10px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 0.78rem;
    line-height: 1.6;
    background: var(--fp-soft);
    border: 1px solid var(--fp-border);
  }
  .fp-legend { display: flex; flex-wrap: wrap; gap: 6px 14px; margin-top: 10px; font-size: 0.78rem; }
  .fp-legend span { display: inline-flex; align-items: center; gap: 6px; }
  .fp-legend i { display: inline-block; width: 18px; height: 3px; border-radius: 2px; }
  .fp-legend i.fp-dashed { height: 0; border-top: 2px dashed currentColor; background: none !important; opacity: 0.7; }
  .fp-legend button {
    border: none; background: none; cursor: pointer; padding: 0 2px;
    color: inherit; opacity: 0.55; font-size: 0.9rem; line-height: 1;
  }
  .fp-legend button:hover { opacity: 1; }
  @media (max-width: 760px) {
    .fp-app { padding: 12px; }
    .fp-grid { grid-template-columns: 1fr auto; grid-auto-flow: row dense; gap: 4px 10px; }
    .fp-grid .fp-label { grid-column: 1; }
    .fp-grid .fp-value { grid-column: 2; }
    .fp-grid input[type="range"], .fp-grid select { grid-column: 1 / -1; }
    .fp-panels { grid-template-columns: 1fr; }
    #fp-phasor { max-width: 360px; margin: 0 auto; }
  }
</style>

<div class="fp-app" id="fp-app">
  <div class="fp-head">
    <strong>Fabry–Pérot etalon: phasor sum and transmission spectrum</strong>
    <span>Move the sliders, press Scan, or click and drag on the spectrum</span>
  </div>
  <div class="fp-grid">
    <div class="fp-label">Number of phasors N <small>(log scale)</small></div>
    <input id="fp-N" type="range" min="0" max="1000" step="1" value="301" />
    <input class="fp-value fp-num" id="fp-N-v" type="number" min="1" max="1000" step="1" value="8" />
    <div class="fp-label">Reflectivity R</div>
    <input id="fp-R" type="range" min="0" max="0.99" step="0.01" value="0.8" />
    <div class="fp-value" id="fp-R-v"></div>
    <div class="fp-label">OPD between successive phasors</div>
    <input id="fp-opd" type="range" min="0" max="3" step="0.0015" value="0.15" />
    <div class="fp-value" id="fp-opd-v"></div>
    <div class="fp-label">Scan window</div>
    <select id="fp-window">
      <option value="full">0 – 3 λ (three orders)</option>
      <option value="one">0 – 1 λ (one order)</option>
      <option value="zoom">0.9 – 1.1 λ (zoom on a peak)</option>
    </select>
    <div class="fp-value" id="fp-window-v"></div>
    <div class="fp-label">Scan duration (one sweep)</div>
    <input id="fp-speed" type="range" min="2" max="30" step="1" value="8" />
    <div class="fp-value" id="fp-speed-v"></div>
  </div>
  <div class="fp-actions">
    <button id="fp-play" class="fp-primary">▶ Scan</button>
    <button id="fp-hold">Hold curve</button>
    <button id="fp-clear-held">Clear held</button>
    <button id="fp-clear-trace">Clear trace</button>
    <label><input id="fp-theory" type="checkbox" checked /> Show predicted spectrum</label>
    <label><input id="fp-airy" type="checkbox" checked /> Airy limit (N → ∞)</label>
    <label><input id="fp-norm" type="checkbox" checked /> Normalise each curve to its peak</label>
  </div>
  <div class="fp-panels">
    <figure>
      <canvas id="fp-phasor"></canvas>
      <figcaption>Phasors in the complex plane: chain (blue) and resultant (red)</figcaption>
    </figure>
    <figure>
      <canvas id="fp-spectrum"></canvas>
      <figcaption>Transmitted intensity as a function of OPD. The solid line is the scanned trace.</figcaption>
    </figure>
  </div>
  <div class="fp-legend" id="fp-legend"></div>
  <div class="fp-readout" id="fp-readout"></div>
</div>

<script>
(() => {
  const el = (id) => document.getElementById(id);
  const ui = {
    N: el("fp-N"), Nbox: el("fp-N-v"), R: el("fp-R"), opd: el("fp-opd"), win: el("fp-window"), speed: el("fp-speed"),
    play: el("fp-play"), hold: el("fp-hold"), clearHeld: el("fp-clear-held"), clearTrace: el("fp-clear-trace"),
    theory: el("fp-theory"), airy: el("fp-airy"), norm: el("fp-norm"),
    phasor: el("fp-phasor"), spectrum: el("fp-spectrum"), legend: el("fp-legend"), readout: el("fp-readout")
  };

  const WINDOWS = { full: [0, 3], one: [0, 1], zoom: [0.9, 1.1] };
  const HOLD_COLOURS = ["#d9822b", "#2a9d8f", "#9b5de5", "#d6336c", "#6c757d", "#7a9a3a"];
  const MAX_HELD = HOLD_COLOURS.length;
  const N_MAX = 1000;
  const TRACE_BINS = 1500;
  const CURVE_SAMPLES = 3000;

  const state = {
    N: 8, R: 0.8, opd: 0.15, win: WINDOWS.full,
    playing: false, scanSeconds: 8, lastTime: null,
    held: [], nextColour: 0,
    trace: new Float64Array(TRACE_BINS).fill(NaN)
  };
  const curveCache = new Map();

  function css(name, fallback) {
    const v = getComputedStyle(ui.phasor).getPropertyValue(name).trim();
    return v || fallback;
  }

  // ---------- physics ----------
  // Transmitted field: (1-R) * sum_{k<N} (R e^{i delta})^k, built by repeated complex multiplication.
  function field(N, R, delta) {
    const wr = R * Math.cos(delta), wi = R * Math.sin(delta);
    let pr = 1 - R, pi = 0, re = 0, im = 0;
    for (let k = 0; k < N; k++) {
      re += pr; im += pi;
      const t = pr * wr - pi * wi;
      pi = pr * wi + pi * wr;
      pr = t;
    }
    return [re, im];
  }
  function transmission(N, R, delta) {
    const [re, im] = field(N, R, delta);
    return re * re + im * im;
  }
  function airy(R, delta) {
    const F = 4 * R / ((1 - R) * (1 - R));
    const s = Math.sin(delta / 2);
    return 1 / (1 + F * s * s);
  }
  const peakFinite = (N, R) => Math.pow(1 - Math.pow(R, N), 2);
  // Log-scale N slider: position 0..1000 maps to N = 1..N_MAX.
  const sliderToN = (pos) => Math.max(1, Math.min(N_MAX, Math.round(Math.pow(N_MAX, pos / 1000))));
  const nToSlider = (N) => Math.round(1000 * Math.log(N) / Math.log(N_MAX));
  const phase = (opd) => 2 * Math.PI * opd;

  function curve(N, R) {
    const [x0, x1] = state.win;
    const key = N + "|" + R + "|" + x0 + "|" + x1;
    let ys = curveCache.get(key);
    if (!ys) {
      ys = new Float64Array(CURVE_SAMPLES);
      for (let i = 0; i < CURVE_SAMPLES; i++) {
        const x = x0 + (x1 - x0) * i / (CURVE_SAMPLES - 1);
        ys[i] = transmission(N, R, phase(x));
      }
      if (curveCache.size > 40) curveCache.clear();
      curveCache.set(key, ys);
    }
    return ys;
  }
  function airyCurve(R) {
    const [x0, x1] = state.win;
    const key = "airy|" + R + "|" + x0 + "|" + x1;
    let ys = curveCache.get(key);
    if (!ys) {
      ys = new Float64Array(CURVE_SAMPLES);
      for (let i = 0; i < CURVE_SAMPLES; i++) {
        ys[i] = airy(R, phase(x0 + (x1 - x0) * i / (CURVE_SAMPLES - 1)));
      }
      curveCache.set(key, ys);
    }
    return ys;
  }

  // ---------- recorded trace ----------
  function binOf(x) {
    const [x0, x1] = state.win;
    return Math.round((x - x0) / (x1 - x0) * (TRACE_BINS - 1));
  }
  function binX(i) {
    const [x0, x1] = state.win;
    return x0 + (x1 - x0) * i / (TRACE_BINS - 1);
  }
  function record(from, to) {
    let a = binOf(to), b = from === null ? a : binOf(from);
    if (a > b) { const t = a; a = b; b = t; }
    a = Math.max(0, a); b = Math.min(TRACE_BINS - 1, b);
    for (let i = a; i <= b; i++) state.trace[i] = transmission(state.N, state.R, phase(binX(i)));
  }
  function clearTrace() { state.trace.fill(NaN); }

  // ---------- canvas helpers ----------
  function fitCanvas(canvas) {
    const dpr = window.devicePixelRatio || 1;
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(h * dpr);
    }
    const ctx = canvas.getContext("2d");
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx, w, h };
  }
  function arrow(ctx, x0, y0, x1, y1, colour, width) {
    const dx = x1 - x0, dy = y1 - y0, len = Math.hypot(dx, dy);
    if (len < 0.4) return;
    const head = Math.min(9, 0.4 * len);
    const ux = dx / len, uy = dy / len;
    ctx.strokeStyle = colour; ctx.fillStyle = colour; ctx.lineWidth = width;
    ctx.beginPath();
    ctx.moveTo(x0, y0);
    ctx.lineTo(x1 - ux * head * 0.6, y1 - uy * head * 0.6);
    ctx.stroke();
    if (len > 3) {
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x1 - ux * head - uy * head * 0.45, y1 - uy * head + ux * head * 0.45);
      ctx.lineTo(x1 - ux * head + uy * head * 0.45, y1 - uy * head - ux * head * 0.45);
      ctx.closePath();
      ctx.fill();
    }
  }
  function niceStep(span, target) {
    const raw = span / target, p = Math.pow(10, Math.floor(Math.log10(raw))), m = raw / p;
    return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * p;
  }

  // ---------- phasor diagram ----------
  function drawPhasors() {
    const { ctx, w, h } = fitCanvas(ui.phasor);
    const fg = css("--md-default-fg-color", "#222");
    ctx.clearRect(0, 0, w, h);
    const { N, R } = state, delta = phase(state.opd);
    const L = Math.max(1 - Math.pow(R, N), 1e-9);  // total chain length = largest possible resultant
    const cx = w / 2, cy = h / 2, scale = (Math.min(w, h) / 2 - 16) / L;

    ctx.save();
    ctx.globalAlpha = 0.25; ctx.strokeStyle = fg; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(8, cy); ctx.lineTo(w - 8, cy); ctx.moveTo(cx, 8); ctx.lineTo(cx, h - 8); ctx.stroke();
    ctx.setLineDash([4, 4]);
    ctx.beginPath(); ctx.arc(cx, cy, L * scale, 0, 2 * Math.PI); ctx.stroke();
    ctx.restore();
    ctx.fillStyle = fg; ctx.globalAlpha = 0.55; ctx.font = "11px sans-serif";
    ctx.fillText("Re", w - 24, cy - 6); ctx.fillText("Im", cx + 6, 18);
    ctx.globalAlpha = 1;

    let x = 0, y = 0, a = 1 - R;
    for (let k = 0; k < N; k++) {
      const nx = x + a * Math.cos(k * delta), ny = y + a * Math.sin(k * delta);
      const t = N > 1 ? k / (N - 1) : 0;
      const colour = "hsl(" + (215 + 55 * t) + ", 70%, " + (45 + 15 * t) + "%)";
      arrow(ctx, cx + x * scale, cy - y * scale, cx + nx * scale, cy - ny * scale, colour, 1.6);
      x = nx; y = ny; a *= R;
    }
    arrow(ctx, cx, cy, cx + x * scale, cy - y * scale, css("--fp-resultant", "#e4572e"), 2.6);

    ctx.fillStyle = fg; ctx.font = "12px sans-serif";
    ctx.fillText("|E|² = " + (x * x + y * y).toFixed(3), 10, h - 12);
  }

  // ---------- spectrum ----------
  function drawSpectrum() {
    const { ctx, w, h } = fitCanvas(ui.spectrum);
    const fg = css("--md-default-fg-color", "#222");
    const accent = css("--fp-accent", "#2f6bd8");
    const norm = ui.norm.checked;
    const [x0, x1] = state.win;
    const pad = { l: 44, r: 12, t: 12, b: 34 };
    const pw = w - pad.l - pad.r, ph = h - pad.t - pad.b;
    const yMax = 1.05;
    const X = (x) => pad.l + (x - x0) / (x1 - x0) * pw;
    const Y = (v) => pad.t + ph * (1 - v / yMax);
    ctx.clearRect(0, 0, w, h);

    // grid + ticks
    ctx.font = "11px sans-serif"; ctx.fillStyle = fg; ctx.strokeStyle = fg; ctx.lineWidth = 1;
    ctx.textAlign = "right";
    for (let v = 0; v <= 1.0001; v += 0.25) {
      ctx.globalAlpha = 0.12; ctx.beginPath(); ctx.moveTo(pad.l, Y(v)); ctx.lineTo(pad.l + pw, Y(v)); ctx.stroke();
      ctx.globalAlpha = 0.7; ctx.fillText(v.toFixed(2), pad.l - 6, Y(v) + 4);
    }
    const step = niceStep(x1 - x0, Math.max(3, Math.floor(pw / 80)));
    const digits = Math.max(0, -Math.floor(Math.log10(step) + 1e-9));
    ctx.textAlign = "center";
    for (let x = Math.ceil(x0 / step - 1e-9) * step; x <= x1 + 1e-9; x += step) {
      ctx.globalAlpha = 0.12; ctx.beginPath(); ctx.moveTo(X(x), pad.t); ctx.lineTo(X(x), pad.t + ph); ctx.stroke();
      ctx.globalAlpha = 0.7; ctx.fillText(x.toFixed(digits), X(x), pad.t + ph + 15);
    }
    ctx.globalAlpha = 0.3; ctx.strokeRect(pad.l, pad.t, pw, ph);
    ctx.globalAlpha = 0.85;
    ctx.fillText("OPD / λ", pad.l + pw / 2, h - 4);
    ctx.save(); ctx.translate(12, pad.t + ph / 2); ctx.rotate(-Math.PI / 2);
    ctx.fillText(norm ? "I / I_peak" : "I_t / I_0", 0, 0); ctx.restore();
    ctx.globalAlpha = 1; ctx.textAlign = "left";

    ctx.save();
    ctx.beginPath(); ctx.rect(pad.l, pad.t, pw, ph); ctx.clip();
    const line = (ys, scaleBy, colour, width, alpha, dash) => {
      ctx.strokeStyle = colour; ctx.lineWidth = width; ctx.globalAlpha = alpha; ctx.setLineDash(dash || []);
      ctx.beginPath();
      let pen = false;
      for (let i = 0; i < ys.length; i++) {
        if (Number.isNaN(ys[i])) { pen = false; continue; }
        const px = pad.l + pw * i / (ys.length - 1), py = Y(ys[i] / scaleBy);
        if (pen) ctx.lineTo(px, py); else { ctx.moveTo(px, py); pen = true; }
      }
      ctx.stroke();
      ctx.globalAlpha = 1; ctx.setLineDash([]);
    };

    for (const hc of state.held) {
      line(curve(hc.N, hc.R), norm ? peakFinite(hc.N, hc.R) : 1, hc.colour, 1.6, 0.9);
    }
    if (ui.airy.checked) line(airyCurve(state.R), 1, fg, 1.3, 0.55, [6, 4]);
    const peak = norm ? Math.max(peakFinite(state.N, state.R), 1e-12) : 1;
    if (ui.theory.checked) line(curve(state.N, state.R), peak, accent, 1.5, 0.3);
    line(state.trace, peak, accent, 2.2, 1);

    // marker
    const T = transmission(state.N, state.R, phase(state.opd));
    ctx.strokeStyle = css("--fp-resultant", "#e4572e"); ctx.globalAlpha = 0.6; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(X(state.opd), pad.t); ctx.lineTo(X(state.opd), pad.t + ph); ctx.stroke();
    ctx.globalAlpha = 1; ctx.fillStyle = css("--fp-resultant", "#e4572e");
    ctx.beginPath(); ctx.arc(X(state.opd), Y(T / peak), 4.5, 0, 2 * Math.PI); ctx.fill();
    ctx.restore();
  }

  // ---------- readouts ----------
  function updateLabels() {
    el("fp-R-v").textContent = state.R.toFixed(2);
    el("fp-opd-v").textContent = state.opd.toFixed(4) + " λ";
    el("fp-speed-v").textContent = state.scanSeconds + " s";
    el("fp-window-v").textContent = "δ: " + (2 * state.win[0]).toFixed(1).replace(".0", "") + "π – " + (2 * state.win[1]).toFixed(1).replace(".0", "") + "π";
  }
  function updateReadout() {
    const { N, R } = state, delta = phase(state.opd);
    const T = transmission(N, R, delta);
    const dmod = ((delta % (2 * Math.PI)) + 2 * Math.PI) % (2 * Math.PI);
    const finesse = R > 0 ? Math.PI * Math.sqrt(R) / (1 - R) : 0;
    ui.readout.innerHTML =
      "δ = 2π·OPD/λ = " + (dmod / Math.PI).toFixed(3) + " π (mod 2π) &nbsp;·&nbsp; " +
      "I<sub>t</sub>/I<sub>0</sub> (N = " + N + ") = " + T.toFixed(4) + " &nbsp;·&nbsp; " +
      "Airy (N → ∞) = " + airy(R, delta).toFixed(4) + "<br>" +
      "peak (1 − R<sup>N</sup>)² = " + peakFinite(N, R).toFixed(4) + " &nbsp;·&nbsp; " +
      "first neglected phasor / first phasor = R<sup>N</sup> = " + Math.pow(R, N).toExponential(2) + " &nbsp;·&nbsp; " +
      "finesse π√R/(1−R) = " + finesse.toFixed(1) + "<br>" +
      (R > 0 && R < 1
        ? "phasors needed to reach the Airy limit (R<sup>N</sup> &lt; 5%): N ≈ " + Math.ceil(Math.log(0.05) / Math.log(R))
        : "R = 0: a single phasor carries all the light") +
      (N === 2 ? " &nbsp;·&nbsp; N = 2 is a two-beam (Michelson-type) interferometer" : "");
  }
  function updateLegend() {
    const accent = css("--fp-accent", "#2f6bd8");
    let html = '<span><i style="background:' + accent + '"></i>N = ' + state.N + ", R = " + state.R.toFixed(2) + " (current)</span>";
    if (ui.airy.checked) html += '<span><i class="fp-dashed"></i>Airy, R = ' + state.R.toFixed(2) + "</span>";
    state.held.forEach((hc, i) => {
      html += '<span><i style="background:' + hc.colour + '"></i>N = ' + hc.N + ", R = " + hc.R.toFixed(2) +
        '<button data-i="' + i + '" title="Remove">×</button></span>';
    });
    ui.legend.innerHTML = html;
  }

  function render() {
    drawPhasors();
    drawSpectrum();
    updateReadout();
  }

  // ---------- interaction ----------
  function setOpd(x, fromScan) {
    const [x0, x1] = state.win;
    const prev = state.opd;
    state.opd = Math.min(x1, Math.max(x0, x));
    record(fromScan === "wrap" ? null : prev, state.opd);
    ui.opd.value = state.opd;
    updateLabels();
  }
  function setWindow(key) {
    state.win = WINDOWS[key];
    const [x0, x1] = state.win;
    ui.opd.min = x0; ui.opd.max = x1; ui.opd.step = (x1 - x0) / 2000;
    state.opd = Math.min(x1, Math.max(x0, state.opd));
    ui.opd.value = state.opd;
    clearTrace();
    record(null, state.opd);
  }
  function setPlaying(on) {
    state.playing = on;
    state.lastTime = null;
    ui.play.textContent = on ? "❚❚ Pause" : "▶ Scan";
    if (on) requestAnimationFrame(tick);
  }
  function tick(now) {
    if (!state.playing) return;
    if (state.lastTime !== null) {
      const [x0, x1] = state.win;
      const dt = Math.min(0.1, (now - state.lastTime) / 1000);
      let x = state.opd + (x1 - x0) * dt / state.scanSeconds;
      if (x > x1) setOpd(x0 + (x - x1), "wrap");
      else setOpd(x);
      render();
    }
    state.lastTime = now;
    requestAnimationFrame(tick);
  }

  function setN(N) {
    if (!Number.isFinite(N)) return;
    N = Math.max(1, Math.min(N_MAX, Math.round(N)));
    if (N === state.N) return;
    state.N = N;
    clearTrace(); record(null, state.opd);
    updateLegend(); render();
  }
  ui.N.addEventListener("input", () => {
    setN(sliderToN(Number(ui.N.value)));
    ui.Nbox.value = state.N;
  });
  ui.Nbox.addEventListener("input", () => {
    setN(Number(ui.Nbox.value));
    ui.N.value = nToSlider(state.N);
  });
  ui.Nbox.addEventListener("change", () => { ui.Nbox.value = state.N; });
  ui.R.addEventListener("input", () => {
    state.R = Number(ui.R.value); clearTrace(); record(null, state.opd);
    updateLabels(); updateLegend(); render();
  });
  ui.opd.addEventListener("input", () => { setOpd(Number(ui.opd.value)); render(); });
  ui.win.addEventListener("change", () => { setWindow(ui.win.value); updateLabels(); render(); });
  ui.speed.addEventListener("input", () => { state.scanSeconds = Number(ui.speed.value); updateLabels(); });
  ui.play.addEventListener("click", () => setPlaying(!state.playing));
  ui.hold.addEventListener("click", () => {
    if (state.held.some((hc) => hc.N === state.N && hc.R === state.R)) return;
    if (state.held.length >= MAX_HELD) state.held.shift();
    state.held.push({ N: state.N, R: state.R, colour: HOLD_COLOURS[state.nextColour++ % HOLD_COLOURS.length] });
    updateLegend(); render();
  });
  ui.clearHeld.addEventListener("click", () => { state.held = []; updateLegend(); render(); });
  ui.clearTrace.addEventListener("click", () => { clearTrace(); record(null, state.opd); render(); });
  ui.theory.addEventListener("change", render);
  ui.airy.addEventListener("change", () => { updateLegend(); render(); });
  ui.norm.addEventListener("change", render);
  ui.legend.addEventListener("click", (e) => {
    const i = e.target.getAttribute && e.target.getAttribute("data-i");
    if (i === null || i === undefined) return;
    state.held.splice(Number(i), 1);
    updateLegend(); render();
  });

  let dragging = false;
  function opdFromPointer(e) {
    const rect = ui.spectrum.getBoundingClientRect();
    const [x0, x1] = state.win;
    const pw = rect.width - 44 - 12;
    return x0 + (e.clientX - rect.left - 44) / pw * (x1 - x0);
  }
  ui.spectrum.addEventListener("pointerdown", (e) => {
    dragging = true; setPlaying(false);
    ui.spectrum.setPointerCapture(e.pointerId);
    setOpd(opdFromPointer(e)); render();
  });
  ui.spectrum.addEventListener("pointermove", (e) => {
    if (!dragging) return;
    setOpd(opdFromPointer(e)); render();
  });
  ui.spectrum.addEventListener("pointerup", () => { dragging = false; });
  ui.spectrum.addEventListener("pointercancel", () => { dragging = false; });

  if (window.ResizeObserver) new ResizeObserver(render).observe(ui.spectrum);
  window.addEventListener("resize", render);

  setWindow("full");
  updateLabels();
  updateLegend();
  render();
})();
</script>

## Things to try

1. **Michelson limit.** Set $N = 2$ and $R = 0.99$. The two phasors are almost equal in length, so the spectrum is a full-contrast $\cos^2$ fringe, exactly what a Michelson interferometer gives. The dashed line is what the *same mirrors* give once all reflections are included. (At lower $R$ the two phasors differ in length and the fringe contrast $2R/(1+R^2)$ drops.)
2. **From Michelson to Fabry–Pérot.** Keep $R = 0.99$ and click *Hold curve* at $N = 2, 10, 50, 300$. Each extra phasor sharpens the peak. The curve only lands on the dashed Airy line once $R^N \ll 1$, here after a few hundred round trips (the readout gives the number). The finesse is really a count of how many beams interfere.
3. **Weakly decaying phasors.** At $R = 0.99$ and $N = 10$ the phasors hardly decay, so the chain is close to a regular polygon. You get $N-2$ small secondary maxima between the main orders, just like an $N$-slit grating.
4. **Watch the chain while you scan.** On resonance the chain is a straight line. At $\delta = \pi$ it zig-zags back and forth. Close to resonance it curls into a spiral. A high-$R$ chain is long, so a very small phase error per step is enough to close the spiral. That is why high finesse means narrow peaks.
5. **Zoom in.** At high finesse the peaks are narrower than one pixel of the 3-order view. Use the *0.9 – 1.1 λ* window to resolve them.
