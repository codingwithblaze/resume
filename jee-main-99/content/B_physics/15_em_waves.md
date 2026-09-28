# Electromagnetic Waves {#p15}

:::stats
Typical questions | ~1 per shift
Difficulty | Easy
Priority | Must-do (easy marks)
NCERT | Class 12 · Ch 8
Study time | ~3 hours
:::

## Concept summary

- Maxwell added the **displacement current** $I_d = \varepsilon_0\,d\Phi_E/dt$ to Ampère's law. A changing $E$ creates $B$, just as a changing $B$ creates $E$. Together they give self-sustaining **electromagnetic waves**.
- EM waves are **transverse**: $\vec E \perp \vec B \perp$ direction of travel ($\vec E\times\vec B$ points along the propagation). They need no medium, and in vacuum they travel at $c = 1/\sqrt{\mu_0\varepsilon_0}$.
- They carry energy and momentum, so they exert radiation pressure.
- The **spectrum** runs from radio to gamma rays. Only the wavelength or frequency differs.

## Formulas

:::formula EM wave relations
$$c = \frac1{\sqrt{\mu_0\varepsilon_0}} = 3\times10^8\ \text{m s}^{-1} \qquad \frac{E_0}{B_0} = c \qquad v_{medium} = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{\sqrt{\mu_r\varepsilon_r}}$$
$$u = \tfrac12\varepsilon_0E^2 + \frac{B^2}{2\mu_0}\ \text{(equal shares)} \qquad \langle u\rangle = \tfrac12\varepsilon_0E_0^2 \qquad I = \langle u\rangle c = \tfrac12\varepsilon_0cE_0^2$$
$$\text{momentum } p = \frac Uc \qquad \text{radiation pressure: } \frac Ic\ \text{(absorbed)},\ \frac{2I}{c}\ \text{(reflected)} \qquad I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$
Inside the gap of a charging capacitor, the displacement current equals the conduction current in the wires.
:::

## The electromagnetic spectrum (NCERT ranges)

| Type | Wavelength range | Produced by | Main uses |
|---|---|---|---|
| Radio | > 0.1 m | oscillating charges in antennas | radio/TV communication |
| Microwaves | 0.1 m – 1 mm | klystron, magnetron, Gunn diode | radar, microwave ovens, satellite links |
| Infrared | 1 mm – 700 nm | hot bodies, molecular vibrations | remote controls, night vision, greenhouse effect, physiotherapy |
| Visible | 700 nm – 400 nm | electron transitions in atoms | vision, photography |
| Ultraviolet | 400 nm – 1 nm | very hot bodies (Sun), discharge lamps | sterilisation, water purification, LASIK; mostly absorbed by ozone |
| X-rays | 1 nm – $10^{-3}$ nm | X-ray tubes (fast electrons hitting metal) | medical imaging, crystallography |
| Gamma rays | < $10^{-3}$ nm | radioactive nuclei | cancer therapy, nuclear physics |

:::shortcut Memory order
"**R**aman's **M**other **I**nvited **V**ery **U**nusual e**X**tra **G**uests": increasing frequency, decreasing wavelength. Energy per photon increases along the same order.
:::

:::pyq Recurring structures
1. $E_0 \leftrightarrow B_0$ conversion, direction of $\vec B$ from a given $\vec E$ and propagation direction.
2. Intensity / energy density / radiation pressure numericals.
3. **Spectrum ordering** and matching uses (UV–sterilisation, IR–remote, microwave–radar).
4. Displacement current in a charging capacitor.
5. Speed in a medium from $\varepsilon_r$, $\mu_r$.
:::

:::trap Mistake alerts
- Energy is shared **equally** between the electric and magnetic fields, even though $B_0 = E_0/c$ looks small.
- Radiation pressure doubles for a perfectly reflecting surface.
- Direction: $\vec E\times\vec B$ gives the propagation direction. If $E$ is along $\hat x$ and the wave travels along $+\hat z$, then $B$ is along $+\hat y$.
:::

## Practice questions

@@SET P15 · Practice

@@Q P15-01 | E | 0.5 | E–B amplitude relation | Speed
An EM wave in vacuum has electric field amplitude 30 V/m. Its magnetic field amplitude is:
(A) $10^{-7}$ T
(B) $9\times10^9$ T
(C) $10^{-8}$ T
(D) $3\times10^{-7}$ T
@ans A
@sol $B_0 = E_0/c = 30/(3\times10^8) = 10^{-7}$ T.
@short —
@trap Multiplying by $c$.
@@END

@@Q P15-02 | E | 0.5 | Spectrum order | Speed
Which of the following has the shortest wavelength?
(A) X-rays
(B) microwaves
(C) γ-rays
(D) ultraviolet
@ans C
@sol Gamma rays lie at the high-frequency end of the spectrum.
@short —
@trap Choosing X-rays.
@@END

@@Q P15-03 | E | 0.5 | Displacement current | NV
A capacitor is charged by a steady 2 A current. Find the displacement current (in A) between its plates.
@ans 2
@sol Continuity of current: $I_d = I_c = 2$ A.
@short —
@trap Answering zero because "no charge crosses the gap".
@@END

@@Q P15-04 | M | 1 | Intensity from field amplitude | Calc
An EM wave has $E_0 = 100$ V/m. Its intensity is about ($\varepsilon_0 = 8.85\times10^{-12}$ SI):
(A) 13.3 W/m²
(B) 26.6 W/m²
(C) 1.33 W/m²
(D) 133 W/m²
@ans A
@sol $I = \tfrac12\varepsilon_0cE_0^2 = 0.5\times8.85\times10^{-12}\times3\times10^8\times10^4 \approx 13.3\ \text{W m}^{-2}$.
@short —
@trap Forgetting the $\tfrac12$ (26.6).
@@END

@@Q P15-05 | M | 1 | Field directions | Concept
An EM wave travels along $+z$ with $\vec E$ along $+x$. At that instant, $\vec B$ points along:
(A) $+y$
(B) $-y$
(C) $+z$
(D) $-x$
@ans A
@sol $\vec E\times\vec B$ must point along $+\hat z$: $\hat x\times\hat y = \hat z$, so $\vec B$ is along $+\hat y$.
@short —
@trap Using $\vec B\times\vec E$.
@@END

@@Q P15-06 | E | 0.75 | Identify the band | Basic
An EM wave has a wavelength of 3 cm. Its frequency and type are:
(A) 10 GHz, microwave
(B) 1 GHz, radio
(C) 100 GHz, infrared
(D) 10 MHz, radio
@ans A
@sol $f = c/\lambda = 3\times10^8/0.03 = 10^{10}$ Hz; 3 cm lies in the microwave band (1 mm – 0.1 m).
@short —
@trap —
@@END

@@SET P15 · Chapter Test

@@Q P15-T1 | E | 0.5 | Energy sharing | Concept
In an EM wave, the average energy density associated with the magnetic field is:
(A) greater than that of the electric field
(B) smaller than that of the electric field
(C) equal to that of the electric field
(D) zero
@ans C
@sol $\tfrac12\varepsilon_0E^2 = \dfrac{B^2}{2\mu_0}$ since $E = cB$ and $c^2 = 1/\mu_0\varepsilon_0$.
@short —
@trap —
@@END

@@Q P15-T2 | E | 0.5 | Uses of UV | Speed
The EM radiation used to sterilise surgical instruments is:
(A) infrared
(B) ultraviolet
(C) microwaves
(D) radio waves
@ans B
@sol UV kills bacteria by damaging their DNA.
@short —
@trap —
@@END

@@Q P15-T3 | E | 0.5 | Speed in a medium | Basic
The speed of EM waves in a non-magnetic medium with $\varepsilon_r = 4$ is:
(A) $3\times10^8$ m/s
(B) $1.5\times10^8$ m/s
(C) $0.75\times10^8$ m/s
(D) $6\times10^8$ m/s
@ans B
@sol $v = c/\sqrt{\varepsilon_r} = c/2$.
@short —
@trap Dividing by 4.
@@END

@@Q P15-T4 | E | 0.75 | Radiation pressure | NV
Radiation of intensity 900 W/m² falls normally on a perfectly absorbing surface. The pressure is $x\times10^{-6}$ Pa. Find $x$.
@ans 3
@sol $P = I/c = 900/(3\times10^8) = 3\times10^{-6}$ Pa.
@short —
@trap Using $2I/c$ (for a reflecting surface).
@@END

## Answers & Solutions {#p15-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · EM Waves
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
