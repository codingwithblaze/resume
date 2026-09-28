# Chemical Kinetics {#c08}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 12 · Ch 3
Study time | ~7 hours
:::

## Important concepts

- **Rate** of $a\ce{A} + b\ce{B} \to c\ce{C}$: $-\dfrac1a\dfrac{d[\ce{A}]}{dt} = -\dfrac1b\dfrac{d[\ce{B}]}{dt} = \dfrac1c\dfrac{d[\ce{C}]}{dt}$.
- **Rate law** $r = k[\ce{A}]^x[\ce{B}]^y$ is **experimental**. The order $x + y$ can be zero or fractional.
- **Molecularity** is the number of species colliding in an **elementary** step (1, 2 or 3, never 0 or fractional). For complex reactions, the slowest step determines the rate law.
- **Temperature** raises the rate sharply, roughly doubling it per 10 °C rise for many reactions. Arrhenius: $k = Ae^{-E_a/RT}$.
- **Catalysts** lower $E_a$ by providing an alternative path. They don't change $\Delta H$, $\Delta G$ or $K$.
- **Collision theory:** rate $= PZ_{AB}e^{-E_a/RT}$. Only collisions with enough energy **and** the proper orientation (steric factor $P$) react.

## Formula sheet

:::formula Integrated rate laws
| Order | Integrated law | Half-life | Linear plot | Units of $k$ |
|---|---|---|---|---|
| 0 | $[\ce{A}] = [\ce{A}]_0 - kt$ | $\dfrac{[\ce{A}]_0}{2k}$ | $[\ce{A}]$ vs $t$ | mol L⁻¹ s⁻¹ |
| 1 | $k = \dfrac{2.303}{t}\log\dfrac{[\ce{A}]_0}{[\ce{A}]}$ | $\dfrac{0.693}{k}$ | $\ln[\ce{A}]$ vs $t$ (slope $-k$) | s⁻¹ |
| $n$ (general) | — | $\propto [\ce{A}]_0^{1-n}$ | — | (mol L⁻¹)$^{1-n}$ s⁻¹ |

First order: time for 99.9% completion ≈ $10\,t_{1/2}$; 99% ≈ $6.64\,t_{1/2}$; 75% $= 2t_{1/2}$; 87.5% $= 3t_{1/2}$.
**Gas phase** $\ce{A(g) -> B(g) + C(g)}$ (first order, total pressure $p_t$): $k = \dfrac{2.303}{t}\log\dfrac{p_0}{2p_0 - p_t}$.
**Pseudo-first-order:** acid hydrolysis of an ester in excess water; inversion of cane sugar.
:::

:::formula Temperature dependence
$$k = Ae^{-E_a/RT} \qquad \ln k = \ln A - \frac{E_a}{RT} \qquad \log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac1{T_1} - \frac1{T_2}\right)$$
Plot of $\ln k$ vs $1/T$: slope $= -E_a/R$. Fraction of molecules with energy ≥ $E_a$ is $e^{-E_a/RT}$.
Energy profile: $E_a(\text{backward}) = E_a(\text{forward}) - \Delta H$. For an exothermic reaction, the backward barrier is larger.
:::

@@GRAPH kinetics-plots

## Numerical-solving method

1. From data tables, find the order by comparing two runs where only one concentration changes: $\dfrac{r_2}{r_1} = \left(\dfrac{C_2}{C_1}\right)^x$.
2. For first-order time questions, convert "x% completed" into the fraction remaining, then use half-lives if the number is a power of ½.
3. For Arrhenius, use $2.303R = 19.15$ J K⁻¹ mol⁻¹ and keep $1/T$ in K⁻¹.

:::shortcut The 10-degree rule
If the rate doubles for every 10 °C rise, a rise of $\Delta T$ multiplies the rate by $2^{\Delta T/10}$. Also memorise: a rate that doubles between 300 K and 310 K corresponds to $E_a \approx 53.6$ kJ/mol.
:::

## Common traps

:::trap Mistake alerts
- Order ≠ stoichiometric coefficient (except in elementary steps).
- The half-life of a zero-order reaction **decreases** as $[\ce{A}]_0$ decreases (∝ $[\ce{A}]_0$). For first order it is independent of $[\ce{A}]_0$.
- Mixing up log and ln: $t_{1/2} = 0.693/k$ uses ln 2.
- A catalyst changes $k$ (and $E_a$), but **not** $K_{eq}$.
- Rate-of-appearance questions: divide by the stoichiometric coefficients.
:::

## Question patterns

:::pyq Recurring structures
1. Order from initial-rate tables (Section-B favourite).
2. First-order time/half-life calculations; % completion.
3. Arrhenius: $E_a$ from two temperatures; effect of a catalyst on $E_a$ and rate.
4. Units of $k$ ↔ order.
5. Graph identification (which plot is linear for which order).
6. Relations between rates of disappearance/appearance.
7. Kinetic study of the iodide–H₂O₂ reaction (practical chemistry).
:::

## Practice questions

@@SET C08 · Practice

@@Q C08-01 | E | 0.5 | Units of k | Speed
The units of the rate constant of a second-order reaction are:
(A) s⁻¹
(B) mol L⁻¹ s⁻¹
(C) L mol⁻¹ s⁻¹
(D) L² mol⁻² s⁻¹
@ans C
@sol (mol L⁻¹)$^{1-n}$ s⁻¹ with $n = 2$.
@short —
@trap —
@@END

@@Q C08-02 | M | 1 | 99% completion time | Calc
A first-order reaction has $k = 0.0693\ \text{min}^{-1}$. The time for 99% completion is about:
(A) 10 min
(B) 46 min
(C) 66.5 min
(D) 100 min
@ans C
@sol $t = \dfrac{2.303}{0.0693}\log100 = 33.23\times2 \approx 66.5$ min.
@short $t_{99\%} \approx 6.64\,t_{1/2} = 6.64\times10$.
@trap —
@@END

@@Q C08-03 | E | 1 | Zero-order half-life | NV
A zero-order reaction has $[\ce{A}]_0 = 0.4$ M and $k = 0.01$ M min⁻¹. Find its half-life (in minutes).
@ans 20
@sol $t_{1/2} = [\ce{A}]_0/2k = 0.4/0.02 = 20$ min.
@short —
@trap Using $0.693/k$.
@@END

@@Q C08-04 | M | 1.5 | Arrhenius two-temperature | Calc
The rate constant of a reaction doubles when the temperature rises from 300 K to 310 K. Its activation energy is about ($R = 8.314$, $\log 2 = 0.301$):
(A) 26.8 kJ/mol
(B) 53.6 kJ/mol
(C) 107 kJ/mol
(D) 5.36 kJ/mol
@ans B
@sol $0.301 = \dfrac{E_a}{2.303\times8.314}\left(\dfrac{10}{300\times310}\right) \Rightarrow E_a = \dfrac{0.301\times19.15\times93\,000}{10} \approx 53\,600$ J/mol.
@short Standard result: doubling between 300 K and 310 K means $E_a \approx 53.6$ kJ/mol.
@trap —
@@END

@@Q C08-05 | E | 0.5 | Order from rate change | NV
When the concentration of a reactant is doubled, the rate becomes 8 times larger. Find the order with respect to that reactant.
@ans 3
@sol $2^x = 8 \Rightarrow x = 3$.
@short —
@trap —
@@END

@@Q C08-06 | M | 1 | Relating rates | Concept
For $\ce{2N2O5 -> 4NO2 + O2}$, the rate of formation of $\ce{O2}$ is $1\times10^{-3}$ mol L⁻¹ s⁻¹. The rate of formation of $\ce{NO2}$ is:
(A) $1\times10^{-3}$
(B) $2\times10^{-3}$
(C) $4\times10^{-3}$
(D) $0.25\times10^{-3}$
@ans C
@sol $\dfrac14\dfrac{d[\ce{NO2}]}{dt} = \dfrac{d[\ce{O2}]}{dt} \Rightarrow \dfrac{d[\ce{NO2}]}{dt} = 4\times10^{-3}$.
@short —
@trap Dividing instead of multiplying.
@@END

@@Q C08-07 | E | 0.5 | Effect of catalyst | Concept
A catalyst increases the rate of a reaction by:
(A) increasing $\Delta H$
(B) lowering the activation energy
(C) increasing the equilibrium constant
(D) increasing the number of collisions only
@ans B
@sol —
@short —
@trap —
@@END

@@Q C08-08 | E | 0.5 | Pseudo-first-order reaction | Concept
The acid-catalysed hydrolysis of ethyl acetate in a large excess of water is:
(A) zero order
(B) pseudo-first order
(C) truly second order in the observed rate law
(D) third order
@ans B
@sol Water's concentration is effectively constant, so the rate law reduces to $r = k'[\text{ester}]$.
@short —
@trap —
@@END

@@Q C08-09 | E | 0.5 | Arrhenius plot | Concept
A plot of $\ln k$ against $1/T$ is a straight line with slope:
(A) $E_a/R$
(B) $-E_a/R$
(C) $-E_a/2.303R$
(D) $\ln A$
@ans B
@sol $\ln k = \ln A - \dfrac{E_a}{R}\cdot\dfrac1T$. (For $\log k$ the slope is $-E_a/2.303R$.)
@short —
@trap Mixing up ln and log plots.
@@END

@@Q C08-10 | E | 0.5 | Molecularity vs order | Concept
Which statement is correct?
(A) Molecularity can be fractional.
(B) Order can be zero or fractional.
(C) Order is always equal to molecularity.
(D) Molecularity is determined experimentally.
@ans B
@sol Order is experimental and can take any value. Molecularity is a theoretical positive integer for an elementary step.
@short —
@trap —
@@END

@@SET C08 · Chapter Test

@@Q C08-T1 | E | 0.5 | First-order half-life | Speed
The half-life of a first-order reaction:
(A) is proportional to the initial concentration
(B) is independent of the initial concentration
(C) is inversely proportional to the initial concentration
(D) depends on the square of the initial concentration
@ans B
@sol $t_{1/2} = 0.693/k$.
@short —
@trap —
@@END

@@Q C08-T2 | E | 0.5 | Half-life from 75% completion | NV
A first-order reaction is 75% complete in 30 min. Find its half-life (in minutes).
@ans 15
@sol 75% complete means two half-lives have passed, so $t_{1/2} = 15$ min.
@short —
@trap —
@@END

@@Q C08-T3 | E | 0.5 | Units of zero-order k | Speed
The units of $k$ for a zero-order reaction are:
(A) s⁻¹
(B) mol L⁻¹ s⁻¹
(C) L mol⁻¹ s⁻¹
(D) dimensionless
@ans B
@sol —
@short —
@trap —
@@END

@@Q C08-T4 | E | 0.75 | Temperature-coefficient rule | Basic
If a reaction's rate doubles for every 10 °C rise, raising the temperature from 20 °C to 50 °C multiplies the rate by:
(A) 3
(B) 6
(C) 8
(D) 9
@ans C
@sol $2^{30/10} = 8$.
@short —
@trap Multiplying $2\times3$.
@@END

@@Q C08-T5 | M | 0.75 | Barrier heights | Concept
For an exothermic reaction, the activation energy of the backward reaction is:
(A) smaller than that of the forward reaction
(B) larger than that of the forward reaction
(C) equal to that of the forward reaction
(D) zero
@ans B
@sol $E_a(b) = E_a(f) - \Delta H$, and $\Delta H < 0$.
@short —
@trap —
@@END

## Answers & Solutions {#c08-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Chemical Kinetics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
