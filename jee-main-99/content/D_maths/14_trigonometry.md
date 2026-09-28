# Trigonometry & Inverse Trigonometric Functions {#m14}

:::stats
Typical questions | ~1 per shift
Difficulty | Easy–Medium
Priority | High (also a tool for calculus and complex numbers)
NCERT | Class 11 · Ch 3 · Class 12 · Ch 2
Study time | ~6 hours
:::

## Core concepts

- **Trigonometric functions** of any angle: signs by quadrant, allied-angle reduction, periodicity.
- **Identities:** compound, multiple and sub-multiple angles; sum ↔ product conversions.
- **Inverse trigonometric functions:** principal-value branches, domains and ranges, and the standard properties.
- Trigonometry appears inside other chapters far more often than as its own question. Calculus, complex numbers (polar form) and conics (parametric form) all rely on it.

:::note Syllabus note
The official Unit 14 text lists trigonometric identities, trigonometric functions, inverse trigonometric functions and their properties [NTA-SYL]. Heights and distances were removed in 2024. Trigonometric *equations* are not named separately, but general solutions are included below because identity and inverse-trig questions often reduce to solving one {{tag:rec}}.
:::

## Important formulas: identities

:::formula Compound & multiple angles
$$\sin(A \pm B) = \sin A\cos B \pm \cos A\sin B \qquad \cos(A \pm B) = \cos A\cos B \mp \sin A\sin B \qquad \tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A\tan B}$$
$$\sin2A = 2\sin A\cos A = \frac{2\tan A}{1 + \tan^2A} \qquad \cos2A = 1 - 2\sin^2A = 2\cos^2A - 1 = \frac{1 - \tan^2A}{1 + \tan^2A}$$
$$\sin3A = 3\sin A - 4\sin^3A \qquad \cos3A = 4\cos^3A - 3\cos A \qquad \tan3A = \frac{3\tan A - \tan^3A}{1 - 3\tan^2A}$$
:::

:::formula Sum ↔ product
$$\sin C + \sin D = 2\sin\tfrac{C + D}{2}\cos\tfrac{C - D}{2} \qquad \cos C + \cos D = 2\cos\tfrac{C + D}{2}\cos\tfrac{C - D}{2}$$
$$\sin C - \sin D = 2\cos\tfrac{C + D}{2}\sin\tfrac{C - D}{2} \qquad \cos C - \cos D = -2\sin\tfrac{C + D}{2}\sin\tfrac{C - D}{2}$$
$2\sin A\cos B = \sin(A + B) + \sin(A - B)$; $2\cos A\cos B = \cos(A + B) + \cos(A - B)$; $2\sin A\sin B = \cos(A - B) - \cos(A + B)$.
:::

:::formula Standard values & special products
| Angle | $\sin$ | $\cos$ | $\tan$ |
|---|---|---|---|
| $15^\circ$ | $\dfrac{\sqrt6 - \sqrt2}{4}$ | $\dfrac{\sqrt6 + \sqrt2}{4}$ | $2 - \sqrt3$ |
| $18^\circ$ | $\dfrac{\sqrt5 - 1}{4}$ | $\dfrac{\sqrt{10 + 2\sqrt5}}{4}$ | — |
| $36^\circ$ | $\dfrac{\sqrt{10 - 2\sqrt5}}{4}$ | $\dfrac{\sqrt5 + 1}{4}$ | — |
| $22.5^\circ$ | $\dfrac{\sqrt{2 - \sqrt2}}{2}$ | $\dfrac{\sqrt{2 + \sqrt2}}{2}$ | $\sqrt2 - 1$ |

$\sin\theta\sin(60^\circ - \theta)\sin(60^\circ + \theta) = \tfrac14\sin3\theta$; $\cos\theta\cos(60^\circ - \theta)\cos(60^\circ + \theta) = \tfrac14\cos3\theta$; $\tan\theta\tan(60^\circ - \theta)\tan(60^\circ + \theta) = \tan3\theta$.
$\cos A\cos2A\cos4A\cdots\cos2^{n-1}A = \dfrac{\sin2^nA}{2^n\sin A}$.
:::

:::formula Range & conditional identities
$a\sin x + b\cos x \in \left[-\sqrt{a^2 + b^2},\ \sqrt{a^2 + b^2}\right]$.
If $A + B + C = \pi$: $\tan A + \tan B + \tan C = \tan A\tan B\tan C$ and $\sin2A + \sin2B + \sin2C = 4\sin A\sin B\sin C$.
**General solutions:** $\sin\theta = \sin\alpha \Rightarrow \theta = n\pi + (-1)^n\alpha$; $\cos\theta = \cos\alpha \Rightarrow \theta = 2n\pi \pm \alpha$; $\tan\theta = \tan\alpha \Rightarrow \theta = n\pi + \alpha$ ($n \in \mathbb Z$).
:::

## Important formulas: inverse trigonometric functions

:::formula Principal branches
| Function | Domain | Range (principal) |
|---|---|---|
| $\sin^{-1}x$ | $[-1, 1]$ | $[-\pi/2, \pi/2]$ |
| $\cos^{-1}x$ | $[-1, 1]$ | $[0, \pi]$ |
| $\tan^{-1}x$ | $\mathbb R$ | $(-\pi/2, \pi/2)$ |
| $\cot^{-1}x$ | $\mathbb R$ | $(0, \pi)$ |
| $\sec^{-1}x$ | $\lvert x\rvert \ge 1$ | $[0, \pi] - \{\pi/2\}$ |
| $\csc^{-1}x$ | $\lvert x\rvert \ge 1$ | $[-\pi/2, \pi/2] - \{0\}$ |
:::

:::formula Properties
$\sin^{-1}x + \cos^{-1}x = \tan^{-1}x + \cot^{-1}x = \sec^{-1}x + \csc^{-1}x = \dfrac\pi2$.
**Negative arguments:** $\sin^{-1}(-x) = -\sin^{-1}x$ and $\tan^{-1}(-x) = -\tan^{-1}x$, but $\cos^{-1}(-x) = \pi - \cos^{-1}x$ and $\cot^{-1}(-x) = \pi - \cot^{-1}x$.
$$\tan^{-1}x + \tan^{-1}y = \tan^{-1}\frac{x + y}{1 - xy}\ (xy < 1) \qquad \tan^{-1}x - \tan^{-1}y = \tan^{-1}\frac{x - y}{1 + xy}\ (xy > -1)$$
For $x, y > 0$ and $xy > 1$, add $\pi$ to the sum formula.
$2\tan^{-1}x = \sin^{-1}\dfrac{2x}{1 + x^2}$ ($\lvert x\rvert \le 1$) $= \cos^{-1}\dfrac{1 - x^2}{1 + x^2}$ ($x \ge 0$) $= \tan^{-1}\dfrac{2x}{1 - x^2}$ ($\lvert x\rvert < 1$).
**Compositions:** $\sin^{-1}(\sin x) = x$ only for $x \in [-\pi/2, \pi/2]$. For $x \in [\pi/2, 3\pi/2]$ it equals $\pi - x$. Always reduce into the principal range first.
:::

## Common question models

:::pyq Recurring structures
1. **Evaluate** expressions like $\sin^{-1}(\sin\tfrac{5\pi}{6})$ or $\cos^{-1}(\cos\tfrac{7\pi}{6})$ (principal-range traps).
2. **Sums of $\tan^{-1}$** and **telescoping series** $\sum\tan^{-1}\dfrac{1}{1 + k + k^2} = \sum[\tan^{-1}(k + 1) - \tan^{-1}k]$.
3. **Maximum/minimum** of $a\sin x + b\cos x + c$, or via AM–GM.
4. **Special products** ($\cos20^\circ\cos40^\circ\cos80^\circ$) and standard values.
5. **Number of solutions** of an equation in an interval (graph both sides).
6. **Domain questions** involving inverse trig functions (often inside Sets & Functions).
:::

## Shortcuts & fast methods

:::shortcut Telescoping $\tan^{-1}$
Write the general term as $\tan^{-1}\dfrac{b - a}{1 + ab} = \tan^{-1}b - \tan^{-1}a$. For $\dfrac{1}{1 + k(k + 1)}$, take $a = k$ and $b = k + 1$. The sum up to $n$ collapses to $\tan^{-1}(n + 1) - \tan^{-1}1$.
**Time saved:** 3–4 minutes compared with adding terms.
:::

:::shortcut Substitute a value
For identity-type MCQs, put $\theta = 0$, $\tfrac\pi4$ or $\tfrac\pi6$ in both the expression and each option. Two values usually leave one option (Answer-Choice Strategy, page [[answer-choice]]).
:::

## Common mistakes

:::trap Mistake alerts
- $\cos^{-1}\left(-\tfrac12\right) = \tfrac{2\pi}{3}$, not $-\tfrac\pi3$: the range of $\cos^{-1}$ is $[0, \pi]$.
- $\sin^{-1}(\sin x) = x$ only in the principal range.
- Applying the $\tan^{-1}$ sum formula without checking $xy < 1$.
- $\sin^{-1}x \ne \dfrac{1}{\sin x}$. The notation means the inverse function.
- Squaring an equation introduces extra roots. Check each solution in the original.
:::

## Practice questions

@@SET M14 · Practice

@@Q M14-01 | E | 0.5 | Range of a sin x + b cos x | NV
Find the maximum value of $3\sin x + 4\cos x$.
@ans 5
@sol $\sqrt{9 + 16} = 5$.
@short —
@trap —
@@END

@@Q M14-02 | E | 0.5 | Standard value | Speed
$\sin15^\circ$ equals:
(A) $\dfrac{\sqrt6 - \sqrt2}{4}$
(B) $\dfrac{\sqrt6 + \sqrt2}{4}$
(C) $\dfrac{\sqrt3 - 1}{2}$
(D) $\dfrac{2 - \sqrt3}{4}$
@ans A
@sol $\sin(45^\circ - 30^\circ) = \dfrac{1}{\sqrt2}\cdot\dfrac{\sqrt3}{2} - \dfrac{1}{\sqrt2}\cdot\dfrac12$.
@short $\sin15^\circ \approx 0.26$; only (A) is close ($\approx 0.259$).
@trap —
@@END

@@Q M14-03 | E | 0.5 | Compound angle | Speed
$\tan75^\circ$ equals:
(A) $2 - \sqrt3$
(B) $2 + \sqrt3$
(C) $\sqrt3 + 1$
(D) $\dfrac{\sqrt3 + 1}{2}$
@ans B
@sol $\tan(45^\circ + 30^\circ) = \dfrac{1 + 1/\sqrt3}{1 - 1/\sqrt3} = \dfrac{\sqrt3 + 1}{\sqrt3 - 1} = 2 + \sqrt3$.
@short —
@trap —
@@END

@@Q M14-04 | E | 0.75 | Principal value | Tricky
$\sin^{-1}\left(\sin\dfrac{2\pi}{3}\right)$ equals:
(A) $\dfrac{2\pi}{3}$
(B) $\dfrac{\pi}{3}$
(C) $-\dfrac{\pi}{3}$
(D) $\dfrac{\pi}{6}$
@ans B
@sol $\sin\dfrac{2\pi}{3} = \sin\dfrac\pi3$, and $\dfrac\pi3$ lies in $[-\tfrac\pi2, \tfrac\pi2]$.
@short —
@trap Cancelling $\sin^{-1}$ and $\sin$ directly.
@@END

@@Q M14-05 | E | 0.75 | Sum of inverse tangents | Basic
$\tan^{-1}\dfrac12 + \tan^{-1}\dfrac13$ equals:
(A) $\dfrac\pi4$
(B) $\dfrac\pi3$
(C) $\dfrac\pi6$
(D) $\dfrac\pi2$
@ans A
@sol $\dfrac{1/2 + 1/3}{1 - 1/6} = 1$.
@short —
@trap —
@@END

@@Q M14-06 | M | 1 | Special product | JEE
$\cos20^\circ\cos40^\circ\cos80^\circ$ equals:
(A) $\tfrac18$
(B) $\tfrac14$
(C) $\tfrac{\sqrt3}{8}$
(D) $\tfrac1{16}$
@ans A
@sol With $\theta = 20^\circ$: $\cos\theta\cos(60^\circ - \theta)\cos(60^\circ + \theta) = \tfrac14\cos60^\circ = \tfrac18$.
@short —
@trap —
@@END

@@Q M14-07 | E | 0.5 | Counting solutions | NV
How many solutions does $\sin x = \dfrac12$ have in $[0, 2\pi]$?
@ans 2
@sol $x = \dfrac\pi6$ and $\dfrac{5\pi}{6}$.
@short —
@trap —
@@END

@@Q M14-08 | M | 1 | Squaring an identity | Basic
If $\sin\theta + \cos\theta = \dfrac15$, then $\sin2\theta$ equals:
(A) $-\dfrac{24}{25}$
(B) $\dfrac{24}{25}$
(C) $-\dfrac{12}{25}$
(D) $\dfrac{1}{25}$
@ans A
@sol Squaring: $1 + \sin2\theta = \dfrac{1}{25}$.
@short —
@trap —
@@END

@@Q M14-09 | M | 1 | AM–GM minimum | NV
Find the minimum value of $9\tan^2\theta + 4\cot^2\theta$.
@ans 12
@sol AM–GM: $\ge 2\sqrt{36} = 12$, attained when $\tan^2\theta = \tfrac23$.
@short —
@trap —
@@END

@@Q M14-10 | E | 0.5 | Principal value of cos⁻¹ | Tricky
$\cos^{-1}\left(-\dfrac12\right)$ equals:
(A) $-\dfrac\pi3$
(B) $\dfrac{2\pi}{3}$
(C) $\dfrac{\pi}{3}$
(D) $\dfrac{4\pi}{3}$
@ans B
@sol $\pi - \cos^{-1}\tfrac12 = \pi - \dfrac\pi3$.
@short —
@trap Answering $-\tfrac\pi3$, which lies outside $[0, \pi]$.
@@END

@@Q M14-11 | E | 0.5 | Complementary inverses | Speed
If $\sin^{-1}x = \dfrac\pi5$, then $\cos^{-1}x$ equals:
(A) $\dfrac{3\pi}{10}$
(B) $\dfrac{4\pi}{5}$
(C) $\dfrac{\pi}{5}$
(D) $\dfrac{7\pi}{10}$
@ans A
@sol $\dfrac\pi2 - \dfrac\pi5 = \dfrac{3\pi}{10}$.
@short —
@trap —
@@END

@@Q M14-12 | M | 1.5 | Range of a combination | Tricky
The range of $f(x) = \sin^{-1}x + \cos^{-1}x + \tan^{-1}x$ is:
(A) $\left[\dfrac\pi4, \dfrac{3\pi}{4}\right]$
(B) $[0, \pi]$
(C) $\left(-\dfrac\pi2, \dfrac\pi2\right)$
(D) $\left[\dfrac\pi2, \pi\right]$
@ans A
@sol $f(x) = \dfrac\pi2 + \tan^{-1}x$ with $x \in [-1, 1]$ (the domain of $\sin^{-1}$), so $\tan^{-1}x \in [-\tfrac\pi4, \tfrac\pi4]$.
@short —
@trap Using the full range of $\tan^{-1}$ and ignoring the domain restriction.
@@END

@@Q M14-13 | M | 1 | Double-angle inverse | Concept
$2\tan^{-1}\dfrac13$ equals:
(A) $\tan^{-1}\dfrac34$
(B) $\tan^{-1}\dfrac23$
(C) $\tan^{-1}\dfrac43$
(D) $\tan^{-1}\dfrac19$
@ans A
@sol $\tan^{-1}\dfrac{2/3}{1 - 1/9} = \tan^{-1}\dfrac{2/3}{8/9} = \tan^{-1}\dfrac34$.
@short —
@trap —
@@END

@@SET M14 · Chapter Test

@@Q M14-T1 | E | 0.5 | Double angle in tan | Speed
$\cos2\theta$ equals:
(A) $\dfrac{1 - \tan^2\theta}{1 + \tan^2\theta}$
(B) $\dfrac{2\tan\theta}{1 + \tan^2\theta}$
(C) $\dfrac{1 + \tan^2\theta}{1 - \tan^2\theta}$
(D) $\dfrac{2\tan\theta}{1 - \tan^2\theta}$
@ans A
@sol —
@short —
@trap —
@@END

@@Q M14-T2 | M | 0.75 | Principal values | Tricky
$\tan^{-1}\sqrt3 - \sec^{-1}(-2)$ equals:
(A) $-\dfrac\pi3$
(B) $\pi$
(C) $\dfrac\pi3$
(D) $0$
@ans A
@sol $\dfrac\pi3 - \dfrac{2\pi}{3}$ (the range of $\sec^{-1}$ is $[0, \pi] - \{\tfrac\pi2\}$).
@short —
@trap Taking $\sec^{-1}(-2) = -\tfrac\pi3$.
@@END

@@Q M14-T3 | E | 0.5 | Maximum of a product | Speed
The maximum value of $\sin x\cos x$ is:
(A) $\tfrac12$
(B) 1
(C) $\tfrac{1}{\sqrt2}$
(D) 2
@ans A
@sol $\tfrac12\sin2x \le \tfrac12$.
@short —
@trap —
@@END

@@Q M14-T4 | E | 0.5 | Standard value | Speed
$\sin18^\circ$ equals:
(A) $\dfrac{\sqrt5 - 1}{4}$
(B) $\dfrac{\sqrt5 + 1}{4}$
(C) $\dfrac{\sqrt5 - 1}{2}$
(D) $\dfrac{\sqrt3 - 1}{4}$
@ans A
@sol —
@short $\sin18^\circ \approx 0.309$ and $(\sqrt5 - 1)/4 \approx 0.309$.
@trap Confusing it with $\cos36^\circ = (\sqrt5 + 1)/4$.
@@END

@@Q M14-T5 | M | 0.75 | Product of tangents | NV
Find $\tan1^\circ\tan2^\circ\tan3^\circ\cdots\tan89^\circ$.
@ans 1
@sol Pair $\tan\theta\tan(90^\circ - \theta) = 1$. The middle term is $\tan45^\circ = 1$.
@short —
@trap —
@@END

## Answers & Solutions {#m14-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Trigonometry
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
