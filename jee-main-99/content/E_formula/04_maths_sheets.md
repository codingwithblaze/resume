# Mathematics Formula Sheets {#fh-maths}

:::formula M01–M02 · Sets, functions, complex numbers & quadratics · pages [[m01]], [[m02]]
| Result | Formula |
|---|---|
| Counting | $n(A\cup B) = n(A) + n(B) - n(A\cap B)$ · relations on an $n$-set: $2^{n^2}$ · reflexive: $2^{n^2 - n}$ · symmetric: $2^{n(n+1)/2}$ |
| Functions $A \to B$ | total $\lvert B\rvert^{\lvert A\rvert}$ · one-one $^{m}P_{n}$ ($n = \lvert A\rvert \le m = \lvert B\rvert$) · onto from $n$ to 2 elements: $2^n - 2$ |
| Complex numbers | $\lvert z_1z_2\rvert = \lvert z_1\rvert\lvert z_2\rvert$ · $\arg(z_1z_2) = \arg z_1 + \arg z_2$ · $z\bar z = \lvert z\rvert^2$ · $\lvert z_1 + z_2\rvert \le \lvert z_1\rvert + \lvert z_2\rvert$ |
| Cube roots of unity | $1 + \omega + \omega^2 = 0$ · $\omega^3 = 1$ · $\omega = \dfrac{-1 + i\sqrt3}{2}$ |
| Loci | $\lvert z - z_1\rvert = \lvert z - z_2\rvert$: perpendicular bisector · $\lvert z - z_0\rvert = r$: circle |
| Quadratic | $\alpha + \beta = -\dfrac ba$ · $\alpha\beta = \dfrac ca$ · $D = b^2 - 4ac$ · $\lvert\alpha - \beta\rvert = \dfrac{\sqrt D}{\lvert a\rvert}$ |
| Root location ($a > 0$) | both roots $> k$: $D \ge 0$, $f(k) > 0$, $-\dfrac{b}{2a} > k$ · $k$ between the roots: $f(k) < 0$ |
:::

:::formula M03 · Matrices & determinants · page [[m03]]
| Result | Formula |
|---|---|
| Adjoint & inverse | $A^{-1} = \dfrac{\operatorname{adj}A}{\lvert A\rvert}$ · $A(\operatorname{adj}A) = \lvert A\rvert I$ |
| Determinant rules ($n\times n$) | $\lvert kA\rvert = k^n\lvert A\rvert$ · $\lvert\operatorname{adj}A\rvert = \lvert A\rvert^{n-1}$ · $\lvert\operatorname{adj}(\operatorname{adj}A)\rvert = \lvert A\rvert^{(n-1)^2}$ · $\lvert A^{-1}\rvert = \dfrac{1}{\lvert A\rvert}$ |
| Products | $(AB)^{-1} = B^{-1}A^{-1}$ · $(AB)^T = B^TA^T$ · $\operatorname{adj}(AB) = \operatorname{adj}B\,\operatorname{adj}A$ |
| Special matrices | symmetric $A^T = A$ · skew $A^T = -A$ (odd-order skew: $\lvert A\rvert = 0$) · orthogonal $AA^T = I$ |
| Linear systems $AX = B$ | $\lvert A\rvert \ne 0$: unique · $\lvert A\rvert = 0$ and $(\operatorname{adj}A)B \ne 0$: no solution · $\lvert A\rvert = 0$ and $(\operatorname{adj}A)B = 0$: infinitely many or none (check) |
| Area of a triangle | $\tfrac12\left\lvert\begin{smallmatrix}x_1&y_1&1\\x_2&y_2&1\\x_3&y_3&1\end{smallmatrix}\right\rvert$ |
:::

:::formula M04–M06 · P&C, binomial, sequences · pages [[m04]], [[m05]], [[m06]]
| Result | Formula |
|---|---|
| Permutations & combinations | $^nP_r = \dfrac{n!}{(n - r)!}$ · $^nC_r = \dfrac{n!}{r!(n - r)!}$ · $^nC_r + {}^nC_{r-1} = {}^{n+1}C_r$ |
| Repetition | $\dfrac{n!}{p!\,q!\,r!}$ · circular $(n - 1)!$ · necklace $\dfrac{(n - 1)!}{2}$ |
| Distribution | $n$ identical into $r$ groups: $^{n+r-1}C_{r-1}$ (each $\ge 1$: $^{n-1}C_{r-1}$) |
| Derangements | $D_n = n!\sum_{k=0}^n\dfrac{(-1)^k}{k!}$ · $D_3 = 2$, $D_4 = 9$, $D_5 = 44$ |
| Binomial general term | $T_{r+1} = {}^nC_rx^{n-r}y^r$ · middle term: $T_{n/2 + 1}$ ($n$ even) |
| Coefficient sums | $\sum{}^nC_r = 2^n$ · $\sum_{\text{odd}} = \sum_{\text{even}} = 2^{n-1}$ |
| AP | $a_n = a + (n - 1)d$ · $S_n = \dfrac n2[2a + (n - 1)d]$ |
| GP | $a_n = ar^{n-1}$ · $S_n = \dfrac{a(r^n - 1)}{r - 1}$ · $S_\infty = \dfrac{a}{1 - r}$ ($\lvert r\rvert < 1$) |
| Means | $\text{AM} \ge \text{GM} \ge \text{HM}$ · $\sum k^2 = \dfrac{n(n + 1)(2n + 1)}{6}$ · $\sum k^3 = \left[\dfrac{n(n + 1)}{2}\right]^2$ |
:::

:::formula M07 · Limits, continuity, differentiability & applications · page [[m07]]
| Result | Formula |
|---|---|
| Standard limits | $\lim\dfrac{\sin x}{x} = 1$ · $\lim\dfrac{e^x - 1}{x} = 1$ · $\lim\dfrac{\ln(1 + x)}{x} = 1$ · $\lim\dfrac{a^x - 1}{x} = \ln a$ · $\lim\dfrac{x^n - a^n}{x - a} = na^{n-1}$ |
| $1^\infty$ form | $\lim f^g = e^{\lim g(f - 1)}$ |
| Expansions | $\sin x \approx x - \dfrac{x^3}{6}$ · $\cos x \approx 1 - \dfrac{x^2}{2}$ · $\tan x \approx x + \dfrac{x^3}{3}$ · $e^x \approx 1 + x + \dfrac{x^2}{2}$ |
| Derivatives | $(\tan x)' = \sec^2x$ · $(\sec x)' = \sec x\tan x$ · $(\sin^{-1}x)' = \dfrac{1}{\sqrt{1 - x^2}}$ · $(\tan^{-1}x)' = \dfrac{1}{1 + x^2}$ · $(a^x)' = a^x\ln a$ |
| Rules | product, quotient, chain · parametric $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$ · $x^x$: take logs |
| Applications | rate of change · increasing where $f' > 0$ · maximum: $f' = 0$, $f'' < 0$ (Rolle/LMVT are not in the 2024+ text) |
:::

:::formula M08–M09 · Integration & differential equations · pages [[m08]], [[m09]]
| Result | Formula |
|---|---|
| Standard integrals | $\int\dfrac{dx}{x^2 + a^2} = \dfrac1a\tan^{-1}\dfrac xa$ · $\int\dfrac{dx}{\sqrt{a^2 - x^2}} = \sin^{-1}\dfrac xa$ · $\int\dfrac{dx}{x^2 - a^2} = \dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert$ |
| More | $\int\dfrac{dx}{\sqrt{x^2 \pm a^2}} = \ln\left\lvert x + \sqrt{x^2 \pm a^2}\right\rvert$ · $\int e^x[f + f']\,dx = e^xf$ · $\int\sec x\,dx = \ln\lvert\sec x + \tan x\rvert$ |
| By parts | $\int uv\,dx = u\int v - \int\left(u'\int v\right)$ (ILATE) |
| Definite properties | $\int_a^b f(x)\,dx = \int_a^b f(a + b - x)\,dx$ · even: $2\int_0^a$ · odd: 0 · period $T$: $\int_0^{nT} = n\int_0^T$ |
| Standard results | $\int_0^{\pi/2}\sin^nx\,dx$ (Wallis) · $\int_0^{\pi/2}\ln\sin x\,dx = -\dfrac\pi2\ln2$ · $\int_0^{\pi/2}\dfrac{\sin^n}{\sin^n + \cos^n} = \dfrac\pi4$ |
| Leibniz | $\dfrac{d}{dx}\int_{g(x)}^{h(x)}f(t)\,dt = f(h)h' - f(g)g'$ |
| Areas | $y^2 = 4ax$ and $x^2 = 4by$: $\dfrac{16ab}{3}$ · ellipse $\pi ab$ · parabola $y^2 = 4ax$ with its latus rectum: $\dfrac{8a^2}{3}$ |
| Linear DE | $y' + Py = Q$: IF $= e^{\int P\,dx}$ · $y\cdot\text{IF} = \int Q\cdot\text{IF}\,dx + C$ |
:::

:::formula M10 · Coordinate geometry · page [[m10]]
| Result | Formula |
|---|---|
| Lines | distance $\dfrac{\lvert ax_1 + by_1 + c\rvert}{\sqrt{a^2 + b^2}}$ · $\tan\theta = \left\lvert\dfrac{m_1 - m_2}{1 + m_1m_2}\right\rvert$ · image: $\dfrac{x - x_1}{a} = \dfrac{y - y_1}{b} = \dfrac{-2(ax_1 + by_1 + c)}{a^2 + b^2}$ |
| Circle | centre $(-g, -f)$, $r = \sqrt{g^2 + f^2 - c}$ · chord $2\sqrt{r^2 - d^2}$ |

| Conic | $e$ | Focus | Directrix | Latus rectum |
|---|---|---|---|---|
| $y^2 = 4ax$ | 1 | $(a, 0)$ | $x = -a$ | $4a$ |
| $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ ($a > b$) | $\sqrt{1 - \dfrac{b^2}{a^2}}$ | $(\pm ae, 0)$ | $x = \pm\dfrac ae$ | $\dfrac{2b^2}{a}$ |
| $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ | $\sqrt{1 + \dfrac{b^2}{a^2}}$ | $(\pm ae, 0)$ | $x = \pm\dfrac ae$ | $\dfrac{2b^2}{a}$ |

Ellipse: $PS_1 + PS_2 = 2a$ · hyperbola: $\lvert PS_1 - PS_2\rvert = 2a$ · rectangular hyperbola $e = \sqrt2$.
:::

:::formula M11–M12 · 3D geometry & vectors · pages [[m11]], [[m12]]
| Result | Formula |
|---|---|
| DCs | $l^2 + m^2 + n^2 = 1$ · $\cos\theta = \dfrac{\lvert a_1a_2 + b_1b_2 + c_1c_2\rvert}{\sqrt{\sum a_1^2}\sqrt{\sum a_2^2}}$ |
| Shortest distance | skew $\dfrac{\lvert(\vec a_2 - \vec a_1)\cdot(\vec b_1\times\vec b_2)\rvert}{\lvert\vec b_1\times\vec b_2\rvert}$ · parallel $\dfrac{\lvert(\vec a_2 - \vec a_1)\times\vec b\rvert}{\lvert\vec b\rvert}$ |
| Foot / image in a line | general point $Q(\lambda)$, then $\vec{PQ}\cdot\vec b = 0$ · image $2Q - P$ |
| Products | $\vec a\cdot\vec b = \lvert a\rvert\lvert b\rvert\cos\theta$ · $\lvert\vec a\times\vec b\rvert = \lvert a\rvert\lvert b\rvert\sin\theta$ · projection $\dfrac{\vec a\cdot\vec b}{\lvert\vec b\rvert}$ |
| Areas & volume | triangle $\tfrac12\lvert\vec{AB}\times\vec{AC}\rvert$ · $[\vec a\ \vec b\ \vec c]$ = volume · coplanar iff $[\vec a\ \vec b\ \vec c] = 0$ |
| Identities | $\lvert\vec a\times\vec b\rvert^2 + (\vec a\cdot\vec b)^2 = \lvert a\rvert^2\lvert b\rvert^2$ · $\vec a\times(\vec b\times\vec c) = (\vec a\cdot\vec c)\vec b - (\vec a\cdot\vec b)\vec c$ |
:::

:::formula M13–M14 · Statistics, probability & trigonometry · pages [[m13]], [[m14]]
| Result | Formula |
|---|---|
| Variance | $\sigma^2 = \dfrac{\sum x^2}{n} - \bar x^2$ · $y = ax + b$: $\sigma_y = \lvert a\rvert\sigma_x$ · first $n$ naturals $\dfrac{n^2 - 1}{12}$ |
| Grouped median / mode | $l + \dfrac{N/2 - C}{f}h$ · $l + \dfrac{f_1 - f_0}{2f_1 - f_0 - f_2}h$ |
| Probability | $P(A\cup B) = P(A) + P(B) - P(A\cap B)$ · $P(A\mid B) = \dfrac{P(A\cap B)}{P(B)}$ · independent: $P(A\cap B) = P(A)P(B)$ |
| Bayes | $P(E_k\mid A) = \dfrac{P(E_k)P(A\mid E_k)}{\sum P(E_i)P(A\mid E_i)}$ |
| Random variable | $E(X) = \sum xp$ · $\operatorname{Var} = E(X^2) - [E(X)]^2$ · binomial: mean $np$, variance $npq$ |
| Trig identities | $\sin2A = \dfrac{2\tan A}{1 + \tan^2A}$ · $\cos2A = \dfrac{1 - \tan^2A}{1 + \tan^2A}$ · $\sin3A = 3\sin A - 4\sin^3A$ · $\cos3A = 4\cos^3A - 3\cos A$ |
| Range | $a\sin x + b\cos x \in [-\sqrt{a^2 + b^2}, \sqrt{a^2 + b^2}]$ |
| Inverse trig | $\sin^{-1}x + \cos^{-1}x = \dfrac\pi2$ · $\tan^{-1}x + \tan^{-1}y = \tan^{-1}\dfrac{x + y}{1 - xy}$ ($xy < 1$) · $\cos^{-1}(-x) = \pi - \cos^{-1}x$ |
:::
