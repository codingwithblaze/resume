# Current-Level Diagnostic Test {#diagnostic}

:::mock Instructions
**30 questions · 60 minutes · +4 / −1** (same marking as JEE Main, NV questions included). Use a timer, no calculator, no notes. Mark the time at which you finish each subject. The purpose is **measurement**, not a good score. Don't prepare for it, and don't look at the solutions until you've finished.
:::

@@SET Diagnostic · Physics

@@Q DP-01 | E | 1 | Dimensions of Planck's constant | Basic
The dimensional formula of Planck's constant $h$ is:
(A) $[ML^2T^{-2}]$
(B) $[ML^2T^{-1}]$
(C) $[MLT^{-1}]$
(D) $[ML^{-1}T^{-2}]$
@ans B
@sol $E = h\nu \Rightarrow h = E/\nu = [ML^2T^{-2}]/[T^{-1}] = [ML^2T^{-1}]$.
@short Same dimensions as angular momentum ($L = n h/2\pi$ in Bohr's model).
@trap Confusing with the dimensions of energy, which is option (A).
@@END

@@Q DP-02 | E | 1 | Vertical projectile time of flight | Basic
A ball is thrown vertically upward at $20\ \text{m s}^{-1}$ ($g = 10\ \text{m s}^{-2}$). It returns to the thrower's hand after:
(A) 2 s
(B) 4 s
(C) 6 s
(D) 8 s
@ans B
@sol Time to top $= u/g = 2$ s; the descent takes the same time. Total $= 2u/g = 4$ s.
@short $T = 2u/g$ for return to the launch level.
@trap Answering the time to the top (2 s).
@@END

@@Q DP-03 | E | 1.5 | Kinetic friction | Concept
A 2 kg block **sliding** on a rough horizontal floor ($\mu_k = 0.3$, $g = 10\ \text{m s}^{-2}$) is pulled by a horizontal force of 10 N in the direction of motion. Its acceleration is:
(A) $1\ \text{m s}^{-2}$
(B) $2\ \text{m s}^{-2}$
(C) $3\ \text{m s}^{-2}$
(D) $5\ \text{m s}^{-2}$
@ans B
@sol Friction $f = \mu_k mg = 0.3 \times 20 = 6$ N opposing motion. $a = (10 - 6)/2 = 2\ \text{m s}^{-2}$.
@short Net force $= F - \mu mg$.
@trap Ignoring friction gives 5.
@@END

@@Q DP-04 | M | 1.5 | Rolling kinetic energy split | Concept
A solid sphere rolls without slipping. The fraction of its total kinetic energy that is rotational is:
(A) $2/5$
(B) $2/7$
(C) $5/7$
(D) $1/2$
@ans B
@sol $K_{rot}/K_{tot} = \dfrac{\tfrac12 I\omega^2}{\tfrac12 mv^2(1 + k^2/R^2)} = \dfrac{k^2/R^2}{1 + k^2/R^2} = \dfrac{2/5}{7/5} = \dfrac27$.
@short Fraction $= \dfrac{k^2/R^2}{1+k^2/R^2}$; for a solid sphere $k^2/R^2 = 2/5$.
@trap Answering $k^2/R^2 = 2/5$ itself.
@@END

@@Q DP-05 | M | 1.5 | Escape velocity scaling | Concept
The escape speed from Earth is $11.2\ \text{km s}^{-1}$. For a planet of the same density but twice Earth's radius it is:
(A) $11.2\ \text{km s}^{-1}$
(B) $15.8\ \text{km s}^{-1}$
(C) $22.4\ \text{km s}^{-1}$
(D) $44.8\ \text{km s}^{-1}$
@ans C
@sol $v_e = \sqrt{2GM/R}$ and $M = \tfrac43\pi R^3\rho$, so $v_e = R\sqrt{\tfrac83\pi G\rho} \propto R$ at fixed $\rho$. Doubling $R$ doubles $v_e$.
@short Fixed density: $v_e \propto R$. Fixed mass: $v_e \propto 1/\sqrt{R}$.
@trap Using $v_e \propto 1/\sqrt R$ (fixed-mass case) gives the wrong direction.
@@END

@@Q DP-06 | M | 1.5 | First law, isobaric process | Concept
An ideal monatomic gas is heated at constant pressure. The fraction of the heat supplied that is converted into work is:
(A) $2/5$
(B) $3/5$
(C) $2/3$
(D) $1/3$
@ans A
@sol $W = nR\,\Delta T$, $Q = nC_p\Delta T = \tfrac52 nR\,\Delta T$, so $W/Q = 2/5$.
@short $W/Q = R/C_p = 1 - 1/\gamma$.
@trap Using $C_v$ instead of $C_p$ gives 2/3.
@@END

@@Q DP-07 | E | 1.5 | Series capacitors | Basic
Capacitors of $2\ \mu\text{F}$ and $3\ \mu\text{F}$ are connected in series across a 10 V battery. The charge on each capacitor is:
(A) $12\ \mu\text{C}$
(B) $20\ \mu\text{C}$
(C) $30\ \mu\text{C}$
(D) $50\ \mu\text{C}$
@ans A
@sol $C_{eq} = \dfrac{2\times3}{2+3} = 1.2\ \mu\text{F}$; $Q = C_{eq}V = 12\ \mu\text{C}$ (the same on both in series).
@short Series: same $Q$; $C_{eq} = C_1C_2/(C_1+C_2)$.
@trap Adding capacitances as if in parallel gives 50.
@@END

@@Q DP-08 | E | 1.5 | Resistance of a ring | NV
A uniform wire of resistance $32\ \Omega$ is bent into a circle. Find the resistance (in $\Omega$) between two diametrically opposite points.
@ans 8
@sol Each semicircle is $16\ \Omega$; they're in parallel: $16 \parallel 16 = 8\ \Omega$.
@short Two equal halves in parallel: $R/4$.
@trap Answering 16 (one half only).
@@END

@@Q DP-09 | E | 1.5 | Thin lens formula | Basic
An object is placed 30 cm in front of a convex lens of focal length 20 cm. The image is:
(A) 60 cm behind the lens, real, inverted, twice the size
(B) 12 cm behind the lens, virtual, erect
(C) 60 cm in front of the lens, virtual, erect
(D) 12 cm behind the lens, real, diminished
@ans A
@sol $\dfrac1v - \dfrac1u = \dfrac1f$ with $u = -30$: $\dfrac1v = \dfrac1{20} - \dfrac1{30} = \dfrac1{60}$, so $v = +60$ cm. $m = v/u = -2$: real, inverted, magnified.
@short Object between $f$ and $2f$ → image beyond $2f$, real, magnified.
@trap Sign error with $u$ gives 12 cm.
@@END

@@Q DP-10 | E | 1 | Photoelectric equation | NV
Photons of energy 6.0 eV fall on a metal of work function 2.0 eV. Find the stopping potential (in volts).
@ans 4
@sol $K_{max} = h\nu - \phi = 4.0$ eV, so $eV_0 = 4.0$ eV and $V_0 = 4$ V.
@short In eV units, $V_0$ (volts) $= E_{photon} - \phi$ numerically.
@trap Adding instead of subtracting the work function.
@@END

@@SET Diagnostic · Chemistry

@@Q DC-01 | E | 1 | Mole concept | Basic
The number of moles of oxygen **atoms** in 88 g of $\ce{CO2}$ is:
(A) 2
(B) 4
(C) 6
(D) 8
@ans B
@sol $88/44 = 2$ mol $\ce{CO2}$; each has 2 O atoms, so 4 mol O atoms.
@short Moles of atoms $=$ moles of molecules × atomicity.
@trap Stopping at 2 (moles of molecules).
@@END

@@Q DC-02 | E | 1 | Nodes of orbitals | Basic
The number of radial nodes in a 3p orbital is:
(A) 0
(B) 1
(C) 2
(D) 3
@ans B
@sol Radial nodes $= n - l - 1 = 3 - 1 - 1 = 1$. (Angular nodes $= l = 1$.)
@short Radial $= n-l-1$; angular $= l$; total $= n-1$.
@trap Giving the total nodes (2).
@@END

@@Q DC-03 | E | 1 | Dipole moment & shape | Basic
Which molecule has zero dipole moment?
(A) $\ce{NH3}$
(B) $\ce{H2O}$
(C) $\ce{BF3}$
(D) $\ce{CHCl3}$
@ans C
@sol $\ce{BF3}$ is trigonal planar and symmetric, so the bond dipoles cancel. The others are pyramidal, bent or tetrahedral with unequal substituents.
@short Symmetric shapes (linear $\ce{AX2}$, trigonal planar $\ce{AX3}$, tetrahedral $\ce{AX4}$) with identical atoms → $\mu = 0$.
@trap Polar bonds don't imply a polar molecule.
@@END

@@Q DC-04 | M | 1.5 | Gibbs energy & spontaneity | Concept
For a reaction, $\Delta H = -100\ \text{kJ mol}^{-1}$ and $\Delta S = -200\ \text{J K}^{-1}\text{mol}^{-1}$ (assume both are temperature independent). The reaction is spontaneous:
(A) above 500 K
(B) below 500 K
(C) at all temperatures
(D) at no temperature
@ans B
@sol $\Delta G = \Delta H - T\Delta S = -100 + 0.2T$ (kJ). $\Delta G < 0$ when $T < 500$ K.
@short Both negative → enthalpy-driven → spontaneous at low $T$, below $T = \Delta H/\Delta S$.
@trap Unit mismatch: J vs kJ gives 0.5 K or 500 000 K.
@@END

@@Q DC-05 | E | 1 | pH of strong base | Basic
The pH of $10^{-3}$ M NaOH at 25 °C is:
(A) 3
(B) 10
(C) 11
(D) 12
@ans C
@sol $[\ce{OH-}] = 10^{-3}$, so pOH $= 3$ and pH $= 14 - 3 = 11$.
@short pH + pOH = 14 at 25 °C.
@trap Reporting pOH as pH.
@@END

@@Q DC-06 | E | 1 | First-order half-life | NV
A first-order reaction has a half-life of 10 min. Find the time (in minutes) needed for 87.5% completion.
@ans 30
@sol 87.5% complete means 12.5% $= 1/8$ remains, which is 3 half-lives: $3 \times 10 = 30$ min.
@short Remaining fraction $= (1/2)^n$ for first order.
@trap Using linear (zero-order) thinking.
@@END

@@Q DC-07 | M | 1.5 | Ionisation enthalpy trend | Concept
The correct order of first ionisation enthalpy is:
(A) B < C < N < O
(B) B < C < O < N
(C) C < B < O < N
(D) O < N < C < B
@ans B
@sol Increases across the period, with one exception: N ($2p^3$, half-filled) > O ($2p^4$). So B < C < O < N.
@short Period-2 exceptions: Be > B and N > O.
@trap Forgetting the N > O exception gives (A).
@@END

@@Q DC-08 | M | 1.5 | Low-spin complexes | Concept
The spin-only magnetic moment of $\ce{[Fe(CN)6]^{3-}}$ is closest to:
(A) 1.73 BM
(B) 3.87 BM
(C) 5.92 BM
(D) 0 BM
@ans A
@sol $\ce{Fe^{3+}}$ is $d^5$. $\ce{CN-}$ is a strong-field ligand, so the complex is low spin: $t_{2g}^5 e_g^0$, one unpaired electron. $\mu = \sqrt{n(n+2)} = \sqrt3 \approx 1.73$ BM.
@short Strong-field ligands ($\ce{CN-}$, CO) pair up $d^4$–$d^7$ in octahedral complexes.
@trap Treating it as high spin gives 5.92 BM.
@@END

@@Q DC-09 | E | 1 | Carbocation stability | Basic
The most stable carbocation among the following is:
(A) $\ce{CH3+}$
(B) $\ce{CH3CH2+}$
(C) $\ce{(CH3)2CH+}$
(D) $\ce{(CH3)3C+}$
@ans D
@sol Stability grows with hyperconjugation and +I donation: 3° > 2° > 1° > methyl.
@short More α-hydrogens (hyperconjugation) → more stable alkyl carbocation.
@trap None here; this is a speed item.
@@END

@@Q DC-10 | M | 1.5 | Structural isomers of alcohols | NV
How many structurally isomeric **alcohols** have the formula $\ce{C4H10O}$?
@ans 4
@sol Butan-1-ol, butan-2-ol, 2-methylpropan-1-ol, 2-methylpropan-2-ol. (The 3 ethers are not alcohols. Counting stereoisomers is not asked.)
@short Place –OH on each distinct carbon of each C₄ skeleton: n-butane gives 2, isobutane gives 2.
@trap Including ethers gives 7.
@@END

@@SET Diagnostic · Mathematics

@@Q DM-01 | E | 1 | Composition of functions | Basic
If $f(x) = 2x + 3$ and $g(x) = x^2$, then $(f\circ g)(2)$ equals:
(A) 11
(B) 49
(C) 14
(D) 7
@ans A
@sol $(f\circ g)(2) = f(g(2)) = f(4) = 11$.
@short Apply the inner function first.
@trap Computing $g(f(2)) = 49$.
@@END

@@Q DM-02 | E | 1 | Modulus of a quotient | Basic
$\left|\dfrac{3+4i}{1-i}\right|$ equals:
(A) $5/\sqrt2$
(B) $5\sqrt2$
(C) $5/2$
(D) $7/\sqrt2$
@ans A
@sol $|z_1/z_2| = |z_1|/|z_2| = 5/\sqrt2$.
@short Never rationalise when only the modulus is asked.
@trap Rationalising wastes time and invites arithmetic slips.
@@END

@@Q DM-03 | E | 1 | Symmetric functions of roots | Basic
If $\alpha, \beta$ are the roots of $x^2 - 5x + 6 = 0$, then $\alpha^2 + \beta^2$ is:
(A) 13
(B) 25
(C) 37
(D) 11
@ans A
@sol $\alpha^2 + \beta^2 = (\alpha+\beta)^2 - 2\alpha\beta = 25 - 12 = 13$.
@short Use Vieta's relations; don't solve for the roots.
@trap Forgetting the $-2\alpha\beta$ term.
@@END

@@Q DM-04 | M | 1 | Determinant of adjoint | Concept
If $A$ is a $3\times3$ matrix with $|A| = 4$, then $|\operatorname{adj}A|$ is:
(A) 4
(B) 16
(C) 64
(D) 8
@ans B
@sol $|\operatorname{adj}A| = |A|^{n-1} = 4^2 = 16$ for $n = 3$.
@short $|\operatorname{adj}A| = |A|^{n-1}$ and $|\operatorname{adj}(\operatorname{adj}A)| = |A|^{(n-1)^2}$.
@trap Using $|A|^n = 64$.
@@END

@@Q DM-05 | E | 1.5 | Permutations with repetition | NV
Find the number of distinct arrangements of the letters of the word LEVEL.
@ans 30
@sol 5 letters with L repeated twice and E repeated twice: $\dfrac{5!}{2!\,2!} = 30$.
@short Divide by the factorial of each repeated letter's count.
@trap Dividing by $2!$ only once gives 60.
@@END

@@Q DM-06 | E | 1 | AP sum | Basic
The sum of the first 20 terms of the AP $3, 7, 11, \dots$ is:
(A) 820
(B) 800
(C) 780
(D) 840
@ans A
@sol $S_{20} = \tfrac{20}{2}[2(3) + 19(4)] = 10 \times 82 = 820$.
@short $S_n = \tfrac n2(\text{first} + \text{last})$; the last term is $3 + 76 = 79$, so $10 \times 82$.
@trap Using $20d$ instead of $19d$ gives 840.
@@END

@@Q DM-07 | E | 1 | Standard trigonometric limit | Basic
$\displaystyle\lim_{x\to0}\frac{1-\cos 2x}{x^2}$ equals:
(A) 1
(B) 2
(C) 4
(D) $1/2$
@ans B
@sol $1 - \cos2x = 2\sin^2x$, so the limit is $2\left(\dfrac{\sin x}{x}\right)^2 \to 2$.
@short $1-\cos kx \approx \dfrac{k^2x^2}{2}$ near 0.
@trap Forgetting to square $k$ (giving 1) or dropping the $\tfrac12$ (giving 4).
@@END

@@Q DM-08 | E | 1 | Definite integral | Basic
$\displaystyle\int_0^{\pi/2}\sin^2x\,dx$ equals:
(A) $\pi/2$
(B) $\pi/4$
(C) 1
(D) $\pi/8$
@ans B
@sol By King's property, $\int_0^{\pi/2}\sin^2 x\,dx = \int_0^{\pi/2}\cos^2 x\,dx$. Their sum is $\int_0^{\pi/2}1\,dx = \pi/2$, so each is $\pi/4$.
@short Average value of $\sin^2$ over a quarter period is $\tfrac12$: $\tfrac12\cdot\tfrac\pi2$.
@trap Answering $\pi/2$ by forgetting the halving.
@@END

@@Q DM-09 | E | 1 | Distance of point from line | NV
Find the perpendicular distance of the point $(1, 2)$ from the line $3x + 4y - 1 = 0$.
@ans 2
@sol $d = \dfrac{|3(1) + 4(2) - 1|}{\sqrt{3^2+4^2}} = \dfrac{10}{5} = 2$.
@short Substitute the point, take the modulus, divide by $\sqrt{a^2+b^2}$.
@trap Forgetting the constant term.
@@END

@@Q DM-10 | E | 1 | Classical probability | Basic
Two fair dice are thrown. The probability that the sum is 7 is:
(A) $1/6$
(B) $1/12$
(C) $5/36$
(D) $7/36$
@ans A
@sol Favourable pairs: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), which is 6 of 36 outcomes. $P = 1/6$.
@short Sum 7 is the most likely sum, with 6 outcomes.
@trap Counting unordered pairs gives 3.
@@END

## Diagnostic — Answers & Solutions {#diagnostic-solutions}

@@ANSWERKEY

@@SOLUTIONS

## Interpreting your score {#diagnostic-interpret}

Score each subject out of 40 (+4 correct, −1 wrong, 0 blank).

| Subject score (/40) | Starting level for that subject | What it tells you |
|---|---|---|
| 32–40 | **Advanced start** | Foundations are solid. Your gains will come from speed, PYQs and hard questions |
| 20–31 | **Intermediate start** | The core is there. Gaps are chapter-specific: use the self-audit below |
| below 20 | **Beginner start** | Rebuild concepts first. Don't start mocks until the chapter tests reach 70% |

| Total (/120) | Overall level to enter in your profile |
|---|---|
| 90+ | Advanced |
| 55–89 | Intermediate |
| below 55 | Beginner |

**Also note:**

- Your **strongest subject** is the one with the highest score *per minute*, not just the highest score.
- If you didn't finish in 60 minutes, you have a **speed gap**: add the daily calculation drill (page [[speed-drills]]).
- Two or more wrong answers in a subject *where you felt confident* means an **accuracy gap**: start the Mistake Book routine immediately.

## Syllabus self-audit {#self-audit}

Rate each unit honestly: **0** = not studied · **1** = read, weak · **2** = can solve standard questions · **3** = can solve JEE-level questions under time.

:::cols3
**Physics**

| Unit | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Units & Measurements | [ ] | [ ] | [ ] | [ ] |
| Kinematics | [ ] | [ ] | [ ] | [ ] |
| Laws of Motion | [ ] | [ ] | [ ] | [ ] |
| Work, Energy, Power | [ ] | [ ] | [ ] | [ ] |
| Rotational Motion | [ ] | [ ] | [ ] | [ ] |
| Gravitation | [ ] | [ ] | [ ] | [ ] |
| Solids & Liquids | [ ] | [ ] | [ ] | [ ] |
| Thermodynamics | [ ] | [ ] | [ ] | [ ] |
| Kinetic Theory | [ ] | [ ] | [ ] | [ ] |
| Oscillations & Waves | [ ] | [ ] | [ ] | [ ] |
| Electrostatics | [ ] | [ ] | [ ] | [ ] |
| Current Electricity | [ ] | [ ] | [ ] | [ ] |
| Magnetism | [ ] | [ ] | [ ] | [ ] |
| EMI & AC | [ ] | [ ] | [ ] | [ ] |
| EM Waves | [ ] | [ ] | [ ] | [ ] |
| Optics | [ ] | [ ] | [ ] | [ ] |
| Dual Nature | [ ] | [ ] | [ ] | [ ] |
| Atoms & Nuclei | [ ] | [ ] | [ ] | [ ] |
| Electronic Devices | [ ] | [ ] | [ ] | [ ] |
| Experimental Skills | [ ] | [ ] | [ ] | [ ] |
+++
**Chemistry**

| Unit | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Basic Concepts | [ ] | [ ] | [ ] | [ ] |
| Atomic Structure | [ ] | [ ] | [ ] | [ ] |
| Chemical Bonding | [ ] | [ ] | [ ] | [ ] |
| Thermodynamics | [ ] | [ ] | [ ] | [ ] |
| Solutions | [ ] | [ ] | [ ] | [ ] |
| Equilibrium | [ ] | [ ] | [ ] | [ ] |
| Redox & Electrochem | [ ] | [ ] | [ ] | [ ] |
| Chemical Kinetics | [ ] | [ ] | [ ] | [ ] |
| Periodicity | [ ] | [ ] | [ ] | [ ] |
| p-Block | [ ] | [ ] | [ ] | [ ] |
| d- & f-Block | [ ] | [ ] | [ ] | [ ] |
| Coordination Cpds | [ ] | [ ] | [ ] | [ ] |
| Purification & Analysis | [ ] | [ ] | [ ] | [ ] |
| GOC | [ ] | [ ] | [ ] | [ ] |
| Hydrocarbons | [ ] | [ ] | [ ] | [ ] |
| Haloalkanes/arenes | [ ] | [ ] | [ ] | [ ] |
| Oxygen compounds | [ ] | [ ] | [ ] | [ ] |
| Nitrogen compounds | [ ] | [ ] | [ ] | [ ] |
| Biomolecules | [ ] | [ ] | [ ] | [ ] |
| Practical Chemistry | [ ] | [ ] | [ ] | [ ] |
+++
**Mathematics**

| Unit | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Sets, Relations, Functions | [ ] | [ ] | [ ] | [ ] |
| Complex & Quadratics | [ ] | [ ] | [ ] | [ ] |
| Matrices & Determinants | [ ] | [ ] | [ ] | [ ] |
| Permutations & Comb. | [ ] | [ ] | [ ] | [ ] |
| Binomial Theorem | [ ] | [ ] | [ ] | [ ] |
| Sequences & Series | [ ] | [ ] | [ ] | [ ] |
| Limits, Cont., Diff. | [ ] | [ ] | [ ] | [ ] |
| Integral Calculus | [ ] | [ ] | [ ] | [ ] |
| Differential Equations | [ ] | [ ] | [ ] | [ ] |
| Coordinate Geometry | [ ] | [ ] | [ ] | [ ] |
| 3D Geometry | [ ] | [ ] | [ ] | [ ] |
| Vector Algebra | [ ] | [ ] | [ ] | [ ] |
| Statistics & Probability | [ ] | [ ] | [ ] | [ ] |
| Trigonometry | [ ] | [ ] | [ ] | [ ] |
:::
