# Electronic Devices {#p19}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy
Priority | Must-do (easy marks)
NCERT | Class 12 · Ch 14
Study time | ~5 hours
:::

## Concept summary

- In **semiconductors** (Si, Ge) a small band gap lets thermal energy create electron–hole pairs. **Doping** controls conductivity: pentavalent donors give **n-type**, trivalent acceptors give **p-type**.
- A **p–n junction** forms a depletion layer with a barrier potential. It conducts easily in **forward bias** and hardly at all in **reverse bias**, which makes it a rectifier.
- **Special diodes:** Zener (voltage regulator in reverse breakdown), LED (light from recombination, forward bias), photodiode (light-controlled reverse current), solar cell (generates emf with no bias).
- **Logic gates** process binary signals. NAND and NOR are **universal** gates.

:::warning Syllabus note
**Transistors** (BJT action, amplifiers, oscillators) are **not** in the 2024–2026 syllabus text. Unit 19 covers semiconductors, diode I–V characteristics, rectifiers, LED, photodiode, solar cell, Zener diode and logic gates (OR, AND, NOT, NAND, NOR) [NTA-SYL].
:::

## Formulas & facts

:::formula Semiconductors
| Type | Dopant (group) | Majority carriers | Examples |
|---|---|---|---|
| Intrinsic | none | $n_e = n_h = n_i$ | pure Si, Ge |
| n-type | pentavalent (15) | electrons | P, As, Sb in Si |
| p-type | trivalent (13) | holes | B, Al, Ga, In in Si |

**Mass-action law:** $n_en_h = n_i^2$. A doped semiconductor is still electrically **neutral**.
Band gaps: conductor ≈ 0 (bands overlap), Si ≈ 1.1 eV, Ge ≈ 0.7 eV, insulator > 3 eV. At 0 K an intrinsic semiconductor behaves like an insulator. Conductivity **rises** with temperature (resistance falls).
:::

:::formula p–n junction & diodes
Barrier potential: Si ≈ 0.7 V, Ge ≈ 0.3 V. **Forward bias** narrows the depletion layer. **Reverse bias** widens it, leaving a tiny reverse saturation current (minority carriers) until breakdown.
| Device | Bias | Principle / use |
|---|---|---|
| Rectifier diode | forward conducts | half-wave: output ripple at $f$; full-wave: at $2f$ |
| Zener diode | **reverse** (breakdown) | constant $V_Z$ across the load → voltage regulator |
| LED | forward | recombination emits photons, $\lambda = \dfrac{hc}{E_g}$ |
| Photodiode | reverse | light raises the reverse current (light detector) |
| Solar cell | none (self-generating) | I–V curve in the 4th quadrant; $V_{oc}$, $I_{sc}$ |

**Zener regulator:** $I_R = \dfrac{V_{in} - V_Z}{R_s}$, $I_L = \dfrac{V_Z}{R_L}$, $I_Z = I_R - I_L$.
**Diode in a circuit:** ideal = switch; real Si = 0.7 V drop when conducting.
:::

:::formula Logic gates
| A | B | AND | OR | NAND | NOR | XOR |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

NOT: $\bar A$. **De Morgan:** $\overline{A + B} = \bar A\cdot\bar B$ and $\overline{A\cdot B} = \bar A + \bar B$.
With NAND gates: NOT = 1 gate (inputs tied), AND = 2 gates, OR = 3 gates. With NOR gates: NOT = 1, OR = 2, AND = 3.
:::

@@GRAPH diode-iv

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Gate combinations:** identify the output or the equivalent gate of a 2–3 gate circuit (very frequent).
2. **Zener regulator currents.**
3. **Diode circuits:** which diode conducts; current with ideal or 0.7 V diodes.
4. **Rectifier** output frequency and waveform.
5. **Carrier concentration** with $n_en_h = n_i^2$.
6. **LED colour ↔ band gap**; photodiode and solar-cell bias facts.
:::

## Shortcuts

:::shortcut Boolean algebra over truth tables
For gate puzzles, write the Boolean expression and simplify with De Morgan. It's usually faster than a 4-row table and less error-prone.
Example: NOR followed by NOT is $\overline{\overline{A + B}} = A + B$ (OR).
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Gate identification | E | 45 s |
| Zener currents | E | 1 min |
| Diode circuit current | E–M | 1.5 min |
| Doping / carrier concentration | E | 45 s |
| Special diode facts | E | 30 s |

## Common mistakes

:::trap Mistake alerts
- The Zener is used in **reverse** bias, the LED in **forward** bias, the photodiode in **reverse** bias.
- n-type doesn't mean negatively charged. The material stays neutral.
- Full-wave rectifier ripple frequency is **2f** (100 Hz for 50 Hz mains).
- Forgetting the 0.7 V drop when the question says "silicon diode".
:::

## Practice questions

@@SET P19 · Practice

@@Q P19-01 | E | 0.5 | Type of doping | Speed
Silicon doped with arsenic is:
(A) p-type, with holes as majority carriers
(B) n-type, with electrons as majority carriers
(C) intrinsic
(D) an insulator
@ans B
@sol As is pentavalent (group 15), so it donates electrons.
@short —
@trap —
@@END

@@Q P19-02 | M | 1 | Mass-action law | Calc
An intrinsic semiconductor has $n_i = 1.5\times10^{16}\ \text{m}^{-3}$. After doping, the electron concentration is $4.5\times10^{22}\ \text{m}^{-3}$. The hole concentration is:
(A) $5\times10^{9}\ \text{m}^{-3}$
(B) $3\times10^{6}\ \text{m}^{-3}$
(C) $1.5\times10^{16}\ \text{m}^{-3}$
(D) $4.5\times10^{22}\ \text{m}^{-3}$
@ans A
@sol $n_h = \dfrac{n_i^2}{n_e} = \dfrac{2.25\times10^{32}}{4.5\times10^{22}} = 5\times10^{9}\ \text{m}^{-3}$.
@short —
@trap Assuming $n_h = n_i$.
@@END

@@Q P19-03 | E | 0.5 | Rectifier ripple | Speed
The ripple frequency at the output of a full-wave rectifier fed from 50 Hz mains is:
(A) 25 Hz
(B) 50 Hz
(C) 100 Hz
(D) 200 Hz
@ans C
@sol Both half-cycles are rectified, so the output repeats at $2f$.
@short —
@trap Using the half-wave value.
@@END

@@Q P19-04 | M | 1.5 | Zener regulator | NV
A Zener diode with $V_Z = 5$ V is connected, through a 500 Ω series resistor, to a 15 V supply. The load across the Zener is 1 kΩ. Find the Zener current (in mA).
@ans 15
@sol $I_R = (15 - 5)/500 = 20$ mA; $I_L = 5/1000 = 5$ mA; $I_Z = 15$ mA.
@short —
@trap Forgetting to subtract the load current.
@@END

@@Q P19-05 | E | 0.75 | LED wavelength from band gap | Basic
An LED has a band gap of 2.0 eV. The wavelength of the light it emits is about:
(A) 400 nm
(B) 500 nm
(C) 620 nm
(D) 900 nm
@ans C
@sol $\lambda = 1240/2.0 = 620$ nm (red–orange).
@short —
@trap —
@@END

@@Q P19-06 | E | 0.5 | NAND as NOT | Concept
A NAND gate with both inputs joined together acts as:
(A) AND
(B) OR
(C) NOT
(D) NOR
@ans C
@sol $\overline{A\cdot A} = \bar A$.
@short —
@trap —
@@END

@@Q P19-07 | E | 0.75 | Gate combination | Concept
The output of a NOR gate is fed into a NOT gate. The combination is equivalent to:
(A) AND
(B) OR
(C) NAND
(D) XOR
@ans B
@sol $\overline{\overline{A + B}} = A + B$.
@short —
@trap —
@@END

@@Q P19-08 | E | 1 | Silicon diode current | Basic
A silicon diode (0.7 V drop when conducting) is forward biased in series with a 1 kΩ resistor across a 5 V battery. The current is:
(A) 5.0 mA
(B) 4.3 mA
(C) 5.7 mA
(D) 0.7 mA
@ans B
@sol $I = (5 - 0.7)/1000 = 4.3$ mA.
@short —
@trap Ignoring the diode drop.
@@END

@@Q P19-09 | E | 0.5 | Photodiode bias | Concept
A photodiode is normally operated in:
(A) forward bias
(B) reverse bias
(C) zero bias only
(D) breakdown
@ans B
@sol In reverse bias the small current is very sensitive to light-generated carriers, so the change is easy to measure.
@short —
@trap Confusing it with the LED.
@@END

@@SET P19 · Chapter Test

@@Q P19-T1 | E | 0.5 | Band gaps | Speed
The correct order of band gaps is:
(A) conductor > semiconductor > insulator
(B) insulator > semiconductor > conductor
(C) semiconductor > insulator > conductor
(D) all equal
@ans B
@sol Insulator (> 3 eV) > semiconductor (~1 eV) > conductor (overlapping bands, ~0).
@short —
@trap —
@@END

@@Q P19-T2 | E | 0.5 | Depletion width | Speed
In reverse bias, the depletion layer of a p–n junction:
(A) narrows
(B) widens
(C) disappears
(D) is unchanged
@ans B
@sol The applied field adds to the barrier field, pulling carriers away from the junction.
@short —
@trap —
@@END

@@Q P19-T3 | E | 0.5 | Fourth-quadrant device | Concept
A device whose working I–V characteristic lies in the fourth quadrant is a:
(A) Zener diode
(B) LED
(C) solar cell
(D) rectifier diode
@ans C
@sol A solar cell delivers power: current flows opposite to the voltage it develops across itself.
@short —
@trap —
@@END

@@Q P19-T4 | E | 0.5 | Universal gates | NV
What is the minimum number of NAND gates needed to realise an OR gate?
@ans 3
@sol $A + B = \overline{\bar A\cdot\bar B}$: two NANDs as inverters for $\bar A$ and $\bar B$, then one NAND.
@short —
@trap —
@@END

@@Q P19-T5 | E | 0.5 | Semiconductor at 0 K | Speed
At 0 K, a pure semiconductor behaves as:
(A) a perfect conductor
(B) an insulator
(C) a superconductor
(D) an n-type semiconductor
@ans B
@sol No thermal energy is available to excite electrons across the gap.
@short —
@trap —
@@END

## Answers & Solutions {#p19-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Electronic Devices
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
