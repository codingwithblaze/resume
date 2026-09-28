# JEE MAIN 99+ | The Complete Personalized Preparation System

A Personalized Strategy, Formula, PYQ, Practice, Revision & Mock-Test Handbook.
Prepared for: Gayathri Devu.

## Deliverables (in `output/`)

| File | What it is |
|---|---|
| `A_JEE_Main_99_Master_Book.pdf` | The complete book in 13 parts plus sources: exam facts, 99+ roadmap and percentile strategy, diagnostic test, 54 subject modules (20 Physics, 20 Chemistry, 14 Maths), Master Formula Handbook, Speed & Shortcut Manual, PYQ Intelligence, a 60-question bank and a full-length original mock with solutions, Mistake Book, revision system, psychology, 30–180-day plans, exam-day protocol, last-minute sheets and trackers |
| `B_Quick_Revision_Book.pdf` | Formula Handbook, Speed & Shortcut Manual and the Last-Minute Revision Book |
| `C_Study_Planner.pdf` | Profile, plan selector, revision system, all plans and timetables, weekly scorecard and trackers |
| `D_Mock_Analysis_Template.pdf` | Mock-test system, the two-page Mock Analysis Sheet, the mock log and Mistake Book pages |
| `E_Exam_Day_Command_Sheet.pdf` | One-page exam-day checklist and strategy |

The companion PDFs (B–E) refer to chapters that live only in the Master Book as **MB** plus the page number.

## Source layout

- `content/` holds the book text: Markdown with custom blocks (`:::formula`, `:::shortcut`, `:::trap`, …) and a small question syntax (`@@Q … @@END`). See `content/SYNTAX.md`.
- `build/` holds the pipeline: Markdown → HTML (KaTeX + mhchem) → Chromium PDF → PyMuPDF post-processing. Post-processing adds page numbers, running headers, bookmarks, the clickable contents, quick-jump tabs, fillable checkboxes and text fields.
- MCQ answer keys are balanced across A–D at build time. The build swaps options deterministically and remaps letter references in the solutions.

## Rebuild

```bash
cd jee-main-99
python3 build/build.py          # all five PDFs (the Master Book is built first)
python3 build/build.py A B      # selected PDFs
```
