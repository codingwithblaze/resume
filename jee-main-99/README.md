# JEE MAIN 99+ | The Complete Personalized Preparation System

A Personalized Strategy, Formula, PYQ, Practice, Revision & Mock-Test Handbook.
Prepared for: Gayathri Devu.

## Deliverables (in `output/`)

| File | What it is |
|---|---|
| `A_JEE_Main_99_Master_Book.pdf` | The complete book: strategy, all Physics/Chemistry/Maths modules, formula handbook, shortcut manual, PYQ analysis, question bank, mock system, plans, trackers, sources |
| `B_Quick_Revision_Book.pdf` | Compact formula + shortcut + last-minute revision book |
| `C_Study_Planner.pdf` | Daily / weekly / monthly planner and printable trackers |
| `D_Mock_Analysis_Template.pdf` | Printable mock score sheets, analysis sheets and Mistake Book pages |
| `E_Exam_Day_Command_Sheet.pdf` | One-page exam-day checklist and strategy |

## Source layout

- `content/` — book content written in Markdown with custom blocks (`:::formula`, `:::shortcut`, `:::trap`, …) and a small question syntax (`@@Q … @@END`).
- `build/` — the build pipeline (Markdown → HTML → Chromium PDF → PyMuPDF post-processing for page numbers, running headers, bookmarks, clickable TOC and fillable checkboxes).

## Rebuild

```bash
cd jee-main-99
python3 build/build.py          # builds all five PDFs into output/
```
