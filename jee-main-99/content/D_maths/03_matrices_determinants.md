# Matrices & Determinants {#m03}

:::stats
Typical questions | 2–3 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 12 · Ch 3, 4
Study time | ~10 hours
:::

:::pyq Weight evidence
**33 questions across the 2026 Paper-1 shifts** (≈ 7% of Maths, tied for the highest in that dataset) {{tag:third}} [T-WT-CD]. This is the most reliable scoring unit in Maths.
:::

## Core concepts

- A **matrix** is a rectangular array. Matrix multiplication is associative and distributive, but **not commutative** ($AB \ne BA$ in general).
- **Determinant** of a square matrix: a scalar that is zero exactly when the matrix is singular (non-invertible).
- **Adjoint & inverse:** $A\,\operatorname{adj}A = \lvert A\rvert I$, so $A^{-1} = \operatorname{adj}A/\lvert A\rvert$ when $\lvert A\rvert \ne 0$.
- **Systems of linear equations** are solved as $AX = B$. Consistency depends on $\lvert A\rvert$ and $(\operatorname{adj}A)B$.

## Important formulas & standard results

:::formula Types of matrices
Symmetric: $A^T = A$. Skew-symmetric: $A^T = -A$ (diagonal entries 0). Orthogonal: $AA^T = I$ ($\lvert A\rvert = \pm1$). Idempotent: $A^2 = A$. Involutory: $A^2 = I$. Nilpotent: $A^k = O$.
Every square matrix $= \tfrac12(A + A^T) + \tfrac12(A - A^T)$ (symmetric + skew-symmetric).
$(AB)^T = B^TA^T$; $(AB)^{-1} = B^{-1}A^{-1}$; $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
:::

:::formula Determinant results ($A$ is $n\times n$)
$$\lvert AB\rvert = \lvert A\rvert\lvert B\rvert \qquad \lvert kA\rvert = k^n\lvert A\rvert \qquad \lvert A^T\rvert = \lvert A\rvert \qquad \lvert A^{-1}\rvert = \frac{1}{\lvert A\rvert}$$
- Swapping two rows changes the sign. Two identical or proportional rows give 0. $R_i \to R_i + kR_j$ doesn't change the value.
- A skew-symmetric matrix of **odd** order has determinant 0.
- Vandermonde: $\begin{vmatrix}1&1&1\\a&b&c\\a^2&b^2&c^2\end{vmatrix} = (a - b)(b - c)(c - a)$.
- Area of a triangle: $\Delta = \tfrac12\left\lvert\begin{vmatrix}x_1&y_1&1\\x_2&y_2&1\\x_3&y_3&1\end{vmatrix}\right\rvert$. Zero area means the points are collinear.
:::

:::formula Adjoint & inverse
$$A(\operatorname{adj}A) = (\operatorname{adj}A)A = \lvert A\rvert I \qquad \lvert\operatorname{adj}A\rvert = \lvert A\rvert^{n-1} \qquad \operatorname{adj}(\operatorname{adj}A) = \lvert A\rvert^{n-2}A$$
$$\lvert\operatorname{adj}(\operatorname{adj}A)\rvert = \lvert A\rvert^{(n-1)^2} \qquad \operatorname{adj}(AB) = \operatorname{adj}B\cdot\operatorname{adj}A \qquad \operatorname{adj}(kA) = k^{n-1}\operatorname{adj}A$$
For $2\times2$: $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \dfrac{1}{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ (swap the diagonal, negate the off-diagonal).
**$2\times2$ characteristic relation (Cayley–Hamilton):** $A^2 - (\operatorname{tr}A)A + \lvert A\rvert I = O$.
:::

:::formula Systems of equations $AX = B$
| Condition | Result |
|---|---|
| $\lvert A\rvert \ne 0$ | unique solution $X = A^{-1}B$ |
| $\lvert A\rvert = 0$, $(\operatorname{adj}A)B \ne O$ | no solution (inconsistent) |
| $\lvert A\rvert = 0$, $(\operatorname{adj}A)B = O$ | infinitely many solutions or none (check the equations directly) |
| Homogeneous ($B = O$), $\lvert A\rvert \ne 0$ | only the trivial solution |
| Homogeneous, $\lvert A\rvert = 0$ | infinitely many (non-trivial) solutions |

**Cramer:** $x = \Delta_x/\Delta$, etc. If $\Delta = 0$ and some $\Delta_i \ne 0$, there is no solution.
:::

:::note Syllabus note
The official text lists matrix algebra and types, evaluation of 2×2 and 3×3 determinants, area of triangles, adjoint and inverse using determinants, and consistency/solution of linear systems [NTA-SYL]. Determinant properties aren't named separately, but you still need them to evaluate determinants quickly.
:::

## Common question models

:::pyq Recurring structures
1. **$\lvert\operatorname{adj}A\rvert$, $\lvert kA\rvert$, $\lvert A^{-1}\rvert$** chains with given $\lvert A\rvert$ (very frequent, fast).
2. **Consistency of a 3×3 system** with parameters λ, μ: unique / none / infinitely many.
3. **Matrix powers** via patterns, idempotent/nilpotent properties or Cayley–Hamilton.
4. **Evaluating determinants** with factorisable structure (Vandermonde, cyclic).
5. **Symmetric/skew-symmetric** decomposition and properties; trace questions.
6. **Non-trivial solutions** of homogeneous systems.
:::

## Shortcuts & fast methods

:::shortcut Power chains in one line
For $n\times n$: $\lvert\operatorname{adj}(kA)\rvert = (k^{n-1})^n\lvert A\rvert^{n-1}$. Always reduce to powers of $\lvert A\rvert$ and $k$ **before** computing any number.
**Common mistake:** using $n$ instead of $n - 1$.
:::

:::shortcut Parameter systems (λ, μ)
Find λ from $\Delta = 0$ first. Then substitute that λ and check the other determinant (or eliminate) to find μ for consistency. That's two small steps instead of solving the full system.
:::

## Common mistakes

:::trap Mistake alerts
- $\lvert kA\rvert = k^n\lvert A\rvert$, not $k\lvert A\rvert$.
- $(AB)^{-1} = B^{-1}A^{-1}$. The order reverses.
- $\Delta = 0$ with all $\Delta_i = 0$ doesn't **guarantee** infinitely many solutions for 3 variables. Verify.
- $A^2 = O$ doesn't imply $A = O$. $AB = O$ doesn't imply $A = O$ or $B = O$.
:::

## Practice questions

@@SET M03 · Practice

@@Q M03-01 | E | 0.75 | adj of adj | Speed
If $A$ is $3\times3$ with $\lvert A\rvert = 5$, then $\lvert\operatorname{adj}(\operatorname{adj}A)\rvert$ is:
(A) 25
(B) 125
(C) 625
(D) 3125
@ans C
@sol $\lvert A\rvert^{(n-1)^2} = 5^4 = 625$.
@short —
@trap Using $(n-1)$ instead of $(n-1)^2$ gives 25.
@@END

@@Q M03-02 | E | 0.5 | Determinant of kA | NV
If $A$ is $3\times3$ with $\lvert A\rvert = 3$, find $\lvert 2A\rvert$.
@ans 24
@sol $2^3\times3 = 24$.
@short —
@trap $2\times3 = 6$.
@@END

@@Q M03-03 | M | 2 | Infinitely many solutions | JEE
The system $x + y + z = 6$, $x + 2y + 3z = 14$, $x + 2y + \lambda z = \mu$ has infinitely many solutions when:
(A) $\lambda = 3, \mu = 14$
(B) $\lambda = 3, \mu \ne 14$
(C) $\lambda \ne 3$
(D) $\lambda = 2, \mu = 10$
@ans A
@sol Subtracting the second equation from the third: $(\lambda - 3)z = \mu - 14$. $\lambda \ne 3$ gives a unique solution. $\lambda = 3$, $\mu = 14$ gives infinitely many. $\lambda = 3$, $\mu \ne 14$ gives none.
@short Subtract equations with matching coefficients.
@trap —
@@END

@@Q M03-04 | E | 0.5 | Odd-order skew-symmetric | Concept
The determinant of any $3\times3$ skew-symmetric matrix is:
(A) 1
(B) 0
(C) −1
(D) the product of its diagonal entries squared
@ans B
@sol $\lvert A\rvert = \lvert A^T\rvert = \lvert -A\rvert = (-1)^3\lvert A\rvert$, so $\lvert A\rvert = 0$.
@short —
@trap —
@@END

@@Q M03-05 | E | 0.75 | 2×2 inverse | Basic
If $A = \begin{pmatrix}1&2\\3&4\end{pmatrix}$, then $A^{-1}$ is:
(A) $-\dfrac12\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$
(B) $\dfrac12\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$
(C) $-\dfrac12\begin{pmatrix}1&-2\\-3&4\end{pmatrix}$
(D) $\begin{pmatrix}4&-2\\-3&1\end{pmatrix}$
@ans A
@sol $\lvert A\rvert = 4 - 6 = -2$. Swap the diagonal and negate the off-diagonal, then divide by −2.
@short —
@trap Sign of the determinant.
@@END

@@Q M03-06 | E | 1 | Area by determinant | NV
Find the area of the triangle with vertices $(1, 1)$, $(4, 1)$ and $(1, 5)$.
@ans 6
@sol A right triangle with legs 3 and 4: area $= 6$. (The determinant gives $\tfrac12\lvert12\rvert$.)
@short —
@trap —
@@END

@@Q M03-07 | M | 1.5 | Idempotent matrix power | Concept
If $A^2 = A$, then $(I + A)^3$ equals:
(A) $I + 3A$
(B) $I + 7A$
(C) $I + 8A$
(D) $I + A$
@ans B
@sol $(I + A)^2 = I + 2A + A^2 = I + 3A$. $(I + A)^3 = (I + 3A)(I + A) = I + 4A + 3A^2 = I + 7A$.
@short With $A^n = A$: $(I + A)^n = I + (2^n - 1)A$.
@trap —
@@END

@@Q M03-08 | M | 1.5 | Non-trivial solutions | JEE
The system $kx + y + z = 0$, $x + ky + z = 0$, $x + y + kz = 0$ has non-trivial solutions for:
(A) $k = 1$ only
(B) $k = -2$ only
(C) $k = 1$ or $k = -2$
(D) no real $k$
@ans C
@sol $\Delta = k^3 - 3k + 2 = (k - 1)^2(k + 2) = 0$.
@short For the pattern "$k$ on the diagonal, 1 elsewhere": $\Delta = (k - 1)^2(k + 2)$.
@trap —
@@END

@@Q M03-09 | M | 1 | Vandermonde determinant | Basic
$\begin{vmatrix}1&1&1\\a&b&c\\a^2&b^2&c^2\end{vmatrix}$ equals:
(A) $(a - b)(b - c)(c - a)$
(B) $(a + b)(b + c)(c + a)$
(C) $abc$
(D) $a^2 + b^2 + c^2$
@ans A
@sol Standard result: it vanishes when any two variables are equal, which fixes the factors. Compare the coefficient of $bc^2$ to fix the sign.
@short Check with $a = 0$, $b = 1$, $c = 2$: the determinant is $1\cdot4 - 1\cdot2 = 2$; (A) gives $(-1)(-1)(2) = 2$ ✓.
@trap —
@@END

@@Q M03-10 | M | 1 | Cayley–Hamilton for 2×2 | Concept
A $2\times2$ matrix has trace 5 and determinant 6. Then $A^2$ equals:
(A) $5A - 6I$
(B) $5A + 6I$
(C) $6A - 5I$
(D) $-5A + 6I$
@ans A
@sol $A^2 - (\operatorname{tr}A)A + \lvert A\rvert I = O$.
@short —
@trap —
@@END

@@SET M03 · Chapter Test

@@Q M03-T1 | E | 0.5 | Transpose of a product | Speed
$(AB)^T$ equals:
(A) $A^TB^T$
(B) $B^TA^T$
(C) $AB$
(D) $BA$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M03-T2 | E | 0.5 | Symmetric part | Speed
The symmetric part of a square matrix $A$ is:
(A) $\tfrac12(A - A^T)$
(B) $\tfrac12(A + A^T)$
(C) $AA^T$
(D) $A^T$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M03-T3 | E | 0.5 | 2×2 determinant | NV
Find $\begin{vmatrix}2&1\\3&5\end{vmatrix}$.
@ans 7
@sol $10 - 3 = 7$.
@short —
@trap —
@@END

@@Q M03-T4 | E | 0.5 | Orthogonal matrix | Speed
If $A$ is orthogonal, then $\lvert A\rvert$ is:
(A) 0
(B) ±1
(C) 2
(D) any real number
@ans B
@sol $\lvert AA^T\rvert = \lvert A\rvert^2 = 1$.
@short —
@trap —
@@END

@@Q M03-T5 | E | 0.5 | Cramer's rule | Concept
For a 3×3 system, $\Delta = 0$ and $\Delta_x \ne 0$. The system has:
(A) a unique solution
(B) infinitely many solutions
(C) no solution
(D) exactly two solutions
@ans C
@sol $x = \Delta_x/\Delta$ would need division by zero, so the system is inconsistent.
@short —
@trap —
@@END

## Answers & Solutions {#m03-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Matrices & Determinants
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
