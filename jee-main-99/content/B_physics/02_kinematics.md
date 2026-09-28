# Kinematics {#p02}

:::stats
Typical questions | ~1 per shift
Difficulty | Medium
Priority | High
NCERT | Class 11 · Ch 2, 3
Study time | ~10 hours
:::

## Concept summary

- **Kinematics** describes motion (position, velocity, acceleration) without asking what causes it.
- Everything comes from three definitions: $v = \dfrac{dx}{dt}$, $a = \dfrac{dv}{dt} = v\dfrac{dv}{dx}$, and the **slope/area** rules for graphs.
- For constant acceleration, the equations of motion are exact. For variable acceleration, **integrate**.
- 2D motion (projectiles, relative velocity, circular motion) = two independent 1D motions plus vector addition.

## Core theory & definitions

| Term | Meaning | Key point |
|---|---|---|
| Distance | Total path length (scalar) | Never decreases; ≥ displacement |
| Displacement | Change in position vector | Can be zero for non-zero distance |
| Average velocity | $\Delta\vec r/\Delta t$ | Average speed $=$ distance/time ≥ $|$average velocity$|$ |
| Instantaneous velocity | $d\vec r/dt$ | Always tangent to the path |
| Acceleration | $d\vec v/dt$ | Can be non-zero at an instant where $v = 0$ (top of a vertical throw) |

## Formulas

:::formula Uniformly accelerated motion (1D)
$$v = u + at \qquad s = ut + \tfrac12at^2 \qquad v^2 = u^2 + 2as \qquad s = \tfrac{(u+v)}{2}t$$
$$s_{n^{\text{th}}} = u + \tfrac a2(2n-1) \qquad \text{(displacement in the } n^{\text{th}} \text{ second)}$$
**Free fall from rest:** $h = \tfrac12gt^2$, $v = \sqrt{2gh}$. **Thrown up with $u$:** $H_{max} = \dfrac{u^2}{2g}$, time to top $= u/g$, return time $= 2u/g$.
**From rest, distances in successive equal intervals** are in the ratio $1:3:5:7:\dots$
:::

:::formula Variable acceleration
$$v = \int a\,dt \qquad x = \int v\,dt \qquad a = v\frac{dv}{dx} \Rightarrow \int v\,dv = \int a\,dx$$
Use $a = v\,dv/dx$ whenever $a$ or $v$ is given **as a function of position**.
:::

:::formula Projectile motion (ground to ground, launch speed $u$ at angle $\theta$)
$$T = \frac{2u\sin\theta}{g} \qquad H = \frac{u^2\sin^2\theta}{2g} \qquad R = \frac{u^2\sin2\theta}{g} \qquad R_{max} = \frac{u^2}{g}\ (\theta = 45^\circ)$$
$$y = x\tan\theta - \frac{g x^2}{2u^2\cos^2\theta} = x\tan\theta\left(1 - \frac{x}{R}\right)$$
- Complementary angles ($\theta$ and $90^\circ - \theta$) give the **same range**. $H_1/H_2 = \tan^2\theta$ for the pair, and $H_1H_2 = R^2/16$.
- $\dfrac{H}{R} = \dfrac{\tan\theta}{4}$ and $\dfrac{H}{T^2} = \dfrac{g}{8}$.
- **Horizontal launch** from height $h$ at speed $u$: $t = \sqrt{2h/g}$, range $= u\sqrt{2h/g}$.
- At the highest point: speed $= u\cos\theta$, acceleration $= g$ (downward), and velocity ⟂ acceleration.
:::

:::formula Relative velocity
$$\vec v_{AB} = \vec v_A - \vec v_B$$
**River crossing** (width $d$, boat speed $v$ relative to water, river speed $u$):
- Minimum time: head straight across. $t_{min} = d/v$, drift $= ud/v$.
- Zero drift (shortest path, needs $v > u$): head upstream at $\sin\alpha = u/v$ from the perpendicular. Then $t = \dfrac{d}{\sqrt{v^2-u^2}}$.

**Rain–person problems:** $\vec v_{\text{rain, rel. person}} = \vec v_{\text{rain}} - \vec v_{\text{person}}$. Hold the umbrella along the **relative** velocity.
:::

:::formula Circular motion
$$v = \omega r \qquad a_c = \frac{v^2}{r} = \omega^2 r \qquad a_t = \frac{dv}{dt} = \alpha r \qquad a_{net} = \sqrt{a_c^2 + a_t^2}$$
$\omega = 2\pi/T = 2\pi f$. In uniform circular motion, speed is constant but velocity is not, so the particle accelerates towards the centre.
:::

:::formula Vectors (used everywhere)
$|\vec A + \vec B| = \sqrt{A^2 + B^2 + 2AB\cos\theta}$; direction $\tan\alpha = \dfrac{B\sin\theta}{A + B\cos\theta}$ from $\vec A$.
$\vec A\cdot\vec B = AB\cos\theta$; $|\vec A\times\vec B| = AB\sin\theta$; component of $\vec A$ along $\vec B$ $= \vec A\cdot\hat B$.
$|\vec A + \vec B| = |\vec A - \vec B| \iff \vec A \perp \vec B$.
:::

## Graphs and how to read them

@@GRAPH kin-graphs

| Graph | Slope gives | Area gives |
|---|---|---|
| $x$–$t$ | velocity | — |
| $v$–$t$ | acceleration | **displacement** (signed); distance = total unsigned area |
| $a$–$t$ | jerk (not tested) | change in velocity |
| $v$–$x$ | $dv/dx$, so $a = v \times$ slope | — |

:::trap Graph traps
- A straight $x$–$t$ line means **constant velocity**, not constant acceleration.
- A curved $x$–$t$ graph bending upward means positive acceleration.
- On a $v$–$t$ graph, the area **below** the time axis is negative displacement. Distance counts it as positive.
- A $v$–$t$ graph can never be vertical (that would need infinite acceleration). An $x$–$t$ graph can never go backwards in time.
:::

## Standard models & assumptions

- Air resistance neglected; $g$ constant (take $10\ \text{m s}^{-2}$ unless told otherwise).
- Projectiles: horizontal velocity constant, vertical motion is free fall.
- "Particle" means size is ignored and there is no rotation.

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Variable acceleration:** $x(t)$ or $v(t)$ given as a polynomial, asked for the distance (not displacement) in an interval. Find where $v = 0$ first.
2. **Projectile relations:** $H$ vs $R$, complementary angles, equation of trajectory → $u$ and $\theta$.
3. **River–boat / rain–umbrella** relative velocity.
4. **Graph conversion:** given an $a$–$t$ or $v$–$t$ graph, find displacement or the shape of another graph.
5. **$n^{\text{th}}$-second distance** and ratio questions.
6. **Circular motion:** net acceleration with a tangential component.
:::

## Shortcuts

:::shortcut Distance vs displacement for polynomial motion
If $v(t)$ changes sign inside the interval, split the interval at the root of $v = 0$. Compute $|x(t_1) - x(0)| + |x(t_2) - x(t_1)|$.
**Time saved:** avoids integrating $|v|$. **Common mistake:** forgetting that the particle may reverse direction.
:::

:::shortcut Trajectory equation → everything
Write $y = ax - bx^2$. Then $\tan\theta = a$, $R = a/b$, $H = a^2/(4b)$, and $u^2 = \dfrac{g}{2b\cos^2\theta}$.
**When NOT to use:** when the launch point isn't at the origin.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Equations of motion, free fall | E | 1 min |
| Projectile formulas / ratios | E–M | 1.5 min |
| Variable acceleration with calculus | M | 2–3 min |
| Relative motion (river, rain, two bodies) | M | 2 min |
| Graph interpretation | E–M | 1.5 min |
| Projectile on an incline, or two-body chase | H | 3–4 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Using equations of motion when acceleration is **not** constant.
- Sign convention: pick "up = +" and **stay with it**. With up positive, $g$ enters as $-10$.
- In river problems, confusing "shortest time" (head straight across) with "shortest path" (head upstream).
- Treating speed at the top of a projectile's flight as zero. It's $u\cos\theta$.
:::

## Practice questions

@@SET P02 · Practice

@@Q P02-01 | E | 1 | Distance in nth second | Speed
A particle starts from rest with uniform acceleration and covers 15 m in the 3rd second. The distance it covers in the 5th second is:
(A) 21 m
(B) 25 m
(C) 27 m
(D) 30 m
@ans C
@sol $s_n = \tfrac a2(2n-1)$ for $u = 0$. $s_3 = \tfrac{5a}{2} = 15 \Rightarrow a = 6\ \text{m s}^{-2}$. $s_5 = \tfrac{9a}{2} = 27$ m.
@short $s_5 : s_3 = 9 : 5$, so $15 \times 9/5 = 27$.
@trap Using $s = \tfrac12 at^2$ for the whole 5 s.
@@END

@@Q P02-02 | M | 1.5 | H = R condition | Concept
A projectile's maximum height equals its horizontal range. The angle of projection is:
(A) $\tan^{-1}4$
(B) $\tan^{-1}2$
(C) $45^\circ$
(D) $\tan^{-1}(1/4)$
@ans A
@sol $\dfrac{H}{R} = \dfrac{\tan\theta}{4} = 1 \Rightarrow \tan\theta = 4$.
@short Memorise $H/R = \tan\theta/4$.
@trap Guessing 45° (which gives the maximum range, not $H = R$).
@@END

@@Q P02-03 | M | 1.5 | Rain–person relative velocity | Concept
Rain falls vertically at $12\ \text{m s}^{-1}$. A woman walks east at $5\ \text{m s}^{-1}$. To protect herself she should hold her umbrella:
(A) vertically
(B) tilted towards the east at $\tan^{-1}(5/12)$ from the vertical
(C) tilted towards the west at $\tan^{-1}(5/12)$ from the vertical
(D) tilted towards the east at $\tan^{-1}(12/5)$ from the vertical
@ans B
@sol $\vec v_{rain,woman} = \vec v_{rain} - \vec v_{woman} = (-5\hat i - 12\hat j)$ m s$^{-1}$. The rain appears to come from the east, falling towards the west. The umbrella must face the incoming rain, so tilt it **forward (east)** at $\tan^{-1}(5/12)$ from the vertical. Relative speed $= 13\ \text{m s}^{-1}$.
@short Tilt the umbrella in the direction you are walking.
@trap Measuring the angle from the horizontal gives (D).
@@END

@@Q P02-04 | M | 1.5 | River crossing: zero drift | NV
A river 100 m wide flows at $3\ \text{m s}^{-1}$. A boat moves at $5\ \text{m s}^{-1}$ relative to the water. Find the time (in s) to cross along the shortest path, landing directly opposite.
@ans 25
@sol For zero drift the boat heads upstream so that its upstream component cancels the river: $5\sin\alpha = 3$. The across-component is $\sqrt{25 - 9} = 4\ \text{m s}^{-1}$, so $t = 100/4 = 25$ s.
@short $t = d/\sqrt{v^2 - u^2}$.
@trap Answering $100/5 = 20$ s (that's the minimum-time case, which has drift).
@@END

@@Q P02-05 | M | 2 | Distance for velocity with sign change | Tricky
A particle moves along the $x$-axis with $v = 3t^2 - 6t$ (SI units), starting at $x = 0$. The distance it travels in the first 3 s is:
(A) 0 m
(B) 4 m
(C) 8 m
(D) 12 m
@ans C
@sol $x = t^3 - 3t^2$. $v = 0$ at $t = 0$ and $t = 2$ s. $x(2) = -4$, $x(3) = 0$. Distance $= |-4 - 0| + |0 - (-4)| = 8$ m. (Displacement $= 0$.)
@short Split at the root of $v = 0$.
@trap Answering the displacement (0 m).
@@END

@@Q P02-06 | E | 1 | Acceleration from v(x) | Concept
A particle moves so that $v = 2\sqrt x$ (SI units). Its acceleration is:
(A) $1\ \text{m s}^{-2}$, constant
(B) $2\ \text{m s}^{-2}$, constant
(C) $4\ \text{m s}^{-2}$, constant
(D) proportional to $\sqrt x$
@ans B
@sol $a = v\dfrac{dv}{dx} = 2\sqrt x\cdot\dfrac{1}{\sqrt x} = 2\ \text{m s}^{-2}$.
@short $v^2 = 4x$; compare with $v^2 = 2ax$, giving $a = 2$.
@trap Differentiating $v$ with respect to $x$ and stopping there.
@@END

@@Q P02-07 | E | 1.5 | Horizontal projection | NV
A ball is thrown horizontally at $20\ \text{m s}^{-1}$ from the top of a 45 m tower ($g = 10\ \text{m s}^{-2}$). Find the horizontal distance (in m) from the foot of the tower where it lands.
@ans 60
@sol Fall time $t = \sqrt{2h/g} = \sqrt{9} = 3$ s. $x = ut = 60$ m.
@short Fall time depends only on height.
@trap Using the projectile range formula $u^2\sin2\theta/g$ (which is for ground-to-ground launches).
@@END

@@Q P02-08 | M | 1.5 | Net acceleration in non-uniform circular motion | JEE
A particle moves on a circle of radius 2 m. Its speed increases at a constant $3\ \text{m s}^{-2}$. When its speed is $4\ \text{m s}^{-1}$, the magnitude of its acceleration is:
(A) $\sqrt{73}\ \text{m s}^{-2}$
(B) $11\ \text{m s}^{-2}$
(C) $5\ \text{m s}^{-2}$
(D) $8\ \text{m s}^{-2}$
@ans A
@sol $a_c = v^2/r = 16/2 = 8$; $a_t = 3$. $a = \sqrt{64 + 9} = \sqrt{73} \approx 8.5\ \text{m s}^{-2}$.
@short The two components are perpendicular: add in quadrature.
@trap Adding them directly (11).
@@END

@@Q P02-09 | E | 0.5 | Equal sum and difference | Speed
If $|\vec A + \vec B| = |\vec A - \vec B|$ for non-zero vectors, the angle between them is:
(A) $0^\circ$
(B) $45^\circ$
(C) $90^\circ$
(D) $180^\circ$
@ans C
@sol Squaring: $A^2 + B^2 + 2\vec A\cdot\vec B = A^2 + B^2 - 2\vec A\cdot\vec B \Rightarrow \vec A\cdot\vec B = 0$.
@short Diagonals of a parallelogram are equal only for a rectangle.
@trap None; this is a pure speed item.
@@END

@@SET P02 · Chapter Test

@@Q P02-T1 | E | 1 | Free fall at half time | Basic
A stone dropped from height $h$ reaches the ground in time $T$. At time $T/2$, its height above the ground is:
(A) $h/2$
(B) $h/4$
(C) $3h/4$
(D) $h/8$
@ans C
@sol Distance fallen $\propto t^2$: in $T/2$ it falls $h/4$. Height above ground $= 3h/4$.
@short Ratio $1:3$ in two equal halves of the time.
@trap Answering the distance fallen ($h/4$).
@@END

@@Q P02-T2 | E | 1 | Complementary angles | Basic
Two projectiles are launched at the same speed at $30^\circ$ and $60^\circ$. The ratio of their maximum heights $H_{30}:H_{60}$ is:
(A) $1:1$
(B) $1:3$
(C) $3:1$
(D) $1:\sqrt3$
@ans B
@sol $H \propto \sin^2\theta$: $\sin^230^\circ : \sin^260^\circ = \tfrac14 : \tfrac34 = 1:3$. (The ranges are equal.)
@short $H_1/H_2 = \tan^2\theta_1$ for complementary angles: $\tan^2 30^\circ = 1/3$.
@trap Confusing heights with ranges (1:1).
@@END

@@Q P02-T3 | M | 1.5 | Speed from trajectory equation | JEE
A projectile's trajectory is $y = \sqrt3\,x - \dfrac{x^2}{20}$ (SI units, $g = 10\ \text{m s}^{-2}$). Its speed of projection is:
(A) $10\ \text{m s}^{-1}$
(B) $20\ \text{m s}^{-1}$
(C) $20\sqrt3\ \text{m s}^{-1}$
(D) $40\ \text{m s}^{-1}$
@ans B
@sol $\tan\theta = \sqrt3 \Rightarrow \theta = 60^\circ$, $\cos^2\theta = \tfrac14$. $\dfrac{g}{2u^2\cos^2\theta} = \dfrac1{20} \Rightarrow \dfrac{10}{u^2/2} = \dfrac1{20} \Rightarrow u^2 = 400$, so $u = 20\ \text{m s}^{-1}$.
@short $u^2 = \dfrac{g}{2b\cos^2\theta}$ with $b = 1/20$.
@trap Forgetting $\cos^2\theta$.
@@END

@@Q P02-T4 | E | 1 | Braking distance | NV
A car moving at $20\ \text{m s}^{-1}$ brakes uniformly and stops in 40 m. Find the magnitude of its deceleration (in $\text{m s}^{-2}$).
@ans 5
@sol $0 = u^2 - 2as \Rightarrow a = \dfrac{400}{80} = 5\ \text{m s}^{-2}$.
@short Stopping distance $= u^2/2a$.
@trap Forgetting the factor 2.
@@END

@@Q P02-T5 | E | 0.5 | Angular speed of a clock hand | Speed
The angular speed of the minute hand of a clock is:
(A) $\pi/30\ \text{rad s}^{-1}$
(B) $\pi/1800\ \text{rad s}^{-1}$
(C) $\pi/3600\ \text{rad s}^{-1}$
(D) $\pi/21600\ \text{rad s}^{-1}$
@ans B
@sol $\omega = 2\pi/T = 2\pi/3600 = \pi/1800\ \text{rad s}^{-1}$.
@short Minute hand: $T = 1$ h. Hour hand: $T = 12$ h.
@trap Using 60 s (the second hand).
@@END

## Answers & Solutions {#p02-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Kinematics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
