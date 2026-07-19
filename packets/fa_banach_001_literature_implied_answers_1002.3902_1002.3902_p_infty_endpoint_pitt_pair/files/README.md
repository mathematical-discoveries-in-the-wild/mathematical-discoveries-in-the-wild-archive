# Literature-Implied Answer: The p = infinity Endpoint of Proposition 3.6

Run: `fa_banach_001`

Status: `literature_implied_answer`

## Source Problem

- O. I. Reinov, *Approximation of operators in Banach spaces*,
  arXiv:1002.3902.
- Source location: PDF page 10; parsed source
  `data/parsed/arxiv_sources/1002.3902/source.tex`, lines 1365--1390.

Remark 3.7 says that it is seemingly unknown whether Proposition 3.6 remains
true for `p = +infty`.

## Answer

Yes. Take `X = ell_r` and `Y = ell_s`, where `1 < s < r < infinity`.
These spaces are separable and reflexive. For `p = infinity`,
`Pi_infty(X,Y) = L(X,Y)` and `tau_infty` is the compact-open topology.

By Pitt's theorem, every bounded operator `ell_r -> ell_s` is compact. Since
`ell_s` has the approximation property, every compact operator
`ell_r -> ell_s` is norm-approximable by finite-rank operators. Therefore
`L(X,Y)` equals the norm closure of finite-rank operators. On the other hand,
finite-rank operators are compact-open dense in `L(X,Y)`, so the
`tau_infty` closure also equals `L(X,Y)`. Thus the endpoint equality in
Proposition 3.6 holds for this pair.

## Scope

This answers the existence question in Remark 3.7, not a stronger universal
statement about all pairs `X,Y`. The supporting theorem is classical Pitt
compactness; no later paper was found in the run indexes explicitly presenting
this as an answer to Reinov's remark.

## Files

- `main.tex`: compact status note and proof.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source crop containing Proposition 3.6 and
  Remark 3.7.
