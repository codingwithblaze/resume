"""Markdown -> HTML converter for the JEE Main 99+ book.

Standard Markdown (markdown-it, CommonMark + tables) plus the custom
syntax documented in content/SYNTAX.md.
"""
from __future__ import annotations

import hashlib
import html
import random
import re
from dataclasses import dataclass, field

from markdown_it import MarkdownIt

import graphs
import icons

_md = MarkdownIt("commonmark", {"html": True, "typographer": False}).enable(["table", "strikethrough"])

# ---------------------------------------------------------------- math protection
_MATH_DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
_MATH_INLINE = re.compile(r"(?<![\\$])\$(?!\$)((?:\\\$|[^$])+?)\$")


class MathStore:
    def __init__(self):
        self.items: list[tuple[str, bool]] = []

    def protect(self, text: str) -> str:
        def disp(m):
            self.items.append((m.group(1).strip(), True))
            return f"QQMATH{len(self.items) - 1}QQ"

        def inl(m):
            self.items.append((m.group(1).strip(), False))
            return f"QQMATH{len(self.items) - 1}QQ"

        text = _MATH_DISPLAY.sub(disp, text)
        text = _MATH_INLINE.sub(inl, text)
        return text

    def restore(self, s: str) -> str:
        def rep(m):
            tex, display = self.items[int(m.group(1))]
            cls = "math math-display" if display else "math math-inline"
            tag = "div" if display else "span"
            return f'<{tag} class="{cls}">{html.escape(tex)}</{tag}>'

        # a display formula alone in a paragraph: drop the wrapping <p>
        s = re.sub(r"<p>\s*(QQMATH(\d+)QQ)\s*</p>", lambda m: m.group(1) if self.items[int(m.group(2))][1] else m.group(0), s)
        return re.sub(r"QQMATH(\d+)QQ", rep, s)


# ---------------------------------------------------------------- context
@dataclass
class Question:
    qid: str
    diff: str
    time: str
    concept: str
    tags: list[str]
    text: str
    options: list[tuple[str, str]]
    ans: str
    sol: str = ""
    short: str = ""
    trap: str = ""
    number: int = 0
    set_name: str = ""


@dataclass
class Ctx:
    chapter_id: str = "x"
    subject: str = "general"
    sets: list[tuple[str, list[Question]]] = field(default_factory=list)
    pending: list[tuple[str, list[Question]]] = field(default_factory=list)  # since last @@SOLUTIONS
    key_pending: list[tuple[str, list[Question]]] = field(default_factory=list)  # since last @@ANSWERKEY
    heading_ids: list[tuple[int, str, str]] = field(default_factory=list)  # (level, id, plain title)
    cb_counter: int = 0
    slug_counter: int = 0
    all_questions: list[Question] = field(default_factory=list)
    ans_counts: dict = field(default_factory=lambda: {k: 0 for k in "ABCD"})


# ---------------------------------------------------------------- inline tokens
_TAGS = {
    "verified": ("tag-verified", "Verified"),
    "third": ("tag-third", "Third-party analysis"),
    "rec": ("tag-rec", "Recommendation"),
}
_DIFF = {"E": ("diff-e", "Easy"), "M": ("diff-m", "Medium"), "H": ("diff-h", "Hard")}


def inline_tokens(s: str, ctx: Ctx) -> str:
    def tag(m):
        cls, label = _TAGS.get(m.group(1), ("tag-rec", m.group(1)))
        return f'<span class="tag {cls}">{icons.small(m.group(1))}{label}</span>'

    s = re.sub(r"\{\{tag:(\w+)\}\}", tag, s)
    s = re.sub(r"\{\{diff:(\w)\}\}", lambda m: f'<span class="pill {_DIFF[m.group(1)][0]}">{_DIFF[m.group(1)][1]}</span>', s)

    def fld(m):
        key, width = m.group(1), m.group(2) or "40"
        return f'<a class="fld" href="https://fld.local/{key}" style="width:{width}mm"></a>'

    s = re.sub(r"\{\{field:([\w-]+)(?::(\d+))?\}\}", fld, s)
    s = re.sub(r"\{\{blank(?::(\d+))?\}\}", lambda m: f'<span class="blank" style="width:{m.group(1) or 30}mm"></span>', s)

    def pref(m):
        rid = m.group(1)
        return f'<a class="pref" href="#{rid}"><span class="pnum" data-ref="{rid}">000</span></a>'

    s = re.sub(r"\[\[([\w-]+)\]\]", pref, s)

    def cb(_m):
        ctx.cb_counter += 1
        return f'<a class="cb" href="https://cb.local/{ctx.chapter_id}-{ctx.cb_counter}"></a>'

    s = s.replace("[ ]", "\x00CB\x00")
    s = re.sub("\x00CB\x00", cb, s)
    return s


def slugify(text: str) -> str:
    t = re.sub(r"<[^>]+>", "", text)
    t = re.sub(r"QQMATH\d+QQ", "", t)
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:40] or "s"


def plain(text: str) -> str:
    t = re.sub(r"<[^>]+>", "", text)
    return html.unescape(t).strip()


# ---------------------------------------------------------------- markdown chunk
def md_chunk(text: str, ctx: Ctx, inline: bool = False) -> str:
    ms = MathStore()
    t = ms.protect(text)
    out = _md.renderInline(t) if inline else _md.render(t)

    # headings with explicit ids / auto ids
    def head(m):
        level, content = int(m.group(1)), m.group(2)
        mid = re.search(r"\s*\{#([\w-]+)\}\s*$", content)
        if mid:
            hid = mid.group(1)
            content = content[: mid.start()]
        else:
            ctx.slug_counter += 1
            hid = f"{ctx.chapter_id}-{slugify(content)}-{ctx.slug_counter}"
        title_plain = plain(ms.restore(content)) if "QQMATH" not in content else plain(re.sub(r"QQMATH\d+QQ", "…", content))
        ctx.heading_ids.append((level, hid, title_plain))
        return (f'<h{level} id="{hid}"><a class="probe" href="https://probe.local/{hid}">{content}</a></h{level}>')

    out = re.sub(r"<h([1-6])>(.*?)</h\1>", head, out, flags=re.S)
    # tables: wrap for styling
    out = out.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    out = inline_tokens(out, ctx)
    out = ms.restore(out)
    return out


# ---------------------------------------------------------------- containers
BOX_TYPES = {
    "formula": "Formula",
    "shortcut": "Shortcut",
    "important": "Important",
    "trap": "Mistake Alert",
    "pyq": "PYQ Pattern",
    "revision": "Revision",
    "practice": "Practice",
    "mock": "Mock Test",
    "warning": "Warning",
    "fact": "Verified Fact",
    "strategy": "Strategy",
    "note": "Note",
    "def": "Definition",
    "graph": "Graph",
    "example": "Example",
    "tip": "Tip",
}


def render_container(kind: str, title: str, body: str, ctx: Ctx) -> str:
    if kind == "stats":
        tiles = []
        for line in body.strip().splitlines():
            if "|" not in line:
                continue
            lab, val = [x.strip() for x in line.split("|", 1)]
            tiles.append(f'<div class="stat"><div class="stat-v">{md_chunk(val, ctx, True)}</div>'
                         f'<div class="stat-l">{md_chunk(lab, ctx, True)}</div></div>')
        return f'<div class="stats">{"".join(tiles)}</div>'
    if kind in ("grid2", "grid3", "cols2", "cols3"):
        parts = re.split(r"^\+\+\+\s*$", body, flags=re.M)
        n = kind[-1]
        cls = "grid" if kind.startswith("grid") else "cols"
        cells = "".join(f'<div class="cell">{render_block(p, ctx)}</div>' for p in parts)
        return f'<div class="{cls} {cls}{n}">{cells}</div>'
    if kind == "flow":
        steps = []
        for i, line in enumerate([l for l in body.strip().splitlines() if l.strip()], 1):
            head, _, txt = line.partition("|")
            steps.append(f'<div class="step"><div class="step-n">{i}</div><div class="step-b">'
                         f'<div class="step-h">{md_chunk(head.strip(), ctx, True)}</div>'
                         f'<div class="step-t">{md_chunk(txt.strip(), ctx, True)}</div></div></div>')
        return f'<div class="flow">{"".join(steps)}</div>'
    if kind == "rmap":
        rows = []
        for line in [l for l in body.strip().splitlines() if l.strip()]:
            reag, _, prod = line.partition("|")
            rows.append(f'<div class="rm-row"><div class="rm-arrow"><span class="rm-reag">{md_chunk(reag.strip(), ctx, True)}</span></div>'
                        f'<div class="rm-prod">{md_chunk(prod.strip(), ctx, True)}</div></div>')
        t_html = md_chunk(title, ctx, True) if title else ""
        return (f'<div class="rmap"><div class="rm-head">{icons.box("rmap")}<span class="box-label">Reaction Map</span>'
                f'<span class="box-title">{t_html}</span></div><div class="rm-rows">{"".join(rows)}</div></div>')
    if kind == "mindmap":
        branches = []
        for line in [l for l in body.strip().splitlines() if l.strip()]:
            b, _, leaves = line.partition(":")
            items = "".join(f"<li>{md_chunk(x.strip(), ctx, True)}</li>" for x in leaves.split(";") if x.strip())
            branches.append(f'<div class="mm-branch"><div class="mm-bh">{md_chunk(b.strip(), ctx, True)}</div><ul>{items}</ul></div>')
        return (f'<div class="mindmap"><div class="mm-centre">{md_chunk(title, ctx, True)}</div>'
                f'<div class="mm-branches">{"".join(branches)}</div></div>')
    label = BOX_TYPES.get(kind, kind.title())
    t_html = f'<span class="box-title">{md_chunk(title, ctx, True)}</span>' if title else ""
    return (f'<div class="box box-{kind}"><div class="box-head">{icons.box(kind)}<span class="box-label">{label}</span>{t_html}</div>'
            f'<div class="box-body">{render_block(body, ctx)}</div></div>')


# ---------------------------------------------------------------- questions
_OPT = re.compile(r"^\(([A-D])\)\s*(.*)$")


def parse_question(header: str, lines: list[str]) -> Question:
    parts = [p.strip() for p in header.split("|")]
    while len(parts) < 5:
        parts.append("")
    qid, diff, time, concept, tags = parts[:5]
    q_lines, options, fields = [], [], {"ans": [], "sol": [], "short": [], "trap": []}
    cur = None
    for line in lines:
        m = re.match(r"^@(ans|sol|short|trap)\b\s?(.*)$", line)
        if m:
            cur = m.group(1)
            fields[cur].append(m.group(2))
            continue
        if cur:
            fields[cur].append(line)
            continue
        mo = _OPT.match(line.strip())
        if mo:
            options.append((mo.group(1), mo.group(2)))
        elif options and line.strip():
            letter, txt = options[-1]
            options[-1] = (letter, txt + " " + line.strip())
        else:
            q_lines.append(line)
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    return Question(qid=qid, diff=diff or "M", time=time, concept=concept, tags=tag_list,
                    text="\n".join(q_lines).strip(), options=options,
                    ans="\n".join(fields["ans"]).strip(), sol="\n".join(fields["sol"]).strip(),
                    short="\n".join(fields["short"]).strip(), trap="\n".join(fields["trap"]).strip())


# Hand-written MCQs drift toward (B). Spread keys evenly across A-D by swapping
# the correct option into a target slot (chosen per chapter, weighted toward
# the least-used letters) and remapping "(X)" references in sol/short/trap.
_POSITIONAL = re.compile(r"of the above|\([A-D]\)|\b[A-D] and [A-D]\b|\bA and R\b", re.I)
_LETTER_REF = re.compile(r"(?<![A-Za-z0-9\\_^])\(([A-D])\)")


def balance_answer(q: Question, ctx: Ctx) -> None:
    letters = [o[0] for o in q.options]
    if letters != list("ABCD") or q.ans not in "ABCD" or len(q.ans) != 1:
        return
    if any(_POSITIONAL.search(t) for _, t in q.options):
        ctx.ans_counts[q.ans] += 1
        return
    rng = random.Random(int(hashlib.md5(q.qid.encode()).hexdigest(), 16))
    counts = ctx.ans_counts
    weights = [1.0 / (1 + counts[k]) ** 3 for k in "ABCD"]
    target = rng.choices("ABCD", weights=weights)[0]
    counts[target] += 1
    src = q.ans
    if target == src:
        return
    texts = dict(q.options)
    texts[src], texts[target] = texts[target], texts[src]
    q.options = [(k, texts[k]) for k in "ABCD"]
    swap = {src: target, target: src}
    fix = lambda s: _LETTER_REF.sub(lambda m: f"({swap.get(m.group(1), m.group(1))})", s)
    q.sol, q.short, q.trap = fix(q.sol), fix(q.short), fix(q.trap)
    q.ans = target


def _opt_layout(options) -> str:
    def mlen(tex):
        t = re.sub(r"\\ce\{(.*)\}", r"\1", tex)
        t = re.sub(r"\\(?:dfrac|frac|tfrac)", "", t)
        t = re.sub(r"\\[a-zA-Z]+", "x", t)
        t = re.sub(r"[{}^_\\ ]", "", t)
        return int(len(t) * 1.1) + 1

    def plen(s):
        total = 0
        for part in re.split(r"(\$[^$]*\$)", s):
            total += mlen(part[1:-1]) if part.startswith("$") and part.endswith("$") and len(part) > 1 else len(part)
        return total

    mx = max((plen(o[1]) for o in options), default=0)
    if mx <= 16:
        return "opts4"
    if mx <= 42:
        return "opts2"
    return "opts1"


def _meta_pills(q: Question) -> str:
    cls, label = _DIFF.get(q.diff, ("diff-m", q.diff))
    pills = [f'<span class="pill {cls}">{label}</span>']
    if q.time:
        pills.append(f'<span class="pill pill-time">{icons.small("clock")}{q.time} min</span>')
    for t in q.tags:
        tcls = "pill-nv" if t.upper() == "NV" else "pill-tag"
        pills.append(f'<span class="pill {tcls}">{html.escape(t)}</span>')
    return "".join(pills)


def render_question(q: Question, ctx: Ctx) -> str:
    opts = ""
    if q.options:
        layout = _opt_layout(q.options)
        items = "".join(f'<div class="opt"><span class="opt-l">{l}</span><span class="opt-t">{md_chunk(t, ctx, True)}</span></div>' for l, t in q.options)
        opts = f'<div class="opts {layout}">{items}</div>'
    else:
        opts = '<div class="q-nvline">Your answer (numerical value): <span class="nvbox"></span></div>'
    return (f'<div class="q" id="q-{q.qid}"><div class="q-head"><span class="q-num">{q.number}</span>'
            f'<span class="q-meta">{_meta_pills(q)}</span><span class="q-id">{html.escape(q.qid)}</span></div>'
            f'<div class="q-text">{md_chunk(q.text, ctx)}</div>{opts}</div>')


def _ans_label(q: Question) -> str:
    a = q.ans.strip()
    return f"({a})" if re.fullmatch(r"[A-D]", a) else a


def render_solutions(sets, ctx: Ctx) -> str:
    out = []
    for name, qs in sets:
        out.append(f'<div class="sol-set">{html.escape(name)}</div>')
        for q in qs:
            body = []
            sol = q.sol if q.sol and q.sol != "—" else "Direct recall: see the concept summary and formula box of this chapter."
            body.append(f'<div class="sol-line"><span class="sol-k">Solution</span>{md_chunk(sol, ctx, True)}</div>')
            if q.short and q.short != "—":
                body.append(f'<div class="sol-line sol-short"><span class="sol-k">Shortcut</span>{md_chunk(q.short, ctx, True)}</div>')
            if q.trap and q.trap != "—":
                body.append(f'<div class="sol-line sol-trap"><span class="sol-k">Common trap</span>{md_chunk(q.trap, ctx, True)}</div>')
            concept = md_chunk(q.concept, ctx, True) if q.concept else ""
            out.append(f'<div class="sol"><div class="sol-head"><span class="q-num">{q.number}</span>'
                       f'<span class="sol-ans">Answer: {md_chunk(_ans_label(q), ctx, True)}</span>'
                       f'<span class="sol-concept">{concept}</span><span class="q-meta">{_meta_pills(q)}</span>'
                       f'<span class="q-id">{html.escape(q.qid)}</span></div>{"".join(body)}</div>')
    return f'<div class="solutions">{"".join(out)}</div>'


def render_answerkey(sets, ctx: Ctx) -> str:
    blocks = []
    for name, qs in sets:
        cells = "".join(f'<div class="ak-cell"><span class="ak-n">{q.number}</span><span class="ak-a">{md_chunk(_ans_label(q), ctx, True)}</span></div>' for q in qs)
        blocks.append(f'<div class="ak"><div class="ak-h">{html.escape(name)}</div><div class="ak-grid">{cells}</div></div>')
    return f'<div class="answerkey">{"".join(blocks)}</div>'


# ---------------------------------------------------------------- block renderer
def render_block(text: str, ctx: Ctx) -> str:
    lines = text.split("\n")
    out: list[str] = []
    buf: list[str] = []

    def flush():
        if buf:
            chunk = "\n".join(buf)
            if chunk.strip():
                out.append(md_chunk(chunk, ctx))
            buf.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith(":::") and s != ":::":
            flush()
            head = s[3:].strip()
            kind, _, title = head.partition(" ")
            inner, depth = [], 1
            i += 1
            while i < len(lines):
                l2 = lines[i].strip()
                if l2.startswith(":::") and l2 != ":::":
                    depth += 1
                elif l2 == ":::":
                    depth -= 1
                    if depth == 0:
                        break
                inner.append(lines[i])
                i += 1
            out.append(render_container(kind, title.strip(), "\n".join(inner), ctx))
            i += 1
            continue
        if s.startswith("@@Q "):
            flush()
            header = s[4:]
            body = []
            i += 1
            while i < len(lines) and lines[i].strip() != "@@END":
                body.append(lines[i])
                i += 1
            q = parse_question(header, body)
            balance_answer(q, ctx)
            if not ctx.sets:
                ctx.sets.append(("Questions", []))
                ctx.pending.append(ctx.sets[-1])
                ctx.key_pending.append(ctx.sets[-1])
            qs = ctx.sets[-1][1]
            q.number = len(qs) + 1
            q.set_name = ctx.sets[-1][0]
            qs.append(q)
            ctx.all_questions.append(q)
            out.append(render_question(q, ctx))
            i += 1
            continue
        if s.startswith("@@SET"):
            flush()
            name = s[5:].strip()
            entry = (name, [])
            ctx.sets.append(entry)
            ctx.pending.append(entry)
            ctx.key_pending.append(entry)
            out.append(f'<div class="set-head">{icons.box("practice")}<span>{html.escape(name)}</span></div>')
            i += 1
            continue
        if s == "@@SOLUTIONS":
            flush()
            out.append(render_solutions(ctx.pending, ctx))
            ctx.pending = []
            i += 1
            continue
        if s == "@@ANSWERKEY":
            flush()
            out.append(render_answerkey(ctx.key_pending, ctx))
            ctx.key_pending = []
            i += 1
            continue
        if s == "@@PAGEBREAK":
            flush()
            out.append('<div class="pb"></div>')
            i += 1
            continue
        if s.startswith("@@GRAPH ") or s.startswith("@@CHART "):
            flush()
            out.append(graphs.render(s.split(None, 1)[1].strip(), ctx.subject))
            i += 1
            continue
        if s.startswith("@@QR "):
            flush()
            qrs = []
            while i < len(lines) and lines[i].strip().startswith("@@QR "):
                url, _, label = lines[i].strip()[5:].partition("|")
                qrs.append((url.strip(), label.strip()))
                i += 1
            out.append(graphs.qr_row(qrs))
            continue
        buf.append(line)
        i += 1
    flush()
    return "".join(out)


def split_chapters(text: str) -> list[tuple[str, str, str]]:
    """Split a file into (id, title, body) at top-level '# ' headings."""
    chapters = []
    cur_id, cur_title, cur_lines = None, None, []
    in_q = False
    for line in text.split("\n"):
        if line.startswith("@@Q "):
            in_q = True
        elif line.strip() == "@@END":
            in_q = False
        m = re.match(r"^# (.+?)\s*\{#([\w-]+)\}\s*$", line) if not in_q else None
        if m:
            if cur_id is not None:
                chapters.append((cur_id, cur_title, "\n".join(cur_lines)))
            cur_id, cur_title, cur_lines = m.group(2), m.group(1), []
        else:
            cur_lines.append(line)
    if cur_id is not None:
        chapters.append((cur_id, cur_title, "\n".join(cur_lines)))
    return chapters
