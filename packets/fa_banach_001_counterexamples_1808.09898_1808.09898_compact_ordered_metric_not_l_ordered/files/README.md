# Counterexample: a compact ordered metric space need not be L-ordered

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source paper: arXiv:1808.09898, Tobias Fritz and Paolo Perrone,
*Stochastic order on metric spaces and the ordered Kantorovich monad*.

## Claim

Problem 4.1.3 asks whether every compact ordered metric space is
automatically L-ordered.  The packet gives a negative answer.

On the usual compact metric space `[0,1]`, put

```text
epsilon_n = sqrt(2) / n^3,
a_{n,i} = i/n,
b_{n,i} = (i+1)/n - epsilon_n
```

for `n >= 2` and `0 <= i <= n-1`, and define the order relation as the
diagonal together with the pairs `a_{n,i} <= b_{n,i}`.  This relation is a
closed partial order, so `[0,1]` is a compact ordered metric space.

However, every short monotone function `f : [0,1] -> R` satisfies
`f(0) <= f(1)`, while `0` is not below `1` in the order.  Hence the space is
not L-ordered.

## Key mechanism

For each `n`, the order gives tiny one-way rungs

```text
i/n <= (i+1)/n - epsilon_n
```

and Lipschitz continuity bridges the gap from
`(i+1)/n - epsilon_n` to `(i+1)/n`.  Chaining the inequalities gives
`f(0) <= f(1) + n epsilon_n`, and `n epsilon_n -> 0`.

The order stays closed because the off-diagonal rungs have length tending to
zero; all their new accumulation points lie on the diagonal.  It stays
transitive because all first coordinates of nontrivial order pairs are
rational and all second coordinates are irrational, so no nontrivial pair can
feed into another.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_problem_crop.png` - page 18 crop containing Problem 4.1.3.

## Novelty check

Before promotion, the local run indexes and local arXiv source corpus were
searched for `1808.09898`, `compact ordered metric space`, `L-ordered`,
`short monotone`, `ordered Kantorovich`, and close variants.  No existing
packet or later local answer to Problem 4.1.3 was found.  Web searches for the
exact problem sentence and for close phrases around `L-ordered metric spaces`
and `compact ordered metric space` returned the source paper but no explicit
later solution.  Novelty confidence is therefore moderate-to-high, subject to
human review.
