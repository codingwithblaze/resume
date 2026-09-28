# Full-Length Mock Test 1 {#mock-1}

:::mock Instructions (same pattern as the 2026 paper [NTA-IB26])
- **75 questions, 300 marks, 3 hours.** Each subject has 20 MCQs (Section A) and 5 numerical-value questions (Section B), all compulsory.
- **Marking:** +4 correct, −1 incorrect, 0 unanswered, in **both** sections.
- For numerical answers, enter the integer value.
- No calculator. Use only blank rough sheets.
- Start at your shift time. Before checking answers, fill in Part 1 of the Mock Analysis Sheet (page [[mock-analysis-sheet]]).
:::

:::note About this paper
All 75 questions are original and written for this book, in the style and difficulty mix of recent shifts: about 40% easy, 45% medium and 15% hard {{tag:rec}}. The answer key and full solutions follow the paper (page [[mock-1-solutions]]).
:::

Start time {{field:mt1-start:24}} · End time {{field:mt1-end:24}}

## Physics

@@SET Mock 1 · Physics

@@Q MT1-P01 | E | 1 | Error in density | Units
The percentage errors in measuring the mass and the side of a cube are 1% and 2%. The maximum percentage error in its density is:
(A) 7%
(B) 5%
(C) 3%
(D) 9%
@ans A
@sol $\rho = \dfrac{m}{L^3}$, so $\dfrac{\Delta\rho}{\rho} = 1\% + 3(2\%) = 7\%$.
@short —
@trap Adding without the power (3%).
@@END

@@Q MT1-P02 | E | 1 | Acceleration from position | Kinematics
The position of a particle is $x = 2t^3 - 3t^2 + 4$ (in m, $t$ in s). Its acceleration at $t = 1$ s is:
(A) 6 m/s²
(B) 0
(C) 12 m/s²
(D) −6 m/s²
@ans A
@sol $v = 6t^2 - 6t$ and $a = 12t - 6$, which is 6 m/s² at $t = 1$.
@short —
@trap $v = 0$ at $t = 1$ s. Giving the velocity instead of the acceleration.
@@END

@@Q MT1-P03 | E | 1 | Complementary angles | Projectile
Two projectiles are launched with the same speed at $30^\circ$ and $60^\circ$ to the horizontal. The ratio of their maximum heights is:
(A) $1 : 3$
(B) $1 : 1$
(C) $3 : 1$
(D) $1 : \sqrt3$
@ans A
@sol $H \propto \sin^2\theta$: $\tfrac14 : \tfrac34$.
@short —
@trap Equal ranges for complementary angles don't mean equal heights.
@@END

@@Q MT1-P04 | M | 1.5 | Static friction | Laws of motion
A 5 kg block rests on a horizontal floor ($\mu_s = 0.4$, $\mu_k = 0.3$, $g = 10$ m/s²). A horizontal force of 12 N is applied. The friction force on the block is:
(A) 12 N
(B) 20 N
(C) 15 N
(D) 0
@ans A
@sol Limiting friction is $0.4\times50 = 20$ N > 12 N, so the block stays at rest and static friction balances the push: 12 N.
@short —
@trap Using $\mu_sN$ (20 N) or $\mu_kN$ (15 N) when the block isn't sliding.
@@END

@@Q MT1-P05 | M | 1.5 | Elastic collision | Collisions
A 1 kg ball moving at 6 m/s collides head-on elastically with a stationary 2 kg ball. Their velocities after the collision are:
(A) −2 m/s and 4 m/s
(B) 2 m/s and 2 m/s
(C) 0 and 3 m/s
(D) −4 m/s and 5 m/s
@ans A
@sol $v_1 = \dfrac{1 - 2}{3}(6) = -2$ m/s; $v_2 = \dfrac{2(1)}{3}(6) = 4$ m/s.
@short Check the options: momentum is 6 in (A), (B), (C) and (D), but only (A) conserves KE ($2 + 16 = 18$ J).
@trap (B) is the perfectly inelastic case.
@@END

@@Q MT1-P06 | M | 1.5 | Axis theorems | Rotation
The moment of inertia of a uniform disc (mass $M$, radius $R$) about a tangent in its own plane is:
(A) $\tfrac54MR^2$
(B) $\tfrac32MR^2$
(C) $\tfrac14MR^2$
(D) $\tfrac34MR^2$
@ans A
@sol About a diameter: $\tfrac14MR^2$ (perpendicular-axis theorem). Parallel shift by $R$: $\tfrac14MR^2 + MR^2$.
@short —
@trap $\tfrac32MR^2$ is for a tangent **perpendicular** to the plane.
@@END

@@Q MT1-P07 | M | 1 | Escape speed scaling | Gravitation
A planet has twice Earth's radius and the same mean density. Its escape speed (Earth: 11.2 km/s) is:
(A) 22.4 km/s
(B) 11.2 km/s
(C) 15.8 km/s
(D) 44.8 km/s
@ans A
@sol $v_e = \sqrt{\dfrac{2GM}{R}}$ with $M \propto \rho R^3$, so $v_e \propto R\sqrt\rho$.
@short —
@trap Assuming the same mass (gives $11.2/\sqrt2$).
@@END

@@Q MT1-P08 | M | 1.5 | Bernoulli in a pipe | Fluids
Water flows through a horizontal pipe whose cross-section narrows from 4 cm² to 1 cm². The speed in the wide part is 1 m/s. The pressure difference between the wide and narrow parts is:
(A) 7500 Pa
(B) 15000 Pa
(C) 8000 Pa
(D) 3750 Pa
@ans A
@sol Continuity: $v_2 = 4$ m/s. $\Delta P = \tfrac12\rho(v_2^2 - v_1^2) = 500\times15$.
@short —
@trap Forgetting the $\tfrac12$ (15000 Pa).
@@END

@@Q MT1-P09 | M | 1.5 | Rods in series | Heat conduction
Two rods of equal length and cross-section, with thermal conductivities $K$ and $2K$, are joined end to end. The equivalent conductivity of the combination is:
(A) $\tfrac43K$
(B) $\tfrac32K$
(C) $3K$
(D) $\tfrac23K$
@ans A
@sol Thermal resistances add: $\dfrac{2L}{K_{eq}A} = \dfrac{L}{KA} + \dfrac{L}{2KA}$, so $K_{eq} = \dfrac{4K}{3}$.
@short Harmonic mean of $K$ and $2K$.
@trap Arithmetic mean ($\tfrac32K$) is for rods in parallel.
@@END

@@Q MT1-P10 | M | 1 | Adiabatic compression | Thermodynamics
A monatomic ideal gas ($\gamma = \tfrac53$) is compressed adiabatically to $\tfrac18$ of its volume. Its absolute temperature becomes:
(A) 4 times
(B) 8 times
(C) 2 times
(D) 16 times
@ans A
@sol $TV^{\gamma - 1}$ is constant: $T_2/T_1 = 8^{2/3} = 4$.
@short —
@trap Using the isothermal or ideal-gas-at-constant-$P$ relation (8).
@@END

@@Q MT1-P11 | M | 1.5 | γ of a mixture | Kinetic theory
A mixture contains 1 mol of helium and 1 mol of oxygen (rigid diatomic). Its $\gamma$ is:
(A) 1.50
(B) 1.67
(C) 1.40
(D) 1.33
@ans A
@sol $C_V = \dfrac{\tfrac32R + \tfrac52R}{2} = 2R$, $C_P = 3R$, $\gamma = 1.5$.
@short —
@trap Averaging the two $\gamma$ values gives 1.53, which is not correct.
@@END

@@Q MT1-P12 | M | 1 | Cut spring | SHM
A block on a spring oscillates with period $T$. The spring is cut into two equal halves and the same block is attached to one half. The new period is:
(A) $T/\sqrt2$
(B) $\sqrt2\,T$
(C) $T/2$
(D) $2T$
@ans A
@sol Each half has stiffness $2k$, so $T \propto 1/\sqrt k$ gives $T/\sqrt2$.
@short —
@trap Thinking a shorter spring is "weaker".
@@END

@@Q MT1-P13 | E | 1 | Tension and harmonics | Waves
A string fixed at both ends vibrates in its 3rd harmonic at 300 Hz. If the tension is made four times as large (same length and string), the 3rd-harmonic frequency becomes:
(A) 600 Hz
(B) 1200 Hz
(C) 300 Hz
(D) 150 Hz
@ans A
@sol $v = \sqrt{T/\mu}$ doubles, so every harmonic frequency doubles.
@short —
@trap Scaling with $T$ instead of $\sqrt T$ (1200 Hz).
@@END

@@Q MT1-P14 | E | 1 | Field and potential of a pair | Electrostatics
Charges $+q$ and $-q$ are a distance $d$ apart. At the midpoint:
(A) $E = \dfrac{8kq}{d^2}$, $V = 0$
(B) $E = 0$, $V = 0$
(C) $E = \dfrac{4kq}{d^2}$, $V = \dfrac{2kq}{d}$
(D) $E = 0$, $V = \dfrac{4kq}{d}$
@ans A
@sol The fields add (both point towards $-q$): $2\cdot\dfrac{kq}{(d/2)^2}$. The potentials cancel.
@short —
@trap Assuming $V = 0$ means $E = 0$.
@@END

@@Q MT1-P15 | E | 0.75 | Energy in a capacitor | Capacitors
A 4 μF capacitor is charged to 50 V. The energy stored is:
(A) 5 mJ
(B) 10 mJ
(C) 0.1 mJ
(D) 2.5 mJ
@ans A
@sol $\tfrac12CV^2 = \tfrac12(4\times10^{-6})(2500) = 5\times10^{-3}$ J.
@short —
@trap Forgetting the $\tfrac12$ (10 mJ).
@@END

@@Q MT1-P16 | E | 1 | Meter bridge | Current electricity
In a meter bridge, an unknown resistance $X$ is in the left gap and 30 Ω in the right gap. The balance point is 40 cm from the left end. $X$ is:
(A) 20 Ω
(B) 45 Ω
(C) 12 Ω
(D) 30 Ω
@ans A
@sol $\dfrac{X}{30} = \dfrac{40}{60}$.
@short —
@trap Using $\tfrac{60}{40}$ (45 Ω).
@@END

@@Q MT1-P17 | E | 0.75 | Field of a long wire | Magnetism
The magnetic field 5 cm from a long straight wire carrying 10 A is:
(A) $4\times10^{-5}$ T
(B) $2\times10^{-5}$ T
(C) $4\times10^{-4}$ T
(D) $8\times10^{-5}$ T
@ans A
@sol $\dfrac{\mu_0I}{2\pi r} = \dfrac{2\times10^{-7}\times10}{0.05}$.
@short —
@trap Using $r$ in cm.
@@END

@@Q MT1-P18 | E | 0.75 | Motional emf | EMI
A 0.5 m rod moves at 4 m/s perpendicular to a 0.2 T magnetic field, with the rod, velocity and field mutually perpendicular. The induced emf is:
(A) 0.4 V
(B) 0.1 V
(C) 4 V
(D) 1.6 V
@ans A
@sol $Blv = 0.2\times0.5\times4$.
@short —
@trap —
@@END

@@Q MT1-P19 | E | 0.5 | E–B relation | EM waves
An electromagnetic wave in vacuum has electric-field amplitude 30 V/m. Its magnetic-field amplitude is:
(A) $10^{-7}$ T
(B) $9\times10^{9}$ T
(C) $3\times10^{-7}$ T
(D) $10^{-6}$ T
@ans A
@sol $B_0 = \dfrac{E_0}{c} = \dfrac{30}{3\times10^8}$.
@short —
@trap Multiplying by $c$.
@@END

@@Q MT1-P20 | E | 0.5 | NAND gate | Electronic devices
The output of a NAND gate is 0 when:
(A) both inputs are 1
(B) both inputs are 0
(C) exactly one input is 1
(D) at least one input is 0
@ans A
@sol NAND $= \overline{A\cdot B}$, which is 0 only when $A = B = 1$.
@short —
@trap —
@@END

### Physics · Section B (numerical value)

@@Q MT1-P21 | E | 1 | Thin prism | Optics · NV
A thin prism has refracting angle 5° and refractive index 1.6. Find its angle of minimum deviation in degrees.
@ans 3
@sol $\delta = (n - 1)A = 0.6\times5$.
@short —
@trap —
@@END

@@Q MT1-P22 | E | 0.75 | Number of lines | Atoms · NV
Electrons in a sample of hydrogen atoms are excited to $n = 4$. Find the maximum number of spectral lines emitted as they return to the ground state.
@ans 6
@sol $\dfrac{n(n - 1)}{2} = 6$.
@short —
@trap Counting only the lines that end on $n = 1$ (3).
@@END

@@Q MT1-P23 | M | 1 | Half-life from activity | Nuclei · NV
The activity of a sample falls from 800 to 50 counts per minute in 20 hours. Find the half-life in hours.
@ans 5
@sol $\tfrac{50}{800} = \tfrac1{16}$, which is 4 half-lives in 20 h.
@short —
@trap —
@@END

@@Q MT1-P24 | M | 1 | Angular momentum conservation | Rotation · NV
A disc spins freely at 30 rad/s about its axis. An identical disc, initially at rest, is gently placed on it coaxially, and the two move together. Find the final angular speed in rad/s.
@ans 15
@sol $I\omega = 2I\omega'$.
@short —
@trap Using energy conservation (gives $30/\sqrt2$). Energy is lost as the discs slip against each other.
@@END

@@Q MT1-P25 | M | 1.5 | Cells in parallel | Current electricity · NV
Cells of emf 2 V and 4 V, each with internal resistance 1 Ω, are connected in parallel with like terminals together. Find the emf of the equivalent cell in volts.
@ans 3
@sol $\varepsilon_{eq} = \dfrac{\varepsilon_1/r_1 + \varepsilon_2/r_2}{1/r_1 + 1/r_2} = \dfrac{2 + 4}{2}$.
@short Equal internal resistances: simple average.
@trap Adding the emfs (6 V) as if in series.
@@END

## Chemistry

@@SET Mock 1 · Chemistry

@@Q MT1-C01 | E | 0.75 | Molarity | Basic concepts
4 g of NaOH is dissolved to make 500 mL of solution. The molarity is:
(A) 0.2 M
(B) 0.1 M
(C) 0.4 M
(D) 2 M
@ans A
@sol $\dfrac{4/40}{0.5} = 0.2$ M.
@short —
@trap Forgetting to convert mL to L.
@@END

@@Q MT1-C02 | E | 0.75 | Bohr energy for He⁺ | Atomic structure
The energy of the electron in the second orbit of $\ce{He+}$ is:
(A) −13.6 eV
(B) −3.4 eV
(C) −54.4 eV
(D) −6.8 eV
@ans A
@sol $-13.6\dfrac{Z^2}{n^2} = -13.6\cdot\dfrac44$.
@short —
@trap Using $Z = 1$ (−3.4 eV).
@@END

@@Q MT1-C03 | M | 1 | Bond order of an ion | Bonding
The bond order of $\ce{O2+}$ is:
(A) 2.5
(B) 2
(C) 1.5
(D) 3
@ans A
@sol $\ce{O2}$ has bond order 2. $\ce{O2+}$ loses an antibonding $\pi^*$ electron, which raises the bond order to 2.5.
@short —
@trap Removing a bonding electron (1.5).
@@END

@@Q MT1-C04 | E | 0.75 | VSEPR shape | Bonding
The shape of $\ce{SF4}$ is:
(A) see-saw
(B) tetrahedral
(C) square planar
(D) trigonal pyramidal
@ans A
@sol 4 bond pairs + 1 lone pair: trigonal bipyramidal arrangement, with the lone pair equatorial.
@short —
@trap —
@@END

@@Q MT1-C05 | M | 1.5 | ΔH − ΔU | Thermodynamics
For $\ce{N2(g) + 3H2(g) -> 2NH3(g)}$ at 298 K, $\Delta H - \Delta U$ is approximately:
(A) −4.96 kJ
(B) +4.96 kJ
(C) −2.48 kJ
(D) 0
@ans A
@sol $\Delta n_g = 2 - 4 = -2$, so $\Delta H - \Delta U = -2RT = -2\times8.314\times298$ J.
@short —
@trap Sign of $\Delta n_g$, or taking $\Delta n = -1$.
@@END

@@Q MT1-C06 | E | 0.75 | Boiling-point elevation | Solutions
Which 0.1 m aqueous solution has the highest boiling point?
(A) NaCl
(B) glucose
(C) $\ce{CaCl2}$
(D) urea
@ans C
@sol $i$ values are 2, 1, 3 and 1, so $\ce{CaCl2}$ has the largest elevation.
@short —
@trap —
@@END

@@Q MT1-C07 | E | 0.75 | Kp and Kc | Equilibrium
For $\ce{PCl5(g) <=> PCl3(g) + Cl2(g)}$:
(A) $K_p = K_cRT$
(B) $K_p = K_c$
(C) $K_p = K_c/(RT)$
(D) $K_p = K_c(RT)^2$
@ans A
@sol $\Delta n_g = 2 - 1 = 1$.
@short —
@trap —
@@END

@@Q MT1-C08 | M | 1 | Common-ion effect | Ionic equilibrium
The solubility of AgCl ($K_{sp} = 1.8\times10^{-10}$) in 0.1 M NaCl is:
(A) $1.8\times10^{-9}$ M
(B) $1.34\times10^{-5}$ M
(C) $1.8\times10^{-10}$ M
(D) $1.8\times10^{-11}$ M
@ans A
@sol $s = \dfrac{K_{sp}}{[\ce{Cl-}]} = \dfrac{1.8\times10^{-10}}{0.1}$.
@short —
@trap $1.34\times10^{-5}$ M is the solubility in pure water.
@@END

@@Q MT1-C09 | E | 0.5 | Faraday's law | Electrochemistry
The charge needed to deposit 1 mol of Al from $\ce{Al^3+}$ is:
(A) 3 F
(B) 1 F
(C) 2 F
(D) F/3
@ans A
@sol $\ce{Al^3+ + 3e- -> Al}$.
@short —
@trap —
@@END

@@Q MT1-C10 | E | 0.75 | Zero-order half-life | Kinetics
For a zero-order reaction, the half-life is:
(A) directly proportional to the initial concentration
(B) independent of the initial concentration
(C) inversely proportional to the initial concentration
(D) proportional to the square of the initial concentration
@ans A
@sol $t_{1/2} = \dfrac{[A]_0}{2k}$.
@short —
@trap (B) is true for first order.
@@END

@@Q MT1-C11 | E | 0.5 | Isoelectronic radii | Periodicity
Which ion has the largest radius?
(A) $\ce{N^3-}$
(B) $\ce{O^2-}$
(C) $\ce{F-}$
(D) $\ce{Na+}$
@ans A
@sol Isoelectronic ions (10 electrons): the lowest nuclear charge gives the largest ion.
@short —
@trap —
@@END

@@Q MT1-C12 | E | 0.75 | Basicity of an oxoacid | p-Block
The basicity of $\ce{H3PO3}$ is:
(A) 2
(B) 3
(C) 1
(D) 0
@ans A
@sol $\ce{H3PO3}$ has two P–OH bonds and one P–H bond. Only the OH hydrogens are ionisable.
@short —
@trap Counting all three hydrogens.
@@END

@@Q MT1-C13 | E | 0.5 | Xenon fluoride shapes | p-Block
Which xenon compound is square planar?
(A) $\ce{XeF4}$
(B) $\ce{XeF2}$
(C) $\ce{XeO3}$
(D) $\ce{XeF6}$
@ans A
@sol $\ce{XeF4}$: 4 bond pairs + 2 lone pairs, with $sp^3d^2$ hybridisation.
@short —
@trap —
@@END

@@Q MT1-C14 | E | 0.75 | Colourless ion | d-Block
Which ion is colourless in aqueous solution?
(A) $\ce{Sc^3+}$
(B) $\ce{Ti^3+}$
(C) $\ce{Cu^2+}$
(D) $\ce{Fe^2+}$
@ans A
@sol $\ce{Sc^3+}$ is $d^0$, so no d–d transition is possible.
@short —
@trap —
@@END

@@Q MT1-C15 | M | 1 | IUPAC name | Coordination
The IUPAC name of $\ce{K3[Fe(CN)6]}$ is:
(A) potassium hexacyanidoferrate(III)
(B) potassium hexacyanidoferrate(II)
(C) potassium hexacyanidoiron(III)
(D) tripotassium hexacyanidoferrate(II)
@ans A
@sol Fe is +3 ($3 + x - 6 = 0$), and an anionic complex takes the "-ate" ending (ferrate).
@short —
@trap Using "iron" in an anionic complex.
@@END

@@Q MT1-C16 | E | 0.5 | Carbocation stability | GOC
Which carbocation is the most stable?
(A) $\ce{(CH3)3C+}$
(B) $\ce{CH3CH2+}$
(C) $\ce{CH3+}$
(D) $\ce{(CH3)2CH+}$
@ans A
@sol $3^\circ$: the most hyperconjugation and $+I$ stabilisation.
@short —
@trap —
@@END

@@Q MT1-C17 | E | 0.75 | Peroxide effect | Hydrocarbons
HBr adds to propene in the presence of benzoyl peroxide. The major product is:
(A) 1-bromopropane
(B) 2-bromopropane
(C) 1,2-dibromopropane
(D) propane
@ans A
@sol Free-radical (anti-Markovnikov) addition. It applies to HBr only.
@short —
@trap Markovnikov's product (2-bromopropane) forms without peroxide.
@@END

@@Q MT1-C18 | E | 0.75 | SN2 reactivity | Haloalkanes
Which reacts fastest by the SN2 mechanism?
(A) $\ce{CH3Br}$
(B) $\ce{(CH3)3CBr}$
(C) $\ce{(CH3)2CHBr}$
(D) $\ce{CH3CH2Br}$
@ans A
@sol SN2 is fastest for the least hindered substrate (methyl).
@short —
@trap Using the SN1 order.
@@END

@@Q MT1-C19 | E | 0.75 | Cannizzaro reaction | Carbonyls
Which compound undergoes the Cannizzaro reaction?
(A) HCHO
(B) $\ce{CH3CHO}$
(C) $\ce{CH3COCH3}$
(D) $\ce{CH3CH2CHO}$
@ans A
@sol Cannizzaro requires an aldehyde without α-hydrogens.
@short —
@trap Aldehydes with α-H undergo aldol condensation instead.
@@END

@@Q MT1-C20 | E | 0.5 | Carbylamine test | Amines
Which amine gives the carbylamine test?
(A) $\ce{CH3NH2}$
(B) $\ce{(CH3)2NH}$
(C) $\ce{(CH3)3N}$
(D) $\ce{C6H5N(CH3)2}$
@ans A
@sol Only primary amines form isocyanides.
@short —
@trap —
@@END

### Chemistry · Section B (numerical value)

@@Q MT1-C21 | M | 1 | Tetrahedral nickel complex | Coordination · NV
How many unpaired electrons are in $\ce{[NiCl4]^2-}$?
@ans 2
@sol $\ce{Ni^2+}$ is $d^8$. Tetrahedral, weak-field $\ce{Cl-}$: $e^4t_2^4$ has 2 unpaired electrons.
@short —
@trap Using square planar (0 unpaired), which applies to $\ce{[Ni(CN)4]^2-}$.
@@END

@@Q MT1-C22 | E | 0.75 | Half-life from completion | Kinetics · NV
A first-order reaction is 75% complete in 60 min. Find its half-life in minutes.
@ans 30
@sol 75% complete means 2 half-lives.
@short —
@trap —
@@END

@@Q MT1-C23 | E | 0.5 | pH of a base | Ionic equilibrium · NV
Find the pH of 0.001 M NaOH at 25 °C.
@ans 11
@sol pOH = 3, so pH = 11.
@short —
@trap Answering 3.
@@END

@@Q MT1-C24 | E | 0.5 | Combustion stoichiometry | Basic concepts · NV
Find the mass of $\ce{CO2}$ (in g) formed by complete combustion of 16 g of methane.
@ans 44
@sol 1 mol $\ce{CH4}$ gives 1 mol $\ce{CO2}$.
@short —
@trap —
@@END

@@Q MT1-C25 | E | 0.75 | Chiral centres | Biomolecules · NV
How many chiral carbon atoms are there in open-chain D-glucose?
@ans 4
@sol C-2, C-3, C-4 and C-5.
@short —
@trap Counting C-1 (the aldehyde carbon) or C-6.
@@END

## Mathematics

@@SET Mock 1 · Mathematics

@@Q MT1-M01 | E | 0.5 | Composition | Functions
If $f(x) = 2x + 3$ and $g(x) = x^2$, then $(f\circ g)(2)$ is:
(A) 11
(B) 49
(C) 7
(D) 14
@ans A
@sol $f(g(2)) = f(4) = 11$.
@short —
@trap $(g\circ f)(2) = 49$.
@@END

@@Q MT1-M02 | E | 0.75 | Counting relations | Sets & relations
The number of reflexive relations on a set with 3 elements is:
(A) 64
(B) 512
(C) 8
(D) 27
@ans A
@sol $2^{n^2 - n} = 2^6$.
@short —
@trap $2^{9} = 512$ counts all relations.
@@END

@@Q MT1-M03 | E | 0.5 | Modulus of a power | Complex numbers
$\lvert(1 + i)^8\rvert$ equals:
(A) 16
(B) 8
(C) 256
(D) 4
@ans A
@sol $(\sqrt2)^8 = 16$.
@short —
@trap —
@@END

@@Q MT1-M04 | E | 0.75 | Symmetric functions of roots | Quadratics
If $\alpha$ and $\beta$ are the roots of $x^2 - 5x + 6 = 0$, then $\alpha^2 + \beta^2$ is:
(A) 13
(B) 25
(C) 37
(D) 11
@ans A
@sol $(\alpha + \beta)^2 - 2\alpha\beta = 25 - 12$.
@short —
@trap —
@@END

@@Q MT1-M05 | E | 1 | Inverse of a 2×2 matrix | Matrices
If $A = \begin{bmatrix}2 & 1\\1 & 1\end{bmatrix}$, then $A^{-1}$ is:
(A) $\begin{bmatrix}1 & -1\\-1 & 2\end{bmatrix}$
(B) $\begin{bmatrix}1 & 1\\1 & 2\end{bmatrix}$
(C) $\begin{bmatrix}2 & -1\\-1 & 1\end{bmatrix}$
(D) $\begin{bmatrix}-1 & 1\\1 & -2\end{bmatrix}$
@ans A
@sol $\lvert A\rvert = 1$; swap the diagonal and negate the off-diagonal entries.
@short Check: $A\cdot A^{-1} = I$ for (A).
@trap (C) negates the off-diagonal entries but forgets to swap the diagonal.
@@END

@@Q MT1-M06 | M | 2 | Infinitely many solutions | Determinants
The system $x + y + z = 3$, $x + 2y + 3z = 6$, $x + 3y + kz = 9$ has infinitely many solutions for $k$ equal to:
(A) 5
(B) 3
(C) 4
(D) 6
@ans A
@sol The determinant is $k - 5$. At $k = 5$, subtracting consecutive equations gives $y + 2z = 3$ twice, so the system is consistent with infinitely many solutions.
@short —
@trap Stopping at $\lvert A\rvert = 0$ without checking consistency.
@@END

@@Q MT1-M07 | M | 1 | At least one | P&C
A committee of 3 is chosen from 5 men and 4 women. The number of committees with at least one woman is:
(A) 74
(B) 84
(C) 70
(D) 64
@ans A
@sol Total minus all-men: ${}^9C_3 - {}^5C_3 = 84 - 10$.
@short —
@trap Computing ${}^4C_1\cdot{}^8C_2 = 112$ counts some committees more than once.
@@END

@@Q MT1-M08 | E | 0.75 | Coefficient | Binomial
The coefficient of $x^3$ in $(1 + 2x)^5$ is:
(A) 80
(B) 40
(C) 10
(D) 160
@ans A
@sol ${}^5C_3\cdot2^3 = 10\cdot8$.
@short —
@trap Forgetting $2^3$.
@@END

@@Q MT1-M09 | E | 0.75 | AP sum | Sequences
The sum of the first 20 terms of $3, 7, 11, \dots$ is:
(A) 820
(B) 800
(C) 840
(D) 780
@ans A
@sol $S_{20} = 10[6 + 19(4)] = 820$.
@short —
@trap —
@@END

@@Q MT1-M10 | E | 0.75 | 1^∞ form | Limits
$\displaystyle\lim_{x\to\infty}\left(1 + \frac2x\right)^x$ equals:
(A) $e^2$
(B) $e$
(C) $2e$
(D) $\sqrt e$
@ans A
@sol $e^{\lim x\cdot(2/x)} = e^2$.
@short —
@trap Answering 1 ($1^\infty$ is indeterminate).
@@END

@@Q MT1-M11 | E | 0.75 | Continuity | Continuity
$f(x) = \dfrac{\sin3x}{x}$ for $x \ne 0$ and $f(0) = k$. $f$ is continuous at 0 when $k$ is:
(A) 3
(B) 1
(C) $\tfrac13$
(D) 0
@ans A
@sol $\lim_{x\to0}\dfrac{\sin3x}{x} = 3$.
@short —
@trap —
@@END

@@Q MT1-M12 | E | 1 | Decreasing interval | Applications of derivatives
$f(x) = x^3 - 3x$ is decreasing on:
(A) $(-1, 1)$
(B) $(1, \infty)$
(C) $(-\infty, -1)$
(D) $(0, 3)$
@ans A
@sol $f'(x) = 3(x^2 - 1) < 0$ for $\lvert x\rvert < 1$.
@short —
@trap —
@@END

@@Q MT1-M13 | E | 1 | Integration by parts | Integrals
$\displaystyle\int xe^x\,dx$ equals:
(A) $(x - 1)e^x + C$
(B) $(x + 1)e^x + C$
(C) $xe^x + C$
(D) $\tfrac12x^2e^x + C$
@ans A
@sol $xe^x - \int e^x\,dx$.
@short Differentiate the options: only (A) gives $xe^x$.
@trap —
@@END

@@Q MT1-M14 | E | 0.75 | Odd functions | Definite integrals
$\displaystyle\int_{-1}^{1}(x^3 + x\cos x + 1)\,dx$ equals:
(A) 2
(B) 0
(C) 1
(D) 4
@ans A
@sol $x^3$ and $x\cos x$ are odd, so they integrate to 0 on $[-1, 1]$. What remains is $\int_{-1}^11\,dx = 2$.
@short —
@trap Declaring the whole integrand odd (0).
@@END

@@Q MT1-M15 | E | 0.75 | Integrating factor | Differential equations
The integrating factor of $\dfrac{dy}{dx} + y\tan x = \sec x$ is:
(A) $\sec x$
(B) $\cos x$
(C) $e^{\tan x}$
(D) $\tan x$
@ans A
@sol $e^{\int\tan x\,dx} = e^{\ln\sec x}$.
@short —
@trap —
@@END

@@Q MT1-M16 | M | 1 | Distance between parallel lines | Straight lines
The distance between $3x + 4y = 5$ and $6x + 8y = 20$ is:
(A) 1
(B) 3
(C) $\tfrac32$
(D) 2
@ans A
@sol The second line is $3x + 4y = 10$, so $d = \dfrac{\lvert10 - 5\rvert}{5} = 1$.
@short —
@trap Not making the coefficients equal first (gives 3).
@@END

@@Q MT1-M17 | E | 0.75 | Centre and radius | Circles
The circle $x^2 + y^2 - 4x + 6y - 12 = 0$ has:
(A) centre $(2, -3)$, radius 5
(B) centre $(-2, 3)$, radius 5
(C) centre $(2, -3)$, radius $\sqrt{12}$
(D) centre $(4, -6)$, radius 5
@ans A
@sol $g = -2$ and $f = 3$, so the centre is $(2, -3)$ and $r = \sqrt{4 + 9 + 12} = 5$.
@short —
@trap Sign of the centre.
@@END

@@Q MT1-M18 | E | 0.75 | Latus rectum | Ellipse
The length of the latus rectum of $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ is:
(A) $\tfrac{32}{5}$
(B) $\tfrac{25}{2}$
(C) $\tfrac{16}{5}$
(D) $\tfrac85$
@ans A
@sol $\dfrac{2b^2}{a} = \dfrac{32}{5}$.
@short —
@trap Using $\dfrac{b^2}{a}$ (half the length).
@@END

@@Q MT1-M19 | E | 0.75 | Angle between vectors | Vectors
The angle between $\hat i + \hat j + \hat k$ and $\hat i - \hat j + \hat k$ is:
(A) $\cos^{-1}\tfrac13$
(B) $\tfrac\pi3$
(C) $\tfrac\pi2$
(D) $\cos^{-1}\tfrac23$
@ans A
@sol $\cos\theta = \dfrac{1 - 1 + 1}{\sqrt3\sqrt3}$.
@short —
@trap —
@@END

@@Q MT1-M20 | M | 1 | Conditional probability with dice | Probability
A die is thrown twice. Given that the first throw is even, the probability that the sum is 8 is:
(A) $\tfrac16$
(B) $\tfrac{5}{36}$
(C) $\tfrac1{12}$
(D) $\tfrac13$
@ans A
@sol Of 18 outcomes with an even first throw, $(2, 6)$, $(4, 4)$ and $(6, 2)$ give sum 8: $\tfrac3{18}$.
@short —
@trap $\tfrac5{36}$ is the unconditional probability.
@@END

### Mathematics · Section B (numerical value)

@@Q MT1-M21 | M | 1.5 | Angle between lines | 3D · NV
Find the angle (in degrees) between lines with direction ratios $(1, 1, 2)$ and $(\sqrt3 - 1, -\sqrt3 - 1, 4)$.
@ans 60
@sol Dot product: $\sqrt3 - 1 - \sqrt3 - 1 + 8 = 6$. Magnitudes $\sqrt6$ and $\sqrt{24}$: $\cos\theta = \dfrac{6}{12} = \dfrac12$.
@short —
@trap —
@@END

@@Q MT1-M22 | E | 0.75 | Variance of naturals | Statistics · NV
If $\sigma^2$ is the variance of $1, 2, \dots, 10$, find $4\sigma^2$.
@ans 33
@sol $\sigma^2 = \dfrac{n^2 - 1}{12} = \dfrac{99}{12}$.
@short —
@trap —
@@END

@@Q MT1-M23 | M | 1 | Perpendicular vectors | Vectors · NV
If $\lvert\vec a\rvert = 3$, $\lvert\vec b\rvert = 4$ and $\lvert\vec a + \vec b\rvert = 5$, find $\lvert\vec a - \vec b\rvert^2$.
@ans 25
@sol $25 = 9 + 16 + 2\,\vec a\cdot\vec b$, so $\vec a\cdot\vec b = 0$ and $\lvert\vec a - \vec b\rvert^2 = 25$.
@short —
@trap —
@@END

@@Q MT1-M24 | E | 0.75 | Maximum of a trig expression | Trigonometry · NV
Find the maximum value of $5\sin x + 12\cos x + 7$.
@ans 20
@sol $\sqrt{25 + 144} + 7$.
@short —
@trap —
@@END

@@Q MT1-M25 | M | 1 | Greatest-integer integral | Definite integrals · NV
Find $\displaystyle\int_0^3[x]\,dx$, where $[x]$ is the greatest integer $\le x$.
@ans 3
@sol $0 + 1 + 2 = 3$.
@short —
@trap —
@@END

## Answer Key & Solutions {#mock-1-solutions}

@@ANSWERKEY

:::mock Score yourself
Physics {{field:mt1-p:16}} / 100 · Chemistry {{field:mt1-c:16}} / 100 · Maths {{field:mt1-m:16}} / 100 · **Total** {{field:mt1-t:18}} / 300
Now complete the Mock Analysis Sheet (page [[mock-analysis-sheet]]) before reading the solutions.
:::

@@SOLUTIONS
