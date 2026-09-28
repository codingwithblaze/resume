# Differential Equations {#m09}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 12 · Ch 9
Study time | ~7 hours
:::

## Core concepts

- A **differential equation** relates a function and its derivatives. The **order** is the highest derivative. The **degree** is the power of that highest derivative once the equation is a polynomial in its derivatives (undefined otherwise, e.g. $\sin y'$).
- The syllabus solves three types: **variables separable**, **homogeneous** and **linear first-order** ($y' + P(x)y = Q(x)$).
- An initial condition picks out one particular solution from the general family.

:::note Syllabus note
Formation of differential equations is not listed in the 2024–2026 text. It covers order and degree, separation of variables, homogeneous equations and the linear type $\frac{dy}{dx} + p(x)y = q(x)$ [NTA-SYL].
:::

## Important formulas & standard results

:::formula Solution methods
| Type | Form | Method |
|---|---|---|
| Separable | $\dfrac{dy}{dx} = f(x)g(y)$ | $\int\dfrac{dy}{g(y)} = \int f(x)\,dx + C$ |
| Homogeneous | $\dfrac{dy}{dx} = F\!\left(\dfrac yx\right)$ | put $y = vx$: $v + x\dfrac{dv}{dx} = F(v)$, then separate |
| Linear in $y$ | $\dfrac{dy}{dx} + Py = Q$ | IF $= e^{\int P\,dx}$; $y\cdot\text{IF} = \int Q\cdot\text{IF}\,dx + C$ |
| Linear in $x$ | $\dfrac{dx}{dy} + P(y)x = Q(y)$ | IF $= e^{\int P\,dy}$; $x\cdot\text{IF} = \int Q\cdot\text{IF}\,dy + C$ |
:::

:::formula Useful integrating factors
$P = \dfrac1x \to \text{IF} = x$; $P = -\dfrac1x \to \dfrac1x$; $P = \dfrac nx \to x^n$; $P = k \to e^{kx}$; $P = \tan x \to \sec x$; $P = \cot x \to \sin x$.
**Exact-derivative recognition:** $x\,dy + y\,dx = d(xy)$; $\dfrac{x\,dy - y\,dx}{x^2} = d\!\left(\dfrac yx\right)$; $\dfrac{x\,dy - y\,dx}{x^2 + y^2} = d\!\left(\tan^{-1}\dfrac yx\right)$.
:::

:::formula Applications
Growth/decay: $\dfrac{dN}{dt} = kN \Rightarrow N = N_0e^{kt}$. Doubling time $= \dfrac{\ln2}{k}$; it takes twice the doubling time to quadruple.
Newton's law of cooling: $\dfrac{dT}{dt} = -k(T - T_0) \Rightarrow T - T_0 = (T_i - T_0)e^{-kt}$.
:::

## Common question models

:::pyq Recurring structures
1. **Order and degree**, including "degree not defined" cases and radicals that must be cleared first.
2. **Linear DE with an initial condition** → find $y$ at a point (a very common NV).
3. **Homogeneous DE** → particular solution or curve family.
4. **Separable equations** with exponentials or trig functions.
5. **Equations that are linear in $x$** ($dx/dy$ form).
6. **Application problems:** growth, cooling, curves whose tangent slope satisfies a condition.
:::

## Shortcuts & fast methods

:::shortcut Choose the dependent variable
If the equation is linear in $x$ but not in $y$ (for example, $y$ appears as $y^2$ or $e^y$ while $x$ appears linearly), rewrite it as $\dfrac{dx}{dy}$ and solve for $x$.
:::

:::shortcut Verify by substitution
With options of the form $y = f(x)$, substitute into the DE and the initial condition. Often the initial condition alone eliminates 2–3 options.
:::

## Common mistakes

:::trap Mistake alerts
- Writing the DE in standard form **before** reading off $P$: $x\,y' - y = x^2$ becomes $y' - \dfrac yx = x$, so $P = -\dfrac1x$.
- Losing the constant of integration before applying the initial condition.
- Degree: clear radicals and fractional powers of the derivatives first.
- $e^{\int P\,dx}$ with $P = \dfrac1x$ gives IF $= x$, not $\ln x$.
:::

## Practice questions

@@SET M09 · Practice

@@Q M09-01 | E | 0.5 | Order and degree | Speed
The order and degree of $\left(\dfrac{d^2y}{dx^2}\right)^3 + \left(\dfrac{dy}{dx}\right)^2 + y = 0$ are:
(A) 2, 3
(B) 3, 2
(C) 2, 2
(D) 1, 3
@ans A
@sol The highest derivative is $y''$ (order 2), raised to the power 3 (degree 3).
@short —
@trap —
@@END

@@Q M09-02 | M | 1 | Degree after clearing a radical | Concept
The degree of $\dfrac{d^2y}{dx^2} = \sqrt{1 + \left(\dfrac{dy}{dx}\right)^2}$ is:
(A) 1
(B) 2
(C) 1/2
(D) not defined
@ans B
@sol Squaring: $(y'')^2 = 1 + (y')^2$, so the degree is 2.
@short —
@trap Answering 1 without clearing the radical.
@@END

@@Q M09-03 | E | 1 | Separable with initial condition | Basic
The solution of $\dfrac{dy}{dx} = xy$ with $y(0) = 1$ is:
(A) $y = e^{x^2}$
(B) $y = e^{x^2/2}$
(C) $y = 1 + \dfrac{x^2}{2}$
(D) $y = e^{x}$
@ans B
@sol $\ln y = \dfrac{x^2}{2} + C$, and $C = 0$ from $y(0) = 1$.
@short —
@trap —
@@END

@@Q M09-04 | M | 1 | Linear DE | Basic
The general solution of $\dfrac{dy}{dx} + y = e^{-x}$ is:
(A) $y = (x + C)e^{-x}$
(B) $y = (x + C)e^{x}$
(C) $y = Ce^{-x}$
(D) $y = xe^{x} + C$
@ans A
@sol IF $= e^x$: $ye^x = \int1\,dx = x + C$.
@short —
@trap —
@@END

@@Q M09-05 | M | 1.5 | Homogeneous DE | Concept
The general solution of $\dfrac{dy}{dx} = \dfrac{x + y}{x}$ ($x > 0$) is:
(A) $y = x\ln x + Cx$
(B) $y = \ln x + C$
(C) $y = x^2 + C$
(D) $y = Cx$
@ans A
@sol $y' - \dfrac yx = 1$ (linear) with IF $= \dfrac1x$: $\dfrac yx = \ln x + C$. (Or put $y = vx$: $x\,v' = 1$.)
@short —
@trap —
@@END

@@Q M09-06 | E | 0.75 | Integrating factor | Basic
The integrating factor of $x\dfrac{dy}{dx} - y = x^2$ ($x > 0$) is:
(A) $x$
(B) $1/x$
(C) $e^x$
(D) $\ln x$
@ans B
@sol Standard form: $y' - \dfrac1x y = x$, so IF $= e^{-\ln x} = \dfrac1x$.
@short —
@trap Reading $P$ before dividing by $x$.
@@END

@@Q M09-07 | E | 0.5 | Direct integration | NV
If $\dfrac{dy}{dx} = 2x$ and $y(1) = 3$, find $y(2)$.
@ans 6
@sol $y = x^2 + 2$, so $y(2) = 6$.
@short —
@trap —
@@END

@@Q M09-08 | M | 1 | Exponential growth | NV
A population grows at a rate proportional to its size and doubles in 10 years. Find the number of years it takes to become 4 times its initial size.
@ans 20
@sol $N = N_02^{t/10}$; $2^{t/10} = 4 \Rightarrow t = 20$.
@short Two doublings.
@trap Assuming linear growth (30).
@@END

@@Q M09-09 | M | 1.5 | Linear DE with initial condition | JEE
The solution of $\dfrac{dy}{dx} + \dfrac2xy = x$ ($x > 0$) through $(1, 1)$ is:
(A) $y = \dfrac{x^2}{4} + \dfrac{3}{4x^2}$
(B) $y = \dfrac{x^2}{4} + \dfrac{1}{x^2}$
(C) $y = x^2$
(D) $y = \dfrac{x^2}{2} + \dfrac{1}{2x^2}$
@ans A
@sol IF $= x^2$: $x^2y = \dfrac{x^4}{4} + C$. At $(1, 1)$: $C = \dfrac34$.
@short Check the options at $x = 1$: (A) gives $\frac14 + \frac34 = 1$ ✓; (B) gives $1.25$ ✗; (D) gives 1 ✓, so test the DE for (D): it fails.
@trap —
@@END

@@Q M09-10 | E | 0.5 | Degree not defined | Concept
The degree of the differential equation $\dfrac{dy}{dx} + \sin\left(\dfrac{dy}{dx}\right) = x$ is:
(A) 1
(B) 0
(C) 2
(D) not defined
@ans D
@sol The equation isn't a polynomial in $y'$.
@short —
@trap —
@@END

@@SET M09 · Chapter Test

@@Q M09-T1 | E | 0.5 | Order | Speed
The order of $y''' + y = 0$ is:
(A) 1
(B) 2
(C) 3
(D) 0
@ans C
@sol —
@short —
@trap —
@@END

@@Q M09-T2 | E | 0.5 | Simplest DE | Speed
The general solution of $\dfrac{dy}{dx} = y$ is:
(A) $y = Cx$
(B) $y = Ce^x$
(C) $y = x + C$
(D) $y = Ce^{-x}$
@ans B
@sol —
@short —
@trap —
@@END

@@Q M09-T3 | E | 0.5 | Integrating factor exponent | NV
The integrating factor of $\dfrac{dy}{dx} + 3y = 5$ is $e^{kx}$. Find $k$.
@ans 3
@sol $P = 3$, so IF $= e^{3x}$.
@short —
@trap —
@@END

@@Q M09-T4 | E | 0.5 | Homogeneous substitution | Speed
A homogeneous DE $\dfrac{dy}{dx} = F(y/x)$ is solved with the substitution:
(A) $y = vx$
(B) $y = x + v$
(C) $x = y^2$
(D) $y = e^v$
@ans A
@sol —
@short —
@trap —
@@END

@@Q M09-T5 | M | 0.75 | Linear in x | Concept
The equation $\dfrac{dy}{dx} = \dfrac{y}{x + y^2}$ is best solved by treating it as:
(A) linear in $y$
(B) linear in $x$ (use $\frac{dx}{dy}$)
(C) separable
(D) homogeneous
@ans B
@sol $\dfrac{dx}{dy} = \dfrac{x + y^2}{y} \Rightarrow \dfrac{dx}{dy} - \dfrac xy = y$, which is linear in $x$.
@short —
@trap —
@@END

## Answers & Solutions {#m09-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Differential Equations
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
