# Partial Result: improved upper bound for the free-space distance in arXiv:1311.4584

Status: partial result, likely valid.

Source paper: Antonin Prochazka and Luis Sanchez-Gonzalez, "Low distortion embeddings into Asplund Banach spaces", arXiv:1311.4584.

Open-problem signal: after Proposition 4 in the appendix, the authors write that they do not know whether the Banach-Mazur distance between `F(M)` and `ell_1` is `2`; their proof gives at most `4`, while their `L_1` non-embedding result gives at least `2`.

Result in this packet: for the same metric space `M`,

```text
2 <= d_BM(F(M), ell_1) <= 3.
```

The lower bound is the source paper's argument: if `F(M)` were `(2-epsilon)`-isomorphic to `ell_1`, then the canonical Dirac embedding followed by the isomorphism would embed `M` into `ell_1` with distortion `<2`, contradicting Corollary 3 of the source paper. The new part is the upper bound `3`: send each singleton point `n` to the unit vector `e_n`, and each finite-subset point `A` to `2 e_A`. This linearizes to an isomorphism `T:F(M)->ell_1(N union F)` with `||T|| <= 3`, while `T^{-1}` maps `e_n` to `delta_n` and `e_A` to `delta_A/2`, so `||T^{-1}|| <= 1`.

What remains open: the exact value may still be `2`. The packet records failed full-closure routes and finite cut-metric LP checks for the finite truncations. Those checks do not prove a better lower bound for the free-space Banach-Mazur distance.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the arXiv source paper PDF, when available.
- `code/finite_l1_cut_lp.py`: finite cut-metric LP used as exploratory evidence.

Novelty/literature check: local run indexes contained no exact packet for arXiv:1311.4584 or this Banach-Mazur-distance question. Web searches on 2026-06-20 for exact phrases around the distance question, the paper title, and Prochazka-Sanchez-Gonzalez found the source paper and related later free-space literature, but no exact closure of the constant. The later Aliaga-Petitjean-Prochazka embedding theorem concerns free spaces over subsets of real trees and does not apply directly to this non-tree graph metric.
