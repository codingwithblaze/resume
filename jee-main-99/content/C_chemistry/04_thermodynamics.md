# Chemical Thermodynamics {#c04}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 5
Study time | ~9 hours
:::

## Important concepts

- **System & surroundings:** open, closed and isolated systems. **Extensive** properties depend on amount ($V$, $H$, $S$, $G$, $U$). **Intensive** properties don't ($T$, $P$, density, molar quantities).
- **State functions:** $U$, $H$, $S$, $G$, $P$, $V$, $T$. Heat and work are path functions.
- **First law:** $\Delta U = q + w$. **Chemistry (IUPAC) sign convention:** $w$ is work done **on** the system; $w = -P_{ext}\Delta V$.
- **Enthalpy** $H = U + PV$; $\Delta H = \Delta U + \Delta n_gRT$ for reactions involving gases.
- **Hess's law:** $\Delta H$ is path-independent, so thermochemical equations can be added and subtracted.
- **Second law:** a spontaneous process increases the entropy of the universe. At constant $T$, $P$: $\Delta G < 0$ means spontaneous.

:::warning Sign convention differs from Physics
In Chemistry (NCERT Class 11), $\Delta U = q + w$ with $w$ = work **done on** the system. In Physics, $\Delta U = Q - W$ with $W$ = work **done by** the system. The physics is the same; only the sign of $w$ differs. Stay consistent within each subject.
:::

## Formula sheet

:::formula Work, heat, enthalpy
$$w_{irrev} = -P_{ext}\,\Delta V \qquad w_{rev,\ isothermal} = -2.303\,nRT\log\frac{V_2}{V_1} \qquad q_V = \Delta U \qquad q_P = \Delta H$$
$$\Delta H = \Delta U + \Delta n_gRT \qquad C_p - C_v = R \qquad q = nC\Delta T$$
Free expansion (into vacuum): $w = 0$. Isothermal ideal gas: $\Delta U = \Delta H = 0$.
:::

:::formula Thermochemistry
$$\Delta_rH^\circ = \sum\Delta_fH^\circ_{products} - \sum\Delta_fH^\circ_{reactants} \qquad \Delta_rH = \sum BE_{reactants} - \sum BE_{products}$$
$\Delta_fH^\circ$ of an element in its standard state = 0 (e.g. $\ce{O2(g)}$, C(graphite), $\ce{Br2(l)}$).
Enthalpies to know by definition: formation, combustion (always negative), atomisation, bond dissociation, sublimation ($= \Delta_{fus}H + \Delta_{vap}H$), phase transition, hydration, ionisation, solution.
Strong acid + strong base neutralisation: $\Delta H \approx -57.1$ kJ per mol of water. It is less exothermic for a weak acid or base, because some energy goes into ionisation.
:::

:::formula Entropy & Gibbs energy
$$\Delta S = \frac{q_{rev}}{T} \qquad \Delta S_{fusion/vap} = \frac{\Delta H_{trans}}{T_{trans}} \qquad \Delta S_{total} = \Delta S_{sys} + \Delta S_{surr} > 0\ \text{(spontaneous)}$$
$$\Delta G = \Delta H - T\Delta S \qquad \Delta G^\circ = -RT\ln K = -2.303RT\log K \qquad \Delta G = \Delta G^\circ + RT\ln Q$$
Isothermal reversible expansion of an ideal gas: $\Delta S = nR\ln\dfrac{V_2}{V_1}$.
:::

## Spontaneity table

| $\Delta H$ | $\Delta S$ | $\Delta G = \Delta H - T\Delta S$ | Spontaneous? |
|---|---|---|---|
| − | + | always − | at all temperatures |
| + | − | always + | never |
| − | − | − at low $T$ | below $T = \Delta H/\Delta S$ |
| + | + | − at high $T$ | above $T = \Delta H/\Delta S$ |

:::shortcut Δn_g in 5 seconds
$\Delta n_g$ = (moles of gaseous products) − (moles of gaseous reactants). **Ignore liquids and solids.** Example: $\ce{C(s) + O2(g) -> CO2(g)}$ has $\Delta n_g = 0$, so $\Delta H = \Delta U$.
:::

## Common traps

:::trap Mistake alerts
- Mixing J and kJ in $\Delta G = \Delta H - T\Delta S$ ($\Delta S$ is usually given in J/K).
- Using $\log$ vs $\ln$ incorrectly in $\Delta G^\circ = -2.303RT\log K$.
- Bond-energy method: **reactants minus products** (the reverse of the formation-enthalpy method).
- $\Delta_fH^\circ$ of $\ce{O3}$, diamond or $\ce{H2O(g)}$ is **not** zero.
- The entropy of a pure perfect crystal at 0 K is zero (third law). Entropy increases: solid < liquid < gas; dissolving a solid usually increases $S$.
:::

## Question patterns

:::pyq Recurring structures
1. $\Delta H$ vs $\Delta U$ with $\Delta n_g$ (frequent Section-B numerical).
2. Hess's law manipulation; enthalpy of formation or combustion from given data.
3. Bond-enthalpy calculations.
4. Spontaneity temperature; sign analysis.
5. $\Delta G^\circ$ ↔ $K$ conversions.
6. Work in isothermal reversible vs irreversible expansion.
7. Intensive/extensive and state/path classification.
:::

## Practice questions

@@SET C04 · Practice

@@Q C04-01 | M | 1.5 | ΔH – ΔU relation | NV
For $\ce{N2(g) + 3H2(g) -> 2NH3(g)}$ at 300 K, find $\Delta H - \Delta U$ in kJ/mol. Take $R = 8.3\ \text{J K}^{-1}\text{mol}^{-1}$ and give the answer to the nearest integer (with sign).
@ans -5
@sol $\Delta n_g = 2 - 4 = -2$. $\Delta H - \Delta U = \Delta n_gRT = -2\times8.3\times300 = -4980$ J $\approx -5$ kJ/mol.
@short —
@trap Counting $\Delta n_g$ as $+2$.
@@END

@@Q C04-02 | M | 1.5 | Hess's law | JEE
Given: $\ce{C(s) + O2(g) -> CO2(g)}$, $\Delta H = -393.5$ kJ; $\ce{CO(g) + 1/2 O2(g) -> CO2(g)}$, $\Delta H = -283.0$ kJ. The enthalpy of formation of CO(g) is:
(A) −110.5 kJ/mol
(B) −676.5 kJ/mol
(C) +110.5 kJ/mol
(D) −221.0 kJ/mol
@ans A
@sol Subtract the second equation from the first: $\ce{C + 1/2 O2 -> CO}$, $\Delta H = -393.5 + 283.0 = -110.5$ kJ/mol.
@short —
@trap Adding the two equations.
@@END

@@Q C04-03 | M | 1.5 | Bond-enthalpy calculation | Calc
Using bond enthalpies (kJ/mol) H–H 436, Cl–Cl 243, H–Cl 431, $\Delta_rH$ for $\ce{H2 + Cl2 -> 2HCl}$ is:
(A) −183 kJ
(B) +183 kJ
(C) −248 kJ
(D) −431 kJ
@ans A
@sol $\Delta H = (436 + 243) - 2(431) = 679 - 862 = -183$ kJ.
@short Bonds broken − bonds formed.
@trap Doing products − reactants (+183).
@@END

@@Q C04-04 | M | 1 | Spontaneity temperature | Concept
For a reaction, $\Delta H = +30$ kJ/mol and $\Delta S = +100$ J K⁻¹ mol⁻¹. It is spontaneous:
(A) above 300 K
(B) below 300 K
(C) at all temperatures
(D) at no temperature
@ans A
@sol Both positive, so entropy-driven: spontaneous when $T > \Delta H/\Delta S = 30\,000/100 = 300$ K.
@short —
@trap Unit mismatch (0.3 K).
@@END

@@Q C04-05 | M | 1 | ΔG° from K | Calc
For a reaction at 300 K with $K = 10$, $\Delta G^\circ$ is about ($R = 8.314$):
(A) −5.74 kJ/mol
(B) +5.74 kJ/mol
(C) −2.49 kJ/mol
(D) −57.4 kJ/mol
@ans A
@sol $\Delta G^\circ = -2.303\times8.314\times300\times\log10 \approx -5744$ J/mol.
@short $2.303RT \approx 5.74$ kJ at 300 K: memorise it.
@trap Using $\ln10 = 1$.
@@END

@@Q C04-06 | E | 0.75 | Irreversible work | Basic
A gas expands against a constant external pressure of 2 bar from 1 L to 6 L. The work done **on** the gas is (1 L bar = 100 J):
(A) +1000 J
(B) −1000 J
(C) −1200 J
(D) −500 J
@ans B
@sol $w = -P_{ext}\Delta V = -2\times5 = -10$ L bar $= -1000$ J.
@short Expansion → $w < 0$ in the chemistry convention.
@trap Positive sign.
@@END

@@Q C04-07 | E | 0.5 | Intensive properties | Speed
Which is an intensive property?
(A) enthalpy
(B) volume
(C) molar heat capacity
(D) internal energy
@ans C
@sol Molar (per-mole) quantities are intensive.
@short Any extensive quantity ÷ amount → intensive.
@trap —
@@END

@@Q C04-08 | E | 1 | Entropy of vaporisation | NV
The enthalpy of vaporisation of a liquid is 30 kJ/mol at its boiling point of 300 K. Find $\Delta_{vap}S$ (in J K⁻¹ mol⁻¹).
@ans 100
@sol $\Delta S = \Delta H/T = 30\,000/300 = 100$ J K⁻¹ mol⁻¹.
@short —
@trap —
@@END

@@Q C04-09 | E | 0.75 | Standard enthalpy of formation | Concept
For which species is $\Delta_fH^\circ = 0$?
(A) $\ce{O3(g)}$
(B) C(diamond)
(C) $\ce{Br2(l)}$
(D) $\ce{H2O(l)}$
@ans C
@sol Bromine's standard state is liquid, so $\ce{Br2(l)}$ is an element in its standard state.
@short —
@trap Diamond (graphite is carbon's standard state).
@@END

@@SET C04 · Chapter Test

@@Q C04-T1 | E | 0.5 | Condition for spontaneity | Speed
At constant $T$ and $P$, a process is spontaneous when:
(A) $\Delta G > 0$
(B) $\Delta G < 0$
(C) $\Delta H > 0$
(D) $\Delta S < 0$
@ans B
@sol At constant $T$ and $P$, the criterion for a spontaneous process is $\Delta G = \Delta H - T\Delta S < 0$. Neither $\Delta H$ nor $\Delta S_{sys}$ alone decides it.
@short —
@trap —
@@END

@@Q C04-T2 | E | 0.5 | Heat of neutralisation | Concept
The enthalpy of neutralisation of HCl by NaOH is −57.1 kJ/mol. For $\ce{CH3COOH}$ with NaOH it is:
(A) exactly −57.1 kJ/mol
(B) less negative than −57.1 kJ/mol
(C) more negative than −57.1 kJ/mol
(D) zero
@ans B
@sol Some heat is used to ionise the weak acid.
@short —
@trap —
@@END

@@Q C04-T3 | E | 0.5 | Free expansion | Speed
For the free expansion of an ideal gas into a vacuum:
(A) $w = 0$, $q = 0$, $\Delta U = 0$
(B) $w < 0$, $q > 0$
(C) $\Delta U > 0$
(D) $\Delta S = 0$
@ans A
@sol No external pressure → no work. Adiabatic/ideal → $\Delta U = 0$. (But $\Delta S > 0$, since the process is spontaneous.)
@short —
@trap Choosing (D).
@@END

@@Q C04-T4 | M | 1 | Isothermal reversible work | NV
2 mol of an ideal gas expands isothermally and reversibly at 300 K from 1 L to 10 L. Find the magnitude of the work done (in kJ, nearest integer). ($R = 8.314$)
@ans 11
@sol $|w| = 2.303nRT\log(V_2/V_1) = 2.303\times2\times8.314\times300\times1 \approx 11\,488$ J ≈ 11 kJ.
@short —
@trap —
@@END

@@Q C04-T5 | E | 0.5 | Entropy increase | Speed
Which process involves a decrease in entropy?
(A) melting of ice
(B) evaporation of water
(C) freezing of water
(D) dissolving NaCl in water
@ans C
@sol Liquid → solid is more ordered.
@short —
@trap —
@@END

## Answers & Solutions {#c04-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Chemical Thermodynamics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
