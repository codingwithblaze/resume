# Sets, Relations & Functions {#m01}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy–Medium
Priority | High
NCERT | Class 11 · Ch 1, 2; Class 12 · Ch 1
Study time | ~8 hours
:::

## Core concepts

- **Sets:** union, intersection, complement, difference; De Morgan's laws; power set; Cartesian product.
- **Relations** from A to B are subsets of $A\times B$. On a single set they can be reflexive, symmetric, transitive, or all three (**equivalence**).
- **Functions** assign exactly one output to each input. They can be one-one (injective), onto (surjective) or both (bijective). Only bijections have inverses.
- Composition $(f\circ g)(x) = f(g(x))$ is associative but generally **not commutative**.

## Important formulas & standard results

:::formula Sets
$$n(A\cup B) = n(A) + n(B) - n(A\cap B)$$
$$n(A\cup B\cup C) = \sum n(A) - \sum n(A\cap B) + n(A\cap B\cap C)$$
$(A\cup B)' = A'\cap B'$, $(A\cap B)' = A'\cup B'$ (De Morgan). $|P(A)| = 2^n$. $n(A\times B) = n(A)\,n(B)$.
:::

:::formula Counting relations and functions ($|A| = m$, $|B| = n$; relations on a set of size $n$)
| Object | Number |
|---|---|
| Relations from A to B | $2^{mn}$ |
| Relations on a set | $2^{n^2}$ |
| Reflexive relations | $2^{n^2 - n}$ |
| Symmetric relations | $2^{n(n+1)/2}$ |
| Reflexive **and** symmetric | $2^{n(n-1)/2}$ |
| Functions A → B | $n^m$ |
| One-one functions ($m \le n$) | $^nP_m = \dfrac{n!}{(n-m)!}$ |
| Onto functions (A → B) | $\sum_{k=0}^{n}(-1)^k\binom nk(n-k)^m$; for $n = 2$: $2^m - 2$ |
| Bijections ($m = n$) | $n!$ |
:::

:::formula Domain & range rules
- $\sqrt{g(x)}$ needs $g(x) \ge 0$; $\log g(x)$ needs $g(x) > 0$; $\dfrac{1}{g(x)}$ needs $g(x) \ne 0$; $\sin^{-1}g(x)$, $\cos^{-1}g(x)$ need $-1 \le g(x) \le 1$. With $\log_{g(x)}$ also $g(x) \ne 1$.
- **Range:** solve $y = f(x)$ for $x$ and find the $y$ values that give a valid $x$; or use monotonicity/AM–GM.
- $\dfrac{x^2}{1 + x^2} \in [0, 1)$; $x + \dfrac1x \ge 2$ for $x > 0$; $a\sin x + b\cos x \in [-\sqrt{a^2 + b^2}, \sqrt{a^2 + b^2}]$.
:::

:::formula Special functions
| Function | Key facts |
|---|---|
| $\lvert x\rvert$ | even; $\sqrt{x^2} = \lvert x\rvert$ |
| Greatest integer $[x]$ | $[x] \le x < [x] + 1$; $[x + n] = [x] + n$ for integer $n$; $[-2.3] = -3$ |
| Fractional part $\{x\} = x - [x]$ | $0 \le \{x\} < 1$; period 1 |
| Signum $\operatorname{sgn}x$ | $1, 0, -1$ for $x > 0, = 0, < 0$ |
| Even / odd | $f(-x) = f(x)$ / $f(-x) = -f(x)$. Every $f$ = even part + odd part |
| Periods | $\sin kx$, $\cos kx$: $2\pi/\lvert k\rvert$; $\tan kx$: $\pi/\lvert k\rvert$; $\lvert\sin x\rvert$: $\pi$; $\lvert\sin x\rvert + \lvert\cos x\rvert$: $\pi/2$; $\{x\}$: 1 |
:::

## Common question models

:::pyq Recurring structures
1. **Classify a relation** (reflexive/symmetric/transitive/equivalence) defined on a small set or by a rule (e.g. $a - b$ divisible by 3).
2. **Count** relations/functions with a property (onto, one-one, reflexive, symmetric).
3. **Domain of a composite expression** with roots, logs and inverse trig.
4. **Range** of rational or trigonometric functions.
5. **Inverse / composition**: $f^{-1}(x)$, $f\circ g$, solving $f(x) = f^{-1}(x)$.
6. **Venn-diagram counting** with 2–3 sets.
:::

## Shortcuts & formula recognition

:::shortcut Equivalence test in 30 seconds
For a relation given as a list of pairs, check **reflexive** first (all $(a,a)$ present?), then **symmetric** (is every pair's reverse present?). Only if both pass, check **transitive**, and only on chains of pairs with a shared middle element. Most relations fail at the first two checks, which saves the slowest check.
:::

:::shortcut Inverse of a Möbius function
If $f(x) = \dfrac{ax + b}{cx + d}$, then $f^{-1}(x) = \dfrac{dx - b}{-cx + a}$: swap $a$ and $d$, negate $b$ and $c$.
**When NOT to use:** when the function isn't of this form, or when the domain restricts the inverse.
:::

## Common mistakes

:::trap Mistake alerts
- $\sqrt{x^2} = \lvert x\rvert$, not $x$. So $g(f(x))$ with $f = x^2$, $g = \sqrt{\ }$ gives $\lvert x\rvert$.
- Onto-ness depends on the **codomain**. The same rule can be onto or not.
- $[x]$ for negative numbers: $[-0.5] = -1$.
- Forgetting $g(x) \ne 1$ for a logarithm's base, or $\ne 0$ for a denominator, when finding the domain.
:::

## Practice questions

@@SET M01 · Practice

@@Q M01-01 | E | 0.5 | Counting relations | Speed
The number of relations on a set with 3 elements is:
(A) 9
(B) 64
(C) 512
(D) 8
@ans C
@sol $2^{n^2} = 2^9 = 512$.
@short —
@trap Using $2^n$.
@@END

@@Q M01-02 | E | 1 | Equivalence relation check | Concept
On $A = \{1, 2, 3\}$, $R = \{(1,1), (2,2), (3,3), (1,2), (2,1)\}$ is:
(A) reflexive only
(B) symmetric only
(C) an equivalence relation
(D) transitive but not symmetric
@ans C
@sol Reflexive (all $(a,a)$ present), symmetric ($(1,2)$ and $(2,1)$), transitive (the only chains give $(1,1)$ and $(2,2)$, both present).
@short The classes are $\{1,2\}$ and $\{3\}$: a partition, so it's an equivalence.
@trap —
@@END

@@Q M01-03 | E | 1 | Onto functions onto a 2-set | NV
Find the number of onto functions from a 4-element set to a 2-element set.
@ans 14
@sol Total functions $2^4 = 16$, minus the 2 constant functions: 14.
@short Onto a 2-set: $2^m - 2$.
@trap Forgetting to subtract.
@@END

@@Q M01-04 | M | 1.5 | Domain with root and log | JEE
The domain of $f(x) = \sqrt{x - 1} + \dfrac{1}{\log_e(2 - x)}$ is:
(A) $[1, 2)$
(B) $(1, 2)$
(C) $[1, 2]$
(D) $(-\infty, 2)$
@ans B
@sol Need $x \ge 1$, $2 - x > 0$ and $\log(2 - x) \ne 0$, i.e. $x \ne 1$. Together: $(1, 2)$.
@short Check the endpoint $x = 1$: it makes the log zero.
@trap Missing the denominator condition gives $[1, 2)$.
@@END

@@Q M01-05 | E | 0.5 | Union of two sets | Speed
If $n(A) = 40$, $n(B) = 30$ and $n(A\cap B) = 10$, then $n(A\cup B)$ is:
(A) 70
(B) 60
(C) 80
(D) 50
@ans B
@sol $40 + 30 - 10 = 60$.
@short —
@trap —
@@END

@@Q M01-06 | M | 1 | Inverse of a rational function | Basic
If $f(x) = \dfrac{2x + 3}{x - 1}$ ($x \ne 1$), then $f^{-1}(x)$ is:
(A) $\dfrac{x + 3}{x - 2}$
(B) $\dfrac{x - 1}{2x + 3}$
(C) $\dfrac{x - 3}{x + 2}$
(D) $\dfrac{2x - 3}{x + 1}$
@ans A
@sol $y(x - 1) = 2x + 3 \Rightarrow x(y - 2) = y + 3 \Rightarrow x = \dfrac{y + 3}{y - 2}$.
@short Möbius rule: swap $a = 2$ and $d = -1$, negate $b$ and $c$: $\dfrac{-x - 3}{-x + 2}$, which equals (A).
@trap Taking the reciprocal (B).
@@END

@@Q M01-07 | M | 1 | Period of a sum | Concept
The fundamental period of $f(x) = \lvert\sin x\rvert + \lvert\cos x\rvert$ is:
(A) $2\pi$
(B) $\pi$
(C) $\pi/2$
(D) $\pi/4$
@ans C
@sol $f(x + \pi/2) = \lvert\cos x\rvert + \lvert\sin x\rvert = f(x)$, and no smaller positive period works.
@short —
@trap Taking the LCM of the individual periods ($\pi$) without checking a smaller value.
@@END

@@Q M01-08 | E | 0.75 | Counting reflexive relations | NV
Find the number of reflexive relations on a set with 3 elements.
@ans 64
@sol The 3 diagonal pairs must be included; each of the remaining 6 pairs is optional: $2^6 = 64$.
@short $2^{n^2 - n}$.
@trap —
@@END

@@Q M01-09 | M | 1 | Range of a rational function | Concept
The range of $f(x) = \dfrac{x^2}{1 + x^2}$, $x \in \mathbb R$, is:
(A) $[0, 1]$
(B) $[0, 1)$
(C) $(0, 1)$
(D) $[0, \infty)$
@ans B
@sol $f = 1 - \dfrac{1}{1 + x^2}$. At $x = 0$, $f = 0$; as $\lvert x\rvert \to \infty$, $f \to 1$ but never reaches it.
@short —
@trap Including 1.
@@END

@@Q M01-10 | M | 1 | Composition with square root | Tricky
If $f(x) = x^2$ and $g(x) = \sqrt x$ ($x \ge 0$), then $(g\circ f)(x)$ for real $x$ is:
(A) $x$
(B) $\lvert x\rvert$
(C) $x^2$
(D) not defined for $x < 0$
@ans B
@sol $g(f(x)) = \sqrt{x^2} = \lvert x\rvert$, which is defined for all real $x$ because $x^2 \ge 0$.
@short —
@trap Writing $x$.
@@END

@@SET M01 · Chapter Test

@@Q M01-T1 | E | 0.5 | Power set | Speed
A set has 4 elements. Its power set has:
(A) 8 elements
(B) 16 elements
(C) 4 elements
(D) 24 elements
@ans B
@sol $2^4 = 16$.
@short —
@trap —
@@END

@@Q M01-T2 | E | 0.5 | Bijective linear function | Speed
$f:\mathbb R \to \mathbb R$, $f(x) = 3x + 5$ is:
(A) one-one but not onto
(B) onto but not one-one
(C) bijective
(D) neither
@ans C
@sol A non-constant linear function on $\mathbb R$ is strictly monotonic and takes every real value.
@short —
@trap —
@@END

@@Q M01-T3 | E | 0.5 | Counting one-one functions | NV
Find the number of one-one functions from $\{a, b\}$ to $\{1, 2, 3, 4\}$.
@ans 12
@sol $^4P_2 = 4\times3 = 12$.
@short —
@trap —
@@END

@@Q M01-T4 | E | 0.75 | Even function | Concept
Which function is even?
(A) $x\sin x$
(B) $x\cos x$
(C) $x + \sin x$
(D) $e^x$
@ans A
@sol odd × odd = even. $x\cos x$ and $x + \sin x$ are odd; $e^x$ is neither.
@short —
@trap —
@@END

@@Q M01-T5 | E | 0.5 | Greatest integer function | Speed
$[-2.3]$ (greatest integer function) equals:
(A) −2
(B) −3
(C) 2
(D) −2.3
@ans B
@sol The greatest integer ≤ −2.3 is −3.
@short —
@trap Truncating to −2.
@@END

## Answers & Solutions {#m01-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Sets, Relations & Functions
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
