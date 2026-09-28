# JEE MAIN 99+ | The Complete Personalized Preparation System

A Personalized Strategy, Formula, PYQ, Practice, Revision & Mock-Test Handbook.
Author: BM Excel Blaze · JEE Main 2027 Edition · M.R.P. ₹1,499.

## Output

`output/JEE_Main_99_Complete_Edition.pdf` is the all-in-one book. It includes the cover, title and copyright pages, 13 parts plus Sources, and a back cover:

- exam facts, the 99+ roadmap and percentile strategy, and a diagnostic test
- 54 subject modules (20 Physics, 20 Chemistry, 14 Maths)
- the Master Formula Handbook and the Speed & Shortcut Manual
- PYQ Intelligence
- a 60-question bank and two full-length original mock tests with solutions
- the Mistake Book, revision system and psychology chapters
- 30–180-day plans, the exam-day protocol, last-minute sheets and trackers

## Source layout

- `content/` holds the book text: Markdown with custom blocks (`:::formula`, `:::shortcut`, `:::trap`, …) and a small question syntax (`@@Q … @@END`). See `content/SYNTAX.md`.
- `build/` holds the pipeline: Markdown → HTML (KaTeX + mhchem) → Chromium PDF → PyMuPDF post-processing. Post-processing adds page numbers, running headers, bookmarks, the clickable contents, quick-jump tabs, fillable checkboxes and text fields.
- `build/book.py` holds the title, author, edition and price (`AUTHOR`, `EDITION`, `PRICE`).
- MCQ answer keys are balanced across A–D at build time. The build swaps options deterministically and remaps letter references in the solutions.

## Rebuild

```bash
cd jee-main-99
python3 build/build.py          # the complete edition
python3 build/build.py B C D E  # optional extracts (quick revision, planner, mock kit, command sheet)
```
