# The Question Bank {#question-bank}

Sixty original questions in six sets, each built for a different exam skill. All are written for this book and modelled on the repeated structures (page [[pyq-structures]]). None is copied from a past paper.

| Set | Skill trained | Questions | Target time |
|---|---|---|---|
| QB-A | Mixed Physics | 10 | 16 min |
| QB-B | Mixed Chemistry | 10 | 12 min |
| QB-C | Mixed Mathematics | 10 | 18 min |
| QB-D | Calculation-heavy (by hand) | 8 | 24 min |
| QB-E | Tricky / trap-laden | 10 | 15 min |
| QB-F | Time pressure (sprint) | 12 | 12 min |

:::strategy How to use the sets {{tag:rec}}
Take each set **timed** and in one sitting, after the relevant chapters are done. Mark your confidence (sure / 50-50) next to each answer before checking. Take QB-E only after QB-A to QB-C: its purpose is to see whether you fall for traps when you aren't warned. Take QB-F again every two weeks, since your time on it is a clean measure of recall speed.
:::

@@SET QB-A · Mixed Physics

@@Q QB-A01 | E | 1 | Vertical projection | Kinematics
A ball is thrown vertically upward at 20 m/s ($g = 10$ m/s²). Its maximum height and total time of flight are:
(A) 20 m, 4 s
(B) 40 m, 4 s
(C) 20 m, 2 s
(D) 10 m, 2 s
@ans A
@sol $H = \dfrac{u^2}{2g} = \dfrac{400}{20} = 20$ m; $T = \dfrac{2u}{g} = 4$ s.
@short Time up = $u/g = 2$ s, so the total is 4 s.
@trap Taking the time to the top (2 s) as the total time.
@@END

@@Q QB-A02 | M | 1.5 | Rolling race | Rotation
A solid sphere and a hollow sphere of the same mass and radius roll without slipping down the same incline from rest. The ratio of their speeds at the bottom (solid : hollow) is:
(A) $5/\sqrt{21}$
(B) $\sqrt{21}/5$
(C) $1$
(D) $7/5$
@ans A
@sol $v^2 = \dfrac{2gh}{1 + k^2/R^2}$: solid $\dfrac{10gh}{7}$, hollow $\dfrac{6gh}{5}$. Ratio $= \sqrt{\dfrac{10/7}{6/5}} = \sqrt{\dfrac{25}{21}}$.
@short The body with the smaller $k^2/R^2$ is faster, so the ratio must exceed 1. Only (A) and (D) do, and (D) is a ratio of $1 + k^2/R^2$, not of speeds.
@trap Choosing 1 because "mass and radius are equal".
@@END

@@Q QB-A03 | M | 1.5 | Orbital speed | Gravitation · NV
A satellite orbits at a height $R$ above Earth's surface, where $R = 6400$ km is Earth's radius and $g = 10$ m/s² at the surface. Its orbital speed is $\sqrt x$ km/s. Find $x$.
@ans 32
@sol $v = \sqrt{\dfrac{GM}{2R}} = \sqrt{\dfrac{gR}{2}} = \sqrt{\dfrac{10\times6.4\times10^6}{2}}$ m/s $= \sqrt{3.2\times10^7}$ m/s $= \sqrt{32}$ km/s.
@short $gR = 64$ km²/s², so $v^2 = 32$ km²/s².
@trap Using $r = R$ instead of $2R$ (gives 64).
@@END

@@Q QB-A04 | M | 1.5 | Heat at constant pressure | Thermodynamics
One mole of an ideal monatomic gas is heated at constant pressure through 100 K ($R = 8.3$ J/mol K). The heat supplied is:
(A) 2075 J
(B) 1245 J
(C) 830 J
(D) 2905 J
@ans A
@sol $Q = nC_P\Delta T = \tfrac52(8.3)(100) = 2075$ J.
@short $Q : \Delta U : W = 5 : 3 : 2$ for a monatomic gas at constant pressure.
@trap Using $C_V$ (1245 J is $\Delta U$; 830 J is the work).
@@END

@@Q QB-A05 | E | 0.75 | rms speed ratio | Kinetic theory
The rms speed of oxygen molecules at temperature $T$ is $v$. At the same temperature, the rms speed of hydrogen molecules is:
(A) $4v$
(B) $v/4$
(C) $16v$
(D) $2v$
@ans A
@sol $v_{rms} \propto \dfrac{1}{\sqrt M}$: $\sqrt{32/2} = 4$.
@short —
@trap Forgetting the square root (16v).
@@END

@@Q QB-A06 | M | 1.5 | Partial dielectric slab | Capacitors · NV
An air-filled parallel-plate capacitor has capacitance 10 μF. A slab of dielectric constant 4, with thickness half the plate separation, is inserted parallel to the plates and covers their full area. Find the new capacitance in μF.
@ans 16
@sol $C = \dfrac{\varepsilon_0A}{d - t + t/K}$ with $t = \tfrac d2$: the denominator is $\tfrac d2 + \tfrac d8 = \tfrac{5d}{8}$, so $C = \tfrac85C_0 = 16$ μF.
@short Two capacitors in series: $2C_0$ (air) and $8C_0$ (dielectric) give $\dfrac{16}{10}C_0$.
@trap Multiplying by $K$ as if the gap were completely filled (40 μF).
@@END

@@Q QB-A07 | E | 1 | Maximum power transfer | Current electricity · NV
A cell of emf 12 V and internal resistance 1 Ω is connected to a variable external resistor. Find the maximum power (in W) that can be delivered to the resistor.
@ans 36
@sol Maximum power occurs at $R = r$: $P = \dfrac{\varepsilon^2}{4r} = \dfrac{144}{4} = 36$ W.
@short —
@trap Computing $\varepsilon^2/r = 144$ W (the power at short circuit, dissipated inside the cell).
@@END

@@Q QB-A08 | M | 1.5 | Radius in a magnetic field | Magnetism
A proton and an alpha particle with equal kinetic energies move perpendicular to the same uniform magnetic field. The ratio of their radii $r_p : r_\alpha$ is:
(A) $1 : 1$
(B) $1 : 2$
(C) $2 : 1$
(D) $1 : \sqrt2$
@ans A
@sol $r = \dfrac{\sqrt{2mK}}{qB}$. For the alpha particle, $m \to 4m$ and $q \to 2e$: $\dfrac{\sqrt{4}}{2} = 1$.
@short $r \propto \dfrac{\sqrt m}{q}$ at fixed $K$.
@trap Using $r \propto m$ alone (equal speeds) gives $1 : 2$.
@@END

@@Q QB-A09 | E | 1 | Thin lens | Optics
A convex lens of focal length 20 cm forms a real image 60 cm from the lens. The object distance is:
(A) 30 cm
(B) 15 cm
(C) 40 cm
(D) 60 cm
@ans A
@sol $\dfrac1v - \dfrac1u = \dfrac1f$: $\dfrac1u = \dfrac1{60} - \dfrac1{20} = -\dfrac{1}{30}$, so $u = -30$ cm.
@short —
@trap Adding the reciprocals ($\tfrac1{20} + \tfrac1{60}$) gives 15 cm.
@@END

@@Q QB-A10 | E | 1 | Stopping potential | Modern physics · NV
Light of wavelength 310 nm falls on a metal with work function 2 eV. Find the stopping potential in volts.
@ans 2
@sol $E = \dfrac{1240}{310} = 4$ eV, so $K_{max} = 2$ eV and $V_0 = 2$ V.
@short —
@trap —
@@END

@@SET QB-B · Mixed Chemistry

@@Q QB-B01 | E | 0.75 | Atoms in a sample | Mole concept · NV
How many moles of oxygen atoms are present in 49 g of $\ce{H2SO4}$ ($M = 98$)?
@ans 2
@sol 0.5 mol of $\ce{H2SO4}$ contains $0.5\times4 = 2$ mol of O atoms.
@short —
@trap Answering 0.5 (moles of molecules).
@@END

@@Q QB-B02 | E | 0.5 | Nodes | Atomic structure
The number of radial nodes in a 3p orbital is:
(A) 1
(B) 0
(C) 2
(D) 3
@ans A
@sol Radial nodes $= n - l - 1 = 3 - 1 - 1 = 1$.
@short —
@trap Giving the total number of nodes (2).
@@END

@@Q QB-B03 | E | 0.5 | Dipole moment | Bonding
Which molecule has zero dipole moment?
(A) $\ce{NH3}$
(B) $\ce{BF3}$
(C) $\ce{H2O}$
(D) $\ce{CHCl3}$
@ans B
@sol $\ce{BF3}$ is trigonal planar and symmetrical, so the bond dipoles cancel.
@short —
@trap —
@@END

@@Q QB-B04 | M | 1 | Temperature of spontaneity | Thermodynamics · NV
For a reaction, $\Delta H = +30$ kJ/mol and $\Delta S = +100$ J K⁻¹ mol⁻¹. Find the temperature (in K) above which it is spontaneous.
@ans 300
@sol $T = \dfrac{\Delta H}{\Delta S} = \dfrac{30000}{100} = 300$ K.
@short —
@trap Mixing kJ and J (gives 0.3).
@@END

@@Q QB-B05 | E | 0.75 | Buffer pH | Equilibrium
The pH of a solution that is 0.1 M in $\ce{CH3COOH}$ and 0.1 M in $\ce{CH3COONa}$ ($\text{p}K_a = 4.74$) is:
(A) 4.74
(B) 9.26
(C) 7.00
(D) 2.87
@ans A
@sol Equal concentrations: $\text{pH} = \text{p}K_a + \log1 = 4.74$.
@short —
@trap Answering $\text{p}K_b$ (9.26).
@@END

@@Q QB-B06 | E | 0.75 | Half-lives | Kinetics · NV
A first-order reaction has a half-life of 10 min. Find the time (in min) for 87.5% completion.
@ans 30
@sol 87.5% complete means $\tfrac18$ remains: 3 half-lives.
@short —
@trap —
@@END

@@Q QB-B07 | M | 1 | Low-spin complex | Coordination
The spin-only magnetic moment of $\ce{[Fe(CN)6]^3-}$ is:
(A) 1.73 BM
(B) 5.92 BM
(C) 3.87 BM
(D) 0 BM
@ans A
@sol $\ce{Fe^3+}$ is $d^5$; $\ce{CN-}$ is strong-field, giving $t_{2g}^5$ with 1 unpaired electron: $\sqrt3 = 1.73$ BM.
@short —
@trap The high-spin value (5.92 BM) applies to weak-field ligands such as $\ce{F-}$.
@@END

@@Q QB-B08 | M | 1 | Ionisation enthalpy order | Periodicity
The correct order of first ionisation enthalpy is:
(A) $\ce{Be} < \ce{B} < \ce{C} < \ce{N}$
(B) $\ce{B} < \ce{Be} < \ce{O} < \ce{N}$
(C) $\ce{B} < \ce{Be} < \ce{N} < \ce{O}$
(D) $\ce{Be} < \ce{B} < \ce{O} < \ce{N}$
@ans B
@sol Two exceptions: $\ce{Be} > \ce{B}$ (removal from $2p$ in B) and $\ce{N} > \ce{O}$ (half-filled $2p^3$ in N).
@short —
@trap Using the plain left-to-right trend.
@@END

@@Q QB-B09 | E | 0.75 | Acidity | GOC
The most acidic compound among these is:
(A) phenol
(B) $p$-nitrophenol
(C) $p$-cresol
(D) ethanol
@ans B
@sol The $-\ce{NO2}$ group at the para position stabilises the phenoxide ion by $-M$ and $-I$ effects.
@short —
@trap —
@@END

@@Q QB-B10 | M | 1 | Iodoform without Tollens' | Carbonyls
A compound $\ce{C3H6O}$ gives a positive iodoform test and a negative Tollens' test. It is:
(A) propanone
(B) propanal
(C) prop-2-en-1-ol
(D) methoxyethene
@ans A
@sol Acetone has $\ce{CH3CO-}$ (iodoform positive) and is a ketone (Tollens' negative).
@short —
@trap Propanal is an aldehyde (Tollens' positive) and has no $\ce{CH3CO-}$ group.
@@END

@@SET QB-C · Mixed Mathematics

@@Q QB-C01 | M | 1.5 | Locus in the Argand plane | Complex numbers
The locus of $z$ satisfying $\lvert z - 2\rvert = \lvert z + 2i\rvert$ is:
(A) $x + y = 0$
(B) $x - y = 0$
(C) $x + y = 2$
(D) a circle
@ans A
@sol The points equidistant from $(2, 0)$ and $(0, -2)$ lie on the perpendicular bisector, through $(1, -1)$ with slope $-1$: $y = -x$.
@short Test $z = 0$: $\lvert-2\rvert = \lvert2i\rvert$ ✓, so the locus passes through the origin. Only (A) and (B) do; (B) fails at $z = 1 + i$.
@trap —
@@END

@@Q QB-C02 | M | 1.5 | Determinant of an adjoint | Matrices · NV
$A$ is a $3\times3$ matrix with $\lvert A\rvert = 4$. Find $\lvert\operatorname{adj}(2A)\rvert$.
@ans 1024
@sol $\lvert\operatorname{adj}B\rvert = \lvert B\rvert^2$ for $3\times3$ matrices, and $\lvert2A\rvert = 8\cdot4 = 32$. So the answer is $32^2 = 1024$.
@short —
@trap Using $\lvert2A\rvert = 2\lvert A\rvert$.
@@END

@@Q QB-C03 | E | 1 | Term independent of x | Binomial · NV
Find the term independent of $x$ in $\left(x^2 + \dfrac1x\right)^6$.
@ans 15
@sol $T_{r+1} = {}^6C_rx^{12 - 3r}$; $r = 4$ gives ${}^6C_4 = 15$.
@short —
@trap —
@@END

@@Q QB-C04 | E | 0.75 | Arrangements with repetition | P&C · NV
In how many ways can the letters of BANANA be arranged?
@ans 60
@sol $\dfrac{6!}{3!\,2!} = 60$.
@short —
@trap —
@@END

@@Q QB-C05 | M | 2 | Infinite GP conditions | Sequences · NV
An infinite GP has sum 20, and the sum of the squares of its terms is 100. Find its first term.
@ans 8
@sol $\dfrac{a}{1 - r} = 20$ and $\dfrac{a^2}{1 - r^2} = 100$. Dividing the second by the square of the first: $\dfrac{1 - r}{1 + r} = \dfrac14 \Rightarrow r = \dfrac35$, so $a = 20\cdot\dfrac25 = 8$.
@short —
@trap —
@@END

@@Q QB-C06 | E | 1 | Standard limit | Limits · NV
Find $\displaystyle\lim_{x\to0}\frac{1 - \cos2x}{x^2}$.
@ans 2
@sol $1 - \cos2x = 2\sin^2x$, and $\dfrac{2\sin^2x}{x^2} \to 2$.
@short $1 - \cos kx \approx \dfrac{k^2x^2}{2}$.
@trap —
@@END

@@Q QB-C07 | M | 1.5 | King's property | Definite integrals
$\displaystyle\int_0^\pi x\sin x\,dx$ equals:
(A) $\pi$
(B) $\pi/2$
(C) $2\pi$
(D) $0$
@ans A
@sol By King's rule, $I = \int_0^\pi(\pi - x)\sin x\,dx$, so $2I = \pi\int_0^\pi\sin x\,dx = 2\pi$.
@short —
@trap Assuming odd symmetry (the interval is not symmetric about 0).
@@END

@@Q QB-C08 | E | 1 | Separable DE | Differential equations · NV
If $\dfrac{dy}{dx} = \dfrac yx$ and $y(1) = 2$, find $y(3)$.
@ans 6
@sol $\ln y = \ln x + C$, so $y = kx$ with $k = 2$.
@short —
@trap —
@@END

@@Q QB-C09 | E | 1 | Hyperbola eccentricity | Conics
The eccentricity of the hyperbola $9x^2 - 16y^2 = 144$ is:
(A) $5/4$
(B) $4/5$
(C) $5/3$
(D) $3/4$
@ans A
@sol $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$, so $e = \sqrt{1 + \tfrac9{16}} = \tfrac54$.
@short —
@trap Swapping $a^2$ and $b^2$ gives $\sqrt{1 + 16/9} = 5/3$.
@@END

@@Q QB-C10 | E | 1 | Without replacement | Probability
Two cards are drawn without replacement from a pack of 52. The probability that both are aces is:
(A) $1/221$
(B) $1/169$
(C) $1/13$
(D) $2/221$
@ans A
@sol $\dfrac{4}{52}\cdot\dfrac{3}{51} = \dfrac{1}{221}$.
@short —
@trap $1/169$ is the answer *with* replacement.
@@END

@@SET QB-D · Calculation-Heavy

@@Q QB-D01 | M | 2.5 | Pushing up a rough incline | Laws of motion · NV
A 2 kg block is pushed up a rough incline ($\theta = 37^\circ$, $\mu = 0.5$) at constant velocity by a force parallel to the incline. Take $g = 10$ m/s², $\sin37^\circ = 0.6$. Find the force in newtons.
@ans 20
@sol $F = mg\sin\theta + \mu mg\cos\theta = 20(0.6) + 0.5\times20\times0.8 = 12 + 8 = 20$ N.
@short —
@trap Friction acts down the incline when the block moves up. Subtracting it gives 4 N.
@@END

@@Q QB-D02 | M | 2.5 | Fringe positions | Wave optics · NV
In a YDSE, $d = 0.3$ mm, $D = 1.5$ m and $\lambda = 600$ nm. Find the distance (in mm) between the 2nd bright fringe on one side of the central maximum and the 4th bright fringe on the other side.
@ans 18
@sol $\beta = \dfrac{\lambda D}{d} = \dfrac{600\times10^{-9}\times1.5}{0.3\times10^{-3}} = 3$ mm. Distance $= (2 + 4)\beta = 18$ mm.
@short —
@trap Subtracting the positions ($2\beta$) as if both fringes were on the same side.
@@END

@@Q QB-D03 | M | 2.5 | Power in an LCR circuit | AC · NV
A series LCR circuit has $R = 30$ Ω, $X_L = 80$ Ω and $X_C = 40$ Ω, and is connected to a 200 V (rms) supply. Find the average power in watts.
@ans 480
@sol $Z = \sqrt{30^2 + 40^2} = 50$ Ω, so $I_{rms} = 4$ A and $P = I^2R = 480$ W.
@short $P = \dfrac{V^2R}{Z^2} = \dfrac{40000\times30}{2500}$.
@trap Using $VI = 800$ W (it ignores the power factor 0.6).
@@END

@@Q QB-D04 | M | 2 | Nernst equation | Electrochemistry
For $\ce{Zn | Zn^2+ (0.01 M) || Cu^2+ (1 M) | Cu}$ with $E^\circ = 1.10$ V at 298 K, the cell emf is:
(A) 1.159 V
(B) 1.041 V
(C) 1.10 V
(D) 1.218 V
@ans A
@sol $E = 1.10 - \dfrac{0.059}{2}\log\dfrac{[\ce{Zn^2+}]}{[\ce{Cu^2+}]} = 1.10 - 0.0295(-2) = 1.159$ V.
@short A lower product concentration ($\ce{Zn^2+}$) must *raise* the emf, so (B) and (C) are out immediately.
@trap Inverting $Q$ gives 1.041 V.
@@END

@@Q QB-D05 | M | 1.5 | Depression with a van 't Hoff factor | Solutions
The freezing-point depression of 0.1 molal aqueous $\ce{K2SO4}$, assuming complete dissociation ($K_f = 1.86$ K kg/mol), is:
(A) 0.558 K
(B) 0.186 K
(C) 0.372 K
(D) 0.744 K
@ans A
@sol $i = 3$: $\Delta T_f = 3\times1.86\times0.1 = 0.558$ K.
@short —
@trap Using $i = 2$ (0.372 K).
@@END

@@Q QB-D06 | M | 2 | Area between curves | Area
The area bounded by $y = x^2$ and $y = 2x$ is:
(A) $4/3$
(B) $8/3$
(C) $2/3$
(D) $16/3$
@ans A
@sol The curves meet at $x = 0$ and $x = 2$. $\int_0^2(2x - x^2)\,dx = 4 - \tfrac83 = \tfrac43$.
@short Area between $y = x^2$ and $y = mx$ is $\dfrac{m^3}{6}$.
@trap —
@@END

@@Q QB-D07 | M | 2.5 | Removing observations | Statistics · NV
Ten observations have mean 5 and variance 4. Two observations, 1 and 9, are found to be invalid and removed. Find the variance of the remaining eight.
@ans 1
@sol $\sum x = 50$ and $\sum x^2 = 10(4 + 25) = 290$. After removal: $\sum x = 40$, $\sum x^2 = 290 - 1 - 81 = 208$. Mean $= 5$, variance $= 26 - 25 = 1$.
@short —
@trap Assuming the variance is unchanged because the mean is unchanged.
@@END

@@Q QB-D08 | H | 3 | Shortest distance | 3D · NV
If $d$ is the shortest distance between $\dfrac{x - 1}{2} = \dfrac{y - 2}{3} = \dfrac{z - 3}{4}$ and $\dfrac{x - 2}{3} = \dfrac{y - 4}{4} = \dfrac{z - 5}{5}$, find $6d^2$.
@ans 1
@sol $\vec a_2 - \vec a_1 = (1, 2, 2)$; $\vec b_1\times\vec b_2 = (-1, 2, -1)$ with magnitude $\sqrt6$. Dot product $= -1 + 4 - 2 = 1$, so $d = \tfrac1{\sqrt6}$.
@short Keep it squared: $d^2 = \tfrac16$.
@trap —
@@END

@@SET QB-E · Tricky & Trap-Laden

@@Q QB-E01 | M | 1.5 | Rod pivoted at one end | Rotation
A uniform rod of length $L$, pivoted at one end, is released from rest in a horizontal position. Its initial angular acceleration is:
(A) $3g/(2L)$
(B) $6g/L$
(C) $2g/L$
(D) $g/L$
@ans A
@sol $\tau = mg\tfrac L2$ and $I = \tfrac13mL^2$, so $\alpha = \dfrac{3g}{2L}$.
@short —
@trap Using $I_{cm} = \tfrac1{12}mL^2$ gives $6g/L$. The axis is at the end.
@@END

@@Q QB-E02 | E | 0.5 | Uniform circular motion | Concept
A particle moves in a circle at constant speed. Which quantity stays constant?
(A) velocity
(B) acceleration
(C) kinetic energy
(D) momentum
@ans C
@sol The speed is constant, so KE is constant. The directions of velocity, momentum and acceleration change continuously.
@short —
@trap Choosing acceleration: its magnitude is constant, but its direction is not.
@@END

@@Q QB-E03 | E | 0.75 | Current division | Circuits
Resistors of 4 Ω and 12 Ω are connected in parallel across an ideal 6 V battery. The current through the 4 Ω resistor is:
(A) 1.5 A
(B) 0.5 A
(C) 2 A
(D) 1 A
@ans A
@sol Each resistor has the full 6 V across it: $I = \dfrac64 = 1.5$ A.
@short —
@trap Splitting the total current (2 A) in the ratio of the resistances instead of inversely gives 0.5 A.
@@END

@@Q QB-E04 | M | 1 | Overtones of a closed pipe | Waves · NV
A pipe 50 cm long is closed at one end. Taking $v = 340$ m/s, find the frequency (in Hz) of its second overtone.
@ans 850
@sol $f_1 = \dfrac{v}{4L} = 170$ Hz. A closed pipe has only odd harmonics, so the second overtone is the 5th harmonic: 850 Hz.
@short —
@trap Answering $3f_1$ (the *first* overtone) or $2f_1$ (not present in a closed pipe).
@@END

@@Q QB-E05 | E | 0.5 | Reducing sugars | Biomolecules
Which of the following is **not** a reducing sugar?
(A) sucrose
(B) glucose
(C) maltose
(D) lactose
@ans A
@sol In sucrose, both anomeric carbons are tied up in the glycosidic bond.
@short —
@trap Missing the word "not".
@@END

@@Q QB-E06 | M | 1 | Very dilute acid | Ionic equilibrium
The pH of $10^{-8}$ M $\ce{HCl}$ at 25 °C is approximately:
(A) 6.98
(B) 8
(C) 7
(D) 6
@ans A
@sol Include water's ions: $x^2 - 10^{-8}x - 10^{-14} = 0$ gives $[\ce{H+}] \approx 1.05\times10^{-7}$, so pH ≈ 6.98.
@short An acid solution can't have pH > 7. (B) and (C) are impossible.
@trap Taking $\text{pH} = -\log10^{-8} = 8$.
@@END

@@Q QB-E07 | M | 1 | Counting isomers | Isomerism · NV
How many structural isomers of $\ce{C4H10O}$ are alcohols?
@ans 4
@sol Butan-1-ol, butan-2-ol, 2-methylpropan-1-ol and 2-methylpropan-2-ol.
@short —
@trap Including the three ethers (the question asks for alcohols only), or counting the enantiomers of butan-2-ol (not structural isomers).
@@END

@@Q QB-E08 | M | 1 | Modulus equation | Quadratics · NV
Find the number of real roots of $x^2 - 5\lvert x\rvert + 6 = 0$.
@ans 4
@sol $\lvert x\rvert = 2$ or $3$, so $x = \pm2, \pm3$.
@short —
@trap Answering 2 by ignoring the modulus.
@@END

@@Q QB-E09 | E | 1 | Conditional probability | Probability
If $P(A) = 0.6$, $P(B) = 0.5$ and $P(A\cup B) = 0.8$, then $P(A\mid B)$ equals:
(A) 0.6
(B) 0.3
(C) 0.5
(D) 0.75
@ans A
@sol $P(A\cap B) = 0.6 + 0.5 - 0.8 = 0.3$, so $P(A\mid B) = \dfrac{0.3}{0.5} = 0.6$.
@short —
@trap Stopping at $P(A\cap B) = 0.3$.
@@END

@@Q QB-E10 | M | 1.5 | Log with base below 1 | Functions
The domain of $f(x) = \sqrt{\log_{1/2}(x - 1)}$ is:
(A) $(1, 2]$
(B) $[2, \infty)$
(C) $(1, \infty)$
(D) $[1, 2]$
@ans A
@sol We need $\log_{1/2}(x - 1) \ge 0$. Since the base is below 1, this means $0 < x - 1 \le 1$.
@short —
@trap Not reversing the inequality for a base below 1 gives $[2, \infty)$.
@@END

@@SET QB-F · Time-Pressure Sprint (target: 12 minutes)

@@Q QB-F01 | E | 0.5 | Dimensions | Speed
The dimensional formula of impulse is:
(A) $\text{MLT}^{-1}$
(B) $\text{MLT}^{-2}$
(C) $\text{ML}^2\text{T}^{-1}$
(D) $\text{ML}^{-1}\text{T}$
@ans A
@sol Impulse = change in momentum.
@short —
@trap Confusing it with force ($\text{MLT}^{-2}$).
@@END

@@Q QB-F02 | E | 0.5 | de Broglie wavelength | Speed
The de Broglie wavelength of an electron accelerated through 100 V is about:
(A) 1.23 Å
(B) 12.3 Å
(C) 0.123 Å
(D) 123 Å
@ans A
@sol $\lambda = \dfrac{12.27}{\sqrt{100}}$ Å.
@short —
@trap —
@@END

@@Q QB-F03 | E | 0.5 | Radioactive decay | Speed
A nuclide has a half-life of 5 days. The fraction left after 15 days is:
(A) $1/8$
(B) $1/3$
(C) $1/6$
(D) $1/16$
@ans A
@sol Three half-lives: $(1/2)^3$.
@short —
@trap —
@@END

@@Q QB-F04 | E | 0.5 | Series capacitors | Speed · NV
Find the equivalent capacitance (in μF) of three 3 μF capacitors in series.
@ans 1
@sol $\dfrac1C = \dfrac13\times3$.
@short —
@trap —
@@END

@@Q QB-F05 | E | 0.5 | Hybridisation | Speed
The hybridisation of Xe in $\ce{XeF4}$ is:
(A) $sp^3d^2$
(B) $sp^3d$
(C) $sp^3$
(D) $dsp^2$
@ans A
@sol 4 bond pairs + 2 lone pairs give a steric number of 6 (square planar shape).
@short —
@trap Deducing hybridisation from the square planar shape ($dsp^2$) instead of the steric number.
@@END

@@Q QB-F06 | E | 0.5 | Oxidation state | Speed · NV
Find the oxidation state of Cr in $\ce{K2Cr2O7}$.
@ans 6
@sol $2 + 2x - 14 = 0$.
@short —
@trap —
@@END

@@Q QB-F07 | E | 0.5 | Sigma bonds | Speed · NV
How many σ bonds are there in ethyne?
@ans 3
@sol Two C–H bonds and one C–C σ bond (plus two π bonds).
@short —
@trap —
@@END

@@Q QB-F08 | E | 0.5 | Unpaired electrons | Speed · NV
How many unpaired electrons does a ground-state Cr atom ($Z = 24$) have?
@ans 6
@sol $[\ce{Ar}]\,3d^5\,4s^1$.
@short —
@trap Using $3d^44s^2$ (gives 4).
@@END

@@Q QB-F09 | E | 0.5 | Powers of i | Speed
$i^{2027}$ equals:
(A) $-i$
(B) $i$
(C) $-1$
(D) $1$
@ans A
@sol $2027 = 4\times506 + 3$, and $i^3 = -i$.
@short —
@trap —
@@END

@@Q QB-F10 | E | 0.5 | Combinations | Speed · NV
Find $^{10}C_3$.
@ans 120
@sol $\dfrac{10\cdot9\cdot8}{6}$.
@short —
@trap —
@@END

@@Q QB-F11 | E | 0.5 | Derivative | Speed · NV
Find $\dfrac{d}{dx}e^{2x}$ at $x = 0$.
@ans 2
@sol $2e^{2x}$ at $x = 0$.
@short —
@trap —
@@END

@@Q QB-F12 | E | 0.5 | Slope of a line | Speed
The slope of $3x - 4y + 7 = 0$ is:
(A) $3/4$
(B) $-3/4$
(C) $4/3$
(D) $-4/3$
@ans A
@sol $-\dfrac ab = -\dfrac{3}{-4}$.
@short —
@trap Sign error with $-a/b$.
@@END

## Answers & Solutions {#question-bank-solutions}

@@ANSWERKEY

@@SOLUTIONS
