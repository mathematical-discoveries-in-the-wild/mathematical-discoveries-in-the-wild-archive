# Partial Result: compact Tandori function multipliers are trivial

- Run: `fa_banach_001`
- Source paper: Tomasz Kiwerski and Jakub Tomaszewski, *Essential norms of pointwise multipliers in the non-algebraic setting*, arXiv:2212.06723.
- Source location: Problem 7.5, page 51 of the source PDF; TeX source lines 2969--2981.
- Result type: partial result for Problem 7.5.
- Status: candidate partial result, likely valid; recommended for human review.

## Source Problem

Problem 7.5 asks what can be said about `(weakly) compact multipliers` between
abstract Tandori function spaces `\widetilde X` and `\widetilde Y`.

## Result

Let `I` be `(0,1)` or `(0,\infty)` with Lebesgue measure, and let `X` and `Y`
be Köthe function spaces on `I` in the source paper's convention. If

```text
M_lambda : \widetilde X -> \widetilde Y
```

is a compact multiplication operator, then `lambda = 0` almost everywhere.
Thus, in the standard non-atomic Tandori function setting, there are no
non-trivial compact multipliers.

## Proof Idea

If `lambda` is nonzero, then `|lambda| > eps` on a positive-measure set.
Inside a finite interval, split that set into infinitely many disjoint pieces
whose essential suprema are the same endpoint `b`. The characteristic
functions of those pieces all have the same Tandori majorant, namely
`\chi_(0,b)`, so after normalization they form a bounded sequence in
`\widetilde X`. Since the pieces are disjoint but all accumulate at the same
endpoint, the images under `M_lambda` stay separated in `\widetilde Y`. This
contradicts compactness.

## Verification

- `source_paper.pdf`: local copy of arXiv:2212.06723.
- `figures/open_problem_crop.png`: real crop of page 51 containing Problem 7.5.
- `main.tex` and `solution_packet.pdf`: formal proof packet.
- No computational verification is needed; the proof is a direct measure
  decomposition argument.

## Novelty / Duplicate Check

Local duplicate checks over `registry_index.tsv`, `solutions/index.tsv`,
`attempts/index.tsv`, `proof_gaps/index.tsv`, and active claims found no
existing packet or attempt for arXiv:2212.06723 or the Tandori compact
multiplier problem.

Bounded web searches on 2026-06-14 for exact and close phrases including
`"compact multipliers" "Tandori" function spaces`, `"Tandori function space"
"compact multipliers"`, `"weakly compact multipliers" "Tandori"`, and
`"Essential norms of pointwise multipliers" Tandori compact` found only the
source paper as a directly relevant hit and no later answer to Problem 7.5.

## Limitations

This answers the compact-multiplier part of Problem 7.5 in the standard
non-atomic interval setting for Tandori function spaces. It does not address
weakly compact multipliers. It also does not revise the source paper's Tandori
sequence-space results, where compactness is already characterized under the
paper's hypotheses.
