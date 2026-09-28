# Vector Algebra {#m12}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy
Priority | Must-do
NCERT | Class 12 · Ch 10
Study time | ~5 hours
:::

:::pyq Weight evidence
**27 questions across the 2026 Paper-1 shifts** {{tag:third}} [T-WT-CD]. Most were direct applications of the dot and cross products.
:::

## Core concepts

- A **vector** has magnitude and direction; a **scalar** has only magnitude. In components, $\vec a = a_1\hat i + a_2\hat j + a_3\hat k$ and $\lvert\vec a\rvert = \sqrt{a_1^2 + a_2^2 + a_3^2}$.
- **Addition:** triangle and parallelogram laws. The position vector of the point dividing $AB$ in $m : n$ is $\dfrac{m\vec b + n\vec a}{m + n}$.
- **Dot product** (a scalar) measures alignment. **Cross product** (a vector perpendicular to both) measures area.

:::note Syllabus note
The official Unit 12 text lists vectors and scalars, addition, components in 2D and 3D, and **scalar and vector products** [NTA-SYL]. Triple products are not named. The "tools" box below covers them because they compress coplanarity and shortest-distance work {{tag:rec}}.
:::

## Important formulas & standard results

:::formula Dot product
$$\vec a\cdot\vec b = \lvert\vec a\rvert\lvert\vec b\rvert\cos\theta = a_1b_1 + a_2b_2 + a_3b_3$$
- $\vec a\perp\vec b \iff \vec a\cdot\vec b = 0$ (for non-zero vectors); $\hat i\cdot\hat i = 1$, $\hat i\cdot\hat j = 0$.
- **Projection** of $\vec a$ on $\vec b$: $\dfrac{\vec a\cdot\vec b}{\lvert\vec b\rvert}$. Vector projection: $\left(\dfrac{\vec a\cdot\vec b}{\lvert\vec b\rvert^2}\right)\vec b$.
- $\lvert\vec a\pm\vec b\rvert^2 = \lvert\vec a\rvert^2 + \lvert\vec b\rvert^2 \pm 2\,\vec a\cdot\vec b$.
- $\lvert\vec a + \vec b\rvert = \lvert\vec a - \vec b\rvert \iff \vec a\perp\vec b$.
:::

:::formula Cross product
$$\vec a\times\vec b = \begin{vmatrix}\hat i & \hat j & \hat k\\ a_1 & a_2 & a_3\\ b_1 & b_2 & b_3\end{vmatrix} \qquad \lvert\vec a\times\vec b\rvert = \lvert\vec a\rvert\lvert\vec b\rvert\sin\theta$$
- $\hat i\times\hat j = \hat k$, $\hat j\times\hat k = \hat i$, $\hat k\times\hat i = \hat j$ (cyclic); reversing the order flips the sign.
- $\vec a\times\vec b = \vec 0 \iff \vec a\parallel\vec b$ (non-zero vectors).
- Parallelogram with adjacent sides $\vec a$, $\vec b$: area $= \lvert\vec a\times\vec b\rvert$. Triangle: $\tfrac12\lvert\vec a\times\vec b\rvert$. Parallelogram with diagonals $\vec d_1$, $\vec d_2$: area $= \tfrac12\lvert\vec d_1\times\vec d_2\rvert$.
- Unit vector perpendicular to both: $\pm\dfrac{\vec a\times\vec b}{\lvert\vec a\times\vec b\rvert}$.
- **Lagrange's identity:** $\lvert\vec a\times\vec b\rvert^2 + (\vec a\cdot\vec b)^2 = \lvert\vec a\rvert^2\lvert\vec b\rvert^2$.
:::

:::formula Tools (not named in the syllabus text)
**Scalar triple product:** $[\vec a\ \vec b\ \vec c] = \vec a\cdot(\vec b\times\vec c) = \begin{vmatrix}a_1&a_2&a_3\\b_1&b_2&b_3\\c_1&c_2&c_3\end{vmatrix}$. This is the volume of the parallelepiped; it is zero iff the vectors are coplanar.
**Vector triple product:** $\vec a\times(\vec b\times\vec c) = (\vec a\cdot\vec c)\,\vec b - (\vec a\cdot\vec b)\,\vec c$.
:::

## Common question models

:::pyq Recurring structures
1. **Magnitudes from conditions:** given $\lvert\vec a\rvert$, $\lvert\vec b\rvert$ and $\lvert\vec a + \vec b\rvert$, find $\vec a\cdot\vec b$ or the angle.
2. **$\vec a + \vec b + \vec c = \vec 0$** problems: square both sides.
3. **Projection** and component questions.
4. **Area** of a triangle or parallelogram from vertices or diagonals.
5. **Unknown parameter** from perpendicularity, parallelism or coplanarity.
6. **Vector equations** such as $\vec r\times\vec a = \vec b\times\vec a$ and $\vec r\cdot\vec c = k$: find $\vec r$.
:::

## Shortcuts & fast methods

:::shortcut Square it
Almost every magnitude question is solved by squaring: $\lvert\vec a + \vec b + \vec c\rvert^2 = \sum\lvert\vec a\rvert^2 + 2\sum\vec a\cdot\vec b$.
**Time saved:** avoids components entirely.
:::

:::shortcut $\vec r\times\vec a = \vec b\times\vec a$
This gives $(\vec r - \vec b)\times\vec a = \vec 0$, so $\vec r = \vec b + t\vec a$. Use the second condition to find $t$.
:::

:::shortcut Spot linear combinations
Before expanding a $3\times3$ determinant for coplanarity, check whether one vector is a sum or multiple of the others. If $\vec c = \vec a + \vec b$, the vectors are coplanar at once.
:::

## Common mistakes

:::trap Mistake alerts
- The projection formula divides by $\lvert\vec b\rvert$ (the vector you project **onto**), not by $\lvert\vec a\rvert$.
- The cross product isn't commutative: $\vec b\times\vec a = -\vec a\times\vec b$.
- The angle between vectors lies in $[0, \pi]$. A negative dot product means an obtuse angle, not an error.
- Triangle area is **half** of $\lvert\vec{AB}\times\vec{AC}\rvert$.
:::

## Practice questions

@@SET M12 · Practice

@@Q M12-01 | E | 0.5 | Angle from dot product | Basic
If $\lvert\vec a\rvert = 3$, $\lvert\vec b\rvert = 4$ and $\vec a\cdot\vec b = 6$, the angle between $\vec a$ and $\vec b$ is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $90^\circ$
@ans C
@sol $\cos\theta = \dfrac{6}{12} = \dfrac12$.
@short —
@trap —
@@END

@@Q M12-02 | E | 0.5 | Unit vector | Speed
The unit vector along $2\hat i - \hat j + 2\hat k$ is:
(A) $\tfrac13(2\hat i - \hat j + 2\hat k)$
(B) $\tfrac19(2\hat i - \hat j + 2\hat k)$
(C) $2\hat i - \hat j + 2\hat k$
(D) $\tfrac15(2\hat i - \hat j + 2\hat k)$
@ans A
@sol The magnitude is $\sqrt{4 + 1 + 4} = 3$.
@short —
@trap —
@@END

@@Q M12-03 | E | 0.5 | Perpendicularity | NV
If $\hat i + \lambda\hat j + 2\hat k$ is perpendicular to $2\hat i - \hat j + \hat k$, find $\lambda$.
@ans 4
@sol $2 - \lambda + 2 = 0$.
@short —
@trap —
@@END

@@Q M12-04 | E | 0.75 | Projection | Basic
The projection of $\vec a = 2\hat i + 3\hat j + 2\hat k$ on $\vec b = \hat i + 2\hat j + \hat k$ is:
(A) $\dfrac{10}{\sqrt6}$
(B) $\dfrac{10}{\sqrt{17}}$
(C) $\sqrt6$
(D) $\dfrac{5}{\sqrt6}$
@ans A
@sol $\vec a\cdot\vec b = 2 + 6 + 2 = 10$ and $\lvert\vec b\rvert = \sqrt6$.
@short —
@trap Dividing by $\lvert\vec a\rvert = \sqrt{17}$ gives (B).
@@END

@@Q M12-05 | E | 1 | Parallelogram area | Basic
The area of the parallelogram with adjacent sides $\hat i + \hat j - \hat k$ and $\hat i - \hat j + \hat k$ is:
(A) $2\sqrt2$
(B) $\sqrt2$
(C) 4
(D) $2\sqrt3$
@ans A
@sol The cross product is $(0, -2, -2)$, with magnitude $2\sqrt2$.
@short —
@trap —
@@END

@@Q M12-06 | M | 1 | Triangle area from vertices | JEE
The area of the triangle with vertices $A(1, 1, 1)$, $B(1, 2, 3)$ and $C(2, 3, 1)$ is:
(A) $\dfrac{\sqrt{21}}{2}$
(B) $\sqrt{21}$
(C) $\dfrac{\sqrt{14}}{2}$
(D) $\dfrac{21}{2}$
@ans A
@sol $\vec{AB} = (0, 1, 2)$ and $\vec{AC} = (1, 2, 0)$. $\vec{AB}\times\vec{AC} = (-4, 2, -1)$, with magnitude $\sqrt{21}$. Area $= \tfrac12\sqrt{21}$.
@short —
@trap Forgetting the $\tfrac12$.
@@END

@@Q M12-07 | E | 0.75 | Lagrange's identity | NV
If $\lvert\vec a\rvert = 2$, $\lvert\vec b\rvert = 5$ and $\lvert\vec a\times\vec b\rvert = 8$, find $\lvert\vec a\cdot\vec b\rvert$.
@ans 6
@sol $(\vec a\cdot\vec b)^2 = 100 - 64 = 36$.
@short —
@trap —
@@END

@@Q M12-08 | E | 0.5 | Equal sum and difference | Concept
If $\lvert\vec a + \vec b\rvert = \lvert\vec a - \vec b\rvert$ for non-zero vectors, then:
(A) $\vec a\parallel\vec b$
(B) $\vec a\perp\vec b$
(C) $\lvert\vec a\rvert = \lvert\vec b\rvert$
(D) $\vec a = \vec b$
@ans B
@sol Squaring gives $4\,\vec a\cdot\vec b = 0$.
@short —
@trap Choosing (C): that is the condition for the diagonals of the parallelogram to be perpendicular.
@@END

@@Q M12-09 | M | 1 | Sum of three vectors is zero | NV
$\vec a + \vec b + \vec c = \vec 0$, with $\lvert\vec a\rvert = 3$, $\lvert\vec b\rvert = 5$ and $\lvert\vec c\rvert = 7$. Find the angle between $\vec a$ and $\vec b$ in degrees.
@ans 60
@sol $\vec c = -(\vec a + \vec b)$, so $49 = 9 + 25 + 2\,\vec a\cdot\vec b \Rightarrow \vec a\cdot\vec b = \tfrac{15}{2}$. $\cos\theta = \dfrac{15/2}{15} = \dfrac12$.
@short —
@trap Answering $120^\circ$ (the angle between the sides of the triangle, not between the vectors placed tail to tail).
@@END

@@Q M12-10 | M | 1 | Unit vectors summing to zero | Tricky
If $\vec a + \vec b + \vec c = \vec 0$ and all three are unit vectors, then $\vec a\cdot\vec b + \vec b\cdot\vec c + \vec c\cdot\vec a$ equals:
(A) $-\tfrac32$
(B) $\tfrac32$
(C) 0
(D) $-3$
@ans A
@sol $0 = \lvert\vec a + \vec b + \vec c\rvert^2 = 3 + 2S \Rightarrow S = -\tfrac32$.
@short —
@trap —
@@END

@@Q M12-11 | M | 1 | Perpendicular unit vector | Basic
A unit vector perpendicular to both $\hat i + \hat j + \hat k$ and $\hat i + 2\hat j + 3\hat k$ is:
(A) $\dfrac{\hat i - 2\hat j + \hat k}{\sqrt6}$
(B) $\dfrac{\hat i + 2\hat j + \hat k}{\sqrt6}$
(C) $\dfrac{\hat i - \hat j}{\sqrt2}$
(D) $\dfrac{2\hat i - \hat j}{\sqrt5}$
@ans A
@sol The cross product is $(3 - 2, -(3 - 1), 2 - 1) = (1, -2, 1)$.
@short Check the options by dot product with both vectors: (A) gives $1 - 2 + 1 = 0$ and $1 - 4 + 3 = 0$.
@trap —
@@END

@@Q M12-12 | M | 1 | Coplanarity (tool) | NV
The vectors $\hat i + \hat j + \hat k$, $\hat i + 2\hat j + 3\hat k$ and $2\hat i + \lambda\hat j + 4\hat k$ are coplanar. Find $\lambda$.
@ans 3
@sol The determinant is $6 - 2\lambda = 0$.
@short With $\lambda = 3$ the third vector is the sum of the first two.
@trap —
@@END

@@SET M12 · Chapter Test

@@Q M12-T1 | E | 0.5 | Unit-vector triple product | Speed
$\hat i\cdot(\hat j\times\hat k)$ equals:
(A) 0
(B) 1
(C) $-1$
(D) $\hat k$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M12-T2 | E | 0.5 | Order of the cross product | Speed
$\hat j\times\hat i$ equals:
(A) $\hat k$
(B) $-\hat k$
(C) $\vec 0$
(D) 1
@ans B
@sol —
@short —
@trap —
@@END

@@Q M12-T3 | E | 0.5 | Magnitude | NV
Find $\lvert3\hat i - 4\hat j + 12\hat k\rvert$.
@ans 13
@sol $\sqrt{9 + 16 + 144} = 13$.
@short —
@trap —
@@END

@@Q M12-T4 | E | 0.5 | Maximum of a dot product | Concept
$\vec a\cdot\vec b = \lvert\vec a\rvert\lvert\vec b\rvert$ (both non-zero) when the angle between them is:
(A) $0$
(B) $\pi/2$
(C) $\pi$
(D) $\pi/4$
@ans A
@sol —
@short —
@trap —
@@END

@@Q M12-T5 | E | 0.5 | Magnitude of a sum | NV
If $\lvert\vec a\rvert = 1$, $\lvert\vec b\rvert = 2$ and $\vec a\cdot\vec b = 1$, find $\lvert\vec a + \vec b\rvert^2$.
@ans 7
@sol $1 + 4 + 2 = 7$.
@short —
@trap —
@@END

## Answers & Solutions {#m12-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Vector Algebra
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
