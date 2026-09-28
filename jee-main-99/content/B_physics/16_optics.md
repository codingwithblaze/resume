# Optics: Ray & Wave {#p16}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 12 · Ch 9, 10
Study time | ~16 hours
:::

## Concept summary

- **Ray optics** treats light as rays. It covers reflection (mirrors), refraction (Snell's law, lenses, prisms), total internal reflection and optical instruments.
- **Wave optics** treats light as a wave. It covers Huygens' principle, interference (YDSE), diffraction (single slit) and polarisation (Malus, Brewster).
- **Sign convention (Cartesian):** distances are measured from the pole or optical centre. Positive means in the direction of the incident light, negative means against it. Heights are positive upward.

## Formulas: Ray optics

:::formula Mirrors & refraction
$$\frac1v + \frac1u = \frac1f \qquad f = \frac R2 \qquad m = -\frac vu$$
$$n_1\sin\theta_1 = n_2\sin\theta_2 \qquad n = \frac cv \qquad \text{apparent depth} = \frac{\text{real depth}}{n} \qquad \text{shift} = t\left(1 - \frac1n\right)$$
**Total internal reflection** (dense → rare, $i > C$): $\sin C = \dfrac{n_{rare}}{n_{dense}}$. Applications: optical fibres, totally reflecting prisms, sparkle of diamond, mirage.
Plane mirror rotated by $\theta$ → the reflected ray turns by $2\theta$. Two mirrors at angle $\theta$ form $\dfrac{360^\circ}{\theta} - 1$ images (when $360/\theta$ is even).
:::

:::formula Spherical surfaces & lenses
$$\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2 - n_1}{R} \qquad \frac1f = (n - 1)\left(\frac1{R_1} - \frac1{R_2}\right) \qquad \frac1v - \frac1u = \frac1f \qquad m = \frac vu$$
- Lens in a medium: replace $(n - 1)$ with $\left(\dfrac{n_{lens}}{n_{medium}} - 1\right)$. If $n_{lens} < n_{medium}$, a convex lens diverges.
- **Power** $P = \dfrac1{f\,(\text{m})}$ dioptre. **In contact:** $P = P_1 + P_2$. **Separated by $d$:** $P = P_1 + P_2 - dP_1P_2$.
- **Silvered lens** acts as a mirror with $P_{eq} = 2P_{lens} + P_{mirror}$. For a plano-convex lens (curved radius $R$): silvered on the **plane** face, $f = \dfrac{R}{2(n-1)}$; silvered on the **curved** face, $f = \dfrac{R}{2n}$.
- **Displacement method:** $f = \dfrac{D^2 - x^2}{4D}$ ($D$ = object–screen distance, $x$ = distance between the two lens positions). Needs $D \ge 4f$.
:::

:::formula Prism
$$A = r_1 + r_2 \qquad \delta = i + e - A \qquad n = \frac{\sin\frac{A + \delta_m}{2}}{\sin\frac A2} \qquad \text{thin prism: } \delta = (n - 1)A$$
At minimum deviation: $i = e$, $r_1 = r_2 = A/2$, and the ray passes symmetrically. The $\delta$–$i$ graph is U-shaped (see below). Dispersion: $\delta_v > \delta_r$ because $n_v > n_r$.
:::

@@GRAPH prism-deviation

:::formula Optical instruments ($D = 25$ cm)
| Instrument | Image at infinity (normal adjustment) | Image at $D$ |
|---|---|---|
| Simple microscope | $M = \dfrac Df$ | $M = 1 + \dfrac Df$ |
| Compound microscope | $M \approx \dfrac{L}{f_o}\cdot\dfrac{D}{f_e}$ | $M = m_o\left(1 + \dfrac D{f_e}\right)$ |
| Astronomical telescope | $M = \dfrac{f_o}{f_e}$, tube length $f_o + f_e$ | $M = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right)$ |

Telescope: large-aperture objective (more light, better resolution), short-$f$ eyepiece. **Reflecting telescopes** (Newtonian, Cassegrain) avoid chromatic aberration, and mirrors are easier to support than large lenses.
:::

## Formulas: Wave optics

:::formula Interference (YDSE)
$$\Delta x = d\sin\theta \approx \frac{yd}{D} \qquad \beta = \frac{\lambda D}{d} \qquad \text{bright: } \Delta x = n\lambda \qquad \text{dark: } \Delta x = (2n - 1)\frac\lambda2$$
$$I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi \qquad \text{equal slits: } I = 4I_0\cos^2\frac\phi2 \qquad \frac{I_{max}}{I_{min}} = \left(\frac{\sqrt{I_1} + \sqrt{I_2}}{\sqrt{I_1} - \sqrt{I_2}}\right)^2$$
- Apparatus immersed in a medium of index $n$: $\beta' = \beta/n$.
- A thin film (index $\mu$, thickness $t$) over one slit shifts the pattern **towards that slit** by $\dfrac{(\mu - 1)tD}{d}$. The number of fringes shifted is $\dfrac{(\mu - 1)t}{\lambda}$.
- Sustained interference needs **coherent** sources (constant phase difference).
:::

:::formula Diffraction (single slit, width $a$)
Minima: $a\sin\theta = n\lambda$ ($n = \pm1, \pm2, \dots$). Angular width of the central maximum $= \dfrac{2\lambda}{a}$; linear width $= \dfrac{2\lambda D}{a}$. Secondary maxima get rapidly weaker. Narrower slit → wider central maximum.
:::

:::formula Polarisation
**Malus's law:** $I = I_0\cos^2\theta$. Unpolarised light through one polaroid → $I_0/2$.
**Brewster's law:** $\tan\theta_B = n$; at $\theta_B$ the reflected light is completely polarised, and the reflected and refracted rays are **perpendicular**.
Polarisation proves light is **transverse**.
:::

@@GRAPH ydse-intensity

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Mirror/lens formula** with sign conventions: nature, position and size of the image.
2. **Lens maker's formula**, including a lens in a liquid, and combinations (contact/separated).
3. **TIR/critical angle**, apparent depth, glass slab shift.
4. **Prism minimum deviation**; thin-prism deviation.
5. **Microscope/telescope magnification** and tube length.
6. **YDSE:** fringe width changes (medium, $D$, $d$, $\lambda$), intensity at a point, thin-film shift, $I_{max}/I_{min}$.
7. **Single-slit width** of the central maximum; **Malus/Brewster** numericals.
:::

## Shortcuts

:::shortcut Image-nature table (concave mirror / convex lens)
| Object position | Image |
|---|---|
| beyond $2f$ ($C$) | between $f$ and $2f$, real, inverted, diminished |
| at $2f$ | at $2f$, real, inverted, same size |
| between $f$ and $2f$ | beyond $2f$, real, inverted, magnified |
| inside $f$ | virtual, erect, magnified |

Convex mirrors and concave lenses: **always virtual, erect, diminished**. This settles many MCQs without any calculation.
:::

:::shortcut Fringe-width checks
$\beta \propto \lambda D/d$. Any change → multiply the old fringe width by the ratios. For a medium: divide by $n$. Changing the slit **width** doesn't change $\beta$, only the intensity and visibility.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Mirror/lens formula | E | 1 min |
| Lens maker / lens in liquid | M | 1.5 min |
| Prism min deviation | E | 1 min |
| TIR / apparent depth | E | 1 min |
| Instruments | E | 1 min |
| YDSE fringe/intensity | E–M | 1.5 min |
| Thin film shift / multiple wavelengths coinciding | M | 2 min |
| Combined systems (lens + mirror, refraction at two surfaces) | H | 3 min (Round 2) |

## Common mistakes

:::trap Mistake alerts
- Sign convention: for a concave mirror $f < 0$. Object distance $u$ is **negative** for real objects.
- Lens formula has a **minus** ($1/v - 1/u$); mirror formula has a **plus**.
- Critical angle is defined only for dense → rare.
- The intensity after the first polaroid is $I_0/2$, **before** applying $\cos^2\theta$ at the second.
- In a medium, the wavelength changes but the frequency doesn't.
:::

## Practice questions

@@SET P16 · Practice

@@Q P16-01 | M | 1.5 | Concave mirror, object inside f | Concept
An object is 10 cm in front of a concave mirror of focal length 15 cm. The image is:
(A) 30 cm behind the mirror, virtual, erect, 3× magnified
(B) 30 cm in front, real, inverted, 3× magnified
(C) 6 cm behind, virtual, erect, diminished
(D) at infinity
@ans A
@sol $u = -10$, $f = -15$: $\dfrac1v = \dfrac1f - \dfrac1u = -\dfrac1{15} + \dfrac1{10} = \dfrac1{30}$, so $v = +30$ cm (behind the mirror). $m = -v/u = 3$: virtual, erect.
@short Object inside $f$ of a concave mirror → virtual, erect, magnified. Only (A) fits.
@trap Using $+15$ for $f$.
@@END

@@Q P16-02 | E | 0.5 | Critical angle | Speed
The critical angle for glass of refractive index $\sqrt2$ (against air) is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $90^\circ$
@ans B
@sol $\sin C = 1/\sqrt2 \Rightarrow C = 45^\circ$.
@short —
@trap —
@@END

@@Q P16-03 | M | 1.5 | Lens in water | JEE
A biconvex glass lens ($n = 1.5$) with both radii 20 cm has focal length 20 cm in air. Immersed in water ($n = 4/3$), its focal length becomes:
(A) 20 cm
(B) 40 cm
(C) 60 cm
(D) 80 cm
@ans D
@sol In water: $\dfrac1{f'} = \left(\dfrac{1.5}{4/3} - 1\right)\dfrac{2}{20} = 0.125\times0.1 \Rightarrow f' = 80$ cm.
@short $\dfrac{f'}{f} = \dfrac{n - 1}{n/n_m - 1} = \dfrac{0.5}{0.125} = 4$.
@trap Assuming $f$ is unchanged.
@@END

@@Q P16-04 | E | 1 | Lenses in contact | NV
A convex lens of focal length 20 cm is placed in contact with a concave lens of focal length 40 cm. Find the focal length (in cm) of the combination.
@ans 40
@sol $P = \dfrac{100}{20} - \dfrac{100}{40} = 5 - 2.5 = 2.5$ D, so $f = 40$ cm (converging).
@short —
@trap Adding focal lengths.
@@END

@@Q P16-05 | M | 1 | Minimum deviation | NV
A prism with $A = 60^\circ$ is made of glass with $n = \sqrt2$. Find its angle of minimum deviation (in degrees).
@ans 30
@sol $\sqrt2 = \dfrac{\sin\frac{60^\circ + \delta_m}{2}}{\sin30^\circ} \Rightarrow \sin\dfrac{60^\circ + \delta_m}{2} = \dfrac{\sqrt2}{2} \Rightarrow \dfrac{60^\circ + \delta_m}{2} = 45^\circ \Rightarrow \delta_m = 30^\circ$.
@short —
@trap Using the thin-prism formula: $(n - 1)A \approx 24.9^\circ$.
@@END

@@Q P16-06 | E | 0.75 | Apparent depth | Basic
A coin lies at the bottom of a tank filled with water ($n = 4/3$) to a depth of 12 cm. Viewed from above, the coin appears raised by:
(A) 9 cm
(B) 3 cm
(C) 4 cm
(D) 16 cm
@ans B
@sol Apparent depth $= 12/(4/3) = 9$ cm, so the rise is $12 - 9 = 3$ cm.
@short Shift $= t(1 - 1/n)$.
@trap Answering the apparent depth (9 cm).
@@END

@@Q P16-07 | E | 0.75 | YDSE fringe width | Calc
In YDSE, $d = 1$ mm, $D = 1$ m and $\lambda = 600$ nm. The fringe width is:
(A) 0.6 mm
(B) 6 mm
(C) 0.06 mm
(D) 1.2 mm
@ans A
@sol $\beta = \dfrac{\lambda D}{d} = \dfrac{6\times10^{-7}\times1}{10^{-3}} = 6\times10^{-4}$ m $= 0.6$ mm.
@short —
@trap —
@@END

@@Q P16-08 | M | 1 | Maximum to minimum intensity | NV
In YDSE the intensities from the two slits are in the ratio 9 : 1. Find $I_{max}/I_{min}$.
@ans 4
@sol Amplitude ratio 3 : 1. $\dfrac{I_{max}}{I_{min}} = \left(\dfrac{3+1}{3-1}\right)^2 = 4$.
@short Work with amplitudes ($\sqrt I$).
@trap Using intensities directly: $(9+1)/(9-1)$.
@@END

@@Q P16-09 | E | 1 | Single-slit central maximum | Basic
Light of 500 nm falls on a slit 0.2 mm wide, and the screen is 1 m away. The width of the central bright band is:
(A) 2.5 mm
(B) 5 mm
(C) 10 mm
(D) 1.25 mm
@ans B
@sol Width $= \dfrac{2\lambda D}{a} = \dfrac{2\times5\times10^{-7}}{2\times10^{-4}} = 5\times10^{-3}$ m.
@short —
@trap Forgetting the 2 (half-width).
@@END

@@Q P16-10 | M | 1 | Two polaroids | Concept
Unpolarised light of intensity $I_0$ passes through two polaroids whose axes are at $60^\circ$. The emerging intensity is:
(A) $I_0/2$
(B) $I_0/4$
(C) $I_0/8$
(D) $3I_0/8$
@ans C
@sol After the first: $I_0/2$. After the second: $\tfrac{I_0}{2}\cos^260^\circ = I_0/8$.
@short —
@trap Skipping the first halving ($I_0/4$).
@@END

@@Q P16-11 | E | 0.5 | Brewster's angle | Speed
The Brewster angle for glass of refractive index $\sqrt3$ is:
(A) $30^\circ$
(B) $45^\circ$
(C) $60^\circ$
(D) $90^\circ$
@ans C
@sol $\tan\theta_B = \sqrt3 \Rightarrow \theta_B = 60^\circ$.
@short —
@trap Using $\sin$ (critical-angle thinking).
@@END

@@Q P16-12 | E | 0.75 | Astronomical telescope | Basic
An astronomical telescope has $f_o = 100$ cm and $f_e = 5$ cm. In normal adjustment, its magnifying power and tube length are:
(A) 20, 105 cm
(B) 20, 95 cm
(C) 500, 105 cm
(D) 0.05, 105 cm
@ans A
@sol $M = f_o/f_e = 20$; $L = f_o + f_e = 105$ cm.
@short —
@trap —
@@END

@@SET P16 · Chapter Test

@@Q P16-T1 | E | 0.5 | Rotating a plane mirror | Speed
A plane mirror is rotated through $\theta$ while the incident ray stays fixed. The reflected ray turns through:
(A) $\theta$
(B) $2\theta$
(C) $\theta/2$
(D) 0
@ans B
@sol Both the angle of incidence and the angle of reflection change by $\theta$.
@short —
@trap —
@@END

@@Q P16-T2 | E | 0.5 | Speed of light in glass | Speed
The speed of light in glass of refractive index 1.5 is:
(A) $4.5\times10^8$ m/s
(B) $2\times10^8$ m/s
(C) $3\times10^8$ m/s
(D) $1.5\times10^8$ m/s
@ans B
@sol $v = c/n = 2\times10^8$ m/s.
@short —
@trap —
@@END

@@Q P16-T3 | E | 0.5 | Power of a lens | Speed
A lens has focal length −25 cm. Its power is:
(A) +4 D
(B) −4 D
(C) −0.04 D
(D) −25 D
@ans B
@sol $P = 1/f(\text{m}) = 1/(-0.25) = -4$ D (diverging).
@short —
@trap Using cm (−0.04).
@@END

@@Q P16-T4 | E | 0.75 | YDSE in water | Basic
A YDSE apparatus is immersed in water ($n = 4/3$). The fringe width becomes:
(A) $4/3$ of the original
(B) $3/4$ of the original
(C) unchanged
(D) $9/16$ of the original
@ans B
@sol $\lambda' = \lambda/n$, so $\beta' = \beta/n = \tfrac34\beta$.
@short —
@trap —
@@END

@@Q P16-T5 | E | 0.5 | Simple microscope | NV
A simple microscope has focal length 5 cm. Find its magnifying power when the image forms at the near point ($D = 25$ cm).
@ans 6
@sol $M = 1 + D/f = 1 + 5 = 6$.
@short —
@trap Using $D/f = 5$ (the normal-adjustment case).
@@END

@@Q P16-T6 | M | 1.5 | Film over one slit | JEE
A thin film of refractive index 1.5 placed over one slit of a YDSE shifts the central fringe by 5 fringe widths ($\lambda = 600$ nm). The film's thickness is:
(A) 3 μm
(B) 6 μm
(C) 2 μm
(D) 12 μm
@ans B
@sol Extra path $(\mu - 1)t = 5\lambda \Rightarrow t = \dfrac{5\times600\times10^{-9}}{0.5} = 6\times10^{-6}$ m.
@short —
@trap Using $\mu t$ instead of $(\mu - 1)t$ gives 2 μm.
@@END

## Answers & Solutions {#p16-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Optics
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
