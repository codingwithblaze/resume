# Properties of Solids & Liquids (incl. Thermal Properties) {#p07}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 8, 9, 10
Study time | ~14 hours
:::

## Concept summary

This unit bundles four mini-chapters, and each regularly gets a question:

1. **Elasticity:** stress, strain, the three moduli, stress–strain curve, elastic energy.
2. **Fluids:** pressure, Pascal's law, buoyancy, continuity, Bernoulli, viscosity (Stokes, terminal velocity).
3. **Surface tension:** surface energy, excess pressure, capillary rise, angle of contact.
4. **Thermal properties:** expansion, calorimetry, latent heat, conduction, radiation, Newton's law of cooling.

## Formulas: Elasticity

:::formula Moduli & energy
$$\text{Stress} = \frac FA \qquad \text{Strain} = \frac{\Delta L}{L} \qquad Y = \frac{FL}{A\,\Delta L} \qquad B = -\frac{\Delta P}{\Delta V/V} \qquad \eta_{rigidity} = \frac{F/A}{\theta}$$
- **Compressibility** $= 1/B$. **Poisson's ratio** $\sigma = -\dfrac{\text{lateral strain}}{\text{longitudinal strain}}$ (between 0 and 0.5 for real materials).
- **Elastic energy:** $U = \tfrac12F\,\Delta L$; energy density $u = \tfrac12\,\text{stress}\times\text{strain} = \dfrac{\text{stress}^2}{2Y}$.
- **Thermal stress** in a rod clamped at both ends: $Y\alpha\,\Delta T$.
- **Wire under its own weight** (mass $M$, hanging): $\Delta L = \dfrac{MgL}{2AY}$.
- For the same material and load: $\Delta L \propto \dfrac{L}{r^2}$.
:::

@@GRAPH stress-strain

:::important Stress–strain curve vocabulary
Proportional limit (Hooke's law holds up to here) → elastic limit (full recovery up to here) → yield point (plastic flow begins) → ultimate tensile strength → fracture. **Ductile** materials (copper) have a long plastic region. **Brittle** materials (glass) fracture soon after the elastic limit. **Elastomers** (rubber) have large elastic strain but no Hooke's-law region.
:::

## Formulas: Fluids

:::formula Statics
$$P = P_0 + \rho gh \qquad \text{Pascal (hydraulic lift): } \frac{F_1}{A_1} = \frac{F_2}{A_2} \qquad \text{Buoyancy: } F_B = \rho_{fluid}V_{sub}g$$
Floating body: fraction submerged $= \rho_{body}/\rho_{fluid}$. Gauge pressure $= P - P_0$.
:::

:::formula Dynamics
$$A_1v_1 = A_2v_2 \qquad P + \tfrac12\rho v^2 + \rho gh = \text{constant} \qquad \text{Torricelli: } v = \sqrt{2gh}$$
- Hole at depth $h$ below the surface in a tank of height $H$ (on the ground): horizontal range $= 2\sqrt{h(H-h)}$, maximum at $h = H/2$.
- **Venturi meter:** $v_1 = A_2\sqrt{\dfrac{2\Delta P}{\rho(A_1^2 - A_2^2)}}$.
- Lift on a wing / roof blown off: faster flow means lower pressure (Bernoulli).
:::

:::formula Viscosity
$$F = -\eta A\frac{dv}{dx} \qquad \text{Stokes: } F = 6\pi\eta rv \qquad \text{Terminal velocity: } v_t = \frac{2r^2(\rho - \sigma)g}{9\eta}$$
$\rho$ = density of the sphere, $\sigma$ = density of the fluid. **Reynolds number** $R_e = \dfrac{\rho vD}{\eta}$: flow is streamline for $R_e \lesssim 1000$ and turbulent for $R_e \gtrsim 2000$. Critical velocity $v_c = \dfrac{R_e\,\eta}{\rho D}$. The viscosity of liquids falls with temperature, while that of gases rises.
:::

## Formulas: Surface tension

:::formula Surface tension
$$T = \frac FL \qquad W = T\,\Delta A \qquad \text{Excess pressure: drop } \frac{2T}{R},\ \text{soap bubble } \frac{4T}{R},\ \text{air bubble in liquid } \frac{2T}{R}$$
$$\text{Capillary rise: } h = \frac{2T\cos\theta}{\rho gr}$$
- $\theta < 90^\circ$ (water–glass): the liquid rises and the meniscus is concave. $\theta > 90^\circ$ (mercury–glass): the liquid is depressed and the meniscus is convex.
- **Combining $n$ drops** of radius $r$ into one: $R = n^{1/3}r$; energy released $= 4\pi T(nr^2 - R^2)$.
- Detergents **lower** surface tension. Surface tension falls as temperature rises.
- If a capillary tube is shorter than $h$, the liquid doesn't overflow. The radius of curvature of the meniscus adjusts instead.
:::

## Formulas: Thermal properties

:::formula Expansion & calorimetry
$$\Delta L = L\alpha\,\Delta T \qquad \beta = 2\alpha \qquad \gamma = 3\alpha \qquad Q = mc\,\Delta T \qquad Q = mL$$
- **Principle of calorimetry:** heat lost = heat gained (no losses).
- Water: $c = 4186\ \text{J kg}^{-1}\text{K}^{-1}$ ($1\ \text{cal g}^{-1}\,^\circ\text{C}^{-1}$). $L_f = 80$ cal/g ($3.34\times10^5$ J/kg). $L_v = 540$ cal/g ($2.26\times10^6$ J/kg).
- **Anomalous expansion of water:** it contracts from 0 °C to 4 °C and has maximum density at 4 °C.
:::

:::formula Heat transfer
$$\frac{dQ}{dt} = \frac{kA\,\Delta T}{L} \qquad R_{th} = \frac{L}{kA} \qquad \text{series: } R = R_1 + R_2 \qquad \text{parallel: } \frac1R = \frac1{R_1} + \frac1{R_2}$$
Two slabs of equal length in series: $k_{eq} = \dfrac{2k_1k_2}{k_1+k_2}$. Equal area in parallel: $k_{eq} = \dfrac{k_1+k_2}{2}$.
**Radiation:** Stefan–Boltzmann $P = e\sigma AT^4$; net $P = e\sigma A(T^4 - T_0^4)$; $\sigma = 5.67\times10^{-8}\ \text{W m}^{-2}\text{K}^{-4}$.
**Wien's law:** $\lambda_mT = b = 2.9\times10^{-3}$ m K.
**Newton's law of cooling:** $\dfrac{dT}{dt} = -k(T - T_0)$, approximately $\dfrac{T_1 - T_2}{t} = k\left(\dfrac{T_1 + T_2}{2} - T_0\right)$.
:::

@@GRAPH newton-cooling

## Frequently tested concepts & question patterns

:::pyq Recurring structures
1. **Young's modulus / extension** comparisons between wires (same material, different $L$ and $r$); elastic energy.
2. **Bernoulli + continuity:** pressure difference in a pipe, efflux speed, range of a jet.
3. **Terminal velocity** scaling (drops merging), Stokes force.
4. **Capillary rise** changes when $r$ or $\theta$ changes; excess pressure in bubbles; energy when drops merge.
5. **Calorimetry with phase change:** ice + water mixing. Check whether all the ice melts.
6. **Conduction through composite slabs** (junction temperature), and **Newton's law of cooling** (time for successive intervals).
7. **Stefan/Wien:** power ratios for temperature changes; peak wavelength.
:::

## Shortcuts

:::shortcut Junction temperature of two slabs in series
$\theta_{junction} = \dfrac{\theta_1/R_1 + \theta_2/R_2}{1/R_1 + 1/R_2}$, the weighted mean with weights $kA/L$. This is the "Kirchhoff" approach used for resistors, with heat current in place of electric current.
:::

:::shortcut Is all the ice melted?
First compute the heat the warm water can give up by cooling to 0 °C, $Q_{avail}$. Compare it with $m_{ice}L_f$ (plus any heat needed to warm the ice to 0 °C). If $Q_{avail}$ is smaller, the final temperature is 0 °C with some ice left. **Saves** you from impossible negative answers.
:::

## Question classification

| Type | Difficulty | Target time |
|---|---|---|
| Moduli / extension ratios | E | 1 min |
| Bernoulli / continuity | M | 2 min |
| Terminal velocity scaling | E | 1 min |
| Capillarity / excess pressure | E–M | 1.5 min |
| Calorimetry with phase change | M | 2.5 min |
| Composite conduction / Newton cooling | M | 2 min |
| Stefan / Wien ratios | E | 1 min |

## Common mistakes

:::trap Mistake alerts
- Soap bubbles have **two** surfaces: $4T/R$, not $2T/R$.
- Stokes' law uses the **radius**, not the diameter.
- Using °C in Stefan's law. $T$ must be in **kelvin**.
- Assuming the final temperature is above 0 °C without checking that all the ice has melted.
- Forgetting that $\gamma = 3\alpha$ (volume) when a question switches from length to volume.
- In Bernoulli, mixing gauge and absolute pressure.
:::

## Practice questions

@@SET P07 · Practice

@@Q P07-01 | E | 1 | Young's modulus | Calc
A 2 m wire of cross-section $1\ \text{mm}^2$ stretches by 1 mm under a 10 kg load ($g = 10$). Young's modulus is:
(A) $2\times10^{10}\ \text{N m}^{-2}$
(B) $2\times10^{11}\ \text{N m}^{-2}$
(C) $1\times10^{11}\ \text{N m}^{-2}$
(D) $2\times10^{9}\ \text{N m}^{-2}$
@ans B
@sol $Y = \dfrac{FL}{A\Delta L} = \dfrac{100\times2}{10^{-6}\times10^{-3}} = 2\times10^{11}\ \text{N m}^{-2}$.
@short Convert mm² → $10^{-6}$ m² and mm → $10^{-3}$ m first.
@trap Converting 1 mm² as $10^{-3}$ m².
@@END

@@Q P07-02 | E | 1 | Elastic energy | Basic
A wire stretched by 2 mm under a load of 50 N stores elastic energy of:
(A) 0.05 J
(B) 0.1 J
(C) 0.025 J
(D) 100 J
@ans A
@sol $U = \tfrac12F\Delta L = \tfrac12(50)(2\times10^{-3}) = 0.05$ J.
@short The factor $\tfrac12$ is there because the force rises linearly from 0 to $F$.
@trap Forgetting the $\tfrac12$ (0.1 J).
@@END

@@Q P07-03 | E | 0.75 | Torricelli's theorem | NV
Water flows out of a small hole 5 m below the free surface of a large open tank. Find the efflux speed (in m/s, $g = 10$).
@ans 10
@sol $v = \sqrt{2gh} = \sqrt{100} = 10\ \text{m s}^{-1}$.
@short Same as the speed of free fall through $h$.
@trap Measuring $h$ from the bottom instead of from the free surface.
@@END

@@Q P07-04 | E | 0.5 | Continuity equation | Speed
If a pipe's diameter halves, the speed of an incompressible fluid in it becomes:
(A) twice
(B) four times
(C) half
(D) one-fourth
@ans B
@sol $Av$ is constant and $A \propto d^2$: the area becomes 1/4, so the speed is ×4.
@short Speed $\propto 1/d^2$.
@trap Taking speed $\propto 1/d$.
@@END

@@Q P07-05 | M | 1 | Terminal velocity of merged drops | Concept
Eight identical rain drops, each falling at terminal velocity $v$, merge into one drop. Its terminal velocity is:
(A) $2v$
(B) $4v$
(C) $8v$
(D) $16v$
@ans B
@sol Volume ×8 means $R = 2r$. $v_t \propto r^2$, so $v' = 4v$.
@short $v' = n^{2/3}v$.
@trap Assuming $v_t \propto$ volume (8v).
@@END

@@Q P07-06 | M | 1.5 | Capillary rise | NV
Find the height (in cm) to which water rises in a clean glass capillary of radius 0.07 mm. Take surface tension 0.07 N/m, contact angle 0°, $\rho = 1000\ \text{kg m}^{-3}$, $g = 10$.
@ans 20
@sol $h = \dfrac{2T}{\rho gr} = \dfrac{0.14}{1000\times10\times7\times10^{-5}} = \dfrac{0.14}{0.7} = 0.2$ m $= 20$ cm.
@short $hr$ is constant for a given liquid: here $hr = 1.4\times10^{-5}\ \text{m}^2$.
@trap Using the diameter for $r$ gives 10 cm.
@@END

@@Q P07-07 | E | 0.75 | Excess pressure in a soap bubble | Basic
The excess pressure inside a soap bubble of radius 1 cm (surface tension $0.03\ \text{N m}^{-1}$) is:
(A) 6 Pa
(B) 12 Pa
(C) 3 Pa
(D) 24 Pa
@ans B
@sol $\Delta P = 4T/R = 0.12/0.01 = 12$ Pa.
@short Two surfaces, so $4T/R$.
@trap Using $2T/R$ gives 6 Pa.
@@END

@@Q P07-08 | E | 1 | Method of mixtures | NV
100 g of water at 80 °C is mixed with 200 g of water at 20 °C. Find the final temperature (in °C), neglecting heat losses.
@ans 40
@sol $100(80 - T) = 200(T - 20) \Rightarrow 8000 + 4000 = 300T \Rightarrow T = 40$ °C.
@short Mass-weighted mean: $\dfrac{100\times80 + 200\times20}{300}$.
@trap Taking a simple average (50).
@@END

@@Q P07-09 | E | 1 | Latent heat + sensible heat | Basic
The heat needed to convert 10 g of ice at 0 °C into water at 20 °C is ($L_f = 80$ cal/g):
(A) 800 cal
(B) 1000 cal
(C) 200 cal
(D) 1600 cal
@ans B
@sol Melt: $10\times80 = 800$ cal. Warm: $10\times1\times20 = 200$ cal. Total 1000 cal.
@short Always add the phase-change step.
@trap Stopping after melting (800).
@@END

@@Q P07-10 | M | 1 | Series conduction | Concept
Two rods of equal length and area, with conductivities $k$ and $2k$, are joined end to end. The equivalent conductivity of the combination is:
(A) $3k/2$
(B) $4k/3$
(C) $3k$
(D) $2k/3$
@ans B
@sol Series, equal lengths: $k_{eq} = \dfrac{2k_1k_2}{k_1+k_2} = \dfrac{2(k)(2k)}{3k} = \dfrac{4k}{3}$.
@short The harmonic mean is closer to the smaller value.
@trap Using the arithmetic mean (the parallel formula).
@@END

@@Q P07-11 | E | 0.5 | Stefan's law | Speed
If the absolute temperature of a black body doubles, the power it radiates becomes:
(A) 2 times
(B) 4 times
(C) 8 times
(D) 16 times
@ans D
@sol $P \propto T^4 = 2^4 = 16$.
@short —
@trap Doubling a Celsius temperature is **not** doubling $T$.
@@END

@@Q P07-12 | M | 2 | Newton's law of cooling | NV
A body cools from 80 °C to 70 °C in 5 minutes in surroundings at 15 °C. Using the average-temperature form of Newton's law of cooling, find the time (in minutes) it takes to cool from 70 °C to 60 °C.
@ans 6
@sol $\dfrac{10}{5} = k(75 - 15) \Rightarrow k = \dfrac{1}{30}$. Next: $\dfrac{10}{t} = k(65 - 15) = \dfrac{50}{30} \Rightarrow t = 6$ min.
@short Equal temperature drops: $t_2/t_1 = \dfrac{\text{mean excess}_1}{\text{mean excess}_2} = \dfrac{60}{50}$.
@trap Assuming the same 5 min, i.e. constant cooling rate.
@@END

@@SET P07 · Chapter Test

@@Q P07-T1 | E | 0.5 | Poisson's ratio | Basic
A wire's longitudinal strain is $2\times10^{-3}$ and its lateral strain is $-6\times10^{-4}$. Poisson's ratio is:
(A) 0.3
(B) 3.3
(C) 0.03
(D) 0.12
@ans A
@sol $\sigma = -\dfrac{-6\times10^{-4}}{2\times10^{-3}} = 0.3$.
@short Must lie between 0 and 0.5.
@trap Inverting the ratio gives 3.3.
@@END

@@Q P07-T2 | E | 0.5 | Hydraulic lift | Speed
The pistons of a hydraulic lift have areas in the ratio 1 : 50. A 200 N force on the small piston can support a load of weight:
(A) 4 N
(B) 250 N
(C) 10 000 N
(D) 2 000 N
@ans C
@sol $F_2 = F_1\dfrac{A_2}{A_1} = 200\times50 = 10\,000$ N.
@short Pascal's law multiplies the force by the area ratio.
@trap Dividing by the ratio.
@@END

@@Q P07-T3 | E | 0.75 | Wien's displacement law | Basic
A star's spectrum peaks at 500 nm. Its surface temperature is about ($b = 2.9\times10^{-3}$ m K):
(A) 580 K
(B) 5800 K
(C) 58 000 K
(D) 1450 K
@ans B
@sol $T = b/\lambda_m = \dfrac{2.9\times10^{-3}}{5\times10^{-7}} = 5800$ K.
@short Remember: the Sun ≈ 5800 K ≈ 500 nm.
@trap Using $500\times10^{-6}$ m for nm.
@@END

@@Q P07-T4 | E | 0.5 | Volume expansion coefficient | NV
A solid has $\alpha = 2\times10^{-5}\ \text{K}^{-1}$. Its volume expansion coefficient is $x\times10^{-5}\ \text{K}^{-1}$. Find $x$.
@ans 6
@sol $\gamma = 3\alpha = 6\times10^{-5}\ \text{K}^{-1}$.
@short $\alpha : \beta : \gamma = 1 : 2 : 3$.
@trap Using $\gamma = \alpha^3$.
@@END

@@Q P07-T5 | E | 1 | Stokes' law | Calc
A sphere of radius 1 mm moves at $0.1\ \text{m s}^{-1}$ through a liquid of viscosity 1 Pa s. The viscous drag is about:
(A) $1.9\times10^{-3}$ N
(B) $6.0\times10^{-4}$ N
(C) $1.9\times10^{-2}$ N
(D) $3.8\times10^{-3}$ N
@ans A
@sol $F = 6\pi\eta rv = 6\pi(1)(10^{-3})(0.1) = 6\pi\times10^{-4} \approx 1.88\times10^{-3}$ N.
@short $6\pi \approx 18.85$.
@trap Omitting the factor $\pi$ gives (B).
@@END

## Answers & Solutions {#p07-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Solids & Liquids
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
