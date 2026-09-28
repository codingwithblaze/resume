# Work, Energy & Power {#p04}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | High
NCERT | Class 11 · Ch 5
Study time | ~8 hours
:::

## Concept summary

- **Work–energy theorem:** $W_{net} = \Delta K$. This is the single most powerful problem-solving tool in mechanics. It skips accelerations and time entirely.
- **Conservative forces** (gravity, spring, electrostatic) store potential energy: $F = -\dfrac{dU}{dx}$. If only conservative forces do work, $K + U$ is constant.
- **Power** is the rate of doing work: $P = \vec F\cdot\vec v$.
- **Collisions:** momentum is always conserved (no external impulse). Kinetic energy is conserved only in elastic collisions.

## Formulas

:::formula Work & energy
$$W = \vec F\cdot\vec s = Fs\cos\theta \qquad W = \int\vec F\cdot d\vec r \ (\text{area under } F\text{–}x) \qquad K = \tfrac12mv^2 = \frac{p^2}{2m}$$
$$U_{gravity} = mgh \qquad U_{spring} = \tfrac12kx^2 \qquad W_{spring} = \tfrac12k(x_1^2 - x_2^2)$$
$$W_{all\ forces} = \Delta K \qquad W_{non\text{-}conservative} = \Delta(K + U) \qquad P = \frac{dW}{dt} = \vec F\cdot\vec v$$
Units: 1 kWh $= 3.6\times10^6$ J; 1 hp $= 746$ W; 1 eV $= 1.6\times10^{-19}$ J.
:::

:::formula Potential energy curves
$F = -dU/dx$. Equilibrium where $dU/dx = 0$: **stable** if $d^2U/dx^2 > 0$ (minimum of $U$), **unstable** if $< 0$ (maximum), **neutral** if $U$ is flat. A particle with total energy $E$ is confined to where $U(x) \le E$ (turning points at $U = E$).
:::

:::formula Vertical circle (string / light rod, radius $R$)
| Case | Minimum speed at the lowest point | Minimum speed at the top |
|---|---|---|
| String (or inside a track) | $\sqrt{5gR}$ | $\sqrt{gR}$ |
| Light rod (or tube) | $\sqrt{4gR}$ | 0 |

$T_{bottom} - T_{top} = 6mg$ (string, full circle). If $\sqrt{2gR} < u < \sqrt{5gR}$ at the bottom, the string goes slack somewhere above the horizontal diameter. If $u \le \sqrt{2gR}$, the bob only oscillates below the horizontal diameter.
:::

:::formula Collisions
**Coefficient of restitution:** $e = \dfrac{\text{velocity of separation}}{\text{velocity of approach}}$ (along the line of impact). Elastic: $e = 1$. Perfectly inelastic: $e = 0$.
**1D elastic, $m_2$ initially at rest:**
$$v_1 = \frac{m_1 - m_2}{m_1 + m_2}u_1 \qquad v_2 = \frac{2m_1}{m_1 + m_2}u_1$$
- Equal masses exchange velocities. A heavy body hitting a light one at rest: the light one leaves at about $2u_1$.
- **KE lost in any 1D collision:** $\Delta K = \dfrac12\dfrac{m_1m_2}{m_1+m_2}(u_1 - u_2)^2(1 - e^2)$.
- **Perfectly inelastic, $m_2$ at rest:** fraction of KE lost $= \dfrac{m_2}{m_1 + m_2}$.
- **Bouncing ball:** $h_n = e^{2n}h_0$, $e = \sqrt{h_1/h_0}$.
- **Oblique elastic collision of equal masses (one at rest):** they move off at $90^\circ$ to each other.
:::

@@GRAPH pe-curve

## Standard models & assumptions

- Springs are massless and obey Hooke's law. "Smooth" surfaces do no work (the normal force ⟂ displacement).
- The normal force and tension in a vertical circle do no work. Only gravity changes the speed.
- In collisions, impulsive forces dominate: ignore gravity and friction *during* the brief impact.

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Work by a variable force** $F(x)$ or from an $F$–$x$ graph (area).
2. **Spring–block** energy: maximum compression, speed at a given compression.
3. **Vertical circle:** minimum speed, tension at a point, where the string slackens.
4. **Collisions:** final velocities, KE loss, coefficient of restitution from bounce heights.
5. **Power:** vehicle on an incline at constant speed; pumping water; $P = Fv$ with variable force.
6. **$U(x)$ → force and equilibrium type.**
7. **Kinetic energy–momentum relation:** percentage changes, $p = \sqrt{2mK}$.
:::

## Shortcuts

:::shortcut Energy method first
If the question asks for a **speed, height or compression** (not a time), use energy conservation or the work–energy theorem straight away.
**Time saved:** 1–2 minutes compared with a force/kinematics approach. **When NOT to use:** when the question asks for time or acceleration, or when the path matters for a non-conservative force whose work you can't easily compute.
:::

:::shortcut Percentage changes
$K \propto p^2$. If $p$ rises by $x\%$ (small), $K$ rises by about $2x\%$. For large changes use exact ratios: $K \times 4 \Rightarrow p \times 2$ (a 300% rise in $K$ is a 100% rise in $p$).
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Work from $F(x)$ or graph area | E | 1 min |
| Spring–block energy | E | 1 min |
| Power on an incline | E–M | 1.5 min |
| 1D collision velocities / KE loss | M | 2 min |
| Vertical circle tension/slack point | M–H | 2.5 min |
| 2D collision, or collision + spring combined | H | 3–4 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Taking work by friction as $\mu mg\times d$ on an incline. Use $\mu mg\cos\theta\times d$.
- Sign errors in $W_{spring}$ when the spring is stretched from $x_1$ to $x_2$.
- Conserving KE in an inelastic collision.
- For a rod in a vertical circle, using the string condition $\sqrt{5gR}$.
- Forgetting that $P = Fv$ uses the **force exerted by the engine**, not the net force.
:::

## Practice questions

@@SET P04 · Practice

@@Q P04-01 | E | 1 | Work by variable force | NV
A force $F = 3x^2$ N acts along the $x$-axis. Find the work done (in J) as a body moves from $x = 0$ to $x = 2$ m.
@ans 8
@sol $W = \int_0^2 3x^2\,dx = x^3\big|_0^2 = 8$ J.
@short Integrate: the antiderivative of $3x^2$ is $x^3$.
@trap Using $F(2)\times2 = 24$ J.
@@END

@@Q P04-02 | E | 1 | Spring maximum compression | Basic
A 2 kg block moving at $4\ \text{m s}^{-1}$ on a smooth floor hits a spring of constant $200\ \text{N m}^{-1}$. The maximum compression is:
(A) 0.2 m
(B) 0.4 m
(C) 0.8 m
(D) 0.04 m
@ans B
@sol $\tfrac12mv^2 = \tfrac12kx^2 \Rightarrow x = v\sqrt{m/k} = 4\sqrt{0.01} = 0.4$ m.
@short $x = v\sqrt{m/k}$.
@trap Forgetting the square root gives 0.04.
@@END

@@Q P04-03 | M | 1.5 | Power on an incline | JEE
A 1000 kg car climbs an incline with $\sin\theta = 1/20$ at a constant $10\ \text{m s}^{-1}$ against a resistive force of 500 N ($g = 10$). The engine's power is:
(A) 5 kW
(B) 10 kW
(C) 15 kW
(D) 20 kW
@ans B
@sol At constant speed, the engine force $= mg\sin\theta + f = 500 + 500 = 1000$ N. $P = Fv = 10$ kW.
@short Constant speed means driving force = sum of resisting forces.
@trap Omitting the gravity component (5 kW).
@@END

@@Q P04-04 | M | 1 | Vertical circle, minimum speed | Basic
A bob on a light string of length 0.9 m is to complete a vertical circle ($g = 10$). The minimum speed needed at the lowest point is:
(A) $3\ \text{m s}^{-1}$
(B) $3\sqrt5\ \text{m s}^{-1}$
(C) $3\sqrt2\ \text{m s}^{-1}$
(D) $6\ \text{m s}^{-1}$
@ans B
@sol $u_{min} = \sqrt{5gR} = \sqrt{45} = 3\sqrt5 \approx 6.7\ \text{m s}^{-1}$.
@short String: $\sqrt{5gR}$ at the bottom. Rod: $\sqrt{4gR}$.
@trap Using the rod condition gives 6.
@@END

@@Q P04-05 | E | 1 | 1D elastic collision | Basic
A 2 kg ball moving at $6\ \text{m s}^{-1}$ collides elastically head-on with a stationary 4 kg ball. The velocity of the 4 kg ball afterwards is:
(A) $2\ \text{m s}^{-1}$
(B) $3\ \text{m s}^{-1}$
(C) $4\ \text{m s}^{-1}$
(D) $6\ \text{m s}^{-1}$
@ans C
@sol $v_2 = \dfrac{2m_1}{m_1+m_2}u_1 = \dfrac{4}{6}\times6 = 4\ \text{m s}^{-1}$. (The 2 kg ball rebounds at $2\ \text{m s}^{-1}$.)
@short Check: relative speed of separation = relative speed of approach: $4 - (-2) = 6$.
@trap Assuming the balls exchange velocities (true only for equal masses).
@@END

@@Q P04-06 | M | 1.5 | KE loss in perfectly inelastic collision | NV
A 1 kg block moving at $10\ \text{m s}^{-1}$ collides with and sticks to a stationary 4 kg block. Find the percentage of the initial kinetic energy lost.
@ans 80
@sol $v = \dfrac{1\times10}{5} = 2\ \text{m s}^{-1}$. $K_i = 50$ J, $K_f = \tfrac12(5)(4) = 10$ J. Loss $= 40/50 = 80\%$.
@short Fraction lost $= \dfrac{m_2}{m_1+m_2} = \dfrac45$.
@trap Reporting the percentage retained (20).
@@END

@@Q P04-07 | E | 1 | Equilibrium from U(x) | Concept
A particle has potential energy $U(x) = x^2 - 4x$ (SI units). Its equilibrium position and type are:
(A) $x = 2$ m, stable
(B) $x = 2$ m, unstable
(C) $x = 4$ m, stable
(D) $x = 0$, neutral
@ans A
@sol $dU/dx = 2x - 4 = 0 \Rightarrow x = 2$. $d^2U/dx^2 = 2 > 0$, a minimum, so stable.
@short U is an upward parabola, so its vertex is a stable equilibrium.
@trap Taking the root of $U = 0$ ($x = 4$) as the equilibrium.
@@END

@@Q P04-08 | E | 1 | Restitution from bounce height | Basic
A ball dropped from 10 m rebounds to 6.4 m. The coefficient of restitution is:
(A) 0.64
(B) 0.8
(C) 0.36
(D) 0.6
@ans B
@sol $e = \sqrt{h_1/h_0} = \sqrt{0.64} = 0.8$.
@short Speed $\propto \sqrt h$.
@trap Using $h_1/h_0$ directly (0.64).
@@END

@@Q P04-09 | E | 1 | Stopping distance with friction | Basic
A 1 kg block slides on a floor with $\mu_k = 0.2$ from an initial speed of $6\ \text{m s}^{-1}$ ($g = 10$). It stops after:
(A) 3 m
(B) 6 m
(C) 9 m
(D) 18 m
@ans C
@sol $\mu mg\,d = \tfrac12mv^2 \Rightarrow d = \dfrac{v^2}{2\mu g} = \dfrac{36}{4} = 9$ m.
@short Mass cancels.
@trap Forgetting the 2 gives 18 m.
@@END

@@SET P04 · Chapter Test

@@Q P04-T1 | E | 0.5 | Work by centripetal force | Speed
The work done by Earth's gravity on a satellite in a circular orbit during one full revolution is:
(A) positive
(B) negative
(C) zero
(D) $2\pi r\times mg$
@ans C
@sol Gravity is always perpendicular to the velocity in a circular orbit, so it does no work at any instant.
@short Force ⟂ velocity → no work.
@trap Multiplying force by the circumference.
@@END

@@Q P04-T2 | E | 1 | KE–momentum relation | Basic
If the kinetic energy of a body increases by 300%, its momentum increases by:
(A) 100%
(B) 200%
(C) 300%
(D) 50%
@ans A
@sol $K' = 4K \Rightarrow p' = \sqrt{2mK'} = 2p$, an increase of 100%.
@short $p \propto \sqrt K$.
@trap Reading "+300%" as ×3 instead of ×4.
@@END

@@Q P04-T3 | M | 1 | Power of a machine gun | Calc
A machine gun fires 10 bullets per second, each of mass 50 g, at $1000\ \text{m s}^{-1}$. The power delivered to the bullets is:
(A) 25 kW
(B) 250 kW
(C) 500 kW
(D) 2.5 kW
@ans B
@sol KE per bullet $= \tfrac12(0.05)(10^6) = 2.5\times10^4$ J. Power $= 10\times2.5\times10^4 = 2.5\times10^5$ W $= 250$ kW.
@short $P = \tfrac12 n m v^2$.
@trap Unit slip: 50 g as 0.5 kg.
@@END

@@Q P04-T4 | E | 0.75 | Force from potential energy | NV
The potential energy of a particle is $U = 5x^3$ J ($x$ in m). Find the magnitude of the force (in N) on it at $x = 1$ m.
@ans 15
@sol $F = -dU/dx = -15x^2$; at $x = 1$, $|F| = 15$ N.
@short Force = −slope of $U$.
@trap Reporting $U(1) = 5$.
@@END

@@Q P04-T5 | E | 0.5 | Net work at constant speed | Tricky
A 2 kg body is lifted 5 m vertically at **constant speed** ($g = 10$). The net work done on the body is:
(A) 100 J
(B) −100 J
(C) 0
(D) 200 J
@ans C
@sol $W_{net} = \Delta K = 0$ (constant speed). The applied force does $+100$ J, and gravity does $-100$ J.
@short Constant speed means zero net work.
@trap Answering the work done by the lifting force alone.
@@END

## Answers & Solutions {#p04-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Work, Energy & Power
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
