# Three-Dimensional Geometry {#m11}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 11 · Ch 11 · Class 12 · Ch 11
Study time | ~7 hours
:::

:::pyq Weight evidence
**29 questions across the 2026 Paper-1 shifts** {{tag:third}} [T-WT-CD]. For the time it takes to learn, this unit gives some of the highest returns in Maths.
:::

## Core concepts

- A point in space is $(x, y, z)$. Distance and section formulas extend directly from 2D.
- **Direction cosines** $(l, m, n)$ are the cosines of the angles a line makes with the axes, and $l^2 + m^2 + n^2 = 1$. **Direction ratios** $(a, b, c)$ are any numbers proportional to them.
- A line is fixed by **a point and a direction**. Lines in space are parallel, intersecting or **skew** (neither parallel nor intersecting).
- **Shortest distance** between two lines is measured along their common perpendicular.

:::note Syllabus note
The official Unit 11 text lists coordinates, distance, section formula, direction ratios and cosines, angle between intersecting lines, skew lines and the shortest distance between them, and equations of a line [NTA-SYL]. Planes are not listed. The insurance box at the end of this module covers the four plane results worth two hours {{tag:rec}} (see the warning in the Maths strategy, page [[maths-strategy]]).
:::

## Important formulas & standard results

:::formula Points
$$PQ = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$
Section $m : n$ (internal): $\left(\dfrac{mx_2 + nx_1}{m + n}, \dfrac{my_2 + ny_1}{m + n}, \dfrac{mz_2 + nz_1}{m + n}\right)$; external: replace $n$ by $-n$.
Centroid of a triangle: $\left(\dfrac{\sum x_i}{3}, \dfrac{\sum y_i}{3}, \dfrac{\sum z_i}{3}\right)$.
Distance of $(x, y, z)$ from the $x$-axis: $\sqrt{y^2 + z^2}$ (similarly for the other axes). Distance from the $xy$-plane: $\lvert z\rvert$.
**Ratio in which the $yz$-plane divides $PQ$:** $-x_1 : x_2$.
:::

:::formula Direction cosines & ratios
$$l = \cos\alpha,\ m = \cos\beta,\ n = \cos\gamma \qquad l^2 + m^2 + n^2 = 1 \qquad \sin^2\alpha + \sin^2\beta + \sin^2\gamma = 2$$
From DRs $(a, b, c)$: $l = \dfrac{a}{\sqrt{a^2 + b^2 + c^2}}$, etc. For the line through $P$ and $Q$, the DRs are $(x_2 - x_1, y_2 - y_1, z_2 - z_1)$.
**Angle between two lines:** $\cos\theta = \dfrac{\lvert a_1a_2 + b_1b_2 + c_1c_2\rvert}{\sqrt{a_1^2 + b_1^2 + c_1^2}\sqrt{a_2^2 + b_2^2 + c_2^2}}$.
Perpendicular: $a_1a_2 + b_1b_2 + c_1c_2 = 0$. Parallel: $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$.
:::

:::formula Equations of a line
| Form | Vector | Cartesian |
|---|---|---|
| point $\vec a$, direction $\vec b$ | $\vec r = \vec a + \lambda\vec b$ | $\dfrac{x - x_1}{a} = \dfrac{y - y_1}{b} = \dfrac{z - z_1}{c}$ |
| two points | $\vec r = \vec a + \lambda(\vec b - \vec a)$ | $\dfrac{x - x_1}{x_2 - x_1} = \dfrac{y - y_1}{y_2 - y_1} = \dfrac{z - z_1}{z_2 - z_1}$ |

**General point** on $\dfrac{x - x_1}{a} = \dfrac{y - y_1}{b} = \dfrac{z - z_1}{c}$: $(x_1 + a\lambda,\ y_1 + b\lambda,\ z_1 + c\lambda)$. Almost every line question starts here.
:::

:::formula Shortest distance
**Skew lines** $\vec r = \vec a_1 + \lambda\vec b_1$ and $\vec r = \vec a_2 + \mu\vec b_2$:
$$d = \frac{\lvert(\vec a_2 - \vec a_1)\cdot(\vec b_1\times\vec b_2)\rvert}{\lvert\vec b_1\times\vec b_2\rvert}$$
**Parallel lines** ($\vec b_1 = \vec b_2 = \vec b$): $d = \dfrac{\lvert(\vec a_2 - \vec a_1)\times\vec b\rvert}{\lvert\vec b\rvert}$.
**Intersecting (coplanar) lines:** $(\vec a_2 - \vec a_1)\cdot(\vec b_1\times\vec b_2) = 0$, i.e. $\begin{vmatrix}x_2 - x_1 & y_2 - y_1 & z_2 - z_1\\ a_1 & b_1 & c_1\\ a_2 & b_2 & c_2\end{vmatrix} = 0$ (for non-parallel lines).
:::

:::formula Foot of the perpendicular & image (point $P$, line $L$)
1. Take the general point $Q(\lambda)$ on $L$.
2. Set $\vec{PQ}\cdot\vec b = 0$ and solve for $\lambda$. $Q$ is the foot; $PQ$ is the perpendicular distance.
3. Image $P' = 2Q - P$.
:::

## Common question models

:::pyq Recurring structures
1. **Shortest distance between skew lines** (the single most repeated 3D model). Often an NV, with the answer as $d^2$ or $\sqrt{k}$.
2. **Foot of the perpendicular / image** of a point in a line, then a distance or a sum of coordinates.
3. **Intersecting lines:** find the unknown $k$ or the point of intersection.
4. **Angle between lines;** DCs from two conditions ($l + m + n = 0$ and a quadratic).
5. **Section formula** with a coordinate plane; collinearity.
6. **Line through a point meeting / perpendicular to two given lines** (cross product for the direction).
:::

## Shortcuts & fast methods

:::shortcut Distance to a line by the cross product
Distance of $P$ from the line through $A$ with direction $\vec b$: $\dfrac{\lvert\vec{AP}\times\vec b\rvert}{\lvert\vec b\rvert}$. No need to find the foot when only the distance is asked.
**Time saved:** ~1 minute.
:::

:::shortcut Intersection test on one coordinate
To check whether two lines meet, equate the general points on **two** coordinates, solve for $\lambda$ and $\mu$, and test the third. It is faster than the determinant when the numbers are small.
:::

:::shortcut Squared answers
When an NV asks for $d^2$ or $6d^2$, keep everything squared: $d^2 = \dfrac{[(\vec a_2 - \vec a_1)\cdot\vec n]^2}{\lvert\vec n\rvert^2}$. This avoids surds entirely.
:::

## Common mistakes

:::trap Mistake alerts
- Using DRs as DCs without normalising. $\left(\tfrac12, \tfrac12, \tfrac12\right)$ cannot be DCs, because $l^2 + m^2 + n^2 \ne 1$.
- Sign slips in the cross product. Expand the middle ($\hat j$) term with a minus sign.
- Forgetting the modulus in the shortest-distance formula.
- Reading the direction from the wrong form: in $\dfrac{2x - 1}{3} = \dots$, the $x$-DR is $\dfrac32$, not 3. First rewrite as $\dfrac{x - 1/2}{3/2}$.
:::

## Insurance topic: planes

:::important Plane insurance (2 hours, not in the official text) {{tag:rec}}
| Result | Formula |
|---|---|
| Plane with normal $(a, b, c)$ through $(x_1, y_1, z_1)$ | $a(x - x_1) + b(y - y_1) + c(z - z_1) = 0$ |
| Distance of a point from $ax + by + cz + d = 0$ | $\dfrac{\lvert ax_1 + by_1 + cz_1 + d\rvert}{\sqrt{a^2 + b^2 + c^2}}$ |
| Angle between a line (DRs $\vec b$) and a plane (normal $\vec n$) | $\sin\phi = \dfrac{\lvert\vec b\cdot\vec n\rvert}{\lvert\vec b\rvert\lvert\vec n\rvert}$ |
| Plane through three points | normal $= \vec{AB}\times\vec{AC}$ |
:::

## Practice questions

@@SET M11 · Practice

@@Q M11-01 | E | 0.5 | Distance formula | NV
Find the distance between $(1, 2, 3)$ and $(4, 6, 15)$.
@ans 13
@sol $\sqrt{9 + 16 + 144} = \sqrt{169} = 13$.
@short —
@trap —
@@END

@@Q M11-02 | E | 0.5 | DCs from DRs | Basic
The direction cosines of a line with direction ratios $2, -1, 2$ are:
(A) $\tfrac23, -\tfrac13, \tfrac23$
(B) $2, -1, 2$
(C) $\tfrac25, -\tfrac15, \tfrac25$
(D) $\tfrac13, -\tfrac16, \tfrac13$
@ans A
@sol $\sqrt{4 + 1 + 4} = 3$; divide each DR by 3.
@short —
@trap —
@@END

@@Q M11-03 | E | 0.5 | Sum of squares of sines | Speed
If a line makes angles $\alpha$, $\beta$, $\gamma$ with the coordinate axes, then $\sin^2\alpha + \sin^2\beta + \sin^2\gamma$ equals:
(A) 1
(B) 2
(C) 3
(D) 0
@ans B
@sol $\sum\sin^2 = 3 - \sum\cos^2 = 3 - 1 = 2$.
@short —
@trap —
@@END

@@Q M11-04 | E | 0.75 | Angle between lines | Basic
The angle between lines with direction ratios $(1, 1, 0)$ and $(0, 1, 1)$ is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $90^\circ$
@ans C
@sol $\cos\theta = \dfrac{0 + 1 + 0}{\sqrt2\cdot\sqrt2} = \dfrac12$.
@short —
@trap —
@@END

@@Q M11-05 | E | 0.75 | Section formula | Basic
The point dividing the join of $(1, 2, 3)$ and $(4, 5, 6)$ internally in the ratio $1 : 2$ is:
(A) $(2, 3, 4)$
(B) $(3, 4, 5)$
(C) $(2.5, 3.5, 4.5)$
(D) $(1.5, 2.5, 3.5)$
@ans A
@sol $\left(\dfrac{4 + 2}{3}, \dfrac{5 + 4}{3}, \dfrac{6 + 6}{3}\right) = (2, 3, 4)$.
@short The point is one-third of the way from the first point: $(1, 2, 3) + \tfrac13(3, 3, 3)$.
@trap Using $2 : 1$ by mistake gives $(3, 4, 5)$.
@@END

@@Q M11-06 | M | 1 | DCs from two conditions | Tricky
The angle between the two lines whose direction cosines satisfy $l + m + n = 0$ and $l^2 + m^2 - n^2 = 0$ is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $90^\circ$
@ans C
@sol $n = -(l + m)$, so $l^2 + m^2 - (l + m)^2 = -2lm = 0$. If $l = 0$, the DRs are $(0, 1, -1)$; if $m = 0$, they are $(1, 0, -1)$. $\cos\theta = \dfrac{1}{\sqrt2\cdot\sqrt2} = \dfrac12$.
@short —
@trap Stopping at $lm = 0$ without building both direction vectors.
@@END

@@Q M11-07 | M | 2 | Shortest distance (skew lines) | JEE
The shortest distance between $\vec r = (\hat i + 2\hat j + \hat k) + \lambda(\hat i - \hat j + \hat k)$ and $\vec r = (2\hat i - \hat j - \hat k) + \mu(2\hat i + \hat j + 2\hat k)$ is:
(A) $\dfrac{3}{\sqrt2}$
(B) $\dfrac{9}{\sqrt2}$
(C) $\sqrt2$
(D) $3\sqrt2$
@ans A
@sol $\vec a_2 - \vec a_1 = (1, -3, -2)$; $\vec b_1\times\vec b_2 = (-3, 0, 3)$ with magnitude $3\sqrt2$. Dot product: $-3 + 0 - 6 = -9$. $d = \dfrac{9}{3\sqrt2} = \dfrac{3}{\sqrt2}$.
@short —
@trap Dropping the minus on the $\hat j$ term of the cross product.
@@END

@@Q M11-08 | M | 1.5 | Shortest distance (parallel lines) | JEE
The distance between the parallel lines $\vec r = \hat i + \hat j + \lambda(2\hat i - \hat j + \hat k)$ and $\vec r = 2\hat i + \hat j - \hat k + \mu(4\hat i - 2\hat j + 2\hat k)$ is:
(A) $\sqrt{\dfrac{11}{6}}$
(B) $\sqrt{\dfrac{6}{11}}$
(C) $\sqrt{11}$
(D) $\dfrac{11}{6}$
@ans A
@sol Take $\vec b = (2, -1, 1)$, $\lvert\vec b\rvert = \sqrt6$. $\vec a_2 - \vec a_1 = (1, 0, -1)$; $(1, 0, -1)\times(2, -1, 1) = (-1, -3, -1)$ with magnitude $\sqrt{11}$. $d = \sqrt{11}/\sqrt6$.
@short —
@trap Using the skew-line formula: $\vec b_1\times\vec b_2 = \vec 0$ for parallel lines.
@@END

@@Q M11-09 | M | 2 | Intersecting lines | JEE
The lines $\dfrac{x - 1}{2} = \dfrac{y + 1}{3} = \dfrac{z - 1}{4}$ and $\dfrac{x - 3}{1} = \dfrac{y - k}{2} = \dfrac{z}{1}$ intersect. Then $k$ equals:
(A) $\tfrac92$
(B) $\tfrac32$
(C) $\tfrac29$
(D) 5
@ans A
@sol General points: $(1 + 2\lambda, -1 + 3\lambda, 1 + 4\lambda)$ and $(3 + \mu, k + 2\mu, \mu)$. From $z$: $\mu = 1 + 4\lambda$. From $x$: $1 + 2\lambda = 4 + 4\lambda \Rightarrow \lambda = -\tfrac32$, so $\mu = -5$. From $y$: $-1 - \tfrac92 = k - 10 \Rightarrow k = \tfrac92$.
@short Two coordinates fix $\lambda$ and $\mu$; the third gives $k$.
@trap —
@@END

@@Q M11-10 | M | 1.5 | Foot of perpendicular | JEE
The foot of the perpendicular from $(0, 2, 3)$ to the line $\dfrac{x + 3}{5} = \dfrac{y - 1}{2} = \dfrac{z + 4}{3}$ is:
(A) $(2, 3, -1)$
(B) $(-3, 1, -4)$
(C) $(7, 5, 2)$
(D) $(2, 3, 1)$
@ans A
@sol $Q = (5\lambda - 3, 2\lambda + 1, 3\lambda - 4)$; $\vec{PQ} = (5\lambda - 3, 2\lambda - 1, 3\lambda - 7)$. Dot with $(5, 2, 3)$: $38\lambda - 38 = 0 \Rightarrow \lambda = 1$, giving $Q = (2, 3, -1)$.
@short Check the options: (D) is not on the line. (A), (B) and (C) are on it ($\lambda = 1, 0, 2$), but only (A) makes $\vec{PQ}\perp\vec b$.
@trap —
@@END

@@Q M11-11 | M | 1.5 | Image in a line | JEE
The image of $(1, 6, 3)$ in the line $\dfrac x1 = \dfrac{y - 1}{2} = \dfrac{z - 2}{3}$ is:
(A) $(1, 0, 7)$
(B) $(1, 3, 5)$
(C) $(7, 0, 1)$
(D) $(-1, 0, 7)$
@ans A
@sol $Q = (\lambda, 1 + 2\lambda, 2 + 3\lambda)$; $\vec{PQ}\cdot(1, 2, 3) = 14\lambda - 14 = 0 \Rightarrow Q = (1, 3, 5)$. Image $= 2Q - P = (1, 0, 7)$.
@short —
@trap Giving the foot $(1, 3, 5)$ as the image.
@@END

@@Q M11-12 | E | 0.75 | Point–plane distance (insurance) | NV
Find the distance of $(1, 2, 3)$ from the plane $2x - y + 2z + 3 = 0$.
@ans 3
@sol $\dfrac{\lvert2 - 2 + 6 + 3\rvert}{\sqrt{4 + 1 + 4}} = \dfrac93 = 3$.
@short —
@trap —
@@END

@@SET M11 · Chapter Test

@@Q M11-T1 | E | 0.5 | Valid direction cosines | Concept
Which of the following can be the direction cosines of a line?
(A) $\tfrac12, \tfrac12, \tfrac12$
(B) $\tfrac{1}{\sqrt3}, \tfrac{1}{\sqrt3}, \tfrac{1}{\sqrt3}$
(C) $1, 1, 1$
(D) $\tfrac12, \tfrac{1}{\sqrt2}, 1$
@ans B
@sol Only (B) has $l^2 + m^2 + n^2 = 1$.
@short —
@trap —
@@END

@@Q M11-T2 | E | 0.5 | Distance from an axis | Speed
The distance of $(3, 4, 5)$ from the $x$-axis is:
(A) $\sqrt{41}$
(B) 3
(C) $5\sqrt2$
(D) $\sqrt{34}$
@ans A
@sol $\sqrt{y^2 + z^2} = \sqrt{16 + 25}$.
@short —
@trap Answering 3 (the $x$-coordinate).
@@END

@@Q M11-T3 | E | 0.5 | Perpendicular lines | NV
Find the angle (in degrees) between lines with direction ratios $(1, 2, 3)$ and $(-3, 0, 1)$.
@ans 90
@sol $-3 + 0 + 3 = 0$.
@short —
@trap —
@@END

@@Q M11-T4 | E | 0.5 | Centroid | NV
The centroid of the triangle with vertices $(1, 2, 3)$, $(2, 3, 1)$ and $(3, 1, 2)$ is $(\alpha, \beta, \gamma)$. Find $\alpha + \beta + \gamma$.
@ans 6
@sol The centroid is $(2, 2, 2)$.
@short Sum of all nine coordinates divided by 3: $18/3 = 6$.
@trap —
@@END

@@Q M11-T5 | E | 0.5 | Skew lines | Concept
Two lines in space are called skew when they are:
(A) parallel
(B) intersecting at right angles
(C) neither parallel nor intersecting
(D) coincident
@ans C
@sol —
@short —
@trap —
@@END

## Answers & Solutions {#m11-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · 3D Geometry
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
