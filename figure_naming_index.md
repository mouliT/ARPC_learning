# ARCP Figure Naming Index
# Naming convention: [PaperID]_Fig[number]_[description].png
# PaperIDs: P1 = De Doncker & Lyons 1990 | P2 = Walters & Wasyncuk (Purdue) | P3 = ITEC / NASA Glenn
# Dot in figure number written as 'p': Fig3.4 → Fig3p4

---

## PAPER 1 — De Doncker & Lyons, IEEE IAS 1990
**File:** `The_auxiliary_resonant_commutated_pole_converter.pdf`

| Filename | Page | Original Caption | Key Equations | Figure Type |
|----------|------|-----------------|---------------|-------------|
| `P1_Fig1_resonant_pole_inverter.png` | 1 | The Resonant Pole Inverter (RPI) | — | Circuit topology |
| `P1_Fig2_resonant_pole_load_side.png` | 1 | Resonant Inverter Pole at Load Side | — | Circuit topology |
| `P1_Fig3_ARDPI_topology.png` | 2 | Auxiliary Resonant Diode Pole Inverter (ARDPI) | — | Circuit topology (×2 variants) |
| `P1_Fig4_ARPI_topology.png` | 2 | Auxiliary Resonant Pole Inverter (ARPI) | — | Circuit topology |
| `P1_Fig5_ARCP_pole_leg.png` | 3 | The Auxiliary Resonant Commutated Pole (ARCP) | — | **Primary circuit topology** |
| `P1_Fig6_ARCP_ac_to_ac_system.png` | 3 | ARCP ac-to-ac Converter | — | System-level topology |
| `P1_Fig7a_state1_D2_conducting.png` | 4 | Commutation from Diode — State (a): $D_2$ conducts, $\vf=0$, $\ir=0$ | — | Initial idle state |
| `P1_Fig7b_state2_A1_boost_start.png` | 4 | Commutation from Diode — State (b): $A_1$ fires, $\ir$ ramps up linearly | $\dot{i}_r = V_{dc}/2L_r$ | Boost phase begins |
| `P1_Fig7c_state3_boost_complete.png` | 4 | Commutation from Diode — State (c): $\ir = I_L + i_\text{boost}$, resonant swing starts | $I_\text{peak} = I_L + i_\text{boost} + V_{dc}/2Z_r$ | Boost ends, LC swing begins |
| `P1_Fig7d_state4_resonant_swing.png` | 4–5 | Commutation from Diode — State (d): $\vf$ swings toward $V_{dc}$, LC trajectory | $\ddot{v}_f + \omega_r^2 v_f = \omega_r^2 V_{dc}/2$ | **Core resonant swing** |
| `P1_Fig7e_state5_upper_diode_clamp.png` | 5 | Commutation from Diode — State (e): $\vf = V_{dc}$, $D_1$ clamps, $A_1$ turns off | ZVS condition met | Upper rail reached |
| `P1_Fig7f_state6_ir_ramps_down.png` | 5 | Commutation from Diode — State (f): $\ir$ ramps back to 0, $S_1$ fires at ZVS | $\dot{i}_r = -V_{dc}/2L_r$ | ZVS turn-on of $S_1$ |
| `P1_Fig7g_state7_S1_steady.png` | 5 | Commutation from Diode — State (g): $S_1$ conducting, $\ir=0$, steady state | — | Commutation complete |
| `P1_Fig8a_waveform_switch_low_current.png` | 5 | Commutation from Switch (Low $I$) — Full waveform with all timing strips labelled (S1/A1, Cr/A1, D2/A1, S2) | — | **Waveform only** (no circuit snapshot) |
| `P1_Fig8b_state1_S1_conducting.png` | 5 | Commutation from Switch (Low $I$) — State (b): $S_1$ on, $v_f=V_{dc}$, $i_r=0$ | — | Initial idle state (mirror of Fig.\,7g) |
| `P1_Fig8c_state2_A1_boost_start.png` | 5 | Commutation from Switch (Low $I$) — State (c): $A_1$ fires; $i_r$ ramps up; $S_1$ still on | $\dot{i}_r = V_{dc}/(2L_r)$ | Boost phase; $S_1$ carries $I_L+i_r$ |
| `P1_Fig8d_state3_resonant_swing.png` | 5 | Commutation from Switch (Low $I$) — State (d): $S_1$ gated off; LC resonant swing; $v_f: V_{dc}\to 0$ | $\ddot{v}_f+\omega_r^2 v_f=\omega_r^2 V_{dc}/2$ | **Core resonant swing** (downward) |
| `P1_Fig8e_state4_D2_clamp.png` | 5 | Commutation from Switch (Low $I$) — State (e): $D_2$ clamps $v_f=0$; $S_2$ gated on at ZVS; $A_1$ still on; $i_r$ ramps down | $\dot{i}_r = -V_{dc}/(2L_r)$ | Clamp + ramp-down; $A_1$ on until $i_r=0$ |
| `P1_Fig8f_state5_S2_steady.png` | 5 | Commutation from Switch (Low $I$) — State (f): $S_2$ conducting, $i_r=0$, $A_1$ gated off | — | Commutation complete (mirror of Fig.\,7g) |
| `P1_Fig9a_waveform_switch_high_current.png` | 6 | Commutation from Switch (High $I$) — Full waveform with all timing strips labelled | — | **Waveform only** (no circuit snapshot) |
| `P1_Fig9b_state1_S1_conducting.png` | 6 | Commutation from Switch (High $I$) — State (a): $S_1$ on, $v_f = V_{dc}$, $I_L \geq I_{th}$, no boost needed | — | Initial idle state (downward commutation) |
| `P1_Fig9c_state2_natural_swing.png` | 6 | Commutation from Switch (High $I$) — State (b): $S_1$ off; $I_L$ alone discharges $C_r$; $v_f$ falls $V_{dc} \to 0$ | $\dot{v}_f = -I_L/(2C_r)$ | Natural capacitive discharge |
| `P1_Fig9d_state3_S2_ZVS_on.png` | 6 | Commutation from Switch (High $I$) — State (c): $D_2$ clamps at $v_f = 0$; $S_2$ fires at ZVS | ZVS achieved | Commutation complete |
| `P1_Fig10a_vf_low_current.png` | 7 | ARCP Commutation at Low Current — top panel: $v_f(t)$ | — | Simulated $v_f(t)$ time trace |
| `P1_Fig10b_ir_low_current.png` | 7 | ARCP Commutation at Low Current — bottom panel: $i_r(t)$ | — | Simulated $i_r(t)$ time trace |
| `P1_Fig11a_vf_high_current.png` | 7 | ARCP Commutation at High Current — top panel: $v_f(t)$ | — | Simulated $v_f(t)$ time trace |
| `P1_Fig11b_ir_high_current.png` | 7 | ARCP Commutation at High Current — bottom panel: $i_r(t)$ | — | Simulated $i_r(t)$ time trace |

---

## PAPER 2 — Walters & Wasyncuk, Purdue University
**File:** `Analysis of the auxiliary resonant commutated pole inverter.pdf`

| Filename | Page | Original Caption | Key Equations | Figure Type |
|----------|------|-----------------|---------------|-------------|
| `P2_Fig2p1_hard_switched_BJT_leg.png` | 4 | A Hard-Switched Phase Leg Using BJTs | $v_\text{load}$ expressions (2-1) to (2-10) | Circuit topology (baseline reference) |
| `P2_Fig2p2_BJT_IC_VCE_characteristic.png` | 5 | $I_C$ vs $V_{CE}$ with Constant $I_B$ | — | Device characteristic curve |
| `P2_Fig2p3_BJT_turn_on_waveforms.png` | 9 | Simplified Turn-On Switching Waveforms | $E_\text{on} = V_{dc}\,i_\text{load}\,t_r$ (2-16, 2-19) | 4-trace time-domain waveforms |
| `P2_Fig2p4_BJT_turn_off_waveforms.png` | 11 | Simplified Turn-Off Switching Waveform | $E_\text{off} = V_{dc}\,i_\text{load}\,t_c$ (2-22, 2-25) | 4-trace time-domain waveforms |
| `P2_Fig3p1_ARCP_circuit_full.png` | 16 | The Auxiliary Resonant Commutated Pole (ARCP) | $\dot{i}_r = V_{dc}/(2L_r)$ (3-1 to 3-4) | Full ARCP circuit with state-space notation |
| `P2_Fig3p2_state1_lower_switch_on.png` | 16 | Circuit Diagram of ARCP in State 1 | $\dot{V}_{C1}=0,\ \dot{i}_r=0$ | Equivalent circuit — idle state |
| `P2_Fig3p3_state2_boost_phase.png` | 17 | Circuit Diagram of ARCP in State 2 | $\dot{i}_r = V_{dc}/(2L_r)$ (3-5, 3-6) | Equivalent circuit — linear $i_r$ ramp |
| `P2_Fig3p4_state3_resonant_swing.png` | 18 | Circuit Diagram of ARCP in State 3 | $\dot{V}_{C1}=(i_L-i_r)/(2C_r)$, $\dot{i}_r=(V_{C1}-V_{dc}/2)/L_r$ (3-9 to 3-11) | **Key equiv. circuit — LC oscillation** |
| `P2_Fig3p5_state4_post_clamp.png` | 20 | Circuit Diagram of ARCP in State 4 | $\dot{V}_{C1}=0,\ \dot{i}_r=-V_{dc}/(2L_r)$ (3-12, 3-13) | Equivalent circuit — $i_r$ ramps down |
| `P2_Fig3p6_state5_upper_switch_ZVS.png` | 20 | Circuit Diagram of ARCP in State 5 | — | Equivalent circuit — ZVS turn-on |
| `P2_Fig3p7_sim_commutation_diode.png` | 22 | ARCP Commutation Low-to-High from Diode | — | Simulated $V_{C1}(t)$ and $i_r(t)$ |
| `P2_Fig3p8_sim_commutation_switch_low_I.png` | 24 | ARCP Commutation Low-to-High from Switch (Low $I$) | — | Simulated $V_{C1}(t)$ and $i_r(t)$ |
| `P2_Fig3p9_state6_high_current.png` | 25 | Circuit Diagram of ARCP in State 6 | $\dot{V}_{C1}=i_L/(2C_r),\ \dot{i}_r=0$ (3-16, 3-17) | Equivalent circuit — natural commutation |
| `P2_Fig3p10_sim_commutation_switch_high_I.png` | 26 | ARCP Commutation Low-to-High from Switch (High $I$) | — | Simulated $V_{C1}(t)$ and $i_r(t)$ |
| `P2_Fig4p1_Hbridge_ARCP.png` | 28 | H-Bridge Using Two ARCP Phase Legs | — | Full H-bridge system topology |
| `P2_Fig4p2_PWM_vload_waveforms.png` | 29 | $v_\text{load}$ vs. Time and PWM Waveforms | — | 3-trace PWM control waveforms |
| `P2_Fig4p3_energy_loss_comparison.png` | 30 | Energy Losses: Hard-Switched vs. ARCP | — | Comparative loss accumulation plots |
| `P2_Fig4p4_Hbridge_VC1_ir1.png` | 31 | H-Bridge $V_{C1}$ and $i_{r1}$ vs. Time | — | Leg 1 simulated waveforms |
| `P2_Fig4p5_Hbridge_VC2_ir2.png` | 32 | H-Bridge $V_{C2}$ and $i_{r2}$ vs. Time | — | Leg 2 simulated waveforms |
| `P2_Fig4p6_Hbridge_iload_vload.png` | 33 | H-Bridge $i_\text{load}$ and $v_\text{load}$ vs. Time | — | Load current and voltage waveforms |

---

## PAPER 3 — Belovich et al., ITEC / NASA Glenn Research Center
**File:** `ITEC_Resonant_Algorithms_Paper_Final.pdf`

| Filename | Page | Original Caption | Key Equations | Figure Type |
|----------|------|-----------------|---------------|-------------|
| `P3_Fig1_ARCP_FPGA_circuit.png` | 1 | Electrical Diagram of ARCP Inverter (One Phase Leg) | $L_r=0.33\,\mu\text{H},\ C_r=1\,\text{nF},\ V_{dc}=500\,\text{V},\ f_s=100\,\text{kHz}$ | FPGA-driven circuit implementation |
| `P3_Fig2_Atype_commutation_waveforms.png` | 2 | ARCP Waveforms — A-Type Commutation | — | Control + resonant waveforms (4 panels) |
| `P3_Fig3_Btype_capacitive_waveforms.png` | 2 | ARCP Waveforms — B-Type Capacitive Commutation | — | Waveforms at near-zero load current |
| `P3_Fig4_Btype_resonant_waveforms.png` | 2 | ARCP Waveforms — B-Type Resonant Commutation | — | Waveforms with resonant assist at low $i_L$ |
| `P3_Fig5_FTOL_simulation.png` | 3 | Simulation Results of FTOL Control Method | $T_\text{ramp}=63.4\,\text{ns},\ T_\text{res}=30.7\,\text{ns}$ | 3-panel MATLAB simulation |
| `P3_Fig6_FTCL_simulation.png` | 4 | Simulation Results of FTCL Control Method | $T_\text{ramp}=2L_rI_L/V_{dc}$, $T_\text{res}=\pi\sqrt{L_rC_r}$, $T_\text{res,B}=\frac{2}{\omega_r}\tan^{-1}(V_{dc}/2I_LZ_r)$ | 3-panel closed-loop simulation |
| `P3_Fig7_Atype_experimental.png` | 4 | A-Type Commutation — Experimental | — | Oscilloscope trace (hardware validation) |
| `P3_Fig8_toplevel_state_machine.png` | 4 | Top-Level State Machine | $I_{th}$ threshold | 4-state FPGA flowchart |
| `P3_Fig9_detailed_state_machine_AB.png` | 5 | Detailed State Machine — A-Type and B-Type Resonant | Counter values, $T_\text{RAMP}$, $T_\text{RES}$ states | FPGA state machine (A-type red, B-res green) |
| `P3_Fig10_detailed_state_machine_Bcap.png` | 5 | Detailed State Machine — B-Type Capacitive | $T_\text{RES}$, $T_\text{RAMP\_2}$ | FPGA state machine (B-cap path) |

---

## Quick-Reference: Priority Figures for Step 1 Study

| Priority | Filename | Why |
|----------|----------|-----|
| ⭐⭐⭐ | `P1_Fig5_ARCP_pole_leg.png` | The circuit — draw and memorize first |
| ⭐⭐⭐ | `P1_Fig7a` – `P1_Fig7g` (7 files) | Full commutation sequence — one PNG per state |
| ⭐⭐⭐ | `P2_Fig3p4_state3_resonant_swing.png` | The two governing ODEs of the LC swing |
| ⭐⭐ | `P1_Fig8a` – `P1_Fig8e` (5 files) | Low-current path: S2 turn-off + boost + resonant swing |
| ⭐⭐ | `P1_Fig9a` – `P1_Fig9d` (4 files) | High-current natural commutation (no boost) |
| ⭐⭐ | `P1_Fig10a/b` and `P1_Fig11a/b` (4 files) | Simulated $v_f$ and $i_r$ for low- and high-current commutation |
| ⭐⭐ | `P2_Fig4p3_energy_loss_comparison.png` | Core motivation: ARCP vs hard-switching |
| ⭐ | `P3_Fig8_toplevel_state_machine.png` | How physics maps to control logic |
