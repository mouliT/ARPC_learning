"""
arcp_equations_illustration.py
===============================
Step-by-step illustration of the ARCP governing equations.

Addresses three confusions from studying P1 Fig.5 (green box):
  Q1. Are the ODEs independent of circuit operation?
  Q2. How do equations (1) and (2) combine into the harmonic oscillator?
  Q3. What is the shifted state j = ir - IL and why does it give a circle?

Reference: De Doncker & Lyons, IEEE IAS 1990 (Paper 1).

Run:  python arcp_equations_illustration.py
Output: 4 PNG figures saved in the current directory.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1 — PARAMETERS
# ─────────────────────────────────────────────────────────────────────────────
Vdc    = 600.0    # DC bus voltage [V]
Lr     = 4e-6     # Resonant inductance [H]
Cr     = 47e-9    # Total snubber cap at pole node (= Cr/2 + Cr/2) [F]
IL     = 30.0     # Load current — quasi-constant during commutation [A]
iboost = 10.0     # Boost current added above IL before resonant swing [A]

# Derived resonant parameters
wr = 1.0 / np.sqrt(Lr * Cr)      # Angular resonant frequency [rad/s]
Zr = np.sqrt(Lr / Cr)             # Characteristic impedance [Ω]
fr = wr / (2 * np.pi)             # Resonant frequency [Hz]
Tr = 2 * np.pi / wr               # Full resonant period [s]

print("=" * 60)
print("ARCP Parameters")
print("=" * 60)
print(f"  Vdc     = {Vdc:.0f} V")
print(f"  Lr      = {Lr*1e6:.1f} µH,   Cr = {Cr*1e9:.0f} nF")
print(f"  IL      = {IL:.0f} A,   iboost = {iboost:.0f} A")
print(f"  ωr      = {wr/1e6:.3f} Mrad/s")
print(f"  fr      = {fr/1e3:.1f} kHz")
print(f"  Zr      = {Zr:.2f} Ω")
print(f"  Tr      = {Tr*1e6:.2f} µs  (half-period = {Tr/2*1e6:.2f} µs)")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2 — ANALYTICAL SOLUTION FOR EACH PHASE
#
# The commutation sequence (from diode D2 conducting → S1 ZVS turn-on):
#
#  Phase 0  Idle:          vf = 0, ir = 0  — trivial, NO ODEs
#  Phase 1  Boost:         A1 fires; ir ramps up linearly, vf = 0
#  Phase 2  Resonant swing:  LC oscillation — the ODEs apply HERE ONLY
#  Phase 3  Post-clamp:    D1 clamps (vf = Vdc); ir ramps back to 0
#
# Q1 ANSWER: The ODEs ONLY apply in Phase 2. In Phases 0, 1, 3 the circuit
# is in a different topological state and the ODEs change.
# ─────────────────────────────────────────────────────────────────────────────

# --- Phase 0: Idle ---
T_idle  = 0.5e-6
t_idle  = np.linspace(0, T_idle, 300)
vf_idle = np.zeros_like(t_idle)
ir_idle = np.zeros_like(t_idle)

# --- Phase 1: Boost ---
# A1 fires; Vdc/2 appears across Lr; dir/dt = Vdc/(2*Lr) = constant
# ir ramps from 0 → IL + iboost; vf stays at 0 (D2 still conducts, clamps pole node)
T_boost = 2 * Lr * (IL + iboost) / Vdc     # solve: (Vdc/2Lr)*T = IL + iboost
t_boost = np.linspace(0, T_boost, 400)
vf_boost = np.zeros_like(t_boost)
ir_boost = (Vdc / (2 * Lr)) * t_boost      # ir(t) = (Vdc/2Lr)*t

print(f"\n  Boost duration T_boost = {T_boost*1e6:.3f} µs")
print(f"  dir/dt during boost    = {Vdc/(2*Lr)/1e6:.2f} A/µs")

# --- Phase 2: Resonant Swing ---
# At start of swing: vf = 0, ir = IL + iboost
#
# Q2 DERIVATION:
#   KCL at pole node:  Cr * dvf/dt = ir - IL   →  dvf/dt = (ir - IL)/Cr      ... (1)
#   KVL aux loop:      Lr * dir/dt = Vdc/2 - vf →  dir/dt = (Vdc/2 - vf)/Lr  ... (2)
#
#   Differentiate (1): d²vf/dt² = (1/Cr) * dir/dt
#   Substitute (2):    d²vf/dt² = (1/Cr) * (Vdc/2 - vf)/Lr
#                   → d²vf/dt² + ωr² * vf = ωr² * Vdc/2      [forced oscillator]
#
# Q3 SHIFTED STATE:
#   Let j = ir - IL.  Then:  dvf/dt = j/Cr,   dj/dt = (Vdc/2 - vf)/Lr
#   Let u = vf - Vdc/2.  Then:  du/dt = j/Cr,   dj/dt = -u/Lr
#   → d²u/dt² + ωr²*u = 0  (simple harmonic motion in (u, j) space)
#
# Analytical solution with ICs: u0 = -Vdc/2, j0 = iboost
#   u(t) = u0*cos(ωr*t) + j0*Zr*sin(ωr*t)
#   j(t) = -(u0/Zr)*sin(ωr*t) + j0*cos(ωr*t)
#   vf(t) = Vdc/2 + u(t)
#   ir(t) = IL + j(t)
#
# Circle: u(t)² + [j(t)*Zr]² = u0² + (j0*Zr)² = R²  = constant

u0 = 0.0 - Vdc / 2    # = -Vdc/2 (initial u at start of swing)
j0 = iboost            # initial j = ir - IL = iboost

R = np.sqrt(u0**2 + (j0 * Zr)**2)
print(f"\n  Circle radius R = {R:.2f} V  (in (u, j*Zr) space)")
print(f"  u0 = {u0:.1f} V,  j0*Zr = {j0*Zr:.2f} V")

# Time when vf first reaches Vdc (D1 clamps): find numerically
N_sw = 4000
t_sw_full = np.linspace(0, Tr / 2, N_sw)
u_sw_full = u0 * np.cos(wr * t_sw_full) + j0 * Zr * np.sin(wr * t_sw_full)
vf_sw_full = Vdc / 2 + u_sw_full

idx_clamp = np.argmax(vf_sw_full >= Vdc - 0.01)
if idx_clamp == 0:
    idx_clamp = N_sw - 1    # fallback: full half-period
T_swing = t_sw_full[idx_clamp]

t_swing = t_sw_full[:idx_clamp + 1]
u_swing = u_sw_full[:idx_clamp + 1]
vf_swing = vf_sw_full[:idx_clamp + 1]
j_swing  = -(u0 / Zr) * np.sin(wr * t_swing) + j0 * np.cos(wr * t_swing)
ir_swing = IL + j_swing

ir_at_clamp = ir_swing[-1]
print(f"  Resonant swing duration  T_swing = {T_swing*1e6:.3f} µs")
print(f"  ir at clamp (D1 fires)   ir_end  = {ir_at_clamp:.2f} A  "
      f"(NOTE: D1 clamps at FIRST crossing of vf=Vdc, where ir ≈ IL+iboost = {IL+iboost:.1f} A)")

# --- Phase 3: Post-clamp ramp-down ---
# D1 has clamped: vf = Vdc.  Aux loop now: Vdc/2 (midpoint) to Lr to Vdc.
# Voltage across Lr = Vdc/2 - Vdc = -Vdc/2  →  dir/dt = -Vdc/(2*Lr)
# ir ramps from ir_at_clamp down to 0.  S1 fires at ZVS when ir = 0.
T_ramp = ir_at_clamp / (Vdc / (2 * Lr))
t_ramp = np.linspace(0, T_ramp, 400)
vf_ramp = np.full_like(t_ramp, Vdc)
ir_ramp = ir_at_clamp - (Vdc / (2 * Lr)) * t_ramp

print(f"  Post-clamp ramp duration T_ramp  = {T_ramp*1e6:.3f} µs")

# ─────────────────────────────────────────────────────────────────────────────
# Stitch phases together on a common time axis
# ─────────────────────────────────────────────────────────────────────────────
t0  = T_idle
t1  = t0 + T_boost
t2  = t1 + T_swing
t3  = t2 + T_ramp

t_all  = np.concatenate([t_idle,
                          t0 + t_boost,
                          t1 + t_swing,
                          t2 + t_ramp])
vf_all = np.concatenate([vf_idle, vf_boost, vf_swing, vf_ramp])
ir_all = np.concatenate([ir_idle, ir_boost, ir_swing, ir_ramp])
t_us   = t_all * 1e6   # µs for plotting

# Phase boundary markers in µs
m0, m1, m2, m3 = t0*1e6, t1*1e6, t2*1e6, t3*1e6

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 1 — Full time traces, four phases annotated
# ─────────────────────────────────────────────────────────────────────────────
c_idle  = '#e0e0e0'
c_boost = '#ffc97a'
c_swing = '#a8d5cc'
c_ramp  = '#ffe0a0'

fig1, (ax_vf, ax_ir) = plt.subplots(2, 1, figsize=(11, 6.5), sharex=True)
fig1.suptitle("ARCP Commutation — Time Traces (Analytical)\n"
              r"Sequence: Idle $\to$ Boost $\to$ Resonant Swing $\to$ Post-Clamp",
              fontsize=12, fontweight='bold')

for ax in (ax_vf, ax_ir):
    ax.axvspan(0,   m0, alpha=0.35, color=c_idle,  zorder=0)
    ax.axvspan(m0, m1,  alpha=0.35, color=c_boost, zorder=0)
    ax.axvspan(m1, m2,  alpha=0.35, color=c_swing, zorder=0)
    ax.axvspan(m2, m3,  alpha=0.35, color=c_ramp,  zorder=0)
    for xm in (m0, m1, m2, m3):
        ax.axvline(xm, color='#777', lw=0.8, ls='--', zorder=1)

# vf panel
ax_vf.plot(t_us, vf_all, 'b-', lw=2.2, zorder=2)
ax_vf.axhline(Vdc,   color='red',  lw=1.2, ls=':', label=f'$V_{{dc}}$ = {Vdc:.0f} V')
ax_vf.axhline(Vdc/2, color='gray', lw=1.0, ls=':', label=f'$V_{{dc}}/2$ = {Vdc/2:.0f} V')
ax_vf.set_ylabel(r'$v_f$ (V)', fontsize=11)
ax_vf.set_ylim(-40, Vdc + 100)
ax_vf.legend(loc='upper left', fontsize=9)
ax_vf.set_title(r"Pole-node voltage $v_f(t)$  — state variable 1", fontsize=10)

# ir panel
ax_ir.plot(t_us, ir_all, 'r-', lw=2.2, zorder=2)
ax_ir.axhline(IL,            color='green',    lw=1.2, ls=':',  label=f'$I_L$ = {IL:.0f} A')
ax_ir.axhline(IL + iboost,   color='darkorange', lw=1.0, ls='--', label=f'$I_L+i_{{boost}}$ = {IL+iboost:.0f} A')
ax_ir.set_ylabel(r'$i_r$ (A)', fontsize=11)
ax_ir.set_xlabel('Time (µs)', fontsize=11)
ax_ir.legend(loc='upper right', fontsize=9)
ax_ir.set_title(r"Auxiliary inductor current $i_r(t)$  — state variable 2", fontsize=10)

# Phase labels on top panel
label_y = Vdc + 55
for mid, label, col in [
    ((0 + m0) / 2,  'Phase 0\nIdle',          '#555'),
    ((m0 + m1) / 2, 'Phase 1\nBoost\n(linear)', '#7a4500'),
    ((m1 + m2) / 2, 'Phase 2\nResonant Swing\n(ODEs active here)', '#1a5c52'),
    ((m2 + m3) / 2, 'Phase 3\nPost-clamp\nramp ↓', '#6a5200'),
]:
    ax_vf.text(mid, label_y, label, ha='center', va='bottom', fontsize=7.5,
               color=col, linespacing=1.3)

# Annotation: ZVS turn-on
ax_ir.annotate('ZVS: $S_1$ fires here\n$i_r = 0$, $v_f = V_{dc}$',
               xy=(m3, 0), xytext=(m3 - 0.8, IL * 0.6),
               arrowprops=dict(arrowstyle='->', color='navy'), fontsize=8.5,
               color='navy')

fig1.tight_layout()
fig1.savefig('arcp_fig1_time_traces.png', dpi=150, bbox_inches='tight')
print("\nSaved: arcp_fig1_time_traces.png")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 2 — Phase plane: the circle in (vf, j·Zr) space
# ─────────────────────────────────────────────────────────────────────────────
fig2, ax2 = plt.subplots(figsize=(7.5, 7.5))
ax2.set_title("Phase Plane During Resonant Swing\n"
              r"Trajectory in $(v_f,\; j \cdot Z_r)$ space  — a perfect circle",
              fontsize=12, fontweight='bold')

# Full theoretical circle (for reference)
theta = np.linspace(0, 2 * np.pi, 600)
circ_u = R * np.cos(theta)      # u = vf - Vdc/2
circ_j = R * np.sin(theta)      # j*Zr
ax2.plot(Vdc / 2 + circ_u, circ_j, 'k--', lw=1, alpha=0.3,
         label=f'Full circle  R = {R:.1f} V')

# Actual trajectory (only the swing portion that executes)
ax2.plot(vf_swing, j_swing * Zr, color='#2a9d8f', lw=2.5, zorder=3,
         label='Actual trajectory (resonant swing)')

# Mark start and end
ax2.scatter([vf_swing[0]],  [j_swing[0]  * Zr], s=120, color='green',
            zorder=5, label=f'Start: $v_f=0$, $j_0 Z_r={j0*Zr:.1f}$ V')
ax2.scatter([vf_swing[-1]], [j_swing[-1] * Zr], s=120, marker='s', color='red',
            zorder=5, label=r'End: $v_f = V_{dc}$, $D_1$ clamps')

# Centre of circle
ax2.scatter([Vdc / 2], [0], s=200, marker='+', color='black', zorder=5, linewidths=2.5,
            label=f'Centre $(V_{{dc}}/2, 0)$')

# Radius arrow
ax2.annotate('', xy=(Vdc / 2 + R, 0), xytext=(Vdc / 2, 0),
             arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
ax2.text(Vdc / 2 + R / 2, 12, f'R = {R:.1f} V', ha='center', fontsize=9, color='gray')

# Vertical reference lines
ax2.axvline(0,     color='black', lw=0.7, ls=':')
ax2.axvline(Vdc/2, color='gray',  lw=0.8, ls=':', label=r'$v_f = V_{dc}/2$  (equilibrium)')
ax2.axvline(Vdc,   color='black', lw=0.7, ls=':')
ax2.axhline(0,     color='gray',  lw=0.7, ls=':')

# Annotations
ax2.annotate(r'Start: $v_f = 0$', xy=(vf_swing[0], j_swing[0] * Zr),
             xytext=(80, j_swing[0] * Zr + 60),
             arrowprops=dict(arrowstyle='->', color='green'), fontsize=9)
ax2.annotate(r'$D_1$ clamps at $v_f = V_{dc}$', xy=(vf_swing[-1], j_swing[-1] * Zr),
             xytext=(vf_swing[-1] - 250, j_swing[-1] * Zr + 50),
             arrowprops=dict(arrowstyle='->', color='red'), fontsize=9)

# Direction arrow on trajectory (midpoint)
mid = len(vf_swing) // 3
dx = vf_swing[mid + 5] - vf_swing[mid]
dy = (j_swing[mid + 5] - j_swing[mid]) * Zr
ax2.annotate('', xy=(vf_swing[mid] + dx * 10, (j_swing[mid] + (j_swing[mid+5]-j_swing[mid])*10) * Zr),
             xytext=(vf_swing[mid], j_swing[mid] * Zr),
             arrowprops=dict(arrowstyle='->', color='#2a9d8f', lw=2))

ax2.set_xlabel(r'$v_f$ (V)', fontsize=12)
ax2.set_ylabel(r'$j \cdot Z_r$ (V)    where $j \equiv i_r - I_L$', fontsize=12)
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.legend(loc='lower right', fontsize=8.5)

# Text box: circle equation
boxtext = (r"$u(t)^2 + [j(t) \cdot Z_r]^2 = R^2$" + "\n"
           r"$u = v_f - V_{dc}/2$" + "\n"
           fr"$R = \sqrt{{u_0^2 + (j_0 Z_r)^2}} = {R:.1f}$ V")
ax2.text(0.02, 0.04, boxtext, transform=ax2.transAxes, fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor='gray', alpha=0.9))

fig2.tight_layout()
fig2.savefig('arcp_fig2_phase_plane.png', dpi=150, bbox_inches='tight')
print("Saved: arcp_fig2_phase_plane.png")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 3 — Math derivation: KCL+KVL → oscillator → shifted state → circle
# ─────────────────────────────────────────────────────────────────────────────
fig3 = plt.figure(figsize=(11, 9))
ax3  = fig3.add_subplot(111)
ax3.axis('off')
ax3.set_title("From KCL + KVL to the Forced Oscillator — Step-by-Step Derivation\n"
              "(Green box in the reference document, P1 Fig.5)",
              fontsize=12, fontweight='bold', pad=15)

steps = [
    {
        'color': '#d0eaf8',
        'title': 'Step 1  —  KCL at the pole node  (Phase 2 only: A1 on, Cr charging, ir > IL)',
        'lines': [
            r'Net current into $C_r$  =  $i_r - I_L$',
            r'$C_r \dfrac{dv_f}{dt} = i_r - I_L$',
            r'$\Longrightarrow\quad \dfrac{dv_f}{dt} = \dfrac{i_r - I_L}{C_r}$     ...(1)',
        ],
    },
    {
        'color': '#d8f0e0',
        'title': r'Step 2  —  KVL around the auxiliary loop  (A1 on: $V_{dc}/2$ drives $L_r$)',
        'lines': [
            r'Voltage across $L_r$  =  $V_{dc}/2 - v_f$',
            r'$L_r \dfrac{di_r}{dt} = \dfrac{V_{dc}}{2} - v_f$',
            r'$\Longrightarrow\quad \dfrac{di_r}{dt} = \dfrac{V_{dc}/2 - v_f}{L_r}$     ...(2)',
        ],
    },
    {
        'color': '#fff3cd',
        'title': 'Step 3  —  Combine: differentiate (1), substitute (2)',
        'lines': [
            r'$\frac{d^2 v_f}{dt^2} = \frac{1}{C_r} \frac{di_r}{dt} = \frac{1}{C_r} \cdot \frac{V_{dc}/2 - v_f}{L_r}$',
            r'$\Rightarrow\quad \ddot{v}_f + \omega_r^2\, v_f = \omega_r^2 \frac{V_{dc}}{2}$'
            r'      where $\omega_r^2 = \frac{1}{L_r C_r}$   [Forced harmonic oscillator]',
            r'Equilibrium (forced solution) sits at $v_f = V_{dc}/2$, not at 0.',
        ],
    },
    {
        'color': '#f8d7da',
        'title': r'Step 4  —  Shifted state  j := i_r - I_L  removes I_L from the equations',
        'lines': [
            r'With $j = i_r - I_L$:   $\dot{v}_f = j/C_r$,   $\dot{j} = (V_{dc}/2 - v_f)/L_r$',
            r'Let $u = v_f - V_{dc}/2$.  Then: $\dot{u} = j/C_r$,   $\dot{j} = -u/L_r$',
            r'$\Rightarrow\quad \ddot{u} + \omega_r^2 u = 0$     [SHM in $(u,\,j)$ space — no forcing term!]',
            r'$I_L$ disappears from the ODE. Load current only sets the initial conditions.',
        ],
    },
    {
        'color': '#e8d5f0',
        'title': r'Step 5  —  Analytic solution and the circle',
        'lines': [
            r'IC at start of swing: $u_0 = -V_{dc}/2$,  $j_0 = i_{boost}$',
            r'$u(t) = u_0 \cos(\omega_r t) + j_0 Z_r \sin(\omega_r t)$,   '
            r'$j(t) = -(u_0/Z_r)\sin(\omega_r t) + j_0 \cos(\omega_r t)$',
            r'Check: $u(t)^2 + [j(t) Z_r]^2 = u_0^2 + (j_0 Z_r)^2 = R^2$  (constant)',
            r'$\Rightarrow$ Circle in $(v_f,\; j Z_r)$ space, centre $(V_{dc}/2,\,0)$, radius $R$.',
        ],
    },
]

y_top  = 0.93
height = 0.165
gap    = 0.01

for i, step in enumerate(steps):
    y0 = y_top - i * (height + gap) - height
    rect = mpatches.FancyBboxPatch(
        (0.01, y0), 0.98, height,
        boxstyle="round,pad=0.008",
        facecolor=step['color'], edgecolor='#999', lw=0.8,
        transform=ax3.transAxes, clip_on=False
    )
    ax3.add_patch(rect)
    # Title line
    ax3.text(0.03, y0 + height - 0.018, step['title'],
             transform=ax3.transAxes, fontsize=8.5, fontweight='bold',
             va='top', color='#333')
    # Content lines
    dy_line = (height - 0.032) / max(len(step['lines']), 1)
    for k, line in enumerate(step['lines']):
        ax3.text(0.05, y0 + height - 0.030 - k * dy_line, line,
                 transform=ax3.transAxes, fontsize=8.5, va='top', color='#222')

fig3.tight_layout()
fig3.savefig('arcp_fig3_math_derivation.png', dpi=150, bbox_inches='tight')
print("Saved: arcp_fig3_math_derivation.png")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURE 4 — Effect of iboost on commutation (ZVS condition visualized)
# ─────────────────────────────────────────────────────────────────────────────
fig4, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(12, 5.5))
fig4.suptitle("Effect of Boost Current on Commutation\n"
              r"(Resonant swing from $v_f = 0$ to $v_f = V_{dc}$)",
              fontsize=12, fontweight='bold')

t_full  = np.linspace(0, Tr / 2, 2000)
cases   = [
    (20.0, '#1d6fa4', r'$i_{boost}$ = 20 A  (large boost)'),
    (10.0, '#2a9d8f', r'$i_{boost}$ = 10 A  (nominal)'),
    (2.0,  '#f4a261', r'$i_{boost}$ = 2 A   (small boost)'),
    (-10.0,'#e63946', r'$j_0 = -10$ A  (wrong direction → v_f drops first)'),
]

for ax, ylabel_unit in [(ax_left, 'vf'), (ax_right, 'ir')]:
    ax.axhline(Vdc if ylabel_unit == 'vf' else IL + 10,
               color='black', lw=0.5, ls=':')

for iboost_val, col, lbl in cases:
    j0_v  = iboost_val       # j = ir - IL at start of swing
    u0_v  = -Vdc / 2

    u_t  = u0_v * np.cos(wr * t_full) + j0_v * Zr * np.sin(wr * t_full)
    j_t  = -(u0_v / Zr) * np.sin(wr * t_full) + j0_v * np.cos(wr * t_full)
    vf_t = Vdc / 2 + u_t
    ir_t = IL + j_t

    # Clip at vf = Vdc (D1 clamps there)
    mask = vf_t <= Vdc + 1
    idx_end = np.argmax(~mask)
    if idx_end == 0:
        idx_end = len(t_full)
    t_plot  = t_full[:idx_end] * 1e6   # µs
    vf_plot = vf_t[:idx_end]
    ir_plot = ir_t[:idx_end]

    ls = '--' if iboost_val < 0 else '-'
    ax_left.plot(t_plot,  vf_plot, color=col, lw=2, ls=ls, label=lbl)
    ax_right.plot(t_plot, ir_plot, color=col, lw=2, ls=ls)

ax_left.axhline(Vdc,   color='black', lw=1.5, ls=':', label=f'Target $V_{{dc}}$ = {Vdc:.0f} V')
ax_left.axhline(Vdc/2, color='gray',  lw=0.8, ls=':', label='Equilibrium $V_{dc}/2$')
ax_left.axhline(0,     color='gray',  lw=0.8, ls=':')
ax_left.set_xlabel('Time (µs)', fontsize=10)
ax_left.set_ylabel(r'$v_f$ (V)', fontsize=11)
ax_left.set_title(r'Pole voltage $v_f(t)$ — must reach $V_{dc}$ for ZVS', fontsize=10)
ax_left.legend(fontsize=8, loc='upper left')
ax_left.set_ylim(-120, Vdc + 120)
ax_left.grid(True, alpha=0.3)

ax_right.axhline(IL, color='green', lw=1.2, ls=':', label=f'$I_L$ = {IL:.0f} A')
ax_right.axhline(0,  color='gray',  lw=0.8, ls=':')
ax_right.set_xlabel('Time (µs)', fontsize=10)
ax_right.set_ylabel(r'$i_r$ (A)', fontsize=11)
ax_right.set_title(r'Auxiliary current $i_r(t)$  (same colour code)', fontsize=10)
ax_right.legend(fontsize=9, loc='upper right')
ax_right.grid(True, alpha=0.3)

# Annotation on left panel
ax_left.annotate('j0 < 0: vf initially drops!\n(wrong direction)',
                 xy=(0.15, -80), xytext=(0.5, -80),
                 arrowprops=dict(arrowstyle='->', color='#e63946'), fontsize=8.5,
                 color='#e63946')

fig4.tight_layout()
fig4.savefig('arcp_fig4_zvs_condition.png', dpi=150, bbox_inches='tight')
print("Saved: arcp_fig4_zvs_condition.png")

# ─────────────────────────────────────────────────────────────────────────────
plt.show()

print()
print("=" * 60)
print("Summary:")
print("  arcp_fig1_time_traces.png   — 4 phases with vf(t) and ir(t)")
print("  arcp_fig2_phase_plane.png   — circular trajectory in (vf, j·Zr)")
print("  arcp_fig3_math_derivation.png — KCL+KVL → oscillator → circle")
print("  arcp_fig4_zvs_condition.png — effect of j0 on commutation success")
print("=" * 60)
