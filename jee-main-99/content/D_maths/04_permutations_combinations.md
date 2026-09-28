# Permutations & Combinations {#m04}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 6
Study time | ~10 hours
:::

## Core concepts

- **Fundamental principle of counting:** independent stages multiply (AND). Mutually exclusive alternatives add (OR).
- **Permutation** = arrangement (order matters): $^nP_r$. **Combination** = selection (order doesn't matter): $^nC_r$.
- Most JEE questions are **counting with constraints**: identical objects, restrictions (together/apart), circular arrangements, distributions, digits.

## Important formulas & standard results

:::formula Core formulas
$$^nP_r = \frac{n!}{(n-r)!} \qquad ^nC_r = \frac{n!}{r!(n-r)!} \qquad ^nC_r = {}^nC_{n-r} \qquad ^nC_r + {}^nC_{r-1} = {}^{n+1}C_r$$
$$^nC_x = {}^nC_y \Rightarrow x = y\ \text{or}\ x + y = n \qquad \frac{^nC_r}{^nC_{r-1}} = \frac{n - r + 1}{r} \qquad r\,{}^nC_r = n\,{}^{n-1}C_{r-1}$$
:::

:::formula Arrangements
| Situation | Count |
|---|---|
| $n$ distinct objects in a row | $n!$ |
| $n$ objects with $p$ alike, $q$ alike, … | $\dfrac{n!}{p!\,q!\cdots}$ |
| $r$ from $n$ with repetition allowed | $n^r$ |
| Circular arrangement of $n$ distinct objects | $(n - 1)!$ |
| Circular, clockwise = anticlockwise (necklace, garland) | $\dfrac{(n - 1)!}{2}$ |
| $k$ particular objects **together** | $(n - k + 1)!\,k!$ |
| No two of $k$ particular objects together (gap method) | $(n - k)!\cdot{}^{n-k+1}P_k$ |
| Derangements of $n$ objects (useful tool) | $D_n = n!\sum_{k=0}^{n}\dfrac{(-1)^k}{k!}$: $D_2 = 1$, $D_3 = 2$, $D_4 = 9$, $D_5 = 44$ |
:::

:::formula Selections & distributions
- At least one from $n$ distinct objects: $2^n - 1$. From $p$ alike + $q$ alike + $r$ alike: $(p + 1)(q + 1)(r + 1) - 1$.
- Divisors of $N = p^aq^br^c$: $(a + 1)(b + 1)(c + 1)$ (including 1 and $N$).
- $n$ **identical** objects into $r$ distinct boxes: $^{n+r-1}C_{r-1}$ (empty allowed); $^{n-1}C_{r-1}$ (none empty). The same counts give non-negative/positive integer solutions of $x_1 + \dots + x_r = n$.
- Dividing $m + n$ distinct objects into groups of $m$ and $n$ ($m \ne n$): $\dfrac{(m + n)!}{m!\,n!}$. Into two **equal** unlabelled groups of $n$: $\dfrac{(2n)!}{2!\,(n!)^2}$.
- Geometry: lines through $n$ points (no 3 collinear): $^nC_2$; triangles: $^nC_3$; diagonals of an $n$-gon: $^nC_2 - n$.
:::

## Common question models

:::pyq Recurring structures
1. **Word arrangements** (with repeated letters, vowels together/apart, rank of a word in dictionary order).
2. **Digit problems:** numbers formed under conditions (even, divisible by 3/5, greater than a value, digits not repeated).
3. **Selections with constraints:** committees containing at least/at most $k$ of a type.
4. **Distributions:** identical balls into boxes; integer solutions.
5. **Circular arrangements** with restrictions.
6. **Geometry counting:** lines, triangles, diagonals, rectangles in a grid.
:::

## Shortcuts & fast methods

:::shortcut "At least" by complement
Count = total − (count with none). For "at least 2", subtract the cases with 0 and with 1. This almost always has fewer cases than direct counting.
**When NOT to use:** when the complement is harder (e.g. "exactly 3").
:::

:::shortcut Divisibility by 3 in digit problems
A number is divisible by 3 iff its digit sum is. Group the digits into residue classes mod 3, pick combinations whose sum is ≡ 0, then arrange. Handle the "0 can't lead" rule last, by subtraction.
:::

:::shortcut Rank of a word
Go letter by letter. For each position, count the letters **smaller** than the current letter still unused, and multiply by the arrangements of the remaining letters (divide for repeats). Add 1 at the end.
:::

## Common mistakes

:::trap Mistake alerts
- Treating selections as arrangements: a committee is a combination; a line-up is a permutation.
- Leading zero in digit problems.
- Circular arrangements of **identical-looking** necklace beads: divide by 2.
- "Groups" vs "boxes": unlabelled groups of equal size need an extra division by $k!$.
- Adding when you should multiply. Ask whether it's "and then" (×) or "either/or" (+).
:::

## Practice questions

@@SET M04 · Practice

@@Q M04-01 | E | 1 | Vowels together | Basic
The number of arrangements of the letters of TRIANGLE in which the three vowels (I, A, E) are together is:
(A) 720
(B) 4320
(C) 5040
(D) 1440
@ans B
@sol Treat the vowels as one block: 6 units, so $6!$ arrangements, times $3!$ inside the block: $720\times6 = 4320$.
@short —
@trap Forgetting the internal $3!$.
@@END

@@Q M04-02 | M | 1.5 | Gap method | Concept
The number of ways to arrange 5 boys and 3 girls in a row so that no two girls are together is:
(A) $5!\times{}^6P_3$
(B) $5!\times{}^6C_3$
(C) $8! - 3!\,6!$
(D) $5!\times3!$
@ans A
@sol Arrange the boys ($5!$), which creates 6 gaps. Place the girls in 3 of those gaps in order: $^6P_3$. Total $= 120\times120 = 14\,400$.
@short —
@trap Using $^6C_3$ (forgetting that the girls are distinct).
@@END

@@Q M04-03 | M | 1.5 | Committee with at least one woman | NV
From 6 men and 4 women, a committee of 3 is formed. Find the number of committees with **at least one** woman.
@ans 100
@sol Total $^{10}C_3 = 120$; all-men $^6C_3 = 20$; so $120 - 20 = 100$.
@short Complement.
@trap Computing $^4C_1\times{}^9C_2$, which overcounts.
@@END

@@Q M04-04 | M | 1.5 | Integer solutions | JEE
The number of non-negative integer solutions of $x_1 + x_2 + x_3 = 10$ is:
(A) 36
(B) 66
(C) 45
(D) 120
@ans B
@sol $^{10+3-1}C_{3-1} = {}^{12}C_2 = 66$.
@short Stars and bars: $^{n+r-1}C_{r-1}$.
@trap Using the positive-solution formula: $^9C_2 = 36$.
@@END

@@Q M04-05 | E | 0.75 | Circular arrangement | Speed
The number of ways 6 people can sit around a round table is:
(A) 720
(B) 120
(C) 60
(D) 360
@ans B
@sol $(6 - 1)! = 120$.
@short —
@trap —
@@END

@@Q M04-06 | E | 1 | Diagonals of a polygon | NV
Find the number of diagonals of a decagon (10-sided polygon).
@ans 35
@sol $^{10}C_2 - 10 = 45 - 10 = 35$.
@short $\dfrac{n(n-3)}{2}$.
@trap —
@@END

@@Q M04-07 | M | 1.5 | Even numbers from digits | JEE
Using the digits 0, 1, 2, 3, 4 without repetition, how many 3-digit even numbers can be formed?
(A) 30
(B) 24
(C) 36
(D) 48
@ans A
@sol Last digit 0: $4\times3 = 12$. Last digit 2 or 4 (2 ways): first digit can't be 0 or the last digit (3 choices), middle 3 choices: $2\times3\times3 = 18$. Total 30.
@short Split on whether the units digit is 0.
@trap Allowing a leading 0 gives 36.
@@END

@@Q M04-08 | E | 0.75 | Symmetry of nCr | Speed
If $^nC_8 = {}^nC_6$, then $^nC_2$ equals:
(A) 91
(B) 14
(C) 182
(D) 28
@ans A
@sol $8 + 6 = n = 14$, so $^{14}C_2 = 91$.
@short —
@trap —
@@END

@@Q M04-09 | M | 1 | Number of divisors | NV
Find the number of positive divisors of 360.
@ans 24
@sol $360 = 2^3\cdot3^2\cdot5$: $(3 + 1)(2 + 1)(1 + 1) = 24$.
@short —
@trap —
@@END

@@Q M04-10 | M | 1.5 | Triangles from collinear points | Tricky
There are 10 points in a plane, of which exactly 4 are collinear (no other three collinear). The number of triangles they form is:
(A) 120
(B) 116
(C) 110
(D) 104
@ans B
@sol $^{10}C_3 - {}^4C_3 = 120 - 4 = 116$.
@short Subtract the degenerate "triangles".
@trap Forgetting to subtract.
@@END

@@SET M04 · Chapter Test

@@Q M04-T1 | E | 0.5 | Permutation value | Speed
$^7P_3$ equals:
(A) 35
(B) 210
(C) 343
(D) 5040
@ans B
@sol $7\times6\times5 = 210$.
@short —
@trap Giving $^7C_3 = 35$.
@@END

@@Q M04-T2 | E | 0.75 | Arrangements with repetition of letters | Basic
The number of distinct arrangements of the letters of ARRANGE is:
(A) 5040
(B) 1260
(C) 2520
(D) 630
@ans B
@sol 7 letters with A×2 and R×2: $\dfrac{7!}{2!\,2!} = 1260$.
@short —
@trap —
@@END

@@Q M04-T3 | E | 0.75 | Handshakes | NV
In a party of 12 people, each shakes hands with every other person exactly once. Find the number of handshakes.
@ans 66
@sol $^{12}C_2 = 66$.
@short —
@trap —
@@END

@@Q M04-T4 | M | 1 | Garland | Concept
The number of different garlands that can be made with 6 distinct flowers is:
(A) 120
(B) 60
(C) 720
(D) 360
@ans B
@sol $\dfrac{(6 - 1)!}{2} = 60$, because clockwise and anticlockwise arrangements look the same.
@short —
@trap —
@@END

@@Q M04-T5 | M | 1 | Selections with at least one | Concept
The number of ways to choose at least one fruit from 3 identical apples and 4 identical oranges is:
(A) 19
(B) 20
(C) 12
(D) 11
@ans A
@sol $(3 + 1)(4 + 1) - 1 = 19$.
@short —
@trap Using $2^7 - 1$ (that's for distinct objects).
@@END

## Answers & Solutions {#m04-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Permutations & Combinations
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
