# The JEE Main Speed & Shortcut Manual {#speed-manual}

In JEE Main, "speed" is not fast writing. It is three separate skills:

:::grid3
**1 · Selection**

Recognising within about 20 seconds which questions to attempt now, later or never. This is the biggest time saver (Exam-Hall Protocol, page [[hall-protocol]]).
+++
**2 · Recognition**

Seeing the question model ("this is a shortest-distance problem") so the method comes to mind at once. It comes from model drills in every chapter.
+++
**3 · Execution**

Doing the algebra and arithmetic cleanly by hand, with no calculator. This manual and the drills in the next chapter train it.
:::

The sixteen techniques below are **legitimate methods**: each one is either a mathematically valid shortcut or a way to eliminate options with certainty. Each gives when to use it, when **not** to use it, a worked example, the approximate time saved and the most common mistake. The time savings are this book's estimates {{tag:rec}}, not measured data.

| # | Technique | Main subjects |
|---|---|---|
| 1 | Dimensional analysis | Physics |
| 2 | Limiting cases | Physics, Maths |
| 3 | Special-value substitution | Maths |
| 4 | Back-substitution of options | Maths, Chemistry |
| 5 | Symmetry | Physics, Maths |
| 6 | One-significant-figure estimation | Physics, Chemistry |
| 7 | Ratio (proportionality) method | Physics, Chemistry |
| 8 | Conservation laws first | Physics |
| 9 | The standard-result bank | all |
| 10 | Graph instead of algebra | Maths, Physics |
| 11 | Equivalents and the $n$-factor | Chemistry |
| 12 | Log and pH shortcuts | Chemistry |
| 13 | Working backwards in organic chemistry | Chemistry |
| 14 | Elimination by impossibility | all |
| 15 | Casting out nines | all (arithmetic checks) |
| 16 | Cancel before you multiply | all |

@@PAGEBREAK

:::shortcut 1 · Dimensional analysis
| Use it when | Don't use it when |
|---|---|
| the options differ in the powers of physical quantities | the options differ only in pure numbers ($2$, $\pi$, $\tfrac12$) or in dimensionless groups |

**Example.** The speed of a transverse wave on a string with tension $T$ and linear mass density $\mu$ is (A) $\sqrt{T/\mu}$ (B) $\sqrt{T\mu}$ (C) $T/\mu$ (D) $\sqrt{\mu/T}$. $[T] = \text{MLT}^{-2}$ and $[\mu] = \text{ML}^{-1}$, so $[T/\mu] = \text{L}^2\text{T}^{-2}$ and only $\sqrt{T/\mu}$ is a speed.
**Time saved:** 1–2 minutes (no derivation).
**Common mistake:** treating angles, strains or $e^{x}$ arguments as dimensional. Exponents and trig arguments must be dimensionless.
:::

:::shortcut 2 · Limiting cases
| Use it when | Don't use it when |
|---|---|
| a formula depends on masses, angles or distances that can be pushed to $0$, $\infty$ or equality | the limit changes the physical situation (e.g. a block that stops sliding once $\mu$ gets large enough) |

**Example.** For an Atwood machine, $a = \dfrac{(m_1 - m_2)g}{m_1 + m_2}$. Check: $m_2 \to 0$ gives $a \to g$ (free fall) ✓; $m_1 = m_2$ gives $a = 0$ ✓. An option such as $\dfrac{(m_1 - m_2)g}{2m_1}$ passes the second test but fails the first ($m_2 \to 0$ gives $g/2$). Test two limits.
**Time saved:** 1–3 minutes on formula-choice MCQs.
**Common mistake:** using only one limit. Several options often pass the same one.
:::

:::shortcut 3 · Special-value substitution
| Use it when | Don't use it when |
|---|---|
| the options are formulas in $n$, $x$ or $\theta$ and the statement is an identity | the options agree at every easy value, or the question asks for a count of solutions |

**Example.** $\sum_{k=1}^n k\cdot k!$ equals (A) $(n + 1)! - 1$ (B) $n! + 1$ (C) $(n + 1)!$ (D) $n\cdot n!$. At $n = 1$ the sum is 1: (A) and (D) survive. At $n = 2$ the sum is $1 + 4 = 5$: (A) gives 5 and (D) gives 4. The answer is (A).
**Time saved:** 2–4 minutes compared with proving the result.
**Common mistake:** testing only $n = 1$ or $x = 0$, where several options coincide. Always test a second value.
:::

:::shortcut 4 · Back-substitution of options
| Use it when | Don't use it when |
|---|---|
| the options are numbers and checking one is faster than solving | numerical-value questions (there are no options), or options that contain parameters |

**Example.** Solve $\sqrt{x + 5} + \sqrt x = 5$: options 4, 9, 1, 16. At $x = 4$: $3 + 2 = 5$ ✓. No squaring is needed, so no extraneous roots can appear.
**Time saved:** 1–2 minutes.
**Common mistake:** accepting an option that "almost" works. The check must be exact.
:::

:::shortcut 5 · Symmetry
| Use it when | Don't use it when |
|---|---|
| a circuit, charge distribution or integral is unchanged by a reflection, rotation or $x \to a + b - x$ | one element breaks the symmetry (a single different resistor, an asymmetric limit) |

**Example.** $I = \displaystyle\int_0^{\pi/2}\frac{\sqrt{\sin x}}{\sqrt{\sin x} + \sqrt{\cos x}}\,dx$. Replacing $x$ by $\tfrac\pi2 - x$ swaps $\sin$ and $\cos$, so $2I = \int_0^{\pi/2}1\,dx$ and $I = \tfrac\pi4$.
**Time saved:** 3–5 minutes.
**Common mistake:** assuming a circuit is symmetric without checking every branch.
:::

:::shortcut 6 · One-significant-figure estimation
| Use it when | Don't use it when |
|---|---|
| the options differ by a factor of 2 or more | the options are within about 10% of each other, or you are subtracting nearly equal numbers |

**Example.** Energy of a 500 nm photon: (A) $1.3\times10^{-19}$ J (B) $4\times10^{-19}$ J (C) $4\times10^{-18}$ J (D) $4\times10^{-20}$ J. Estimate: $\dfrac{(6.6\times10^{-34})(3\times10^{8})}{5\times10^{-7}} \approx 4\times10^{-19}$ J. (In eV it is $1240/500 \approx 2.5$ eV. An option of $2.5\times10^{-19}$ J would be a unit trap.)
**Time saved:** about 1 minute per calculation-heavy question.
**Common mistake:** estimating in mass-defect or small-difference problems, where the difference is the answer.
:::

:::shortcut 7 · Ratio (proportionality) method
| Use it when | Don't use it when |
|---|---|
| the question changes one quantity and asks for the effect on another | quantities combine additively ($R + r$, $u + at$), so no single power law applies |

**Example.** A planet orbits at 4 times Earth's orbital radius. Since $T \propto r^{3/2}$, $T = 4^{3/2} = 8$ years. Chemistry: the time for equal volumes to effuse scales as $\sqrt M$, so $\ce{O2}$ takes $\sqrt{32/2} = 4$ times as long as $\ce{H2}$.
**Time saved:** 1–2 minutes (no constants needed).
**Common mistake:** using the wrong power, such as $r^{2/3}$ instead of $r^{3/2}$.
:::

:::shortcut 8 · Conservation laws first
| Use it when | Don't use it when |
|---|---|
| the question asks for a speed, height or final velocity and the forces are conservative (or collisions are involved) | time, force or acceleration at an instant is asked, or friction does unknown work |

**Example.** A bead slides from rest down a frictionless curved wire through a height $h$. Its speed at the bottom is $\sqrt{2gh}$, whatever the shape of the wire. Force analysis would need the curve's equation.
**Time saved:** 2–5 minutes.
**Common mistake:** conserving kinetic energy in an inelastic collision. Only momentum is conserved there.
:::

:::shortcut 9 · The standard-result bank
| Use it when | Don't use it when |
|---|---|
| the situation matches a standard case exactly | a condition differs (a projectile launched from a height, a non-uniform rod) |

**Example.** Spin-only magnetic moments for $n = 1$ to 5 unpaired electrons are 1.73, 2.83, 3.87, 4.90 and 5.92 BM. For $\ce{Fe^3+}$ (high-spin $d^5$) you know 5.92 BM without computing $\sqrt{35}$. Other entries in the bank: $\int_0^{\pi/2}\ln\sin x\,dx = -\tfrac\pi2\ln2$; the maximum range at $45^\circ$; area between $y^2 = 4ax$ and $x^2 = 4by$ is $\tfrac{16ab}{3}$.
**Time saved:** 1–3 minutes each.
**Common mistake:** applying a standard result outside its conditions.
:::

:::shortcut 10 · Graph instead of algebra
| Use it when | Don't use it when |
|---|---|
| the question asks for the number of solutions or the sign of a root | the exact value of a root is required |

**Example.** Number of real solutions of $e^x = x^2$. Sketch both curves. For $x < 0$ they cross once. For $x > 0$, $e^x - x^2$ is always positive (its minimum there is $2 - 2\ln 2 > 0$). Answer: 1.
**Time saved:** 2–4 minutes.
**Common mistake:** careless sketching near tangency or asymptotes. Check one or two exact points.
:::

:::shortcut 11 · Equivalents and the n-factor
| Use it when | Don't use it when |
|---|---|
| titration, redox stoichiometry or electrolysis questions | disproportionation or an unclear product, where the $n$-factor is ambiguous. Balance the equation instead |

**Example.** Volume of 0.1 M $\ce{KMnO4}$ (acidic, $n = 5$) needed for 50 mL of 0.1 M $\ce{FeSO4}$ ($n = 1$): milliequivalents of $\ce{Fe^2+}$ $= 50\times0.1\times1 = 5$, so $V = \dfrac{5}{0.1\times5} = 10$ mL.
**Time saved:** 1–2 minutes (no balanced equation needed).
**Common mistake:** using $n = 5$ for $\ce{KMnO4}$ in neutral or weakly basic medium, where it is 3.
:::

:::shortcut 12 · Log and pH shortcuts
| Use it when | Don't use it when |
|---|---|
| weak acids and bases with small $\alpha$, and buffers | very dilute solutions (below about $10^{-6}$ M), where water's own ions matter |

**Example.** 0.01 M acetic acid with $\text{p}K_a = 4.74$: $\text{pH} = \tfrac12(\text{p}K_a - \log C) = \tfrac12(4.74 + 2) = 3.37$. A buffer with $[\text{salt}] = 10[\text{acid}]$ has $\text{pH} = \text{p}K_a + 1$.
**Time saved:** about 1 minute.
**Common mistake:** giving pH 8 for $10^{-8}$ M $\ce{HCl}$. An acid solution can't be basic; the answer is just below 7.
:::

:::shortcut 13 · Working backwards in organic chemistry
| Use it when | Don't use it when |
|---|---|
| the products are given and the starting compound is asked (ozonolysis, hydrolysis, degradation) | carbocation rearrangements are possible. Then the forward mechanism is needed |

**Example.** An alkene gives acetone and acetaldehyde on ozonolysis. Join the two carbonyl carbons with a double bond: $\ce{(CH3)2C=CHCH3}$ (2-methylbut-2-ene).
**Time saved:** 1–3 minutes.
**Common mistake:** miscounting carbons. Each $\ce{C=O}$ carbon came from one alkene carbon.
:::

:::shortcut 14 · Elimination by impossibility
| Use it when | Don't use it when |
|---|---|
| always, as a first filter: probability > 1, efficiency > 1, negative speed or count, wrong sign of a quantity | you are tempted to eliminate an option that merely *looks* unusual (a negative focal length is valid) |

**Example.** Carnot efficiency between 500 K and 300 K: (A) 0.6 (B) 1.67 (C) 0.4 (D) 0.8. (B) is impossible, and $1 - \tfrac{300}{500} = 0.4$.
**Time saved:** varies; turns some four-way guesses into two-way decisions (Answer-Choice Strategy, page [[answer-choice]]).
**Common mistake:** eliminating on "looks" instead of on a physical or mathematical impossibility.
:::

:::shortcut 15 · Casting out nines
| Use it when | Don't use it when |
|---|---|
| checking a long multiplication or addition before you commit an NV answer | as proof of correctness: it cannot detect swapped digits |

**Example.** Is $347\times26 = 9022$? Digit sums reduce to $3 + 4 + 7 = 14 \to 5$ and $2 + 6 = 8$; $5\times8 = 40 \to 4$. $9 + 0 + 2 + 2 = 13 \to 4$ ✓. A mismatch would prove an error.
**Time saved:** prevents lost marks rather than saving time: about 15 seconds per check.
**Common mistake:** treating a match as proof. $9202$ gives the same check digit.
:::

:::shortcut 16 · Cancel before you multiply
| Use it when | Don't use it when |
|---|---|
| always: every fraction with products above and below | — |

**Example.** $\dfrac{\frac{22}{7}\times49\times3}{11\times7}$: cancel $22$ with $11$ (giving 2) and $49$ with $7\times7$ (giving 1), leaving $2\times3 = 6$. No four-digit numbers are ever written.
**Time saved:** 30–60 seconds per calculation, with fewer arithmetic slips.
**Common mistake:** rounding intermediate values (e.g. $\pi \approx 3$) and then being "between two options". Keep exact values until the last step.
:::
