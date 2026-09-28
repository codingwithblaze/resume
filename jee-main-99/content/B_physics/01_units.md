# Units & Measurements {#p01}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy
Priority | Must-do
NCERT | Class 11 · Ch 1
Study time | ~6 hours
:::

## Concept summary

- Every physical quantity = **numerical value × unit**. The SI system has **7 base units**. Everything else is derived.
- **Dimensions** express a quantity in terms of $[M]$, $[L]$, $[T]$, $[A]$, $[K]$, $[\text{mol}]$, $[\text{cd}]$. They are used to check equations, derive relations and convert units.
- **Significant figures** record how precisely something was measured. **Errors** measure how far a measurement may be from the true value.
- JEE Main asks almost only four things here: *dimensions of an unfamiliar constant*, *error propagation*, *significant figures / rounding*, and *instrument readings* (Vernier, screw gauge; see Unit 20).

## Core theory

### SI base units

| Quantity | Unit | Symbol | Dimension |
|---|---|---|---|
| Length | metre | m | $[L]$ |
| Mass | kilogram | kg | $[M]$ |
| Time | second | s | $[T]$ |
| Electric current | ampere | A | $[A]$ |
| Thermodynamic temperature | kelvin | K | $[K]$ |
| Amount of substance | mole | mol | $[\text{mol}]$ |
| Luminous intensity | candela | cd | $[\text{cd}]$ |

Plane angle (radian) and solid angle (steradian) are **dimensionless**, but they do have units. Since the 2019 SI revision, base units are defined by fixing exact values of constants: $h$, $e$, $k_B$, $N_A$, $c$ and others.

### Dimensions you must know by heart

| Quantity | Dimension | Quantity | Dimension |
|---|---|---|---|
| Force | $[MLT^{-2}]$ | Pressure, stress, modulus, energy density | $[ML^{-1}T^{-2}]$ |
| Work, energy, torque | $[ML^2T^{-2}]$ | Power | $[ML^2T^{-3}]$ |
| Momentum, impulse | $[MLT^{-1}]$ | Angular momentum, $h$ | $[ML^2T^{-1}]$ |
| Gravitational constant $G$ | $[M^{-1}L^3T^{-2}]$ | Surface tension, spring constant | $[MT^{-2}]$ |
| Coefficient of viscosity $\eta$ | $[ML^{-1}T^{-1}]$ | Moment of inertia | $[ML^2]$ |
| Charge | $[AT]$ | Potential (voltage) | $[ML^2T^{-3}A^{-1}]$ |
| Resistance | $[ML^2T^{-3}A^{-2}]$ | Capacitance | $[M^{-1}L^{-2}T^4A^2]$ |
| Inductance | $[ML^2T^{-2}A^{-2}]$ | Magnetic field $B$ | $[MT^{-2}A^{-1}]$ |
| Permittivity $\varepsilon_0$ | $[M^{-1}L^{-3}T^4A^2]$ | Permeability $\mu_0$ | $[MLT^{-2}A^{-2}]$ |
| Electric field | $[MLT^{-3}A^{-1}]$ | Magnetic flux | $[ML^2T^{-2}A^{-1}]$ |
| Specific heat | $[L^2T^{-2}K^{-1}]$ | Latent heat | $[L^2T^{-2}]$ |
| Thermal conductivity | $[MLT^{-3}K^{-1}]$ | Boltzmann constant | $[ML^2T^{-2}K^{-1}]$ |

:::shortcut Build dimensions from a defining equation, never from memory alone
Unknown constant? Write the simplest equation it appears in and solve for it.
$\varepsilon_0$: from $F = \dfrac{q^2}{4\pi\varepsilon_0 r^2}$ we get $[\varepsilon_0] = \dfrac{[A^2T^2]}{[MLT^{-2}][L^2]} = [M^{-1}L^{-3}T^4A^2]$.
$B$: from $F = qvB$. $L$: from $\varepsilon = L\,dI/dt$. $\eta$: from $F = 6\pi\eta r v$.
**Time saved:** 30–60 s per question, with far fewer memory errors.
:::

### Uses of dimensional analysis

1. **Checking** an equation: every added or subtracted term must have the same dimensions (principle of homogeneity).
2. **Deriving** a relation when the quantity depends on 3 others as a product of powers.
3. **Converting units:** $n_2 = n_1\left[\dfrac{M_1}{M_2}\right]^a\left[\dfrac{L_1}{L_2}\right]^b\left[\dfrac{T_1}{T_2}\right]^c$ for a quantity of dimension $[M^aL^bT^c]$.

:::trap Limitations examiners test
Dimensional analysis **cannot**: find dimensionless constants ($2\pi$, $\tfrac12$); derive relations that involve sums ($s = ut + \tfrac12at^2$ as a whole) or trig/log/exp functions; tell apart quantities with the same dimensions (work vs torque). Arguments of $\sin$, $\log$, $e^{x}$ **must be dimensionless**. That's often the key to the whole question.
:::

### Significant figures

- All non-zero digits count. Zeros **between** non-zeros count. **Leading** zeros never count ($0.00520$ has 3). **Trailing zeros after a decimal point** count ($2.50$ has 3).
- Trailing zeros in an integer without a decimal point are ambiguous. Use scientific notation: $4.50\times10^3$ has 3.
- **Multiplication/division:** the result has as many s.f. as the *least* precise factor.
- **Addition/subtraction:** the result has as many *decimal places* as the term with the fewest decimal places.
- **Rounding:** if the digit to drop is > 5, round up; if < 5, leave it; if exactly 5 (followed by nothing), make the preceding digit **even**.

### Errors

:::formula Error formulas
| Operation | Maximum error |
|---|---|
| $Z = A \pm B$ | $\Delta Z = \Delta A + \Delta B$ |
| $Z = AB$ or $A/B$ | $\dfrac{\Delta Z}{Z} = \dfrac{\Delta A}{A} + \dfrac{\Delta B}{B}$ |
| $Z = \dfrac{A^pB^q}{C^r}$ | $\dfrac{\Delta Z}{Z} = p\dfrac{\Delta A}{A} + q\dfrac{\Delta B}{B} + r\dfrac{\Delta C}{C}$ |
| $n$ readings | mean $\bar a = \dfrac{\sum a_i}{n}$, mean absolute error $\overline{\Delta a} = \dfrac{\sum|a_i - \bar a|}{n}$ |
| Relative / percentage error | $\delta a = \dfrac{\overline{\Delta a}}{\bar a}$, percentage $= \delta a\times100\%$ |

Errors always **add**, even in subtraction and division. That's the maximum-error convention used in JEE.
:::

:::shortcut Percentage error of a formula in one line
$g = 4\pi^2 L/T^2$: %error in $g$ = %$L$ + **2**×%$T$. Multiply each percentage by the **absolute value of its power** and add. Constants ($4\pi^2$) contribute nothing.
**When NOT to use:** when a quantity appears in a sum, e.g. $Z = \dfrac{A}{A+B}$. There you must differentiate properly.
:::

### Instruments (details in Unit 20, page [[p20]])

- **Vernier callipers:** least count $= 1\ \text{MSD} - 1\ \text{VSD}$. If $N$ VSD $= (N-1)$ MSD, then LC $= \text{MSD}/N$.
- **Screw gauge:** least count $= \dfrac{\text{pitch}}{\text{number of circular-scale divisions}}$.
- **Zero error:** true reading = observed reading − (zero error), with the zero error's sign included.

## Frequently tested concepts & question patterns

:::pyq Recurring structures (2024–2026 papers)
1. **"Find the dimensions of $a$, $b$ in $X = \dots$"** Van der Waals-type equations, $y = A\sin(\omega t - kx)$, $P = \dfrac{a - t^2}{bx}$. Use homogeneity term by term.
2. **Combination checks:** which of these has the dimensions of speed / time / energy? ($1/\sqrt{\mu_0\varepsilon_0}$, $RC$, $L/R$, $\sqrt{LC}$, $hc/\lambda$, $\varepsilon_0E^2$, $B^2/\mu_0$)
3. **Error in a derived quantity** (density of a sphere, $g$ from a pendulum, Young's modulus): the power rule.
4. **Significant-figure arithmetic** and rounding.
5. **Vernier/screw-gauge reading with zero error**, sometimes combined with an error calculation.
6. **New unit system:** "If the units of mass, length and time are changed to…, find the new value of 1 J."
:::

## Question classification

| Type | Difficulty | Approach | Target time |
|---|---|---|---|
| Dimensions of a named quantity | E | Defining equation | 45 s |
| Dimensions of constants in an unfamiliar formula | E–M | Homogeneity, term by term | 1.5 min |
| Percentage error, power rule | E | One line | 45 s |
| Error with a sum/difference inside | M | Differentiate / add absolute errors | 2 min |
| Instrument reading + zero error | E–M | LC first, then sign of zero error | 1.5 min |
| Dimensional derivation (3 variables) | M | Solve 3 equations in $M, L, T$ | 2 min |

**Selection rule:** almost always Round-1 questions. Skip only if the unfamiliar formula is very long.

## Common mistakes

:::trap Mistake alerts
- Treating an angle as having a dimension. It's dimensionless, even though it has a unit (rad).
- Subtracting errors in $A - B$. **Errors add.**
- Forgetting to multiply by the power: %error in $r^3$ is $3\times$%$r$.
- Getting the zero-error sign backwards. With the jaws closed, a reading *above* zero is a **positive** zero error, and you subtract it.
- Counting leading zeros as significant.
- Rounding intermediate results. Keep one extra digit and round at the end.
:::

## Practice questions

@@SET P01 · Practice

@@Q P01-01 | E | 1 | Dimensions of energy density | Basic
The dimensions of $\tfrac12\varepsilon_0E^2$ ($\varepsilon_0$ = permittivity of free space, $E$ = electric field) are:
(A) $[MLT^{-2}]$
(B) $[ML^{-1}T^{-2}]$
(C) $[ML^2T^{-2}]$
(D) $[ML^{-2}T^{-1}]$
@ans B
@sol $\tfrac12\varepsilon_0E^2$ is the **energy per unit volume** of an electric field: $[ML^2T^{-2}]/[L^3] = [ML^{-1}T^{-2}]$.
@short Energy density has the dimensions of pressure. Same for $B^2/2\mu_0$.
@trap Answering the dimension of energy.
@@END

@@Q P01-02 | M | 1.5 | Homogeneity in van der Waals equation | Concept
In $\left(P + \dfrac{a}{V^2}\right)(V - b) = RT$, the dimensions of $a/b$ are those of:
(A) pressure
(B) energy
(C) force
(D) momentum
@ans B
@sol $a/V^2$ must be a pressure, so $[a] = [PV^2]$. $b$ must be a volume, so $[b] = [V]$. Then $[a/b] = [PV]$, which is energy ($PV$ has units N m$^{-2}$ × m$^3$ = J).
@short $a/b \sim PV$ → energy.
@trap Stopping at "$a$ has dimensions of $PV^2$" and choosing pressure.
@@END

@@Q P01-03 | E | 0.75 | Percentage error with powers | Speed
In $g = 4\pi^2L/T^2$, the percentage errors in $L$ and $T$ are 1% and 2%. The maximum percentage error in $g$ is:
(A) 3%
(B) 4%
(C) 5%
(D) 1%
@ans C
@sol $\dfrac{\Delta g}{g} = \dfrac{\Delta L}{L} + 2\dfrac{\Delta T}{T} = 1\% + 4\% = 5\%$.
@short Power rule: add |power| × %error.
@trap Using $-2$ and subtracting gives 3%.
@@END

@@Q P01-04 | E | 1 | Significant figures in multiplication | Basic
The product $12.5 \times 1.25$, reported to the correct number of significant figures, is:
(A) 15.625
(B) 15.63
(C) 15.6
(D) 16
@ans C
@sol Both factors have 3 s.f., so the result keeps 3 s.f.: $15.625 \to 15.6$.
@short Multiplication: keep the least number of s.f.
@trap Applying the decimal-place rule, which is for addition only.
@@END

@@Q P01-05 | M | 2 | Vernier reading with zero error | JEE
A Vernier calliper has 1 MSD = 1 mm and 10 VSD = 9 MSD. With the jaws closed, the Vernier zero lies to the **right** of the main-scale zero and the 3rd Vernier division coincides with a main-scale division. When a rod is measured, the main-scale reading is 32 mm and the 6th Vernier division coincides. The corrected diameter is:
(A) 3.29 cm
(B) 3.26 cm
(C) 3.23 cm
(D) 3.20 cm
@ans C
@sol LC $= 1\ \text{MSD} - 1\ \text{VSD} = 1 - 0.9 = 0.1$ mm. Zero error $= +3 \times 0.1 = +0.3$ mm (zero to the right means positive). Observed $= 32 + 6(0.1) = 32.6$ mm. Corrected $= 32.6 - 0.3 = 32.3$ mm $= 3.23$ cm.
@short Corrected = observed − (signed zero error).
@trap Adding the positive zero error gives 3.29 cm.
@@END

@@Q P01-06 | M | 2 | Screw gauge with zero error | JEE
A screw gauge has pitch 0.5 mm and 50 circular-scale divisions. With the studs closed, the reference line reads **+4** divisions on the circular scale. Measuring a wire, the main-scale reading is 2.5 mm and the circular-scale reading is 36. The diameter of the wire is:
(A) 2.86 mm
(B) 2.82 mm
(C) 2.90 mm
(D) 2.54 mm
@ans B
@sol LC $= 0.5/50 = 0.01$ mm. Zero error $= +4 \times 0.01 = +0.04$ mm. Observed $= 2.5 + 36(0.01) = 2.86$ mm. Corrected $= 2.86 - 0.04 = 2.82$ mm.
@short Observed − zero error.
@trap Forgetting the correction gives 2.86.
@@END

@@Q P01-07 | M | 1.5 | Conversion to a new unit system | NV
In a new system, the unit of mass is 5 kg, the unit of length is 2 m and the unit of time is 2 s. What is the numerical value of 100 J in this system?
@ans 20
@sol New energy unit $= (5\ \text{kg})(2\ \text{m})^2/(2\ \text{s})^2 = 5$ J. So 100 J $= 100/5 = 20$ new units.
@short Compute the size of the new unit, then divide.
@trap Inverting the ratio gives 500.
@@END

@@Q P01-08 | M | 2 | Dimensional derivation | Concept
The time period $T$ of oscillation of a small liquid drop depends on its density $\rho$, radius $r$ and surface tension $\sigma$. Dimensional analysis gives $T \propto$:
(A) $\sqrt{\rho r^3/\sigma}$
(B) $\sqrt{\sigma/(\rho r^3)}$
(C) $\sqrt{\rho r/\sigma}$
(D) $\rho r^3/\sigma$
@ans A
@sol Let $T = k\rho^a r^b \sigma^c$. $[\sigma] = [MT^{-2}]$. M: $a + c = 0$. L: $-3a + b = 0$. T: $-2c = 1$. So $c = -\tfrac12$, $a = \tfrac12$, $b = \tfrac32$, giving $T \propto \sqrt{\rho r^3/\sigma}$.
@short The time dimension comes only from $\sigma$, so $\sigma$ must sit under a square root in the denominator. That leaves (A) or (C), and only (A) balances $M$ and $L$.
@trap Taking $[\sigma] = [MLT^{-2}]$ (the dimensions of force).
@@END

@@Q P01-09 | M | 2 | Mean absolute error | Calc
Five measurements of a time period are 1.52 s, 1.48 s, 1.55 s, 1.45 s and 1.50 s. The period, with its mean absolute error, is:
(A) $(1.50 \pm 0.03)$ s
(B) $(1.50 \pm 0.05)$ s
(C) $(1.51 \pm 0.02)$ s
(D) $(1.50 \pm 0.10)$ s
@ans A
@sol Mean $= 7.50/5 = 1.50$ s. Deviations: 0.02, 0.02, 0.05, 0.05, 0.00. Mean absolute error $= 0.14/5 = 0.028 \approx 0.03$ s.
@short Round the error to the same decimal place as the mean.
@trap Using the largest deviation (0.05) instead of the mean deviation.
@@END

@@SET P01 · Chapter Test

@@Q P01-T1 | E | 0.75 | Speed of light from constants | Speed
The dimensions of $\mu_0\varepsilon_0$ are:
(A) $[L^2T^{-2}]$
(B) $[L^{-2}T^{2}]$
(C) $[LT^{-1}]$
(D) dimensionless
@ans B
@sol $c = 1/\sqrt{\mu_0\varepsilon_0}$, so $\mu_0\varepsilon_0 = 1/c^2$, which has dimensions $[L^{-2}T^2]$.
@short Memorise: $1/\sqrt{\mu_0\varepsilon_0}$ = speed.
@trap Answering the dimension of $c^2$.
@@END

@@Q P01-T2 | E | 0.5 | Same dimensions | Basic
Which pair has the same dimensions?
(A) torque and work
(B) momentum and impulse per unit time
(C) stress and strain
(D) power and energy
@ans A
@sol Torque ($r\times F$) and work ($F\cdot d$) are both $[ML^2T^{-2}]$. Impulse per unit time is force. Strain is dimensionless. Power is energy per unit time.
@short Same dimensions don't mean the same physical quantity: torque is a vector, work a scalar.
@trap Thinking momentum = impulse per unit time. Momentum = impulse.
@@END

@@Q P01-T3 | E | 1 | Error in a quotient | Basic
$V = (100 \pm 5)$ V and $I = (10 \pm 0.2)$ A. The percentage error in $R = V/I$ is:
(A) 3%
(B) 5%
(C) 7%
(D) 2.5%
@ans C
@sol $\dfrac{\Delta R}{R} = \dfrac{5}{100} + \dfrac{0.2}{10} = 5\% + 2\% = 7\%$.
@short Quotient: add the relative errors.
@trap Subtracting (3%).
@@END

@@Q P01-T4 | E | 0.5 | Counting significant figures | NV
How many significant figures are there in $0.007020$?
@ans 4
@sol Leading zeros don't count. 7, 0 (between non-zeros), 2 and the trailing 0 after the decimal point do: 4 s.f.
@short Start counting from the first non-zero digit.
@trap Excluding the final zero gives 3.
@@END

@@Q P01-T5 | M | 1.5 | Dimensionless combination | Concept
$E$ = energy, $J$ = angular momentum, $M$ = mass, $G$ = gravitational constant. The quantity $\dfrac{EJ^2}{M^5G^2}$ has the dimensions of:
(A) length
(B) time
(C) mass
(D) an angle (dimensionless)
@ans D
@sol $[EJ^2] = [ML^2T^{-2}][M^2L^4T^{-2}] = [M^3L^6T^{-4}]$. $[M^5G^2] = [M^5][M^{-2}L^6T^{-4}] = [M^3L^6T^{-4}]$. The ratio is dimensionless.
@short Count powers of $T$ first: numerator $T^{-4}$, denominator $T^{-4}$.
@trap Arithmetic slip in the powers of $G$.
@@END

## Answers & Solutions {#p01-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Units & Measurements
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
