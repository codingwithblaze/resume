"""HTML assembly, Chromium PDF rendering (two passes) and PyMuPDF post-processing."""
from __future__ import annotations

import html
import os
import re
import time

import pymupdf
from playwright.sync_api import sync_playwright

import book

BUILD = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BUILD)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
MM = 72 / 25.4

SUBJECT_LABEL = {"physics": "PHYSICS", "chemistry": "CHEMISTRY", "maths": "MATHEMATICS"}


def _css_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def page_rules(chapters, doc_label, tabs_list=None) -> str:
    rules = []
    base = (
        "@top-left { content: %s; font-family: Inter, sans-serif; font-size: 6.4pt; font-weight: 800; letter-spacing: 0.16em; color: #767b93; vertical-align: bottom; padding-bottom: 6.8mm; }"
        "@top-right { content: %s; font-family: Inter, sans-serif; font-size: 6.4pt; font-weight: 800; letter-spacing: 0.1em; color: %s; vertical-align: bottom; padding-bottom: 6.8mm; text-transform: uppercase; }"
        "@bottom-left { content: %s; font-family: Inter, sans-serif; font-size: 6.2pt; color: #9aa0b6; vertical-align: top; padding-top: 5.2mm; }"
        "@bottom-center { content: %s; font-family: Inter, sans-serif; font-size: 5.9pt; font-weight: 800; letter-spacing: 0.12em; color: #8a8fa6; vertical-align: top; padding-top: 5.2mm; white-space: pre; }"
        "@bottom-right { content: counter(page); font-family: Inter, sans-serif; font-size: 8.5pt; font-weight: 800; color: %s; vertical-align: top; padding-top: 4.6mm; }"
    )
    tabs = "   ".join(t for t, _ in (book.TABS if tabs_list is None else tabs_list))
    for ch in chapters:
        colour = book.SUBJECT_COLOURS.get(ch.subject, "#3b2e7e")
        left = f"{book.TITLE}   ·   {doc_label}"
        subj = SUBJECT_LABEL.get(ch.subject)
        num = f"{ch.number} · " if ch.number else ""
        right = f"{subj + ' · ' if subj else ''}{num}{book.plain_title(ch.title)}"
        if len(right) > 70:
            right = right[:68] + "…"
        rules.append(f"section.ch-{ch.cid} {{ page: pg-{ch.cid}; }}")
        rules.append(f"@page pg-{ch.cid} {{ " + base % (_css_str(left), _css_str(right), colour,
                                                       _css_str("Prepared for " + book.PREPARED_FOR),
                                                       _css_str(tabs), colour) + " }")
    return "\n".join(rules)


KATEX_JS = r"""
<script>
window.__katexErrors = [];
function renderAllMath() {
  document.querySelectorAll('.math').forEach(function (el) {
    var tex = el.textContent; var disp = el.classList.contains('math-display');
    try { katex.render(tex, el, {displayMode: disp, throwOnError: true, strict: 'ignore', trust: false, output: 'html'}); }
    catch (e) { window.__katexErrors.push(tex + '  ::  ' + e.message);
      try { katex.render(tex, el, {displayMode: disp, throwOnError: false, strict: 'ignore', output: 'html'}); } catch (e2) {} }
  });
}
function fitAll() {
  window.__overflow = [];
  document.querySelectorAll('.opts').forEach(function (o) {
    var order = ['opts4', 'opts2', 'opts1'];
    for (var k = 0; k < 3; k++) {
      var bad = false;
      o.querySelectorAll('.opt').forEach(function (x) { if (x.scrollWidth > x.clientWidth + 1) bad = true; });
      if (!bad) break;
      var cur = order.find(function (c) { return o.classList.contains(c); });
      var idx = order.indexOf(cur);
      if (idx >= 2) break;
      o.classList.remove(cur); o.classList.add(order[idx + 1]);
    }
  });
  document.querySelectorAll('.math-display').forEach(function (el) {
    if (el.scrollWidth > el.clientWidth + 1) {
      var f = Math.max(0.55, el.clientWidth / el.scrollWidth);
      el.style.fontSize = (f * 100).toFixed(1) + '%';
    }
  });
  document.querySelectorAll('.katex').forEach(function (el) {
    if (el.closest('.math-display')) return;
    var box = el.parentElement.closest('td, th, .cell, .opt-t, li, p, .box-body, .rm-arrow, .rm-prod, .stat-v, .step-t, .sol-line, div');
    if (!box) return;
    var br = box.getBoundingClientRect(), r = el.getBoundingClientRect();
    if (r.right > br.right + 1 && r.width > 0) {
      var avail = br.right - r.left;
      var f = Math.max(0.6, avail / r.width);
      el.style.fontSize = (f * 1.03 * 100).toFixed(1) + '%';
    }
  });
  var W = document.documentElement.clientWidth;
  document.querySelectorAll('body *').forEach(function (el) {
    if (el.closest('.fullpage') || el.closest('svg')) return;
    var r = el.getBoundingClientRect();
    if (r.right > W + 1 && r.width > 0 && window.__overflow.length < 60) {
      var sec = el.closest('section');
      window.__overflow.push((sec ? sec.className : '') + ' | ' + el.tagName + '.' + (typeof el.className === 'string' ? el.className : '') + ' | ' + Math.round(r.right) + ' | ' + (el.textContent || '').slice(0, 80));
    }
  });
}
window.addEventListener('load', function () {
  renderAllMath();
  document.fonts.ready.then(function () { fitAll(); setTimeout(function () { fitAll(); window.__done = true; }, 300); });
});
</script>
"""


def assemble_html(body: str, chapters, doc_label: str, title: str, tabs_list=None) -> str:
    a = f"file://{BUILD}/assets"
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<base href="file://{BUILD}/">'
            f'<link rel="stylesheet" href="{a}/katex/katex.min.css"><link rel="stylesheet" href="file://{BUILD}/style.css">'
            f'<style>{page_rules(chapters, doc_label, tabs_list)}</style>'
            f'<script src="{a}/katex/katex.min.js"></script><script src="{a}/katex/mhchem.min.js"></script>{KATEX_JS}'
            f'</head><body>{body}</body></html>')


def fill_page_numbers(html_str: str, pages: dict, fallback: dict | None = None) -> tuple[str, list]:
    """Fill page refs; refs to chapters outside this document point to the Master Book ("MB 123")."""
    missing = []

    def rep(m):
        rid = m.group(1)
        if rid in pages:
            return f'data-ref="{rid}">{pages[rid]}<'
        if fallback and rid in fallback:
            return f'data-ref="{rid}">MB {fallback[rid]}<'
        missing.append(rid)
        return f'data-ref="{rid}">?<'

    return re.sub(r'data-ref="([\w-]+)">[^<]*<', rep, html_str), missing


def chrome_pdf(html_path: str, pdf_path: str, log=print):
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=CHROME, args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": 680, "height": 1100})
        pg.goto(f"file://{html_path}", wait_until="load", timeout=600_000)
        pg.wait_for_function("window.__done === true", timeout=600_000)
        errs = pg.evaluate("window.__katexErrors")
        ov = pg.evaluate("window.__overflow")
        if ov:
            log(f"  overflow warnings: {len(ov)}")
            seen = set()
            for o in ov:
                k = o.split(' | ')[0] + o.split(' | ')[1]
                if k in seen:
                    continue
                seen.add(k)
                log("    " + o[:200])
        pg.pdf(path=pdf_path, prefer_css_page_size=True, print_background=True)
        b.close()
    if errs:
        log(f"  KaTeX errors: {len(errs)}")
        for e in errs[:40]:
            log("    " + e[:220])
    return errs


def probe_map(pdf_path: str) -> dict:
    doc = pymupdf.open(pdf_path)
    pages = {}
    for i, page in enumerate(doc):
        for l in page.get_links():
            uri = l.get("uri") or ""
            if uri.startswith("https://probe.local/"):
                pid = uri.rsplit("/", 1)[1]
                if pid not in pages:
                    pages[pid] = (i, l["from"].y0)
    doc.close()
    return pages


def render_doc(body: str, chapters, doc_label: str, title: str, out_pdf: str, bookmarks, log=print, meta_subject="",
               tabs_list=None, fallback=None):
    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    stem = os.path.splitext(os.path.basename(out_pdf))[0]
    html_path = os.path.join(ROOT, "work", stem + ".html")
    tmp_pdf = os.path.join(ROOT, "work", stem + ".raw.pdf")
    doc_html = assemble_html(body, chapters, doc_label, title, tabs_list)
    pages = {}
    for it in range(4):
        filled, missing = fill_page_numbers(doc_html, {k: v[0] + 1 for k, v in pages.items()}, fallback)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(filled)
        t0 = time.time()
        chrome_pdf(html_path, tmp_pdf, log)
        new_pages = probe_map(tmp_pdf)
        n = len(pymupdf.open(tmp_pdf))
        log(f"  pass {it + 1}: {n} pages, {len(new_pages)} anchors, {time.time() - t0:.1f}s")
        stable = {k: v[0] for k, v in new_pages.items()} == {k: v[0] for k, v in pages.items()}
        pages = new_pages
        if stable and it > 0:
            break
    if missing:
        log(f"  unresolved page refs: {sorted(set(missing))[:30]}")
    postprocess(tmp_pdf, out_pdf, chapters, pages, bookmarks, title, meta_subject, log, tabs_list)
    return pages


# ---------------------------------------------------------------- post-processing
def postprocess(src, dst, chapters, pages, bookmarks, title, meta_subject, log=print, tabs_list=None):
    doc = pymupdf.open(src)
    n = len(doc)
    full_pages = {v[0] for k, v in pages.items() if k.startswith("full-")}
    # chapter start pages -> subject colour for the progress bar
    starts = sorted((pages[c.cid][0], c) for c in chapters if c.cid in pages)
    colour_of = {}
    cur = None
    si = 0
    for i in range(n):
        while si < len(starts) and starts[si][0] <= i:
            cur = starts[si][1]
            si += 1
        colour_of[i] = book.SUBJECT_COLOURS.get(cur.subject, "#3b2e7e") if cur else "#3b2e7e"
    tab_targets = {label: pages[t][0] for label, t in (book.TABS if tabs_list is None else tabs_list) if t in pages}
    n_cb = n_fld = 0
    for i, page in enumerate(doc):
        W, H = page.rect.width, page.rect.height
        links = page.get_links()
        for l in links:
            uri = l.get("uri") or ""
            if uri.startswith("https://probe.local/"):
                page.delete_link(l)
            elif uri.startswith("https://cb.local/"):
                r = l["from"]
                page.delete_link(l)
                w = pymupdf.Widget()
                w.field_type = pymupdf.PDF_WIDGET_TYPE_CHECKBOX
                w.field_name = "cb_" + uri.rsplit("/", 1)[1] + f"_{i}_{n_cb}"
                w.rect = pymupdf.Rect(r.x0 + 0.6, r.y0 + 0.6, r.x1 - 0.6, r.y1 - 0.6)
                w.field_value = False
                w.border_width = 0
                w.text_color = (0.2, 0.18, 0.49)
                page.add_widget(w)
                n_cb += 1
            elif uri.startswith("https://fld.local/"):
                r = l["from"]
                page.delete_link(l)
                w = pymupdf.Widget()
                w.field_type = pymupdf.PDF_WIDGET_TYPE_TEXT
                w.field_name = "f_" + uri.rsplit("/", 1)[1] + f"_{i}_{n_fld}"
                w.rect = pymupdf.Rect(r.x0 + 1, r.y0, r.x1 - 1, r.y1)
                w.text_fontsize = 0
                w.text_color = (0.1, 0.12, 0.23)
                w.border_width = 0
                page.add_widget(w)
                n_fld += 1
        if i in full_pages:
            continue
        # progress bar
        y = 13.2 * MM
        x0, x1 = 15 * MM, W - 15 * MM
        frac = (i + 1) / n
        page.draw_line((x0, y), (x1, y), color=(0.9, 0.91, 0.94), width=1.1)
        hexc = colour_of[i].lstrip("#")
        rgb = tuple(int(hexc[k:k + 2], 16) / 255 for k in (0, 2, 4))
        page.draw_line((x0, y), (x0 + (x1 - x0) * frac, y), color=rgb, width=1.6)
        # footer tabs -> links
        band = pymupdf.Rect(0, H - 16 * MM, W, H)
        for label, target in tab_targets.items():
            for r in page.search_for(label, clip=band):
                page.insert_link({"kind": pymupdf.LINK_GOTO, "from": r + (-1, -2, 1, 2), "page": target, "to": pymupdf.Point(0, 0)})
                break
    # bookmarks
    toc = []
    for level, label, pid in bookmarks:
        if pid in pages:
            toc.append([level, label, pages[pid][0] + 1])
    # enforce valid hierarchy
    fixed, prev = [], 0
    for lvl, lab, p in toc:
        lvl = min(lvl, prev + 1) if prev else 1
        fixed.append([lvl, lab, p])
        prev = lvl
    if fixed:
        doc.set_toc(fixed)
    doc.set_metadata({"title": title, "author": "Prepared for " + book.PREPARED_FOR,
                      "subject": meta_subject or book.SUBTITLE, "keywords": "JEE Main 2027, 99 percentile, Physics, Chemistry, Mathematics, PYQ, mock tests, study planner",
                      "creator": "JEE Main 99+ build system", "producer": "Chromium + PyMuPDF"})
    doc.set_page_labels([{"startpage": 0, "prefix": "", "style": "D", "firstpagenum": 1}])
    doc.save(dst, garbage=3, deflate=True)
    doc.close()
    log(f"  saved {os.path.basename(dst)}: {n} pages, {n_cb} checkboxes, {n_fld} text fields, {len(fixed)} bookmarks")
