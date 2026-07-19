# Signed uniformly distributed sequences by Jordan interleaving

Status: full_solution_likely_valid.

Source target: S. K. Mercourakis and G. Vassiliadis, *Uniform
Distribution of Sequences and its interplay with Functional Analysis*,
arXiv:2102.02306, concluding future-work item 2(b).

## Result

The future-work question 2(b) has an affirmative answer in its natural stated
generality.

Let `K` be a compact Hausdorff space such that every probability measure
`nu in P(K)` admits a uniformly distributed sequence in the classical sense.
Then every real signed regular Borel measure `mu in M(K)` with `||mu||=1`
admits a `mu`-u.d. sequence in the sense of Definition 1 of the source paper.

Consequently, all classes of compact non-metrizable spaces mentioned in item
2(b), including the compact separable group cases under the set-theoretic
hypotheses cited there, also have the signed-measure property.

## Idea

Write the Jordan decomposition `mu = mu^+ - mu^-`, and put
`alpha = mu^+(K)`, `beta = mu^-(K)`, so `alpha + beta = 1`. If both masses are
positive, choose ordinary u.d. sequences for the probability measures
`mu^+/alpha` and `mu^-/beta`. Then interleave the two sequences with
asymptotic densities `alpha` and `beta`, assigning sign `+1` to the first
sequence and `-1` to the second. The unsigned averages converge to `|mu|`,
while the signed averages converge to `mu`.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2102.02306.
- `figures/open_problem_crop.png`: source future-work item 2(b).
- Ledger: `runs/fa_banach_001/ledger/results/2102.02306_signed_ud_jordan_interleaving.json`.

## Novelty Check

The run's cheap indexes had no prior packet, attempt, or proof-gap entry for
arXiv:2102.02306 or this signed u.d. sequence question. Local corpus searches
for signed uniformly distributed sequence terminology found the source paper
and unrelated signed-sum results, but no later solution.

Web/arXiv spot checks on 2026-06-30 for exact phrases around
`2102.02306 signed measure uniformly distributed`, `every signed measure
admits a u.d. sequence`, `compact non-metrizable signed measure u.d. sequence`,
and `Mercourakis Vassiliadis Uniform Distribution of Sequences` found the
source paper but no exact later resolution.

## Human Review

Recommended review focus: confirm that the source future-work item assumes the
ordinary probability-measure u.d. property for every probability measure on
`K`, and check the density-controlled interleaving calculation. The proof is
otherwise just Jordan decomposition plus weak-star testing against
`C(K)`.
