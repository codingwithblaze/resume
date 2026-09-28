"""Build all five PDFs.

    python3 build/build.py            # all deliverables
    python3 build/build.py A C        # selected deliverables
"""
from __future__ import annotations

import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import book  # noqa: E402
import render  # noqa: E402

OUT = os.path.join(book.ROOT, "output")
PAGEMAP = os.path.join(book.ROOT, "work", "pagemap_A.json")  # Master Book pages, for "MB" refs in B–E


def part_by_roman(roman):
    for p in book.MASTER_PARTS:
        if p[0] == roman:
            return p
    raise KeyError(roman)


def make_parts(spec):
    """spec: list of (roman, title, subject, lead, files) -> list with Chapter objects."""
    out = []
    for roman, title, subject, lead, files in spec:
        chapters = book.build_chapters(files, subject, roman, title)
        out.append((roman, title, subject, lead, chapters))
    return out


def assemble(parts, cover_label, cover_desc, with_cover=True, with_toc=True, with_dividers=True, toc_title="Contents",
             toc_intro=""):
    parts = [p for p in parts if p[4]]
    body, chapters, marks = [], [], []
    if with_cover:
        body.append(book.cover_html(cover_label, cover_desc))
        marks.append((1, "Cover", "full-cover"))
    all_ch = [c for p in parts for c in p[4]]
    if with_toc:
        toc_ch = book.Chapter("contents", toc_title, "general", "", "", "", "", [], [])
        chapters.append(toc_ch)
        body.append(book.toc_html(parts, toc_title, toc_intro))
        marks.append((1, "Contents", "contents"))
    for roman, title, subject, lead, chs in parts:
        if with_dividers and roman:
            body.append(book.divider_html(roman, title, subject, lead, chs))
            marks.append((1, f"Part {roman} · {title}", f"part-{roman}"))
        elif not roman and chs:
            marks.append((1, title, chs[0].cid))
        for c in chs:
            kicker = f"Part {roman} · {title}" if roman else title
            if c.number:
                kicker += f" · Unit {c.number}"
            body.append(book.chapter_html(c, kicker))
            chapters.append(c)
            level = 2 if (with_dividers and roman) or (not roman and c is not chs[0]) else 1
            label = f"{c.number} · {book.plain_title(c.title)}" if c.number else book.plain_title(c.title)
            if not (not roman and c is chs[0]):
                marks.append((level, label, c.cid))
            for hl, hid, htitle in c.headings:
                if hl == 2:
                    marks.append((level + 1, htitle, hid))
    return "".join(body), chapters, marks


DELIVERABLES = {
    "A": dict(file="A_JEE_Main_99_Master_Book.pdf", label="Master Book",
              desc="Strategy · Physics · Chemistry · Maths · Formulas · PYQs · Mocks · Plans · Trackers",
              parts=lambda: book.MASTER_PARTS, doc_label="MASTER BOOK", tabs=None),
    "B": dict(file="B_Quick_Revision_Book.pdf", label="Quick Revision Book",
              desc="Formula handbook · Speed & shortcut manual · Last-minute sheets",
              parts=lambda: [part_by_roman("V"), part_by_roman("VI"), part_by_roman("XII")], doc_label="QUICK REVISION",
              tabs=[("CONTENTS", "contents"), ("FORMULAS", "part-V"), ("SPEED MANUAL", "part-VI"), ("LAST-MINUTE", "part-XII")]),
    "C": dict(file="C_Study_Planner.pdf", label="Study Planner",
              desc="Plan selector · 30–180-day plans · Final plans · Timetables · Weekly system · Trackers",
              parts=lambda: [("I", "Choose Your Plan", "general", "Profile, plan selector and the revision system that every plan uses.",
                              ["A_start/05_profile.md", "A_start/07_plan_selector.md"] + [f for f in book.files("I_systems") if "revision" in f]),
                             part_by_roman("X"), part_by_roman("XIII")], doc_label="STUDY PLANNER",
              tabs=[("CONTENTS", "contents"), ("CHOOSE", "part-I"), ("PLANS", "part-X"), ("TRACKERS", "part-XIII")]),
    "D": dict(file="D_Mock_Analysis_Template.pdf", label="Mock Analysis Template",
              desc="Mock-test system · Analysis sheet · Mock log · Mistake Book pages",
              parts=lambda: [("I", "Mock Analysis Kit", "systems", "Printable mock-score, analysis and error-log sheets. Print one set per mock.",
                              [f for f in book.files("H_practice") if "mock_system" in f] + [f for f in book.files("M_trackers") if "mock" in f] +
                              [f for f in book.files("I_systems") if "mistake" in f])], doc_label="MOCK ANALYSIS",
              tabs=[("CONTENTS", "contents"), ("MOCK SYSTEM", "mock-system"), ("ANALYSIS SHEET", "mock-analysis-sheet"),
                    ("MOCK LOG", "mock-log"), ("MISTAKE BOOK", "mistake-book")]),
    "E": dict(file="E_Exam_Day_Command_Sheet.pdf", label="Exam Day Command Sheet", desc="",
              parts=lambda: [("", "Exam Day Command Sheet", "systems", "", [f for f in book.files("K_examday") if "command" in f])],
              doc_label="EXAM DAY", cover=False, toc=False, dividers=False, tabs=[]),
}


def build(key):
    d = DELIVERABLES[key]
    t0 = time.time()
    print(f"[{key}] {d['file']}")
    parts = make_parts(d["parts"]())
    intro = "" if key == "A" else "Page numbers marked <b>MB</b> refer to the Master Book, where the full chapter is."
    body, chapters, marks = assemble(parts, d["label"], d["desc"], with_cover=d.get("cover", True),
                                     with_toc=d.get("toc", True), with_dividers=d.get("dividers", True), toc_intro=intro)
    os.makedirs(OUT, exist_ok=True)
    title = f"{book.TITLE} | {d['label']}"
    fallback = None
    if key != "A" and os.path.exists(PAGEMAP):
        with open(PAGEMAP, encoding="utf-8") as f:
            fallback = json.load(f)
    pages = render.render_doc(body, chapters, d["doc_label"], title, os.path.join(OUT, d["file"]), marks,
                              tabs_list=d["tabs"], fallback=fallback)
    if key == "A":
        os.makedirs(os.path.dirname(PAGEMAP), exist_ok=True)
        with open(PAGEMAP, "w", encoding="utf-8") as f:
            json.dump({k: v[0] + 1 for k, v in pages.items()}, f)
    print(f"[{key}] done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    keys = [a for a in sys.argv[1:] if a in DELIVERABLES] or list(DELIVERABLES)
    keys.sort(key=lambda k: k != "A")  # the Master Book first, so "MB" page refs are current
    for k in keys:
        build(k)
