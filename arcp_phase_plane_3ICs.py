"""
arcp_phase_plane_3ICs.py
=========================
Phase-plane plot of the ARCP resonant swing for three initial condition vectors.

All three start from vf0 = 0 (pole node clamped to lower rail before swing).
The three cases differ only in j0 = i_boost (the boost current above IL).

The trajectory in (vf, j*Zr) space is a circle because:
    E = u^2 + (j*Zr)^2  is conserved  (proved in the LaTeX green box)
where u = vf - Vdc/2.

Run:  py arcp_phase_plane_3ICs.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Parameters ───────────────────────────────────────────────────────────────
Vdc = 600.0          # DC bus voltage [V]
Lr  = 4e-6           # Resonant inductance [H]
Cr  = 47e-9          # Total snubber capacitance at pole node [F]
IL  = 30.0           # Load current (quasi-constant) [A]

wr = 1.0 / np.sqrt(Lr * Cr)    # Resonant angular frequency [rad/s]
Zr = np.sqrt(Lr / Cr)           # Characteristic impedance [Ω]
Tr = 2 * np.pi / wr             # Full resonant period [s]

print(f"Zr = {Zr:.2f} Ohm,   wr = {wr/1e6:.3f} Mrad/s,   fr = {wr/(2*np.pi)/1e3:.1f} kHz")

# ── Three initial condition vectors ───────────────────────────────────────────
# All have:  vf0 = 0   →   u0 = vf0 - Vdc/2 = -Vdc/2
# They differ in j0 = i_boost (auxiliary current above IL at start of swing)
ICs = [
    {
        'j0':    0.0,
        'label': r'IC-1:  $j_0 = 0$ A  (no boost, $i_{boost}=0$)',
        'color': '#e63946',
    },
    {
        'j0':   10.0,
        'label': r'IC-2:  $j_0 = 10$ A  ($i_{boost}=10$ A)',
        'color': '#2a9d8f',
    },
    {
        'j0':   20.0,
        'label': r'IC-3:  $j_0 = 20$ A  ($i_{boost}=20$ A)',
        'color': '#264653',
    },
]

# ── Figure ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8.5, 8.5))
ax.set_title(
    r"Phase Plane $(v_f,\; j \cdot Z_r)$ — Three Initial Condition Vectors"
    "\n"
    r"All start at $v_{f0}=0$, $u_0=-V_{dc}/2$;  vary $j_0 = i_{boost}$",
    fontsize=11, fontweight='bold', pad=12
)

t = np.linspace(0, Tr / 2, 8000)

for ic in ICs:
    j0 = ic['j0']
    u0 = -Vdc / 2          # fixed: vf0=0 → u0 = 0 - Vdc/2

    # Radius of this circle
    R = np.sqrt(u0**2 + (j0 * Zr)**2)

    # Analytical solution during resonant swing
    u_t   = u0 * np.cos(wr * t) + j0 * Zr * np.sin(wr * t)
    j_t   = -(u0 / Zr) * np.sin(wr * t) + j0 * np.cos(wr * t)
    vf_t  = Vdc / 2 + u_t
    jZr_t = j_t * Zr

    # Stop at first crossing of vf = Vdc  (D1 clamps)
    idx = np.argmax(vf_t >= Vdc - 0.5)
    if idx == 0:
        idx = len(t) - 1

    # Plot actual trajectory (solid)
    ax.plot(vf_t[:idx + 1], jZr_t[:idx + 1],
            color=ic['color'], lw=2.5, zorder=3,
            label=f"{ic['label']}\n"
                  r"$\quad R = \sqrt{(V_{dc}/2)^2 + (j_0 Z_r)^2}$"
                  f" = {R:.1f} V")

    # Full dashed circle (for reference)
    theta = np.linspace(0, 2 * np.pi, 600)
    ax.plot(Vdc / 2 + R * np.cos(theta), R * np.sin(theta),
            color=ic['color'], lw=0.9, ls='--', alpha=0.35, zorder=2)

    # Start point ● (circle marker)
    ax.scatter([vf_t[0]], [jZr_t[0]],
               s=140, color=ic['color'], edgecolors='black', lw=0.8, zorder=6)

    # End point ■ (square marker — where D1 clamps)
    ax.scatter([vf_t[idx]], [jZr_t[idx]],
               s=140, marker='s', color=ic['color'], edgecolors='black', lw=0.8, zorder=6)

    # Label the radius on the dashed circle
    # Place label at the top of each circle
    ax.text(Vdc / 2, R + 8, f"R={R:.0f} V",
            ha='center', fontsize=8, color=ic['color'], fontweight='bold')

# ── Reference lines ───────────────────────────────────────────────────────────
for xval, xlbl in [(0, r'$0$'), (Vdc / 2, r'$V_{dc}/2$'), (Vdc, r'$V_{dc}$')]:
    ax.axvline(xval, color='gray', lw=0.9, ls=':', zorder=1)
    ax.text(xval, -55, xlbl, ha='center', va='top', fontsize=9.5, color='#555')

ax.axhline(0, color='gray', lw=0.9, ls=':', zorder=1)

# Centre of all circles (common to all three ICs in (vf, jZr) plane)
ax.scatter([Vdc / 2], [0], s=220, marker='+', color='black',
           lw=2.5, zorder=7, label=r'Common centre $(V_{dc}/2,\;0)$')

# ── Legend entries for markers ────────────────────────────────────────────────
start_patch = mpatches.Patch(color='gray', label=r'● Start: $(v_{f0}=0,\; j_0 Z_r)$')
end_patch   = mpatches.Patch(color='gray', label=r'■ End: $D_1$ clamps at $v_f = V_{dc}$')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles + [start_patch, end_patch],
          labels  + [r'● Start: $(v_{f0}=0,\; j_0 Z_r)$',
                     r'■ End: $D_1$ clamps at $v_f = V_{dc}$'],
          loc='lower right', fontsize=8.5, framealpha=0.9)

# ── Formula box ───────────────────────────────────────────────────────────────
formula = (
    r"$u = v_f - V_{dc}/2$" + "\n"
    r"$\mathcal{E} = u^2 + (j Z_r)^2 = R^2$  (constant)" + "\n"
    r"$R = \sqrt{u_0^2 + (j_0 Z_r)^2}$" + "\n"
    r"$= \sqrt{(V_{dc}/2)^2 + (i_{boost}\,Z_r)^2}$"
)
ax.text(0.02, 0.97, formula,
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#fffde7',
                  edgecolor='#aaa', alpha=0.95))

ax.set_xlabel(r'$v_f$  (V)', fontsize=12)
ax.set_ylabel(r'$j \cdot Z_r$  (V)     where $j = i_r - I_L$', fontsize=12)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

fig.tight_layout()
out = 'arcp_phase_plane_3ICs.png'
fig.savefig(out, dpi=150, bbox_inches='tight')
print(f"Saved: {out}")
plt.show()
