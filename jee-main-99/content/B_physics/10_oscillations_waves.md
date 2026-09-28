# Oscillations & Waves {#p10}

:::stats
Typical questions | 1–2 per shift
Difficulty | Medium
Priority | High
NCERT | Class 11 · Ch 13, 14
Study time | ~12 hours
:::

## Concept summary

- **SHM** is motion under a restoring force proportional to displacement: $a = -\omega^2x$. Its solution is a sine or cosine, and its energy oscillates between KE and PE.
- To find the period of **any** SHM system, write the restoring force or torque as $-(\text{const})\times\text{displacement}$ and read off $\omega$.
- A **wave** carries energy, not matter. Its speed depends on the medium: tension/density for strings, elasticity/density for sound.
- **Superposition** gives interference, standing waves (strings, pipes) and beats.

:::warning Syllabus note
The official Unit 10 text (2024–2026) lists waves up to **"Standing waves in strings and organ pipes, fundamental mode and harmonics. Beats."** The **Doppler effect is not listed**, so treat it as low priority [NTA-SYL].
:::

## Formulas: Oscillations

:::formula SHM kinematics & energy
$$x = A\sin(\omega t + \phi) \qquad v = \omega\sqrt{A^2 - x^2} \qquad a = -\omega^2x \qquad v_{max} = A\omega \qquad a_{max} = A\omega^2$$
$$K = \tfrac12m\omega^2(A^2 - x^2) \qquad U = \tfrac12m\omega^2x^2 \qquad E = \tfrac12m\omega^2A^2 = \tfrac12kA^2$$
- $K = U$ at $x = A/\sqrt2$. KE and PE each oscillate at frequency $2f$.
- Phase difference: $v$ leads $x$ by $\pi/2$; $a$ leads $x$ by $\pi$.
:::

:::formula Time periods of standard systems
| System | Period |
|---|---|
| Spring–mass | $T = 2\pi\sqrt{m/k}$ (horizontal or vertical; the same) |
| Springs in series / parallel | $\dfrac1{k_s} = \dfrac1{k_1} + \dfrac1{k_2}$ ; $k_p = k_1 + k_2$ |
| Spring cut into $n$ equal parts | each part has $nk$ |
| Simple pendulum (small angle) | $T = 2\pi\sqrt{L/g}$ |
| Pendulum in a lift accelerating up / down at $a$ | $2\pi\sqrt{L/(g \pm a)}$ |
| Pendulum in a car accelerating horizontally at $a$ | $2\pi\sqrt{L/\sqrt{g^2+a^2}}$ |
| Physical (compound) pendulum | $2\pi\sqrt{I/(mgd)}$, $d$ = pivot-to-COM distance |
| Liquid in a U-tube (total column length $L$) | $2\pi\sqrt{L/2g}$ |
| Floating cylinder (submerged length $h$) | $2\pi\sqrt{h/g}$ |
:::

@@GRAPH shm-energy

## Formulas: Waves

:::formula Wave speed & equation
$$v = f\lambda = \frac\omega k \qquad \text{string: } v = \sqrt{T/\mu} \qquad \text{sound: } v = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma RT}{M}} \ \text{(Laplace)}$$
$$y = A\sin(kx - \omega t) \ \text{(travelling in } +x) \qquad k = \frac{2\pi}\lambda \qquad \omega = 2\pi f \qquad v_{particle} = \frac{\partial y}{\partial t} = -v\frac{\partial y}{\partial x}$$
- Speed of sound $\propto \sqrt T$ (kelvin), independent of pressure at constant $T$. Newton's formula $\sqrt{P/\rho}$ was 15% too low.
- Intensity $\propto A^2\omega^2$. Phase difference $\Delta\phi = \dfrac{2\pi}{\lambda}\Delta x$.
- Reflection from a fixed end: phase change $\pi$. From a free end: no phase change.
:::

:::formula Superposition, standing waves, beats
**Interference:** $A_R = \sqrt{A_1^2 + A_2^2 + 2A_1A_2\cos\phi}$; $I_R = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi$.
**Standing wave** $y = 2A\sin kx\cos\omega t$: nodes $\lambda/2$ apart, node-to-antinode $\lambda/4$.
| System | Allowed frequencies | Harmonics present |
|---|---|---|
| String fixed at both ends | $f_n = \dfrac{nv}{2L}$ | all ($n = 1, 2, 3, \dots$) |
| Open pipe (both ends open) | $f_n = \dfrac{nv}{2L}$ | all |
| Closed pipe (one end closed) | $f_n = \dfrac{(2n-1)v}{4L}$ | odd only (1, 3, 5, …) |

End correction $e \approx 0.6r$: closed pipe $L \to L + e$; open pipe $L \to L + 2e$.
**Resonance tube:** $\lambda = 2(L_2 - L_1)$, end correction $e = \dfrac{L_2 - 3L_1}{2}$.
**Beats:** $f_{beat} = |f_1 - f_2|$. Loading a fork with wax **lowers** its frequency; filing its prongs **raises** it.
:::

@@GRAPH standing-waves

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Period of a system:** springs in combination, pendulum in an accelerating frame, liquid columns.
2. **SHM energy:** where $K = U$; speed at a given displacement; phase from given $x$ and $v$.
3. **Wave equation reading:** find $v$, $\lambda$, $f$, direction and particle velocity from $y(x,t)$.
4. **Organ pipes and strings:** harmonics, overtones, open vs closed comparisons, resonance tube.
5. **Beats with wax/filing** to determine an unknown frequency.
6. **Superposition of two SHMs** in the same direction (resultant amplitude and phase).
:::

## Shortcuts

:::shortcut Overtone vs harmonic
For a closed pipe, the **first overtone is the 3rd harmonic**. For open pipes and strings, the first overtone is the 2nd harmonic. Translate the question's word before computing.
:::

:::shortcut Period by "restoring constant"
Write $F = -k_{eff}x$ (or $\tau = -\kappa\theta$). Then $T = 2\pi\sqrt{m/k_{eff}}$ (or $2\pi\sqrt{I/\kappa}$). Works for liquids, floating bodies and springs with pulleys.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| SHM formulas ($v_{max}$, $a_{max}$, energy) | E | 1 min |
| Spring combinations / pendulum variants | E–M | 1.5 min |
| Wave-equation reading | E | 1 min |
| Pipes and strings harmonics | M | 2 min |
| Beats with loading | M | 1.5 min |
| Composite SHM (pulley + spring, rolling + spring) | H | 3 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Closed pipe: only **odd** harmonics. Asked for the "second harmonic of a closed pipe"? It doesn't exist.
- Confusing $\mu$ (mass per unit **length**) with density.
- Using °C in $v \propto \sqrt T$.
- Wax lowers frequency. After deciding the sign of the change, check which way the beats moved.
- The spring–mass period is independent of $g$. The pendulum period is independent of mass.
:::

## Practice questions

@@SET P10 · Practice

@@Q P10-01 | E | 0.75 | Maximum speed in SHM | Basic
A particle performs SHM with amplitude 10 cm and period 2 s. Its maximum speed is:
(A) $0.1\pi\ \text{m s}^{-1}$
(B) $0.2\pi\ \text{m s}^{-1}$
(C) $0.05\pi\ \text{m s}^{-1}$
(D) $\pi\ \text{m s}^{-1}$
@ans A
@sol $\omega = 2\pi/T = \pi$ rad/s; $v_{max} = A\omega = 0.1\pi \approx 0.314\ \text{m s}^{-1}$.
@short —
@trap Forgetting to convert cm to m.
@@END

@@Q P10-02 | E | 0.5 | Equal kinetic and potential energy | Speed
In SHM of amplitude $A$, kinetic energy equals potential energy at a displacement of:
(A) $A/2$
(B) $A/\sqrt2$
(C) $A/4$
(D) $\sqrt3A/2$
@ans B
@sol $\tfrac12k(A^2 - x^2) = \tfrac12kx^2 \Rightarrow x = A/\sqrt2$.
@short —
@trap Answering $A/2$.
@@END

@@Q P10-03 | M | 1 | Springs in series | Basic
A mass $m$ hangs from two springs of constants $k$ and $2k$ joined in series. The period of oscillation is:
(A) $2\pi\sqrt{3m/2k}$
(B) $2\pi\sqrt{m/3k}$
(C) $2\pi\sqrt{2m/3k}$
(D) $2\pi\sqrt{3m/k}$
@ans A
@sol $k_s = \dfrac{k\cdot2k}{3k} = \dfrac{2k}{3}$; $T = 2\pi\sqrt{m/k_s} = 2\pi\sqrt{3m/2k}$.
@short Series springs behave like parallel resistors.
@trap Adding them ($3k$), which is the parallel case.
@@END

@@Q P10-04 | M | 1 | Pendulum in accelerating lift | Concept
A simple pendulum has period $T$. In a lift accelerating **upward** at $g/3$, its period becomes:
(A) $\tfrac{\sqrt3}{2}T$
(B) $\tfrac{2}{\sqrt3}T$
(C) $\tfrac34T$
(D) $T$
@ans A
@sol $g_{eff} = g + g/3 = \tfrac43g$. $T' = T\sqrt{g/g_{eff}} = T\sqrt{3/4} = \tfrac{\sqrt3}{2}T$.
@short Upward acceleration raises $g_{eff}$, so the period gets shorter.
@trap Using $g - a$.
@@END

@@Q P10-05 | E | 0.75 | Wave speed on a string | NV
A string with linear mass density $0.01\ \text{kg m}^{-1}$ is under 100 N tension. Find the transverse wave speed (in m/s).
@ans 100
@sol $v = \sqrt{T/\mu} = \sqrt{10^4} = 100\ \text{m s}^{-1}$.
@short —
@trap —
@@END

@@Q P10-06 | M | 1.5 | Overtone of a closed pipe | Concept
A pipe closed at one end is 25 cm long, and the speed of sound is 340 m/s (ignore end correction). The frequency of its **first overtone** is:
(A) 680 Hz
(B) 1020 Hz
(C) 340 Hz
(D) 1360 Hz
@ans B
@sol Fundamental $= \dfrac{v}{4L} = \dfrac{340}{1} = 340$ Hz. The first overtone of a closed pipe is the 3rd harmonic: 1020 Hz.
@short Closed pipe: 1, 3, 5, … × fundamental.
@trap Taking the 2nd harmonic (680 Hz).
@@END

@@Q P10-07 | M | 1.5 | Beats with wax loading | Tricky
Fork A (256 Hz) and fork B give 4 beats per second. When B is loaded with a little wax, the beat frequency **decreases**. The original frequency of B was:
(A) 252 Hz
(B) 260 Hz
(C) 256 Hz
(D) 248 Hz
@ans B
@sol B is 252 or 260 Hz. Wax lowers B's frequency. If B were 252, lowering it would *increase* the beats. The beats decreased, so B = 260 Hz.
@short Wax pulls $f$ down. Fewer beats means $f_B$ was above $f_A$.
@trap Assuming wax raises the frequency.
@@END

@@Q P10-08 | E | 1 | Speed from wave equation | NV
A wave is described by $y = 0.02\sin[2\pi(10t - 0.5x)]$ (SI units). Find its speed (in m/s).
@ans 20
@sol $\omega = 20\pi$, $k = \pi$, so $v = \omega/k = 20\ \text{m s}^{-1}$ (towards $+x$).
@short $v$ = coefficient of $t$ ÷ coefficient of $x$ = $10/0.5$.
@trap Reading $\lambda = 0.5$ m. It is actually $1/0.5 = 2$ m, so the wrong reading gives 5 m/s.
@@END

@@Q P10-09 | M | 1.5 | Resonance tube | JEE
In a resonance-tube experiment with a 500 Hz fork, the first and second resonances occur at 16.0 cm and 50.0 cm. The speed of sound is:
(A) 330 m/s
(B) 340 m/s
(C) 350 m/s
(D) 320 m/s
@ans B
@sol $\lambda/2 = L_2 - L_1 = 34$ cm, so $\lambda = 0.68$ m and $v = f\lambda = 340\ \text{m s}^{-1}$. (End correction $= (L_2 - 3L_1)/2 = 1$ cm.)
@short The difference between successive resonances is always $\lambda/2$, so the end correction cancels.
@trap Using $4L_1$ as $\lambda$ gives 320 m/s.
@@END

@@Q P10-10 | E | 1 | Standing wave on a string | Basic
A 1 m string fixed at both ends vibrates in 3 loops at 300 Hz. The wave speed on the string is:
(A) 100 m/s
(B) 200 m/s
(C) 300 m/s
(D) 600 m/s
@ans B
@sol 3 loops means $3\lambda/2 = 1$ m, so $\lambda = 2/3$ m. $v = 300\times\tfrac23 = 200\ \text{m s}^{-1}$.
@short $f_1 = 100$ Hz $= v/2L$, so $v = 200$.
@trap Taking $\lambda = L/3$.
@@END

@@SET P10 · Chapter Test

@@Q P10-T1 | E | 0.5 | Maximum acceleration | Speed
The maximum acceleration of a particle in SHM with $A = 5$ cm and $\omega = 10$ rad/s is:
(A) $0.5\ \text{m s}^{-2}$
(B) $5\ \text{m s}^{-2}$
(C) $50\ \text{m s}^{-2}$
(D) $0.05\ \text{m s}^{-2}$
@ans B
@sol $a_{max} = \omega^2A = 100\times0.05 = 5\ \text{m s}^{-2}$.
@short —
@trap —
@@END

@@Q P10-T2 | E | 0.5 | Sound speed vs temperature | Speed
If the absolute temperature of air is made 4 times larger, the speed of sound in it becomes:
(A) 4 times
(B) 2 times
(C) 16 times
(D) unchanged
@ans B
@sol $v \propto \sqrt T$.
@short —
@trap —
@@END

@@Q P10-T3 | M | 1 | Cutting a spring | Concept
A mass on a spring has period $T$. The spring is cut into two equal halves and the same mass is hung from one half. The new period is:
(A) $T/2$
(B) $T/\sqrt2$
(C) $\sqrt2T$
(D) $2T$
@ans B
@sol Each half has spring constant $2k$, so $T' = 2\pi\sqrt{m/2k} = T/\sqrt2$.
@short $k \propto 1/\text{length}$.
@trap Thinking a shorter spring is "weaker".
@@END

@@Q P10-T4 | E | 0.5 | Beat frequency | NV
Two sources of 510 Hz and 514 Hz sound together. Find the number of beats heard per second.
@ans 4
@sol $|514 - 510| = 4$.
@short —
@trap —
@@END

@@Q P10-T5 | E | 0.75 | Open vs closed pipe | Basic
An open pipe and a closed pipe have the same length. The ratio of their fundamental frequencies (open : closed) is:
(A) 1 : 2
(B) 2 : 1
(C) 1 : 1
(D) 4 : 1
@ans B
@sol Open: $v/2L$. Closed: $v/4L$. Ratio 2 : 1.
@short —
@trap —
@@END

## Answers & Solutions {#p10-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Oscillations & Waves
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
