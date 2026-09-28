# Electromagnetic Induction & Alternating Current {#p14}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | High
NCERT | Class 12 · Ch 6, 7
Study time | ~12 hours
:::

## Concept summary

- **Faraday's law:** a changing magnetic flux induces an emf, $\varepsilon = -N\dfrac{d\Phi}{dt}$. The flux can change through $B$, the area, or the orientation.
- **Lenz's law:** the induced current opposes the *change* that produced it. It is a consequence of energy conservation.
- **Inductance** is the "inertia" of current: $L = N\Phi/I$. It stores energy $\tfrac12LI^2$.
- **AC circuits:** resistors keep $V$ and $I$ in phase. In an inductor the current *lags* by $90^\circ$; in a capacitor it *leads* by $90^\circ$. Impedance combines them like vectors (phasors).
- Only resistors dissipate average power. Pure $L$ and $C$ carry **wattless** current.

## Formulas: Induction

:::formula Faraday–Lenz & motional emf
$$\Phi = \vec B\cdot\vec A = BA\cos\theta \qquad \varepsilon = -N\frac{d\Phi}{dt} \qquad \text{induced charge: } q = \frac{N\,\Delta\Phi}{R}$$
$$\text{rod moving}\perp B: \varepsilon = Blv \qquad \text{rod rotating about one end: } \varepsilon = \tfrac12B\omega l^2 \qquad \text{coil rotating: } \varepsilon = NBA\omega\sin\omega t$$
The force needed to pull a rod at constant speed in a closed circuit of resistance $R$: $F = \dfrac{B^2l^2v}{R}$, with power $\dfrac{B^2l^2v^2}{R}$ (all dissipated as heat).
:::

:::formula Inductance
$$L = \frac{N\Phi}{I} \qquad \varepsilon = -L\frac{dI}{dt} \qquad \text{solenoid: } L = \mu_0n^2Al = \frac{\mu_0N^2A}{l} \qquad U = \tfrac12LI^2$$
$$M = \mu_0n_1n_2Al \qquad M = k\sqrt{L_1L_2}\ (k \le 1) \qquad \text{series (no coupling): } L_1 + L_2 \qquad \text{parallel: } \frac{L_1L_2}{L_1+L_2}$$
**LR circuit:** growth $I = I_0(1 - e^{-t/\tau})$, decay $I = I_0e^{-t/\tau}$, with $\tau = L/R$. After one $\tau$ the current reaches 63% of its final value.
Energy density of a magnetic field: $u = \dfrac{B^2}{2\mu_0}$.
:::

## Formulas: Alternating current

:::formula AC basics
$$V = V_0\sin\omega t \qquad V_{rms} = \frac{V_0}{\sqrt2} \qquad V_{avg,\ half\ cycle} = \frac{2V_0}{\pi} \qquad V_{avg,\ full\ cycle} = 0$$
Household mains in India: $V_{rms} = 220$–230 V, $f = 50$ Hz. AC meters read **rms** values.
:::

:::formula Series LCR circuit
$$X_L = \omega L \qquad X_C = \frac1{\omega C} \qquad Z = \sqrt{R^2 + (X_L - X_C)^2} \qquad \tan\phi = \frac{X_L - X_C}{R}$$
$$\text{Resonance: } \omega_0 = \frac1{\sqrt{LC}},\ Z = R,\ I = I_{max} \qquad Q = \frac{\omega_0L}{R} = \frac1R\sqrt{\frac LC} \qquad \text{bandwidth } \Delta\omega = \frac{\omega_0}{Q} = \frac{R}{L}$$
$$P_{avg} = V_{rms}I_{rms}\cos\phi = I_{rms}^2R \qquad \cos\phi = \frac RZ \qquad \text{wattless component} = I_{rms}\sin\phi$$
| Element | Phase of $I$ relative to $V$ | Average power |
|---|---|---|
| R | in phase | $V_{rms}I_{rms}$ |
| L | lags by $90^\circ$ | 0 |
| C | leads by $90^\circ$ | 0 |
:::

:::formula LC oscillations, generator, transformer
**LC circuit:** $\omega = \dfrac1{\sqrt{LC}}$; energy swaps between $\dfrac{q^2}{2C}$ and $\tfrac12LI^2$ (analogue: $q \leftrightarrow x$, $L \leftrightarrow m$, $1/C \leftrightarrow k$).
**AC generator:** peak emf $\varepsilon_0 = NBA\omega$.
**Ideal transformer:** $\dfrac{V_s}{V_p} = \dfrac{N_s}{N_p} = \dfrac{I_p}{I_s}$. Step-up raises $V$ and lowers $I$. Losses: copper ($I^2R$), eddy currents (reduced by laminating the core), hysteresis (reduced with soft iron), and flux leakage.
:::

@@GRAPH lcr-resonance

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Motional emf:** rods on rails, rotating rods and discs, force/power needed.
2. **Flux-change emf and induced charge** in coils ($q = N\Delta\Phi/R$, independent of time).
3. **LCR series:** impedance, phase, power factor, average power, resonance frequency, Q factor.
4. **rms/average values** from a given $V(t)$.
5. **Transformer** turns/voltage/current ratios and efficiency.
6. **LR growth/decay** and energy stored in inductors.
7. **LC oscillation** frequency and energy exchange.
:::

## Shortcuts

:::shortcut Phasor triangle
Draw $R$ horizontally and $(X_L - X_C)$ vertically. The hypotenuse is $Z$, the angle is $\phi$, and the power factor is the cosine. Use 3-4-5 triangles: numbers like $R = 30$, $X = 40$ are chosen deliberately.
**Time saved:** about 1 minute.
:::

:::shortcut Resonance in rad/s vs Hz
$\omega_0 = 1/\sqrt{LC}$ is in **rad/s**. $f_0 = \omega_0/2\pi$. Options often include both. Check the unit asked for.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Motional emf / rotating rod | E | 1 min |
| Induced charge / emf from $\Delta\Phi$ | E | 1 min |
| LCR impedance/power | M | 2 min |
| Resonance / Q factor | E–M | 1 min |
| Transformer | E | 45 s |
| LR growth / energy | M | 1.5 min |
| Rod on rails with mass (terminal velocity) | H | 3 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Using $V_0$ instead of $V_{rms}$ in the power formula.
- Taking the full-cycle average of a sinusoid as $2V_0/\pi$. It's 0 over a full cycle.
- Missing the $\tfrac12$ in the rotating-rod emf $\tfrac12B\omega l^2$.
- Mixing up "lead" and "lag": **ELI the ICE man**. In L, E (voltage) leads I; in C, I leads E.
- Forgetting $N$ (the number of turns) in Faraday's law.
:::

## Practice questions

@@SET P14 · Practice

@@Q P14-01 | E | 0.5 | Motional emf | Speed
A 0.5 m rod moves at $4\ \text{m s}^{-1}$ perpendicular to a 0.2 T field (and perpendicular to its own length). The emf across its ends is:
(A) 0.1 V
(B) 0.4 V
(C) 0.8 V
(D) 4 V
@ans B
@sol $\varepsilon = Blv = 0.2\times0.5\times4 = 0.4$ V.
@short —
@trap —
@@END

@@Q P14-02 | E | 1 | Faraday's law for a coil | NV
A 100-turn coil of area $0.1\ \text{m}^2$ lies perpendicular to a field that falls uniformly from 0.5 T to zero in 0.1 s. Find the average induced emf (in V).
@ans 50
@sol $\varepsilon = N\dfrac{\Delta(BA)}{\Delta t} = 100\times\dfrac{0.5\times0.1}{0.1} = 50$ V.
@short —
@trap Omitting $N$ (0.5 V).
@@END

@@Q P14-03 | E | 1 | Induced charge | Basic
The flux through each turn of a 100-turn coil changes by 0.05 Wb. The coil's total resistance is 10 Ω. The charge that flows is:
(A) 0.005 C
(B) 0.05 C
(C) 0.5 C
(D) 5 C
@ans C
@sol $q = \dfrac{N\Delta\Phi}{R} = \dfrac{100\times0.05}{10} = 0.5$ C, regardless of how quickly the change happens.
@short Charge depends on the change in flux, not its rate.
@trap Thinking you need the time interval.
@@END

@@Q P14-04 | E | 0.5 | Energy in an inductor | NV
Find the energy (in J) stored in a 2 H inductor carrying 3 A.
@ans 9
@sol $U = \tfrac12LI^2 = \tfrac12\times2\times9 = 9$ J.
@short —
@trap —
@@END

@@Q P14-05 | M | 2 | LCR average power | JEE
A series LCR circuit has $R = 30\ \Omega$, $X_L = 80\ \Omega$, $X_C = 40\ \Omega$ and is connected to a 100 V (rms) source. The average power consumed is:
(A) 200 W
(B) 120 W
(C) 160 W
(D) 333 W
@ans B
@sol $Z = \sqrt{30^2 + 40^2} = 50\ \Omega$; $I_{rms} = 2$ A; $\cos\phi = 30/50 = 0.6$. $P = 100\times2\times0.6 = 120$ W (check: $I^2R = 4\times30$).
@short $P = I_{rms}^2R$ once you have $I$.
@trap Using $V^2/R$ (333 W).
@@END

@@Q P14-06 | M | 1 | Resonance: rad/s vs Hz | Tricky
In a series LCR circuit, $L = 0.1$ H and $C = 10\ \mu\text{F}$. The resonant **angular** frequency is:
(A) 1000 rad/s
(B) 159 rad/s
(C) 100 rad/s
(D) 10 000 rad/s
@ans A
@sol $\omega_0 = \dfrac1{\sqrt{LC}} = \dfrac1{\sqrt{10^{-6}}} = 1000$ rad/s. (That's $f_0 \approx 159$ Hz. The trap is option (B), with the wrong unit.)
@short —
@trap Choosing 159 rad/s.
@@END

@@Q P14-07 | E | 0.5 | Reading an AC expression | Speed
For $V = 220\sqrt2\sin(100\pi t)$ volts, the rms voltage and frequency are:
(A) 220 V, 50 Hz
(B) $220\sqrt2$ V, 100 Hz
(C) 220 V, 100 Hz
(D) 311 V, 50 Hz
@ans A
@sol $V_{rms} = V_0/\sqrt2 = 220$ V; $\omega = 100\pi \Rightarrow f = 50$ Hz.
@short —
@trap Reading $f = 100$ from $100\pi$.
@@END

@@Q P14-08 | E | 1 | Ideal transformer | Basic
An ideal transformer has 200 primary and 1000 secondary turns. The primary is at 220 V, and the secondary delivers 0.2 A. The primary current is:
(A) 0.04 A
(B) 1 A
(C) 0.2 A
(D) 5 A
@ans B
@sol $\dfrac{I_p}{I_s} = \dfrac{N_s}{N_p} = 5 \Rightarrow I_p = 1$ A. ($V_s = 1100$ V; power $220 = 220$ W.)
@short Power in = power out.
@trap Inverting the ratio (0.04 A).
@@END

@@Q P14-09 | E | 0.5 | LR time constant | Speed
A 4 H inductor is in series with a 2 Ω resistor. The time constant of the circuit is:
(A) 8 s
(B) 2 s
(C) 0.5 s
(D) 6 s
@ans B
@sol $\tau = L/R = 2$ s.
@short —
@trap $R/L$.
@@END

@@Q P14-10 | E | 1 | Rotating rod | Basic
A 1 m metal rod rotates at 20 rad/s about one end, in a plane perpendicular to a uniform 0.5 T field. The emf between its ends is:
(A) 10 V
(B) 5 V
(C) 20 V
(D) 2.5 V
@ans B
@sol $\varepsilon = \tfrac12B\omega l^2 = \tfrac12\times0.5\times20\times1 = 5$ V.
@short —
@trap Omitting the $\tfrac12$.
@@END

@@SET P14 · Chapter Test

@@Q P14-T1 | E | 0.5 | Basis of Lenz's law | Concept
Lenz's law is a consequence of the conservation of:
(A) charge
(B) momentum
(C) energy
(D) mass
@ans C
@sol If the induced current aided the change, it would create energy from nothing.
@short —
@trap —
@@END

@@Q P14-T2 | E | 0.5 | Phase in a pure inductor | Speed
In a purely inductive AC circuit, the current:
(A) leads the voltage by $\pi/2$
(B) lags the voltage by $\pi/2$
(C) is in phase with the voltage
(D) lags by $\pi$
@ans B
@sol The inductor opposes changes in current, so the current lags behind the voltage by $90^\circ$.
@short ELI.
@trap —
@@END

@@Q P14-T3 | E | 0.5 | Reactance vs frequency | Speed
If the frequency of an AC source is doubled, the capacitive reactance:
(A) doubles
(B) halves
(C) stays the same
(D) becomes 4 times
@ans B
@sol $X_C = 1/(\omega C) \propto 1/f$.
@short —
@trap Applying the inductive behaviour instead.
@@END

@@Q P14-T4 | E | 1 | Generator peak emf | NV
A 100-turn coil of area $0.01\ \text{m}^2$ rotates at 60 rad/s in a 0.5 T field. Find the peak emf (in V).
@ans 30
@sol $\varepsilon_0 = NBA\omega = 100\times0.5\times0.01\times60 = 30$ V.
@short —
@trap —
@@END

@@Q P14-T5 | E | 0.5 | Power factor at resonance | Speed
At resonance in a series LCR circuit, the power factor is:
(A) 0
(B) 0.5
(C) 1
(D) $1/\sqrt2$
@ans C
@sol $X_L = X_C$, so $Z = R$, $\phi = 0$ and $\cos\phi = 1$.
@short —
@trap —
@@END

## Answers & Solutions {#p14-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · EMI & AC
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
