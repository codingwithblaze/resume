# Electrostatics & Capacitors {#p11}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 12 · Ch 1, 2
Study time | ~16 hours
:::

## Concept summary

- Charge is **quantised** ($q = ne$) and **conserved**. **Coulomb's law** gives the force between point charges, and superposition handles many charges.
- The **electric field** $\vec E = \vec F/q_0$ is a vector. The **potential** $V$ is a scalar, and $\vec E = -\nabla V$. Scalar potentials are usually easier to add.
- **Gauss's law** gives the field of symmetric distributions (line, sheet, sphere) in one line.
- **Conductors** in equilibrium: $E = 0$ inside, all charge on the surface, the surface is an equipotential, and the field just outside is $\sigma/\varepsilon_0$ (⟂ to the surface).
- **Capacitors** store energy $\tfrac12CV^2$. Dielectrics increase $C$ by a factor $K$.

## Formulas

:::formula Coulomb, field, potential
$$F = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2} \qquad k = \frac1{4\pi\varepsilon_0} = 9\times10^9\ \text{N m}^2\text{C}^{-2} \qquad E = \frac{kq}{r^2} \qquad V = \frac{kq}{r}$$
$$\vec E = -\frac{dV}{dr}\hat r \qquad V_A - V_B = -\int_B^A\vec E\cdot d\vec l \qquad U_{12} = \frac{kq_1q_2}{r} \qquad W_{ext} = q(V_f - V_i)$$
In a medium of dielectric constant $K$: $F$ and $E$ are reduced by a factor $K$.
:::

:::formula Electric dipole ($\vec p = q\vec d$, from − to +)
| Quantity | Axial point (distance $r \gg d$) | Equatorial point |
|---|---|---|
| Field | $\dfrac{2kp}{r^3}$ (along $\vec p$) | $\dfrac{kp}{r^3}$ (opposite to $\vec p$) |
| Potential | $\dfrac{kp}{r^2}$ | 0 |

General point: $V = \dfrac{kp\cos\theta}{r^2}$, $E = \dfrac{kp}{r^3}\sqrt{1 + 3\cos^2\theta}$.
In a uniform field: torque $\vec\tau = \vec p\times\vec E$, energy $U = -\vec p\cdot\vec E$, and net force zero. Work to rotate from $\theta_1$ to $\theta_2$ is $pE(\cos\theta_1 - \cos\theta_2)$. Stable equilibrium at $\theta = 0$, unstable at $\theta = 180^\circ$.
:::

:::formula Gauss's law results
$$\oint\vec E\cdot d\vec A = \frac{q_{enc}}{\varepsilon_0}$$
| Distribution | Field |
|---|---|
| Infinite line charge ($\lambda$) | $\dfrac{\lambda}{2\pi\varepsilon_0r}$ |
| Infinite plane sheet ($\sigma$) | $\dfrac{\sigma}{2\varepsilon_0}$ (independent of distance) |
| Near a charged conductor's surface | $\dfrac{\sigma}{\varepsilon_0}$ |
| Thin spherical shell ($Q$, $R$) | $0$ inside; $\dfrac{kQ}{r^2}$ outside |
| Uniformly charged solid sphere | $\dfrac{kQr}{R^3}$ inside; $\dfrac{kQ}{r^2}$ outside |

Flux through a closed surface depends **only** on the enclosed charge. A charge $q$ at the centre of a cube gives flux $q/6\varepsilon_0$ through each face. At a corner of the cube, the flux through the whole cube is $q/8\varepsilon_0$.
:::

:::formula Capacitors
$$C = \frac QV \qquad \text{parallel plate: } C = \frac{\varepsilon_0A}{d} \qquad \text{with dielectric filling the gap: } C = \frac{K\varepsilon_0A}{d}$$
$$\text{slab of thickness } t < d: \ C = \frac{\varepsilon_0A}{d - t + t/K} \qquad \text{metal slab: } C = \frac{\varepsilon_0A}{d - t}$$
$$\text{isolated sphere: } C = 4\pi\varepsilon_0R \qquad U = \frac12CV^2 = \frac{Q^2}{2C} = \frac12QV \qquad u = \frac12\varepsilon_0E^2$$
**Series:** $\dfrac1{C} = \sum\dfrac1{C_i}$ (same $Q$). **Parallel:** $C = \sum C_i$ (same $V$).
**Sharing charge** between two capacitors: common $V = \dfrac{C_1V_1 + C_2V_2}{C_1 + C_2}$; energy lost $= \dfrac{C_1C_2(V_1 - V_2)^2}{2(C_1+C_2)}$.
**Inserting a dielectric:** battery connected → $V$ fixed, so $Q$, $C$, $U$ all rise by $K$. Battery disconnected → $Q$ fixed, so $V$ and $U$ fall by $K$.
Force between the plates: $F = \dfrac{Q^2}{2\varepsilon_0A}$.
:::

@@GRAPH field-sphere

:::important Conductors vs insulators in one table
| | Conductor (charged, isolated) | Insulator (uniform volume charge) |
|---|---|---|
| Charge location | outer surface only | throughout the volume |
| $E$ inside | 0 | grows ∝ $r$ (sphere) |
| $V$ inside | constant = surface value | maximum at the centre, $\tfrac32kQ/R$ |
| Sharp points | high $\sigma$, high $E$ (corona discharge) | — |
:::

## Standard models & assumptions

- Point charges; infinite sheets and lines as idealisations; fringing ignored for parallel-plate capacitors.
- "Earthed" means $V = 0$, not $Q = 0$.
- The potential at infinity is zero.

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Superposition:** net force or field at a point due to charges at the corners of a triangle or square; null points on a line.
2. **Gauss's law / flux:** charge inside a cube, flux through a face; field of a sphere at $r < R$ vs $r > R$.
3. **Dipoles:** torque, work to rotate, axial vs equatorial ratios.
4. **Capacitor networks:** equivalent $C$, charge on one capacitor, energy stored.
5. **Dielectric insertion** with and without a battery; partially filled capacitors.
6. **Potential energy of a system of charges** (work to assemble).
7. **Motion of a charge in a uniform field** (projectile analogue: $a = qE/m$).
:::

## Shortcuts

:::shortcut Symmetry kills vectors
Equal charges at the vertices of a regular polygon give $E = 0$ at the centre, but $V = nkq/r \ne 0$. Use symmetry to cancel field components before writing any vector sum.
**Time saved:** 1–2 minutes on "square of charges" questions.
:::

:::shortcut Dielectric slab as series capacitors
A slab of thickness $t$ in a gap $d$ acts as an air capacitor $(d - t)$ in series with a dielectric capacitor $(t, K)$. Slabs placed side by side (each covering part of the area) act in **parallel**.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Coulomb / field superposition | E–M | 1.5 min |
| Gauss flux (cube/face) | E | 45 s |
| Dipole torque/energy | E | 1 min |
| Capacitor networks | M | 2 min |
| Dielectric with/without battery | M | 1.5 min |
| System energy / work to assemble | M | 2 min |
| Non-uniform charge density + Gauss | H | 3 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Adding fields as scalars. Resolve into components first.
- Sheet field: $\sigma/2\varepsilon_0$ for an isolated sheet but $\sigma/\varepsilon_0$ near a conductor's surface.
- Dielectric questions: always check whether the **battery stays connected**.
- Potential energy of a system: count **each pair once**, $\tfrac{n(n-1)}{2}$ pairs.
- Forgetting the sign of charges in potential sums.
:::

## Practice questions

@@SET P11 · Practice

@@Q P11-01 | E | 1 | Coulomb force change | Basic
Two point charges repel with force $F$. If each charge is doubled and the distance between them is also doubled, the force becomes:
(A) $F$
(B) $2F$
(C) $F/2$
(D) $4F$
@ans A
@sol $F \propto q_1q_2/r^2 = \dfrac{(2)(2)}{2^2} = 1$, so the force is unchanged.
@short Numerator ×4, denominator ×4.
@trap —
@@END

@@Q P11-02 | E | 0.75 | Flux through a cube face | Speed
A charge $q$ sits at the centre of a cube. The electric flux through **one face** of the cube is:
(A) $q/\varepsilon_0$
(B) $q/6\varepsilon_0$
(C) $q/8\varepsilon_0$
(D) $6q/\varepsilon_0$
@ans B
@sol The total flux $q/\varepsilon_0$ divides equally among 6 faces by symmetry.
@short —
@trap Choosing the corner-charge value $q/8\varepsilon_0$.
@@END

@@Q P11-03 | M | 1.5 | Work to rotate a dipole | Concept
A dipole of moment $p$ is aligned with a uniform field $E$. The work needed to rotate it by $180^\circ$ is:
(A) 0
(B) $pE$
(C) $2pE$
(D) $-2pE$
@ans C
@sol $W = pE(\cos0^\circ - \cos180^\circ) = 2pE$.
@short From stable ($U = -pE$) to unstable ($U = +pE$).
@trap Using the torque $pE\sin\theta$, which is zero at both ends.
@@END

@@Q P11-04 | M | 2 | Capacitor network | JEE
Three capacitors of $2\ \mu\text{F}$, $3\ \mu\text{F}$ and $6\ \mu\text{F}$ are in series across a 12 V battery. The charge on the $3\ \mu\text{F}$ capacitor and the energy it stores are:
(A) $12\ \mu\text{C}$, $24\ \mu\text{J}$
(B) $12\ \mu\text{C}$, $48\ \mu\text{J}$
(C) $24\ \mu\text{C}$, $24\ \mu\text{J}$
(D) $6\ \mu\text{C}$, $6\ \mu\text{J}$
@ans A
@sol $\dfrac1C = \dfrac12 + \dfrac13 + \dfrac16 = 1 \Rightarrow C = 1\ \mu\text{F}$. $Q = 12\ \mu\text{C}$ on each. $U_3 = \dfrac{Q^2}{2C_3} = \dfrac{144}{6} = 24\ \mu\text{J}$.
@short In series: same $Q$; $V_3 = Q/C_3 = 4$ V, so $U = \tfrac12QV = 24\ \mu$J.
@trap Using $\tfrac12CV^2$ with the full 12 V.
@@END

@@Q P11-05 | M | 1.5 | Dielectric with battery disconnected | Concept
A charged parallel-plate capacitor is **disconnected** from its battery, and a dielectric slab ($K = 4$) is then inserted to fill the gap. The stored energy:
(A) becomes 4 times
(B) becomes 1/4
(C) stays the same
(D) becomes 16 times
@ans B
@sol $Q$ is fixed and $C \to 4C$, so $U = \dfrac{Q^2}{2C}$ falls to $1/4$.
@short Isolated: $U \propto 1/C$. Connected: $U \propto C$.
@trap Assuming the battery stays connected (×4).
@@END

@@Q P11-06 | M | 1.5 | Field of a charged solid sphere | Concept
A uniformly charged **non-conducting** sphere of radius $R$ carries total charge $Q$. The field at $r = R/2$ is:
(A) 0
(B) $\dfrac{kQ}{2R^2}$
(C) $\dfrac{4kQ}{R^2}$
(D) $\dfrac{kQ}{4R^2}$
@ans B
@sol Inside: $E = \dfrac{kQr}{R^3} = \dfrac{kQ}{2R^2}$ at $r = R/2$.
@short Inside $E \propto r$: at half the radius, half the surface field.
@trap Treating it as a conductor ($E = 0$).
@@END

@@Q P11-07 | M | 2 | Potential energy of a charge system | NV
Three charges of $+1\ \mu\text{C}$ each are placed at the corners of an equilateral triangle of side 0.3 m. Find the electrostatic potential energy of the system (in mJ). ($k = 9\times10^9$ SI.)
@ans 90
@sol Each pair: $U = \dfrac{kq^2}{r} = \dfrac{9\times10^9\times10^{-12}}{0.3} = 0.03$ J. Three pairs: $0.09$ J $= 90$ mJ.
@short Count the 3 pairs once each.
@trap Counting 6 ordered pairs.
@@END

@@Q P11-08 | E | 1 | Common potential after sharing | NV
A $2\ \mu\text{F}$ capacitor charged to 100 V is connected in parallel to an uncharged $3\ \mu\text{F}$ capacitor. Find the common potential (in V).
@ans 40
@sol $V = \dfrac{C_1V_1}{C_1 + C_2} = \dfrac{200}{5} = 40$ V.
@short Charge is conserved; energy is not.
@trap Conserving energy instead of charge.
@@END

@@Q P11-09 | E | 1 | Null point of two charges | Basic
Charges $+4q$ and $+q$ are 30 cm apart. The point where the net field is zero lies on the line joining them, at a distance from $+4q$ of:
(A) 10 cm
(B) 15 cm
(C) 20 cm
(D) 24 cm
@ans C
@sol $\dfrac{4q}{x^2} = \dfrac{q}{(30-x)^2} \Rightarrow 2(30 - x) = x \Rightarrow x = 20$ cm.
@short For like charges, the null point lies between them, closer to the smaller charge.
@trap Measuring from the smaller charge.
@@END

@@SET P11 · Chapter Test

@@Q P11-T1 | E | 0.5 | Field inside a conductor | Speed
Inside a charged hollow conducting sphere, the electric field is:
(A) maximum at the centre
(B) zero
(C) $kQ/R^2$
(D) proportional to $r$
@ans B
@sol In electrostatic equilibrium, the field inside a conductor (and inside its cavity, if there's no charge in it) is zero.
@short —
@trap —
@@END

@@Q P11-T2 | E | 0.75 | Parallel-plate capacitance | Basic
If the plate separation of a parallel-plate capacitor is halved and its plate area is doubled, its capacitance becomes:
(A) the same
(B) 2 times
(C) 4 times
(D) 1/4 times
@ans C
@sol $C \propto A/d = 2/(1/2) = 4$.
@short —
@trap —
@@END

@@Q P11-T3 | M | 1 | Dipole on its equatorial line | Concept
At a point on the equatorial line of a short dipole:
(A) $V = 0$ and $\vec E$ is parallel to $\vec p$
(B) $V = 0$ and $\vec E$ is antiparallel to $\vec p$
(C) $V \ne 0$ and $\vec E = 0$
(D) $V$ and $E$ are both zero
@ans B
@sol On the equatorial line the potentials of $+q$ and $-q$ cancel, but their fields add to a resultant pointing opposite to $\vec p$.
@short Zero potential doesn't mean zero field.
@trap Choosing (D).
@@END

@@Q P11-T4 | E | 1 | Energy of a capacitor | NV
A $10\ \mu\text{F}$ capacitor is charged to 20 V. Find the stored energy (in mJ).
@ans 2
@sol $U = \tfrac12CV^2 = \tfrac12\times10^{-5}\times400 = 2\times10^{-3}$ J $= 2$ mJ.
@short —
@trap Forgetting the $\tfrac12$ (4 mJ).
@@END

@@Q P11-T5 | M | 1.5 | Partially filled capacitor | JEE
A parallel-plate capacitor with gap $d$ has capacitance $C_0$. A dielectric slab of $K = 2$ and thickness $d/2$ is inserted parallel to the plates. The new capacitance is:
(A) $\tfrac43C_0$
(B) $\tfrac32C_0$
(C) $2C_0$
(D) $\tfrac54C_0$
@ans A
@sol $C = \dfrac{\varepsilon_0A}{d - t + t/K} = \dfrac{\varepsilon_0A}{d/2 + d/4} = \dfrac{4}{3}\dfrac{\varepsilon_0A}{d} = \tfrac43C_0$.
@short Effective gap: $d - t(1 - 1/K)$.
@trap Treating the halves as parallel gives $\tfrac32C_0$.
@@END

## Answers & Solutions {#p11-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Electrostatics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
