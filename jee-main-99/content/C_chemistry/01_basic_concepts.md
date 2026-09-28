# Some Basic Concepts in Chemistry {#c01}

:::stats
Typical questions | ~1 per shift (+ used in every numerical)
Difficulty | Easy
Priority | High
NCERT | Class 11 · Ch 1
Study time | ~5 hours
:::

## Important concepts

- **Laws of chemical combination:** conservation of mass; definite proportions (a compound always has the same composition); multiple proportions (masses of B combining with a fixed mass of A are in small whole-number ratios, as in CO/CO₂); Gay-Lussac's law of gaseous volumes; Avogadro's law (equal volumes of gases at the same $T$, $P$ contain equal numbers of molecules).
- **Dalton's atomic theory:** matter is made of indivisible atoms. Atoms of an element are identical, and compounds form in fixed whole-number ratios.
- **Atomic mass unit:** $1\ \text{u} = \tfrac1{12}$ of the mass of one $^{12}$C atom $= 1.66\times10^{-24}$ g.
- **Mole:** $6.022\times10^{23}$ entities ($N_A$). Molar mass (g/mol) is numerically equal to the atomic or molecular mass in u.

## Formula sheet

:::formula Mole relations
$$n = \frac{m}{M} = \frac{N}{N_A} = \frac{V_{gas}}{V_m} \qquad V_m = 22.4\ \text{L (273 K, 1 atm)} \quad \text{or}\quad 22.7\ \text{L (273.15 K, 1 bar, NCERT STP)}$$
$$\text{Mass \% of element} = \frac{\text{(atoms)}\times\text{(atomic mass)}}{\text{molar mass}}\times100 \qquad \text{Molecular formula} = n\times\text{empirical formula},\ n = \frac{M}{M_{empirical}}$$
:::

:::formula Concentration terms
| Term | Definition | Temperature dependent? |
|---|---|---|
| Mass % (w/w) | $\dfrac{m_{solute}}{m_{solution}}\times100$ | No |
| Molarity $M$ | mol solute / L solution | **Yes** (volume changes) |
| Molality $m$ | mol solute / kg solvent | No |
| Mole fraction $x$ | $n_i/\sum n$ | No |
| ppm | $\dfrac{m_{solute}}{m_{solution}}\times10^6$ | No |

**Conversions:** $m = \dfrac{1000M}{1000d - MM_B}$ ($d$ in g/mL, $M_B$ = molar mass of solute). Dilution: $M_1V_1 = M_2V_2$. Mixing: $M_{mix} = \dfrac{M_1V_1 + M_2V_2}{V_1 + V_2}$.
Mole fraction of solute in a 1 molal aqueous solution: $\dfrac{1}{1 + 55.5} \approx 0.018$.
:::

## Numerical-solving method: stoichiometry in 4 steps

1. Write and **balance** the equation.
2. Convert every given quantity to **moles**.
3. Find the **limiting reagent**: divide moles by the stoichiometric coefficient; the smallest value is limiting.
4. Use mole ratios from the limiting reagent, then convert to the unit asked.

:::shortcut Empirical formula in 30 seconds
Divide each mass % by its atomic mass, then divide by the smallest result. If you get x.5, double everything; x.33 or x.67, triple; x.25, quadruple.
Example: C 40, H 6.67, O 53.3 → 3.33 : 6.67 : 3.33 → 1 : 2 : 1, so CH₂O.
:::

## Common traps

:::trap Mistake alerts
- Molarity uses the volume of **solution**; molality uses the mass of **solvent** (not solution).
- Counting atoms vs molecules: 1 mol of $\ce{NH3}$ contains 4 mol of atoms.
- Using 22.4 L for gases **not** at STP. Use $PV = nRT$ instead.
- Forgetting to check the limiting reagent when both reactant amounts are given.
- Mass % of an element: multiply by the **number of atoms** of that element in the formula.
:::

## Question patterns

:::pyq Recurring structures
1. Moles/atoms/molecules counting; mass of one molecule.
2. Empirical and molecular formula from % composition or combustion data.
3. Limiting reagent and yield.
4. Concentration interconversion (molarity ↔ molality ↔ mole fraction) with density.
5. Volume of gases in reactions (usually as a Section-B numerical).
:::

## Practice questions

@@SET C01 · Practice

@@Q C01-01 | E | 1 | Counting atoms | Basic
The total number of atoms in 4.25 g of $\ce{NH3}$ is about:
(A) $1.5\times10^{23}$
(B) $6.0\times10^{23}$
(C) $2.4\times10^{24}$
(D) $3.0\times10^{23}$
@ans B
@sol $n = 4.25/17 = 0.25$ mol of molecules; atoms $= 0.25\times4\times N_A = N_A \approx 6.0\times10^{23}$.
@short 0.25 mol × 4 atoms = 1 mol of atoms.
@trap Counting molecules only ($1.5\times10^{23}$).
@@END

@@Q C01-02 | E | 1 | Empirical formula | Basic
A compound contains C 40.0%, H 6.67% and O 53.3% by mass. Its empirical formula is:
(A) CHO
(B) $\ce{CH2O}$
(C) $\ce{C2H4O}$
(D) $\ce{CH2O2}$
@ans B
@sol Moles: C $40/12 = 3.33$, H $6.67/1 = 6.67$, O $53.3/16 = 3.33$. Ratio 1 : 2 : 1.
@short —
@trap —
@@END

@@Q C01-03 | M | 1.5 | Limiting reagent | NV
3 g of $\ce{H2}$ reacts with 32 g of $\ce{O2}$ to form water. Find the mass of water formed (in g).
@ans 27
@sol $2\ce{H2} + \ce{O2} \to 2\ce{H2O}$. $\ce{H2}$: 1.5 mol (÷2 = 0.75); $\ce{O2}$: 1 mol (÷1 = 1). $\ce{H2}$ is limiting, so it gives 1.5 mol $\ce{H2O}$ = 27 g.
@short Divide moles by coefficients; the smaller value is limiting.
@trap Using $\ce{O2}$ as limiting gives 36 g.
@@END

@@Q C01-04 | E | 0.5 | Molarity | Speed
5.85 g of NaCl is dissolved in water to make 500 mL of solution. The molarity is:
(A) 0.1 M
(B) 0.2 M
(C) 0.01 M
(D) 2 M
@ans B
@sol $n = 5.85/58.5 = 0.1$ mol; $M = 0.1/0.5 = 0.2$ M.
@short —
@trap Dividing by 500 mL as if it were 1 L.
@@END

@@Q C01-05 | M | 1.5 | Molarity → molality | Calc
A 2 M NaOH solution has density 1.1 g/mL. Its molality is about:
(A) 1.82 m
(B) 1.96 m
(C) 2.00 m
(D) 2.20 m
@ans B
@sol Per litre: solution mass 1100 g, solute $2\times40 = 80$ g, solvent 1020 g. $m = 2/1.020 \approx 1.96$ m.
@short $m = \dfrac{1000M}{1000d - MM_B} = \dfrac{2000}{1100 - 80}$.
@trap Using the solution mass (1.1 kg) gives 1.82.
@@END

@@Q C01-06 | E | 1 | Mole fraction from molality | Basic
The mole fraction of solute in a 1 molal aqueous solution is about:
(A) 0.018
(B) 0.1
(C) 0.5
(D) 0.001
@ans A
@sol 1 mol solute per 1000 g water (55.5 mol): $x = 1/56.5 \approx 0.0177$.
@short —
@trap —
@@END

@@Q C01-07 | E | 0.5 | Law of multiple proportions | Concept
In CO and $\ce{CO2}$, the masses of oxygen that combine with a fixed mass of carbon are in the ratio:
(A) 1 : 1
(B) 1 : 2
(C) 2 : 1
(D) 3 : 8
@ans B
@sol 12 g C combines with 16 g O (CO) and 32 g O ($\ce{CO2}$), a ratio of 1 : 2.
@short —
@trap Using mass percentages (3 : 8 is the C : O mass ratio in CO₂).
@@END

@@Q C01-08 | E | 0.5 | Molecular formula | Speed
A compound with empirical formula $\ce{CH2O}$ has molar mass 180 g/mol. Its molecular formula is:
(A) $\ce{C3H6O3}$
(B) $\ce{C6H12O6}$
(C) $\ce{C12H22O11}$
(D) $\ce{C2H4O2}$
@ans B
@sol $n = 180/30 = 6$.
@short —
@trap —
@@END

@@Q C01-09 | E | 1 | Gas volume in combustion | Basic
The volume of oxygen at STP (take 22.4 L/mol) needed to burn 1 mol of methane completely is:
(A) 22.4 L
(B) 44.8 L
(C) 67.2 L
(D) 11.2 L
@ans B
@sol $\ce{CH4 + 2O2 -> CO2 + 2H2O}$: 2 mol $\ce{O2}$ = 44.8 L.
@short —
@trap Not balancing the equation.
@@END

@@SET C01 · Chapter Test

@@Q C01-T1 | E | 0.5 | Mass of one atom | Speed
The mass of one $^{12}$C atom is about:
(A) 12 g
(B) $1.99\times10^{-23}$ g
(C) $1.66\times10^{-24}$ g
(D) $6.02\times10^{-23}$ g
@ans B
@sol $12/(6.022\times10^{23}) \approx 1.99\times10^{-23}$ g.
@short —
@trap Choosing (C), which is the value of 1 u.
@@END

@@Q C01-T2 | E | 0.5 | Percentage composition | Speed
The percentage of nitrogen in urea, $\ce{NH2CONH2}$, is about:
(A) 23.3%
(B) 46.7%
(C) 28.0%
(D) 60.0%
@ans B
@sol $28/60\times100 \approx 46.7\%$.
@short —
@trap Counting only one N (23.3%).
@@END

@@Q C01-T3 | E | 0.5 | Combustion stoichiometry | NV
Find the number of moles of $\ce{CO2}$ formed by the complete combustion of 2 mol of propane ($\ce{C3H8}$).
@ans 6
@sol $\ce{C3H8 + 5O2 -> 3CO2 + 4H2O}$: $2\times3 = 6$ mol.
@short Carbon balance: moles of $\ce{CO2}$ = moles of C atoms.
@trap —
@@END

@@Q C01-T4 | E | 0.5 | Dilution | Speed
100 mL of 0.5 M HCl is diluted to 250 mL. The new molarity is:
(A) 0.25 M
(B) 0.2 M
(C) 1.25 M
(D) 0.5 M
@ans B
@sol $M_2 = 0.5\times100/250 = 0.2$ M.
@short —
@trap —
@@END

@@Q C01-T5 | E | 0.75 | Maximum number of atoms | Concept
Which of the following contains the largest number of atoms?
(A) 1 g $\ce{H2}$
(B) 1 g He
(C) 1 g $\ce{O2}$
(D) 1 g $\ce{N2}$
@ans A
@sol Moles of atoms: $\ce{H2}$: $0.5\times2 = 1$; He: 0.25; $\ce{O2}$: $2/32 = 0.0625$; $\ce{N2}$: $2/28 \approx 0.071$.
@short Lowest mass per atom wins.
@trap —
@@END

## Answers & Solutions {#c01-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Basic Concepts
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
