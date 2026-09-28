# Complex Numbers & Quadratic Equations {#m02}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 4 (Complex Numbers & Quadratic Equations)
Study time | ~14 hours
:::

## Core concepts

- A complex number $z = a + ib$ is an ordered pair $(a, b)$, plotted as a point in the **Argand plane**. $\lvert z\rvert$ is its distance from the origin; $\arg z$ is its angle, with principal value in $(-\pi, \pi]$.
- **Polar form** $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$ turns multiplication into "multiply moduli, add arguments".
- **Geometry:** $\lvert z - z_1\rvert$ is the distance between points, so modulus equations describe **loci** (circles, lines, ellipses).
- **Quadratics:** roots, discriminant, Vieta's relations, symmetric functions of roots, and conditions on where the roots lie.

:::note Syllabus note
The official text lists: complex numbers as ordered pairs, $a + ib$ form, Argand diagram, algebra, modulus, argument; quadratics in real and complex systems, roots and coefficients, nature of roots, forming equations [NTA-SYL]. **Cube roots of unity** and **De Moivre's theorem** are not named; they're included here as time-saving tools only.
:::

## Important formulas & identities

:::formula Algebra of complex numbers
$$\bar z = a - ib \qquad z\bar z = \lvert z\rvert^2 \qquad \frac{1}{z} = \frac{\bar z}{\lvert z\rvert^2} \qquad \operatorname{Re}z = \frac{z + \bar z}{2} \qquad \operatorname{Im}z = \frac{z - \bar z}{2i}$$
$$\lvert z_1z_2\rvert = \lvert z_1\rvert\lvert z_2\rvert \qquad \left\lvert\frac{z_1}{z_2}\right\rvert = \frac{\lvert z_1\rvert}{\lvert z_2\rvert} \qquad \arg(z_1z_2) = \arg z_1 + \arg z_2\ (\text{mod } 2\pi)$$
$$\lvert z_1 \pm z_2\rvert^2 = \lvert z_1\rvert^2 + \lvert z_2\rvert^2 \pm 2\operatorname{Re}(z_1\bar z_2) \qquad \big\lvert\lvert z_1\rvert - \lvert z_2\rvert\big\rvert \le \lvert z_1 + z_2\rvert \le \lvert z_1\rvert + \lvert z_2\rvert$$
Powers of $i$ cycle with period 4: $i, -1, -i, 1$. $(1 + i)^2 = 2i$, $(1 - i)^2 = -2i$.
**Principal argument** of $a + ib$: find $\alpha = \tan^{-1}\lvert b/a\rvert$, then place it in the right quadrant: I: $\alpha$; II: $\pi - \alpha$; III: $-(\pi - \alpha)$; IV: $-\alpha$.
:::

:::formula Standard loci
| Condition | Locus |
|---|---|
| $\lvert z - z_0\rvert = r$ | circle, centre $z_0$, radius $r$ |
| $\lvert z - z_1\rvert = \lvert z - z_2\rvert$ | perpendicular bisector of $z_1z_2$ |
| $\lvert z - z_1\rvert + \lvert z - z_2\rvert = 2a$, $2a > \lvert z_1 - z_2\rvert$ | ellipse with foci $z_1$, $z_2$ |
| $\lvert z - z_1\rvert = k\lvert z - z_2\rvert$, $k \ne 1$ | circle (Apollonius) |
| $\arg\dfrac{z - z_1}{z - z_2} = \pm\dfrac\pi2$ | circle with $z_1z_2$ as diameter (minus the endpoints) |
| $\operatorname{Re}z = c$ / $\operatorname{Im}z = c$ | vertical / horizontal line |
:::

:::formula Tools (not named in the syllabus text)
**Cube roots of unity:** $1, \omega, \omega^2$ with $\omega = \dfrac{-1 + i\sqrt3}{2}$, $1 + \omega + \omega^2 = 0$, $\omega^3 = 1$. Reduce powers mod 3.
**De Moivre:** $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$.
:::

:::formula Quadratic equations $ax^2 + bx + c = 0$
$$x = \frac{-b \pm\sqrt D}{2a},\ D = b^2 - 4ac \qquad \alpha + \beta = -\frac ba \qquad \alpha\beta = \frac ca \qquad \lvert\alpha - \beta\rvert = \frac{\sqrt D}{\lvert a\rvert}$$
$$\alpha^2 + \beta^2 = S^2 - 2P \qquad \alpha^3 + \beta^3 = S^3 - 3PS \qquad \frac1\alpha + \frac1\beta = \frac SP \qquad \text{equation with roots } \alpha, \beta:\ x^2 - Sx + P = 0$$
**Nature (real coefficients):** $D > 0$ real distinct; $D = 0$ equal; $D < 0$ complex conjugates. Rational coefficients with $D$ a perfect square give rational roots. Irrational/complex roots come in conjugate pairs.
**Common root** of $a_1x^2 + b_1x + c_1 = 0$ and $a_2x^2 + b_2x + c_2 = 0$: $(c_1a_2 - c_2a_1)^2 = (a_1b_2 - a_2b_1)(b_1c_2 - b_2c_1)$. Often faster: subtract the equations.
**Sign of $f(x) = ax^2 + bx + c$:** if $D < 0$, $f$ has the sign of $a$ for all $x$. Extreme value $-\dfrac{D}{4a}$ at $x = -\dfrac{b}{2a}$.
**Location of roots** (both roots greater than $k$, $a > 0$): $D \ge 0$, $f(k) > 0$, $-\dfrac{b}{2a} > k$. $k$ lies between the roots iff $a\,f(k) < 0$.
:::

## Common question models

:::pyq Recurring structures
1. **Modulus/argument** of a quotient or power; principal argument in the correct quadrant.
2. **Loci** from modulus/argument conditions; maximum/minimum $\lvert z\rvert$ on a circle (distance from the origin to the centre ± radius).
3. **Equations in $z$** ($z^2 + \lvert z\rvert = 0$, $\bar z = iz^2$): substitute $z = x + iy$ and compare real and imaginary parts.
4. **Vieta / symmetric functions**, forming new equations with transformed roots.
5. **Nature and location of roots**, common roots, parameter ranges.
6. **Powers of $i$ or $\omega$** in sums.
:::

## Shortcuts & fast methods

:::shortcut Min/max of |z| on a circle
If $\lvert z - z_0\rvert = r$, then $\lvert z\rvert$ ranges over $\big[\,\lvert\lvert z_0\rvert - r\rvert,\ \lvert z_0\rvert + r\,\big]$. More generally, $\lvert z - w\rvert$ ranges over the distance from $w$ to the centre ± $r$.
**Time saved:** a whole parametrisation.
:::

:::shortcut Transformed roots
Equation whose roots are $k\alpha$, $k\beta$: replace $x$ by $x/k$. Roots $\alpha + h$: replace $x$ by $x - h$. Roots $1/\alpha$: reverse the coefficients.
:::

## Common mistakes

:::trap Mistake alerts
- Principal argument of $-1 - i$ is $-3\pi/4$, not $\pi/4$ ($\tan^{-1}(b/a)$ loses the quadrant).
- $\sqrt{a}\sqrt{b} = \sqrt{ab}$ fails when both are negative: $\sqrt{-1}\sqrt{-1} = -1$.
- For "real roots", check $D \ge 0$, and also $a \ne 0$ if the problem says "quadratic".
- Conjugate-pair rules need **real** coefficients.
:::

## Practice questions

@@SET M02 · Practice

@@Q M02-01 | E | 0.75 | Modulus and argument of a quotient | Basic
For $z = \dfrac{1 + i}{1 - i}$, $\lvert z\rvert$ and $\arg z$ are:
(A) $1, \pi/2$
(B) $\sqrt2, \pi/4$
(C) $1, \pi/4$
(D) $1, -\pi/2$
@ans A
@sol $\dfrac{(1+i)^2}{2} = \dfrac{2i}{2} = i$.
@short —
@trap —
@@END

@@Q M02-02 | M | 1.5 | Perpendicular-bisector locus | Concept
The locus of $z$ satisfying $\lvert z - 2\rvert = \lvert z + 2i\rvert$ is the line:
(A) $x + y = 0$
(B) $x - y = 0$
(C) $x = 2$
(D) $y = -2$
@ans A
@sol $(x - 2)^2 + y^2 = x^2 + (y + 2)^2 \Rightarrow -4x = 4y \Rightarrow y = -x$.
@short The perpendicular bisector of $(2, 0)$ and $(0, -2)$ passes through their midpoint $(1, -1)$ with slope $-1$.
@trap —
@@END

@@Q M02-03 | M | 1 | Roots differing by 1 | Basic
If the roots of $x^2 - px + q = 0$ differ by 1, then:
(A) $p^2 = 4q + 1$
(B) $p^2 = 4q - 1$
(C) $q^2 = 4p + 1$
(D) $p^2 + 4q = 1$
@ans A
@sol $(\alpha - \beta)^2 = (\alpha + \beta)^2 - 4\alpha\beta = p^2 - 4q = 1$.
@short —
@trap —
@@END

@@Q M02-04 | M | 1 | Symmetric function of roots | Calc
If $\alpha, \beta$ are the roots of $2x^2 - 3x - 5 = 0$, then $\alpha^2 + \beta^2$ equals:
(A) $29/4$
(B) $19/4$
(C) $9/4$
(D) $-11/4$
@ans A
@sol $S = 3/2$, $P = -5/2$. $S^2 - 2P = 9/4 + 5 = 29/4$.
@short —
@trap Sign of $P$.
@@END

@@Q M02-05 | E | 1 | Real-root condition | NV
Find the largest integer $k$ for which $kx^2 + 4x + 1 = 0$ has real roots.
@ans 4
@sol $D = 16 - 4k \ge 0 \Rightarrow k \le 4$. At $k = 4$ the root is repeated, which is still real (and $k \ne 0$ keeps it quadratic).
@short —
@trap Using $D > 0$ strictly.
@@END

@@Q M02-06 | M | 1.5 | Common root | JEE
If $x^2 + ax + 1 = 0$ and $x^2 + x + a = 0$ ($a \ne 1$) have a common root, then $a$ equals:
(A) $-2$
(B) $2$
(C) $1$
(D) $0$
@ans A
@sol Subtracting: $(a - 1)x - (a - 1) = 0 \Rightarrow x = 1$. Substituting: $1 + a + 1 = 0 \Rightarrow a = -2$.
@short Subtract to find the common root first.
@trap —
@@END

@@Q M02-07 | E | 0.75 | Power of (1 + i) | NV
Find the value of $(1 + i)^8$.
@ans 16
@sol $(1 + i)^2 = 2i$, so $(1 + i)^8 = (2i)^4 = 16i^4 = 16$.
@short —
@trap —
@@END

@@Q M02-08 | M | 1 | Triangle-inequality equality | Concept
For non-zero $z_1, z_2$, $\lvert z_1 + z_2\rvert = \lvert z_1\rvert + \lvert z_2\rvert$ implies:
(A) $\arg z_1 = \arg z_2$
(B) $\arg z_1 = -\arg z_2$
(C) $z_1 = \bar z_2$
(D) $\lvert z_1\rvert = \lvert z_2\rvert$
@ans A
@sol Equality holds only when the vectors point in the same direction.
@short —
@trap —
@@END

@@Q M02-09 | M | 1 | Powers of ω | Concept
If $\omega$ is a non-real cube root of unity, then $1 + \omega^{100} + \omega^{200}$ equals:
(A) 0
(B) 1
(C) 3
(D) $\omega$
@ans A
@sol $\omega^{100} = \omega^{99}\omega = \omega$; $\omega^{200} = \omega^{198}\omega^2 = \omega^2$. Sum $= 1 + \omega + \omega^2 = 0$.
@short Reduce the exponents mod 3.
@trap —
@@END

@@Q M02-10 | M | 1.5 | Location of roots | JEE
Both roots of $x^2 - 2kx + k^2 - 1 = 0$ lie strictly between −2 and 4. Then $k$ lies in:
(A) $(-1, 3)$
(B) $(-2, 4)$
(C) $(-3, 5)$
(D) $(0, 2)$
@ans A
@sol The roots are $k \pm 1$. Need $k - 1 > -2$ and $k + 1 < 4$, so $-1 < k < 3$.
@short Factor first: $(x - k)^2 = 1$.
@trap Using the general location conditions and making an algebra slip.
@@END

@@SET M02 · Chapter Test

@@Q M02-T1 | E | 0.5 | Power of i | Speed
$i^{2027}$ equals:
(A) $1$
(B) $i$
(C) $-1$
(D) $-i$
@ans D
@sol $2027 = 4\times506 + 3$, so $i^3 = -i$.
@short —
@trap —
@@END

@@Q M02-T2 | E | 0.75 | Conjugate of a reciprocal | Basic
The conjugate of $\dfrac{1}{2 - i}$ is:
(A) $\dfrac{2 - i}{5}$
(B) $\dfrac{2 + i}{5}$
(C) $2 + i$
(D) $\dfrac{-2 + i}{5}$
@ans A
@sol $\dfrac{1}{2 - i} = \dfrac{2 + i}{5}$, whose conjugate is $\dfrac{2 - i}{5}$.
@short —
@trap Stopping at $\dfrac{2 + i}{5}$.
@@END

@@Q M02-T3 | E | 1 | Sum of cubes of roots | NV
If $\alpha, \beta$ are the roots of $x^2 - 5x + 6 = 0$, find $\alpha^3 + \beta^3$.
@ans 35
@sol $S^3 - 3PS = 125 - 90 = 35$ (check: $8 + 27$).
@short —
@trap —
@@END

@@Q M02-T4 | E | 0.5 | Forming a quadratic | Speed
The quadratic with roots $2 \pm \sqrt3$ is:
(A) $x^2 - 4x + 1 = 0$
(B) $x^2 + 4x + 1 = 0$
(C) $x^2 - 4x - 1 = 0$
(D) $x^2 - 2x + 3 = 0$
@ans A
@sol $S = 4$, $P = 4 - 3 = 1$.
@short —
@trap —
@@END

@@Q M02-T5 | E | 0.5 | Circle locus | Speed
The locus $\lvert z - 1\rvert = 3$ is a circle with:
(A) centre $(1, 0)$, radius 3
(B) centre $(0, 1)$, radius 3
(C) centre $(-1, 0)$, radius 3
(D) centre $(1, 0)$, radius 9
@ans A
@sol —
@short —
@trap —
@@END

## Answers & Solutions {#m02-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Complex & Quadratics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
