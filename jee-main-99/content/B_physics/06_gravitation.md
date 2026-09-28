# Gravitation {#p06}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 11 · Ch 7
Study time | ~7 hours
:::

## Concept summary

- **Newton's law:** every pair of masses attracts with $F = Gm_1m_2/r^2$ along the line joining them. Spherically symmetric bodies act as point masses for external points.
- **$g$** falls with height and with depth. It is maximum at the surface.
- **Potential energy** is negative, $U = -GMm/r$, with zero at infinity. Bound orbits have negative total energy.
- **Satellites:** gravity provides the centripetal force. Everything (speed, period, energy) follows from $\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}$.
- **Kepler's laws** summarise planetary motion. The second law is angular momentum conservation.

## Formulas

:::formula Acceleration due to gravity
$$g = \frac{GM}{R^2} \qquad g_h = \frac{g}{(1 + h/R)^2} \approx g\left(1 - \frac{2h}{R}\right)\ (h \ll R) \qquad g_d = g\left(1 - \frac dR\right)$$
- $g$ is zero at the centre of the Earth.
- For the same small fractional decrease in $g$: $d = 2h$.
- Effect of rotation at latitude $\lambda$: $g' = g - \omega^2R\cos^2\lambda$. $g$ is minimum at the equator.
:::

:::formula Field and potential
| Source | Field $E_g$ | Potential $V$ |
|---|---|---|
| Point mass / outside a sphere ($r \ge R$) | $\dfrac{GM}{r^2}$ | $-\dfrac{GM}{r}$ |
| **Inside a thin shell** ($r < R$) | **0** | $-\dfrac{GM}{R}$ (constant) |
| **Inside a solid sphere** ($r < R$) | $\dfrac{GMr}{R^3}$ | $-\dfrac{GM(3R^2 - r^2)}{2R^3}$ |

At the centre of a solid sphere, $V = -\tfrac32\dfrac{GM}{R}$. $E_g = -dV/dr$.
:::

:::formula Energy, escape and orbits
$$U = -\frac{GMm}{r} \qquad v_{esc} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR} \approx 11.2\ \text{km s}^{-1}$$
$$v_{orb} = \sqrt{\frac{GM}{r}} \qquad T = 2\pi\sqrt{\frac{r^3}{GM}} \qquad \text{near the surface: } v_o = \sqrt{gR} \approx 7.9\ \text{km s}^{-1},\ T \approx 84\ \text{min}$$
$$K = \frac{GMm}{2r} \qquad U = -\frac{GMm}{r} \qquad E = -\frac{GMm}{2r} \qquad K = -E = -\tfrac12U$$
- $v_{esc} = \sqrt2\,v_{orb}$ at the same point. Binding energy $= +\dfrac{GMm}{2r}$.
- Energy to move a satellite from $r_1$ to $r_2$: $\Delta E = \dfrac{GMm}{2}\left(\dfrac1{r_1} - \dfrac1{r_2}\right)$.
- **Geostationary orbit:** $T = 24$ h, equatorial, same sense as Earth's rotation, $r \approx 42\,000$ km from the centre ($h \approx 36\,000$ km).
- Escape speed does **not** depend on the mass of the body or the direction of launch.
:::

:::formula Kepler's laws
1. Orbits are ellipses with the Sun at one focus.
2. The radius vector sweeps equal areas in equal times: $\dfrac{dA}{dt} = \dfrac{L}{2m}$ = constant, so speed is maximum at perihelion. $v_pr_p = v_ar_a$.
3. $T^2 \propto a^3$, where $a$ is the semi-major axis: $T^2 = \dfrac{4\pi^2}{GM}a^3$.
:::

@@GRAPH gravity-g-r

## Standard models & assumptions

- Earth is a uniform sphere, $R = 6400$ km, $g = 9.8$ (or 10) $\text{m s}^{-2}$, $G = 6.67\times10^{-11}\ \text{N m}^2\text{kg}^{-2}$.
- Satellites are in circular orbits unless an ellipse is stated. The satellite's own mass doesn't affect its orbit.

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **$g$ vs height and depth:** ratios, "at what height/depth does $g$ become x%", comparisons.
2. **Satellite energies:** KE/PE/total relations, energy to shift orbits, binding energy.
3. **Escape speed** for planets with changed $M$, $R$ or density; escape vs orbital speed.
4. **Kepler's third law:** period ratios; areal velocity.
5. **Field/potential inside shells and spheres** (graph-based).
6. **Null point** between two masses.
:::

## Shortcuts

:::shortcut Scaling instead of computing
Most gravitation MCQs are ratio questions. Write the dependence and scale it:
$g \propto M/R^2 \propto \rho R$, $v_{esc} \propto \sqrt{M/R} \propto R\sqrt\rho$, $T \propto r^{3/2}$, $v_{orb} \propto r^{-1/2}$.
**Time saved:** 1 minute. **Common mistake:** holding the wrong variable fixed (mass vs density).
:::

:::shortcut Null point between masses $m_1$, $m_2$ a distance $d$ apart
From $m_1$: $x = \dfrac{d\sqrt{m_1}}{\sqrt{m_1}+\sqrt{m_2}}$.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| $g$ at height/depth | E | 1 min |
| Kepler III ratio | E | 45 s |
| Satellite energy relations | E–M | 1 min |
| Escape/orbital speed scaling | E | 1 min |
| Field/potential inside bodies | M | 2 min |
| Elliptical orbits (angular momentum + energy) | M–H | 3 min |

## Common mistakes

:::trap Mistake alerts
- Using $h$ (height above the surface) where $r = R + h$ is needed.
- Applying $g(1 - 2h/R)$ when $h$ is not small compared with $R$.
- Treating PE as positive, or forgetting that total energy is negative.
- Claiming $g$ inside a **shell** is non-zero. The field is zero, but the potential is not.
- Taking $T^2 \propto r^3$ with $r$ measured from the surface.
:::

## Practice questions

@@SET P06 · Practice

@@Q P06-01 | E | 0.75 | g at height R | Speed
The acceleration due to gravity at a height equal to Earth's radius, above the surface, is:
(A) $g/2$
(B) $g/4$
(C) $g/\sqrt2$
(D) $g/8$
@ans B
@sol $g_h = g\left(\dfrac{R}{R+h}\right)^2 = g\left(\tfrac12\right)^2 = g/4$.
@short $r$ doubles, so $g$ falls by a factor of 4.
@trap Using $g(1 - 2h/R)$, which gives $-g$ and is invalid for large $h$.
@@END

@@Q P06-02 | E | 1 | Small-height decrease | Basic
At what height above Earth's surface does $g$ decrease by 1%? ($R = 6400$ km; assume $h \ll R$.)
(A) 64 km
(B) 32 km
(C) 16 km
(D) 128 km
@ans B
@sol $\dfrac{\Delta g}{g} = \dfrac{2h}{R} = 0.01 \Rightarrow h = \dfrac{0.01 \times 6400}{2} = 32$ km.
@short Depth for the same 1% decrease: 64 km, which is $2h$.
@trap Forgetting the 2 gives 64 km.
@@END

@@Q P06-03 | E | 0.75 | Kepler's third law | Speed
A planet's orbital radius is 4 times Earth's. Its orbital period is:
(A) 2 years
(B) 4 years
(C) 8 years
(D) 16 years
@ans C
@sol $T \propto r^{3/2}$: $4^{3/2} = 8$, so 8 years.
@short $\sqrt{4^3} = 8$.
@trap Using $T \propto r^2$ gives 16.
@@END

@@Q P06-04 | E | 0.75 | Satellite energy relations | Basic
A satellite in a circular orbit has kinetic energy $K$. Its total mechanical energy is:
(A) $K$
(B) $-K$
(C) $-2K$
(D) $2K$
@ans B
@sol $E = -\dfrac{GMm}{2r} = -K$ (and $U = -2K$).
@short $K : U : E = 1 : -2 : -1$.
@trap Confusing $U$ with $E$.
@@END

@@Q P06-05 | M | 1 | Extra speed to escape | Concept
A satellite orbits just above Earth's surface ($v_o \approx 7.9\ \text{km s}^{-1}$). The minimum *additional* speed it needs to escape is about:
(A) 11.2 km/s
(B) 3.3 km/s
(C) 7.9 km/s
(D) 1.4 km/s
@ans B
@sol $v_e = \sqrt2\,v_o \approx 11.2$ km/s. Additional $= (\sqrt2 - 1)v_o \approx 0.414 \times 7.9 \approx 3.3$ km/s.
@short $\Delta v = (\sqrt2 - 1)v_o$.
@trap Answering $v_e$ itself.
@@END

@@Q P06-06 | M | 1.5 | Energy to shift orbits | JEE
The energy needed to move a satellite of mass $m$ from a circular orbit of radius $2R$ to one of radius $3R$ ($R$ = Earth's radius) is:
(A) $mgR/12$
(B) $mgR/6$
(C) $mgR/3$
(D) $mgR/2$
@ans A
@sol $\Delta E = \dfrac{GMm}{2}\left(\dfrac1{2R} - \dfrac1{3R}\right) = \dfrac{GMm}{12R} = \dfrac{mgR}{12}$, using $GM = gR^2$.
@short Take the difference of total energies $-GMm/2r$.
@trap Using the difference of potential energies gives $mgR/6$.
@@END

@@Q P06-07 | E | 0.75 | Field inside a shell | Concept
Inside a uniform thin spherical shell of mass $M$ and radius $R$:
(A) field and potential are both zero
(B) the field is zero and the potential is $-GM/R$ everywhere
(C) the field is $GM/R^2$ and the potential is zero
(D) the field increases linearly with $r$
@ans B
@sol By the shell theorem the field inside is zero, so the potential is constant and equal to its surface value $-GM/R$.
@short Zero field ⇒ constant (not zero) potential.
@trap Assuming zero potential.
@@END

@@Q P06-08 | E | 1 | Null point between two masses | NV
Masses of 1 kg and 4 kg are 3 m apart. Find the distance (in m) from the 1 kg mass of the point between them where the net gravitational field is zero.
@ans 1
@sol $\dfrac{G(1)}{x^2} = \dfrac{G(4)}{(3-x)^2} \Rightarrow 3 - x = 2x \Rightarrow x = 1$ m.
@short $x = \dfrac{d\sqrt{m_1}}{\sqrt{m_1}+\sqrt{m_2}} = \dfrac{3}{3}$.
@trap Measuring from the heavier mass (2 m).
@@END

@@Q P06-09 | E | 0.75 | Surface gravity of another planet | Speed
A planet has twice Earth's mass and twice its radius. Its surface gravity is:
(A) $g$
(B) $2g$
(C) $g/2$
(D) $g/4$
@ans C
@sol $g \propto M/R^2 = 2/4 = 1/2$.
@short Ratio scaling.
@trap Using $M/R$ gives $g$.
@@END

@@SET P06 · Chapter Test

@@Q P06-T1 | E | 0.5 | What escape speed depends on | Concept
The escape speed from a planet depends on:
(A) the mass of the object being launched
(B) the angle of launch
(C) the mass and radius of the planet
(D) all of the above
@ans C
@sol $v_e = \sqrt{2GM/R}$ is independent of the object's mass and of the launch direction (energy is a scalar).
@short Energy is a scalar, so direction doesn't matter.
@trap Choosing (B).
@@END

@@Q P06-T2 | E | 0.5 | Weight at Earth's centre | Speed
The weight of a body at the centre of the Earth is:
(A) the same as at the surface
(B) half of that at the surface
(C) zero
(D) infinite
@ans C
@sol $g_d = g(1 - d/R) = 0$ at $d = R$.
@short $g$ grows linearly from 0 at the centre to the surface value.
@trap Thinking gravity is strongest at the centre.
@@END

@@Q P06-T3 | E | 1 | Orbital speed at height R | Basic
If the orbital speed just above Earth's surface is 7.9 km/s, the orbital speed at a height $R$ above the surface is about:
(A) 3.95 km/s
(B) 5.6 km/s
(C) 7.9 km/s
(D) 11.2 km/s
@ans B
@sol $v \propto 1/\sqrt r$; $r$ doubles, so $v = 7.9/\sqrt2 \approx 5.6$ km/s.
@short Divide by $\sqrt2$.
@trap Halving the speed (3.95).
@@END

@@Q P06-T4 | E | 0.5 | Period scaling | NV
The orbital radius of a satellite is made 4 times larger. By what factor does its period increase?
@ans 8
@sol $T \propto r^{3/2} = 4^{3/2} = 8$.
@short —
@trap Answering 16 ($r^2$).
@@END

@@Q P06-T5 | E | 0.5 | Binding energy | Basic
The binding energy of a satellite of mass $m$ in a circular orbit of radius $r$ around a planet of mass $M$ is:
(A) $GMm/r$
(B) $GMm/2r$
(C) $-GMm/2r$
(D) $2GMm/r$
@ans B
@sol Binding energy $= -E = +\dfrac{GMm}{2r}$: the energy needed to free the satellite completely.
@short Binding energy is positive.
@trap Choosing the (negative) total energy itself.
@@END

## Answers & Solutions {#p06-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Gravitation
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
