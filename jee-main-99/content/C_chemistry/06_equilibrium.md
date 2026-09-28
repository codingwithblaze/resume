# Equilibrium: Chemical & Ionic {#c06}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 6
Study time | ~12 hours
:::

## Important concepts

- **Dynamic equilibrium:** forward and backward rates are equal, and concentrations stay constant. It can be reached from either side.
- **Law of mass action:** for $a\ce{A} + b\ce{B} \rightleftharpoons c\ce{C} + d\ce{D}$, $K_c = \dfrac{[\ce{C}]^c[\ce{D}]^d}{[\ce{A}]^a[\ce{B}]^b}$. Pure solids and liquids are omitted.
- **Reaction quotient $Q$** has the same form at any moment. $Q < K$ → forward; $Q > K$ → backward; $Q = K$ → at equilibrium.
- **Le Chatelier's principle:** a system at equilibrium shifts to partly counteract any imposed change. Only **temperature** changes the value of $K$.
- **Ionic equilibria:** acids/bases (Arrhenius, Brønsted–Lowry, Lewis), $K_w$, pH, weak electrolytes, common-ion effect, salt hydrolysis, buffers, solubility product.

## Formula sheet: Chemical equilibrium

:::formula K relations
$$K_p = K_c(RT)^{\Delta n_g} \qquad \Delta G^\circ = -RT\ln K \qquad \log\frac{K_2}{K_1} = \frac{\Delta H^\circ}{2.303R}\left(\frac1{T_1} - \frac1{T_2}\right)$$
| Operation on the equation | New $K$ |
|---|---|
| reverse | $1/K$ |
| multiply by $n$ | $K^n$ |
| add two equations | $K_1K_2$ |

**Degree of dissociation from vapour density** ($\ce{A -> nB}$): $\alpha = \dfrac{D - d}{(n - 1)d}$, where $D$ = initial and $d$ = equilibrium vapour density.
:::

:::formula Le Chatelier summary
| Change | Effect |
|---|---|
| add reactant / remove product | shifts forward ($K$ unchanged) |
| increase pressure (decrease $V$) | shifts towards fewer gas moles |
| increase temperature | shifts in the endothermic direction; $K$ rises for endothermic reactions |
| catalyst | no shift; equilibrium reached faster |
| inert gas at constant **volume** | no effect |
| inert gas at constant **pressure** | shifts towards more gas moles |
:::

## Formula sheet: Ionic equilibrium

:::formula pH and weak electrolytes
$$K_w = [\ce{H+}][\ce{OH-}] = 10^{-14}\ (298\ \text{K}) \qquad \text{pH} = -\log[\ce{H+}] \qquad \text{pH} + \text{pOH} = 14$$
$$\text{Weak acid: } \alpha = \sqrt{\frac{K_a}{C}},\ [\ce{H+}] = \sqrt{K_aC},\ \text{pH} = \tfrac12(\text{p}K_a - \log C) \qquad K_aK_b = K_w \ \text{(conjugate pair)}$$
Ostwald's dilution law: $\alpha$ increases on dilution. $K_w$ increases with temperature (neutral pH < 7 above 25 °C).
Very dilute strong acid ($< 10^{-6}$ M): include water's $\ce{H+}$. $10^{-8}$ M HCl has pH ≈ 6.98, not 8.
:::

:::formula Buffers & hydrolysis
$$\text{Acidic buffer: } \text{pH} = \text{p}K_a + \log\frac{[\text{salt}]}{[\text{acid}]} \qquad \text{Basic buffer: } \text{pOH} = \text{p}K_b + \log\frac{[\text{salt}]}{[\text{base}]}$$
| Salt of | Nature | pH |
|---|---|---|
| strong acid + strong base (NaCl) | neutral | 7 |
| weak acid + strong base ($\ce{CH3COONa}$) | basic | $7 + \tfrac12\text{p}K_a + \tfrac12\log C$ |
| strong acid + weak base ($\ce{NH4Cl}$) | acidic | $7 - \tfrac12\text{p}K_b - \tfrac12\log C$ |
| weak acid + weak base ($\ce{CH3COONH4}$) | depends | $7 + \tfrac12\text{p}K_a - \tfrac12\text{p}K_b$ |
Maximum buffer capacity at [salt] = [acid], i.e. pH = p$K_a$.
:::

:::formula Solubility product
$\ce{A_xB_y <=> xA^{y+} + yB^{x-}}$: $K_{sp} = x^xy^ys^{x+y}$.
| Type | $K_{sp}$ | Example |
|---|---|---|
| AB | $s^2$ | AgCl, $\ce{BaSO4}$ |
| AB₂ / A₂B | $4s^3$ | $\ce{CaF2}$, $\ce{Ag2CrO4}$ |
| AB₃ | $27s^4$ | $\ce{Fe(OH)3}$ |
| A₂B₃ | $108s^5$ | $\ce{Bi2S3}$ |
**Precipitation** occurs when the ionic product > $K_{sp}$. **Common ion** lowers solubility: AgCl in $c$ M NaCl has $s \approx K_{sp}/c$.
:::

## Numerical-solving method (ICE table)

1. Write **I**nitial, **C**hange ($-x$, $+x$ with stoichiometric coefficients) and **E**quilibrium rows.
2. Substitute into $K$. If $K$ is small relative to $C$, approximate $C - x \approx C$.
3. Check: if $x/C > 5\%$, solve the quadratic.

:::shortcut pH of a buffer in your head
If [salt] = [acid], pH = p$K_a$. Every 10× increase in [salt]/[acid] adds 1 pH unit.
Acetic acid p$K_a$ = 4.74; $\ce{NH3}$ p$K_b$ = 4.74 (NH₄⁺ p$K_a$ = 9.26).
:::

## Common traps

:::trap Mistake alerts
- Including solids/liquids in $K$ expressions.
- $\Delta n_g$ for $K_p/K_c$: gaseous moles **products − reactants**.
- Catalysts don't change $K$ or the equilibrium composition.
- Diprotic bases: $\ce{Ba(OH)2}$ gives $[\ce{OH-}] = 2C$.
- $K_{sp}$ of $\ce{Ag2CrO4}$ is $4s^3$ (not $s^2$): $[\ce{Ag+}] = 2s$.
- Applying the Henderson equation to a solution with no conjugate pair.
:::

## Question patterns

:::pyq Recurring structures
1. $K_p$–$K_c$ relation; $K$ for combined/reversed reactions.
2. Le Chatelier predictions (pressure, temperature, inert gas).
3. pH of weak acids/bases, very dilute strong acids, mixtures of acid and base (after neutralisation).
4. Buffer pH (Henderson); buffer made by partial neutralisation.
5. $K_{sp}$ ↔ solubility; common-ion effect; precipitation condition.
6. Salt hydrolysis pH.
7. Degree of dissociation from vapour density or pressure data.
:::

## Practice questions

@@SET C06 · Practice

@@Q C06-01 | E | 0.75 | Kp and Kc | Basic
For $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$:
(A) $K_p = K_c$
(B) $K_p = K_c(RT)^2$
(C) $K_p = K_c(RT)^{-2}$
(D) $K_p = K_c(RT)^{-1}$
@ans C
@sol $\Delta n_g = 2 - 4 = -2$.
@short —
@trap Reversing the sign of $\Delta n_g$.
@@END

@@Q C06-02 | E | 0.5 | Reaction quotient | Concept
At some instant $Q < K$ for a reaction. The reaction will:
(A) proceed backward
(B) proceed forward
(C) be at equilibrium
(D) stop
@ans B
@sol Too few products relative to equilibrium, so the net reaction goes forward until $Q = K$.
@short —
@trap —
@@END

@@Q C06-03 | E | 0.5 | Effect of pressure | Speed
For $\ce{N2O4(g) <=> 2NO2(g)}$, increasing the total pressure (by compression) at constant temperature:
(A) shifts the equilibrium towards $\ce{NO2}$
(B) shifts it towards $\ce{N2O4}$
(C) has no effect
(D) changes $K_p$
@ans B
@sol The shift is towards fewer gas moles: 1 mol $\ce{N2O4}$ vs 2 mol $\ce{NO2}$. $K_p$ is unchanged.
@short —
@trap —
@@END

@@Q C06-04 | M | 1 | pH of a weak acid | Calc
The pH of 0.1 M acetic acid ($K_a = 1.8\times10^{-5}$) is about:
(A) 2.87
(B) 1.00
(C) 4.74
(D) 3.87
@ans A
@sol $[\ce{H+}] = \sqrt{1.8\times10^{-6}} \approx 1.34\times10^{-3}$; pH $\approx 2.87$.
@short pH $= \tfrac12(4.74 + 1) = 2.87$.
@trap Treating it as a strong acid (pH 1).
@@END

@@Q C06-05 | M | 1 | Buffer pH | Basic
A buffer contains 0.2 M $\ce{CH3COONa}$ and 0.02 M $\ce{CH3COOH}$ (p$K_a$ = 4.74). Its pH is:
(A) 3.74
(B) 4.74
(C) 5.74
(D) 6.74
@ans C
@sol pH $= 4.74 + \log(0.2/0.02) = 4.74 + 1 = 5.74$.
@short —
@trap Inverting the ratio.
@@END

@@Q C06-06 | M | 1 | Ksp from solubility | Calc
The solubility of $\ce{CaF2}$ is $2\times10^{-4}$ mol/L. Its $K_{sp}$ is:
(A) $4\times10^{-8}$
(B) $8\times10^{-12}$
(C) $3.2\times10^{-11}$
(D) $1.6\times10^{-11}$
@ans C
@sol $K_{sp} = (s)(2s)^2 = 4s^3 = 4\times8\times10^{-12} = 3.2\times10^{-11}$.
@short —
@trap Using $s^2$.
@@END

@@Q C06-07 | M | 1 | Common-ion effect | Concept
The solubility of AgCl ($K_{sp} = 1.8\times10^{-10}$) in 0.1 M NaCl is about:
(A) $1.34\times10^{-5}$ M
(B) $1.8\times10^{-9}$ M
(C) $1.8\times10^{-11}$ M
(D) 0.1 M
@ans B
@sol $s(0.1 + s) = 1.8\times10^{-10} \Rightarrow s \approx 1.8\times10^{-9}$ M.
@short $s \approx K_{sp}/[\text{common ion}]$.
@trap Answering the solubility in pure water (A).
@@END

@@Q C06-08 | H | 2 | pH of very dilute HCl | NV
Find the pH of $10^{-8}$ M HCl at 25 °C, to the nearest integer.
@ans 7
@sol $[\ce{H+}] = 10^{-8} + x$ with $x(10^{-8} + x) = 10^{-14}$. So $x \approx 9.5\times10^{-8}$ and $[\ce{H+}] \approx 1.05\times10^{-7}$, giving pH ≈ 6.98 → 7.
@short An acid solution can't have pH > 7. At this dilution, water's ions dominate.
@trap Answering 8.
@@END

@@Q C06-09 | M | 1.5 | Hydrolysis of sodium acetate | JEE
The pH of 0.1 M $\ce{CH3COONa}$ (p$K_a$ of acetic acid = 4.74) is about:
(A) 8.87
(B) 9.37
(C) 7.00
(D) 5.13
@ans A
@sol pH $= 7 + \tfrac12(4.74) + \tfrac12\log0.1 = 7 + 2.37 - 0.5 = 8.87$.
@short Salt of a weak acid and strong base is basic.
@trap Sign of the $\log C$ term.
@@END

@@Q C06-10 | E | 0.5 | Conjugate base | Speed
The conjugate base of $\ce{HSO4-}$ is:
(A) $\ce{H2SO4}$
(B) $\ce{SO4^{2-}}$
(C) $\ce{HSO3-}$
(D) $\ce{SO3^{2-}}$
@ans B
@sol Remove one $\ce{H+}$.
@short —
@trap Giving the conjugate acid.
@@END

@@Q C06-11 | E | 0.75 | K for reversed and doubled reaction | Basic
For $\ce{A <=> B}$, $K = 4$. For $\ce{2B <=> 2A}$, $K$ is:
(A) 1/16
(B) 16
(C) 1/8
(D) −8
@ans A
@sol Reverse: $1/4$. Double: $(1/4)^2 = 1/16$.
@short —
@trap —
@@END

@@SET C06 · Chapter Test

@@Q C06-T1 | E | 0.5 | Role of a catalyst | Speed
A catalyst added to a reaction at equilibrium:
(A) increases $K$
(B) shifts the equilibrium forward
(C) doesn't change the equilibrium composition, but equilibrium is reached faster
(D) decreases $K$
@ans C
@sol It speeds up both directions equally.
@short —
@trap —
@@END

@@Q C06-T2 | E | 0.5 | Lewis acid | Speed
Which is a Lewis acid?
(A) $\ce{NH3}$
(B) $\ce{BF3}$
(C) $\ce{H2O}$
(D) $\ce{Cl-}$
@ans B
@sol B has an incomplete octet and accepts an electron pair.
@short —
@trap —
@@END

@@Q C06-T3 | E | 1 | pH of a diacidic base | NV
Find the pH of 0.001 M $\ce{Ba(OH)2}$ (complete dissociation) to the nearest integer.
@ans 11
@sol $[\ce{OH-}] = 0.002$ M, so pOH $= 2.70$ and pH $= 11.30 \approx 11$.
@short —
@trap Forgetting the factor 2 (still pH 11, but the exact value is 11.0 rather than 11.3).
@@END

@@Q C06-T4 | E | 0.5 | Ksp expression | Speed
For $\ce{Ag2CrO4}$ with molar solubility $s$, $K_{sp}$ is:
(A) $s^2$
(B) $2s^3$
(C) $4s^3$
(D) $27s^4$
@ans C
@sol $[\ce{Ag+}] = 2s$, $[\ce{CrO4^{2-}}] = s$.
@short —
@trap —
@@END

@@Q C06-T5 | E | 0.5 | Ostwald's dilution law | Concept
On diluting a weak acid, its degree of dissociation:
(A) decreases
(B) increases
(C) stays constant
(D) becomes zero
@ans B
@sol $\alpha = \sqrt{K_a/C}$ rises as $C$ falls.
@short —
@trap —
@@END

## Answers & Solutions {#c06-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Equilibrium
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
