# Coordinate Geometry: Lines, Circles & Conics {#m10}

:::stats
Typical questions | 3–4 per shift
Difficulty | Medium
Priority | Must-do (largest Maths unit)
NCERT | Class 11 · Ch 9, 10
Study time | ~20 hours
:::

## Core concepts

- **Points & lines:** distance, section formula, slope, forms of a line, angle between lines, distance from a point, concurrency; the centroid, orthocentre and circumcentre of a triangle.
- **Circle:** standard and general forms, circles on a diameter, intersection with lines.
- **Conics** (parabola, ellipse, hyperbola) **in standard form**: focus, directrix, eccentricity, latus rectum, vertices, axes.

:::note Syllabus note
The official Unit 10 text covers points and lines (including intercepts, concurrency, triangle centres), circles (standard/general form, diameter form, intersection with a line through the origin-centred case) and conics in standard forms [NTA-SYL]. Tangent/normal equations, family of lines and angle bisectors were removed in 2024. This module stays on the listed core.
:::

## Important formulas: points & lines

:::formula Points
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \qquad \text{section } m:n \text{ internal: } \left(\frac{mx_2 + nx_1}{m + n}, \frac{my_2 + ny_1}{m + n}\right)$$
Centroid $G = \left(\dfrac{x_1 + x_2 + x_3}{3}, \dfrac{y_1 + y_2 + y_3}{3}\right)$. **Euler line:** $O$ (orthocentre), $G$, $C$ (circumcentre) are collinear with $OG : GC = 2 : 1$.
In a right triangle the circumcentre is the midpoint of the hypotenuse, and the orthocentre is the right-angle vertex.
Area of a triangle $= \tfrac12\lvert x_1(y_2 - y_3) + x_2(y_3 - y_1) + x_3(y_1 - y_2)\rvert$.
:::

:::formula Lines
| Form | Equation |
|---|---|
| slope–intercept | $y = mx + c$ |
| point–slope | $y - y_1 = m(x - x_1)$ |
| two-point | $\dfrac{y - y_1}{y_2 - y_1} = \dfrac{x - x_1}{x_2 - x_1}$ |
| intercept | $\dfrac xa + \dfrac yb = 1$ |
| normal | $x\cos\alpha + y\sin\alpha = p$ |
| general | $ax + by + c = 0$: slope $-a/b$, intercepts $-c/a$, $-c/b$ |

$$\tan\theta = \left\lvert\frac{m_1 - m_2}{1 + m_1m_2}\right\rvert \qquad \text{parallel: } m_1 = m_2 \qquad \text{perpendicular: } m_1m_2 = -1$$
$$\text{distance of } (x_1, y_1) \text{ from } ax + by + c = 0:\ \frac{\lvert ax_1 + by_1 + c\rvert}{\sqrt{a^2 + b^2}} \qquad \text{between parallel lines: } \frac{\lvert c_1 - c_2\rvert}{\sqrt{a^2 + b^2}}$$
**Concurrency** of $a_ix + b_iy + c_i = 0$ ($i = 1, 2, 3$): $\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix} = 0$.
**Foot of perpendicular / image** of $(x_1, y_1)$ in $ax + by + c = 0$: $\dfrac{x - x_1}{a} = \dfrac{y - y_1}{b} = -\dfrac{ax_1 + by_1 + c}{a^2 + b^2}$ (use $-2(\cdot)$ for the image).
:::

## Important formulas: circles

:::formula Circle
$$(x - h)^2 + (y - k)^2 = r^2 \qquad x^2 + y^2 + 2gx + 2fy + c = 0:\ \text{centre } (-g, -f),\ r = \sqrt{g^2 + f^2 - c}$$
**Diameter form** (ends $A$, $B$): $(x - x_1)(x - x_2) + (y - y_1)(y - y_2) = 0$.
**Line and circle:** with $d$ = distance from the centre to the line: $d < r$ secant (2 points), $d = r$ touching, $d > r$ no intersection. Chord length $= 2\sqrt{r^2 - d^2}$.
**Two circles** ($d$ = distance between centres): $d > r_1 + r_2$ separate; $= r_1 + r_2$ touch externally; $\lvert r_1 - r_2\rvert < d < r_1 + r_2$ intersect; $= \lvert r_1 - r_2\rvert$ touch internally.
A point is inside, on or outside the circle according to whether $S_1 = x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c$ is $< 0$, $= 0$ or $> 0$.
:::

## Important formulas: conics (standard forms)

:::formula Parabola $y^2 = 4ax$ ($a > 0$)
Vertex $(0, 0)$ · focus $(a, 0)$ · directrix $x = -a$ · axis $y = 0$ · latus rectum $4a$ (ends $(a, \pm2a)$) · $e = 1$ · focal distance of $(x, y)$: $x + a$ · parametric $(at^2, 2at)$.
Other orientations: $y^2 = -4ax$, $x^2 = 4ay$ (focus $(0, a)$), $x^2 = -4ay$.
:::

:::formula Ellipse $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ ($a > b$)
$b^2 = a^2(1 - e^2)$ · foci $(\pm ae, 0)$ · directrices $x = \pm\dfrac ae$ · latus rectum $\dfrac{2b^2}{a}$ · major axis $2a$, minor axis $2b$ · $e < 1$.
**Focal property:** $PS + PS' = 2a$. Parametric: $(a\cos\theta, b\sin\theta)$. If $b > a$, the major axis is along $y$ and $a^2 = b^2(1 - e^2)$.
:::

:::formula Hyperbola $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$
$b^2 = a^2(e^2 - 1)$ · foci $(\pm ae, 0)$ · directrices $x = \pm\dfrac ae$ · latus rectum $\dfrac{2b^2}{a}$ · transverse axis $2a$ · $e > 1$ · **asymptotes** $y = \pm\dfrac bax$ · $\lvert PS - PS'\rvert = 2a$.
**Rectangular hyperbola** $a = b$: $e = \sqrt2$. **Conjugate hyperbola** $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$: $\dfrac{1}{e_1^2} + \dfrac{1}{e_2^2} = 1$.
:::

| Conic | $e$ | Latus rectum | Focus–directrix |
|---|---|---|---|
| Circle | 0 | — | — |
| Parabola $y^2 = 4ax$ | 1 | $4a$ | focus $(a, 0)$, directrix $x = -a$ |
| Ellipse | $\sqrt{1 - b^2/a^2}$ | $2b^2/a$ | $(\pm ae, 0)$; $x = \pm a/e$ |
| Hyperbola | $\sqrt{1 + b^2/a^2}$ | $2b^2/a$ | $(\pm ae, 0)$; $x = \pm a/e$ |

## Common question models

:::pyq Recurring structures
1. **Triangle centres** from vertices or side equations; reflection/image of a point; foot of the perpendicular.
2. **Distance/angle** between lines; lines at a given distance or angle through a point.
3. **Circle from conditions** (centre on a line, passing through points, touching the axes); chord lengths; relative position of two circles.
4. **Conic parameters:** find $e$, foci, latus rectum, or the equation from given data; ellipse/hyperbola with the same foci.
5. **Locus problems:** eliminate a parameter to get a line, circle or conic.
6. **Area** of regions defined by lines/conics (overlaps with integration).
:::

## Shortcuts & fast methods

:::shortcut Reflection formula
The image of $(x_1, y_1)$ in $ax + by + c = 0$ is $(x_1, y_1) - \dfrac{2(ax_1 + by_1 + c)}{a^2 + b^2}(a, b)$. It's a single vector step, so there's no need to find the foot first.
:::

:::shortcut Circles touching both axes
Centre $(\pm r, \pm r)$ and radius $r$: $(x \mp r)^2 + (y \mp r)^2 = r^2$. A circle touching the x-axis has $r = \lvert k\rvert$; touching the y-axis, $r = \lvert h\rvert$.
:::

:::shortcut Eccentricity from latus rectum
For an ellipse or hyperbola, $\ell = \dfrac{2b^2}{a}$ together with $b^2 = a^2(1 \mp e^2)$ gives $e$ in two lines. Keep "ellipse: minus; hyperbola: plus" in mind.
:::

## Common mistakes

:::trap Mistake alerts
- Assuming $a > b$ for an ellipse without checking. If the $y^2$ denominator is larger, the major axis is vertical.
- Hyperbola: $b^2 = a^2(e^2 - 1)$, not $(1 - e^2)$.
- Radius of $x^2 + y^2 + 2gx + 2fy + c = 0$ needs the coefficients of $x^2$ and $y^2$ to equal 1 first. Divide if they don't.
- Distance formula: the line must be in the form $ax + by + c = 0$ before substituting.
:::

## Practice questions

@@SET M10 · Practice

@@Q M10-01 | E | 1 | Centroid | Basic
The centroid of the triangle with vertices $(1, 2)$, $(3, 4)$ and $(5, 0)$ is:
(A) $(3, 2)$
(B) $(9, 6)$
(C) $(3, 3)$
(D) $(2, 3)$
@ans A
@sol $\left(\dfrac{9}{3}, \dfrac{6}{3}\right)$.
@short —
@trap —
@@END

@@Q M10-02 | E | 1 | Distance between parallel lines | NV
Find the distance between the parallel lines $3x + 4y - 5 = 0$ and $6x + 8y + 20 = 0$.
@ans 3
@sol Write the second as $3x + 4y + 10 = 0$. Distance $= \dfrac{\lvert -5 - 10\rvert}{5} = 3$.
@short Normalise the coefficients first.
@trap Using $c_2 = 20$ directly gives 5.
@@END

@@Q M10-03 | M | 1.5 | Image of a point | JEE
The image of the point $(1, 2)$ in the line $x + y - 5 = 0$ is:
(A) $(3, 4)$
(B) $(4, 3)$
(C) $(2, 1)$
(D) $(-1, -2)$
@ans A
@sol $\dfrac{2(1 + 2 - 5)}{2} = -2$, so the image is $(1, 2) - (-2)(1, 1) = (3, 4)$.
@short —
@trap Giving the foot $(2, 3)$ instead of the image.
@@END

@@Q M10-04 | E | 0.75 | Circle centre and radius | Basic
The centre and radius of $x^2 + y^2 - 4x + 6y - 12 = 0$ are:
(A) $(2, -3)$, 5
(B) $(-2, 3)$, 5
(C) $(2, -3)$, 25
(D) $(4, -6)$, 5
@ans A
@sol $g = -2$, $f = 3$: centre $(2, -3)$, $r = \sqrt{4 + 9 + 12} = 5$.
@short —
@trap —
@@END

@@Q M10-05 | M | 1 | Chord length | NV
Find the length of the chord cut by the line $x = 3$ from the circle $x^2 + y^2 = 25$.
@ans 8
@sol $d = 3$, so the chord is $2\sqrt{25 - 9} = 8$.
@short —
@trap —
@@END

@@Q M10-06 | E | 0.75 | Parabola focus and latus rectum | Basic
For the parabola $y^2 = 12x$, the focus and the length of the latus rectum are:
(A) $(3, 0)$, 12
(B) $(12, 0)$, 3
(C) $(0, 3)$, 12
(D) $(3, 0)$, 6
@ans A
@sol $4a = 12 \Rightarrow a = 3$.
@short —
@trap —
@@END

@@Q M10-07 | M | 1 | Ellipse eccentricity | Basic
The eccentricity of the ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ is:
(A) $3/5$
(B) $4/5$
(C) $5/3$
(D) $3/4$
@ans A
@sol $e^2 = 1 - \dfrac{16}{25} = \dfrac{9}{25}$.
@short —
@trap —
@@END

@@Q M10-08 | M | 1 | Hyperbola asymptotes | Basic
The asymptotes of $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$ are:
(A) $y = \pm\tfrac34x$
(B) $y = \pm\tfrac43x$
(C) $y = \pm\tfrac{9}{16}x$
(D) $x = \pm4$
@ans A
@sol $y = \pm\dfrac bax$ with $a = 4$, $b = 3$.
@short —
@trap —
@@END

@@Q M10-09 | M | 1.5 | Relative position of circles | Concept
The circles $x^2 + y^2 = 4$ and $x^2 + y^2 - 6x + 5 = 0$:
(A) touch externally
(B) intersect at two points
(C) are separate
(D) touch internally
@ans B
@sol $C_1 = (0, 0)$, $r_1 = 2$. $C_2 = (3, 0)$, $r_2 = \sqrt{9 - 5} = 2$. $d = 3$, and $0 < 3 < 4$, so they intersect.
@short —
@trap —
@@END

@@Q M10-10 | M | 1.5 | Ellipse from foci and latus rectum | JEE
An ellipse centred at the origin with foci on the x-axis has eccentricity $1/2$ and latus rectum 6. Its equation is:
(A) $\dfrac{x^2}{16} + \dfrac{y^2}{12} = 1$
(B) $\dfrac{x^2}{12} + \dfrac{y^2}{16} = 1$
(C) $\dfrac{x^2}{4} + \dfrac{y^2}{3} = 1$
(D) $\dfrac{x^2}{36} + \dfrac{y^2}{27} = 1$
@ans A
@sol $b^2 = a^2(1 - \tfrac14) = \tfrac34a^2$ and $\dfrac{2b^2}{a} = 6 \Rightarrow \tfrac32a = 6 \Rightarrow a = 4$, $b^2 = 12$.
@short Check the options' latus rectum: (A) $2\cdot12/4 = 6$ ✓, and $e^2 = 1 - 12/16 = 1/4$ ✓.
@trap —
@@END

@@Q M10-11 | M | 1 | Angle between lines | Basic
The acute angle between $y = 2x + 1$ and $y = -3x + 4$ is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $90^\circ$
@ans B
@sol $\tan\theta = \left\lvert\dfrac{2 - (-3)}{1 + (2)(-3)}\right\rvert = \dfrac{5}{5} = 1$.
@short —
@trap —
@@END

@@Q M10-12 | M | 1.5 | Circle on a diameter | Concept
The circle with the segment joining $(1, 2)$ and $(5, 6)$ as diameter is:
(A) $x^2 + y^2 - 6x - 8y + 17 = 0$
(B) $x^2 + y^2 + 6x + 8y + 17 = 0$
(C) $x^2 + y^2 - 6x - 8y - 17 = 0$
(D) $x^2 + y^2 - 3x - 4y + 17 = 0$
@ans A
@sol $(x - 1)(x - 5) + (y - 2)(y - 6) = 0 \Rightarrow x^2 + y^2 - 6x - 8y + 5 + 12 = 0$.
@short Centre $(3, 4)$ fixes $-6x - 8y$. The constant is $x_1x_2 + y_1y_2 = 5 + 12$.
@trap —
@@END

@@SET M10 · Chapter Test

@@Q M10-T1 | E | 0.5 | Perpendicular slopes | Speed
A line perpendicular to $2x - 3y + 5 = 0$ has slope:
(A) $2/3$
(B) $-3/2$
(C) $3/2$
(D) $-2/3$
@ans B
@sol The given slope is $\tfrac23$; perpendicular means $-\tfrac32$.
@short —
@trap —
@@END

@@Q M10-T2 | E | 0.5 | Directrix of a parabola | Speed
The directrix of $x^2 = 8y$ is:
(A) $y = -2$
(B) $y = 2$
(C) $x = -2$
(D) $y = -8$
@ans A
@sol $4a = 8$, so $a = 2$: the directrix is $y = -2$.
@short —
@trap —
@@END

@@Q M10-T3 | E | 0.75 | Distance from a point to a line | NV
Find the distance of $(2, 3)$ from $5x + 12y + 6 = 0$.
@ans 4
@sol $\dfrac{\lvert10 + 36 + 6\rvert}{\sqrt{25 + 144}} = \dfrac{52}{13} = 4$.
@short —
@trap —
@@END

@@Q M10-T4 | E | 0.5 | Rectangular hyperbola | Speed
The eccentricity of a rectangular hyperbola is:
(A) 1
(B) $\sqrt2$
(C) 2
(D) $\sqrt3$
@ans B
@sol $a = b \Rightarrow e^2 = 2$.
@short —
@trap —
@@END

@@Q M10-T5 | E | 0.75 | Circle touching both axes | Basic
A circle of radius 3 in the first quadrant touches both axes. Its equation is:
(A) $x^2 + y^2 - 6x - 6y + 9 = 0$
(B) $x^2 + y^2 - 6x - 6y = 0$
(C) $x^2 + y^2 + 6x + 6y + 9 = 0$
(D) $x^2 + y^2 - 3x - 3y + 9 = 0$
@ans A
@sol Centre $(3, 3)$, $r = 3$: $x^2 + y^2 - 6x - 6y + 18 - 9 = 0$.
@short —
@trap —
@@END

## Answers & Solutions {#m10-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Coordinate Geometry
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
