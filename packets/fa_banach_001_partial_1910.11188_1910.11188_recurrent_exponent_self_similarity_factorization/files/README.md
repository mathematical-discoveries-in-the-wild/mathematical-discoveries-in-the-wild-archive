# Recurrent exponent self-similarity for the Lechner--Motakis--Mueller--Schlumprecht factorization problem

Status: `partial_result_likely_valid`

Source paper: R. Lechner, P. Motakis, P. F. X. Mueller, and Th. Schlumprecht, *The factorization property of ell^\infty(X_k)*, arXiv:1910.11188.

Target: Question 2 on page 26 asks whether the Haar array has the factorization property in
`Z = ell^\infty(L^{p_k}: k in N)` when `p_k -> 1` or `p_k -> infinity`.

## Result

This packet proves a self-similarity criterion adjacent to the source questions. If the exponent sequence
`(p_k)` is recurrent, meaning that for every `k` and every `epsilon > 0` the set
`{m : |p_m - p_k| < epsilon}` is infinite, then the Haar array has the large-diagonal
factorization property in `ell^\infty(L^{p_k})`.

The proof upgrades Theorem 2.5 of the source paper: their theorem factors the identity on a selected
sub-sum `Z_Gamma`; recurrence lets us choose `Gamma` so that `Z_Gamma` is isomorphic to the original
mixed sum.

## Scope

This does not settle the strict endpoint cases in Question 2. If `p_k -> 1` or `p_k -> infinity`
with genuinely isolated early exponents, the recurrence hypothesis fails, and the missing step is
exactly absorption of those isolated `L^p` coordinates into endpoint tails.

## Files

- `main.tex`: full partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1910.11188.
- `figures/open_problem_crop.png`: crop of Question 2 from the source PDF.

## Verification

Rendered with `pdflatex` on 2026-06-23. No computational verification is involved; the human-review
focus is the generalized use of the source paper's Proposition 7.2 and the Pelczynski decomposition
step.
