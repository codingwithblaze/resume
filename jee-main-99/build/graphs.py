"""Schematic physics/chemistry graphs, data charts and QR codes as inline SVG."""
from __future__ import annotations

import html
import io
import math

import segno

W, H = 240, 160          # panel viewBox
L, R, T, B = 30, 12, 14, 26  # plot margins


def _esc(s):
    return html.escape(str(s))


class Panel:
    def __init__(self, title, xlabel, ylabel, xr=(0, 1), yr=(0, 1), w=W, h=H):
        self.title, self.xlabel, self.ylabel = title, xlabel, ylabel
        self.x0, self.x1 = xr
        self.y0, self.y1 = yr
        self.w, self.h = w, h
        self.items: list[str] = []

    def X(self, x):
        return L + (x - self.x0) / (self.x1 - self.x0) * (self.w - L - R)

    def Y(self, y):
        return self.h - B - (y - self.y0) / (self.y1 - self.y0) * (self.h - T - B)

    # --- marks
    def curve(self, fn, a=None, b=None, n=160, cls="g-c1", dash=False):
        a = self.x0 if a is None else a
        b = self.x1 if b is None else b
        pts = []
        for i in range(n + 1):
            x = a + (b - a) * i / n
            try:
                y = fn(x)
            except (ZeroDivisionError, ValueError, OverflowError):
                continue
            if y is None or not math.isfinite(y):
                continue
            y = max(min(y, self.y1 * 1.05 + 0.0), self.y0 - (self.y1 - self.y0) * 0.05)
            pts.append(f"{self.X(x):.1f},{self.Y(y):.1f}")
        d = ' stroke-dasharray="4 3"' if dash else ""
        self.items.append(f'<polyline class="{cls}" points="{" ".join(pts)}"{d}/>')

    def poly(self, pts, cls="g-c1", dash=False, closed=False):
        p = " ".join(f"{self.X(x):.1f},{self.Y(y):.1f}" for x, y in pts)
        d = ' stroke-dasharray="4 3"' if dash else ""
        tag = "polygon" if closed else "polyline"
        self.items.append(f'<{tag} class="{cls}" points="{p}"{d}/>')

    def area(self, fn, a, b, n=80, cls="g-fill"):
        pts = [(a, 0)] + [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)] + [(b, 0)]
        self.poly(pts, cls=cls, closed=True)

    def dot(self, x, y, cls="g-dot"):
        self.items.append(f'<circle class="{cls}" cx="{self.X(x):.1f}" cy="{self.Y(y):.1f}" r="2.6"/>')

    def text(self, x, y, s, anchor="start", cls="g-lab", dx=0, dy=0):
        self.items.append(f'<text class="{cls}" x="{self.X(x) + dx:.1f}" y="{self.Y(y) + dy:.1f}" text-anchor="{anchor}">{_esc(s)}</text>')

    def vline(self, x, y0=None, y1=None, cls="g-guide"):
        y0 = self.y0 if y0 is None else y0
        y1 = self.y1 if y1 is None else y1
        self.items.append(f'<line class="{cls}" x1="{self.X(x):.1f}" y1="{self.Y(y0):.1f}" x2="{self.X(x):.1f}" y2="{self.Y(y1):.1f}"/>')

    def hline(self, y, x0=None, x1=None, cls="g-guide"):
        x0 = self.x0 if x0 is None else x0
        x1 = self.x1 if x1 is None else x1
        self.items.append(f'<line class="{cls}" x1="{self.X(x0):.1f}" y1="{self.Y(y):.1f}" x2="{self.X(x1):.1f}" y2="{self.Y(y):.1f}"/>')

    def svg(self):
        ax = (f'<line class="g-axis" x1="{L}" y1="{self.h - B}" x2="{self.w - R + 4}" y2="{self.h - B}"/>'
              f'<line class="g-axis" x1="{L}" y1="{self.h - B}" x2="{L}" y2="{T - 4}"/>'
              f'<path class="g-axisarrow" d="M{self.w - R + 4},{self.h - B} l-5,-2.5 v5 z"/>'
              f'<path class="g-axisarrow" d="M{L},{T - 4} l-2.5,5 h5 z"/>')
        # zero line if y-range crosses 0
        zero = ""
        if self.y0 < 0 < self.y1:
            zero = f'<line class="g-zero" x1="{L}" y1="{self.Y(0):.1f}" x2="{self.w - R}" y2="{self.Y(0):.1f}"/>'
        lab = (f'<text class="g-axlab" x="{self.w - R + 2}" y="{self.h - B + 13}" text-anchor="end">{_esc(self.xlabel)}</text>'
               f'<text class="g-axlab" x="{L - 5}" y="{T - 6}" text-anchor="start">{_esc(self.ylabel)}</text>')
        return (f'<svg class="gpanel" viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg">'
                f'{zero}{ax}{"".join(self.items)}{lab}</svg>')


def figure(panels, caption=""):
    cells = "".join(f'<div class="gcell">{p.svg()}<div class="gcap">{_esc(p.title)}</div></div>' for p in panels)
    cap = f'<figcaption>{caption}</figcaption>' if caption else ""
    return f'<figure class="graph graph-n{len(panels)}"><div class="grow">{cells}</div>{cap}</figure>'


# ============================================================ physics graphs
def g_kin():
    a = Panel("x–t: uniform velocity (slope = v)", "t", "x")
    a.curve(lambda t: 0.1 + 0.8 * t)
    b = Panel("x–t: uniform acceleration", "t", "x")
    b.curve(lambda t: 0.05 + 0.9 * t * t)
    c = Panel("v–t: uniform acceleration", "t", "v")
    c.area(lambda t: 0.2 + 0.7 * t, 0, 0.85)
    c.curve(lambda t: 0.2 + 0.7 * t)
    c.text(0.42, 0.22, "area = displacement", "middle")
    c.text(0.9, 0.9, "slope = a", "end")
    d = Panel("a–t: constant acceleration", "t", "a")
    d.area(lambda t: 0.6, 0, 0.85)
    d.curve(lambda t: 0.6)
    d.text(0.42, 0.3, "area = Δv", "middle")
    return figure([a, b, c, d])


def g_friction():
    p = Panel("Friction vs applied force", "applied force F", "friction f", w=300)
    p.poly([(0, 0), (0.55, 0.75)])
    p.poly([(0.55, 0.75), (0.58, 0.55), (1, 0.55)])
    p.dot(0.55, 0.75)
    p.text(0.27, 0.46, "static: f = F", "end", dx=-4)
    p.text(0.55, 0.8, "limiting μₛN", "middle")
    p.text(0.8, 0.6, "kinetic μₖN", "middle")
    p.hline(0.55, 0, 0.58)
    return figure([p])


def g_pe():
    p = Panel("Potential-energy curve", "x", "U(x)", yr=(-0.2, 1), w=300)
    f = lambda x: 0.55 + 0.35 * math.sin(2 * math.pi * (x - 0.05) * 1.3) * (1 - 0.3 * x)
    p.curve(f, 0, 1)
    p.hline(0.7, cls="g-c2")
    p.text(0.99, 0.74, "total energy E", "end")
    p.text(0.49, 0.12, "stable (U min)", "middle")
    p.text(0.84, 0.95, "unstable (U max)", "middle")
    return figure([p])


def g_gravity():
    p = Panel("g inside and outside the Earth", "r", "g", w=300)
    p.poly([(0, 0), (0.3, 0.9)])
    p.curve(lambda r: 0.9 * (0.3 / r) ** 2, 0.3, 1)
    p.vline(0.3)
    p.text(0.3, -0.1, "R", "middle", dy=10)
    p.text(0.13, 0.62, "∝ r", "middle")
    p.text(0.62, 0.36, "∝ 1/r²", "middle")
    return figure([p])


def g_stress():
    p = Panel("Stress–strain curve (metal wire)", "strain", "stress", w=300)
    pts = [(0, 0), (0.18, 0.55), (0.22, 0.62), (0.3, 0.66), (0.5, 0.8), (0.68, 0.86), (0.82, 0.8), (0.9, 0.72)]
    p.curve(lambda x: 0, 0, 0)  # noop
    p.poly(pts)
    for (x, y, s, anc) in [(0.18, 0.55, "A proportional limit", "start"), (0.3, 0.66, "B yield point", "start"),
                           (0.68, 0.86, "D ultimate strength", "middle"), (0.9, 0.72, "E fracture", "middle")]:
        p.dot(x, y)
        p.text(x, y, s, anc, dx=4 if anc == "start" else 0, dy=-6)
    p.text(0.09, 0.15, "Hooke's law", "start")
    return figure([p])


def g_cooling():
    p = Panel("Newton's law of cooling", "t", "T", w=300)
    p.curve(lambda t: 0.2 + 0.7 * math.exp(-3.2 * t))
    p.hline(0.2, cls="g-c2", )
    p.text(0.98, 0.24, "surroundings T₀", "end")
    p.text(0.2, 0.62, "excess T − T₀ decays exponentially", "start")
    return figure([p])


def g_pv():
    p = Panel("P–V: four basic processes", "V", "P", w=300)
    V0, P0 = 0.35, 0.6
    p.curve(lambda v: P0 * V0 / v, 0.2, 0.95)
    p.curve(lambda v: P0 * (V0 / v) ** 1.67, 0.23, 0.95, cls="g-c2")
    p.hline(P0, 0.1, 0.9, cls="g-c3")
    p.vline(V0, 0.05, 0.95, cls="g-c3")
    p.dot(V0, P0)
    p.text(0.93, 0.28, "isothermal", "end")
    p.text(0.93, 0.09, "adiabatic (steeper)", "end")
    p.text(0.88, 0.64, "isobaric", "end")
    p.text(V0 + 0.02, 0.95, "isochoric", "start")
    return figure([p])


def g_maxwell():
    p = Panel("Maxwell speed distribution", "speed v", "fraction", w=300)
    f = lambda v, a: 4 / math.sqrt(math.pi) * (v / a) ** 2 * math.exp(-(v / a) ** 2) / a * 0.28
    p.curve(lambda v: f(v, 0.25), 0, 1)
    p.curve(lambda v: f(v, 0.42), 0, 1, cls="g-c2")
    p.text(0.26, 0.9, "T₁", "middle")
    p.text(0.47, 0.6, "T₂ > T₁", "start")
    p.text(0.98, 0.9, "area under each curve = 1", "end")
    return figure([p])


def g_shm():
    p = Panel("Energy in SHM", "x (−A to +A)", "energy", xr=(-1, 1), w=300)
    p.curve(lambda x: 0.9 * x * x, cls="g-c2")
    p.curve(lambda x: 0.9 * (1 - x * x))
    p.hline(0.9, cls="g-c3")
    p.text(0, 0.95, "total E = ½kA²", "middle")
    p.text(-0.95, 0.12, "KE", "start")
    p.text(-0.98, 0.78, "PE", "start")
    p.text(0.72, 0.52, "KE = PE at x = ±A/√2", "middle")
    return figure([p])


def g_standing():
    panels = []
    for n in (1, 2, 3):
        p = Panel(f"String, fixed ends: n = {n}", "", "", xr=(0, 1), yr=(-1, 1))
        p.curve(lambda x, n=n: 0.8 * math.sin(n * math.pi * x))
        p.curve(lambda x, n=n: -0.8 * math.sin(n * math.pi * x), cls="g-c2")
        panels.append(p)
    q = Panel("Closed pipe: fundamental (λ/4)", "", "", xr=(0, 1), yr=(-1, 1))
    q.curve(lambda x: 0.8 * math.sin(math.pi / 2 * x))
    q.curve(lambda x: -0.8 * math.sin(math.pi / 2 * x), cls="g-c2")
    q.text(0.02, 0.85, "N (closed)", "start")
    q.text(0.98, 0.85, "A (open)", "end")
    panels.append(q)
    return figure(panels, "Nodes (N) where the envelope pinches; antinodes (A) at maximum amplitude.")


def g_field_sphere():
    a = Panel("Conducting / hollow sphere", "r", "E")
    a.poly([(0, 0), (0.35, 0)])
    a.curve(lambda r: 0.9 * (0.35 / r) ** 2, 0.35, 1)
    a.vline(0.35)
    a.text(0.35, 0, "R", "middle", dy=12)
    b = Panel("Uniformly charged solid sphere", "r", "E")
    b.poly([(0, 0), (0.35, 0.9)])
    b.curve(lambda r: 0.9 * (0.35 / r) ** 2, 0.35, 1)
    b.vline(0.35)
    b.text(0.35, 0, "R", "middle", dy=12)
    c = Panel("Potential of a conducting sphere", "r", "V")
    c.poly([(0, 0.8), (0.35, 0.8)])
    c.curve(lambda r: 0.8 * 0.35 / r, 0.35, 1)
    c.vline(0.35)
    c.text(0.35, 0, "R", "middle", dy=12)
    return figure([a, b, c])


def g_vi():
    p = Panel("V–I characteristics", "V", "I", w=300)
    p.curve(lambda v: 0.85 * v)
    p.curve(lambda v: 0.05 * (math.exp(3.2 * v) - 1), 0, 1, cls="g-c2")
    p.text(0.72, 0.68, "ohmic (straight line)", "end")
    p.text(0.88, 0.95, "non-ohmic", "end")
    return figure([p])


def g_bwire():
    p = Panel("B of a long thick wire (radius R)", "r", "B", w=300)
    p.poly([(0, 0), (0.3, 0.9)])
    p.curve(lambda r: 0.9 * 0.3 / r, 0.3, 1)
    p.vline(0.3)
    p.text(0.3, 0, "R", "middle", dy=12)
    p.text(0.12, 0.62, "∝ r", "middle")
    p.text(0.65, 0.5, "∝ 1/r", "middle")
    return figure([p])


def g_lcr():
    p = Panel("Series LCR: current vs frequency", "ω", "I", w=300)
    f = lambda w, r: 1 / math.sqrt(r * r + (w * 1.0 - 0.25 / max(w, 1e-6)) ** 2)
    p.curve(lambda w: 0.9 * f(w, 0.08) / f(0.5, 0.08), 0.05, 1)
    p.curve(lambda w: 0.45 * f(w, 0.25) / f(0.5, 0.25), 0.05, 1, cls="g-c2")
    p.vline(0.5)
    p.text(0.5, 0, "ω₀ = 1/√LC", "middle", dy=12)
    p.text(0.56, 0.9, "small R: sharp", "start")
    p.text(0.72, 0.36, "large R: broad", "start")
    return figure([p])


def g_prism():
    p = Panel("Angle of deviation vs angle of incidence", "i", "δ", w=300)
    p.curve(lambda i: 0.3 + 1.6 * (i - 0.45) ** 2, 0.08, 0.95)
    p.hline(0.3, 0, 0.45)
    p.vline(0.45, 0, 0.3)
    p.text(0.02, 0.33, "δₘ", "start")
    p.text(0.45, 0, "i = e", "middle", dy=12)
    return figure([p])


def g_ydse():
    a = Panel("YDSE: I = 4I₀cos²(φ/2)", "y", "I", xr=(-1, 1))
    a.curve(lambda y: 0.9 * math.cos(3 * math.pi * y) ** 2, n=300)
    a.text(0, 0.95, "equal-width fringes, β = λD/d", "middle", dy=-2)
    b = Panel("Single slit: central max twice as wide", "y", "I", xr=(-1, 1))

    def s(y):
        u = 3.2 * math.pi * y
        return 0.9 * (math.sin(u) / u) ** 2 if abs(u) > 1e-6 else 0.9

    b.curve(s, n=300)
    return figure([a, b])


def g_photo():
    a = Panel("Photocurrent vs V: intensity", "V", "I", xr=(-0.4, 1))
    a.curve(lambda v: 0.85 * (1 - math.exp(-6 * (v + 0.3))) if v > -0.3 else 0, -0.4, 1)
    a.curve(lambda v: 0.45 * (1 - math.exp(-6 * (v + 0.3))) if v > -0.3 else 0, -0.4, 1, cls="g-c2")
    a.text(-0.3, 0, "−V₀", "middle", dy=12)
    a.text(0.95, 0.9, "I₂ > I₁", "end")
    b = Panel("Photocurrent vs V: frequency", "V", "I", xr=(-0.6, 1))
    b.curve(lambda v: 0.7 * (1 - math.exp(-6 * (v + 0.5))) if v > -0.5 else 0, -0.6, 1)
    b.curve(lambda v: 0.7 * (1 - math.exp(-6 * (v + 0.25))) if v > -0.25 else 0, -0.6, 1, cls="g-c2")
    b.text(-0.5, 0, "ν₂", "middle", dy=12)
    b.text(-0.25, 0, "ν₁", "middle", dy=12)
    c = Panel("Stopping potential vs frequency", "ν", "V₀", yr=(-0.3, 1))
    c.curve(lambda n: 1.2 * (n - 0.3), 0.3, 1)
    c.curve(lambda n: 1.2 * (n - 0.3), 0, 0.3, dash=True, cls="g-c2")
    c.text(0.3, 0, "ν₀", "middle", dy=12)
    c.text(0.7, 0.72, "slope = h/e", "end")
    return figure([a, b, c])


def g_be():
    p = Panel("Binding energy per nucleon vs mass number", "A", "BE/A (MeV)", xr=(0, 250), yr=(0, 10), w=320)

    def be(A):
        Z = A / (2 + 0.0155 * A ** (2 / 3))
        E = 15.8 * A - 18.3 * A ** (2 / 3) - 0.714 * Z * (Z - 1) / A ** (1 / 3) - 23.2 * (A - 2 * Z) ** 2 / A
        return E / A

    p.curve(be, 8, 245)
    for A, v, lab in [(4, 7.07, "⁴He"), (56, 8.79, "⁵⁶Fe (peak)"), (238, 7.57, "²³⁸U")]:
        p.dot(A, v)
        p.text(A, v, lab, "start" if A < 200 else "end", dx=4 if A < 200 else -4, dy=-6)
    p.text(30, 2.2, "fusion releases energy ←", "start")
    p.text(245, 5.8, "→ fission releases energy", "end")
    for yv in (2, 4, 6, 8):
        p.text(0, yv, str(yv), "end", cls="g-tick", dx=-3, dy=3)
    for xv in (50, 100, 150, 200):
        p.text(xv, 0, str(xv), "middle", cls="g-tick", dy=10)
    return figure([p])


def g_diode():
    p = Panel("p–n junction / Zener diode I–V", "V", "I", xr=(-1, 1), yr=(-1, 1), w=320)
    p.curve(lambda v: min(0.95, 0.02 * (math.exp(9 * (v - 0.25)) - 0.0)) if v > 0 else 0, 0, 0.72)
    p.curve(lambda v: -0.03, -0.72, 0, cls="g-c1")
    p.poly([(-0.72, -0.03), (-0.75, -0.95)])
    p.text(0.45, 0.2, "knee ≈ 0.7 V (Si)", "start")
    p.text(-0.7, -0.6, "breakdown (−V_Z)", "start", dx=6)
    p.text(-0.2, -0.13, "tiny reverse current", "end")
    return figure([p])


# ============================================================ chemistry graphs
def g_radial():
    a = Panel("1s: radial probability 4πr²ψ²", "r (units of a₀)", "P(r)", xr=(0, 8))
    f1 = lambda r: r * r * math.exp(-2 * r)
    m1 = f1(1)
    a.curve(lambda r: 0.9 * f1(r) / m1)
    a.vline(1, 0, 0.9)
    a.text(1, 0, "a₀", "middle", dy=12)
    b = Panel("2s: one radial node", "r (units of a₀)", "P(r)", xr=(0, 14))
    f2 = lambda r: r * r * (2 - r) ** 2 * math.exp(-r)
    m2 = max(f2(x / 10) for x in range(1, 140))
    b.curve(lambda r: 0.9 * f2(r) / m2)
    b.text(2, 0, "node", "middle", dy=12)
    return figure([a, b])


def g_raoult():
    a = Panel("Ideal solution", "x_B", "p")
    a.poly([(0, 0.55), (1, 0.9)])
    a.poly([(0, 0.55), (1, 0)], cls="g-c2", dash=True)
    a.poly([(0, 0), (1, 0.9)], cls="g-c2", dash=True)
    b = Panel("Positive deviation", "x_B", "p")
    b.curve(lambda x: 0.55 + 0.35 * x + 0.35 * x * (1 - x) * 1.6)
    b.poly([(0, 0.55), (1, 0.9)], cls="g-c3", dash=True)
    c = Panel("Negative deviation", "x_B", "p")
    c.curve(lambda x: 0.55 + 0.35 * x - 0.35 * x * (1 - x) * 1.6)
    c.poly([(0, 0.55), (1, 0.9)], cls="g-c3", dash=True)
    return figure([a, b, c], "Solid line: total vapour pressure. Dashed: ideal (Raoult) behaviour for comparison.")


def g_conduct():
    p = Panel("Molar conductivity vs √C", "√C", "Λm", w=300)
    p.curve(lambda c: 0.85 - 0.35 * c)
    p.curve(lambda c: 0.12 + 0.8 * math.exp(-14 * c), 0.02, 1, cls="g-c2")
    p.text(0.98, 0.54, "strong electrolyte (KCl): linear", "end")
    p.text(0.12, 0.93, "weak electrolyte (CH₃COOH)", "start")
    return figure([p])


def g_kinetics():
    a = Panel("Zero order: [A] vs t", "t", "[A]")
    a.curve(lambda t: 0.9 - 0.8 * t)
    a.text(0.55, 0.62, "slope = −k", "start")
    b = Panel("First order: ln[A] vs t", "t", "ln[A]")
    b.curve(lambda t: 0.9 - 0.7 * t)
    b.text(0.55, 0.65, "slope = −k", "start")
    c = Panel("First order: [A] vs t", "t", "[A]")
    c.curve(lambda t: 0.9 * math.exp(-3 * t))
    c.hline(0.45, 0, 0.231)
    c.vline(0.231, 0, 0.45)
    c.text(0.231, 0, "t½", "middle", dy=12)
    d = Panel("Arrhenius: ln k vs 1/T", "1/T", "ln k")
    d.curve(lambda t: 0.9 - 0.75 * t)
    d.text(0.5, 0.65, "slope = −Eₐ/R", "start")
    return figure([a, b, c, d])


# ============================================================ data charts
def c_p99():
    rows = [("2025 · January", 147, 177, "~147", "~177"), ("2025 · April", 160, 203, "~160", "~203"), ("2026 · January", 155, 193, "~155", "~190–195"), ("2026 · April", 151, 191, "~151", "~191")]
    w, h = 560, 190
    x0, x1 = 130, 220
    left, right, top = 118, 24, 26

    def X(v):
        return left + (v - x0) / (x1 - x0) * (w - left - right)

    parts = []
    for v in range(130, 221, 10):
        parts.append(f'<line class="g-grid" x1="{X(v):.1f}" y1="{top - 8}" x2="{X(v):.1f}" y2="{h - 26}"/>'
                     f'<text class="g-tick" x="{X(v):.1f}" y="{h - 12}" text-anchor="middle">{v}</text>')
    for i, (lab, lo, hi, llo, lhi) in enumerate(rows):
        y = top + i * 34 + 8
        parts.append(f'<text class="g-lab g-strong" x="{left - 10}" y="{y + 5}" text-anchor="end">{_esc(lab)}</text>')
        parts.append(f'<rect class="g-bar" x="{X(lo):.1f}" y="{y - 7}" width="{X(hi) - X(lo):.1f}" height="14" rx="4"/>')
        parts.append(f'<text class="g-lab" x="{X(lo) - 5:.1f}" y="{y + 4}" text-anchor="end">{llo}</text>'
                     f'<text class="g-lab" x="{X(hi) + 5:.1f}" y="{y + 4}" text-anchor="start">{lhi}</text>')
    parts.append(f'<line class="g-target" x1="{X(200):.1f}" y1="{top - 14}" x2="{X(200):.1f}" y2="{h - 26}"/>'
                 f'<text class="g-lab g-strong" x="{X(200) + 4:.1f}" y="{top - 16}" text-anchor="start">planning target: 200+</text>')
    parts.append(f'<text class="g-axlab" x="{w - right}" y="{h - 1}" text-anchor="end">raw marks out of 300 (toughest → easiest shift)</text>')
    svg = f'<svg class="gchart" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'
    return (f'<figure class="graph chart">{svg}<figcaption>Approximate raw marks for ~99 percentile, by session. '
            f'Each bar spans the toughest to the easiest shift (third-party analyses; see Sources). Not official NTA data.</figcaption></figure>')


def bar_chart(rows, title, unit="typical questions per shift (range)", maxv=3.5, subject="general"):
    """rows: (label, lo, hi). Horizontal range bars with midpoint dot."""
    w = 560
    rowh = 17
    top, left, right = 16, 190, 30
    h = top + rowh * len(rows) + 30

    def X(v):
        return left + v / maxv * (w - left - right)

    parts = []
    for v in [0, 1, 2, 3]:
        parts.append(f'<line class="g-grid" x1="{X(v):.1f}" y1="{top - 6}" x2="{X(v):.1f}" y2="{h - 24}"/>'
                     f'<text class="g-tick" x="{X(v):.1f}" y="{h - 12}" text-anchor="middle">{v}</text>')
    for i, (lab, lo, hi) in enumerate(rows):
        y = top + i * rowh + 6
        parts.append(f'<text class="g-lab" x="{left - 8}" y="{y + 4}" text-anchor="end">{_esc(lab)}</text>')
        x_lo = X(lo)
        wid = max(X(hi) - X(lo), 6)
        parts.append(f'<rect class="g-bar g-bar-{subject}" x="{x_lo:.1f}" y="{y - 5}" width="{wid:.1f}" height="10" rx="4"/>')
        parts.append(f'<text class="g-lab" x="{x_lo + wid + 5:.1f}" y="{y + 4}" text-anchor="start">{lo:g}–{hi:g}</text>' if hi != lo else
                     f'<text class="g-lab" x="{x_lo + wid + 5:.1f}" y="{y + 4}" text-anchor="start">{lo:g}</text>')
    parts.append(f'<text class="g-axlab" x="{w - right}" y="{h - 1}" text-anchor="end">{_esc(unit)}</text>')
    svg = f'<svg class="gchart" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'
    return f'<figure class="graph chart">{svg}<figcaption>{title}</figcaption></figure>'


PHY_ROWS = [("Units & Measurements", 1, 2), ("Kinematics", 1, 1), ("Laws of Motion", 1, 1), ("Work, Energy, Power", 1, 2),
            ("Rotational Motion", 1, 2), ("Gravitation", 1, 2), ("Solids & Liquids + Thermal", 2, 3), ("Thermodynamics", 1, 2),
            ("Kinetic Theory", 1, 1), ("Oscillations & Waves", 1, 2), ("Electrostatics", 2, 3), ("Current Electricity", 2, 3),
            ("Magnetism", 2, 3), ("EMI & AC", 1, 2), ("EM Waves", 1, 1), ("Optics", 2, 3), ("Dual Nature", 1, 1),
            ("Atoms & Nuclei", 1, 2), ("Electronic Devices", 1, 2), ("Experimental Skills (direct)", 0, 2)]
CHEM_ROWS = [("Basic Concepts", 1, 1), ("Atomic Structure", 1, 2), ("Chemical Bonding", 1, 2), ("Thermodynamics", 1, 2),
             ("Solutions", 1, 1), ("Equilibrium", 1, 2), ("Redox & Electrochemistry", 1, 2), ("Chemical Kinetics", 1, 2),
             ("Periodicity", 1, 1), ("p-Block", 1, 2), ("d- & f-Block", 1, 2), ("Coordination Compounds", 2, 3),
             ("Purification & Analysis", 0, 1), ("GOC", 1, 2), ("Hydrocarbons", 1, 1), ("Halogen compounds", 1, 1),
             ("Oxygen compounds", 2, 3), ("Nitrogen compounds", 1, 1), ("Biomolecules", 1, 1), ("Practical Chemistry", 1, 1)]
MATH_ROWS = [("Sets, Relations, Functions", 1, 2), ("Complex & Quadratics", 2, 3), ("Matrices & Determinants", 2, 3),
             ("Permutations & Combinations", 1, 2), ("Binomial Theorem", 1, 2), ("Sequences & Series", 1, 2),
             ("Limits, Continuity, Differentiability", 2, 3), ("Integral Calculus", 2, 3), ("Differential Equations", 1, 2),
             ("Coordinate Geometry", 3, 4), ("3D Geometry", 1, 2), ("Vector Algebra", 1, 2),
             ("Statistics & Probability", 2, 3), ("Trigonometry", 1, 1)]


def render(name: str, subject: str = "general") -> str:
    table = {
        "kin-graphs": g_kin, "friction-graph": g_friction, "pe-curve": g_pe, "gravity-g-r": g_gravity,
        "stress-strain": g_stress, "newton-cooling": g_cooling, "pv-processes": g_pv, "maxwell": g_maxwell,
        "shm-energy": g_shm, "standing-waves": g_standing, "field-sphere": g_field_sphere, "vi-ohmic": g_vi,
        "b-field-wire": g_bwire, "lcr-resonance": g_lcr, "prism-deviation": g_prism, "ydse-intensity": g_ydse,
        "photoelectric": g_photo, "be-curve": g_be, "diode-iv": g_diode, "radial-probability": g_radial,
        "raoult-deviation": g_raoult, "conductivity": g_conduct, "kinetics-plots": g_kinetics,
        "p99-ranges": c_p99,
        "pyq-physics": lambda: bar_chart(PHY_ROWS, "Physics: typical questions per shift by unit (compiled from 2024–2026 third-party PYQ analyses; approximate).", maxv=4, subject="physics"),
        "pyq-chemistry": lambda: bar_chart(CHEM_ROWS, "Chemistry: typical questions per shift by unit (compiled from 2024–2026 third-party PYQ analyses; approximate).", maxv=4, subject="chemistry"),
        "pyq-maths": lambda: bar_chart(MATH_ROWS, "Mathematics: typical questions per shift by unit (compiled from 2024–2026 third-party PYQ analyses; approximate).", maxv=4.5, subject="maths"),
    }
    fn = table.get(name)
    if fn is None:
        return f'<div class="missing">[graph {name} missing]</div>'
    return fn()


# ============================================================ QR codes
def qr_svg(url: str) -> str:
    q = segno.make(url, error="m")
    buf = io.BytesIO()
    q.save(buf, kind="svg", scale=4, border=1, dark="#1b1f3b", light=None, xmldecl=False, svgns=True, nl=False)
    s = buf.getvalue().decode()
    return s.replace("<svg ", '<svg class="qr" ', 1)


def qr_row(items) -> str:
    cells = "".join(f'<a class="qrcell" href="{_esc(u)}">{qr_svg(u)}<span class="qr-l">{_esc(l)}</span>'
                    f'<span class="qr-u">{_esc(u.replace("https://", ""))}</span></a>' for u, l in items)
    return f'<div class="qrrow">{cells}</div>'
