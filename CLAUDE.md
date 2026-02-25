# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: ARCP Topology Learning and Interactive Tutorial Development

**Student:** Vignesh (B.Tech 2nd Year, Power Electronics)

**End goal:** Interactive web-based animations and visualizations of ARCP converter operation, integrated into the research website at `C:\Users\tmouli\Documents\WebProjects\mouli-research-site`.

### Learning Path
- **Phase 1** — Study foundational papers; understand circuit-level operation from first principles
- **Phase 2** — Develop mathematical models, ODEs, and transfer functions
- **Phase 3** — Build interactive visualizations and animations (commutation waveforms, phase-plane plots, energy trajectories)
- **Phase 4** — Integrate finished tutorials into the website

---

## Literature Collection (this folder)

All files are PDFs. Primary paper is De Doncker & Lyons 1990.

| File | Coverage |
|------|---------|
| `The_auxiliary_resonant_commutated_pole_converter.pdf` | **Primary paper** — De Doncker & Lyons, IEEE IAS 1990. Foundational topology and analysis. |
| `Analysis of the auxiliary resonant commutated pole inverter.pdf` | Detailed circuit-level ARCPI analysis |
| `Applications of an ARPC.pdf` | Application scope and use-cases |
| `Auxiliary_Resonant_Commutated_Pole_Inverter_ARCPI_Operation_Using_online_voltage_measurements.pdf` | Online measurement-based commutation control |
| `Performance_Evaluation_of_MOS-Gated_Thyristors_as_Auxiliary_Switches_in_the_ARCP_Inverter.pdf` | Auxiliary switch device selection (MCT vs IGBT) |
| `IET Power Electronics - 2016 - Chu - Three‐phase double auxiliary resonant commutated pole inverter topology and analysis.pdf` | Three-phase double-ARCP variant |
| `Comprehensive_evaluation_of_auxiliary_resonant_commutated_pole_inverter_for_electric_vehicle_applications.pdf` | EV application performance data |
| `ITEC_Resonant_Algorithms_Paper_Final.pdf` | Resonant commutation switching algorithms |

---

## Core ARCP Physics (Reference)

**Topology:** One inverter pole-leg with an auxiliary resonant branch ($L_r$, $C_r$, auxiliary bidirectional switches) that pre-charges $C_r$ to enable zero-voltage switching (ZVS) of the main devices.

**State variables:** pole-node voltage $v_f$ and auxiliary inductor current $i_r$.

**Commutation ODE** (each subinterval is a forced 2nd-order oscillator):
$$\ddot{v}_f + \omega_0^2\, v_f = \omega_0^2\, u_f, \qquad \omega_0 = \frac{1}{\sqrt{L_r C_r}}, \quad Z_0 = \sqrt{\frac{L_r}{C_r}}$$

**Shifted state** ($j = i_r - I_L$, quasi-constant load current assumption):
$$\dot{v}_f = j/C_r, \qquad \dot{j} = (u_f - v_f)/L_r$$

**ZVS condition:** $i_r$ must exceed $I_L$ before the resonant swing begins; otherwise commutation fails and hard-switching energy loss results.

**Load threshold $I_T$:** Below $I_T$, auxiliary boost interval is required to pre-charge $i_r$. Above $I_T$, load current alone sustains commutation.

**Two-time-scale control:**
- Fast: commutation logic (auxiliary boost duration / current target)
- Slow: standard current/voltage loop (PI in dq, deadbeat, MPC) on averaged VSI-like plant with corrected duty $d_\text{eff} = d_\text{cmd} - \Delta d_\text{comm}$

**Recommended visualizations for tutorials:**
1. Time traces: $v_f(t)$, $i_r(t)$, gate signals, diode conduction intervals
2. Phase-plane: $(v_f,\; i_r - I_L)$ circular trajectory through each commutation event
3. Energy: $E_L(t) = \frac{1}{2}L_r i_r^2$ and $E_C(t) = \frac{1}{2}C_r(v_f - u_f)^2$ with event markers
4. Commutation map: success/fail regions vs. $(I_L,\; i_{r0},\; V_{dc})$

---

## Website Integration

**Project location:** `C:\Users\tmouli\Documents\WebProjects\mouli-research-site`
**Stack:** React 19 + Vite + React Router v7

### Dev Commands (run from website root)
```bash
npm run dev        # start dev server with HMR
npm run build      # production build to dist/
npm run preview    # preview production build
npm run lint       # ESLint check
```

### Key Libraries Available
| Library | Use |
|---------|-----|
| `three` + `@react-three/fiber` + `@react-three/drei` | 3D scenes and animations |
| `katex` + `rehype-katex` + `remark-math` | Math equation rendering in articles |
| `react-markdown` + `rehype-raw` | Markdown-based article content |
| `@dimforge/rapier2d-compat` / `rapier3d-compat` | 2D/3D physics simulations |
| `matter-js`, `cannon-es` | Alternative physics engines |

### How to Add a New ARCP Tutorial Page

1. **Create feature folder:** `src/features/arcp-tutorial/`
   - `pages/ARCPTutorialPage.jsx` — top-level page component
   - `components/` — animation/plot sub-components
   - `data/` — simulation parameters, waveform data

2. **Register the route** in `src/app/AppRoutes.jsx`:
   ```jsx
   import ARCPTutorialPage from "../features/arcp-tutorial/pages/ARCPTutorialPage";
   // inside <Routes>:
   <Route path="/tutorials/arcp" element={<ARCPTutorialPage />} />
   ```

3. **Register in content index** `src/features/content/contentIndex.js` — add an entry to `CONTENT_ITEMS`:
   ```js
   {
     id: "arcp-tutorial",
     title: "ARCP Converter",
     type: "interactive",
     topic: "power-electronics",
     track: "advanced",   // or "research"
     path: "/tutorials/arcp",
     summary: "Interactive commutation waveforms and phase-plane for the ARCP inverter.",
   }
   ```

### Website Architecture Pattern

- `src/app/AppRoutes.jsx` — single routing file; all routes defined here
- `src/features/content/contentIndex.js` — single source of truth for `TOPICS`, `TRACKS`, and `CONTENT_ITEMS`; drives both `/tutorials` page and `/topics/:topic` pages
- Each feature is self-contained: its own `pages/`, `components/`, `data/`, and CSS file
- Articles use Markdown files rendered via `react-markdown` with KaTeX math support
- Interactive pages build custom SVG/Canvas or Three.js components directly in React

### LaTeX Notes (for Phase 1–2 derivation documents)
When creating `.tex` derivation documents in this folder:
```bash
pdflatex <filename>.tex
pdflatex <filename>.tex   # second pass for TOC/cross-refs
```
Packages used in prior tutorials here: `amsmath`, `siunitx`, `tikz`, `pgfplots`, `circuitikz`, `tcolorbox`, `hyperref`.
