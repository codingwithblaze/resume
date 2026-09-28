"""Book structure, cover, part dividers and table of contents."""
from __future__ import annotations

import html
import math
import os
import re

import md

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")

TITLE = "JEE MAIN 99+"
SYSTEM = "The Complete Personalized Preparation System"
SUBTITLE = "A Personalized Strategy, Formula, PYQ, Practice, Revision & Mock-Test Handbook"
AUTHOR = "BM Excel Blaze"
PRICE = "₹1,499"
EDITION = "JEE Main 2027 Edition"
YEAR = "2026"
FEATURES = [("1,000+", "original questions"), ("54", "chapter modules"), ("2", "full-length mocks"),
            ("30–180", "day study plans"), ("25+", "fillable trackers")]

SUBJECT_COLOURS = {"general": "#3b2e7e", "physics": "#2563a8", "chemistry": "#0f8a6a", "maths": "#8a3fa0",
                   "tools": "#3f51b5", "systems": "#b45309"}


def files(folder):
    d = os.path.join(CONTENT, folder)
    if not os.path.isdir(d):
        return []
    return [os.path.join(folder, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]


# (roman, title, subject, lead, [files])
MASTER_PARTS = [
    ("I", "Start Here", "general",
     "Welcome, verified exam facts, the 99+ roadmap and percentile strategy, your personal profile, the diagnostic test and the plan selector.",
     files("A_start")),
    ("II", "Physics", "physics",
     "Strategy for maximising Physics marks, then 20 unit modules: concepts, formulas, graphs, PYQ patterns, traps, shortcuts, practice sets and chapter tests.",
     files("B_physics")),
    ("III", "Chemistry", "chemistry",
     "Chemistry strategy and the NCERT method, then Physical, Inorganic and Organic modules with reaction maps, reagent tables and NCERT fact sheets.",
     files("C_chemistry")),
    ("IV", "Mathematics", "maths",
     "Mathematics strategy, then 14 unit modules: formulas, identities, standard results, question models, fast methods, practice sets and chapter tests.",
     files("D_maths")),
    ("V", "Master Formula Handbook", "tools",
     "Every formula, constant, identity, reaction and trend, organised for 1-day, 3-day, 7-day and final 24-hour revision.",
     files("E_formula")),
    ("VI", "Speed & Shortcut Manual", "tools",
     "Legitimate speed methods (when to use, when not to, time saved, common mistake) and the answer-choice strategy.",
     files("F_speed")),
    ("VII", "PYQ Intelligence", "tools",
     "Trend analysis through 2026, the PYQ Priority Matrix, master priority lists and a system for working through previous-year papers.",
     files("G_pyq")),
    ("VIII", "Question Bank & Mock Tests", "tools",
     "Mixed, calculation-heavy, tricky and time-pressure sets, two full-length original mock tests, and the mock-test system with analysis sheets.",
     files("H_practice")),
    ("IX", "Mistakes, Revision & Mindset", "systems",
     "The Mistake Book, the spaced revision system, and practical, evidence-based methods for focus, anxiety and consistency.",
     files("I_systems")),
    ("X", "Study Plans & Timetables", "systems",
     "30- to 180-day plans at 6, 8 and 10 hours a day, the final 30/14/7/3-day plans, daily timetables and the weekly system.",
     files("J_plans")),
    ("XI", "Exam Day", "systems",
     "Exam-eve and exam-day plans, the exam-hall protocol, subject-specific scoring strategies and the one-page Command Sheet.",
     files("K_examday")),
    ("XII", "Last-Minute Revision Book", "tools",
     "Compressed one-page sheets for Physics, Chemistry and Maths, reaction and shortcut sheets, and the final checklists.",
     files("L_lastminute")),
    ("XIII", "Trackers & Final Checklist", "systems",
     "Printable, fillable trackers for hours, chapters, questions, PYQs, mocks, accuracy, weak chapters, formulas and the Mistake Book.",
     files("M_trackers")),
    ("", "Sources & References", "general", "", files("N_sources")),
]

TABS = [("CONTENTS", "contents"), ("PHYSICS", "part-II"), ("CHEMISTRY", "part-III"), ("MATHS", "part-IV"),
        ("FORMULAS", "part-V"), ("PLANS", "part-X"), ("TRACKERS", "part-XIII")]


class Chapter:
    def __init__(self, cid, title, subject, part_roman, part_title, number, body_html, headings, questions):
        self.cid, self.title, self.subject = cid, title, subject
        self.part_roman, self.part_title, self.number = part_roman, part_title, number
        self.body_html, self.headings, self.questions = body_html, headings, questions


def title_html(title: str) -> str:
    return md.md_chunk(title, md.Ctx(), inline=True)


def plain_title(title: str) -> str:
    t = re.sub(r"\$[^$]*\$", "", title)
    t = re.sub(r"[*_`]", "", t)
    return html.unescape(t).strip()


def build_chapters(file_list, subject, part_roman, part_title):
    chapters = []
    for rel in file_list:
        text = open(os.path.join(CONTENT, rel), encoding="utf-8").read()
        base = os.path.basename(rel)
        num = base.split("_", 1)[0]
        for idx, (cid, title, body) in enumerate(md.split_chapters(text)):
            ctx = md.Ctx(chapter_id=cid, subject=subject)
            body_html = md.render_block(body, ctx)
            number = num if (subject in ("physics", "chemistry", "maths") and num != "00" and idx == 0) else ""
            chapters.append(Chapter(cid, title, subject, part_roman, part_title, number, body_html, ctx.heading_ids, ctx.all_questions))
    return chapters


# ---------------------------------------------------------------- decorative SVG
def _pattern_cover():
    parts = []
    cx, cy = 165, 58
    for i, ang in enumerate((0, 60, 120)):
        parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="58" ry="20" transform="rotate({ang} {cx} {cy})" fill="none" stroke="#e8c98a" stroke-opacity="{0.55 - i * 0.1}" stroke-width="0.5"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#e8c98a" fill-opacity="0.8"/>')
    for ang, r in ((20, 58), (140, 58), (260, 58)):
        a = math.radians(ang)
        parts.append(f'<circle cx="{cx + r * math.cos(a) * 0.98:.1f}" cy="{cy + 20 * math.sin(a):.1f}" r="1.6" fill="#ffffff" fill-opacity="0.8"/>')
    for gx in range(0, 211, 7):
        for gy in range(150, 297, 7):
            op = max(0, 0.22 - (gy - 150) / 900)
            parts.append(f'<circle cx="{gx}" cy="{gy}" r="0.35" fill="#ffffff" fill-opacity="{op:.3f}"/>')
    wave = " ".join(f"{x},{232 + 9 * math.sin(x / 13):.1f}" for x in range(0, 211, 2))
    wave2 = " ".join(f"{x},{240 + 6 * math.sin(x / 9 + 1):.1f}" for x in range(0, 211, 2))
    parts.append(f'<polyline points="{wave}" fill="none" stroke="#e8c98a" stroke-opacity="0.35" stroke-width="0.5"/>')
    parts.append(f'<polyline points="{wave2}" fill="none" stroke="#ffffff" stroke-opacity="0.2" stroke-width="0.4"/>')
    return f'<svg class="cv-pattern" viewBox="0 0 210 297" preserveAspectRatio="none">{"".join(parts)}</svg>'


def _pattern_divider(subject):
    p = []
    if subject == "physics":
        for k in range(9):
            pts = " ".join(f"{x},{40 + k * 28 + 7 * math.sin(x / 11 + k):.1f}" for x in range(0, 211, 2))
            p.append(f'<polyline points="{pts}" fill="none" stroke="#fff" stroke-opacity="{0.07 + 0.02 * (k % 3)}" stroke-width="0.5"/>')
    elif subject == "chemistry":
        s = 11
        for row in range(0, 22):
            for col in range(0, 13):
                x = col * s * 1.732 + (row % 2) * s * 0.866
                y = row * s * 1.5
                pts = " ".join(f"{x + s * math.cos(math.radians(60 * i + 30)):.1f},{y + s * math.sin(math.radians(60 * i + 30)):.1f}" for i in range(6))
                p.append(f'<polygon points="{pts}" fill="none" stroke="#fff" stroke-opacity="0.07" stroke-width="0.4"/>')
    elif subject == "maths":
        for x in range(0, 211, 10):
            p.append(f'<line x1="{x}" y1="0" x2="{x}" y2="297" stroke="#fff" stroke-opacity="0.06" stroke-width="0.3"/>')
        for y in range(0, 298, 10):
            p.append(f'<line x1="0" y1="{y}" x2="210" y2="{y}" stroke="#fff" stroke-opacity="0.06" stroke-width="0.3"/>')
        pts = " ".join(f"{x},{150 - 60 * math.sin(x / 30) * math.exp(-x / 260):.1f}" for x in range(0, 211, 2))
        p.append(f'<polyline points="{pts}" fill="none" stroke="#fff" stroke-opacity="0.25" stroke-width="0.6"/>')
    else:
        for gx in range(0, 211, 8):
            for gy in range(0, 297, 8):
                p.append(f'<circle cx="{gx}" cy="{gy}" r="0.4" fill="#fff" fill-opacity="0.12"/>')
    return f'<svg class="dv-pattern" viewBox="0 0 210 297" preserveAspectRatio="none">{"".join(p)}</svg>'


# ---------------------------------------------------------------- page elements
def cover_html(book_label: str, book_desc: str) -> str:
    chips = "".join(f'<span class="cv-chip"><i style="background:{c}"></i>{t}</span>' for t, c in
                    (("Physics", "#6aa6e8"), ("Chemistry", "#4cc9a0"), ("Mathematics", "#c68ad6"), ("Strategy · PYQs · Mocks", "#e8c98a")))
    feats = "".join(f'<div class="cv-feat"><b>{html.escape(n)}</b><span>{html.escape(t)}</span></div>' for n, t in FEATURES)
    return (f'<section class="fullpage cover" id="cover"><a class="probe" href="https://probe.local/full-cover"></a>{_pattern_cover()}'
            f'<div class="cv-inner"><div class="cv-edition">{EDITION} · Session 1: 22–30 Jan 2027 (tentative)</div>'
            f'<div class="cv-title">JEE MAIN <span class="plus">99+</span></div>'
            f'<div class="cv-sys">{html.escape(SYSTEM)}</div><div class="cv-rule"></div>'
            f'<div class="cv-sub">{html.escape(SUBTITLE)}</div><div class="cv-chips">{chips}</div>'
            f'<div class="cv-feats">{feats}</div>'
            f'<div class="cv-bottom"><div class="cv-for"><div class="k">By</div><div class="v">{html.escape(AUTHOR.upper())}</div>'
            f'<div class="cv-book"><b>{html.escape(book_label)}</b> · {html.escape(book_desc)}</div></div>'
            f'<div class="cv-price"><div class="k">M.R.P.</div><div class="v">{PRICE}</div><div class="s">inclusive of all taxes</div></div>'
            f'</div></div></section>')


def front_matter_html(book_label: str) -> str:
    """Title page and copyright/disclaimer page (unnumbered, no running heads)."""
    title = (f'<section class="fullpage titlepage"><a class="probe" href="https://probe.local/full-titlepage"></a>'
             f'<div class="tp-inner"><div class="tp-edition">{EDITION}</div>'
             f'<div class="tp-title">JEE MAIN <span>99+</span></div><div class="tp-sys">{html.escape(SYSTEM)}</div>'
             f'<div class="tp-rule"></div><div class="tp-sub">{html.escape(SUBTITLE)}</div>'
             f'<div class="tp-author"><div class="k">Author</div><div class="v">{html.escape(AUTHOR.upper())}</div></div>'
             f'<div class="tp-label">{html.escape(book_label)}</div></div></section>')
    rights = (f'<section class="fullpage copyright"><a class="probe" href="https://probe.local/full-copyright"></a><div class="cp-inner">'
              f'<p class="cp-title">JEE MAIN 99+ · {html.escape(SYSTEM)}</p>'
              f'<p>{html.escape(SUBTITLE)}</p>'
              f'<p><b>Author:</b> {html.escape(AUTHOR)}<br><b>Edition:</b> {EDITION}, first edition, September {YEAR}<br>'
              f'<b>M.R.P.:</b> {PRICE} (inclusive of all taxes)</p>'
              f'<p>© {YEAR} {html.escape(AUTHOR)}. All rights reserved. No part of this publication may be reproduced, stored in a retrieval '
              f'system, shared, resold or transmitted in any form or by any means (electronic, photocopying, recording or otherwise) '
              f'without the prior written permission of the author. A purchased copy is licensed for the personal use of one student; '
              f'printing pages for that student\'s own study is permitted.</p>'
              f'<p class="cp-h">Independent publication</p>'
              f'<p>This book is an independent study guide. It is <b>not</b> published, endorsed or approved by the National Testing '
              f'Agency (NTA), the Ministry of Education, JoSAA, NCERT, any IIT/NIT or any coaching institute. "JEE (Main)" and other '
              f'names are used only to identify the examination and the sources cited.</p>'
              f'<p class="cp-h">Accuracy and currency</p>'
              f'<p>Exam rules are taken from official documents available in September {YEAR} (the JEE (Main) 2026 Information Bulletin '
              f'and NTA notices) and are labelled <i>Verified</i>. The JEE (Main) 2027 Information Bulletin had not been released when this '
              f'edition went to press. Always check the current bulletin and your admit card, which override anything in this book. '
              f'Chapter weights and marks-vs-percentile figures come from third-party analyses, are approximate, and are labelled as such.</p>'
              f'<p class="cp-h">No guarantee of results</p>'
              f'<p>Percentile and rank depend on each candidate\'s performance and on every other candidate in the same shift. '
              f'No book can guarantee a score, percentile, rank or admission, and this one does not.</p>'
              f'<p class="cp-h">Original content</p>'
              f'<p>All practice questions, mock tests, solutions, plans and tables were written for this book. Previous-year questions are '
              f'referenced and classified, not reproduced. Sources are listed at the end of the book.</p>'
              f'<p class="cp-small">Typeset with Inter, Fraunces and JetBrains Mono (SIL Open Font License) and KaTeX (MIT License).</p>'
              f'</div></section>')
    return title + rights


def back_cover_html() -> str:
    points = ["All 54 units of the official syllabus: concepts, formulas, graphs, traps and shortcuts",
              "1,000+ original questions with full solutions, shortcuts and common traps",
              "Two full-length original mock tests (+4/−1 pattern, Sections A and B)",
              "Master Formula Handbook and a one-page Last-Minute Revision Book",
              "PYQ trend analysis 2024–2026 and a topic-level Priority Matrix",
              "30- to 180-day plans at 6, 8 and 10 hours a day, with final 30/14/7/3-day plans",
              "The Mistake Book, spaced revision calendar, mock analysis sheets and fillable trackers",
              "Exam-hall protocol and a one-page Exam Day Command Sheet"]
    lis = "".join(f"<li>{html.escape(p)}</li>" for p in points)
    return (f'<section class="fullpage cover backcover"><a class="probe" href="https://probe.local/full-backcover"></a>{_pattern_cover()}'
            f'<div class="bc-inner"><div class="bc-kicker">{EDITION}</div>'
            f'<div class="bc-head">Everything you need to turn preparation into a 99+ percentile score, in one book.</div>'
            f'<ul class="bc-list">{lis}</ul>'
            f'<div class="bc-note">Every rule is labelled Verified, Third-party analysis or Recommendation, and every source is listed. '
            f'Built on retrieval practice, spaced revision and mistake analysis, not on slogans.</div>'
            f'<div class="bc-bottom"><div class="bc-author"><div class="k">By</div><div class="v">{html.escape(AUTHOR.upper())}</div></div>'
            f'<div class="cv-price"><div class="k">M.R.P.</div><div class="v">{PRICE}</div><div class="s">inclusive of all taxes</div></div></div>'
            f'</div></section>')


def divider_html(roman, title, subject, lead, chapters):
    colour = SUBJECT_COLOURS.get(subject, "#3b2e7e")
    rows = "".join(f'<a href="#{c.cid}"><span class="n">{html.escape(c.number or "•")}</span><span class="t">{title_html(c.title)}</span>'
                   f'<span class="p"><span class="pnum" data-ref="{c.cid}">000</span></span></a>' for c in chapters)
    pid = f"part-{roman}"
    return (f'<section class="fullpage divider" id="{pid}" style="--pc:{colour}"><a class="probe" href="https://probe.local/full-{pid}"></a>'
            f'<a class="probe" href="https://probe.local/{pid}"></a>{_pattern_divider(subject)}'
            f'<div class="dv-inner"><div class="dv-num">{roman}</div><div class="dv-part">Part {roman}</div>'
            f'<div class="dv-title">{html.escape(title)}</div><div class="dv-lead">{html.escape(lead)}</div>'
            f'<div class="dv-list">{rows}</div></div></section>')


def chapter_html(ch: Chapter, kicker: str) -> str:
    num = f'<div class="ch-num">{html.escape(ch.number)}</div>' if ch.number else ""
    return (f'<section class="chapter ch-{ch.cid}" data-subject="{ch.subject}"><header class="ch-open">'
            f'<div class="ch-kicker">{html.escape(kicker)}</div>{num}'
            f'<h1 class="ch-title" id="{ch.cid}"><a class="probe" href="https://probe.local/{ch.cid}">{title_html(ch.title)}</a></h1></header>'
            f'{ch.body_html}</section>')


def toc_html(parts_with_chapters, title="Contents", intro="") -> str:
    blocks = []
    for roman, ptitle, subject, _lead, chapters in parts_with_chapters:
        colour = SUBJECT_COLOURS.get(subject, "#3b2e7e")
        target = f"part-{roman}" if roman else (chapters[0].cid if chapters else "")
        rows = "".join(f'<a class="toc-row" href="#{c.cid}"><span class="tr-n">{html.escape(c.number)}</span>'
                       f'<span class="tr-t">{title_html(c.title)}</span><span class="tr-d"></span>'
                       f'<span class="tr-p pnum" data-ref="{c.cid}">000</span></a>' for c in chapters)
        label = f"Part {roman}" if roman else ""
        blocks.append(f'<div class="toc-block" style="--pc:{colour}"><a class="toc-part" href="#{target}"><span class="tp-n">{roman}</span>'
                      f'<span class="tp-t">{html.escape(ptitle)}</span><span class="tp-p pnum" data-ref="{target}">000</span></a>{rows}</div>')
    intro_html = f'<p class="toc-intro">{intro}</p>' if intro else ""
    return (f'<section class="chapter ch-contents" data-subject="general"><header class="ch-open"><div class="ch-kicker">{html.escape(TITLE)} · Navigation</div>'
            f'<h1 class="ch-title" id="contents"><a class="probe" href="https://probe.local/contents">{html.escape(title)}</a></h1></header>'
            f'{intro_html}<div class="toc-cols">{"".join(blocks)}</div></section>')
