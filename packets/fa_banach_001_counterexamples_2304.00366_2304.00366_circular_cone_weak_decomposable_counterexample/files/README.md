# Counterexample packet: the circular cone is weakly decomposable

Status: likely valid counterexample.

Source paper: Maud Szusterman, "Extremizers in Soprunov and Zvavitch's Bezout inequalities for mixed volumes", arXiv:2304.00366.

Targeted question: Question 2 asks whether the cone
`C = Conv(e_n,B)`, where `B` is the Euclidean unit ball in `e_n^\perp`,
is weakly indecomposable.

Result: no for the support-inclusion formulation of Definition 7 in the
source paper. For any `n >= 3`, let `P` be a nondegenerate segment in
`e_n^\perp` and let `eps > 0`. Then `L = P + eps C` is a full-dimensional
convex body not homothetic to `C`, while `C + L = P + (1+eps)C` has surface
area measure supported only on the original lateral normal sphere of `C` and
the base normal. Thus `C` is weakly decomposable.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of Definition 7 and Question 2 in the source paper.

Scope: this answers the cone weak-indecomposability question negatively under
the source paper's displayed condition `supp(S_{K+L}) subset supp(S_K)`. It
does not claim to settle the stronger absolute-continuity variant
`S_{K+L} << S_K`, nor the broader Soprunov-Zvavitch minimizer conjecture for
`b_2(K)`.
