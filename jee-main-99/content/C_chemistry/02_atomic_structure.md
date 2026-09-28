# Atomic Structure {#c02}

:::stats
Typical questions | 1–2 per shift
Difficulty | Easy–Medium
Priority | Must-do
NCERT | Class 11 · Ch 2
Study time | ~7 hours
:::

## Important concepts

- **Electromagnetic radiation:** $c = \nu\lambda$, wavenumber $\bar\nu = 1/\lambda$. Planck's quantum: $E = h\nu$. The photoelectric effect supports the particle nature of light.
- **Bohr model** (one-electron species): quantised orbits. It explains the hydrogen spectrum but fails for multi-electron atoms, the Zeeman/Stark effects and the uncertainty principle.
- **Dual nature:** $\lambda = h/mv$ (de Broglie). **Heisenberg:** $\Delta x\cdot\Delta p \ge h/4\pi$, so exact orbits are impossible. Hence orbitals.
- **Quantum-mechanical model:** $\psi$ is a one-electron wave function, and $\psi^2$ is the probability density. Orbitals are described by four quantum numbers.
- **Filling rules:** Aufbau ($n + l$ rule), Pauli exclusion, Hund's rule of maximum multiplicity. Half-filled and fully filled subshells give extra stability.

## Formula sheet

:::formula Spectra & Bohr model
$$E_n = -2.18\times10^{-18}\frac{Z^2}{n^2}\ \text{J} = -13.6\frac{Z^2}{n^2}\ \text{eV} \qquad r_n = 52.9\frac{n^2}{Z}\ \text{pm} \qquad v_n = 2.18\times10^6\frac Zn\ \text{m s}^{-1}$$
$$\bar\nu = \frac1\lambda = R_HZ^2\left(\frac1{n_1^2} - \frac1{n_2^2}\right) \qquad R_H = 109\,677\ \text{cm}^{-1} \qquad \text{lines} = \frac{(n_2 - n_1)(n_2 - n_1 + 1)}{2}$$
Series: Lyman ($n_1 = 1$, UV), Balmer (2, visible), Paschen (3), Brackett (4), Pfund (5) (IR).
:::

:::formula Quantum-mechanical results
$$\lambda = \frac hp \qquad \Delta x\,\Delta p \ge \frac{h}{4\pi} \qquad \text{orbital angular momentum} = \sqrt{l(l+1)}\frac{h}{2\pi} \qquad \mu_{spin} = \sqrt{n(n+2)}\ \text{BM}$$
Radial nodes $= n - l - 1$; angular nodes $= l$; total nodes $= n - 1$.
Maximum electrons: shell $2n^2$; subshell $2(2l + 1)$; orbital 2. Orbitals in a shell $= n^2$.
:::

:::formula Quantum numbers
| Symbol | Name | Values | Determines |
|---|---|---|---|
| $n$ | principal | 1, 2, 3, … | size, energy (for H) |
| $l$ | azimuthal | 0 … $(n - 1)$ | shape (s, p, d, f) |
| $m_l$ | magnetic | $-l$ … $+l$ | orientation |
| $m_s$ | spin | $\pm\tfrac12$ | spin |
:::

## Electronic configuration: rules and exceptions

- **Order ($n + l$ rule):** 1s 2s 2p 3s 3p **4s 3d** 4p 5s 4d 5p 6s 4f 5d 6p … For equal $n + l$, the lower $n$ fills first.
- **Anomalies to memorise:** Cr $[\text{Ar}]3d^54s^1$, Cu $[\text{Ar}]3d^{10}4s^1$. Similar: Mo $4d^55s^1$, Ag $4d^{10}5s^1$, Au $5d^{10}6s^1$, Pd $4d^{10}5s^0$.
- **Ions of d-block elements lose 4s electrons first:** $\ce{Fe^{2+}}$ is $[\text{Ar}]3d^6$ and $\ce{Fe^{3+}}$ is $[\text{Ar}]3d^5$.

@@GRAPH radial-probability

:::important ψ² plots (NCERT)
For 1s, $\psi^2$ is maximum at the nucleus and decays. For 2s, $\psi^2$ has **one radial node**. The *radial probability* $4\pi r^2\psi^2$ for 1s peaks at $a_0 = 52.9$ pm. The $\mathrm{d}_{z^2}$ orbital has two lobes and a ring (torus). The other four d orbitals have four lobes each.
:::

## Common traps

:::trap Mistake alerts
- $l$ can't equal $n$: "3f" and "2d" don't exist.
- Using the **atomic** configuration for ions: remove 4s electrons before 3d.
- Unpaired electrons in Cr: **6** (3d⁵4s¹), not 4.
- The Heisenberg product uses $h/4\pi$ (NCERT). Some books use $\hbar/2$, which is the same value.
- Wavenumber in cm⁻¹ vs m⁻¹: $R_H = 1.097\times10^7\ \text{m}^{-1}$.
:::

## Question patterns

:::pyq Recurring structures
1. Valid/invalid quantum-number sets; number of electrons with given $n$, $l$, $m_l$, $m_s$.
2. Nodes of orbitals (radial/angular/total).
3. Bohr energies, radii, wavelengths for H, He⁺, Li²⁺; number of spectral lines.
4. de Broglie / Heisenberg numericals.
5. Configurations and magnetic moments of ions (feeds into d-block and coordination questions).
:::

## Practice questions

@@SET C02 · Practice

@@Q C02-01 | E | 0.5 | Allowed quantum numbers | Speed
Which set of quantum numbers is **not** allowed?
(A) $n = 2, l = 1, m_l = 0, m_s = +\tfrac12$
(B) $n = 3, l = 3, m_l = 1, m_s = -\tfrac12$
(C) $n = 4, l = 2, m_l = -2, m_s = +\tfrac12$
(D) $n = 1, l = 0, m_l = 0, m_s = -\tfrac12$
@ans B
@sol $l$ must be ≤ $n - 1$. With $n = 3$, $l = 3$ is impossible.
@short —
@trap —
@@END

@@Q C02-02 | E | 0.5 | Capacity of a subshell | Speed
The maximum number of electrons that can have $n = 3$ and $l = 2$ is:
(A) 2
(B) 6
(C) 10
(D) 18
@ans C
@sol $l = 2$ is a d subshell: $2(2l + 1) = 10$.
@short —
@trap Answering 18 (the whole shell).
@@END

@@Q C02-03 | M | 1 | Wavelength of H-α | Calc
The wavelength emitted when the electron in a hydrogen atom falls from $n = 3$ to $n = 2$ is about:
(A) 486 nm
(B) 656 nm
(C) 122 nm
(D) 1875 nm
@ans B
@sol $\Delta E = 13.6\left(\tfrac14 - \tfrac19\right) = 13.6\times\tfrac5{36} \approx 1.89$ eV; $\lambda = 1240/1.89 \approx 656$ nm.
@short The first Balmer line is red, at 656 nm.
@trap Using $n_1 = 1$ (Lyman).
@@END

@@Q C02-04 | M | 1.5 | Uncertainty principle | Calc
An electron's position is known to within 1 Å. The minimum uncertainty in its velocity is about ($m_e = 9.1\times10^{-31}$ kg, $h = 6.626\times10^{-34}$ J s):
(A) $5.8\times10^5$ m/s
(B) $5.8\times10^3$ m/s
(C) $1.2\times10^6$ m/s
(D) $5.8\times10^7$ m/s
@ans A
@sol $\Delta v = \dfrac{h}{4\pi m\Delta x} = \dfrac{6.626\times10^{-34}}{4\pi\times9.1\times10^{-31}\times10^{-10}} \approx 5.8\times10^5$ m/s.
@short $4\pi\times9.1 \approx 114$.
@trap Using $h/2\pi$ gives about $1.2\times10^6$.
@@END

@@Q C02-05 | E | 0.5 | Total nodes | NV
Find the total number of nodes in a 4d orbital.
@ans 3
@sol Total $= n - 1 = 3$ (radial $4 - 2 - 1 = 1$, angular 2).
@short —
@trap Counting only radial nodes (1).
@@END

@@Q C02-06 | E | 0.5 | Anomalous configuration | Speed
The ground-state electronic configuration of copper ($Z = 29$) is:
(A) $[\text{Ar}]3d^94s^2$
(B) $[\text{Ar}]3d^{10}4s^1$
(C) $[\text{Ar}]3d^{10}4s^2$
(D) $[\text{Ar}]3d^84s^2 4p^1$
@ans B
@sol A completely filled 3d subshell gives extra stability.
@short —
@trap Applying Aufbau blindly (A).
@@END

@@Q C02-07 | E | 0.75 | Orbital angular momentum | Basic
The orbital angular momentum of an electron in a d orbital is:
(A) $\sqrt2\,\dfrac{h}{2\pi}$
(B) $\sqrt6\,\dfrac{h}{2\pi}$
(C) $2\,\dfrac{h}{2\pi}$
(D) $\sqrt{12}\,\dfrac{h}{2\pi}$
@ans B
@sol $\sqrt{l(l+1)}\,\hbar$ with $l = 2$: $\sqrt6\,\hbar$.
@short —
@trap Using Bohr's $n h/2\pi$.
@@END

@@Q C02-08 | E | 0.75 | Spin-only magnetic moment | Basic
The spin-only magnetic moment of $\ce{Fe^{2+}}$ is about:
(A) 2.83 BM
(B) 3.87 BM
(C) 4.90 BM
(D) 5.92 BM
@ans C
@sol $\ce{Fe^{2+}}$: $3d^6$ with 4 unpaired electrons (free ion). $\sqrt{4\times6} = \sqrt{24} \approx 4.90$ BM.
@short Memorise $\sqrt{n(n+2)}$: 1.73, 2.83, 3.87, 4.90, 5.92 for $n$ = 1–5.
@trap Removing 3d before 4s electrons.
@@END

@@Q C02-09 | E | 0.5 | Unpaired electrons in an ion | NV
How many unpaired electrons are there in a gaseous $\ce{Mn^{2+}}$ ion ($Z = 25$)?
@ans 5
@sol Mn is $[\text{Ar}]3d^54s^2$, so $\ce{Mn^{2+}}$ is $3d^5$: 5 unpaired electrons.
@short —
@trap —
@@END

@@SET C02 · Chapter Test

@@Q C02-T1 | E | 0.5 | (n + l) rule | Speed
Which orbital is filled first?
(A) 3d
(B) 4s
(C) 4p
(D) they fill together
@ans B
@sol $n + l$: 4s = 4, 3d = 5, 4p = 5. The lowest value fills first.
@short —
@trap —
@@END

@@Q C02-T2 | E | 0.5 | Energy of the second orbit | Speed
The energy of an electron in the second Bohr orbit of hydrogen is:
(A) −13.6 eV
(B) −3.4 eV
(C) −1.51 eV
(D) −6.8 eV
@ans B
@sol $-13.6/4 = -3.4$ eV.
@short —
@trap —
@@END

@@Q C02-T3 | E | 0.5 | Shell capacity | NV
Find the maximum number of electrons that can be accommodated in the shell with $n = 4$.
@ans 32
@sol $2n^2 = 32$.
@short —
@trap —
@@END

@@Q C02-T4 | E | 0.5 | Spherical orbital | Concept
Which orbital is spherically symmetric (non-directional)?
(A) $p_x$
(B) $d_{z^2}$
(C) s
(D) $d_{xy}$
@ans C
@sol s orbitals have $l = 0$, so there are no angular nodes and no directional dependence.
@short —
@trap —
@@END

@@Q C02-T5 | E | 0.5 | Hund's rule | Concept
According to Hund's rule, the three 2p electrons of nitrogen are arranged as:
(A) two paired, one unpaired
(B) all three unpaired, with parallel spins
(C) all three in one orbital
(D) all three unpaired, with alternating spins
@ans B
@sol Degenerate orbitals are singly occupied, with parallel spins, before any pairing.
@short —
@trap —
@@END

## Answers & Solutions {#c02-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Atomic Structure
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
