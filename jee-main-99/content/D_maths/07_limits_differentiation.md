# Limits, Continuity & Differentiability (with Applications of Derivatives) {#m07}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 12; Class 12 · Ch 5, 6
Study time | ~16 hours
:::

## Core concepts

- **Limit:** the value a function approaches. It exists iff LHL = RHL (finite). **Continuity at $a$:** $\lim_{x\to a}f(x) = f(a)$. **Differentiability at $a$:** LHD = RHD (finite).
- Differentiable ⇒ continuous, but **not** conversely ($\lvert x\rvert$ at 0).
- **Derivative rules:** sum, product, quotient, chain; implicit, parametric and logarithmic differentiation; second derivatives.
- **Applications (syllabus):** rate of change, increasing/decreasing functions, maxima and minima of functions of one variable.

:::note Syllabus note
Unit 7 lists real functions and their graphs, limits, continuity, differentiability, differentiation techniques up to second order, and AOD limited to **rate of change, monotonicity and maxima/minima** [NTA-SYL]. Tangents/normals, mean value theorems and approximations are not listed.
:::

## Important formulas & standard results

:::formula Standard limits ($x \to 0$ unless stated)
$$\frac{\sin x}{x},\ \frac{\tan x}{x},\ \frac{\sin^{-1}x}{x},\ \frac{\tan^{-1}x}{x} \to 1 \qquad \frac{1 - \cos x}{x^2} \to \frac12 \qquad \frac{e^x - 1}{x} \to 1 \qquad \frac{a^x - 1}{x} \to \ln a$$
$$\frac{\ln(1 + x)}{x} \to 1 \qquad (1 + x)^{1/x} \to e \qquad \lim_{x\to a}\frac{x^n - a^n}{x - a} = na^{n-1} \qquad \lim_{x\to\infty}\left(1 + \frac ax\right)^{bx} = e^{ab}$$
**$1^\infty$ form:** $\lim f^g = e^{\lim g(f - 1)}$ when $f \to 1$, $g \to \infty$.
**Series (fast for $0/0$):** $\sin x = x - \dfrac{x^3}{6} + \dots$, $\cos x = 1 - \dfrac{x^2}{2} + \dfrac{x^4}{24} - \dots$, $\tan x = x + \dfrac{x^3}{3} + \dots$, $e^x = 1 + x + \dfrac{x^2}{2} + \dots$, $\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dots$
**L'Hôpital's rule** (a tool, not named in the syllabus): for $0/0$ or $\infty/\infty$, $\lim\dfrac fg = \lim\dfrac{f'}{g'}$.
:::

:::formula Derivatives
| $f(x)$ | $f'(x)$ | $f(x)$ | $f'(x)$ |
|---|---|---|---|
| $x^n$ | $nx^{n-1}$ | $\sin^{-1}x$ | $\dfrac{1}{\sqrt{1 - x^2}}$ |
| $e^x$, $a^x$ | $e^x$, $a^x\ln a$ | $\cos^{-1}x$ | $-\dfrac{1}{\sqrt{1 - x^2}}$ |
| $\ln x$, $\log_ax$ | $\dfrac1x$, $\dfrac{1}{x\ln a}$ | $\tan^{-1}x$ | $\dfrac{1}{1 + x^2}$ |
| $\sin x$, $\cos x$ | $\cos x$, $-\sin x$ | $\cot^{-1}x$ | $-\dfrac{1}{1 + x^2}$ |
| $\tan x$, $\cot x$ | $\sec^2x$, $-\csc^2x$ | $\sec^{-1}x$ | $\dfrac{1}{\lvert x\rvert\sqrt{x^2 - 1}}$ |
| $\sec x$, $\csc x$ | $\sec x\tan x$, $-\csc x\cot x$ | $x^x$ | $x^x(1 + \ln x)$ |

**Parametric:** $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$, $\dfrac{d^2y}{dx^2} = \dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)\Big/\dfrac{dx}{dt}$. **Implicit:** differentiate both sides with respect to $x$, treating $y$ as $y(x)$.
**Substitutions for inverse-trig derivatives:** $\tan^{-1}\dfrac{2x}{1 - x^2} = 2\tan^{-1}x$ ($\lvert x\rvert < 1$); $\sin^{-1}\dfrac{2x}{1 + x^2} = 2\tan^{-1}x$ ($\lvert x\rvert \le 1$); $\cos^{-1}\dfrac{1 - x^2}{1 + x^2} = 2\tan^{-1}x$ ($x \ge 0$).
:::

:::formula Continuity & differentiability facts
- Polynomials, $\sin$, $\cos$, $e^x$ are continuous everywhere; rational functions except where the denominator is zero; $\ln x$ for $x > 0$.
- $[x]$ is discontinuous at every integer. $\{x\}$ likewise.
- $\lvert f(x)\rvert$ is non-differentiable at the **simple roots** of $f$ (where $f$ changes sign) where $f' \ne 0$.
- $\lvert x - a_1\rvert + \lvert x - a_2\rvert + \dots$ is non-differentiable exactly at $a_1, a_2, \dots$
:::

:::formula Applications of derivatives
**Rate of change:** $\dfrac{dA}{dt} = \dfrac{dA}{dr}\cdot\dfrac{dr}{dt}$ (circle: $2\pi r\,\dot r$; sphere volume: $4\pi r^2\dot r$).
**Monotonicity:** $f' > 0$ on an interval → strictly increasing; $f' < 0$ → strictly decreasing.
**Extrema:** critical points where $f' = 0$ or $f'$ doesn't exist. First-derivative test: $f'$ changes from + to − means a local max. Second-derivative test: $f'(c) = 0$, $f''(c) < 0$ means a max; $> 0$ means a min.
**Absolute extrema on $[a, b]$:** compare $f$ at the critical points **and** the endpoints.
**Classic optima:** fixed perimeter → the square has maximum area; the largest rectangle in a circle is a square; $a\sin x + b\cos x$ has maximum $\sqrt{a^2 + b^2}$.
:::

## Common question models

:::pyq Recurring structures
1. **Evaluate limits:** standard forms, rationalisation, series expansion, $1^\infty$, limits at infinity with polynomials.
2. **Find constants for continuity/differentiability** of piecewise functions.
3. **Count points of non-differentiability** (modulus, greatest-integer and max/min compositions).
4. **Derivatives:** composite, parametric, implicit, logarithmic, inverse-trig simplification, second derivatives.
5. **Monotonicity intervals;** local/absolute extrema; optimisation word problems.
6. **Rates of change** (ladders, balloons, circles).
:::

## Shortcuts & fast methods

:::shortcut Series expansion beats L'Hôpital
For $\dfrac{\sin x - x}{x^3}$-type limits, substitute the first two terms of the series. It's one line, versus three rounds of differentiation.
**When NOT to use:** when the limit isn't at 0 (substitute $x = a + h$ first).
:::

:::shortcut Leading terms at infinity
$\lim_{x\to\infty}\dfrac{a_nx^n + \dots}{b_mx^m + \dots}$: if $n = m$ the answer is $a_n/b_m$; if $n < m$ it's 0; if $n > m$ it's ±∞.
:::

## Common mistakes

:::trap Mistake alerts
- Using $\lim\dfrac{\sin x}{x} = 1$ in degrees. JEE uses **radians**.
- A limit existing (LHL = RHL) doesn't make the function continuous. $f(a)$ must also equal it.
- In optimisation, forgetting the endpoints of a closed interval.
- $\dfrac{d}{dx}(x^x) \ne x\cdot x^{x-1}$.
:::

## Practice questions

@@SET M07 · Practice

@@Q M07-01 | E | 0.75 | Standard limits | Basic
$\displaystyle\lim_{x\to0}\frac{e^{2x} - 1}{\sin3x}$ equals:
(A) $2/3$
(B) $3/2$
(C) 1
(D) 6
@ans A
@sol $\dfrac{e^{2x} - 1}{2x}\cdot\dfrac{3x}{\sin3x}\cdot\dfrac{2}{3} \to \dfrac23$.
@short Replace each by its linear approximation: $2x/3x$.
@trap —
@@END

@@Q M07-02 | M | 1 | 1^∞ form | Concept
$\displaystyle\lim_{x\to\infty}\left(1 + \frac2x\right)^{3x}$ equals:
(A) $e^6$
(B) $e^{2/3}$
(C) $e^{3/2}$
(D) 1
@ans A
@sol $e^{\lim 3x\cdot(2/x)} = e^6$.
@short $e^{ab}$.
@trap Answering 1 (treating $1^\infty$ as 1).
@@END

@@Q M07-03 | M | 1 | Series expansion limit | Concept
$\displaystyle\lim_{x\to0}\frac{\sin x - x}{x^3}$ equals:
(A) $1/6$
(B) $-1/6$
(C) 0
(D) $-1/3$
@ans B
@sol $\sin x - x = -\dfrac{x^3}{6} + O(x^5)$.
@short —
@trap Sign.
@@END

@@Q M07-04 | E | 0.75 | Removable discontinuity | NV
$f(x) = \dfrac{x^2 - 4}{x - 2}$ for $x \ne 2$ and $f(2) = k$. Find $k$ if $f$ is continuous at $x = 2$.
@ans 4
@sol $\lim_{x\to2}(x + 2) = 4$.
@short —
@trap —
@@END

@@Q M07-05 | E | 0.75 | Non-differentiability of |·| sums | NV
Find the number of points where $f(x) = \lvert x - 1\rvert + \lvert x - 2\rvert$ is not differentiable.
@ans 2
@sol The corners are at $x = 1$ and $x = 2$.
@short —
@trap —
@@END

@@Q M07-06 | E | 0.75 | Logarithmic differentiation | Basic
$\dfrac{d}{dx}(x^x)$ for $x > 0$ is:
(A) $x\cdot x^{x-1}$
(B) $x^x\ln x$
(C) $x^x(1 + \ln x)$
(D) $x^x(1 - \ln x)$
@ans C
@sol $y = x^x \Rightarrow \ln y = x\ln x \Rightarrow \dfrac{y'}{y} = 1 + \ln x$.
@short —
@trap Option (A) uses the power rule wrongly.
@@END

@@Q M07-07 | E | 0.75 | Parametric derivative | Basic
If $x = a\cos t$ and $y = a\sin t$, then $\dfrac{dy}{dx}$ is:
(A) $\cot t$
(B) $-\cot t$
(C) $\tan t$
(D) $-\tan t$
@ans B
@sol $\dfrac{a\cos t}{-a\sin t} = -\cot t$.
@short —
@trap —
@@END

@@Q M07-08 | M | 1 | Monotonicity | Basic
$f(x) = x^3 - 3x$ is strictly increasing on:
(A) $(-1, 1)$
(B) $(-\infty, -1)\cup(1, \infty)$
(C) $(0, \infty)$
(D) $\mathbb R$
@ans B
@sol $f' = 3(x^2 - 1) > 0 \iff \lvert x\rvert > 1$.
@short —
@trap —
@@END

@@Q M07-09 | E | 1 | Optimisation | NV
A rectangle has perimeter 20. Find its maximum possible area.
@ans 25
@sol $A = x(10 - x)$, which is maximised at $x = 5$: $A = 25$.
@short Fixed perimeter → square.
@trap —
@@END

@@Q M07-10 | E | 1 | Rate of change | Basic
The radius of a circle grows at 0.5 cm/s. When $r = 4$ cm, its area grows at:
(A) $2\pi$ cm²/s
(B) $4\pi$ cm²/s
(C) $8\pi$ cm²/s
(D) $16\pi$ cm²/s
@ans B
@sol $\dot A = 2\pi r\dot r = 2\pi(4)(0.5) = 4\pi$.
@short —
@trap —
@@END

@@Q M07-11 | E | 0.75 | Implicit differentiation | Basic
For $x^2 + y^2 = 25$, $\dfrac{dy}{dx}$ at $(3, 4)$ is:
(A) $3/4$
(B) $-3/4$
(C) $-4/3$
(D) $4/3$
@ans B
@sol $2x + 2yy' = 0 \Rightarrow y' = -x/y = -3/4$.
@short —
@trap —
@@END

@@Q M07-12 | M | 1 | Inverse-trig simplification | Concept
For $\lvert x\rvert < 1$, $\dfrac{d}{dx}\tan^{-1}\left(\dfrac{2x}{1 - x^2}\right)$ equals:
(A) $\dfrac{1}{1 + x^2}$
(B) $\dfrac{2}{1 + x^2}$
(C) $\dfrac{2}{1 - x^2}$
(D) $\dfrac{-2}{1 + x^2}$
@ans B
@sol With $x = \tan\theta$ the expression is $\tan^{-1}(\tan2\theta) = 2\theta = 2\tan^{-1}x$ for $\lvert x\rvert < 1$.
@short —
@trap Differentiating directly (slow, error-prone).
@@END

@@SET M07 · Chapter Test

@@Q M07-T1 | E | 0.5 | Basic limit | Speed
$\displaystyle\lim_{x\to0}\frac{\tan2x}{x}$ equals:
(A) 1
(B) 2
(C) 1/2
(D) 0
@ans B
@sol —
@short —
@trap —
@@END

@@Q M07-T2 | E | 0.5 | |x| at 0 | Concept
At $x = 0$, $f(x) = \lvert x\rvert$ is:
(A) discontinuous
(B) continuous but not differentiable
(C) differentiable
(D) neither defined nor continuous
@ans B
@sol LHD = −1, RHD = +1.
@short —
@trap —
@@END

@@Q M07-T3 | M | 1 | Local maximum value | NV
Find the local maximum value of $f(x) = x^3 - 6x^2 + 9x + 1$.
@ans 5
@sol $f' = 3(x - 1)(x - 3)$. $f'' = 6x - 12 < 0$ at $x = 1$, so there's a local max: $f(1) = 5$.
@short —
@trap Giving the local minimum $f(3) = 1$.
@@END

@@Q M07-T4 | E | 0.5 | Derivative of arcsin | Speed
$\dfrac{d}{dx}\sin^{-1}x$ equals:
(A) $\dfrac{1}{\sqrt{1 - x^2}}$
(B) $-\dfrac{1}{\sqrt{1 - x^2}}$
(C) $\dfrac{1}{1 + x^2}$
(D) $\dfrac{1}{x\sqrt{x^2 - 1}}$
@ans A
@sol —
@short —
@trap —
@@END

@@Q M07-T5 | E | 0.5 | Second-derivative test | Concept
If $f'(c) = 0$ and $f''(c) < 0$, then at $x = c$, $f$ has:
(A) a local minimum
(B) a local maximum
(C) a point of inflection
(D) no conclusion possible
@ans B
@sol —
@short —
@trap —
@@END

## Answers & Solutions {#m07-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Limits & Differentiation
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
