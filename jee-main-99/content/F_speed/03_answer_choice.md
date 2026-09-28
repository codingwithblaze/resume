# Answer-Choice Strategy {#answer-choice}

The options in an MCQ are information. Using them well is a legitimate exam skill. Guessing blindly is not: with $-1$ for a wrong answer, it adds risk for almost no expected gain.

## The mathematics of attempting

Under the verified +4 / −1 scheme (page [[exam-facts]]), suppose $k$ options remain and you have no further information, so each is equally likely. The expected marks from attempting are:

$$E = \frac{4}{k} - \frac{k - 1}{k} = \frac{5 - k}{k}$$

| Options remaining | Expected marks if you attempt | Probability of −1 | Book rule {{tag:rec}} |
|---|---|---|---|
| 4 (pure guess) | +0.25 | 75% | **Never.** |
| 3 (one eliminated) | +0.67 | 67% | Skip, unless the remaining three are not equally likely and your reasoning favours one |
| 2 (two eliminated with certainty) | +1.50 | 50% | **Attempt.** |
| 1 (solved) | +4.00 | only if you erred | Attempt, then verify quickly |

:::warning Why the book is stricter than the arithmetic
The table assumes your eliminations are **certainly right**. Under time pressure they often aren't, and every wrong answer also worsens your incorrect-to-correct ratio, which is a tie-breaker (page [[exam-facts]]). Hence the rule used throughout this book: **attempt only after eliminating at least two options through real reasoning.**
:::

:::important Numerical-value questions: never guess
Section B answers are typed in, so there is nothing to eliminate and a guess is almost never right. Enter an NV answer only after solving it. A blank costs 0; a wrong answer costs 1.
:::

## Seven legitimate ways to use the options

:::flow
1 · Impossibility filter | Remove options that are physically or mathematically impossible: probability > 1, efficiency ≥ 1, negative counts, wrong sign of $\Delta G$ for a spontaneous process (Technique 14).
2 · Dimensions & units | In Physics, remove every option with the wrong dimensions (Technique 1).
3 · Limiting / special cases | Test each surviving option at a special value or limit (Techniques 2 and 3).
4 · Back-substitution | If the options are numbers, substitute them into the condition (Technique 4).
5 · Estimation | If the options are far apart, compute to one significant figure (Technique 6).
6 · Structure of the options | If two options differ only in sign or by a factor of 2, the question is testing that detail. Solve for that detail specifically.
7 · Consistency across parts | In "Statement I / Statement II" and "match the columns" questions, decide the item you are surest of first. It often removes two or three options at once.
:::

## Match-the-column and statement questions

These are common in Chemistry and Physics. Don't evaluate every pair in order.

:::strategy Method
1. Find the **one pairing you are most certain of** and eliminate every option that contradicts it.
2. Repeat with the next most certain pairing. Usually two pairings leave one option.
3. For "Statement I and II" questions, decide each statement separately (true/false) before reading the options. Only then check whether II explains I, if the options ask for it.
:::

## What *not* to do

:::trap Myths that cost marks
- **"Option C is correct most often."** There is no reliable answer-position pattern to exploit in NTA papers, and this book's own question bank deliberately has balanced keys.
- **"The longest option is usually right."** No evidence. It is a habit from poorly written tests.
- **"If I've left many questions, I should guess a few."** No. Skipped questions cost 0. The only way to raise your score is to solve more, or to eliminate with certainty.
- **Changing an answer on a "feeling"** during the final minutes. Change an answer only if you find a specific error in your working.
:::

## Mark-for-review discipline

:::shortcut Use the review status as a queue, not a verdict
Use **Marked for Review** only for questions you intend to return to, with a note on your rough sheet of how far you got ("Q14: $\lambda = 2$ found, need $d$"). In the last 10 minutes, review only questions where you already know the next step (Exam-Hall Protocol, page [[hall-protocol]]).
:::

:::note How marked answers are evaluated
In recent NTA instructions, a question that is answered and also "marked for review" is evaluated, while one only marked (with no answer) is not. Confirm this in the instructions on your screen before the exam starts. {{tag:third}}
:::
