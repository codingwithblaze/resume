# Solutions {#c05}

:::stats
Typical questions | ~1 per shift
Difficulty | Easy–Medium
Priority | High
NCERT | Class 12 · Ch 1
Study time | ~6 hours
:::

## Important concepts

- **Concentration terms:** molarity, molality, mole fraction, mass %, volume %, ppm. For definitions and conversions see Unit 1 (page [[c01]]).
- **Henry's law:** the solubility of a gas is proportional to its partial pressure: $p = K_Hx$. A **larger $K_H$ means lower solubility**. Solubility of gases falls as temperature rises.
- **Raoult's law:** for volatile components, $p_i = p_i^\circ x_i$. For a non-volatile solute, the solution's vapour pressure is $p = p_1^\circ x_1$.
- **Ideal solutions** obey Raoult's law exactly: $\Delta_{mix}H = 0$, $\Delta_{mix}V = 0$ (benzene–toluene, n-hexane–n-heptane).
- **Colligative properties** depend on the **number** of solute particles, not their nature: RLVP, $\Delta T_b$, $\Delta T_f$, $\pi$.
- **van't Hoff factor $i$** corrects for dissociation ($i > 1$) or association ($i < 1$).

## Formula sheet

:::formula Colligative properties
$$\frac{p^\circ - p}{p^\circ} = x_B \qquad \Delta T_b = iK_bm \qquad \Delta T_f = iK_fm \qquad \pi = iCRT$$
$$M_B = \frac{K_b\,w_B\times1000}{\Delta T_b\,w_A} \ \text{(same form for } K_f) \qquad M_B = \frac{w_BRT}{\pi V}$$
Water: $K_b = 0.52$ K kg mol⁻¹, $K_f = 1.86$ K kg mol⁻¹. $R = 0.0821$ L atm K⁻¹ mol⁻¹ (or 0.083 L bar K⁻¹ mol⁻¹).
:::

:::formula van't Hoff factor
$$i = \frac{\text{observed colligative property}}{\text{calculated (normal) value}} = \frac{\text{normal molar mass}}{\text{observed molar mass}}$$
Dissociation into $n$ ions with degree $\alpha$: $i = 1 + (n - 1)\alpha$. Association of $n$ molecules into one: $i = 1 - \alpha\left(1 - \dfrac1n\right)$.
Complete dissociation: NaCl 2, $\ce{CaCl2}$ 3, $\ce{K2SO4}$ 3, $\ce{K4[Fe(CN)6]}$ 5, $\ce{Al2(SO4)3}$ 5. Benzoic/acetic acid fully dimerised in benzene: $i = 0.5$.
:::

:::formula Vapour pressure of binary liquid mixtures
$$P_{total} = p_A^\circ x_A + p_B^\circ x_B \qquad y_A = \frac{p_A^\circ x_A}{P_{total}}\ \text{(vapour-phase mole fraction)}$$
The vapour is always richer in the **more volatile** component.
:::

## Deviations from Raoult's law

| | Positive deviation | Negative deviation |
|---|---|---|
| A–B interactions | weaker than A–A, B–B | stronger than A–A, B–B |
| $\Delta_{mix}H$, $\Delta_{mix}V$ | > 0, > 0 | < 0, < 0 |
| Vapour pressure | higher than ideal | lower than ideal |
| Azeotrope | **minimum-boiling** (e.g. ethanol–water, ~95% ethanol) | **maximum-boiling** (e.g. $\ce{HNO3}$–water, ~68% acid) |
| Examples | ethanol + acetone, $\ce{CS2}$ + acetone, ethanol + water | chloroform + acetone (H-bond), $\ce{HNO3}$ + water, phenol + aniline |

@@GRAPH raoult-deviation

## Numerical-solving method

1. Identify the colligative property and write its formula **with $i$**.
2. Molality needs moles of solute ÷ **kg of solvent**. Convert grams to kg.
3. For electrolytes, decide on complete dissociation vs a given $\alpha$.
4. For osmotic pressure use $C$ in mol/L and $R = 0.0821$ L atm (answer in atm).

:::shortcut Comparing colligative effects
For equal molal concentrations, compare **$i\times m$** only. Largest $i m$ → largest $\Delta T_b$, $\Delta T_f$, $\pi$ and lowest vapour pressure/freezing point.
:::

## Common traps

:::trap Mistake alerts
- Forgetting $i$ for electrolytes.
- **Higher $K_H$ → lower solubility.** It's easy to reverse this.
- Using the mass of the **solution** in molality.
- Osmotic pressure units: with $R = 0.0821$ the answer is in atm. With $R = 8.314$ you need SI units throughout.
- Freezing point depression is **positive** $\Delta T_f$; the new freezing point is $T_f^\circ - \Delta T_f$.
:::

## Question patterns

:::pyq Recurring structures
1. Molar mass from $\Delta T_b$, $\Delta T_f$, $\pi$ (common Section-B numerical).
2. $i$ and degree of dissociation/association.
3. Ordering boiling/freezing points of several solutions.
4. Raoult's law with two volatile liquids; vapour composition.
5. Positive/negative deviation identification; azeotropes.
6. Henry's law applications (scuba diving, soft drinks).
:::

## Practice questions

@@SET C05 · Practice

@@Q C05-01 | E | 0.75 | Relative lowering of vapour pressure | Basic
Pure water has a vapour pressure of 100 mm Hg at some temperature. A non-volatile solute is added so that its mole fraction is 0.02. The solution's vapour pressure is:
(A) 102 mm
(B) 98 mm
(C) 2 mm
(D) 80 mm
@ans B
@sol $p = p^\circ x_{solvent} = 100\times0.98 = 98$ mm Hg.
@short —
@trap Answering the lowering (2 mm).
@@END

@@Q C05-02 | E | 1 | Freezing-point depression | Basic
The freezing-point depression of a 0.1 molal aqueous NaCl solution, assuming complete dissociation ($K_f = 1.86$), is:
(A) 0.186 K
(B) 0.372 K
(C) 0.558 K
(D) 0.093 K
@ans B
@sol $\Delta T_f = iK_fm = 2\times1.86\times0.1 = 0.372$ K.
@short —
@trap Forgetting $i = 2$.
@@END

@@Q C05-03 | E | 1 | Osmotic pressure | Calc
The osmotic pressure of 0.1 M glucose at 300 K is about ($R = 0.0821$ L atm K⁻¹ mol⁻¹):
(A) 2.46 atm
(B) 24.6 atm
(C) 0.246 atm
(D) 4.92 atm
@ans A
@sol $\pi = CRT = 0.1\times0.0821\times300 \approx 2.46$ atm.
@short —
@trap —
@@END

@@Q C05-04 | M | 1.5 | Molar mass from elevation of boiling point | NV
1.8 g of a non-volatile non-electrolyte dissolved in 100 g of water raises its boiling point by 0.052 K ($K_b = 0.52$). Find the molar mass of the solute (in g/mol).
@ans 180
@sol $m = \Delta T_b/K_b = 0.1$ mol/kg, so moles of solute $= 0.1\times0.1 = 0.01$. $M = 1.8/0.01 = 180$ g/mol.
@short $M = \dfrac{K_b w_B\times1000}{\Delta T_b w_A} = \dfrac{0.52\times1.8\times1000}{0.052\times100}$.
@trap Using 100 g as 1 kg.
@@END

@@Q C05-05 | E | 0.5 | van't Hoff factor of a complex salt | NV
Find the van't Hoff factor of $\ce{K4[Fe(CN)6]}$ in dilute solution, assuming complete dissociation.
@ans 5
@sol $\ce{K4[Fe(CN)6] -> 4K+ + [Fe(CN)6]^{4-}}$: 5 ions. The complex ion doesn't break up.
@short —
@trap Counting the CN⁻ ligands (11).
@@END

@@Q C05-06 | E | 0.75 | Association in benzene | Concept
Acetic acid in benzene is completely dimerised. Its van't Hoff factor is:
(A) 2
(B) 1
(C) 0.5
(D) 0.25
@ans C
@sol Two molecules form one particle, so $i = 1/2$. The observed molar mass is double.
@short —
@trap —
@@END

@@Q C05-07 | E | 0.5 | Positive deviation example | Concept
Which mixture shows a **positive** deviation from Raoult's law?
(A) chloroform + acetone
(B) ethanol + acetone
(C) nitric acid + water
(D) benzene + toluene
@ans B
@sol Acetone breaks up ethanol's hydrogen bonding and forms weaker A–B interactions, so the vapour pressure is higher than ideal.
@short Chloroform–acetone forms new H-bonds, which gives a negative deviation.
@trap —
@@END

@@Q C05-08 | E | 0.5 | Henry's constant | Concept
At the same temperature, gas X has a larger Henry's-law constant $K_H$ than gas Y in water. Therefore:
(A) X is more soluble than Y
(B) X is less soluble than Y
(C) both are equally soluble
(D) solubility doesn't depend on $K_H$
@ans B
@sol $x = p/K_H$: at a given $p$, a larger $K_H$ means a smaller mole fraction dissolved.
@short —
@trap —
@@END

@@Q C05-09 | E | 1 | Isotonic solutions | Basic
Which NaCl concentration (complete dissociation) is isotonic with 0.1 M glucose?
(A) 0.1 M
(B) 0.05 M
(C) 0.2 M
(D) 0.025 M
@ans B
@sol Isotonic means equal $iC$: $1\times0.1 = 2\times C \Rightarrow C = 0.05$ M.
@short —
@trap —
@@END

@@SET C05 · Chapter Test

@@Q C05-T1 | E | 0.5 | What colligative properties depend on | Speed
Colligative properties depend on:
(A) the nature of the solute
(B) the number of solute particles
(C) the molar mass of the solvent only
(D) the chemical reactivity of the solute
@ans B
@sol —
@short —
@trap —
@@END

@@Q C05-T2 | E | 0.75 | Lowest freezing point | Concept
Among 0.1 m aqueous solutions of glucose, NaCl, $\ce{CaCl2}$ and $\ce{Al2(SO4)3}$ (complete dissociation), the lowest freezing point belongs to:
(A) glucose
(B) NaCl
(C) $\ce{CaCl2}$
(D) $\ce{Al2(SO4)3}$
@ans D
@sol $i$ = 1, 2, 3, 5. The largest $i$ gives the largest depression.
@short —
@trap —
@@END

@@Q C05-T3 | E | 0.75 | Boiling-point elevation | NV
The elevation of boiling point of 0.5 m aqueous urea ($K_b = 0.52$) is $x\times0.01$ K. Find $x$.
@ans 26
@sol $\Delta T_b = 0.52\times0.5 = 0.26$ K, so $x = 26$.
@short —
@trap —
@@END

@@Q C05-T4 | E | 0.5 | Reverse osmosis | Concept
Reverse osmosis requires:
(A) a pressure greater than the osmotic pressure applied on the solution side
(B) heating the solution
(C) a pressure smaller than the osmotic pressure
(D) no semipermeable membrane
@ans A
@sol This forces the solvent out of the solution through the membrane, as in desalination.
@short —
@trap —
@@END

@@Q C05-T5 | E | 0.5 | Azeotrope type | Concept
A solution showing large positive deviation from Raoult's law forms:
(A) a maximum-boiling azeotrope
(B) a minimum-boiling azeotrope
(C) no azeotrope
(D) an ideal solution
@ans B
@sol Higher vapour pressure → lower boiling point at the azeotropic composition.
@short —
@trap —
@@END

## Answers & Solutions {#c05-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Solutions
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
