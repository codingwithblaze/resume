# Atoms & Nuclei {#p18}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy
Priority | Must-do (easy marks)
NCERT | Class 12 · Ch 12, 13
Study time | ~6 hours
:::

## Concept summary

- **Rutherford's α-scattering:** most α-particles pass straight through gold foil, and a few bounce back. So an atom is mostly empty space, with a tiny, dense, positive nucleus.
- **Bohr's model** (for H-like atoms) quantises angular momentum, $mvr = nh/2\pi$. It gives discrete orbits and energies, and explains the hydrogen spectrum.
- A **nucleus** of $Z$ protons and $N$ neutrons weighs **less** than its parts. The **mass defect** is the binding energy, $\Delta mc^2$.
- **Binding energy per nucleon** peaks near $A \approx 56$. Heavy nuclei release energy by **fission** and light ones by **fusion**.

:::warning Syllabus note
The 2024–2026 syllabus text for Unit 18 lists α-scattering, Rutherford and Bohr models, the hydrogen spectrum, nuclear composition and size, mass–energy relation, mass defect, BE/A, fission and fusion. **Radioactivity (decay law, half-life, α/β/γ properties) is not listed** [NTA-SYL]. Give it a short read only.
:::

## Formulas: Atoms

:::formula Bohr model (hydrogen-like ion, atomic number $Z$)
$$r_n = 0.529\frac{n^2}{Z}\ \text{Å} \qquad v_n = 2.18\times10^6\frac Zn\ \text{m s}^{-1} \qquad E_n = -13.6\frac{Z^2}{n^2}\ \text{eV}$$
$$K = -E \qquad U = 2E \qquad mvr = \frac{nh}{2\pi} \qquad 2\pi r_n = n\lambda_{dB}$$
Scaling: $r \propto n^2/Z$, $v \propto Z/n$, $E \propto Z^2/n^2$, time period $\propto n^3/Z^2$.
**Rutherford closest approach** of an α-particle with kinetic energy $K$: $d = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2Ze^2}{K}$.
:::

:::formula Hydrogen spectrum
$$\frac1\lambda = RZ^2\left(\frac1{n_1^2} - \frac1{n_2^2}\right) \qquad R = 1.097\times10^7\ \text{m}^{-1} \qquad \Delta E = h\nu$$
| Series | $n_1$ | Region |
|---|---|---|
| Lyman | 1 | ultraviolet |
| Balmer | 2 | visible |
| Paschen | 3 | infrared |
| Brackett | 4 | infrared |
| Pfund | 5 | infrared |

- Lines from level $n$ down to ground: $\dfrac{n(n-1)}{2}$.
- Ionisation energy of H: 13.6 eV. Excitation energies: 10.2 eV ($1\to2$), 12.09 eV ($1\to3$).
- Lyman series limit $\approx 91$ nm; Balmer limit $\approx 365$ nm; first Balmer line (H-α) $\approx 656$ nm.
- **Bohr's limitations:** works only for single-electron atoms; can't explain line intensities or fine structure.
:::

## Formulas: Nuclei

:::formula Size, mass defect, binding energy
$$R = R_0A^{1/3},\ R_0 \approx 1.2\ \text{fm} \qquad \rho_{nucleus} \approx 2.3\times10^{17}\ \text{kg m}^{-3}\ \text{(independent of } A)$$
$$\Delta m = [Zm_p + (A - Z)m_n] - M_{nucleus} \qquad BE = \Delta m\,c^2 \qquad 1\ \text{u} = 931.5\ \text{MeV}/c^2$$
$$Q\text{-value} = \left(\sum m_{reactants} - \sum m_{products}\right)c^2 \qquad Q > 0 \Rightarrow \text{energy released}$$
- **Nuclear force:** strongest force, short range (a few fm), charge independent, saturates.
- **Fission:** $^{235}$U + n → two medium nuclei + 2–3 neutrons + ~200 MeV. **Fusion:** light nuclei combine (4 ¹H → ⁴He releases ~26.7 MeV in stars). Fusion needs very high temperatures to overcome Coulomb repulsion.
:::

@@GRAPH be-curve

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Bohr scaling** for H, He⁺, Li²⁺: radius, speed, energy, ratios between orbits.
2. **Spectral wavelengths:** ratio of first lines of two series, series limits, number of lines.
3. **Energy-level diagrams:** which transition emits the longest/shortest wavelength.
4. **Binding energy/nucleon** from given masses; Q-values of reactions.
5. **Nuclear radius/density** scaling with $A$.
6. **Closest approach** in α-scattering.
:::

## Shortcuts

:::shortcut Wavelength ratios without R
$\lambda \propto \dfrac{1}{\left(\frac1{n_1^2} - \frac1{n_2^2}\right)}$. For the first lines: Lyman $\propto 4/3$, Balmer $\propto 36/5$, Paschen $\propto 144/7$. Take ratios directly.
:::

:::shortcut BE/A curve reading
Anything that moves nucleons **towards the peak** at $A \approx 56$ releases energy. Energy released $= \sum(BE)_{products} - \sum(BE)_{reactants}$.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Bohr formulas | E | 45 s |
| Spectral lines / ratios | E | 1 min |
| BE per nucleon | E | 1 min |
| Q-value | E–M | 1.5 min |
| Closest approach | M | 1.5 min |

## Common mistakes

:::trap Mistake alerts
- Using $Z$ instead of $Z^2$ in energy scaling.
- The **longest** wavelength in a series is its **first** line (smallest $\Delta E$).
- Mass defect uses the **nucleus** mass. If atomic masses are given, electron masses cancel only when you use hydrogen-atom masses for the protons.
- Converting u to MeV with 931 **before** multiplying by the mass defect in u.
:::

## Practice questions

@@SET P18 · Practice

@@Q P18-01 | E | 0.75 | Bohr radius scaling | Basic
The radius of the first Bohr orbit of hydrogen is 0.53 Å. The radius of the $n = 3$ orbit of $\ce{Li^{2+}}$ is:
(A) 0.53 Å
(B) 1.59 Å
(C) 4.77 Å
(D) 0.18 Å
@ans B
@sol $r = 0.53\times\dfrac{n^2}{Z} = 0.53\times\dfrac93 = 1.59$ Å.
@short —
@trap Using $n$ instead of $n^2$.
@@END

@@Q P18-02 | E | 0.5 | Energy in He⁺ | Speed
The energy of the electron in the $n = 2$ state of $\ce{He+}$ is:
(A) −3.4 eV
(B) −13.6 eV
(C) −54.4 eV
(D) −6.8 eV
@ans B
@sol $E = -13.6\times\dfrac{Z^2}{n^2} = -13.6\times\dfrac44 = -13.6$ eV.
@short —
@trap Using $Z$ instead of $Z^2$ (−6.8).
@@END

@@Q P18-03 | M | 1 | Ratio of first lines | Concept
The ratio of the wavelength of the first line of the Balmer series to that of the first line of the Lyman series in hydrogen is:
(A) 27 : 5
(B) 5 : 27
(C) 4 : 1
(D) 9 : 4
@ans A
@sol $\dfrac{\lambda_B}{\lambda_L} = \dfrac{1 - \tfrac14}{\tfrac14 - \tfrac19} = \dfrac{3/4}{5/36} = \dfrac{27}{5}$.
@short —
@trap Inverting the ratio.
@@END

@@Q P18-04 | E | 0.5 | Number of spectral lines | NV
Electrons in a sample of hydrogen are excited to $n = 5$. Find the maximum number of different spectral lines emitted as they return to the ground state.
@ans 10
@sol $\dfrac{n(n-1)}{2} = \dfrac{5\times4}{2} = 10$.
@short —
@trap Counting only direct jumps to $n = 1$ (4 lines).
@@END

@@Q P18-05 | E | 0.5 | Nuclear radius scaling | Speed
The ratio of the nuclear radii of nuclei with $A = 216$ and $A = 27$ is:
(A) 8
(B) 2
(C) 4
(D) $2^{1/3}$
@ans B
@sol $R \propto A^{1/3}$: $(216/27)^{1/3} = 8^{1/3} = 2$.
@short —
@trap —
@@END

@@Q P18-06 | E | 1 | Binding energy per nucleon | Calc
The mass defect of $^4_2\text{He}$ is 0.0304 u. Its binding energy per nucleon is about:
(A) 28.3 MeV
(B) 7.1 MeV
(C) 14.2 MeV
(D) 3.5 MeV
@ans B
@sol $BE = 0.0304\times931.5 \approx 28.3$ MeV. Per nucleon: $28.3/4 \approx 7.1$ MeV.
@short —
@trap Stopping at the total BE.
@@END

@@Q P18-07 | M | 1.5 | Distance of closest approach | Calc
A 5 MeV α-particle is aimed head-on at a gold nucleus ($Z = 79$). Its distance of closest approach is about:
(A) $4.5\times10^{-14}$ m
(B) $4.5\times10^{-15}$ m
(C) $2.3\times10^{-14}$ m
(D) $9.1\times10^{-14}$ m
@ans A
@sol $d = \dfrac{k(2e)(79e)}{K} = \dfrac{9\times10^9\times158\times(1.6\times10^{-19})^2}{5\times1.6\times10^{-13}} \approx 4.55\times10^{-14}$ m.
@short In MeV·fm units: $ke^2 = 1.44$ MeV fm, so $d = 1.44\times158/5 \approx 45.5$ fm.
@trap Forgetting the α-particle's charge 2e gives (C).
@@END

@@Q P18-08 | E | 0.5 | Ionisation energy of Li²⁺ | NV
Find the ionisation energy (in eV, nearest integer) of $\ce{Li^{2+}}$ in its ground state.
@ans 122
@sol $13.6\times Z^2 = 13.6\times9 = 122.4$ eV.
@short —
@trap —
@@END

@@Q P18-09 | E | 0.75 | Why fission releases energy | Concept
Fission of a heavy nucleus releases energy because:
(A) the products have a smaller binding energy per nucleon
(B) the products have a larger binding energy per nucleon
(C) the number of nucleons decreases
(D) neutrons are destroyed
@ans B
@sol Middle-mass nuclei are more tightly bound (higher BE/A). The increase in total binding energy is released.
@short —
@trap —
@@END

@@SET P18 · Chapter Test

@@Q P18-T1 | E | 0.5 | Balmer region | Speed
The Balmer series of hydrogen lies in the:
(A) ultraviolet
(B) visible
(C) infrared
(D) X-ray region
@ans B
@sol Transitions to $n = 2$ emit 656 nm to 365 nm, mostly visible.
@short —
@trap —
@@END

@@Q P18-T2 | E | 0.5 | Nuclear density | Concept
Nuclear density:
(A) increases with $A$
(B) decreases with $A$
(C) is nearly the same for all nuclei
(D) is maximum for $A \approx 56$
@ans C
@sol $R^3 \propto A$ and mass $\propto A$, so the density is constant.
@short —
@trap Confusing it with BE/A (D).
@@END

@@Q P18-T3 | E | 0.5 | Energy equivalent of 1 u | Speed
The energy equivalent of 1 atomic mass unit is about:
(A) 9.31 MeV
(B) 931.5 MeV
(C) 1.6 MeV
(D) 0.511 MeV
@ans B
@sol $1\ \text{u}\times c^2 \approx 931.5$ MeV. (0.511 MeV is the electron's rest energy.)
@short —
@trap —
@@END

@@Q P18-T4 | E | 0.75 | Lyman series limit | NV
Using $R = 1.097\times10^7\ \text{m}^{-1}$, find the series-limit wavelength of the Lyman series (in nm, nearest integer).
@ans 91
@sol $\lambda = 1/R = 9.116\times10^{-8}$ m $\approx 91$ nm.
@short —
@trap —
@@END

@@Q P18-T5 | E | 0.5 | Trends with n | Concept
In the Bohr model, as $n$ increases:
(A) KE increases and total energy decreases
(B) KE decreases and total energy increases (becomes less negative)
(C) both increase
(D) both decrease
@ans B
@sol $K \propto 1/n^2$ decreases; $E = -K$ rises towards 0.
@short —
@trap —
@@END

## Answers & Solutions {#p18-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Atoms & Nuclei
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
