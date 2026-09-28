# Experimental Skills {#p20}

:::stats
Typical questions | 0–2 direct per shift
Difficulty | Easy
Priority | High (predictable)
NCERT | Class 11 & 12 Physics Lab Manuals
Study time | ~6 hours
:::

## Concept summary

The official syllabus lists **18 experiments** [NTA-SYL]. Questions test three things: **(1)** reading an instrument correctly (least count, zero error), **(2)** the formula and graph behind an experiment, and **(3)** which measurement contributes the most error. Learn each experiment as a one-line card: *aim → formula → graph → main error source*.

## Measuring instruments

:::formula Vernier callipers & screw gauge
**Vernier:** LC $= 1\ \text{MSD} - 1\ \text{VSD}$. If $N$ VSD $= (N-1)$ MSD, then LC $= \dfrac{\text{MSD}}{N}$.
Reading $= \text{MSR} + (\text{coinciding VSD})\times\text{LC}$. Zero error: vernier zero to the **right** of the main zero is positive; to the **left** is negative. **Corrected = observed − zero error.**
Parts: outer jaws (external diameter), inner jaws (internal diameter), depth strip (depth).

**Screw gauge:** LC $= \dfrac{\text{pitch}}{\text{no. of circular divisions}}$. Reading $= \text{MSR} + \text{CSR}\times\text{LC}$. **Backlash error** comes from play in the screw. Avoid it by always turning in one direction.
:::

## The 18 syllabus experiments on one page

| # | Experiment | Key formula / relation | Graph | Main error source / tip |
|---|---|---|---|---|
| 1 | Vernier callipers: internal/external diameter, depth | LC, zero error | — | zero-error sign |
| 2 | Screw gauge: thickness/diameter of sheet/wire | LC $=$ pitch/divisions | — | backlash, zero error |
| 3 | Simple pendulum: dissipation of energy | $A^2 \propto e^{-bt/m}$; $T = 2\pi\sqrt{L/g}$ | $A^2$ vs $t$: exponential decay; $L$ vs $T^2$: straight line, slope $g/4\pi^2$ | amplitude reading, air drag |
| 4 | Metre scale: mass by principle of moments | $m_1l_1 = m_2l_2$ | — | knife-edge position |
| 5 | Young's modulus of a wire (Searle's) | $Y = \dfrac{MgL}{\pi r^2\,\Delta L}$ | load vs extension: line through origin | **radius** ($r^2$) and $\Delta L$ (smallest quantities) |
| 6 | Surface tension by capillary rise; effect of detergent | $T = \dfrac{rh\rho g}{2\cos\theta}$ | — | radius of bore; detergent lowers $h$ |
| 7 | Viscosity by terminal velocity | $\eta = \dfrac{2r^2(\rho - \sigma)g}{9v_t}$ | — | timing only after terminal speed is reached; wall effects |
| 8 | Speed of sound, resonance tube | $v = 2f(L_2 - L_1)$; $e = 0.3d$ | — | end correction cancels in $L_2 - L_1$ |
| 9 | Specific heat of a solid/liquid (mixtures) | $m_sc_s(T_s - T) = (m_wc_w + W)(T - T_w)$ | — | heat loss to the surroundings |
| 10 | Resistivity using a metre bridge | $\dfrac RS = \dfrac{l}{100 - l}$, $\rho = \dfrac{\pi r^2R}{L}$ | — | end errors (interchange R and S and average); balance near 50 cm |
| 11 | Resistance by Ohm's law | $R = V/I$ | $V$–$I$ straight line, slope $R$ | heating of the wire |
| 12 | Galvanometer resistance & figure of merit (half deflection) | $G = \dfrac{RS}{R - S}$; $k = \dfrac{E}{(R + G)\theta}$ | — | use $R \gg G$ |
| 13 | Focal length by parallax: convex mirror, concave mirror, convex lens | $\dfrac1f = \dfrac1v + \dfrac1u$ (mirror), $\dfrac1v - \dfrac1u$ (lens) | $u$–$v$ hyperbola; $1/u$ vs $1/v$ line with intercepts $1/f$ | parallax removal; for a lens, $u = v = 2f$ point |
| 14 | $i$–$\delta$ curve for a prism | $n = \dfrac{\sin\frac{A+\delta_m}{2}}{\sin\frac A2}$ | U-shaped, minimum at $\delta_m$ | pin alignment |
| 15 | Refractive index of a slab with a travelling microscope | $n = \dfrac{\text{real}}{\text{apparent}} = \dfrac{R_3 - R_1}{R_3 - R_2}$ | — | focusing |
| 16 | p–n junction diode, forward & reverse characteristics | knee ≈ 0.7 V (Si) | exponential forward curve; tiny reverse current | use mA in forward, μA in reverse |
| 17 | Zener diode characteristics, breakdown voltage | $V_Z$ at the sharp rise in reverse current | vertical reverse breakdown | series resistor to limit current |
| 18 | Identify diode, LED, resistor, capacitor (multimeter) | — | — | see the table below |

:::important Component identification (Experiment 18)
| Component | Multimeter behaviour |
|---|---|
| Resistor | same resistance in both directions |
| Diode | low resistance one way, very high the other way |
| LED | conducts one way **and glows** |
| Capacitor | momentary deflection (charging), then very high resistance |
:::

:::pyq Recurring structures
1. Vernier/screw-gauge readings with zero error (often combined with the error in a derived quantity).
2. "Which measurement has the largest percentage error?" (usually the one raised to a power or the smallest reading).
3. Metre-bridge null points, interchange; galvanometer half-deflection.
4. Resonance tube: $v$ and end correction from two resonance lengths.
5. Pendulum graphs ($L$–$T^2$ slope; $A^2$–$t$ decay).
6. Travelling microscope readings → refractive index.
:::

:::trap Mistake alerts
- Screw gauge: "the reference line is below/above zero" statements are orientation-dependent. Convert them into a **signed reading with the jaws closed** first.
- Metre bridge: $l$ is measured from the end connected to the **unknown** in its gap, or whichever the question says. Read carefully.
- End correction of the resonance tube is $0.3\times$ **diameter** ($0.6\times$ radius).
:::

## Practice questions

@@SET P20 · Practice

@@Q P20-01 | E | 0.5 | Vernier least count | Speed
In a Vernier calliper, 20 VSD coincide with 19 MSD, and 1 MSD = 1 mm. The least count is:
(A) 0.1 mm
(B) 0.05 mm
(C) 0.02 mm
(D) 0.5 mm
@ans B
@sol LC $= \text{MSD}/N = 1/20 = 0.05$ mm.
@short —
@trap —
@@END

@@Q P20-02 | M | 1.5 | Screw gauge, negative zero error | JEE
A screw gauge has pitch 1 mm and 100 circular divisions. With the studs closed it reads −0.03 mm. Measuring a wire, the main-scale reading is 4 mm and the circular-scale reading is 52. The corrected diameter is:
(A) 4.49 mm
(B) 4.52 mm
(C) 4.55 mm
(D) 4.82 mm
@ans C
@sol LC $= 0.01$ mm; observed $= 4 + 0.52 = 4.52$ mm; corrected $= 4.52 - (-0.03) = 4.55$ mm.
@short Subtracting a negative error means adding.
@trap Subtracting 0.03 gives 4.49.
@@END

@@Q P20-03 | M | 1.5 | Half-deflection method | Calc
In the half-deflection method, the galvanometer shows deflection $\theta$ with 5000 Ω in series. Connecting a 50 Ω shunt across the galvanometer reduces the deflection to $\theta/2$. The galvanometer resistance is about:
(A) 50 Ω
(B) 50.5 Ω
(C) 49.5 Ω
(D) 100 Ω
@ans B
@sol $G = \dfrac{RS}{R - S} = \dfrac{5000\times50}{4950} \approx 50.5\ \Omega$.
@short When $R \gg G$, $G \approx S$.
@trap —
@@END

@@Q P20-04 | E | 0.5 | Pendulum energy dissipation graph | Concept
In the simple-pendulum energy-dissipation experiment, the graph of (amplitude)² against time is:
(A) a straight line with positive slope
(B) an exponentially decaying curve
(C) a parabola
(D) constant
@ans B
@sol Damping makes the energy (∝ $A^2$) decay exponentially: $A^2 \propto e^{-bt/m}$.
@short —
@trap —
@@END

@@Q P20-05 | E | 1 | Surface tension from capillary rise | Calc
Water rises 3 cm in a capillary of radius 0.5 mm (contact angle 0°, $\rho = 1000$, $g = 10$). The surface tension is:
(A) 0.075 N/m
(B) 0.15 N/m
(C) 0.0375 N/m
(D) 0.75 N/m
@ans A
@sol $T = \dfrac{rh\rho g}{2} = \dfrac{5\times10^{-4}\times0.03\times1000\times10}{2} = 0.075$ N/m.
@short —
@trap Forgetting the 2.
@@END

@@Q P20-06 | M | 1 | Travelling microscope | Basic
Travelling-microscope readings: mark on paper (no slab) 10.20 mm, mark seen through the slab 13.20 mm, top surface of the slab 19.20 mm. The refractive index of the slab is:
(A) 1.33
(B) 1.50
(C) 1.60
(D) 2.00
@ans B
@sol Real thickness $= 19.20 - 10.20 = 9.00$ mm. Apparent $= 19.20 - 13.20 = 6.00$ mm. $n = 9/6 = 1.5$.
@short —
@trap Using $13.20 - 10.20$ as the apparent thickness (that's the *shift*).
@@END

@@Q P20-07 | M | 1.5 | Method of mixtures | Calc
A 0.1 kg metal piece at 100 °C is dropped into 0.2 kg of water at 20 °C (negligible calorimeter heat capacity), and the final temperature is 24 °C. With $c_w = 4200\ \text{J kg}^{-1}\text{K}^{-1}$, the metal's specific heat is about:
(A) 221 J/kg K
(B) 442 J/kg K
(C) 884 J/kg K
(D) 336 J/kg K
@ans B
@sol $0.1\,c(76) = 0.2(4200)(4) = 3360 \Rightarrow c = 3360/7.6 \approx 442$ J/kg K.
@short —
@trap Using $100 - 20$ instead of $100 - 24$.
@@END

@@Q P20-08 | E | 0.5 | End correction | Speed
The end correction of a resonance tube of internal diameter 5 cm is about:
(A) 0.6 cm
(B) 1.5 cm
(C) 3.0 cm
(D) 5.0 cm
@ans B
@sol $e = 0.3d = 1.5$ cm.
@short —
@trap Using $0.6d$.
@@END

@@Q P20-09 | E | 0.5 | Identifying a capacitor | Concept
Tested with a multimeter, a component shows a momentary deflection that then falls to (almost) zero current. The component is a:
(A) resistor
(B) diode
(C) capacitor
(D) LED
@ans C
@sol The capacitor charges briefly, then blocks DC.
@short —
@trap —
@@END

@@Q P20-10 | E | 0.75 | u = v point of a convex lens | NV
In the $u$–$v$ experiment with a convex lens, the object and image distances are equal at 40 cm. Find the focal length (in cm).
@ans 20
@sol $|u| = |v| = 2f \Rightarrow f = 20$ cm.
@short —
@trap —
@@END

@@SET P20 · Chapter Test

@@Q P20-T1 | E | 0.75 | Largest error in Searle's experiment | Concept
In Searle's experiment for Young's modulus, the largest contribution to the percentage error usually comes from measuring:
(A) the length $L$ of the wire
(B) the load $M$
(C) the radius $r$ of the wire
(D) $g$
@ans C
@sol $r$ is small and appears squared in $Y = MgL/(\pi r^2\Delta L)$, so its percentage error is doubled. (The extension $\Delta L$ is also critical, which is why a micrometer is used.)
@short Small quantity × high power ⇒ largest error.
@trap Choosing $L$ (large, easy to measure precisely).
@@END

@@Q P20-T2 | E | 0.5 | Screw gauge least count | Speed
A screw gauge has pitch 0.5 mm and 50 circular divisions. Its least count is:
(A) 0.1 mm
(B) 0.01 mm
(C) 0.001 mm
(D) 0.05 mm
@ans B
@sol $0.5/50 = 0.01$ mm.
@short —
@trap —
@@END

@@Q P20-T3 | E | 0.5 | Terminal velocity scaling | Speed
In the viscosity experiment, the radius of the ball is doubled (same material). Its terminal velocity becomes:
(A) 2 times
(B) 4 times
(C) 8 times
(D) half
@ans B
@sol $v_t \propto r^2$.
@short —
@trap —
@@END

@@Q P20-T4 | E | 0.5 | Least count in micrometres | NV
Find the least count (in μm) of a screw gauge with pitch 1 mm and 200 circular divisions.
@ans 5
@sol $1\ \text{mm}/200 = 0.005$ mm $= 5\ \mu$m.
@short —
@trap —
@@END

## Answers & Solutions {#p20-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Experimental Skills
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
