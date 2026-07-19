# Literature Status: Compact Manifold CLSI

status: literature_already_answered
source_arxiv_id: 1807.08838
supporting_arxiv_id: 2007.06138
updated_at: 2026-07-19

## Source Question

Li Gao, Marius Junge, and Nicholas LaRacuente, *Fisher Information and
Logarithmic Sobolev Inequality for Matrix Valued Functions*, arXiv:1807.08838.

The source paper's final "Major Open Problems" subsection asks:

> Does every compact Riemanin manifold satisfy CLSI?

This is Problem 1 of the three listed major open problems.

## Supporting Answer

Michael Brannan, Li Gao, and Marius Junge, *Complete logarithmic Sobolev
inequalities via Ricci curvature bounded below*, arXiv:2007.06138, published
in Advances in Mathematics 394 (2022), article 108129.

The supporting paper cites arXiv:1807.08838 as `CLSI` and states in the
introduction that every heat semigroup on a connected compact weighted
Riemannian manifold satisfies CLSI. The theorem labelled `riemann` in the
arXiv source proves the stronger statement: if `(M,g,e^{-W}dvol)` is a compact
connected weighted Riemannian manifold, then the weighted heat semigroup
`exp(-t Delta_W)` satisfies `lambda`-CLSI for some `lambda > 0`. The
Laplace-Beltrami case is the special case `W=0`.

## Scope

This packet answers only Problem 1 in the source's Major Open Problems list.
It does not address:

- whether every generator of a selfadjoint semigroup on a matrix algebra
  satisfies CLSI;
- whether CLSI is stable under free products.

## Files

- `source_paper.pdf`: arXiv:1807.08838.
- `supporting_paper_2007.06138.pdf`: arXiv:2007.06138.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
