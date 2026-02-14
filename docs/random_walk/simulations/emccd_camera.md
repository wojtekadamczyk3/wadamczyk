# EMCCD Camera Simulation

Here I wanted to make a small interactive EMCCD simulator for a single pixel (in ADU), mostly to build intuition.

The website version is deliberately simplified so that it runs fast in-browser, but the logic is still the same as in a full camera model: we generate electrons, we add background processes, we multiply in the EM register, and finally we read out with noise and offset.

## Model

### Big picture

Lets look at one pixel in one frame. A useful way to think about the measured value is:
1. start from digital offset,
2. add the EM-amplified charge converted to ADU,
3. then add readout/pattern imperfections.

One compact way to write this is

$$
D
=
B_{\mathrm{off}}(\boldsymbol\theta_{\mathrm{ADC}})
+
G_{\mathrm{ADC}}(\boldsymbol\theta_{\mathrm{ADC}})
\Big[
\mathcal{M}\!\big(N^{\mathrm{in}}; g_{\mathrm{EM}}(\boldsymbol\theta_{\mathrm{EM}})\big)
+
\epsilon^{\mathrm{read}}(\boldsymbol\theta_{\mathrm{read}})
\Big].
$$

where

- $B_{\mathrm{off}}$ is the digital bias/offset
- $G_{\mathrm{ADC}}$ is the conversion gain (ADU per output electron)
- $\mathcal{M}$ is the stochastic EM multiplication
- $\epsilon^{\mathrm{read}}$ is output amplifier read noise

The number of electrons entering the EM register is

$$
N^{\mathrm{in}}=N^{\mathrm{sig}}+N^{\mathrm{bg}}.
$$

### Signal and background terms

For the signal part, we use Poisson counting:

$$
N^{\mathrm{sig}}\sim \mathrm{Poisson}(\mu^{\mathrm{sig}}),\quad
\mu^{\mathrm{sig}}
=
\eta_{\mathrm{QE}}(\boldsymbol\theta_{\mathrm{QE}})
T_{\mathrm{opt}}(\boldsymbol\theta_{\mathrm{opt}})
I(\boldsymbol\theta_{\mathrm{img}})
t_{\mathrm{exp}}.
$$

Then we split the background into dark current, CIC, and stray light:

$$
N^{\mathrm{bg}}=N^{\mathrm{dark}}+N^{\mathrm{CIC}}+N^{\mathrm{stray}}.
$$

$$
\begin{aligned}
N^{\mathrm{dark}} &\sim \mathrm{Poisson}(\mu^{\mathrm{dark}}), \quad
\mu^{\mathrm{dark}}=r^{\mathrm{dark}}(\boldsymbol\theta_{\mathrm{dark}})\,t_{\mathrm{exp}},\\
N^{\mathrm{CIC}} &\sim \mathrm{Poisson}(\mu^{\mathrm{CIC}}), \quad
\mu^{\mathrm{CIC}}=r^{\mathrm{CIC}}(\boldsymbol\theta_{\mathrm{clk}}),\\
N^{\mathrm{stray}} &\sim \mathrm{Poisson}(\mu^{\mathrm{stray}}), \quad
\mu^{\mathrm{stray}}=\eta_{\mathrm{QE}}T_{\mathrm{opt}}\Phi^{\mathrm{stray}}(\boldsymbol\theta_{\mathrm{env}})\,t_{\mathrm{exp}}.
\end{aligned}
$$

### EM stage and readout

Given $n$ input electrons, the EM register amplifies stochastically:

$$
N^{\mathrm{out}}\sim \mathcal{M}(n; g_{\mathrm{EM}}),\quad
\mathbb{E}[N^{\mathrm{out}}\mid n]=g_{\mathrm{EM}}n,
$$

In this simulator, $\mathcal{M}$ is implemented as a Gamma (Erlang) law conditioned on the input count:

$$
N^{\mathrm{out}} \mid N^{\mathrm{in}}=n \sim \Gamma(\text{shape}=n,\ \text{scale}=g_{\mathrm{EM}}),
$$

with the convention $N^{\mathrm{out}}=0$ for $n=0$.  
So for integer $n$, the EM output is the sum of $n$ exponential gains (mean $g_{\mathrm{EM}}$ each).

At high EM gain, the excess-noise factor for a typical EMCCD approaches $\sqrt{2}$.

Read noise is usually well approximated by a Gaussian:

$$
\epsilon^{\mathrm{read}}\sim \mathcal{N}\!\big(0,\sigma_{\mathrm{read}}^2(\boldsymbol\theta_{\mathrm{read}})\big).
$$

### What the interactive demo actually uses

For the interactive widget below we use a reduced version of the model (same spirit, fewer knobs), so that it stays responsive on the page:

$$
\begin{aligned}
N_{\text{sig}}  &\sim \text{Poisson}(\mu_{\text{signal}} t_{\text{exp}}), \\
N_{\text{str}}  &\sim \text{Poisson}(\mu_{\text{stray}} t_{\text{exp}}), \\
N_{\text{dark}} &\sim \text{Poisson}(\mu_{\text{dark}} t_{\text{exp}}), \\
N_{\text{cic}}  &\sim \text{Poisson}(N_{\text{cic}}),
\end{aligned}
$$

$$
N_{\text{in}} = N_{\text{sig}} + N_{\text{str}} + N_{\text{dark}} + N_{\text{cic}},
\quad
Y \mid N_{\text{in}}=n \sim \Gamma(\text{shape}=n,\ \text{scale}=g_{\text{em}}),
$$

$$
D = B_{\text{offset}} + GY + \mathcal{N}(0, e_{\text{read}}).
$$

## Interactive Web Simulation

This simulator runs directly in your browser on the MkDocs page.

<style>
  .emccd-wrap {
    border: 1px solid color-mix(in srgb, var(--md-default-fg-color--lightest) 70%, transparent);
    border-radius: 14px;
    padding: 18px;
    margin: 12px 0;
    background:
      radial-gradient(1200px 240px at 0% 0%, color-mix(in srgb, var(--md-primary-fg-color) 10%, transparent), transparent 55%),
      var(--md-default-bg-color);
    box-shadow: 0 10px 26px -18px rgba(0, 0, 0, 0.45);
  }
  .emccd-title {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 12px;
  }
  .emccd-title strong {
    font-size: 1rem;
    letter-spacing: 0.2px;
  }
  .emccd-title span {
    font-size: 0.85rem;
    opacity: 0.75;
  }
  .emccd-grid {
    display: grid;
    grid-template-columns: 240px 1fr 120px;
    gap: 10px 14px;
    align-items: center;
  }
  .emccd-rowlabel {
    font-size: 0.92rem;
    opacity: 0.95;
  }
  .emccd-value {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 0.86rem;
    text-align: right;
    font-weight: 600;
    color: var(--md-default-fg-color, #111);
    background: rgba(127, 127, 127, 0.14);
    border: 1px solid rgba(127, 127, 127, 0.28);
    border-radius: 8px;
    padding: 3px 8px;
  }
  .emccd-grid input[type="range"] {
    width: 100%;
    accent-color: var(--md-primary-fg-color);
  }
  .emccd-actions {
    display: flex;
    gap: 10px;
    margin-top: 14px;
    flex-wrap: wrap;
  }
  .emccd-actions button {
    border: 1px solid color-mix(in srgb, var(--md-primary-fg-color) 25%, transparent);
    border-radius: 10px;
    padding: 7px 12px;
    font-weight: 600;
    cursor: pointer;
    background: color-mix(in srgb, var(--md-primary-fg-color) 14%, var(--md-default-bg-color));
    color: var(--md-default-fg-color);
    transition: transform 0.08s ease, filter 0.15s ease;
  }
  .emccd-actions button:hover { filter: brightness(1.05); }
  .emccd-actions button:active { transform: translateY(1px); }
  .emccd-stats {
    margin-top: 12px;
    padding: 8px 10px;
    border-radius: 10px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    background: color-mix(in srgb, var(--md-default-fg-color) 6%, transparent);
    border: 1px solid color-mix(in srgb, var(--md-default-fg-color) 12%, transparent);
  }
  .emccd-canvas {
    margin-top: 12px;
    width: 100%;
    border: 1px solid color-mix(in srgb, var(--md-default-fg-color--lightest) 60%, transparent);
    border-radius: 10px;
    background: color-mix(in srgb, var(--md-default-bg-color) 90%, white);
  }
  @media (max-width: 900px) {
    .emccd-grid {
      grid-template-columns: 1fr;
      gap: 8px;
    }
    .emccd-value {
      text-align: left;
      width: fit-content;
    }
  }
</style>

<div class="emccd-wrap" id="emccd-app">
  <div class="emccd-title">
    <strong>EMCCD Monte Carlo Playground</strong>
    <span>Interactive in-browser simulation</span>
  </div>
  <div class="emccd-grid">
    <div class="emccd-rowlabel">B_offset [ADU]</div>
    <input id="B_offset" type="range" min="0" max="500" step="10" value="200" />
    <div class="emccd-value" id="B_offset_v"></div>

    <div class="emccd-rowlabel">log10(t_exp [s])</div>
    <input id="t_exp_log" type="range" min="-4" max="0" step="0.1" value="-3" />
    <div class="emccd-value" id="t_exp_v"></div>

    <div class="emccd-rowlabel">G [ADU/e-]</div>
    <input id="G" type="range" min="0.1" max="5" step="0.1" value="1.0" />
    <div class="emccd-value" id="G_v"></div>

    <div class="emccd-rowlabel">log10(mu_signal [e-/s])</div>
    <input id="mu_signal_log" type="range" min="0" max="4" step="0.1" value="3" />
    <div class="emccd-value" id="mu_signal_v"></div>

    <div class="emccd-rowlabel">mu_stray [e-/s]</div>
    <input id="mu_stray" type="range" min="0" max="100" step="1" value="0" />
    <div class="emccd-value" id="mu_stray_v"></div>

    <div class="emccd-rowlabel">log10(mu_dark [e-/s])</div>
    <input id="mu_darkcurrent_log" type="range" min="-4" max="1" step="0.1" value="-1" />
    <div class="emccd-value" id="mu_darkcurrent_v"></div>

    <div class="emccd-rowlabel">N_cic [e-/frame]</div>
    <input id="N_cic" type="range" min="0" max="1" step="0.01" value="0.01" />
    <div class="emccd-value" id="N_cic_v"></div>

    <div class="emccd-rowlabel">log10(g_em [x])</div>
    <input id="g_em_log" type="range" min="0" max="4" step="0.1" value="3" />
    <div class="emccd-value" id="g_em_v"></div>

    <div class="emccd-rowlabel">e_read [ADU rms]</div>
    <input id="e_read" type="range" min="0" max="20" step="0.5" value="0" />
    <div class="emccd-value" id="e_read_v"></div>

    <div class="emccd-rowlabel">n_samples</div>
    <input id="n_samples" type="range" min="100" max="10000" step="100" value="1000" />
    <div class="emccd-value" id="n_samples_v"></div>
  </div>

  <div class="emccd-actions">
    <button id="run_btn">Run simulation</button>
    <button id="reroll_btn">Reroll</button>
  </div>

  <div class="emccd-stats" id="emccd_stats"></div>
  <canvas class="emccd-canvas" id="emccd_canvas" width="980" height="420"></canvas>
</div>

<script>
(() => {
  const ids = [
    "B_offset", "t_exp_log", "G", "mu_signal_log", "mu_stray",
    "mu_darkcurrent_log", "N_cic", "g_em_log", "e_read", "n_samples"
  ];

  let seed = 1;
  function rand() {
    seed |= 0;
    seed = (seed + 0x6D2B79F5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }

  function normal01() {
    const u1 = Math.max(rand(), 1e-12);
    const u2 = rand();
    return Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2);
  }

  function poisson(lambda) {
    if (lambda <= 0) return 0;
    if (lambda < 30) {
      const L = Math.exp(-lambda);
      let k = 0;
      let p = 1.0;
      do {
        k += 1;
        p *= rand();
      } while (p > L);
      return k - 1;
    }
    const x = Math.round(lambda + Math.sqrt(lambda) * normal01());
    return Math.max(0, x);
  }

  function gammaSample(shape, scale) {
    if (shape <= 0 || scale <= 0) return 0;
    if (shape < 1) {
      const u = Math.max(rand(), 1e-12);
      return gammaSample(shape + 1, scale) * Math.pow(u, 1 / shape);
    }
    const d = shape - 1 / 3;
    const c = 1 / Math.sqrt(9 * d);
    while (true) {
      const x = normal01();
      let v = 1 + c * x;
      if (v <= 0) continue;
      v = v * v * v;
      const u = rand();
      if (u < 1 - 0.0331 * x * x * x * x) return scale * d * v;
      if (Math.log(u) < 0.5 * x * x + d * (1 - v + Math.log(v))) return scale * d * v;
    }
  }

  function readParams() {
    const get = (id) => Number(document.getElementById(id).value);
    const tExp = Math.pow(10, get("t_exp_log"));
    const muSignal = Math.pow(10, get("mu_signal_log"));
    const muDark = Math.pow(10, get("mu_darkcurrent_log"));
    const gEm = Math.pow(10, get("g_em_log"));
    return {
      B_offset: get("B_offset"),
      t_exp: tExp,
      G: get("G"),
      mu_signal: muSignal,
      mu_stray: get("mu_stray"),
      mu_darkcurrent: muDark,
      N_cic: get("N_cic"),
      g_em: gEm,
      e_read: get("e_read"),
      n_samples: Math.floor(get("n_samples"))
    };
  }

  function updateLabels() {
    const p = readParams();
    document.getElementById("B_offset_v").textContent = p.B_offset.toFixed(1);
    document.getElementById("t_exp_v").textContent = p.t_exp.toExponential(2);
    document.getElementById("G_v").textContent = p.G.toFixed(2);
    document.getElementById("mu_signal_v").textContent = p.mu_signal.toExponential(2);
    document.getElementById("mu_stray_v").textContent = p.mu_stray.toFixed(1);
    document.getElementById("mu_darkcurrent_v").textContent = p.mu_darkcurrent.toExponential(2);
    document.getElementById("N_cic_v").textContent = p.N_cic.toFixed(3);
    document.getElementById("g_em_v").textContent = p.g_em.toExponential(2);
    document.getElementById("e_read_v").textContent = p.e_read.toFixed(1);
    document.getElementById("n_samples_v").textContent = String(p.n_samples);
  }

  function simulateOne(p) {
    const lamSig = p.mu_signal * p.t_exp;
    const lamStr = p.mu_stray * p.t_exp;
    const lamDark = p.mu_darkcurrent * p.t_exp;
    const lamCic = p.N_cic;

    const nIn = poisson(lamSig) + poisson(lamStr) + poisson(lamDark) + poisson(lamCic);
    const yEm = nIn <= 0 ? 0 : gammaSample(nIn, Math.max(p.g_em, 0));
    return p.B_offset + p.G * yEm + p.e_read * normal01();
  }

  function percentile(sorted, q) {
    const idx = (sorted.length - 1) * q;
    const lo = Math.floor(idx);
    const hi = Math.ceil(idx);
    if (lo === hi) return sorted[lo];
    const t = idx - lo;
    return sorted[lo] * (1 - t) + sorted[hi] * t;
  }

  function histogram(data, nBins) {
    let min = Infinity;
    let max = -Infinity;
    for (const x of data) {
      if (x < min) min = x;
      if (x > max) max = x;
    }
    if (!(max > min)) {
      min -= 1;
      max += 1;
    }
    const sorted = [...data].sort((a, b) => a - b);
    const q01 = percentile(sorted, 0.01);
    const q99 = percentile(sorted, 0.99);
    const lo = Math.min(q01, min);
    const hi = Math.max(q99, max);
    const pad = 0.04 * (hi - lo);
    min = lo - pad;
    max = hi + pad;
    const width = (max - min) / nBins;
    const bins = Array(nBins).fill(0);
    for (const x of data) {
      let j = Math.floor((x - min) / width);
      if (j < 0) j = 0;
      if (j >= nBins) j = nBins - 1;
      bins[j] += 1;
    }
    const density = bins.map((c) => c / (data.length * width));
    return { min, max, width, density };
  }

  function drawHistogram(canvas, hist) {
    const ctx = canvas.getContext("2d");
    const W = canvas.width;
    const H = canvas.height;
    ctx.clearRect(0, 0, W, H);

    const left = 58, right = 14, top = 18, bottom = 40;
    const pw = W - left - right;
    const ph = H - top - bottom;
    const ymax = Math.max(...hist.density, 1e-12) * 1.12;
    const n = hist.density.length;

    ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue("--md-default-bg-color").trim() || "#ffffff";
    ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = "rgba(128, 128, 128, 0.35)";
    ctx.lineWidth = 1;
    ctx.strokeRect(left, top, pw, ph);

    const yTicks = 5;
    const xTicks = 6;

    for (let y = 0; y <= yTicks; y++) {
      const gy = top + (y / yTicks) * ph;
      ctx.strokeStyle = "rgba(128, 128, 128, 0.18)";
      ctx.beginPath();
      ctx.moveTo(left, gy);
      ctx.lineTo(left + pw, gy);
      ctx.stroke();
    }

    for (let x = 0; x <= xTicks; x++) {
      const gx = left + (x / xTicks) * pw;
      ctx.strokeStyle = "rgba(128, 128, 128, 0.12)";
      ctx.beginPath();
      ctx.moveTo(gx, top);
      ctx.lineTo(gx, top + ph);
      ctx.stroke();
    }

    ctx.fillStyle = "rgba(65, 130, 255, 0.62)";
    for (let i = 0; i < n; i++) {
      const x0 = left + (i / n) * pw;
      const x1 = left + ((i + 1) / n) * pw;
      const h = (hist.density[i] / ymax) * ph;
      ctx.fillRect(x0 + 0.5, top + ph - h, Math.max(1, x1 - x0 - 1), h);
    }

    ctx.fillStyle = getComputedStyle(document.documentElement).getPropertyValue("--md-default-fg-color").trim() || "#222";
    ctx.font = "12px sans-serif";
    ctx.fillText("Density", 8, top + 12);
    ctx.fillText("ADU", W / 2 - 14, H - 8);

    ctx.font = "11px sans-serif";
    for (let y = 0; y <= yTicks; y++) {
      const gy = top + (y / yTicks) * ph;
      const val = ymax * (1 - y / yTicks);
      ctx.fillText(val.toFixed(3), 8, gy + 4);
    }
    for (let x = 0; x <= xTicks; x++) {
      const gx = left + (x / xTicks) * pw;
      const val = hist.min + (x / xTicks) * (hist.max - hist.min);
      ctx.fillText(val.toFixed(1), gx - 14, H - 16);
    }
  }

  function runSimulation(reseed) {
    if (reseed) seed = (seed + 0x9E3779B9) | 0;
    const p = readParams();
    const data = new Array(p.n_samples);
    for (let i = 0; i < p.n_samples; i++) data[i] = simulateOne(p);

    let sum = 0;
    for (const x of data) sum += x;
    const mean = sum / data.length;
    let s2 = 0;
    for (const x of data) {
      const d = x - mean;
      s2 += d * d;
    }
    const std = Math.sqrt(s2 / data.length);

    const hist = histogram(data, 80);
    drawHistogram(document.getElementById("emccd_canvas"), hist);
    document.getElementById("emccd_stats").textContent =
      `n=${p.n_samples} | mean=${mean.toFixed(2)} ADU | std=${std.toFixed(2)} ADU`;
  }

  ids.forEach((id) => {
    document.getElementById(id).addEventListener("input", () => {
      updateLabels();
      runSimulation(false);
    });
  });
  document.getElementById("run_btn").addEventListener("click", () => runSimulation(false));
  document.getElementById("reroll_btn").addEventListener("click", () => runSimulation(true));

  updateLabels();
  runSimulation(false);
})();
</script>

