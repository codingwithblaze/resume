# Integral Calculus {#m08}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium–Hard
Priority | Must-do
NCERT | Class 12 · Ch 7, 8
Study time | ~18 hours
:::

## Core concepts

- **Indefinite integral:** an antiderivative, $\int f\,dx = F + C$ with $F' = f$. Methods: standard forms, **substitution**, **by parts**, **partial fractions**, trigonometric identities.
- **Definite integral:** $\int_a^b f\,dx = F(b) - F(a)$ (fundamental theorem). Its **properties** often make evaluation unnecessary.
- **Area** between curves: integrate (upper − lower) with respect to $x$, or (right − left) with respect to $y$.

## Important formulas & standard results

:::formula Standard integrals (the syllabus list and the basics)
| $\int$ | Result |
|---|---|
| $x^n\,dx$ ($n \ne -1$) | $\dfrac{x^{n+1}}{n+1}$ |
| $\dfrac1x\,dx$ | $\ln\lvert x\rvert$ |
| $e^{ax}\,dx$ | $\dfrac{e^{ax}}{a}$ |
| $\sin x$, $\cos x$ | $-\cos x$, $\sin x$ |
| $\tan x$, $\cot x$ | $\ln\lvert\sec x\rvert$, $\ln\lvert\sin x\rvert$ |
| $\sec x$, $\csc x$ | $\ln\lvert\sec x + \tan x\rvert$, $\ln\lvert\csc x - \cot x\rvert$ |
| $\dfrac{dx}{x^2 + a^2}$ | $\dfrac1a\tan^{-1}\dfrac xa$ |
| $\dfrac{dx}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert$ |
| $\dfrac{dx}{a^2 - x^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{a + x}{a - x}\right\rvert$ |
| $\dfrac{dx}{\sqrt{a^2 - x^2}}$ | $\sin^{-1}\dfrac xa$ |
| $\dfrac{dx}{\sqrt{x^2 \pm a^2}}$ | $\ln\left\lvert x + \sqrt{x^2 \pm a^2}\right\rvert$ |
| $\sqrt{a^2 - x^2}\,dx$ | $\dfrac x2\sqrt{a^2 - x^2} + \dfrac{a^2}{2}\sin^{-1}\dfrac xa$ |
| $\sqrt{x^2 \pm a^2}\,dx$ | $\dfrac x2\sqrt{x^2 \pm a^2} \pm \dfrac{a^2}{2}\ln\left\lvert x + \sqrt{x^2 \pm a^2}\right\rvert$ |

$\int\dfrac{dx}{ax^2 + bx + c}$ and $\int\dfrac{dx}{\sqrt{ax^2 + bx + c}}$: **complete the square**. $\int\dfrac{(px + q)\,dx}{ax^2 + bx + c}$: write $px + q = A\dfrac{d}{dx}(ax^2 + bx + c) + B$.
(+C omitted throughout.)
:::

:::formula Methods
**By parts:** $\int u\,v\,dx = u\int v\,dx - \int\left(u'\int v\,dx\right)dx$. Choose $u$ by **ILATE** (Inverse trig, Log, Algebraic, Trig, Exponential).
**Special form:** $\int e^x[f(x) + f'(x)]\,dx = e^xf(x)$.
**Partial fractions:** $\dfrac{1}{(x - a)(x - b)} = \dfrac{1}{a - b}\left(\dfrac{1}{x - a} - \dfrac{1}{x - b}\right)$; repeated factor $(x - a)^2$ → $\dfrac{A}{x - a} + \dfrac{B}{(x - a)^2}$; quadratic factor → $\dfrac{Bx + C}{x^2 + px + q}$.
**Trig identities:** $\sin^2x = \dfrac{1 - \cos2x}{2}$, $\cos^2x = \dfrac{1 + \cos2x}{2}$; products → sums.
:::

:::formula Properties of definite integrals
$$\int_a^bf(x)\,dx = \int_a^bf(a + b - x)\,dx \quad \text{(King's rule)} \qquad \int_0^af(x)\,dx = \int_0^af(a - x)\,dx$$
$$\int_{-a}^af = \begin{cases}2\int_0^af & f\ \text{even}\\ 0 & f\ \text{odd}\end{cases} \qquad \int_0^{2a}f = \begin{cases}2\int_0^af & f(2a - x) = f(x)\\ 0 & f(2a - x) = -f(x)\end{cases} \qquad \int_0^{nT}f = n\int_0^Tf\ (\text{period } T)$$
**Leibniz rule** (from the fundamental theorem): $\dfrac{d}{dx}\displaystyle\int_{g(x)}^{h(x)}f(t)\,dt = f(h(x))\,h'(x) - f(g(x))\,g'(x)$.
**Useful values:** $\int_0^{\pi/2}\sin^2x = \int_0^{\pi/2}\cos^2x = \dfrac\pi4$; $\int_0^{\pi/2}\dfrac{\sin^nx}{\sin^nx + \cos^nx}\,dx = \dfrac\pi4$; $\int_0^\pi\lvert\cos x\rvert\,dx = 2$; $\int_0^{\pi/2}\ln\sin x\,dx = -\dfrac\pi2\ln2$.
:::

:::formula Standard areas
Circle $\pi r^2$ · ellipse $\pi ab$ · parabola $y^2 = 4ax$ with its latus rectum: $\dfrac83a^2$ · between $y^2 = 4ax$ and $x^2 = 4ay$: $\dfrac{16a^2}{3}$ · between $y = x^2$ and $y = x$: $\dfrac16$.
:::

## Common question models

:::pyq Recurring structures
1. **Standard-form integrals** after completing the square, or linear-over-quadratic splitting.
2. **By parts / $e^x(f + f')$** recognition.
3. **Definite integrals via properties:** King's rule pairs ($\frac{f(x)}{f(x) + f(a + b - x)}$ gives $\frac{b - a}{2}$), even/odd, periodicity, modulus and greatest-integer integrands (split at the break points).
4. **Leibniz rule:** limits of integrals, derivatives of integral functions.
5. **Area between curves** (parabola–line, circle–parabola, modulus graphs).
6. **Functional equations with integrals:** $f(x) = x + \int_0^1 f(t)\,dt$-type (the integral is a constant).
:::

## Shortcuts & fast methods

:::shortcut King's-rule pairing
If $f(x) + f(a + b - x) = c$ (a constant), then $\int_a^bf(x)\,dx = \dfrac{c(b - a)}{2}$. Classic case: $\int_a^b\dfrac{g(x)}{g(x) + g(a + b - x)}dx = \dfrac{b - a}{2}$.
**Time saved:** 2–3 minutes. **When NOT to use:** when the substituted integrand doesn't simplify when added back to the original.
:::

:::shortcut Differentiate the options
For an indefinite integral MCQ, differentiate each option (starting with the most likely one) and compare with the integrand. That's often faster than integrating.
:::

## Common mistakes

:::trap Mistake alerts
- Forgetting to change the limits when substituting in a definite integral.
- $\int\dfrac{dx}{x^2 - a^2}$ vs $\int\dfrac{dx}{a^2 - x^2}$: the log's argument flips.
- Area: take the **absolute** value. Split the region wherever the curves cross, or wherever the curve crosses the axis.
- Greatest-integer integrands: split at every integer inside the interval.
:::

## Practice questions

@@SET M08 · Practice

@@Q M08-01 | M | 1.5 | Completing the square | Basic
$\displaystyle\int\frac{dx}{x^2 + 4x + 13}$ equals:
(A) $\dfrac13\tan^{-1}\dfrac{x + 2}{3} + C$
(B) $\tan^{-1}\dfrac{x + 2}{3} + C$
(C) $\dfrac13\tan^{-1}\dfrac{x + 2}{9} + C$
(D) $\dfrac19\tan^{-1}(x + 2) + C$
@ans A
@sol $x^2 + 4x + 13 = (x + 2)^2 + 9$, so $\dfrac13\tan^{-1}\dfrac{x + 2}{3}$.
@short —
@trap —
@@END

@@Q M08-02 | E | 0.75 | Integration by parts | Basic
$\displaystyle\int xe^x\,dx$ equals:
(A) $e^x(x + 1) + C$
(B) $e^x(x - 1) + C$
(C) $xe^x + C$
(D) $\dfrac{x^2}{2}e^x + C$
@ans B
@sol $u = x$, $v = e^x$: $xe^x - \int e^x\,dx = e^x(x - 1)$.
@short Differentiate (B): $e^x(x - 1) + e^x = xe^x$ ✓.
@trap —
@@END

@@Q M08-03 | E | 0.5 | The e^x(f + f′) form | Speed
$\displaystyle\int e^x(\sin x + \cos x)\,dx$ equals:
(A) $e^x\cos x + C$
(B) $e^x\sin x + C$
(C) $-e^x\sin x + C$
(D) $e^x(\sin x - \cos x) + C$
@ans B
@sol $f = \sin x$, $f' = \cos x$.
@short —
@trap —
@@END

@@Q M08-04 | M | 1 | King's rule | Concept
$\displaystyle\int_0^{\pi/2}\frac{\sin x}{\sin x + \cos x}\,dx$ equals:
(A) $\pi/2$
(B) $\pi/4$
(C) 1
(D) $\pi$
@ans B
@sol Call it $I$. Replacing $x$ by $\frac\pi2 - x$ gives the cosine version. Adding the two: $2I = \int_0^{\pi/2}1\,dx = \frac\pi2$, so $I = \frac\pi4$.
@short $\dfrac{b - a}{2}$.
@trap —
@@END

@@Q M08-05 | E | 0.5 | Odd integrand | Speed
$\displaystyle\int_{-1}^{1}x^3\cos x\,dx$ equals:
(A) 0
(B) 2
(C) $2\cos1$
(D) 1
@ans A
@sol odd × even = odd, and the interval is symmetric.
@short —
@trap —
@@END

@@Q M08-06 | E | 1 | Greatest-integer integrand | NV
Find $\displaystyle\int_0^2[x]\,dx$, where $[\cdot]$ is the greatest integer function.
@ans 1
@sol $\int_0^1 0\,dx + \int_1^2 1\,dx = 1$.
@short —
@trap —
@@END

@@Q M08-07 | E | 1 | Area between curves | Basic
The area enclosed between $y = x^2$ and $y = x$ is:
(A) $1/2$
(B) $1/3$
(C) $1/6$
(D) $1/12$
@ans C
@sol They meet at $x = 0$ and 1: $\int_0^1(x - x^2)\,dx = \frac12 - \frac13 = \frac16$.
@short —
@trap —
@@END

@@Q M08-08 | E | 0.5 | Area of an ellipse | Speed
The area enclosed by $\dfrac{x^2}{9} + \dfrac{y^2}{4} = 1$ is:
(A) $6\pi$
(B) $12\pi$
(C) $36\pi$
(D) $13\pi$
@ans A
@sol $\pi ab = \pi\cdot3\cdot2$.
@short —
@trap —
@@END

@@Q M08-09 | M | 1 | Leibniz rule | Concept
$\dfrac{d}{dx}\displaystyle\int_0^{x^2}\sin t\,dt$ equals:
(A) $\sin x^2$
(B) $2x\sin x^2$
(C) $2x\cos x^2$
(D) $\cos x^2$
@ans B
@sol $\sin(x^2)\cdot\dfrac{d}{dx}(x^2)$.
@short —
@trap Forgetting the chain factor $2x$.
@@END

@@Q M08-10 | E | 0.5 | Arcsine form | Speed
$\displaystyle\int\frac{dx}{\sqrt{9 - x^2}}$ equals:
(A) $\sin^{-1}\dfrac x3 + C$
(B) $\dfrac13\sin^{-1}\dfrac x3 + C$
(C) $\sin^{-1}3x + C$
(D) $\dfrac13\tan^{-1}\dfrac x3 + C$
@ans A
@sol —
@short —
@trap Adding a spurious $1/3$ (as in the $\tan^{-1}$ form).
@@END

@@Q M08-11 | M | 1 | Partial fractions | Basic
$\displaystyle\int\frac{dx}{x(x + 1)}$ equals:
(A) $\ln\left\lvert\dfrac{x}{x + 1}\right\rvert + C$
(B) $\ln\lvert x(x + 1)\rvert + C$
(C) $\ln\left\lvert\dfrac{x + 1}{x}\right\rvert + C$
(D) $\dfrac{1}{x + 1} + C$
@ans A
@sol $\dfrac{1}{x(x + 1)} = \dfrac1x - \dfrac{1}{x + 1}$.
@short —
@trap —
@@END

@@Q M08-12 | E | 1 | Integral of modulus | NV
Find $\displaystyle\int_0^\pi\lvert\cos x\rvert\,dx$.
@ans 2
@sol $\int_0^{\pi/2}\cos x\,dx - \int_{\pi/2}^\pi\cos x\,dx = 1 + 1 = 2$.
@short —
@trap Ignoring the modulus gives 0.
@@END

@@SET M08 · Chapter Test

@@Q M08-T1 | E | 0.5 | Basic integral | Speed
$\displaystyle\int\sec^2x\,dx$ equals:
(A) $\tan x + C$
(B) $\sec x\tan x + C$
(C) $\cot x + C$
(D) $\sec x + C$
@ans A
@sol —
@short —
@trap —
@@END

@@Q M08-T2 | E | 0.5 | Property | Speed
$\displaystyle\int_0^af(x)\,dx$ equals:
(A) $\displaystyle\int_0^af(x - a)\,dx$
(B) $\displaystyle\int_0^af(a - x)\,dx$
(C) $\displaystyle\int_0^{2a}f(x)\,dx$
(D) $\displaystyle\int_{-a}^0f(x)\,dx$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M08-T3 | E | 0.75 | Definite integral | NV
Find $\displaystyle\int_0^3(2x + 1)\,dx$.
@ans 12
@sol $[x^2 + x]_0^3 = 9 + 3 = 12$.
@short —
@trap —
@@END

@@Q M08-T4 | E | 0.75 | Integral of ln x | Basic
$\displaystyle\int\ln x\,dx$ equals:
(A) $\dfrac1x + C$
(B) $x\ln x - x + C$
(C) $x\ln x + C$
(D) $\dfrac{(\ln x)^2}{2} + C$
@ans B
@sol By parts with $u = \ln x$, $v = 1$.
@short —
@trap —
@@END

@@Q M08-T5 | E | 0.75 | sin² over [0, π] | Basic
$\displaystyle\int_0^\pi\sin^2x\,dx$ equals:
(A) $\pi$
(B) $\pi/2$
(C) $\pi/4$
(D) 1
@ans B
@sol The average of $\sin^2$ over a period is $\tfrac12$: $\tfrac12\cdot\pi$.
@short —
@trap —
@@END

## Answers & Solutions {#m08-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Integral Calculus
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
