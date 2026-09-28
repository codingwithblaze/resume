# Rotational Motion & Centre of Mass {#p05}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium–Hard
Priority | Must-do
NCERT | Class 11 · Ch 6
Study time | ~16 hours
:::

## Concept summary

- The **centre of mass (COM)** moves as if all the mass and all the external forces were concentrated there: $M\vec a_{cm} = \vec F_{ext}$.
- **Rotation** has an exact analogue for every linear quantity: $\theta \leftrightarrow x$, $\omega \leftrightarrow v$, $\alpha \leftrightarrow a$, $I \leftrightarrow m$, $\tau \leftrightarrow F$, $L \leftrightarrow p$.
- **Moment of inertia** depends on the mass *and* how far it lies from the axis. The parallel and perpendicular axis theorems give $I$ about new axes.
- **Rolling without slipping:** $v_{cm} = \omega R$. Rolling KE splits into translational and rotational parts in a fixed ratio.
- **Angular momentum is conserved** when there is no external torque: $I_1\omega_1 = I_2\omega_2$.

## Formulas

:::formula Centre of mass
$$\vec r_{cm} = \frac{\sum m_i\vec r_i}{\sum m_i} \qquad x_{cm} = \frac{\int x\,dm}{\int dm} \qquad \vec v_{cm} = \frac{\sum m_i\vec v_i}{M}$$
| Body | COM location |
|---|---|
| Semicircular **ring** (radius $R$) | $\dfrac{2R}{\pi}$ from the centre |
| Semicircular **disc** | $\dfrac{4R}{3\pi}$ from the centre |
| Solid hemisphere | $\dfrac{3R}{8}$ from the centre of the flat face |
| Hollow hemisphere | $\dfrac{R}{2}$ from the centre |
| Solid cone (height $h$) | $\dfrac{h}{4}$ from the base |
| Triangle (lamina) | centroid |

**Removed-part trick:** $x_{cm} = \dfrac{m_1x_1 - m_2x_2}{m_1 - m_2}$ (treat the hole as negative mass).
:::

:::formula Rotational kinematics & dynamics
$$\omega = \omega_0 + \alpha t \quad \theta = \omega_0t + \tfrac12\alpha t^2 \quad \omega^2 = \omega_0^2 + 2\alpha\theta$$
$$\vec\tau = \vec r\times\vec F \quad \tau = I\alpha \quad \vec L = \vec r\times\vec p = I\vec\omega \quad \vec\tau_{ext} = \frac{d\vec L}{dt}$$
$$K_{rot} = \tfrac12I\omega^2 = \frac{L^2}{2I} \quad W = \int\tau\,d\theta \quad P = \tau\omega \quad \text{angular impulse} = \int\tau\,dt = \Delta L$$
:::

:::formula Moments of inertia
| Body (mass $M$) | Axis | $I$ |
|---|---|---|
| Thin ring, radius $R$ | central, ⟂ plane | $MR^2$ |
| Thin ring | diameter | $\tfrac12MR^2$ |
| Disc / solid cylinder | central axis | $\tfrac12MR^2$ |
| Disc | diameter | $\tfrac14MR^2$ |
| Hollow cylinder (thin) | central axis | $MR^2$ |
| Solid sphere | diameter | $\tfrac25MR^2$ |
| Hollow sphere (thin shell) | diameter | $\tfrac23MR^2$ |
| Thin rod, length $L$ | ⟂ through centre | $\tfrac1{12}ML^2$ |
| Thin rod | ⟂ through one end | $\tfrac13ML^2$ |
| Rectangular plate $a\times b$ | ⟂ plane through centre | $\tfrac1{12}M(a^2+b^2)$ |
| Solid cylinder (length $l$) | ⟂ axis through centre | $M\left(\dfrac{R^2}{4} + \dfrac{l^2}{12}\right)$ |

**Parallel axis:** $I = I_{cm} + Md^2$ (any body). **Perpendicular axis:** $I_z = I_x + I_y$ (planar bodies only). **Radius of gyration:** $k = \sqrt{I/M}$.
:::

:::formula Rolling without slipping
$$v_{cm} = \omega R \qquad K = \tfrac12mv^2\left(1 + \frac{k^2}{R^2}\right) \qquad a_{incline} = \frac{g\sin\theta}{1 + k^2/R^2} \qquad \mu_{min} = \frac{\tan\theta}{1 + R^2/k^2}$$
| Body | $k^2/R^2$ | $K_{rot}/K_{total}$ | $a$ on incline |
|---|---|---|---|
| Ring / hollow cylinder | 1 | 1/2 | $\tfrac12g\sin\theta$ |
| Disc / solid cylinder | 1/2 | 1/3 | $\tfrac23g\sin\theta$ |
| Hollow sphere | 2/3 | 2/5 | $\tfrac35g\sin\theta$ |
| Solid sphere | 2/5 | 2/7 | $\tfrac57g\sin\theta$ |

**Race down an incline** (smallest $k^2/R^2$ wins): solid sphere > disc > hollow sphere > ring. The race result is independent of mass and radius.
**Sliding → rolling on a rough floor** (initial speed $v_0$, $\omega_0 = 0$): the final rolling speed is $\dfrac{v_0}{1 + k^2/R^2}$. For a solid sphere, $\tfrac57v_0$.
:::

:::formula Equilibrium of a rigid body
$\sum\vec F = 0$ **and** $\sum\vec\tau = 0$ about *any* point. Take torques about the point where the most unknown forces act.
**Ladder** (uniform, smooth wall, rough floor, at angle $\theta$ with the floor): on the verge of slipping, $\mu = \dfrac{1}{2\tan\theta}$.
:::

## Linear ↔ rotational comparison

| Linear | Rotational |
|---|---|
| $x$, $v$, $a$ | $\theta$, $\omega$, $\alpha$ |
| $m$ | $I$ |
| $F = ma$ | $\tau = I\alpha$ |
| $p = mv$ | $L = I\omega$ |
| $K = \tfrac12mv^2$ | $K = \tfrac12I\omega^2$ |
| $P = Fv$ | $P = \tau\omega$ |

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **MI about a shifted axis:** parallel/perpendicular axis on a disc, ring, rod or plate; MI of composite bodies (rod + spheres, square of rods).
2. **Rolling on an incline:** acceleration, speed at the bottom, which body reaches first, minimum friction.
3. **Angular momentum conservation:** a person walking on a turntable, a skater, two discs coupled (KE lost).
4. **COM of composite or cut-out bodies**, and COM motion after an explosion.
5. **Torque and angular momentum as cross products** in vector form.
6. **Rolling KE ratios**, and the fraction of KE that is rotational.
:::

## Shortcuts

:::shortcut The $k^2/R^2$ key
Memorise one number per body: ring 1, disc 1/2, hollow sphere 2/3, solid sphere 2/5. Every rolling formula in the table above is generated from it.
**Time saved:** 1–2 min per rolling question. **Common mistake:** using $I/(MR^2)$ about the wrong axis, such as a disc about its diameter (1/4) when it rolls about its central axis (1/2).
:::

:::shortcut Coupled rotating bodies
Two coaxial bodies stick together: $\omega_f = \dfrac{I_1\omega_1 + I_2\omega_2}{I_1+I_2}$ and $\Delta K = \dfrac{I_1I_2(\omega_1-\omega_2)^2}{2(I_1+I_2)}$. This is the rotational version of a perfectly inelastic collision.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| MI from the table + one theorem | E | 1 min |
| Rolling acceleration / KE ratios | E–M | 1.5 min |
| Angular momentum conservation | M | 2 min |
| COM of a cut-out body | M | 2 min |
| Torque/L as a cross product | E | 1 min |
| Rolling + slipping, or impulse on a rod | H | 3–4 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Applying the perpendicular axis theorem to a 3D body (a sphere or cylinder). It works for **planar** bodies only.
- Using the parallel axis theorem between two axes, neither of which passes through the COM. Always go through $I_{cm}$.
- Assuming friction does work in pure rolling. Static friction at the contact point does **no** work.
- Using $v = \omega R$ when the body is still slipping.
- Conserving KE when two rotating bodies couple. Only angular momentum is conserved.
:::

## Practice questions

@@SET P05 · Practice

@@Q P05-01 | M | 1.5 | Parallel + perpendicular axis | Concept
The moment of inertia of a uniform disc (mass $M$, radius $R$) about a **tangent lying in its plane** is:
(A) $\tfrac54MR^2$
(B) $\tfrac32MR^2$
(C) $\tfrac12MR^2$
(D) $\tfrac34MR^2$
@ans A
@sol About a diameter: $\tfrac14MR^2$ (perpendicular axis theorem: $I_x + I_y = \tfrac12MR^2$). A tangent in the plane is parallel to a diameter at distance $R$: $\tfrac14MR^2 + MR^2 = \tfrac54MR^2$.
@short In-plane tangent: $\tfrac54$. Tangent ⟂ plane: $\tfrac32$.
@trap Starting from the central-axis value gives $\tfrac32MR^2$ (the tangent perpendicular to the plane).
@@END

@@Q P05-02 | E | 1 | Rolling acceleration | Basic
A solid cylinder rolls without slipping down a $30^\circ$ incline ($g = 10$). Its acceleration is:
(A) $5\ \text{m s}^{-2}$
(B) $10/3\ \text{m s}^{-2}$
(C) $2.5\ \text{m s}^{-2}$
(D) $25/7\ \text{m s}^{-2}$
@ans B
@sol $a = \dfrac{g\sin\theta}{1 + k^2/R^2} = \dfrac{5}{3/2} = \dfrac{10}{3}\ \text{m s}^{-2}$.
@short Disc/cylinder: $\tfrac23g\sin\theta$.
@trap Using the solid sphere's $k^2/R^2$ gives 25/7.
@@END

@@Q P05-03 | E | 1 | Angular momentum conservation | Concept
A skater spins with MI $4\ \text{kg m}^2$ at 2 rev/s. She pulls in her arms, reducing her MI to $2\ \text{kg m}^2$. The ratio (new KE)/(old KE) is:
(A) 1/2
(B) 1
(C) 2
(D) 4
@ans C
@sol $L$ is conserved: $\omega_2 = 4$ rev/s. $K = L^2/2I$ with $L$ fixed, so $K \propto 1/I$ and the ratio is 2. The extra energy comes from the work she does pulling her arms in.
@short Constant $L$: $K \propto 1/I$.
@trap Assuming KE is conserved (ratio 1).
@@END

@@Q P05-04 | E | 0.75 | COM of a semicircular wire | Speed
The centre of mass of a thin uniform wire bent into a semicircle of radius $R$ is at a distance from the centre of:
(A) $2R/\pi$
(B) $4R/3\pi$
(C) $R/2$
(D) $\pi R/4$
@ans A
@sol For a semicircular ring, $y_{cm} = \dfrac{\int R\sin\theta\,\lambda R\,d\theta}{\lambda\pi R} = \dfrac{2R}{\pi}$.
@short Ring: $2R/\pi$. Disc (lamina): $4R/3\pi$.
@trap Mixing up the wire and lamina results.
@@END

@@Q P05-05 | E | 1 | Torque as a cross product | NV
A force $\vec F = (2\hat i + 3\hat j)$ N acts at the point $\vec r = (\hat i - \hat j)$ m. Find the magnitude of the torque (in N m) about the origin.
@ans 5
@sol $\vec\tau = \vec r\times\vec F = (1)(3) - (-1)(2) = 5$ along $\hat k$. Magnitude 5 N m.
@short In 2D, $\tau_z = xF_y - yF_x$.
@trap Computing $\vec F\times\vec r$ changes the sign only, not the magnitude. The real trap is arithmetic with the negative $y$.
@@END

@@Q P05-06 | E | 0.75 | Rolling race | Speed
A solid sphere, a disc and a ring (all of different masses and radii) are released together from rest at the top of the same incline and roll without slipping. The order in which they reach the bottom is:
(A) ring, disc, sphere
(B) sphere, disc, ring
(C) disc, sphere, ring
(D) all together
@ans B
@sol $a \propto 1/(1 + k^2/R^2)$: sphere (2/5) > disc (1/2) > ring (1). Mass and radius don't matter.
@short Smaller $k^2/R^2$ reaches first.
@trap Thinking the heavier body wins.
@@END

@@Q P05-07 | E | 1 | Rolling kinetic energy | NV
A 2 kg disc rolls without slipping at $2\ \text{m s}^{-1}$. Find its total kinetic energy (in J).
@ans 6
@sol $K = \tfrac12mv^2(1 + \tfrac12) = \tfrac12(2)(4)(1.5) = 6$ J.
@short Disc: $K = \tfrac34mv^2$.
@trap Counting only the translational KE (4 J).
@@END

@@Q P05-08 | H | 2.5 | Ladder friction | JEE
A uniform ladder rests against a smooth vertical wall, making $60^\circ$ with a rough horizontal floor. The minimum coefficient of friction at the floor for equilibrium is:
(A) $\dfrac{1}{2\sqrt3}$
(B) $\dfrac{1}{\sqrt3}$
(C) $\dfrac{\sqrt3}{2}$
(D) $\dfrac{1}{2}$
@ans A
@sol Forces: weight $W$ at the middle, floor normal $N_1 = W$, friction $f$, wall normal $N_2 = f$. Torques about the foot: $N_2L\sin60^\circ = W\tfrac L2\cos60^\circ \Rightarrow N_2 = \dfrac{W}{2\tan60^\circ}$. Then $\mu \ge f/N_1 = \dfrac{1}{2\tan60^\circ} = \dfrac{1}{2\sqrt3}$.
@short $\mu_{min} = \dfrac{1}{2\tan\theta}$ ($\theta$ measured from the floor).
@trap Measuring $\theta$ from the wall, which gives $\dfrac{\tan\theta}{2}$ with the wrong angle.
@@END

@@Q P05-09 | M | 1.5 | Sliding to rolling | Concept
A solid sphere is set sliding (not rotating) at speed $v_0$ on a rough horizontal floor. When it starts rolling without slipping, its speed is:
(A) $v_0$
(B) $\tfrac57v_0$
(C) $\tfrac27v_0$
(D) $\tfrac23v_0$
@ans B
@sol Angular momentum about the contact point is conserved (friction acts through that point): $mv_0R = mvR + \tfrac25mR^2(v/R) \Rightarrow v = \tfrac57v_0$.
@short $v = \dfrac{v_0}{1 + k^2/R^2}$.
@trap Conserving kinetic energy, which friction dissipates during slipping.
@@END

@@Q P05-10 | E | 0.75 | Rotational kinematics | Speed
A wheel starts from rest with a constant angular acceleration of $2\ \text{rad s}^{-2}$. The angle it turns through in the first 5 s is:
(A) 10 rad
(B) 25 rad
(C) 50 rad
(D) 5 rad
@ans B
@sol $\theta = \tfrac12\alpha t^2 = \tfrac12(2)(25) = 25$ rad.
@short Same form as $s = \tfrac12at^2$.
@trap Using $\theta = \alpha t$ (10).
@@END

@@SET P05 · Chapter Test

@@Q P05-T1 | E | 0.5 | Radius of gyration | Speed
The radius of gyration of a solid sphere of radius $R$ about a diameter is:
(A) $\sqrt{2/5}\,R$
(B) $\tfrac25R$
(C) $\sqrt{2/3}\,R$
(D) $R/\sqrt2$
@ans A
@sol $k = \sqrt{I/M} = \sqrt{\tfrac25}R$.
@short $k^2/R^2$ = the fraction in $I = (\cdot)MR^2$.
@trap Forgetting the square root.
@@END

@@Q P05-T2 | E | 0.75 | Perpendicular axis for a ring | Basic
The moment of inertia of a thin ring (mass $M$, radius $R$) about a diameter is:
(A) $MR^2$
(B) $\tfrac12MR^2$
(C) $\tfrac14MR^2$
(D) $2MR^2$
@ans B
@sol $I_z = I_x + I_y = 2I_{dia} = MR^2 \Rightarrow I_{dia} = \tfrac12MR^2$.
@short Diameter MI = half the central-axis MI (for any symmetric planar body).
@trap Using the disc value (1/4).
@@END

@@Q P05-T3 | E | 1 | Torque and angular speed | NV
A constant torque of 10 N m acts on a flywheel of MI $2\ \text{kg m}^2$ that starts from rest. Find its angular speed (in rad/s) after 4 s.
@ans 20
@sol $\alpha = \tau/I = 5\ \text{rad s}^{-2}$; $\omega = \alpha t = 20$ rad/s.
@short Angular impulse $\tau t = I\omega$: $40 = 2\omega$.
@trap None; speed item.
@@END

@@Q P05-T4 | M | 1 | Coupling identical discs | Concept
A disc rotates freely at $\omega_0$. An identical disc, initially at rest, is gently placed on it coaxially, and they rotate together. The final angular speed is:
(A) $\omega_0$
(B) $\omega_0/2$
(C) $\omega_0/\sqrt2$
(D) $2\omega_0$
@ans B
@sol $I\omega_0 = 2I\omega \Rightarrow \omega = \omega_0/2$. (Half of the KE is lost.)
@short Rotational perfectly inelastic collision.
@trap Conserving KE gives $\omega_0/\sqrt2$.
@@END

@@Q P05-T5 | M | 1 | Rolling KE ratio | Concept
A hollow sphere and a solid sphere of equal mass and radius roll without slipping at the same speed. The ratio of their kinetic energies (hollow : solid) is:
(A) 25 : 21
(B) 21 : 25
(C) 5 : 3
(D) 1 : 1
@ans A
@sol $K \propto 1 + k^2/R^2$: $\left(1 + \tfrac23\right) : \left(1 + \tfrac25\right) = \tfrac53 : \tfrac75 = 25 : 21$.
@short Compare the $(1 + k^2/R^2)$ factors.
@trap Inverting the ratio.
@@END

## Answers & Solutions {#p05-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Rotational Motion
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
