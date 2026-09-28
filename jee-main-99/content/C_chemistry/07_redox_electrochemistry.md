# Redox Reactions & Electrochemistry {#c07}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 7; Class 12 · Ch 2
Study time | ~9 hours
:::

## Important concepts

- **Oxidation** = loss of electrons, or increase in oxidation number. **Reduction** = gain of electrons, or decrease in oxidation number. The oxidising agent is itself reduced.
- **Types of redox reactions:** combination, decomposition, displacement, and **disproportionation** (the same element is both oxidised and reduced).
- **Galvanic cell:** a spontaneous redox reaction produces electricity. **Anode = oxidation (−)**, **cathode = reduction (+)**. In electrolytic cells the signs reverse, but the anode is still where oxidation happens.
- **Nernst equation** relates cell emf to concentrations. **$\Delta G = -nFE$** links electrochemistry and thermodynamics.
- **Conductance:** conductivity $\kappa$ falls on dilution, while molar conductivity $\Lambda_m$ rises. **Kohlrausch's law** gives $\Lambda_m^\circ$ of weak electrolytes.

## Formula sheet

:::formula Oxidation-number rules (in order of priority)
F is always −1. O is −2, except in peroxides (−1), superoxides (−½), $\ce{OF2}$ (+2). H is +1 (−1 in metal hydrides). Alkali metals +1, alkaline-earth metals +2. The sum equals the charge on the species.
Watch for **peroxide linkages**: S is +6 in both $\ce{H2SO5}$ and $\ce{H2S2O8}$. Cr is +6 in $\ce{CrO5}$ (butterfly structure).
:::

:::formula Titration & equivalents
**n-factor** = electrons exchanged per formula unit: $\ce{KMnO4}$ 5 (acidic), 3 (neutral), 1 (strongly basic); $\ce{K2Cr2O7}$ 6 (acidic); oxalic acid 2 (redox) or 2 (acid–base); $\ce{Fe^{2+}}$ → $\ce{Fe^{3+}}$ 1.
At the equivalence point: $n_1M_1V_1 = n_2M_2V_2$.
:::

:::formula Cells
$$E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} \qquad E_{cell} = E^\circ_{cell} - \frac{0.0591}{n}\log Q\ \ (298\ \text{K})$$
$$\Delta G = -nFE \qquad \Delta G^\circ = -nFE^\circ = -2.303RT\log K \qquad \log K = \frac{nE^\circ}{0.0591}$$
$F = 96\,500$ C mol⁻¹. Cell notation: anode | anode solution || cathode solution | cathode.
Concentration cell $\ce{M | M^{n+}(C_1) || M^{n+}(C_2) | M}$: $E = \dfrac{0.0591}{n}\log\dfrac{C_2}{C_1}$ (spontaneous when $C_2 > C_1$).
Hydrogen electrode: $E = -0.0591\,\text{pH}$ (at 1 bar $\ce{H2}$).
:::

:::formula Electrolysis (Faraday's laws)
$$m = ZIt = \frac{M}{nF}It \qquad \frac{m_1}{m_2} = \frac{E_1}{E_2}\ \text{(same charge; } E = M/n)$$
| Electrolyte (inert electrodes) | Cathode | Anode |
|---|---|---|
| molten NaCl | Na | $\ce{Cl2}$ |
| aqueous NaCl (concentrated) | $\ce{H2}$ | $\ce{Cl2}$ (overpotential of $\ce{O2}$) |
| aqueous $\ce{CuSO4}$ | Cu | $\ce{O2}$ |
| aqueous $\ce{CuSO4}$, Cu electrodes | Cu | Cu dissolves (purification) |
| dilute $\ce{H2SO4}$ | $\ce{H2}$ | $\ce{O2}$ |
:::

:::formula Conductance
$$G = \frac1R \qquad \kappa = G\cdot\frac lA = \frac{G^*}{R} \qquad \Lambda_m = \frac{\kappa\times1000}{M}\ \ (\text{S cm}^2\text{mol}^{-1},\ \kappa\ \text{in S cm}^{-1})$$
**Strong electrolyte:** $\Lambda_m = \Lambda_m^\circ - A\sqrt C$ (linear in $\sqrt C$). **Weak electrolyte:** steep rise at low $C$; use Kohlrausch.
**Kohlrausch:** $\Lambda_m^\circ = \nu_+\lambda_+^\circ + \nu_-\lambda_-^\circ$; e.g. $\Lambda^\circ(\ce{CH3COOH}) = \Lambda^\circ(\ce{CH3COONa}) + \Lambda^\circ(\ce{HCl}) - \Lambda^\circ(\ce{NaCl})$.
**Weak electrolyte:** $\alpha = \Lambda_m/\Lambda_m^\circ$; $K_a = \dfrac{C\alpha^2}{1 - \alpha}$.
:::

@@GRAPH conductivity

## Batteries & fuel cells (NCERT reactions)

| Cell | Anode | Cathode | Notes |
|---|---|---|---|
| Dry (Leclanché) | $\ce{Zn -> Zn^{2+} + 2e-}$ | $\ce{MnO2 + NH4+ + e- -> MnO(OH) + NH3}$ | ~1.5 V; primary |
| Mercury | $\ce{Zn(Hg) + 2OH- -> ZnO + H2O + 2e-}$ | $\ce{HgO + H2O + 2e- -> Hg + 2OH-}$ | 1.35 V, constant (no ions change in overall reaction) |
| Lead storage | $\ce{Pb + SO4^{2-} -> PbSO4 + 2e-}$ | $\ce{PbO2 + SO4^{2-} + 4H+ + 2e- -> PbSO4 + 2H2O}$ | secondary; $\ce{H2SO4}$ is consumed on discharge (density falls) |
| $\ce{H2}$–$\ce{O2}$ fuel cell | $\ce{2H2 + 4OH- -> 4H2O + 4e-}$ | $\ce{O2 + 2H2O + 4e- -> 4OH-}$ | ~70% efficient; used in Apollo missions; product is water |

## Common traps

:::trap Mistake alerts
- $E^\circ$ is **intensive**. Don't multiply it by coefficients when balancing (but $\Delta G^\circ$ does scale).
- Nernst $Q$ uses products over reactants; solids and pure liquids are omitted.
- For $\ce{KMnO4}$, the n-factor depends on the medium (5/3/1).
- Molar conductivity units: with κ in S cm⁻¹, use $\times1000/M$ to get S cm² mol⁻¹.
- The reducing agent is the one with the **more negative** reduction potential.
:::

## Question patterns

:::pyq Recurring structures
1. Oxidation numbers (including peroxide linkages); balancing and n-factor; titration stoichiometry.
2. $E^\circ_{cell}$, spontaneity, Nernst calculations (a very common NV type).
3. $\Delta G^\circ$ and $K$ from $E^\circ$.
4. Faraday's laws: mass deposited, time, charge; comparative deposition.
5. Conductivity ↔ molar conductivity; Kohlrausch; degree of dissociation.
6. Battery and fuel-cell reactions (NCERT text).
:::

## Practice questions

@@SET C07 · Practice

@@Q C07-01 | M | 1 | Peroxide linkage | Concept
The oxidation number of sulphur in $\ce{H2S2O8}$ (peroxodisulphuric acid) is:
(A) +7
(B) +6
(C) +8
(D) +5
@ans B
@sol The molecule has one O–O (peroxide) bond. Six O are −2 and two are −1: $2(+1) + 2x + 6(-2) + 2(-1) = 0 \Rightarrow x = +6$.
@short S can't exceed +6 (group 16).
@trap Assuming all O are −2 gives +7.
@@END

@@Q C07-02 | E | 0.75 | Disproportionation | Concept
Which reaction is a disproportionation?
(A) $\ce{Zn + CuSO4 -> ZnSO4 + Cu}$
(B) $\ce{Cl2 + 2OH- -> Cl- + ClO- + H2O}$
(C) $\ce{2H2 + O2 -> 2H2O}$
(D) $\ce{CaCO3 -> CaO + CO2}$
@ans B
@sol Cl goes from 0 to −1 (reduced) and to +1 (oxidised).
@short —
@trap —
@@END

@@Q C07-03 | E | 0.5 | Standard cell emf | Speed
$E^\circ(\ce{Zn^{2+}/Zn}) = -0.76$ V and $E^\circ(\ce{Cu^{2+}/Cu}) = +0.34$ V. The standard emf of the Daniell cell is:
(A) 0.42 V
(B) 1.10 V
(C) −1.10 V
(D) 0.34 V
@ans B
@sol $E^\circ = 0.34 - (-0.76) = 1.10$ V.
@short —
@trap —
@@END

@@Q C07-04 | M | 1.5 | Nernst equation | Calc
For $\ce{Zn | Zn^{2+}(0.01\ M) || Cu^{2+}(1\ M) | Cu}$ at 298 K ($E^\circ = 1.10$ V), the cell emf is about:
(A) 1.041 V
(B) 1.100 V
(C) 1.159 V
(D) 1.218 V
@ans C
@sol $Q = [\ce{Zn^{2+}}]/[\ce{Cu^{2+}}] = 0.01$. $E = 1.10 - \dfrac{0.0591}{2}\log0.01 = 1.10 + 0.059 = 1.159$ V.
@short A smaller Q (fewer products) raises E.
@trap Inverting Q gives 1.041 V.
@@END

@@Q C07-05 | E | 1 | ΔG° from E° | Calc
For a cell with $n = 2$ and $E^\circ = 1.10$ V, $\Delta G^\circ$ is about:
(A) −212 kJ/mol
(B) −106 kJ/mol
(C) +212 kJ/mol
(D) −21.2 kJ/mol
@ans A
@sol $\Delta G^\circ = -2\times96\,500\times1.10 \approx -212\,300$ J/mol.
@short —
@trap —
@@END

@@Q C07-06 | M | 1 | Faraday's first law | Calc
The mass of copper deposited by a current of 2 A passed for 965 s through $\ce{CuSO4}$ solution is (Cu = 63.5):
(A) 0.635 g
(B) 1.27 g
(C) 0.3175 g
(D) 6.35 g
@ans A
@sol $Q = 1930$ C $= 0.02$ F. $\ce{Cu^{2+}}$ needs 2 F per mol: $0.01$ mol $= 0.635$ g.
@short —
@trap Using $n = 1$ (1.27 g).
@@END

@@Q C07-07 | E | 1 | Molar conductivity | NV
The conductivity of 0.1 M KCl is $1.29\times10^{-2}\ \text{S cm}^{-1}$. Find its molar conductivity (in S cm² mol⁻¹).
@ans 129
@sol $\Lambda_m = \dfrac{\kappa\times1000}{M} = \dfrac{1.29\times10^{-2}\times1000}{0.1} = 129$.
@short —
@trap —
@@END

@@Q C07-08 | M | 1 | Kohlrausch's law | Basic
$\Lambda^\circ_m$ (S cm² mol⁻¹): $\ce{CH3COONa}$ 91, HCl 426, NaCl 126. $\Lambda^\circ_m$ of $\ce{CH3COOH}$ is:
(A) 391
(B) 643
(C) 461
(D) 209
@ans A
@sol $91 + 426 - 126 = 391$.
@short Add the two salts that contain the ions you want; subtract the one containing the unwanted ions.
@trap —
@@END

@@Q C07-09 | E | 0.75 | Degree of dissociation | Basic
Acetic acid at some concentration has $\Lambda_m = 39.1$ S cm² mol⁻¹, and $\Lambda^\circ_m = 391$. Its degree of dissociation is:
(A) 0.01
(B) 0.1
(C) 0.5
(D) 10
@ans B
@sol $\alpha = 39.1/391 = 0.1$.
@short —
@trap —
@@END

@@Q C07-10 | E | 1 | Equilibrium constant from E° | NV
For a cell reaction with $n = 2$ and $E^\circ = 0.0591$ V at 298 K, find the equilibrium constant.
@ans 100
@sol $\log K = \dfrac{nE^\circ}{0.0591} = 2 \Rightarrow K = 100$.
@short —
@trap —
@@END

@@Q C07-11 | E | 0.5 | Electrolysis of brine | Concept
Electrolysis of concentrated aqueous NaCl with inert electrodes gives:
(A) Na at the cathode, $\ce{Cl2}$ at the anode
(B) $\ce{H2}$ at the cathode, $\ce{Cl2}$ at the anode
(C) $\ce{H2}$ at the cathode, $\ce{O2}$ at the anode
(D) Na at the cathode, $\ce{O2}$ at the anode
@ans B
@sol Water is reduced more easily than $\ce{Na+}$. $\ce{Cl-}$ is oxidised in preference to water because of oxygen's overpotential.
@short —
@trap Using the molten-NaCl result (A).
@@END

@@Q C07-12 | E | 0.75 | Lead storage battery | Concept
When a lead storage battery discharges:
(A) $\ce{H2SO4}$ is produced
(B) $\ce{PbSO4}$ forms at both electrodes and the acid's density falls
(C) Pb is deposited on the cathode
(D) $\ce{PbO2}$ forms at the anode
@ans B
@sol Both electrodes turn to $\ce{PbSO4}$, and $\ce{H2SO4}$ is consumed, producing water.
@short —
@trap —
@@END

@@SET C07 · Chapter Test

@@Q C07-T1 | E | 0.5 | Strongest reducing agent | Speed
Which is the strongest reducing agent?
(A) Li
(B) Na
(C) Zn
(D) Cu
@ans A
@sol Li has the most negative $E^\circ$ (−3.05 V), because of its high hydration enthalpy.
@short —
@trap Choosing Cs/Na by atomic-size reasoning alone.
@@END

@@Q C07-T2 | E | 0.5 | n-factor of permanganate | Speed
The n-factor of $\ce{KMnO4}$ in acidic medium is:
(A) 1
(B) 3
(C) 5
(D) 7
@ans C
@sol $\ce{MnO4-}$ (+7) → $\ce{Mn^{2+}}$ (+2).
@short —
@trap —
@@END

@@Q C07-T3 | E | 0.5 | Electrons for dichromate reduction | NV
How many moles of electrons are needed to reduce 1 mol of $\ce{Cr2O7^{2-}}$ to $\ce{Cr^{3+}}$?
@ans 6
@sol Each Cr goes from +6 to +3 (3 electrons); ×2 = 6.
@short —
@trap —
@@END

@@Q C07-T4 | E | 0.5 | Λm vs √C | Concept
For a strong electrolyte, a plot of $\Lambda_m$ against $\sqrt C$ is:
(A) a straight line with positive slope
(B) a straight line with negative slope
(C) a curve rising steeply at low C
(D) horizontal
@ans B
@sol Debye–Hückel–Onsager: $\Lambda_m = \Lambda_m^\circ - A\sqrt C$.
@short —
@trap Choosing (C), which describes a weak electrolyte.
@@END

@@Q C07-T5 | E | 0.5 | Fuel cell | Speed
The product of an $\ce{H2}$–$\ce{O2}$ fuel cell is:
(A) $\ce{H2O2}$
(B) $\ce{H2O}$
(C) $\ce{O3}$
(D) $\ce{OH-}$ only
@ans B
@sol Overall: $\ce{2H2 + O2 -> 2H2O}$.
@short —
@trap —
@@END

## Answers & Solutions {#c07-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Redox & Electrochemistry
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
