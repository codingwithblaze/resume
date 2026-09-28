# Current Electricity {#p12}

:::stats
Typical questions | 2–3 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 12 · Ch 3
Study time | ~12 hours
:::

## Concept summary

- **Current** is the rate of flow of charge. In metals, free electrons **drift** slowly ($\sim10^{-4}$ m/s) against the field, while the field itself sets up almost instantly.
- **Ohm's law** $V = IR$ holds for ohmic conductors at constant temperature. Diodes and electrolytes are non-ohmic.
- **Resistance** depends on geometry and material: $R = \rho L/A$. Resistivity rises with temperature for metals and falls for semiconductors.
- **Kirchhoff's laws** (junction = charge conservation, loop = energy conservation) solve every circuit. The Wheatstone bridge and metre bridge are special cases.

:::warning Syllabus note
The 2024–2026 syllabus text for this unit ends at **"Kirchhoff's laws and their applications. Wheatstone bridge. Metre Bridge."** The **potentiometer** and **colour code** are not listed. Keep them to a quick read only [NTA-SYL].
:::

## Formulas

:::formula Microscopic view
$$I = \frac{dq}{dt} = neAv_d \qquad v_d = \frac{eE\tau}{m} \qquad \mu = \frac{v_d}{E} = \frac{e\tau}{m} \qquad J = \frac IA = \sigma E \qquad \rho = \frac{m}{ne^2\tau}$$
:::

:::formula Resistance
$$R = \frac{\rho L}{A} \qquad R_T = R_0(1 + \alpha\,\Delta T) \qquad \text{Series: } R = \sum R_i \qquad \text{Parallel: } \frac1R = \sum\frac1{R_i}$$
- **Stretching a wire** (volume constant) to $n$ times its length: $R' = n^2R$. If its radius becomes $r/n$: $R' = n^4R$.
- $n$ equal resistors: $R_{series}/R_{parallel} = n^2$.
:::

:::formula Cells
$$V_{terminal} = \varepsilon - Ir \ \text{(discharging)} \qquad V = \varepsilon + Ir \ \text{(charging)} \qquad I = \frac{\varepsilon}{R + r}$$
- $n$ identical cells in series: $n\varepsilon$, $nr$. In parallel: $\varepsilon$, $r/n$. Mixed ($m$ rows of $n$ cells): $I = \dfrac{n\varepsilon}{R + nr/m}$, maximum when $R = nr/m$.
- Two different cells in parallel: $\varepsilon_{eq} = \dfrac{\varepsilon_1/r_1 + \varepsilon_2/r_2}{1/r_1 + 1/r_2}$, $r_{eq} = \dfrac{r_1r_2}{r_1 + r_2}$.
- **Maximum power transfer:** $R = r$ gives $P_{max} = \dfrac{\varepsilon^2}{4r}$ (efficiency 50%).
:::

:::formula Power & bridges
$$P = VI = I^2R = \frac{V^2}{R} \qquad \text{rated bulb: } R = \frac{V_{rated}^2}{P_{rated}}$$
**Wheatstone bridge balance:** $\dfrac PQ = \dfrac RS$ (no current through the galvanometer; remove that arm).
**Metre bridge:** $\dfrac{R}{S} = \dfrac{l}{100 - l}$ ($l$ in cm from the end next to $R$). Most sensitive near the middle.
- Bulbs in **series**: the lower-wattage bulb (higher $R$) glows brighter. In **parallel**: the higher-wattage bulb glows brighter.
- Heater at a lower voltage: $P' = P(V'/V)^2$.
:::

@@GRAPH vi-ohmic

## Kirchhoff's laws in practice

1. Mark currents in each branch with arbitrary directions.
2. **Junction rule:** $\sum I_{in} = \sum I_{out}$.
3. **Loop rule:** going around a loop, $\sum\Delta V = 0$. Across a resistor in the direction of current: $-IR$. Across a cell from − to +: $+\varepsilon$.
4. Solve. A negative current just means the real direction is opposite to the one you assumed.

:::shortcut Nodal (potential) method
Set one node at 0 V. Write the other node potentials as unknowns, and use $\sum\dfrac{V - V_j}{R_j} = 0$ at each node. This usually needs fewer equations than loops.
**Time saved:** 1–2 minutes on two-loop circuits.
:::

:::shortcut Symmetry & balanced bridges
If a network has a symmetry plane, points on it are at equal potential: join them or remove the resistors between them. Before solving, check $P/Q = R/S$.
:::

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Equivalent resistance** of networks: bridges, symmetric cubes/triangles, infinite ladders.
2. **Cells:** terminal voltage, internal resistance, combinations, maximum power.
3. **Kirchhoff two-loop circuits:** current in a branch.
4. **Drift velocity / current density / mobility** numericals.
5. **Stretched wire** and temperature dependence of resistance.
6. **Metre-bridge balance** and interchange of resistances (part of the experimental skills).
7. **Rated bulbs** in series/parallel: brightness and power.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| $R$ from geometry / stretching | E | 45 s |
| Series–parallel networks | E | 1 min |
| Cells, terminal voltage, max power | E | 1 min |
| Kirchhoff two loops | M | 2 min |
| Bridge (balanced/unbalanced) | M | 1.5 min |
| Infinite ladder / cube networks | M–H | 2.5 min |

## Common mistakes

:::trap Mistake alerts
- Forgetting the internal resistance when finding the current.
- Using $P = I^2R$ for bulbs in parallel when $V$ is the common quantity. Use $V^2/R$.
- In the metre bridge, measuring $l$ from the wrong end.
- Assuming drift speed equals the speed at which the signal travels.
- Sign errors in the loop rule when you cross a cell from + to −.
:::

## Practice questions

@@SET P12 · Practice

@@Q P12-01 | M | 1.5 | Drift velocity | Calc
A copper wire of cross-section $1\ \text{mm}^2$ carries 1.6 A. With $n = 8\times10^{28}\ \text{m}^{-3}$, the drift speed of the electrons is:
(A) $1.25\times10^{-4}\ \text{m s}^{-1}$
(B) $1.25\times10^{-3}\ \text{m s}^{-1}$
(C) $2.5\times10^{-5}\ \text{m s}^{-1}$
(D) $1.25\times10^{-2}\ \text{m s}^{-1}$
@ans A
@sol $v_d = \dfrac{I}{neA} = \dfrac{1.6}{8\times10^{28}\times1.6\times10^{-19}\times10^{-6}} = \dfrac{1}{8\times10^{3}} = 1.25\times10^{-4}\ \text{m s}^{-1}$.
@short $1.6$ cancels with $e$'s $1.6$.
@trap The mm² → m² conversion.
@@END

@@Q P12-02 | E | 0.5 | Stretching a wire | Speed
A wire is stretched uniformly to twice its original length. Its resistance becomes:
(A) 2 times
(B) 4 times
(C) 1/2
(D) 8 times
@ans B
@sol Volume constant: $A$ halves while $L$ doubles, so $R \propto L/A$ rises ×4.
@short $R \propto L^2$ at constant volume.
@trap Assuming $A$ stays constant (×2).
@@END

@@Q P12-03 | M | 1.5 | Balanced Wheatstone network | NV
In a bridge network, $P = 1\ \Omega$, $Q = 2\ \Omega$ (in series on one side) and $R = 2\ \Omega$, $S = 4\ \Omega$ (in series on the other side). A 5 Ω resistor connects the midpoints. Find the equivalent resistance (in Ω) between the two outer ends.
@ans 2
@sol $P/Q = R/S = 1/2$: balanced, so the 5 Ω carries no current. $R_{eq} = (1 + 2)\parallel(2 + 4) = 3\parallel6 = 2\ \Omega$.
@short Check the balance first.
@trap Trying to include the middle resistor.
@@END

@@Q P12-04 | E | 1 | Terminal voltage | Basic
A cell of emf 2 V and internal resistance 0.5 Ω drives current through a 3.5 Ω resistor. The terminal voltage is:
(A) 2.0 V
(B) 1.75 V
(C) 1.5 V
(D) 0.25 V
@ans B
@sol $I = 2/4 = 0.5$ A; $V = \varepsilon - Ir = 2 - 0.25 = 1.75$ V (the same as $IR$).
@short $V = \varepsilon\dfrac{R}{R + r}$.
@trap Reporting the emf.
@@END

@@Q P12-05 | E | 1 | Maximum power transfer | NV
A battery of emf 12 V and internal resistance 2 Ω is connected to a variable load. Find the maximum power (in W) the load can draw.
@ans 18
@sol At $R = r$: $P_{max} = \dfrac{\varepsilon^2}{4r} = \dfrac{144}{8} = 18$ W.
@short —
@trap Using $\varepsilon^2/r = 72$ W.
@@END

@@Q P12-06 | M | 2 | Cells in parallel | JEE
Cells of 6 V and 4 V, each with internal resistance 1 Ω, are connected in parallel (positive to positive) across a 2 Ω resistor. The current through the resistor is:
(A) 1 A
(B) 2 A
(C) 2.5 A
(D) 5 A
@ans B
@sol $\varepsilon_{eq} = \dfrac{6/1 + 4/1}{1 + 1} = 5$ V; $r_{eq} = 0.5\ \Omega$. $I = \dfrac{5}{2 + 0.5} = 2$ A.
@short Nodal method: $\dfrac{V - 6}{1} + \dfrac{V - 4}{1} + \dfrac{V}{2} = 0 \Rightarrow V = 4$ V, so $I = 2$ A.
@trap Adding the emfs (10 V).
@@END

@@Q P12-07 | E | 1 | Metre bridge balance | Basic
In a metre bridge, the balance point is at 40 cm from the end where a 20 Ω resistor is connected. The other resistance is:
(A) 13.3 Ω
(B) 30 Ω
(C) 20 Ω
(D) 50 Ω
@ans B
@sol $\dfrac{20}{S} = \dfrac{40}{60} \Rightarrow S = 30\ \Omega$.
@short —
@trap Inverting the ratio.
@@END

@@Q P12-08 | M | 1 | Temperature coefficient | Basic
A wire's resistance is 10 Ω at 20 °C and 12 Ω at 120 °C. Taking the 20 °C value as the reference, its temperature coefficient of resistance is:
(A) $2\times10^{-3}\ ^\circ\text{C}^{-1}$
(B) $2\times10^{-2}\ ^\circ\text{C}^{-1}$
(C) $1.67\times10^{-3}\ ^\circ\text{C}^{-1}$
(D) $2\times10^{-4}\ ^\circ\text{C}^{-1}$
@ans A
@sol $\alpha = \dfrac{\Delta R}{R_0\,\Delta T} = \dfrac{2}{10\times100} = 2\times10^{-3}\ ^\circ\text{C}^{-1}$.
@short —
@trap Dividing by 12 gives (C).
@@END

@@Q P12-09 | E | 1 | Rated bulbs in series | Concept
A 100 W and a 60 W bulb (both rated at 220 V) are connected in series across 220 V. Then:
(A) the 100 W bulb glows brighter
(B) the 60 W bulb glows brighter
(C) both glow equally
(D) neither glows
@ans B
@sol $R = V^2/P$, so the 60 W bulb has the larger $R$. In series (same $I$), $P = I^2R$ is larger for it.
@short Series: the lower rating glows brighter.
@trap Thinking "100 W is always brighter".
@@END

@@SET P12 · Chapter Test

@@Q P12-T1 | E | 0.5 | Series vs parallel ratio | Speed
Four identical resistors are connected first in series, then in parallel. The ratio $R_{series}/R_{parallel}$ is:
(A) 4
(B) 8
(C) 16
(D) 1/16
@ans C
@sol $4R \div (R/4) = 16$.
@short $n^2$.
@trap —
@@END

@@Q P12-T2 | E | 0.75 | Heater at lower voltage | Basic
A heater rated 1000 W at 220 V is operated at 110 V. Its power is:
(A) 500 W
(B) 250 W
(C) 1000 W
(D) 125 W
@ans B
@sol $P \propto V^2$ (fixed $R$): $1000\times\tfrac14 = 250$ W.
@short —
@trap Using $P \propto V$.
@@END

@@Q P12-T3 | E | 1 | Charge from variable current | NV
A current $I = (2 + 3t)$ A flows in a wire. Find the charge (in C) that passes in the first 2 s.
@ans 10
@sol $q = \int_0^2(2 + 3t)\,dt = 4 + 6 = 10$ C.
@short Area under the $I$–$t$ graph (a trapezium: $\tfrac{2 + 8}{2}\times2$).
@trap Using $I(2)\times2 = 16$ C.
@@END

@@Q P12-T4 | E | 1 | Cells in series | Basic
Five cells, each of emf 1.5 V and internal resistance 0.2 Ω, are connected in series across a 4 Ω resistor. The current is:
(A) 1.5 A
(B) 1.875 A
(C) 0.375 A
(D) 7.5 A
@ans A
@sol $\varepsilon = 7.5$ V, $r = 1\ \Omega$; $I = 7.5/(4 + 1) = 1.5$ A.
@short —
@trap Ignoring the internal resistance gives 1.875 A.
@@END

@@Q P12-T5 | E | 0.5 | Non-ohmic devices | Concept
Which of the following is a non-ohmic device?
(A) a nichrome wire at constant temperature
(B) a copper wire at constant temperature
(C) a semiconductor diode
(D) a manganin resistor
@ans C
@sol A diode's I–V curve is non-linear and depends on the direction of the voltage.
@short —
@trap —
@@END

## Answers & Solutions {#p12-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Current Electricity
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
