# Statistics & Probability {#m13}

:::stats
Typical questions | 2–3 per shift
Difficulty | Medium
Priority | Must-do
NCERT | Class 11 · Ch 13, 14 · Class 12 · Ch 13
Study time | ~12 hours
:::

## Core concepts

- **Statistics:** measures of central tendency (mean, median, mode) and dispersion (mean deviation, variance, standard deviation) for grouped and ungrouped data.
- **Probability:** events and their probabilities, the addition and multiplication theorems, conditional probability, **total probability and Bayes' theorem**, and random variables with their distributions (mean and variance).

:::note Syllabus note
The official Unit 13 text lists measures of dispersion (mean, median, mode, SD, variance, mean deviation), probability of an event, the addition and multiplication theorems, Bayes' theorem and the probability distribution of a random variate [NTA-SYL]. Check the current PDF for Bernoulli trials and the binomial distribution. The two binomial formulas are included below as a cheap tool either way {{tag:rec}}.
:::

## Important formulas: statistics

:::formula Central tendency
Mean $\bar x = \dfrac{\sum f_ix_i}{\sum f_i}$. Assumed-mean method: $\bar x = A + \dfrac{\sum f_id_i}{N}$ with $d_i = x_i - A$ (or step deviation $\times h$).
**Median (grouped):** $l + \dfrac{N/2 - C}{f}\,h$, where $C$ is the cumulative frequency before the median class.
**Mode (grouped):** $l + \dfrac{f_1 - f_0}{2f_1 - f_0 - f_2}\,h$.
Empirical relation (moderately skewed data): Mode $\approx$ 3 Median $-$ 2 Mean.
:::

:::formula Dispersion
$$\sigma^2 = \frac{\sum f_i(x_i - \bar x)^2}{N} = \frac{\sum f_ix_i^2}{N} - \bar x^2 \qquad \text{MD}(a) = \frac{\sum f_i\lvert x_i - a\rvert}{N}$$
- **Change of origin and scale:** if $y = ax + b$, then $\bar y = a\bar x + b$, $\sigma_y = \lvert a\rvert\sigma_x$ and $\sigma_y^2 = a^2\sigma_x^2$. Adding a constant changes the mean, **not** the variance.
- The mean deviation is least when taken about the **median**.
- First $n$ natural numbers: mean $\dfrac{n + 1}{2}$, variance $\dfrac{n^2 - 1}{12}$.
- **Combined mean:** $\bar x = \dfrac{n_1\bar x_1 + n_2\bar x_2}{n_1 + n_2}$. **Combined variance:** $\sigma^2 = \dfrac{n_1(\sigma_1^2 + d_1^2) + n_2(\sigma_2^2 + d_2^2)}{n_1 + n_2}$ with $d_i = \bar x_i - \bar x$.
- **Correcting a wrong observation:** fix $\sum x$ and $\sum x^2$, then recompute. Never "adjust" the variance directly.
:::

## Important formulas: probability

:::formula Rules
$$P(A\cup B) = P(A) + P(B) - P(A\cap B) \qquad P(A') = 1 - P(A) \qquad P(A\mid B) = \frac{P(A\cap B)}{P(B)}$$
- **Independent events:** $P(A\cap B) = P(A)P(B)$. Then $A'$ and $B'$, $A$ and $B'$, and $A'$ and $B$ are also independent.
- **Mutually exclusive:** $P(A\cap B) = 0$. (Events with non-zero probability can't be both independent and mutually exclusive.)
- Three events: $P(A\cup B\cup C) = \sum P(A) - \sum P(A\cap B) + P(A\cap B\cap C)$.
- **"At least one":** $1 - P(\text{none})$.
:::

:::formula Total probability & Bayes
If $E_1, \dots, E_n$ partition the sample space:
$$P(A) = \sum_i P(E_i)P(A\mid E_i) \qquad P(E_k\mid A) = \frac{P(E_k)P(A\mid E_k)}{\sum_i P(E_i)P(A\mid E_i)}$$
Draw a **tree**: branches for $E_i$, then for $A$. Bayes' theorem is the chosen path divided by the sum of all paths that end in $A$.
:::

:::formula Random variables
$$\sum p_i = 1 \qquad E(X) = \mu = \sum x_ip_i \qquad \operatorname{Var}(X) = E(X^2) - \mu^2$$
**Binomial tool:** $P(X = r) = \binom nr p^rq^{n-r}$, mean $np$, variance $npq$.
:::

## Common question models

:::pyq Recurring structures
1. **Mean and variance** with a wrong observation corrected, or observations added/removed.
2. **Unknown observations** from a given mean and variance (e.g. find $a^2 + b^2$ or $\lvert a - b\rvert$).
3. **Effect of transformation** ($y = ax + b$) on the mean and SD.
4. **Mean deviation** about the mean or median.
5. **Bayes' theorem** (bags, machines, a test with false positives). This is a very common model.
6. **Random variable:** find $k$ from $\sum p = 1$, then $E(X)$ or $\operatorname{Var}(X)$.
7. **Dice, coins and cards** with conditional probability.
:::

## Shortcuts & fast methods

:::shortcut Work with Σx and Σx²
For any mean/variance manipulation, convert to $\sum x = n\bar x$ and $\sum x^2 = n(\sigma^2 + \bar x^2)$, change those two totals, then convert back.
**Time saved:** handles every "wrong observation / new observation" question with one method.
:::

:::shortcut Bayes by counting
Imagine 1000 items. With machine shares 50/30/20% and defect rates 2/3/4%, the defectives are 10, 9 and 8. $P(\text{machine 1}\mid\text{defective}) = \dfrac{10}{27}$.
:::

## Common mistakes

:::trap Mistake alerts
- Variance is in **squared units**; SD is its square root. Read which one is asked.
- Adding a constant doesn't change the SD; multiplying by $-2$ multiplies the SD by 2 (not $-2$).
- $P(A\mid B) \ne P(B\mid A)$. Identify the given condition carefully.
- "At least one boy": the sample space is $\{BB, BG, GB\}$, not $\{BB, BG\}$.
- Mutually exclusive is not the same as independent.
:::

## Practice questions

@@SET M13 · Practice

@@Q M13-01 | E | 0.75 | Variance | NV
Find the variance of $2, 4, 6, 8, 10$.
@ans 8
@sol The mean is 6. The squared deviations are $16 + 4 + 0 + 4 + 16 = 40$, so the variance is $40/5 = 8$.
@short —
@trap —
@@END

@@Q M13-02 | E | 0.5 | Change of scale | Speed
If the standard deviation of $x_1, \dots, x_n$ is 3, the standard deviation of $2x_1 + 5, \dots, 2x_n + 5$ is:
(A) 6
(B) 11
(C) 12
(D) 3
@ans A
@sol $\sigma_y = \lvert2\rvert\sigma_x$; the $+5$ has no effect.
@short —
@trap —
@@END

@@Q M13-03 | E | 0.5 | Variance of natural numbers | Speed
The variance of the first 10 natural numbers is:
(A) 8.25
(B) 9.17
(C) 5.5
(D) 10
@ans A
@sol $\dfrac{n^2 - 1}{12} = \dfrac{99}{12} = 8.25$.
@short —
@trap —
@@END

@@Q M13-04 | E | 0.5 | Mean deviation | NV
Find the mean deviation about the mean of $3, 5, 7, 9$.
@ans 2
@sol The mean is 6. $\dfrac{3 + 1 + 1 + 3}{4} = 2$.
@short —
@trap —
@@END

@@Q M13-05 | M | 1 | Grouped mode | NV
The modal class is 20–30 with frequency 12. The classes before and after it have frequencies 8 and 6. Find the mode.
@ans 24
@sol $20 + \dfrac{12 - 8}{24 - 8 - 6}\times10 = 20 + 4 = 24$.
@short —
@trap —
@@END

@@Q M13-06 | E | 0.5 | Combined mean | NV
One section of 30 students has a mean of 40, and another of 20 students has a mean of 50. Find the combined mean.
@ans 44
@sol $\dfrac{1200 + 1000}{50} = 44$.
@short —
@trap Averaging the two means (45).
@@END

@@Q M13-07 | M | 1.5 | Corrected observation | JEE
The mean and variance of 5 observations are 4 and 2. One observation, recorded as 5, was actually 10. The correct variance is:
(A) 8
(B) 6.4
(C) 2
(D) 10
@ans A
@sol Before: $\sum x = 20$ and $\sum x^2 = 5(2 + 4^2) = 90$. After the correction: $\sum x = 25$ and $\sum x^2 = 90 - 25 + 100 = 165$. New mean $= 5$; new variance $= \dfrac{165}{5} - 25 = 8$.
@short Work with the two totals, never with the variance directly.
@trap Correcting only the mean and keeping the variance at 2.
@@END

@@Q M13-08 | M | 1 | Independent events | Concept
$P(A) = 0.5$, $P(B) = 0.4$ and $P(A\cap B) = 0.2$. Which statement is true?
(A) $A$ and $B$ are mutually exclusive
(B) $A$ and $B$ are independent
(C) $P(A\cup B) = 0.9$
(D) $P(A\mid B) = 0.4$
@ans B
@sol $P(A)P(B) = 0.2 = P(A\cap B)$. Also $P(A\cup B) = 0.7$ and $P(A\mid B) = 0.5$.
@short —
@trap —
@@END

@@Q M13-09 | M | 1.5 | Bayes' theorem | JEE
Machines $M_1$, $M_2$ and $M_3$ make 50%, 30% and 20% of a factory's output, with defect rates 2%, 3% and 4%. A randomly chosen item is defective. The probability that it came from $M_1$ is:
(A) $\dfrac{10}{27}$
(B) $\dfrac{1}{2}$
(C) $\dfrac{9}{27}$
(D) $\dfrac{8}{27}$
@ans A
@sol $\dfrac{0.5(0.02)}{0.5(0.02) + 0.3(0.03) + 0.2(0.04)} = \dfrac{0.010}{0.027}$.
@short Per 1000 items: 10, 9, 8 defectives.
@trap —
@@END

@@Q M13-10 | M | 1 | Mean of a random variable | Basic
$X$ takes the values 0, 1 and 2 with probabilities $k$, $2k$ and $3k$. Then $E(X)$ equals:
(A) $\tfrac43$
(B) $\tfrac53$
(C) 1
(D) $\tfrac23$
@ans A
@sol $6k = 1 \Rightarrow k = \tfrac16$. $E(X) = 0 + \tfrac26 + \tfrac66 = \tfrac43$.
@short —
@trap —
@@END

@@Q M13-11 | M | 1.5 | Variance of a random variable | JEE
For the random variable in M13-10, $\operatorname{Var}(X)$ equals:
(A) $\tfrac59$
(B) $\tfrac73$
(C) $\tfrac{16}{9}$
(D) $\tfrac23$
@ans A
@sol $E(X^2) = \tfrac26 + \tfrac{12}{6} = \tfrac73$. $\operatorname{Var} = \tfrac73 - \tfrac{16}{9} = \tfrac59$.
@short —
@trap Giving $E(X^2)$ as the variance.
@@END

@@Q M13-12 | E | 0.5 | At least one | Speed
Three fair coins are tossed. The probability of at least one head is:
(A) $\tfrac78$
(B) $\tfrac12$
(C) $\tfrac38$
(D) $\tfrac34$
@ans A
@sol $1 - \tfrac18$.
@short —
@trap —
@@END

@@Q M13-13 | M | 1 | Conditional probability trap | Tricky
A family has two children, and at least one is a boy. The probability that both are boys is:
(A) $\tfrac13$
(B) $\tfrac12$
(C) $\tfrac14$
(D) $\tfrac23$
@ans A
@sol The reduced sample space is $\{BB, BG, GB\}$.
@short —
@trap Answering $\tfrac12$ by treating the known boy as a specific child.
@@END

@@SET M13 · Chapter Test

@@Q M13-T1 | E | 0.5 | Change of origin | Concept
If every observation is increased by 5, the variance:
(A) increases by 5
(B) increases by 25
(C) is unchanged
(D) is multiplied by 5
@ans C
@sol —
@short —
@trap —
@@END

@@Q M13-T2 | E | 0.75 | Union of independent events | Basic
$A$ and $B$ are independent with $P(A) = \tfrac13$ and $P(B) = \tfrac14$. Then $P(A\cup B)$ equals:
(A) $\tfrac12$
(B) $\tfrac7{12}$
(C) $\tfrac1{12}$
(D) $\tfrac{5}{12}$
@ans A
@sol $\tfrac13 + \tfrac14 - \tfrac1{12} = \tfrac{6}{12}$.
@short $1 - P(A')P(B') = 1 - \tfrac23\cdot\tfrac34 = \tfrac12$.
@trap —
@@END

@@Q M13-T3 | E | 0.5 | Cards | Speed
One card is drawn from a pack of 52. The probability that it is a king or a heart is:
(A) $\tfrac{4}{13}$
(B) $\tfrac{17}{52}$
(C) $\tfrac14$
(D) $\tfrac{1}{52}$
@ans A
@sol $\dfrac{4 + 13 - 1}{52} = \dfrac{16}{52}$.
@short —
@trap Double-counting the king of hearts (17/52).
@@END

@@Q M13-T4 | E | 0.5 | Removing an observation | Speed
The mean of 5 observations is 10. If the observation 20 is removed, the new mean is:
(A) 7.5
(B) 8
(C) 10
(D) 6
@ans A
@sol $\dfrac{50 - 20}{4}$.
@short —
@trap —
@@END

@@Q M13-T5 | E | 0.5 | Variance from sums | NV
For 10 observations, $\sum x = 50$ and $\sum x^2 = 300$. Find the variance.
@ans 5
@sol $30 - 25 = 5$.
@short —
@trap —
@@END

## Answers & Solutions {#m13-solutions}

@@ANSWERKEY

@@SOLUTIONS

:::revision Revision tracker · Statistics & Probability
[ ] Same day  [ ] Day 2  [ ] Day 7  [ ] Day 14  [ ] Day 30  [ ] Final week
:::
