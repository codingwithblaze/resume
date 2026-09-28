# Thermodynamics {#p08}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 11
Study time | ~9 hours
:::

## Concept summary

- **Zeroth law:** thermal equilibrium is transitive, which defines temperature.
- **First law:** energy conservation for heat and work: $Q = \Delta U + W$. Here $W$ is the work done **by** the gas (NCERT convention).
- **Internal energy** of an ideal gas depends **only on temperature**: $\Delta U = nC_v\Delta T$ for *any* process.
- **Work** is the area under the $P$–$V$ curve. It depends on the path. Heat also depends on the path.
- **Second law:** no engine converts heat entirely into work in a cycle (Kelvin–Planck), and heat doesn't flow by itself from cold to hot (Clausius). The Carnot engine sets the maximum efficiency.

## Formulas

:::formula First law & process table (ideal gas, $n$ moles)
| Process | Condition | $W$ (by gas) | $\Delta U$ | $Q$ |
|---|---|---|---|---|
| Isochoric | $V$ const | 0 | $nC_v\Delta T$ | $nC_v\Delta T$ |
| Isobaric | $P$ const | $P\Delta V = nR\Delta T$ | $nC_v\Delta T$ | $nC_p\Delta T$ |
| Isothermal | $T$ const | $nRT\ln\dfrac{V_2}{V_1}$ | 0 | $= W$ |
| Adiabatic | $Q = 0$, $PV^\gamma$ const | $\dfrac{P_1V_1 - P_2V_2}{\gamma - 1} = \dfrac{nR(T_1 - T_2)}{\gamma - 1}$ | $-W$ | 0 |
| Cyclic | returns to start | area enclosed | 0 | $= W$ |
| Free expansion | into vacuum, insulated | 0 | 0 | 0 |

Adiabatic relations: $PV^\gamma = $ const, $TV^{\gamma-1} = $ const, $P^{1-\gamma}T^\gamma = $ const.
:::

:::formula Heat capacities
$$C_p - C_v = R \qquad \gamma = \frac{C_p}{C_v}$$
| Gas | $C_v$ | $C_p$ | $\gamma$ |
|---|---|---|---|
| Monatomic | $\tfrac32R$ | $\tfrac52R$ | $5/3 \approx 1.67$ |
| Diatomic (rigid, room temperature) | $\tfrac52R$ | $\tfrac72R$ | $7/5 = 1.4$ |
| Polyatomic (nonlinear, rigid) | $3R$ | $4R$ | $4/3 \approx 1.33$ |

Mixture: $C_{v,mix} = \dfrac{n_1C_{v1} + n_2C_{v2}}{n_1 + n_2}$. In an isobaric process, the fractions of $Q$ are $\Delta U/Q = 1/\gamma$ and $W/Q = 1 - 1/\gamma$.
:::

:::formula Engines & refrigerators
$$\eta = \frac{W}{Q_1} = 1 - \frac{Q_2}{Q_1} \qquad \eta_{Carnot} = 1 - \frac{T_2}{T_1} \qquad \text{COP}_{ref} = \frac{Q_2}{W} = \frac{T_2}{T_1 - T_2} \qquad \text{COP} = \frac{1 - \eta}{\eta}$$
Temperatures are in **kelvin**. Carnot cycle: two isothermals + two adiabatics. It is reversible, and no engine working between the same two temperatures is more efficient.
:::

@@GRAPH pv-processes

:::important Reading P–V diagrams
- The **adiabatic** curve is steeper than the isothermal through the same point: slope ratio $= \gamma$.
- A clockwise cycle on a $P$–$V$ diagram means net work done **by** the gas ($W > 0$), which is an engine. Anticlockwise means work is done on the gas (a refrigerator).
- On a $P$–$T$ or $V$–$T$ diagram, convert to $P$–$V$ before finding work. Straight lines through the origin on a $V$–$T$ diagram are isobaric.
:::

## Standard models & assumptions

- Ideal gas: $PV = nRT$, $R = 8.314\ \text{J mol}^{-1}\text{K}^{-1}$.
- Quasi-static (slow) processes for the formulas above. Free expansion is not quasi-static.
- "Insulated/thermally isolated/sudden" suggests adiabatic. "Slow in contact with a reservoir" means isothermal.

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Process identification** from graphs ($P$–$V$, $V$–$T$, $P$–$T$) and signs of $Q$, $W$, $\Delta U$ for each leg.
2. **Adiabatic compression/expansion:** final $T$ or $P$ with $\gamma$.
3. **Work in a cycle** as an area; efficiency of a given cycle.
4. **Carnot efficiency / refrigerator COP**, including "what $T_1$ increase raises $\eta$ to …".
5. **Heat supplied in isobaric process** and the split between $\Delta U$ and $W$.
6. **Mixtures of gases:** $\gamma_{mix}$.
:::

## Shortcuts

:::shortcut ΔU first, always
For any process of an ideal gas, write $\Delta U = nC_v\Delta T$ first. Then get whichever of $Q$ or $W$ is easier, and the other from the first law.
**Time saved:** avoids integrating heat along a path.
:::

:::shortcut Temperature ratio in adiabatics
$T_2/T_1 = (V_1/V_2)^{\gamma-1}$. Monatomic: $\gamma - 1 = 2/3$, so compressing to $1/8$ of the volume gives $8^{2/3} = 4$, i.e. $T \times 4$.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| First law sign bookkeeping | E | 45 s |
| Carnot / COP | E | 1 min |
| Adiabatic $T$, $P$, $V$ relations | E–M | 1.5 min |
| Cyclic process work/efficiency from graph | M | 2–3 min |
| Isothermal work with logs | M | 1.5 min |
| $\gamma$ of mixtures, polytropic processes | M–H | 2.5 min |

## Common mistakes

:::trap Mistake alerts
- Sign convention: in this book (NCERT), $W$ is work done **by** the system. Some books use work **on** the system, which flips the sign.
- Using °C in Carnot efficiency.
- Assuming $\Delta U = 0$ in an adiabatic process. It's $Q$ that is zero there. $\Delta U = 0$ in isothermal and cyclic processes.
- Mixing $\ln$ and $\log_{10}$: $\ln 2 = 0.693$, $\ln 10 = 2.303$.
- Using $\gamma = 5/3$ for air (diatomic, so 7/5).
:::

## Practice questions

@@SET P08 · Practice

@@Q P08-01 | M | 1.5 | Isothermal work | Calc
Two moles of an ideal gas expand isothermally at 300 K from 10 L to 20 L. The work done by the gas is about ($R = 8.314\ \text{J mol}^{-1}\text{K}^{-1}$, $\ln2 = 0.693$):
(A) 1.73 kJ
(B) 3.46 kJ
(C) 6.92 kJ
(D) 4.99 kJ
@ans B
@sol $W = nRT\ln(V_2/V_1) = 2\times8.314\times300\times0.693 \approx 3457\ \text{J} \approx 3.46$ kJ.
@short $2\times8.314\times300 \approx 4988$; $\times0.7 \approx 3.49$. Closest option: 3.46.
@trap Using $\log_{10}2 = 0.301$ gives 1.5 kJ.
@@END

@@Q P08-02 | M | 1 | Adiabatic temperature change | Concept
A monatomic ideal gas at temperature $T$ is compressed adiabatically to one-eighth of its volume. Its new temperature is:
(A) $2T$
(B) $4T$
(C) $8T$
(D) $16T$
@ans B
@sol $TV^{\gamma-1} = $ const with $\gamma - 1 = 2/3$: $T_2 = T\cdot8^{2/3} = 4T$.
@short $8^{2/3} = (8^{1/3})^2 = 4$.
@trap Using the isothermal relation (unchanged $T$), or $\gamma$ in place of $\gamma - 1$.
@@END

@@Q P08-03 | E | 1 | Work in a rectangular cycle | NV
An ideal gas goes round a rectangular cycle on a $P$–$V$ diagram with corners at $V = 1$ L and 3 L and $P = 1\times10^5$ Pa and $3\times10^5$ Pa. Find the magnitude of the net work per cycle (in J).
@ans 400
@sol Area $= \Delta P\,\Delta V = (2\times10^5)(2\times10^{-3}) = 400$ J.
@short Work = enclosed area. 1 L = $10^{-3}$ m³.
@trap Leaving litres unconverted.
@@END

@@Q P08-04 | E | 0.5 | First law bookkeeping | Speed
A gas absorbs 500 J of heat and does 200 J of work. The change in its internal energy is:
(A) 700 J
(B) 300 J
(C) −300 J
(D) 200 J
@ans B
@sol $\Delta U = Q - W = 500 - 200 = 300$ J.
@short $Q = \Delta U + W$.
@trap Adding the two.
@@END

@@Q P08-05 | E | 0.5 | Carnot efficiency | Speed
A Carnot engine works between 500 K and 300 K. Its efficiency is:
(A) 60%
(B) 40%
(C) 20%
(D) 66.7%
@ans B
@sol $\eta = 1 - 300/500 = 0.4$.
@short —
@trap Using $T_2/T_1$ (60%).
@@END

@@Q P08-06 | E | 0.75 | Refrigerator COP | NV
An ideal (Carnot) refrigerator keeps its interior at 250 K in a room at 300 K. Find its coefficient of performance.
@ans 5
@sol $\text{COP} = \dfrac{T_2}{T_1 - T_2} = \dfrac{250}{50} = 5$.
@short —
@trap Using $T_1/(T_1 - T_2) = 6$ (the heat-pump COP).
@@END

@@Q P08-07 | M | 1 | Isobaric heat split | Concept
Heat is supplied to a rigid diatomic ideal gas at constant pressure. The fraction of the heat that increases internal energy is:
(A) 2/7
(B) 5/7
(C) 3/5
(D) 2/5
@ans B
@sol $\dfrac{\Delta U}{Q} = \dfrac{C_v}{C_p} = \dfrac{5/2}{7/2} = \dfrac57$.
@short $\Delta U/Q = 1/\gamma$.
@trap Giving the work fraction (2/7).
@@END

@@Q P08-08 | E | 0.75 | Slopes of adiabatic vs isothermal | Concept
At the same point on a $P$–$V$ diagram, the ratio (slope of adiabatic)/(slope of isothermal) is:
(A) 1
(B) $\gamma$
(C) $1/\gamma$
(D) $\gamma - 1$
@ans B
@sol Isothermal: $dP/dV = -P/V$. Adiabatic: $dP/dV = -\gamma P/V$. Ratio $= \gamma$.
@short Adiabatic is steeper by a factor $\gamma > 1$.
@trap Choosing $1/\gamma$.
@@END

@@Q P08-09 | E | 0.5 | Free expansion | Tricky
An ideal gas expands freely into a vacuum inside an insulated container. Its temperature:
(A) rises
(B) falls
(C) stays the same
(D) falls to absolute zero
@ans C
@sol $Q = 0$ (insulated) and $W = 0$ (no external pressure), so $\Delta U = 0$. For an ideal gas, $U$ depends only on $T$, so $T$ is unchanged.
@short Free expansion of an ideal gas: $\Delta T = 0$, though it's **not** an isothermal quasi-static process.
@trap Treating it as an adiabatic *reversible* expansion, which cools the gas.
@@END

@@SET P08 · Chapter Test

@@Q P08-T1 | E | 0.5 | State functions | Basic
Which of the following is a state function?
(A) heat
(B) work
(C) internal energy
(D) the heat rejected in a cycle
@ans C
@sol Internal energy depends only on the state. Heat and work depend on the path. (Their difference $Q - W = \Delta U$ is path-independent, but each alone is not.)
@short $U$, $H$, $P$, $V$, $T$ are state functions; $Q$ and $W$ are path functions.
@trap Treating heat as a property the system "has".
@@END

@@Q P08-T2 | E | 0.5 | γ for a diatomic gas | Speed
For a rigid diatomic ideal gas, $\gamma$ is:
(A) 5/3
(B) 7/5
(C) 4/3
(D) 9/7
@ans B
@sol $C_v = \tfrac52R$ and $C_p = \tfrac72R$, so $\gamma = 7/5$.
@short $\gamma = 1 + \dfrac{2}{f}$ with $f = 5$.
@trap Using the monatomic value.
@@END

@@Q P08-T3 | E | 0.75 | Isobaric work | Basic
One mole of an ideal gas is heated by 10 K at constant pressure. The work done by the gas is ($R = 8.314$):
(A) 8.3 J
(B) 83.1 J
(C) 207.9 J
(D) 124.7 J
@ans B
@sol $W = nR\Delta T = 8.314\times10 \approx 83.1$ J.
@short $P\Delta V = nR\Delta T$.
@trap Computing the heat $nC_p\Delta T$ instead.
@@END

@@Q P08-T4 | E | 0.5 | Engine efficiency | NV
An engine absorbs 1000 J per cycle and rejects 750 J. Find its efficiency (in %).
@ans 25
@sol $\eta = 1 - 750/1000 = 0.25 = 25\%$.
@short $W = 250$ J.
@trap Answering 75.
@@END

@@Q P08-T5 | E | 0.5 | Anticlockwise cycle | Concept
A cyclic process on a $P$–$V$ diagram is traversed anticlockwise. The net work done by the gas is:
(A) positive
(B) negative
(C) zero
(D) equal to the heat absorbed, which is positive
@ans B
@sol Anticlockwise means net work is done **on** the gas, so $W_{by} < 0$ and the gas rejects net heat ($Q = W < 0$).
@short Clockwise = engine; anticlockwise = refrigerator.
@trap Taking work as always positive.
@@END

## Answers & Solutions {#p08-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Thermodynamics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
