# Content syntax used in this book (for maintainers)

Standard Markdown (CommonMark + GFM tables) plus:

| Syntax | Renders as |
|---|---|
| `# Title {#id}` | Chapter / section title with explicit anchor id |
| `:::formula Title` … `:::` | Formula callout (also: shortcut, trap, important, warning, pyq, revision, practice, mock, fact, strategy, note, def, graph, example, tip) |
| `:::cols2` … `:::` | Two-column flow |
| `:::grid2` / `:::grid3` … `+++` … `:::` | Card grid; `+++` separates cards |
| `:::flow` lines `Title | text` | Step flowchart |
| `:::mindmap Centre` lines `Branch: a; b; c` | Mind map |
| `:::stats` lines `Label | Value` | Stat tiles |
| `$…$`, `$$…$$` | KaTeX math (`\ce{}` for chemistry) |
| `[ ]` | Fillable checkbox |
| `{{field:key:40}}` | Fillable text field, 40 mm wide |
| `{{blank:30}}` | Printed blank line |
| `@@PAGEBREAK` | Page break |
| `@@CHART id` | Generated SVG chart |
| `@@QR url | label` | QR code |
| `@@SET Name` | Starts a question set (numbering restarts) |
| `@@Q id | E/M/H | minutes | concept | tags` … `@@END` | Question (options `(A)`…, `@ans`, `@sol`, `@short`, `@trap`) |
| `@@SOLUTIONS` | Prints solutions of all sets since the previous `@@SOLUTIONS` |
| `@@ANSWERKEY` | Compact answer grid for the same sets |
