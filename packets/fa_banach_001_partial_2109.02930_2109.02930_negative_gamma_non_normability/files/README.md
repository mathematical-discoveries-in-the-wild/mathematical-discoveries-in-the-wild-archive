# 2109.02930 negative gamma non-normability

Status: `partial_result_likely_valid`

Source: Haim Brezis, Andreas Seeger, Jean Van Schaftingen, and Po-Lam Yung, *Families of functionals representing Sobolev norms*, arXiv:2109.02930.

## Result

For every `N >= 1` and `-1 < gamma < 0`, the spaces `dot W^{1,1}(gamma)` and `dot BV(gamma)` from Section 7.1 of the source paper are not normable under their natural weak-`L^1` quasi-norm topology.

This gives a negative answer to the source normability question on the open interval `(-1,0)`.

## Remaining Scope

The endpoint `gamma = -1` remains open in this packet.

## Idea

The source paper's Cantor functions `u_m` have weak endpoint size growing like `m`. The added observation is that each `u_m` is a convex average of `2^m` one-scale transition atoms whose quasi-norms are uniformly bounded. If the quasi-norm topology came from an equivalent norm, the convex hull of the quasi-unit ball would be quasi-bounded, contradicting the growth of `u_m`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2109.02930.
- `figures/open_problem_crop.png`: source page containing the normability question.

## Review Focus

Check the uniform one-scale atom estimate, especially with the tensor cutoff in dimensions `N > 1`.
The endpoint `gamma = -1` is intentionally not claimed.
