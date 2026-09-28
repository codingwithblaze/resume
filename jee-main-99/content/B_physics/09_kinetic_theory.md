# Kinetic Theory of Gases {#p09}

:::stats
Typical questions | ~1 per shift
Difficulty | Easy
Priority | Must-do
NCERT | Class 11 · Ch 12
Study time | ~5 hours
:::

## Concept summary

- A gas is a huge number of point molecules in random motion. They collide elastically, and their pressure comes from momentum transfer to the walls.
- **Temperature is a measure of average translational KE:** $\langle\tfrac12mv^2\rangle = \tfrac32k_BT$, independent of the gas.
- **Equipartition:** each quadratic degree of freedom carries $\tfrac12k_BT$ on average, and that fixes $C_v$ and $\gamma$.
- The **mean free path** is the average distance between collisions.

## Formulas

:::formula Ideal gas & pressure
$$PV = nRT = Nk_BT \qquad P = \frac13\rho\,v_{rms}^2 = \frac13\frac{N}{V}m\,v_{rms}^2 \qquad P = \frac23E_{tr} \ \text{(per unit volume)}$$
$R = 8.314\ \text{J mol}^{-1}\text{K}^{-1}$, $k_B = 1.38\times10^{-23}\ \text{J K}^{-1}$, $N_A = 6.022\times10^{23}\ \text{mol}^{-1}$. Total translational KE of a gas $= \tfrac32PV = \tfrac32nRT$.
:::

:::formula Molecular speeds ($M$ = molar mass in kg/mol)
$$v_{rms} = \sqrt{\frac{3RT}{M}} \qquad v_{avg} = \sqrt{\frac{8RT}{\pi M}} \qquad v_{mp} = \sqrt{\frac{2RT}{M}}$$
$v_{rms} : v_{avg} : v_{mp} = \sqrt3 : \sqrt{8/\pi} : \sqrt2 \approx 1.73 : 1.60 : 1.41$. At the same $T$, speed $\propto 1/\sqrt M$. For one gas, speed $\propto \sqrt T$.
Average translational KE per molecule: $\tfrac32k_BT$ (about $6.2\times10^{-21}$ J at 300 K).
:::

:::formula Degrees of freedom & heat capacities
| Molecule | Translational + rotational $f$ | $U$ per mole | $C_v$ | $\gamma = 1 + 2/f$ |
|---|---|---|---|---|
| Monatomic (He, Ar) | 3 | $\tfrac32RT$ | $\tfrac32R$ | 5/3 |
| Diatomic, rigid (O₂, N₂ at room T) | 5 | $\tfrac52RT$ | $\tfrac52R$ | 7/5 |
| Diatomic with vibration (high T) | 7 | $\tfrac72RT$ | $\tfrac72R$ | 9/7 |
| Nonlinear polyatomic, rigid | 6 | $3RT$ | $3R$ | 4/3 |

Each vibrational mode contributes **2** quadratic terms (kinetic + potential), i.e. $k_BT$ per molecule.
:::

:::formula Mean free path
$$\lambda = \frac{1}{\sqrt2\,\pi d^2 n} = \frac{k_BT}{\sqrt2\,\pi d^2P}$$
$n$ = number density, $d$ = molecular diameter. At constant $T$, $\lambda \propto 1/P$. At constant $n$, $\lambda$ doesn't depend on $T$.
:::

@@GRAPH maxwell

## Standard models & assumptions

- Molecules are point masses (negligible volume), with no intermolecular forces except during collisions, and elastic collisions.
- Large number of molecules, random motion, equally likely in all directions (so $\overline{v_x^2} = \tfrac13\overline{v^2}$).

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **rms speed** at a temperature; temperature at which two gases have equal speeds.
2. **Speed ratios** (rms/avg/most probable) and scaling with $T$, $M$.
3. **Degrees of freedom → $C_v$, $C_p$, $\gamma$**, including mixtures.
4. **Pressure–KE relation**: $E = \tfrac32PV$.
5. **Mean free path** dependence on $P$, $T$, $d$.
6. **Maxwell distribution curve**: how the peak shifts with $T$ (the area stays constant).
:::

## Shortcuts

:::shortcut Equal speeds of two gases
Speeds are equal when $T/M$ is equal: $\dfrac{T_1}{M_1} = \dfrac{T_2}{M_2}$. No square roots needed.
:::

:::shortcut γ of a mixture
$\gamma_{mix} = \dfrac{\sum n_iC_{p,i}}{\sum n_iC_{v,i}}$. Never average the $\gamma$ values directly.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| rms speed / temperature scaling | E | 1 min |
| $f$ → $\gamma$, $C_v$ | E | 45 s |
| Mixture $\gamma$ | M | 1.5 min |
| Mean free path | E | 1 min |
| KE–pressure relation | E | 1 min |

## Common mistakes

:::trap Mistake alerts
- Using $M$ in g/mol inside $\sqrt{3RT/M}$. Convert to **kg/mol**.
- Using °C instead of K.
- Averaging $\gamma$ values for mixtures.
- Forgetting that vibration adds 2 (not 1) to $f$ per mode.
- Thinking $\tfrac32k_BT$ depends on the gas's molar mass. It doesn't.
:::

## Practice questions

@@SET P09 · Practice

@@Q P09-01 | E | 1 | rms speed | Calc
The rms speed of oxygen molecules ($M = 32$ g/mol) at 27 °C is about ($R = 8.314$):
(A) $484\ \text{m s}^{-1}$
(B) $342\ \text{m s}^{-1}$
(C) $1600\ \text{m s}^{-1}$
(D) $250\ \text{m s}^{-1}$
@ans A
@sol $v_{rms} = \sqrt{\dfrac{3\times8.314\times300}{0.032}} = \sqrt{2.34\times10^5} \approx 484\ \text{m s}^{-1}$.
@short $3RT \approx 7483$; $7483/0.032 \approx 233\,800$; $\sqrt{} \approx 484$.
@trap Using $M = 32$ (g) gives about 15 m/s, which isn't among the options, so re-check the units.
@@END

@@Q P09-02 | E | 1 | Equal rms speeds | NV
Find the temperature (in K) at which the rms speed of hydrogen equals that of oxygen at 47 °C.
@ans 20
@sol Equal speeds need $T/M$ equal: $\dfrac{T_{H_2}}{2} = \dfrac{320}{32} \Rightarrow T_{H_2} = 20$ K.
@short $T \propto M$ for equal speeds.
@trap Using 47 instead of 320 K.
@@END

@@Q P09-03 | E | 0.5 | Speed–temperature scaling | Speed
To double the rms speed of a gas's molecules, its absolute temperature must be:
(A) doubled
(B) quadrupled
(C) halved
(D) increased by $\sqrt2$
@ans B
@sol $v_{rms} \propto \sqrt T$, so $T \to 4T$.
@short —
@trap Doubling it.
@@END

@@Q P09-04 | E | 0.5 | γ from degrees of freedom | Speed
A gas has molecules with 6 degrees of freedom. Its $\gamma$ is:
(A) 5/3
(B) 7/5
(C) 4/3
(D) 9/7
@ans C
@sol $\gamma = 1 + 2/f = 1 + 1/3 = 4/3$.
@short —
@trap —
@@END

@@Q P09-05 | M | 1.5 | γ of a mixture | Concept
One mole of a monatomic gas is mixed with one mole of a rigid diatomic gas. $\gamma$ of the mixture is:
(A) 1.5
(B) 1.4
(C) 1.53
(D) 1.67
@ans A
@sol $C_v = \dfrac{1.5R + 2.5R}{2} = 2R$, $C_p = C_v + R = 3R$, so $\gamma = 1.5$.
@short Average $C_v$, then add $R$.
@trap Averaging the $\gamma$ values: $(1.67 + 1.4)/2 \approx 1.53$.
@@END

@@Q P09-06 | E | 1 | Translational KE from pressure | Basic
The total translational kinetic energy of the molecules of an ideal gas filling 1 m³ at a pressure of $10^5$ Pa is:
(A) $10^5$ J
(B) $1.5\times10^5$ J
(C) $3\times10^5$ J
(D) $0.67\times10^5$ J
@ans B
@sol $E = \tfrac32PV = 1.5\times10^5$ J.
@short $P = \tfrac23(E/V)$.
@trap Using $P = \tfrac13(E/V)$.
@@END

@@Q P09-07 | E | 0.5 | Mean free path vs pressure | Concept
At constant temperature, if the pressure of a gas is doubled, its mean free path:
(A) doubles
(B) halves
(C) is unchanged
(D) becomes 4 times
@ans B
@sol $\lambda = \dfrac{k_BT}{\sqrt2\pi d^2P} \propto 1/P$.
@short More molecules per volume means more frequent collisions.
@trap —
@@END

@@Q P09-08 | E | 1 | Average KE per molecule | NV
The average translational kinetic energy of a gas molecule at 300 K is $x\times10^{-21}$ J. Find $x$ to the nearest integer ($k_B = 1.38\times10^{-23}\ \text{J K}^{-1}$).
@ans 6
@sol $\tfrac32k_BT = 1.5\times1.38\times10^{-23}\times300 = 6.21\times10^{-21}$ J, so $x \approx 6$.
@short Worth memorising: about 6.2 × 10⁻²¹ J at room temperature (≈ 0.04 eV).
@trap Using $\tfrac12k_BT$ per molecule.
@@END

@@SET P09 · Chapter Test

@@Q P09-T1 | E | 0.5 | Speed ratio | Speed
The ratio $v_{rms} : v_{avg} : v_{mp}$ is:
(A) $\sqrt2 : \sqrt{8/\pi} : \sqrt3$
(B) $\sqrt3 : \sqrt{8/\pi} : \sqrt2$
(C) $\sqrt3 : \sqrt2 : \sqrt{8/\pi}$
(D) $1 : 1 : 1$
@ans B
@sol From the formulas: $\sqrt{3}$, $\sqrt{8/\pi} \approx 1.60$, $\sqrt2$.
@short rms > avg > mp.
@trap —
@@END

@@Q P09-T2 | E | 0.5 | Internal energy | Basic
The internal energy of 2 mol of a rigid diatomic ideal gas at temperature $T$ is:
(A) $3RT$
(B) $5RT$
(C) $7RT$
(D) $\tfrac52RT$
@ans B
@sol $U = n\tfrac f2RT = 2\times\tfrac52RT = 5RT$.
@short —
@trap Forgetting $n = 2$.
@@END

@@Q P09-T3 | E | 0.75 | rms speed ratio of two gases | Basic
At the same temperature, the ratio of rms speeds of $\ce{H2}$ and $\ce{O2}$ molecules is:
(A) 1 : 4
(B) 4 : 1
(C) 16 : 1
(D) 1 : 16
@ans B
@sol $v \propto 1/\sqrt M$: $\sqrt{32/2} = 4$.
@short —
@trap Inverting the ratio.
@@END

@@Q P09-T4 | E | 0.5 | Degrees of freedom | NV
How many degrees of freedom (translational + rotational) does a rigid **nonlinear** triatomic molecule have?
@ans 6
@sol 3 translational + 3 rotational = 6.
@short Linear molecules have 2 rotational degrees of freedom; nonlinear ones have 3.
@trap Answering 5 (as for a linear molecule).
@@END

@@Q P09-T5 | E | 0.75 | Gay-Lussac's law | Basic
The pressure of a gas at constant volume doubles when it is heated from 27 °C to:
(A) 54 °C
(B) 327 °C
(C) 600 °C
(D) 273 °C
@ans B
@sol $P \propto T$: $T_2 = 2\times300 = 600$ K $= 327$ °C.
@short Double the kelvin temperature, then convert back.
@trap Doubling the Celsius value.
@@END

## Answers & Solutions {#p09-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Kinetic Theory
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
