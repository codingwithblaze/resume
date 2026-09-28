# Magnetic Effects of Current & Magnetism {#p13}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 12 · Ch 4, 5
Study time | ~14 hours
:::

## Concept summary

- **Moving charges create magnetic fields** (Biot–Savart, Ampère). **Magnetic fields exert forces on moving charges** (Lorentz) and on currents.
- The magnetic force $q\vec v\times\vec B$ is always ⟂ to the velocity. It **does no work** and changes only direction, which is why charges move on circles or helices.
- A **current loop is a magnetic dipole**, $\vec m = NI\vec A$. It feels a torque $\vec m\times\vec B$ in a uniform field. That is the working principle of the moving-coil galvanometer.
- **Magnetic materials** are dia-, para- or ferromagnetic, depending on their atomic moments and how those moments respond to a field and to temperature.

:::warning Syllabus note
Earth's magnetism (elements, dip, declination) and the tangent galvanometer are **not** in the 2024–2026 syllabus text [NTA-SYL].
:::

## Formulas

:::formula Fields of standard currents
| Source | $B$ |
|---|---|
| Finite straight wire (angles $\alpha$, $\beta$ at the ends, distance $d$) | $\dfrac{\mu_0I}{4\pi d}(\sin\alpha + \sin\beta)$ |
| Infinite straight wire | $\dfrac{\mu_0I}{2\pi d}$ |
| Semi-infinite wire, at a point level with its end | $\dfrac{\mu_0I}{4\pi d}$ |
| Centre of a circular loop ($N$ turns) | $\dfrac{\mu_0NI}{2R}$ |
| Arc subtending angle $\theta$ at the centre | $\dfrac{\mu_0I\theta}{4\pi R}$ |
| Axis of a loop, distance $x$ | $\dfrac{\mu_0NIR^2}{2(R^2 + x^2)^{3/2}}$ |
| Long solenoid ($n$ turns per metre) | $\mu_0nI$ inside; $\tfrac12\mu_0nI$ at an end |
| Toroid ($N$ turns, radius $r$) | $\dfrac{\mu_0NI}{2\pi r}$ |
| Thick wire (radius $R$), inside at $r$ | $\dfrac{\mu_0Ir}{2\pi R^2}$ |

$\mu_0 = 4\pi\times10^{-7}$ T m/A. **Ampère's law:** $\oint\vec B\cdot d\vec l = \mu_0I_{enc}$.
Points lying on the line of a straight wire get **zero** field from it.
:::

:::formula Forces
$$\vec F = q(\vec E + \vec v\times\vec B) \qquad r = \frac{mv}{qB} = \frac{p}{qB} = \frac{\sqrt{2mK}}{qB} = \frac1B\sqrt{\frac{2mV}{q}}$$
$$T = \frac{2\pi m}{qB} \ \text{(independent of speed)} \qquad \text{pitch of helix} = v\cos\theta\cdot T \qquad \text{velocity selector: } v = \frac EB$$
$$\vec F = I\vec L\times\vec B \qquad \frac{F}{L} = \frac{\mu_0I_1I_2}{2\pi d} \ \text{(parallel currents attract, antiparallel repel)}$$
A closed current loop in a **uniform** field feels zero net force.
:::

:::formula Torque, dipoles, galvanometer
$$\vec m = NI\vec A \qquad \vec\tau = \vec m\times\vec B \qquad U = -\vec m\cdot\vec B$$
**Moving-coil galvanometer:** $NIAB = k\phi$. Current sensitivity $\dfrac\phi I = \dfrac{NAB}{k}$; voltage sensitivity $\dfrac\phi V = \dfrac{NAB}{kR_G}$.
**Ammeter:** shunt $S = \dfrac{I_gG}{I - I_g}$ in parallel. **Voltmeter:** series $R = \dfrac{V}{I_g} - G$.
**Orbiting electron:** $\mu = \dfrac{evr}{2} = \dfrac{e}{2m_e}L$. Bohr magneton $\mu_B = \dfrac{eh}{4\pi m_e} \approx 9.27\times10^{-24}\ \text{J T}^{-1}$.
**Bar magnet (short dipole):** axial $B = \dfrac{\mu_0}{4\pi}\dfrac{2m}{r^3}$, equatorial $B = \dfrac{\mu_0}{4\pi}\dfrac{m}{r^3}$.
:::

:::formula Magnetic materials
| Type | $\chi$ | $\mu_r$ | Behaviour | Temperature | Examples |
|---|---|---|---|---|---|
| Diamagnetic | small, negative | < 1 | weakly repelled, moves to weaker field | independent | Bi, Cu, water, superconductors ($\chi = -1$) |
| Paramagnetic | small, positive | > 1 | weakly attracted | $\chi = C/T$ (Curie law) | Al, Na, O₂ |
| Ferromagnetic | large, positive | ≫ 1 | strongly attracted; domains | above the Curie temperature it becomes paramagnetic | Fe, Co, Ni |

$B = \mu_0(H + M)$, $M = \chi H$, $\mu_r = 1 + \chi$. **Soft iron** (low coercivity, narrow hysteresis loop) suits electromagnets and transformer cores. **Steel** (high retentivity and coercivity) suits permanent magnets.
:::

@@GRAPH b-field-wire

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Field at the centre of composite shapes:** arcs + straight segments, loops of several radii, semicircles with radial leads.
2. **Charged particle in B:** radius comparisons (proton, deuteron, α), period, helix pitch, crossed $E$ and $B$.
3. **Force between parallel wires;** force on a wire loop near a long wire.
4. **Galvanometer conversion** to ammeter/voltmeter.
5. **Torque on a coil** and its potential energy.
6. **Magnetic materials:** identifying types from $\chi$ or behaviour; Curie law.
7. **Solenoid/toroid fields** with Ampère's law.
:::

## Shortcuts

:::shortcut Radius ratios for particles
Same **KE**: $r \propto \sqrt m/q$. Same **accelerating voltage**: $r \propto \sqrt{m/q}$. Same **momentum**: $r \propto 1/q$.
Proton : deuteron : α with the same KE: $1 : \sqrt2 : 1$.
:::

:::shortcut Composite-loop fields
Break the shape into arcs (use $\mu_0I\theta/4\pi R$) and straight pieces (radial pieces give **0**). Add with signs from the right-hand rule. That's a full answer in under a minute.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Standard-field formula | E | 45 s |
| Composite loop field | M | 1.5 min |
| Particle radius / period | E–M | 1 min |
| Galvanometer conversion | E | 1 min |
| Force between wires / on loops | M | 1.5 min |
| Magnetic materials facts | E | 30 s |
| Non-uniform $B$ or combined $E$–$B$ motion | H | 3 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Taking the magnetic force as doing work. It never changes the speed.
- For the shunt, using $I$ instead of $(I - I_g)$ in the denominator.
- Diamagnetic susceptibility depends on temperature? **No**, it's independent.
- For a loop's field at its centre, forgetting the number of turns $N$.
- Using $B = \mu_0I/2\pi d$ for a finite wire.
:::

## Practice questions

@@SET P13 · Practice

@@Q P13-01 | E | 0.75 | Field at the centre of a loop | Calc
The magnetic field at the centre of a circular loop of radius 10 cm carrying 5 A is:
(A) $\pi\times10^{-5}$ T
(B) $2\pi\times10^{-5}$ T
(C) $10^{-5}$ T
(D) $\pi\times10^{-6}$ T
@ans A
@sol $B = \dfrac{\mu_0I}{2R} = \dfrac{4\pi\times10^{-7}\times5}{0.2} = \pi\times10^{-5}$ T.
@short —
@trap Using the diameter in place of $R$.
@@END

@@Q P13-02 | M | 1 | Radii of proton and α particle | Concept
A proton and an α-particle with **equal kinetic energies** enter the same uniform magnetic field perpendicularly. The ratio of their radii $r_p : r_\alpha$ is:
(A) 1 : 1
(B) 1 : 2
(C) 2 : 1
(D) 1 : $\sqrt2$
@ans A
@sol $r = \dfrac{\sqrt{2mK}}{qB} \propto \dfrac{\sqrt m}{q}$: proton $\sqrt1/1 = 1$, α $\sqrt4/2 = 1$.
@short —
@trap Using the same-speed rule ($r \propto m/q$), which gives 1 : 2.
@@END

@@Q P13-03 | E | 1 | Force between parallel wires | Basic
Two long parallel wires 10 cm apart carry 10 A and 20 A in the same direction. The force per metre between them is:
(A) $4\times10^{-4}$ N/m, attractive
(B) $4\times10^{-4}$ N/m, repulsive
(C) $2\times10^{-4}$ N/m, attractive
(D) $8\times10^{-4}$ N/m, attractive
@ans A
@sol $\dfrac FL = \dfrac{\mu_0I_1I_2}{2\pi d} = \dfrac{2\times10^{-7}\times200}{0.1} = 4\times10^{-4}$ N/m. Like currents attract.
@short $\dfrac{\mu_0}{2\pi} = 2\times10^{-7}$.
@trap Saying "same direction repels", which is the opposite of electrostatics intuition.
@@END

@@Q P13-04 | E | 1 | Galvanometer → ammeter | Basic
A galvanometer of resistance 50 Ω gives full-scale deflection at 1 mA. The shunt needed to convert it into an ammeter of range 1 A is about:
(A) 0.05 Ω in parallel
(B) 0.05 Ω in series
(C) 50 Ω in parallel
(D) 0.5 Ω in parallel
@ans A
@sol $S = \dfrac{I_gG}{I - I_g} = \dfrac{0.001\times50}{0.999} \approx 0.05\ \Omega$, in parallel.
@short —
@trap Putting the shunt in series.
@@END

@@Q P13-05 | E | 1 | Galvanometer → voltmeter | NV
The same galvanometer (50 Ω, 1 mA full scale) is to be converted into a voltmeter of range 10 V. Find the series resistance needed (in Ω).
@ans 9950
@sol $R = \dfrac{V}{I_g} - G = 10\,000 - 50 = 9950\ \Omega$.
@short —
@trap Forgetting to subtract $G$.
@@END

@@Q P13-06 | E | 1 | Solenoid field | Calc
A 0.5 m long solenoid has 500 turns and carries 2 A. The field inside is about:
(A) $2.5\times10^{-3}$ T
(B) $1.26\times10^{-3}$ T
(C) $5.0\times10^{-3}$ T
(D) $2.5\times10^{-4}$ T
@ans A
@sol $n = 1000\ \text{m}^{-1}$; $B = \mu_0nI = 4\pi\times10^{-7}\times1000\times2 = 8\pi\times10^{-4} \approx 2.5\times10^{-3}$ T.
@short —
@trap Using $N$ in place of $n$.
@@END

@@Q P13-07 | M | 1.5 | Semicircle with radial leads | JEE
A wire runs radially inward to a point on a circle, follows a semicircular arc of radius $R$ to the diametrically opposite point, then runs radially outward, carrying current $I$ throughout. The field at the centre is:
(A) $\dfrac{\mu_0I}{2R}$
(B) $\dfrac{\mu_0I}{4R}$
(C) $\dfrac{\mu_0I}{4\pi R}$
(D) 0
@ans B
@sol The radial segments point through the centre, so they contribute nothing. The semicircle gives $\dfrac{\mu_0I\pi}{4\pi R} = \dfrac{\mu_0I}{4R}$.
@short Radial leads contribute zero.
@trap Adding contributions from the leads.
@@END

@@Q P13-08 | E | 0.5 | Cyclotron frequency | Concept
The time period of a charged particle moving in a circle in a uniform magnetic field:
(A) increases with its speed
(B) decreases with its speed
(C) is independent of its speed
(D) is proportional to the radius
@ans C
@sol $T = 2\pi m/(qB)$. A faster particle moves on a larger circle in the same time. This is the basis of the cyclotron.
@short —
@trap —
@@END

@@Q P13-09 | E | 0.5 | Paramagnetic susceptibility | Speed
The susceptibility of a paramagnetic substance varies with absolute temperature $T$ as:
(A) $T$
(B) $1/T$
(C) independent of $T$
(D) $T^2$
@ans B
@sol Curie's law: $\chi = C/T$. Thermal agitation disturbs the alignment of the atomic moments.
@short —
@trap Confusing it with diamagnetism (independent of $T$).
@@END

@@Q P13-10 | E | 1 | Torque on a coil | NV
A 50-turn coil of area $0.02\ \text{m}^2$ carries 2 A in a uniform 1 T field, with the field **parallel to the plane** of the coil. Find the torque (in N m).
@ans 2
@sol $\tau = NIAB\sin90^\circ = 50\times2\times0.02\times1 = 2$ N m. The field lies in the plane, so it is perpendicular to $\vec m$.
@short The torque is maximum when the field is parallel to the plane.
@trap Using $\sin0^\circ$ by confusing "plane" with "normal".
@@END

@@SET P13 · Chapter Test

@@Q P13-T1 | E | 0.5 | Charge moving along B | Speed
A charge moves parallel to a uniform magnetic field. The magnetic force on it is:
(A) $qvB$
(B) zero
(C) $qvB/2$
(D) along the velocity
@ans B
@sol $\vec v\times\vec B = 0$ when they are parallel.
@short —
@trap —
@@END

@@Q P13-T2 | M | 1 | Field inside a thick wire | Concept
A long straight wire of radius $R$ carries current $I$ uniformly distributed over its cross-section. The field at $r = R/2$ is:
(A) $\dfrac{\mu_0I}{4\pi R}$
(B) $\dfrac{\mu_0I}{2\pi R}$
(C) $\dfrac{\mu_0I}{\pi R}$
(D) 0
@ans A
@sol $B = \dfrac{\mu_0Ir}{2\pi R^2} = \dfrac{\mu_0I}{4\pi R}$ at $r = R/2$.
@short Half of the surface value $\mu_0I/2\pi R$.
@trap Using the outside formula with $r = R/2$.
@@END

@@Q P13-T3 | M | 1 | Helix pitch | Concept
A charge $q$ (mass $m$) enters a uniform field $B$ with speed $v$ at $60^\circ$ to the field. The pitch of its helical path is:
(A) $\dfrac{\pi mv}{qB}$
(B) $\dfrac{2\pi mv}{qB}$
(C) $\dfrac{\sqrt3\pi mv}{qB}$
(D) $\dfrac{\pi mv}{2qB}$
@ans A
@sol Pitch $= v\cos60^\circ\times\dfrac{2\pi m}{qB} = \dfrac{\pi mv}{qB}$.
@short Parallel component × period.
@trap Using $v\sin60^\circ$.
@@END

@@Q P13-T4 | E | 0.5 | Magnetic moment of a coil | NV
A 100-turn coil of area $0.01\ \text{m}^2$ carries 5 A. Find its magnetic moment (in A m²).
@ans 5
@sol $m = NIA = 100\times5\times0.01 = 5$ A m².
@short —
@trap —
@@END

@@Q P13-T5 | E | 0.5 | Curie temperature | Speed
Above its Curie temperature, a ferromagnetic material becomes:
(A) diamagnetic
(B) paramagnetic
(C) a stronger ferromagnet
(D) superconducting
@ans B
@sol Thermal agitation destroys the domain alignment, leaving paramagnetic behaviour.
@short —
@trap —
@@END

## Answers & Solutions {#p13-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Magnetism
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
