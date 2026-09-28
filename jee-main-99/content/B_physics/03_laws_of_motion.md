# Laws of Motion {#p03}

:::stats
Typical questions | ~1 per shift
Difficulty | Medium
Priority | High
NCERT | Class 11 · Ch 4
Study time | ~10 hours
:::

## Concept summary

- **Newton I:** a body stays at rest or in uniform motion unless a net external force acts. It defines inertial frames.
- **Newton II:** $\vec F_{net} = \dfrac{d\vec p}{dt}$, which is $m\vec a$ for constant mass. **Newton III:** forces come in equal and opposite pairs acting on *different* bodies.
- **Method for every problem:** isolate each body → draw a **free-body diagram (FBD)** → choose axes → write $\sum F = ma$ per axis → add the **constraint** relations (string length, contact) → solve.
- **Friction** adjusts itself up to $\mu_sN$ (static) and is $\mu_kN$ once sliding. **Circular motion** needs a net inward force $mv^2/r$ supplied by real forces.

## Formulas

:::formula Momentum & impulse
$$\vec p = m\vec v \qquad \vec J = \int\vec F\,dt = \Delta\vec p \qquad \text{No external force} \Rightarrow \vec p_{total} = \text{constant}$$
Recoil: $m_{bullet}v_{bullet} = M_{gun}V_{gun}$. For a rebound from a wall: $|\Delta p| = m(v_1 + v_2)$.
:::

:::formula Standard systems
| System | Acceleration | Tension / normal force |
|---|---|---|
| Atwood machine ($m_2 > m_1$) | $a = \dfrac{(m_2 - m_1)g}{m_1 + m_2}$ | $T = \dfrac{2m_1m_2g}{m_1 + m_2}$ |
| Block $m_1$ on smooth table pulled by hanging $m_2$ | $a = \dfrac{m_2g}{m_1 + m_2}$ | $T = \dfrac{m_1m_2g}{m_1 + m_2}$ |
| Lift accelerating **up** at $a$ | — | apparent weight $N = m(g + a)$ |
| Lift accelerating **down** at $a$ | — | $N = m(g - a)$; free fall: $N = 0$ |
| Smooth incline | $a = g\sin\theta$ | $N = mg\cos\theta$ |
| Rough incline, sliding down | $a = g(\sin\theta - \mu_k\cos\theta)$ | — |
| Pendulum in a car accelerating at $a$ | string at $\tan\theta = a/g$ from the vertical | $T = m\sqrt{g^2 + a^2}$ |
:::

:::formula Friction
$$f_s \le \mu_sN \qquad f_k = \mu_kN \qquad \mu_k < \mu_s \qquad \text{angle of repose: } \tan\theta_r = \mu_s \qquad \text{angle of friction: } \tan\lambda = \mu_s$$
- Minimum force to move a block on a horizontal surface (pull at angle $\phi$ above the horizontal): $F_{min} = \dfrac{\mu mg}{\sqrt{1+\mu^2}}$ at $\tan\phi = \mu$.
- Two blocks (top $m$ on bottom $M$, force on the bottom block): they move together as long as $F \le \mu_s(m+M)g$.
:::

:::formula Circular dynamics
$$\text{Level road: } v_{max} = \sqrt{\mu rg} \qquad \text{Banked road, no friction: } v = \sqrt{rg\tan\theta}$$
$$\text{Banked road with friction: } v_{max} = \sqrt{rg\,\frac{\mu + \tan\theta}{1 - \mu\tan\theta}} \qquad v_{min} = \sqrt{rg\,\frac{\tan\theta - \mu}{1 + \mu\tan\theta}}$$
Conical pendulum (string length $L$, angle $\theta$): $\tan\theta = \dfrac{v^2}{rg}$, $T = 2\pi\sqrt{\dfrac{L\cos\theta}{g}}$.
:::

:::formula Equilibrium of concurrent forces
$\sum\vec F = 0$. **Lami's theorem** for three forces: $\dfrac{F_1}{\sin\alpha} = \dfrac{F_2}{\sin\beta} = \dfrac{F_3}{\sin\gamma}$, where each angle is the one **opposite** that force (between the other two).
:::

@@GRAPH friction-graph

:::important Friction is a self-adjusting force
Below the limit, static friction equals exactly what's needed to prevent slipping. It is **not** $\mu_sN$. The value $\mu_sN$ is only the maximum. Always first check whether the body slips: compare the applied force (or the force needed for common motion) with $\mu_sN$.
:::

## Standard models & assumptions

- Strings are massless and inextensible (same tension throughout, same acceleration magnitude at both ends). Pulleys are massless and frictionless unless stated otherwise.
- "Smooth" means no friction. "Rough" means friction, with $\mu$ given.
- **Pseudo force** $-m\vec a_0$ acts on every body when you analyse from a frame accelerating at $\vec a_0$.

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Two-block systems** with friction between blocks: find the maximum force for common motion, or the accelerations when slipping occurs.
2. **Incline + friction:** acceleration, minimum/maximum force to hold a block, time to slide down.
3. **Banked roads** and conical pendulums.
4. **Connected bodies over pulleys**: tension and acceleration, sometimes with a movable pulley ($a_1 = 2a_2$ constraint).
5. **Impulse from a force–time graph**: area under the $F$–$t$ graph.
6. **Equilibrium of a mass hung by two strings**: Lami's theorem or components.
:::

## Shortcuts

:::shortcut System approach for acceleration
For connected bodies moving with the same acceleration magnitude: $a = \dfrac{\text{(net driving force)}}{\text{(total mass)}}$. Then find any tension from **one** body's FBD.
**When NOT to use:** when bodies can slip relative to each other. Check the friction limit first.
**Time saved:** about 1 minute per pulley problem.
:::

:::shortcut Pulley constraint in 5 seconds
For a movable pulley carrying block B, with the string's free end attached to A: $x_A + 2x_B = \text{const} \Rightarrow a_A = 2a_B$. Count the strings supporting the pulley.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Lift, recoil, impulse | E | 1 min |
| Atwood / pulley system | E–M | 1.5 min |
| Incline with friction | M | 2 min |
| Banked road / conical pendulum | M | 2 min |
| Two-block friction (slip check) | M–H | 3 min |
| Variable force + pseudo force combined | H | 3–4 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Writing friction $= \mu_sN$ when the body doesn't move.
- Putting a Newton-III pair on the **same** FBD.
- Forgetting that $N \ne mg$ on an incline, or when a force is applied at an angle.
- Using the pseudo force in an inertial frame too, which counts it twice.
- Impulse on a rebound: $m(v_1 + v_2)$, **not** $m(v_1 - v_2)$.
:::

## Practice questions

@@SET P03 · Practice

@@Q P03-01 | E | 1 | Atwood machine tension | Basic
Masses of 3 kg and 5 kg hang from the two ends of a light string over a frictionless pulley ($g = 10\ \text{m s}^{-2}$). The tension in the string is:
(A) 30 N
(B) 37.5 N
(C) 40 N
(D) 50 N
@ans B
@sol $T = \dfrac{2m_1m_2g}{m_1+m_2} = \dfrac{2(3)(5)(10)}{8} = 37.5$ N.
@short $T$ lies between the two weights (30 N and 50 N). It's their harmonic mean.
@trap Taking $T$ equal to the lighter weight (30 N).
@@END

@@Q P03-02 | E | 0.75 | Apparent weight | Speed
A 60 kg person stands on a scale in a lift that accelerates **downward** at $2\ \text{m s}^{-2}$ ($g = 10$). The scale reads:
(A) 720 N
(B) 600 N
(C) 480 N
(D) 120 N
@ans C
@sol $N = m(g - a) = 60 \times 8 = 480$ N.
@short Accelerating down means you feel lighter.
@trap Adding $a$ gives 720 N.
@@END

@@Q P03-03 | M | 1.5 | Rough incline acceleration | Concept
A block slides down a $30^\circ$ incline with $\mu_k = \dfrac{1}{2\sqrt3}$ ($g = 10\ \text{m s}^{-2}$). Its acceleration is:
(A) $5\ \text{m s}^{-2}$
(B) $2.5\ \text{m s}^{-2}$
(C) $7.5\ \text{m s}^{-2}$
(D) $1.25\ \text{m s}^{-2}$
@ans B
@sol $a = g(\sin\theta - \mu_k\cos\theta) = 10\left(\tfrac12 - \tfrac{1}{2\sqrt3}\cdot\tfrac{\sqrt3}{2}\right) = 10(0.5 - 0.25) = 2.5\ \text{m s}^{-2}$.
@short Friction removes $\mu\cot\theta$ of the smooth-incline value: $\mu\cot30^\circ = 0.5$, so half of $g\sin\theta = 5$.
@trap Using $\sin\theta$ in the friction term.
@@END

@@Q P03-04 | E | 1 | Banking speed | NV
A road of radius 50 m is banked at an angle $\theta$ with $\tan\theta = 0.2$. Find the speed (in $\text{m s}^{-1}$) at which a car needs no friction ($g = 10\ \text{m s}^{-2}$).
@ans 10
@sol $v = \sqrt{rg\tan\theta} = \sqrt{50 \times 10 \times 0.2} = \sqrt{100} = 10\ \text{m s}^{-1}$.
@short Design speed of a banked road: $v^2 = rg\tan\theta$.
@trap Using $\sin\theta$ instead of $\tan\theta$.
@@END

@@Q P03-05 | M | 2 | Two-block common motion | NV
A 2 kg block rests on a 4 kg block that lies on a frictionless floor. The coefficient of static friction between the blocks is 0.3. Find the maximum horizontal force (in N) that can be applied to the **lower** block so that the blocks move together ($g = 10\ \text{m s}^{-2}$).
@ans 18
@sol The upper block is accelerated only by friction, so $a_{max} = \mu_sg = 3\ \text{m s}^{-2}$. For common motion $F_{max} = (2 + 4)(3) = 18$ N.
@short $F_{max} = \mu_s g\,(m + M)$ when pushing the lower block.
@trap Using the lower block's mass alone (12 N), or $\mu$ times the total weight used differently.
@@END

@@Q P03-06 | E | 1 | Impulse on rebound | Basic
A 0.2 kg ball hits a wall perpendicularly at $10\ \text{m s}^{-1}$ and rebounds at $8\ \text{m s}^{-1}$. The magnitude of the impulse on the ball is:
(A) 0.4 N s
(B) 2.0 N s
(C) 3.6 N s
(D) 1.8 N s
@ans C
@sol $|\Delta p| = m(v_1 + v_2) = 0.2 \times 18 = 3.6$ N s (the velocity reverses).
@short Rebound: add the speeds.
@trap Subtracting the speeds gives 0.4 N s.
@@END

@@Q P03-07 | M | 1 | Pendulum in accelerating car | Concept
A small bob hangs from the roof of a car accelerating horizontally at $g/\sqrt3$. In equilibrium relative to the car, the string makes an angle with the vertical of:
(A) $30^\circ$, towards the back of the car
(B) $30^\circ$, towards the front of the car
(C) $60^\circ$, towards the back of the car
(D) $45^\circ$, towards the back of the car
@ans A
@sol In the car's frame, a pseudo force $ma$ acts backward. $\tan\theta = a/g = 1/\sqrt3 \Rightarrow \theta = 30^\circ$, with the bob hanging towards the **back**.
@short The bob lags behind the acceleration.
@trap Choosing "front".
@@END

@@Q P03-08 | M | 2 | Equilibrium with two strings | JEE
A 10 kg mass hangs from two strings making angles of $30^\circ$ and $60^\circ$ with the horizontal ceiling ($g = 10\ \text{m s}^{-2}$). The tension in the string at $60^\circ$ to the horizontal is:
(A) 50 N
(B) $50\sqrt3$ N
(C) 100 N
(D) $100/\sqrt3$ N
@ans B
@sol Horizontal: $T_1\cos30^\circ = T_2\cos60^\circ \Rightarrow T_2 = \sqrt3\,T_1$. Vertical: $T_1\sin30^\circ + T_2\sin60^\circ = 100 \Rightarrow \tfrac{T_1}{2} + \tfrac{3T_1}{2} = 100 \Rightarrow T_1 = 50$ N, $T_2 = 50\sqrt3$ N.
@short The strings are perpendicular to each other ($30^\circ + 60^\circ = 90^\circ$), so $T_2 = W\cos30^\circ$ and $T_1 = W\sin30^\circ$.
@trap Swapping which string carries more tension. The steeper string carries more.
@@END

@@Q P03-09 | E | 0.75 | Recoil of a gun | Speed
A 5 kg gun fires a 50 g bullet at $400\ \text{m s}^{-1}$. The recoil speed of the gun is:
(A) $0.4\ \text{m s}^{-1}$
(B) $4\ \text{m s}^{-1}$
(C) $40\ \text{m s}^{-1}$
(D) $2\ \text{m s}^{-1}$
@ans B
@sol $V = \dfrac{mv}{M} = \dfrac{0.05 \times 400}{5} = 4\ \text{m s}^{-1}$.
@short Momentum conservation from rest.
@trap Using 50 kg for 50 g.
@@END

@@SET P03 · Chapter Test

@@Q P03-T1 | M | 1 | Static friction below the limit | Tricky
A 5 kg block rests on a horizontal floor with $\mu_s = 0.5$ ($g = 10$). A horizontal force of 20 N is applied. The friction force on the block is:
(A) 25 N
(B) 20 N
(C) 5 N
(D) 0 N
@ans B
@sol Limiting friction $= \mu_sN = 25$ N > 20 N, so the block doesn't move. Static friction balances the applied force: 20 N.
@short Friction = applied force whenever there is no slipping.
@trap Answering $\mu_sN$ (25 N).
@@END

@@Q P03-T2 | E | 0.5 | Angle of repose | Speed
If $\mu_s = 1/\sqrt3$ between a block and an incline, the angle of repose is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $15^\circ$
@ans A
@sol $\tan\theta_r = \mu_s = 1/\sqrt3 \Rightarrow \theta_r = 30^\circ$.
@short Angle of repose = angle of friction.
@trap None.
@@END

@@Q P03-T3 | E | 1 | Level-road maximum speed | Basic
The maximum safe speed on a level circular road of radius 40 m with $\mu = 0.4$ ($g = 10$) is:
(A) $4\sqrt{10}\ \text{m s}^{-1}$
(B) $16\ \text{m s}^{-1}$
(C) $8\ \text{m s}^{-1}$
(D) $40\ \text{m s}^{-1}$
@ans A
@sol $v = \sqrt{\mu rg} = \sqrt{0.4\times40\times10} = \sqrt{160} = 4\sqrt{10} \approx 12.6\ \text{m s}^{-1}$.
@short $\sqrt{160}$ lies between 12 and 13.
@trap Forgetting the square root.
@@END

@@Q P03-T4 | M | 1.5 | Impulse of variable force | NV
A force $F = 6t$ N acts on a 2 kg body initially at rest. Find its speed (in $\text{m s}^{-1}$) at $t = 2$ s.
@ans 6
@sol $J = \int_0^2 6t\,dt = 3t^2\big|_0^2 = 12$ N s. $v = J/m = 6\ \text{m s}^{-1}$.
@short Impulse = area under the $F$–$t$ graph (a triangle: $\tfrac12 \times 2 \times 12$).
@trap Using $F$ at $t = 2$ with $v = at$ (constant acceleration assumed): 12 m s⁻¹.
@@END

@@Q P03-T5 | E | 1 | Table–pulley system | Basic
A 2 kg block on a smooth table is connected by a string over a pulley to a hanging 3 kg block ($g = 10$). The tension in the string is:
(A) 12 N
(B) 20 N
(C) 30 N
(D) 18 N
@ans A
@sol $a = \dfrac{m_2g}{m_1+m_2} = \dfrac{30}{5} = 6\ \text{m s}^{-2}$. $T = m_1a = 12$ N.
@short $T = \dfrac{m_1m_2g}{m_1+m_2} = \dfrac{60}{5}$.
@trap Taking $T$ = the hanging weight (30 N).
@@END

## Answers & Solutions {#p03-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Laws of Motion
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
