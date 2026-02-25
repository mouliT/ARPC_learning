# ARCP Literature — Figure Index
**Generated from:** De Doncker & Lyons 1990 · Walters & Wasyncuk (Purdue) · ITEC/NASA Glenn
**Total figures indexed:** 40 across 3 papers

---

## Paper 1: The Auxiliary Resonant Commutated Pole Converter
**De Doncker & Lyons, IEEE IAS Annual Meeting, 1990**

| Fig | Page | Caption | Type | State Variables | Equations on Page | Description |
|-----|------|---------|------|----------------|-------------------|-------------|
| 1 | 1 | The Resonant Pole Inverter (RPI) | Circuit topology | $I_r, I_0, V_f, V_{DC}$ | — | Baseline resonant pole with filter caps $C_r$, switches $S_1/S_2$, diodes $D_1/D_2$, resonant inductor $L_r$, output filter $L_F, C_f$ |
| 2 | 1 | Resonant Inverter Pole at Load Side | Circuit topology | $I_r, I_F, V_{DC}, L_r, L_F$ | — | Simplified pole leg with inductive load — introduces $I_F$ (filter/load current) notation |
| 3 | 2 | Auxiliary Resonant Diode Pole Inverter (ARDPI) | Circuit topology (×2) | $V_{DC}, I_r, I_F, C_r, L_r$ | — | Two variants (a, b) showing auxiliary diodes $D_{a1}, D_{a2}$ placed in parallel to reduce $C_r$ stress |
| 4 | 2 | Auxiliary Resonant Pole Inverter (ARPI) | Circuit topology | $V_{DC}, I_r, I_F, C_r, L_r$ | — | Intermediate topology — full auxiliary resonant pole network before adding commutated switches |
| 5 | 3 | The Auxiliary Resonant Commutated Pole (ARCP) | Circuit topology | $V_{DC}, I_r, I_F, C_r, L_r, V_f$ | — | **Key figure.** Complete ARCP phase leg: snubber caps $C_r$, auxiliary thyristors $A_1/A_2$, main switches $S_1/S_2$, diodes $D_1/D_2$, resonant inductor $L_r$ |
| 6 | 3 | ARCP ac-to-ac Converter | System topology | $V_{DC}, I_r, C_f, L_f$ | — | Full three-phase system: rectifier + ARCP inverter + output filter |
| 7 | 4–5 | Commutation from Diode (states a–g) | Switching sequence | $V_{DC}, V_f, I_r, I_z, I_1, D_2, S_1, S_2$ | $I_\text{peak} = I_L + i_\text{boost} + \dfrac{V_{dc}}{2Z_r}$ | **Key figure.** 7-state sequence for turning off a conducting diode using auxiliary resonant circuit |
| 8 | 5 | Commutation from Switch — Low Current (states a–e) | Switching sequence | $I_r, V_f, S_1, D_2$ | $T_c = \dfrac{2L_r(2I_L + I_\text{boost})}{V_{dc}} + \pi\sqrt{L_rC_r}$ | 5-state sequence for low current switch commutation with boost phase |
| 9 | 6 | Commutation from Switch — High Current (states a–c) | Switching sequence | $V_f, I_r, S_1, C_r, D_2$ | $I_{th} = \dfrac{2C_r V_{dc}}{T_\text{max}}$ | High current case: load current alone drives resonant swing, no auxiliary boost needed |
| 10 | 7 | ARCP Commutation at Low Current | Simulated waveforms | $I_r, V_f, i_\text{load}, i_\text{boost}$ | — | Two time traces ($I_r$ and $V_f$) showing resonant current and pole voltage during low-current commutation |
| 11 | 7 | ARCP Commutation at High Current | Simulated waveforms | $I_r, V_f, i_\text{load}$ | — | Two time traces showing different resonant profile when load current dominates |

---

## Paper 2: Analysis of the Auxiliary Resonant Commutated Pole Inverter
**Walters & Wasyncuk, Purdue University**

| Fig | Page | Caption | Type | State Variables | Equations on Page | Description |
|-----|------|---------|------|----------------|-------------------|-------------|
| 2.1 | 4 | A Hard-Switched Phase Leg Using BJTs | Circuit topology | $V_{DC}, I_{C1}, I_{C2}, V_{CE1}, V_{CE2}$ | (2-1) through (2-10): $v_\text{load}$ expressions for all 4 switching states | Baseline hard-switched leg — reference for loss comparison throughout paper |
| 2.2 | 5 | $I_C$ vs $V_{CE}$ with Constant $I_B$ | Characteristic curve | $I_C, V_{CE}, I_B, V_{CE,sat}$ | — | BJT output characteristic showing saturation/active regions; motivation for loss model |
| 2.3 | 9 | Simplified Turn-On Switching Waveforms (BJT) | Time-domain waveforms | $V_{CE1}, i_\text{load}, I_{C1}, P_\text{max}, t_r$ | (2-15) $E_{D2}=\int P_{D2}\,dt$ · (2-16) $E_{Q1,\text{on}}=\tfrac{1}{2}(2V_{dc}\,i_\text{load})\,t_r$ · (2-17) $I_{D2}=i_\text{load}-I_{C1}$ · (2-18) $E_{D2,\text{on}}=\tfrac{1}{4}i_\text{load}V_{D2}t_r$ · (2-19) $E_\text{on}=\tfrac{1}{2}(2V_{dc}\,i_\text{load})\,t_r+\tfrac{1}{4}i_\text{load}V_{D2}t_r$ | 4 waveforms: $V_{CE}$, $I_B$, $I_{C1}$, $P_{diss}$ during turn-on; visual derivation of $E_{Q1,\text{on}}$ |
| 2.4 | 11 | Simplified Turn-Off Switching Waveform (BJT) | Time-domain waveforms | $V_{CE2}, I_{C2}, P_\text{max}, t_c$ | (2-21) $E_{Q2,\text{con}}=V_{CE,sat}i_\text{load}t$ · (2-22) $E_{Q2,\text{off}}=\tfrac{1}{2}(2V_{dc}\,i_\text{load})\,t_c$ · (2-23) $I_{D1}=I_{C1}-i_\text{load}$ · (2-24) $E_{D1,\text{off}}=-\tfrac{1}{4}i_\text{load}V_{D1}t_c$ | 4 waveforms showing voltage rise, current decay, and $P_{diss}$ during turn-off |
| 3.1 | 16 | The Auxiliary Resonant Commutated Pole (ARCP) | Circuit topology | $V_{DC}, C_{dc}, L_r, C_r, i_r, I_f, V_f$ | (3-1) $\dot{V}_{C1}=0$ · (3-2) $\dot{i}_r=0$ · (3-3) $\dot{V}_{C1}=0$ · (3-4) $\dot{i}_r=V_{dc}/(2L_r)$ | Paper 2's main ARCP circuit — same topology as Fig. 5 of Paper 1, with state-space notation |
| 3.2 | 16 | ARCP Equivalent Circuit — State 1 | Equivalent circuit | $V_{dc}, C_1, V_{C1}, i_\text{load}$ | (3-1): $\dot{V}_{C1}=0$ · (3-2): $\dot{i}_r=0$ | Idle state: lower switch conducts, $V_{C1}=0$, $i_r=0$ |
| 3.3 | 17 | ARCP Equivalent Circuit — State 2 | Equivalent circuit | $V_{dc}, L_r, C_1, V_{C1}, i_\text{load}, i_r$ | (3-5) KCL: $i_r+C_1\dot{V}_{C1}-C_2\dot{V}_{C2}-i_\text{load}=0$ · (3-6) $V_{C1}+V_{C2}=V_{dc}$ | Boost phase: auxiliary switch fires, $i_r$ ramps up linearly at $V_{dc}/(2L_r)$ |
| 3.4 | 18 | ARCP Equivalent Circuit — State 3 | Equivalent circuit | $V_{dc}, L_r, C_1, C_2, V_{C1}, V_{C2}, i_r, i_\text{load}$ | (3-7) $\dot{V}_{dc}=0$ · (3-8) $\dot{V}_{C1}=-\dot{V}_{C2}$ · (3-9) $V_{dc}/2+L_r\dot{i}_r-V_{C1}=0$ · (3-10) $\dot{V}_{C1}=(i_\text{load}-i_r)/(C_1+C_2)$ · (3-11) $\dot{i}_r=(V_{C1}-V_{dc}/2)/L_r$ | **Key figure.** Resonant swing state: $L_r$–$C_r$ oscillation drives $V_f$ from $0\to V_{dc}$ |
| 3.5 | 20 | ARCP Equivalent Circuit — State 4 | Equivalent circuit | $V_{dc}, L_r, C_2, V_{C1}, i_r, i_\text{load}$ | (3-12) $\dot{V}_{C1}=0$ · (3-13) $\dot{i}_r=-V_{dc}/(2L_r)$ | Post-clamp: $V_f=V_{dc}$, upper diode clamps, $i_r$ ramps back down |
| 3.6 | 20 | ARCP Equivalent Circuit — State 5 | Equivalent circuit | $V_{dc}, C_2, V_{C1}, i_\text{load}$ | — | Final idle state: upper switch turns on at ZVS, auxiliary circuit off |
| 3.7 | 22 | ARCP Commutation Low-to-High from Diode | Simulated waveforms | $V_{C1}$ (V), $i_r$ (A), $i_\text{load}, i_\text{boost}$ | — | $V_{C1}$ and $i_r$ vs. time ($9.75$–$9.80\,\mu$s); 5 states labeled on plot |
| 3.8 | 24 | ARCP Commutation Low-to-High from Switch (Low $I$) | Simulated waveforms | $V_{C1}$ (V), $i_r$ (A), $i_\text{load}$ | — | Same axes as Fig. 3.7 for switch commutation at low load |
| 3.9 | 25 | ARCP Equivalent Circuit — State 6 (High $I$) | Equivalent circuit | $V_{dc}, C_1, C_2, V_{C1}, i_\text{load}$ | (3-16) $\dot{V}_{C1}=i_\text{load}/(C_1+C_2)$ · (3-17) $\dot{i}_r=0$ | High current case: load current alone charges $C_r$, auxiliary circuit inactive |
| 3.10 | 26 | ARCP Commutation Low-to-High from Switch (High $I$) | Simulated waveforms | $V_{C1}$ (V), $i_r$ (A), $i_\text{load}$ | — | Waveforms confirming natural commutation at high load — $i_r$ stays zero |
| 4.1 | 28 | H-Bridge Using Two ARCP Phase Legs | System topology | $V_{DC}, C_{dc}, L_{r1}, L_{r2}, C_r, i_{r1}, i_{r2}, V_{C1}, V_{C2}, i_\text{load}, v_\text{load}$ | — | Full H-bridge: two ARCP legs sharing DC bus; introduces notation for dual auxiliary circuits |
| 4.2 | 29 | $v_\text{load}$ vs. Time and PWM Waveforms | Control waveforms | $V_\text{load}$, PWM carrier, reference sinusoid | — | 3 waveforms: triangle carrier, 1 kHz reference, resulting $v_\text{load}$ PWM pattern |
| 4.3 | 30 | Energy Losses: Hard-Switched vs. ARCP | Comparative loss plots | Losses (J), time ($\times 10^{-3}$ s) | — | Side-by-side accumulated energy loss over one cycle — key efficiency comparison figure |
| 4.4 | 31 | H-Bridge $V_{C1}$ and $i_{r1}$ vs. Time | Simulated waveforms | $V_{C1}$ (V), $i_{r1}$ (A) | — | Leg 1 waveforms over 1 ms; shows per-commutation current pulses |
| 4.5 | 32 | H-Bridge $V_{C2}$ and $i_{r2}$ vs. Time | Simulated waveforms | $V_{C2}$ (V), $i_{r2}$ (A) | — | Leg 2 waveforms — complements Fig. 4.4 |
| 4.6 | 33 | H-Bridge $i_\text{load}$ and $v_\text{load}$ vs. Time | Load waveforms | $i_\text{load}$ (A $\pm20$), $v_\text{load}$ (V $\pm400$) | — | Full-cycle RL load current (sinusoidal) and switched $v_\text{load}$ confirming motor-drive operation |

---

## Paper 3: Resonant Motor Drive — Algorithms and Controls (ITEC / NASA Glenn)
**Belovich, Carbone, Granger, Kowalewski**

| Fig | Page | Caption | Type | State Variables | Equations / Parameters | Description |
|-----|------|---------|------|----------------|------------------------|-------------|
| 1 | 1 | Electrical Diagram of ARCP Inverter (One Phase Leg) | Circuit topology | PWM inputs, $L_r=0.33\,\mu$H, $C_r=1\,$nF, $V_{DC}=500\,$V | $f_s=100\,$kHz | FPGA-driven implementation: auxiliary MOSFETs $A_1/A_2$, main switches, snubber caps, output filter |
| 2 | 2 | ARCP Waveforms — A-Type Commutation (positive and negative $i_\text{load}$) | Control + resonant waveforms | $V_\text{res}, i_\text{load}$, PWM\_J, $Q_1, Q_2$ | — | 4 waveform sets (2 current directions × 2 polarities); shows $T_\text{ramp}$ and $T_\text{res}$ intervals |
| 3 | 2 | ARCP Waveforms — B-Type Capacitive Commutation | Control waveforms | $V_\text{res}, i_\text{load}$, PWM | — | B-type when load current crosses zero; capacitor charges passively |
| 4 | 2 | ARCP Waveforms — B-Type Resonant Commutation | Resonant waveforms | $V_\text{res}, i_\text{load}$, resonant oscillations | — | B-type resonant case; $i_r$ oscillation needed for $V_f$ swing at low $i_\text{load}$ |
| 5 | 3 | FTOL Simulation Results | Simulation plots | $I_\text{load}$ (A), time (s $\times10^{-3}$) | **Table I params:** $f=680\,$Hz, $f_s=100\,$kHz, $V_{dc}=500\,$V, $L_r=0.33\,\mu$H, $C_r=1\,$nF, $T_\text{ramp}=63.4\,$ns, $T_\text{res}=30.7\,$ns | 3 plots: full cycle $i_\text{load}$, A-type commutation detail, B-type commutation detail |
| 6 | 4 | FTCL Simulation Results | Simulation plots | Current (A), voltage (V), time ($\times10^{-3}$ s) | **Table II timing equations:** A-type: $T_\text{ramp}=2L_r I_\text{load}/V_{dc}$, $T_\text{res}=\pi\sqrt{L_rC_r}$; B-type cap: $T_0=0$, $T_\text{res}=\sqrt{L_rC_r}$; B-type res: $T_\text{res}=\frac{2}{\omega_r}\tan^{-1}\!\left(\frac{V_{dc}/2}{I_\text{load}Z_r}\right)$ | Closed-loop timing vs. FTOL; 3 plots same structure as Fig. 5 |
| 7 | 4 | A-Type Commutation — Experimental (Analog FTCL) | Oscilloscope trace | Voltage, current, switching transitions | — | Real hardware validation of resonant waveform; timing markers for $T_\text{ramp}$, $T_\text{res}$ intervals |
| 8 | 4 | Top-Level State Machine | State machine / flowchart | PWM\_latch, PWM\_rise\_latch, PWM\_fall\_latch, $I_{th}$ | — | 4-state FPGA machine: IDLE → TYPE A / TYPE B CAPACITIVE / TYPE B RESONANT based on $i_\text{load}$ vs. $I_{th}$ |
| 9 | 5 | Detailed State Machine — A-Type and B-Type Resonant | State machine | Counter values, $T_\text{RAMP\_1}$, $T_\text{RES}$, $T_\text{RAMP\_2}$ | — | A-type (red): 3 timed states; B-type resonant (green): 2 timed states with counter transitions |
| 10 | 5 | Detailed State Machine — B-Type Capacitive | State machine | $T_\text{RES}$, $T_\text{RAMP\_2}$, counter values | — | Simplified 2-state machine for capacitive commutation path |

---

## Master Equation Reference

| Equation | Paper | Content |
|----------|-------|---------|
| $\omega_r = 1/\sqrt{L_rC_r}$, $Z_r=\sqrt{L_r/C_r}$ | 1 | Resonant frequency and impedance — governs all commutation timing |
| $I_\text{peak} = I_L + i_\text{boost} + V_{dc}/(2Z_r)$ | 1, (Fig. 7) | Peak auxiliary current during diode commutation |
| $T_c = 2L_r(2I_L+i_\text{boost})/V_{dc} + \pi\sqrt{L_rC_r}$ | 1, (Fig. 8) | Total commutation time for switch at low current |
| $I_{th} = 2C_r V_{dc}/T_\text{max}$ | 1, (Fig. 9) | Load current threshold above which auxiliary boost is unnecessary |
| $E_{Q,\text{on}} = V_{dc}\,i_\text{load}\,t_r$ | 2, (Fig. 2.3) | Hard-switch turn-on energy loss |
| $E_{Q,\text{off}} = V_{dc}\,i_\text{load}\,t_c$ | 2, (Fig. 2.4) | Hard-switch turn-off energy loss |
| $\dot{i}_r = V_{dc}/(2L_r)$ | 2, (Fig. 3.2–3.3) | Auxiliary current ramp rate during boost phase |
| $\dot{V}_{C1} = (i_\text{load}-i_r)/(C_1+C_2)$ | 2, (Fig. 3.4, Eq. 3-10) | Pole voltage rate during resonant swing |
| $\dot{i}_r = (V_{C1}-V_{dc}/2)/L_r$ | 2, (Fig. 3.4, Eq. 3-11) | Auxiliary current rate during resonant swing |
| $T_\text{ramp} = 2L_r I_\text{load}/V_{dc}$ | 3, (Fig. 6, Table II) | A-type boost ramp duration (load-current dependent) |
| $T_\text{res} = \pi\sqrt{L_rC_r}$ | 3, (Fig. 6, Table II) | A-type resonant half-swing duration |
| $T_\text{res,B} = \frac{2}{\omega_r}\tan^{-1}\!\left(\frac{V_{dc}/2}{I_\text{load}Z_r}\right)$ | 3, (Fig. 6, Table II) | B-type resonant commutation time |

---

## Figure Type Summary

| Type | Count | Key Figures |
|------|-------|-------------|
| Circuit / system topology | 7 | P1:Fig5, P2:Fig3.1, P3:Fig1 |
| Equivalent circuit (per state) | 6 | P2:Fig3.2–3.6, 3.9 |
| Switching sequence diagrams | 3 | P1:Fig7–9 |
| Simulated waveforms | 10 | P1:Fig10–11, P2:Fig3.7–3.10, 4.4–4.6 |
| Loss / performance plots | 2 | P2:Fig2.2, 4.3 |
| Control / PWM waveforms | 5 | P2:Fig4.2, P3:Fig2–4 |
| State machine diagrams | 3 | P3:Fig8–10 |
| Experimental oscilloscope | 1 | P3:Fig7 |
