# Sequences & Series {#m06}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 8
Study time | ~8 hours
:::

:::pyq Weight evidence
**33 questions across the 2026 Paper-1 shifts** (≈ 7% of Maths, tied for the top in that dataset) {{tag:third}} [T-WT-CD].
:::

## Core concepts

- **Arithmetic progression (AP):** constant difference $d$. **Geometric progression (GP):** constant ratio $r$.
- **Means:** inserting $n$ arithmetic or geometric means between two numbers.
- **AM ≥ GM** (equality iff all numbers are equal) is the main tool for *minimum/maximum* questions.

:::note Syllabus note
The official text lists AP, GP, insertion of AMs and GMs, and the AM–GM relation [NTA-SYL]. Sums of special series ($\sum n^2$, $\sum n^3$) and arithmetico-geometric series are **not listed**. They appear below as tools because they often shorten calculations.
:::

## Important formulas & standard results

:::formula AP
$$a_n = a + (n - 1)d \qquad S_n = \frac n2[2a + (n - 1)d] = \frac n2(a + l) \qquad a_n = S_n - S_{n-1}$$
- If $S_n$ is quadratic in $n$ ($S_n = pn^2 + qn$), the sequence is an AP with $d = 2p$.
- Three terms in AP: $a - d, a, a + d$. Four terms: $a - 3d, a - d, a + d, a + 3d$.
- $a, b, c$ in AP ⟺ $2b = a + c$.
- $n$ AMs between $a$ and $b$: $d = \dfrac{b - a}{n + 1}$; the sum of the AMs is $n\cdot\dfrac{a + b}{2}$.
:::

:::formula GP
$$a_n = ar^{n-1} \qquad S_n = \frac{a(r^n - 1)}{r - 1}\ (r \ne 1) \qquad S_\infty = \frac{a}{1 - r}\ (\lvert r\rvert < 1)$$
- Three terms in GP: $\dfrac ar, a, ar$ (their product is $a^3$).
- $a, b, c$ in GP ⟺ $b^2 = ac$.
- $n$ GMs between $a$ and $b$: $r = (b/a)^{1/(n+1)}$; the product of the GMs is $(\sqrt{ab})^n$.
- Recurring decimals: $0.\overline{3} = \dfrac{3}{9} = \dfrac13$; $0.\overline{12} = \dfrac{12}{99}$.
:::

:::formula Means & inequalities
$$\text{AM} = \frac{a + b}{2} \ \ge\ \text{GM} = \sqrt{ab} \ \ge\ \text{HM} = \frac{2ab}{a + b} \qquad \text{GM}^2 = \text{AM}\times\text{HM}\ (\text{two numbers})$$
For positive $a_i$: $\dfrac{a_1 + \dots + a_n}{n} \ge (a_1\cdots a_n)^{1/n}$. **Minimum of a sum when the product is fixed**, and **maximum of a product when the sum is fixed**, both occur at equality.
:::

:::formula Tools (not in the syllabus text)
$$\sum_{k=1}^n k = \frac{n(n+1)}{2} \qquad \sum k^2 = \frac{n(n+1)(2n+1)}{6} \qquad \sum k^3 = \left[\frac{n(n+1)}{2}\right]^2$$
Sum of the first $n$ odd numbers $= n^2$.
:::

## Common question models

:::pyq Recurring structures
1. **Find terms/sums** from two given conditions ($a_p$, $a_q$, $S_n$).
2. **$S_n$ given as a function of $n$** → $a_n$, $d$ or $r$.
3. **Three numbers in AP/GP** with given sum and product.
4. **Inserting means;** relations between AM, GM (and HM).
5. **Minimum/maximum** via AM–GM ($x + k/x$, $a^x + a^{c-x}$).
6. **Infinite GP** sums and recurring decimals; mixed AP–GP conditions.
:::

## Shortcuts & fast methods

:::shortcut Symmetric representation
Choose terms symmetric about the middle ($a - d, a, a + d$, or $a/r, a, ar$). The given sum (for an AP) or product (for a GP) then fixes $a$ immediately.
**Time saved:** removes one unknown in one step.
:::

:::shortcut AM–GM for exponentials
$a^x + a^{c-x} \ge 2\sqrt{a^c}$, with equality at $x = c/2$. Example: $4^x + 4^{1-x} \ge 2\sqrt4 = 4$.
:::

## Common mistakes

:::trap Mistake alerts
- Using $S_\infty$ when $\lvert r\rvert \ge 1$.
- $a_n = S_n - S_{n-1}$ is valid for $n \ge 2$. Check $a_1 = S_1$ separately.
- Counting terms: from 5 to 101 in steps of 4 there are $\frac{101 - 5}{4} + 1 = 25$ terms (don't forget the +1).
- AM–GM needs **positive** quantities.
:::

## Practice questions

@@SET M06 · Practice

@@Q M06-01 | E | 1 | AP from two terms | NV
In an AP, the 3rd term is 7 and the 7th term is 19. Find the 20th term.
@ans 58
@sol $4d = 12 \Rightarrow d = 3$; $a = 7 - 6 = 1$; $a_{20} = 1 + 19(3) = 58$.
@short —
@trap —
@@END

@@Q M06-02 | E | 0.5 | Finite GP sum | Speed
$1 + 2 + 4 + \dots + 2^9$ equals:
(A) 511
(B) 1023
(C) 1024
(D) 2047
@ans B
@sol $\dfrac{2^{10} - 1}{2 - 1} = 1023$ (10 terms).
@short —
@trap Counting 9 terms.
@@END

@@Q M06-03 | E | 0.75 | Infinite GP | Basic
$1 - \tfrac13 + \tfrac19 - \tfrac1{27} + \dots$ equals:
(A) $3/2$
(B) $3/4$
(C) $2/3$
(D) $1/2$
@ans B
@sol $a = 1$, $r = -\tfrac13$: $S_\infty = \dfrac{1}{4/3} = \dfrac34$.
@short —
@trap Using $r = +\tfrac13$ (gives 3/2).
@@END

@@Q M06-04 | E | 0.75 | Inserting AMs | Basic
Three arithmetic means inserted between 2 and 18 are:
(A) 6, 10, 14
(B) 4, 8, 12
(C) 5, 10, 15
(D) 6, 12, 16
@ans A
@sol $d = \dfrac{18 - 2}{4} = 4$.
@short —
@trap —
@@END

@@Q M06-05 | E | 0.5 | Geometric mean | Speed
The geometric mean of 4 and 16 is:
(A) 10
(B) 8
(C) 6.4
(D) 12
@ans B
@sol $\sqrt{64} = 8$.
@short —
@trap —
@@END

@@Q M06-06 | E | 0.75 | Minimum by AM–GM | NV
Find the minimum value of $x + \dfrac4x$ for $x > 0$.
@ans 4
@sol $x + 4/x \ge 2\sqrt4 = 4$, with equality at $x = 2$.
@short —
@trap —
@@END

@@Q M06-07 | M | 1 | Sₙ given | Concept
If $S_n = 3n^2 + 2n$, the sequence is an AP with common difference:
(A) 3
(B) 5
(C) 6
(D) 2
@ans C
@sol $a_n = S_n - S_{n-1} = 6n - 1$, so $d = 6$.
@short $d = 2\times$ (coefficient of $n^2$).
@trap —
@@END

@@Q M06-08 | M | 1.5 | Three numbers in GP | JEE
Three numbers in GP have sum 14 and product 64. Their common ratio (taking $r > 1$) is:
(A) 2
(B) 3
(C) 4
(D) 1.5
@ans A
@sol The middle term $b$ satisfies $b^3 = 64 \Rightarrow b = 4$. Then $a + c = 10$ and $ac = 16$, so the terms are 2, 4, 8 and $r = 2$.
@short Symmetric representation.
@trap —
@@END

@@Q M06-09 | M | 1 | AM–GM with exponentials | Tricky
The minimum value of $4^x + 4^{1-x}$, $x \in \mathbb R$, is:
(A) 2
(B) 4
(C) 5
(D) 1
@ans B
@sol $\ge 2\sqrt{4^x\cdot4^{1-x}} = 2\sqrt4 = 4$, attained at $x = \tfrac12$.
@short —
@trap Assuming the minimum is at $x = 0$ (gives 5).
@@END

@@Q M06-10 | E | 0.5 | Sum of squares | NV
Find $\sum_{k=1}^{10}k^2$.
@ans 385
@sol $\dfrac{10\cdot11\cdot21}{6} = 385$.
@short —
@trap —
@@END

@@SET M06 · Chapter Test

@@Q M06-T1 | E | 0.5 | Sum of odd numbers | Speed
The sum of the first $n$ odd natural numbers is:
(A) $n(n + 1)$
(B) $n^2$
(C) $2n^2$
(D) $n^2 + 1$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M06-T2 | E | 0.75 | Three numbers in AP | Basic
Three numbers in AP have sum 15 and product 105. The numbers are:
(A) 3, 5, 7
(B) 1, 5, 9
(C) 2, 5, 8
(D) 4, 5, 6
@ans A
@sol The middle term is 5. $(5 - d)(5 + d) = 21 \Rightarrow d = 2$.
@short —
@trap —
@@END

@@Q M06-T3 | E | 0.5 | Counting terms | NV
How many terms are in the AP $5, 9, 13, \dots, 101$?
@ans 25
@sol $\dfrac{101 - 5}{4} + 1 = 25$.
@short —
@trap Forgetting the +1.
@@END

@@Q M06-T4 | E | 0.5 | AM–GM equality | Concept
For positive $a$ and $b$, AM = GM exactly when:
(A) $a = 2b$
(B) $a = b$
(C) $ab = 1$
(D) always
@ans B
@sol $\text{AM} - \text{GM} = \tfrac12(\sqrt a - \sqrt b)^2 \ge 0$, which is zero iff $a = b$.
@short —
@trap —
@@END

@@Q M06-T5 | E | 0.5 | Recurring decimal | Speed
$0.3 + 0.03 + 0.003 + \dots$ equals:
(A) 0.33
(B) $1/3$
(C) $3/10$
(D) $10/3$
@ans B
@sol $\dfrac{0.3}{1 - 0.1} = \dfrac13$.
@short —
@trap —
@@END

## Answers & Solutions {#m06-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Sequences & Series
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
