# Binomial Theorem {#m05}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 11 · Ch 7
Study time | ~6 hours
:::

## Core concepts

- For a positive integer $n$: $(x + y)^n = \sum_{r=0}^{n}\binom nr x^{n-r}y^r$, which has $n + 1$ terms.
- Almost every question uses **the general term** $T_{r+1}$: find a specific coefficient, the term independent of $x$, or the middle term.
- **Applications:** remainders and divisibility (write the base as a multiple ± 1), approximations, sums of coefficients.

:::note Syllabus note
The official text reads: "Binomial theorem for a positive integral index, general term and middle term, and simple applications" [NTA-SYL]. Detailed identities of binomial coefficients are not listed. The basic sums below are included because they are one-line applications.
:::

## Important formulas & standard results

:::formula General & middle term
$$T_{r+1} = \binom nr x^{n-r}y^r \qquad \text{middle term: } T_{\frac n2 + 1}\ (n\ \text{even});\ \ T_{\frac{n+1}{2}}\ \&\ T_{\frac{n+3}{2}}\ (n\ \text{odd})$$
**Term independent of $x$** in $\left(ax^p + \dfrac{b}{x^q}\right)^n$: set the power of $x$ in $T_{r+1}$ to 0: $p(n - r) - qr = 0 \Rightarrow r = \dfrac{np}{p + q}$ (must be an integer).
**Greatest binomial coefficient:** $\binom{n}{n/2}$ ($n$ even); $\binom{n}{(n-1)/2} = \binom{n}{(n+1)/2}$ ($n$ odd).
:::

:::formula Sums & applications
$$\sum_{r=0}^n\binom nr = 2^n \qquad \binom n0 + \binom n2 + \dots = \binom n1 + \binom n3 + \dots = 2^{n-1}$$
- **Sum of coefficients** of a polynomial $p(x)$: $p(1)$. Sum of coefficients of the even powers: $\dfrac{p(1) + p(-1)}{2}$.
- **Remainders:** write $a^n = (km \pm 1)^N\cdot(\text{leftover})$ and expand. All terms except the last are multiples of $m$.
- **Approximation:** $(1 + x)^n \approx 1 + nx + \dfrac{n(n-1)}{2}x^2$ for small $x$.
- **Divisibility:** $(1 + a)^n - 1 - na$ is divisible by $a^2$ (e.g. $8^n - 7n - 1$ by 49).
:::

## Common question models

:::pyq Recurring structures
1. **Coefficient of $x^k$** in a binomial, or in a product such as $(1 + x)^m(1 - x)^n$ or $(1 + x + x^2)(1 - x)^n$.
2. **Term independent of $x$** (and its value).
3. **Middle term(s)** and the greatest coefficient.
4. **Equal coefficients** of two terms → find $n$ or $r$ using $\binom nx = \binom ny \Rightarrow x = y$ or $x + y = n$.
5. **Remainder / last digits** of large powers.
6. **Sums** of coefficients (substituting $x = 1$, $-1$).
:::

## Shortcuts & fast methods

:::shortcut Power-of-x equation
Write only the exponent of $x$ in $T_{r+1}$ as a linear function of $r$. Solve for $r$, then compute the coefficient. **Never expand.** Time: under 1 minute.
**Common mistake:** a sign error when the second term has a negative sign. Carry $(-1)^r$.
:::

:::shortcut Remainders mod m
Find a small power of the base close to a multiple of $m$: $7^2 = 49 = 50 - 1$ (for mod 25 or 50), $2^5 = 32 = 31 + 1$ (mod 31), $3^4 = 81 = 80 + 1$ (mod 80 or 16). Then use $(km \pm 1)^N \equiv (\pm1)^N$.
:::

## Common mistakes

:::trap Mistake alerts
- The $r$-th term is $T_r$, not $T_{r+1}$: indexing is off by one.
- Losing the constant factors $a^{n-r}b^r$ when the terms have coefficients (e.g. $(2x - 3)^n$).
- A negative remainder: convert $-7 \pmod{25}$ to 18.
- "Coefficient" vs "binomial coefficient": the coefficient includes the powers of the constants.
:::

## Practice questions

@@SET M05 · Practice

@@Q M05-01 | E | 1 | Specific coefficient | Basic
The coefficient of $x^4$ in $(2 - x)^7$ is:
(A) 280
(B) −280
(C) 560
(D) 35
@ans A
@sol $T_{r+1} = \binom7r2^{7-r}(-x)^r$. With $r = 4$: $35\times8\times(+1) = 280$.
@short $(-1)^4 = +1$.
@trap Dropping $2^{7-r}$ gives 35.
@@END

@@Q M05-02 | M | 1 | Term independent of x | NV
Find the term independent of $x$ in $\left(x^2 + \dfrac1x\right)^9$.
@ans 84
@sol Exponent of $x$: $2(9 - r) - r = 18 - 3r = 0 \Rightarrow r = 6$. Term $= \binom96 = 84$.
@short —
@trap —
@@END

@@Q M05-03 | M | 1 | Middle term | Basic
The middle term of $\left(x - \dfrac1x\right)^{10}$ is:
(A) 252
(B) −252
(C) 210
(D) −210
@ans B
@sol $n = 10$, so the middle term is $T_6 = \binom{10}{5}x^5\left(-\dfrac1x\right)^5 = -252$.
@short —
@trap Sign.
@@END

@@Q M05-04 | E | 0.5 | Sum of coefficients | Speed
The sum of the coefficients in the expansion of $(3x - 2)^5$ is:
(A) 1
(B) 32
(C) −1
(D) 243
@ans A
@sol Put $x = 1$: $(3 - 2)^5 = 1$.
@short —
@trap —
@@END

@@Q M05-05 | M | 1.5 | Remainder of a large power | NV
Find the remainder when $7^{103}$ is divided by 25.
@ans 18
@sol $7^{103} = 7\cdot(7^2)^{51} = 7(50 - 1)^{51} \equiv 7(-1)^{51} = -7 \equiv 18 \pmod{25}$.
@short —
@trap Leaving the answer as −7.
@@END

@@Q M05-06 | M | 1 | Equal coefficients | NV
In $(1 + x)^{18}$, the coefficients of the $(2r + 4)$-th and $(r - 2)$-th terms are equal. Find $r$.
@ans 6
@sol $\binom{18}{2r+3} = \binom{18}{r-3}$. Since $2r + 3 \ne r - 3$, we need $(2r + 3) + (r - 3) = 18 \Rightarrow r = 6$.
@short —
@trap Using the term numbers themselves ($2r + 4$, $r - 2$) instead of $r$-values one less.
@@END

@@Q M05-07 | E | 0.5 | Greatest coefficient | Speed
The greatest binomial coefficient in $(1 + x)^9$ is:
(A) 84
(B) 126
(C) 252
(D) 36
@ans B
@sol $\binom94 = \binom95 = 126$.
@short —
@trap —
@@END

@@Q M05-08 | M | 1 | Binomial approximation | Calc
$(1.01)^{10}$, correct to 3 decimal places, is:
(A) 1.100
(B) 1.105
(C) 1.110
(D) 1.010
@ans B
@sol $1 + 10(0.01) + 45(0.0001) + 120(10^{-6}) + \dots = 1 + 0.1 + 0.0045 + 0.00012 \approx 1.1046 \to 1.105$.
@short —
@trap Stopping after the linear term (1.100).
@@END

@@Q M05-09 | M | 1 | Coefficient in a product | Concept
The coefficient of $x$ in $(1 + x)(1 - x)^5$ is:
(A) −4
(B) −5
(C) −6
(D) 4
@ans A
@sol $(1 - x)^5 = 1 - 5x + \dots$. Coefficient of $x$: $1\cdot(-5) + 1\cdot1 = -4$.
@short Collect the ways of making $x^1$: $1\times(-5x)$ and $x\times1$.
@trap —
@@END

@@Q M05-10 | E | 0.75 | Sum of even-index coefficients | NV
Find $\binom80 + \binom82 + \binom84 + \binom86 + \binom88$.
@ans 128
@sol $2^{n-1} = 2^7 = 128$.
@short —
@trap —
@@END

@@SET M05 · Chapter Test

@@Q M05-T1 | E | 0.5 | General term | Speed
The general term of $(a + b)^n$ is:
(A) $\binom nr a^rb^{n-r}$ with index $T_r$
(B) $T_{r+1} = \binom nr a^{n-r}b^r$
(C) $T_{r+1} = \binom{n}{r+1}a^{n-r}b^r$
(D) $T_r = \binom nr a^{n-r}b^r$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M05-T2 | E | 0.5 | Number of terms | Speed
The number of terms in the expansion of $(a + b)^{15}$ is:
(A) 15
(B) 16
(C) 14
(D) 30
@ans B
@sol $n + 1$.
@short —
@trap —
@@END

@@Q M05-T3 | E | 0.75 | Coefficient of x² | NV
Find the coefficient of $x^2$ in $(1 + 2x)^6$.
@ans 60
@sol $\binom62\cdot2^2 = 15\times4 = 60$.
@short —
@trap —
@@END

@@Q M05-T4 | M | 1 | Divisibility via binomial | Concept
For every positive integer $n$, $8^n - 7n - 1$ is divisible by:
(A) 7
(B) 49
(C) 64
(D) 14
@ans B
@sol $8^n = (1 + 7)^n = 1 + 7n + \binom n2 7^2 + \dots$, so $8^n - 7n - 1$ is a multiple of 49.
@short Check $n = 2$: $64 - 15 = 49$ ✓.
@trap Choosing 7 (true, but not the strongest divisor offered).
@@END

@@Q M05-T5 | E | 0.5 | Middle terms for odd n | Speed
The expansion of $(x + y)^{11}$ has:
(A) one middle term
(B) two middle terms, $T_6$ and $T_7$
(C) no middle term
(D) three middle terms
@ans B
@sol $n$ odd: $T_{(n+1)/2} = T_6$ and $T_{(n+3)/2} = T_7$.
@short —
@trap —
@@END

## Answers & Solutions {#m05-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Binomial Theorem
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
