# Dual Nature of Matter & Radiation {#p17}

:::stats
Typical questions | ~1 per shift
Difficulty | Easy
Priority | Must-do (easy marks)
NCERT | Class 12 · Ch 11
Study time | ~4 hours
:::

## Concept summary

- The **photoelectric effect** (observed by Hertz and Lenard, explained by Einstein) shows that light is absorbed in quanta: **photons** of energy $h\nu$.
- One photon ejects at most one electron. The electron's **maximum KE** depends on frequency, not intensity. Intensity controls the **number** of electrons, and so the photocurrent.
- **Matter has wave nature** (de Broglie): $\lambda = h/p$. This was confirmed by electron diffraction in the Davisson–Germer experiment.

## Formulas

:::formula Photons
$$E = h\nu = \frac{hc}{\lambda} \qquad hc \approx 1240\ \text{eV nm} \qquad p = \frac h\lambda = \frac Ec \qquad \text{photon flux } n = \frac{P}{h\nu} = \frac{P\lambda}{hc}$$
$h = 6.63\times10^{-34}$ J s; 1 eV $= 1.6\times10^{-19}$ J.
:::

:::formula Photoelectric effect
$$K_{max} = h\nu - \phi = eV_0 \qquad \nu_0 = \frac\phi h \qquad \lambda_0 = \frac{hc}{\phi} \qquad V_0 = \frac he\nu - \frac\phi e$$
| Change | Saturation current | Stopping potential $V_0$ | $K_{max}$ |
|---|---|---|---|
| Intensity ↑ (same $\nu$) | ↑ (proportional) | unchanged | unchanged |
| Frequency ↑ (same intensity) | about the same (fewer photons per joule) | ↑ | ↑ |
| $\nu < \nu_0$ | zero, whatever the intensity | — | — |

- Emission is **instantaneous** (no time lag), even for very weak light.
- The $V_0$ vs $\nu$ graph is a straight line with slope $h/e$ (**the same for every metal**) and $\nu$-intercept $\nu_0$.
:::

:::formula de Broglie waves
$$\lambda = \frac hp = \frac h{mv} = \frac{h}{\sqrt{2mK}} = \frac{h}{\sqrt{2mqV}}$$
- Electron through $V$ volts: $\lambda = \dfrac{1.227}{\sqrt V}$ nm.
- Thermal particle at temperature $T$: $\lambda = \dfrac{h}{\sqrt{3mk_BT}}$.
- Davisson–Germer: 54 V electrons diffracted by a nickel crystal, $\lambda \approx 0.167$ nm, matching de Broglie's prediction.
:::

@@GRAPH photoelectric

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. $K_{max}$, $V_0$, threshold wavelength for given $\lambda$ and $\phi$ (use 1240 eV nm).
2. **Graph questions:** $I$–$V$ for different intensities/frequencies; $V_0$–$\nu$ slope and intercept.
3. **Two-wavelength problems:** $V_1$, $V_2$ for $\lambda_1$, $\lambda_2$ → find $\phi$ or $h$.
4. **de Broglie wavelength ratios** for particles accelerated through the same potential, or with the same KE/momentum.
5. **Photon flux** from a source of given power.
:::

## Shortcuts

:::shortcut 1240 rule
$E(\text{eV}) = \dfrac{1240}{\lambda(\text{nm})}$. 620 nm → 2 eV, 400 nm → 3.1 eV, 310 nm → 4 eV, 248 nm → 5 eV.
**Time saved:** avoids $6.63\times10^{-34}\times3\times10^8$ arithmetic. **Common mistake:** using Å (divide by 10 first).
:::

:::shortcut de Broglie ratios
Same $V$: $\lambda \propto 1/\sqrt{mq}$. Same $K$: $\lambda \propto 1/\sqrt m$. Same $p$: equal $\lambda$.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Photon energy / flux | E | 45 s |
| Einstein equation numericals | E | 1 min |
| Graph interpretation | E | 45 s |
| Two-wavelength elimination | M | 1.5 min |
| de Broglie ratios | E | 1 min |

## Common mistakes

:::trap Mistake alerts
- Thinking higher intensity gives faster electrons. It gives **more** electrons.
- Using $\lambda$ in Å with 1240 (which needs nm).
- For de Broglie of a charged particle through $V$, forgetting the charge $q$ (α-particle: $q = 2e$).
- Stopping potential in volts = $K_{max}$ in eV, numerically. Don't multiply by $e$ again.
:::

## Practice questions

@@SET P17 · Practice

@@Q P17-01 | E | 0.5 | Photon energy | Speed
The energy of a photon of wavelength 620 nm is about:
(A) 1 eV
(B) 2 eV
(C) 3.1 eV
(D) 0.5 eV
@ans B
@sol $E = 1240/620 = 2$ eV.
@short —
@trap —
@@END

@@Q P17-02 | E | 1 | Stopping potential | Basic
Light of 400 nm falls on a metal with work function 2.3 eV. The stopping potential is:
(A) 0.8 V
(B) 3.1 V
(C) 2.3 V
(D) 5.4 V
@ans A
@sol $h\nu = 1240/400 = 3.1$ eV; $K_{max} = 0.8$ eV, so $V_0 = 0.8$ V.
@short —
@trap Adding the work function.
@@END

@@Q P17-03 | E | 0.75 | Threshold wavelength | NV
A metal has work function 4.13 eV. Find its threshold wavelength (in nm). Take $hc = 1240$ eV nm and give the nearest integer.
@ans 300
@sol $\lambda_0 = hc/\phi = 1240/4.13 \approx 300$ nm.
@short —
@trap —
@@END

@@Q P17-04 | E | 0.5 | Effect of intensity | Concept
The intensity of light on a photo-cell is doubled at the same frequency. Then:
(A) the stopping potential doubles
(B) the saturation current doubles and the stopping potential stays the same
(C) both double
(D) neither changes
@ans B
@sol Twice as many photons eject twice as many electrons, but each electron's maximum energy is unchanged.
@short —
@trap Choosing (A).
@@END

@@Q P17-05 | E | 0.75 | Electron de Broglie wavelength | Basic
An electron is accelerated from rest through 100 V. Its de Broglie wavelength is about:
(A) 1.23 nm
(B) 0.123 nm
(C) 12.3 nm
(D) 0.0123 nm
@ans B
@sol $\lambda = 1.227/\sqrt{100}$ nm $= 0.1227$ nm $\approx 1.23$ Å.
@short —
@trap Forgetting the square root.
@@END

@@Q P17-06 | M | 1 | de Broglie ratio: proton vs α | Concept
A proton and an α-particle are accelerated from rest through the same potential difference. The ratio $\lambda_p : \lambda_\alpha$ is:
(A) $2\sqrt2 : 1$
(B) $1 : 2\sqrt2$
(C) $2 : 1$
(D) $1 : 1$
@ans A
@sol $\lambda \propto 1/\sqrt{mq}$: $\dfrac{\lambda_p}{\lambda_\alpha} = \sqrt{\dfrac{m_\alpha q_\alpha}{m_pq_p}} = \sqrt{4\times2} = 2\sqrt2$.
@short —
@trap Ignoring the charge ($\sqrt4 = 2$).
@@END

@@Q P17-07 | E | 0.5 | Slope of V₀–ν graph | Concept
The slope of the stopping potential vs frequency graph for a photoelectric metal is:
(A) $h$
(B) $h/e$
(C) $e/h$
(D) $\phi/e$
@ans B
@sol $V_0 = \dfrac he\nu - \dfrac\phi e$. The slope is $h/e$, the same for all metals.
@short —
@trap —
@@END

@@Q P17-08 | M | 1 | Photon flux | Calc
A 10 W source emits light of wavelength 662 nm. The number of photons it emits per second is about ($h = 6.62\times10^{-34}$ J s):
(A) $3.3\times10^{19}$
(B) $3.3\times10^{18}$
(C) $1.0\times10^{20}$
(D) $6.6\times10^{19}$
@ans A
@sol $n = \dfrac{P\lambda}{hc} = \dfrac{10\times662\times10^{-9}}{6.62\times10^{-34}\times3\times10^8} = \dfrac{6.62\times10^{-6}}{1.986\times10^{-25}} \approx 3.3\times10^{19}\ \text{s}^{-1}$.
@short Photon energy $\approx 1240/662 \approx 1.87$ eV $\approx 3\times10^{-19}$ J; $10/(3\times10^{-19}) \approx 3.3\times10^{19}$.
@trap Powers-of-ten slips.
@@END

@@SET P17 · Chapter Test

@@Q P17-T1 | E | 0.5 | Time lag | Concept
In the photoelectric effect, the time lag between incidence of light and emission of electrons is:
(A) about 1 s
(B) negligible (< $10^{-9}$ s)
(C) proportional to intensity
(D) inversely proportional to frequency
@ans B
@sol Each photon transfers its energy to one electron at once.
@short —
@trap —
@@END

@@Q P17-T2 | E | 0.5 | Photon momentum | Speed
A photon of energy $E$ has momentum:
(A) $E/c$
(B) $Ec$
(C) $E/c^2$
(D) $\sqrt{2mE}$
@ans A
@sol $p = h/\lambda = h\nu/c = E/c$.
@short —
@trap Using the massive-particle formula (D).
@@END

@@Q P17-T3 | E | 0.5 | Accelerating voltage from wavelength | NV
An electron's de Broglie wavelength after acceleration through $V$ volts is 0.1227 nm. Find $V$.
@ans 100
@sol $0.1227 = 1.227/\sqrt V \Rightarrow \sqrt V = 10 \Rightarrow V = 100$ V.
@short —
@trap —
@@END

@@Q P17-T4 | M | 1 | Electron vs photon, same λ | Concept
An electron and a photon have the same wavelength, 0.1 nm. Then:
(A) they have equal energies
(B) the photon has more energy than the electron's kinetic energy
(C) the electron's KE is greater
(D) they have different momenta
@ans B
@sol The momenta are equal ($h/\lambda$). Photon: $E = pc \approx 12.4$ keV. Electron: $K = p^2/2m \approx 150$ eV. The photon's energy is much larger.
@short Same $\lambda$ ⇒ same $p$; $pc \gg p^2/2m$ when $v \ll c$.
@trap Choosing (D).
@@END

## Answers & Solutions {#p17-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Dual Nature
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
