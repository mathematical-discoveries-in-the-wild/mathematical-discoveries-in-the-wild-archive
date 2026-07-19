# Partial Result Packet: Uniform Tail Property-(H) Obstruction

Run: `fa_banach_001`

Result type: `partial`

## Source Problem

- Valentin Ferenczi, Jordi Lopez-Abad, Behrang Mbombo, and Sebastien Todorcevic,
  *Local Banach-space dichotomies and ergodic spaces*, arXiv:2005.06458.
- Local PDF: `source_paper.pdf`.
- Location: Question 6.17, PDF page 60; parsed source
  `data/parsed/arxiv_sources/2005.06458/main.tex`, lines 2871--2885.

The packet addresses the second part of Question 6.17:

> Does every non-Hilbertian space with unconditional FDD have a non-Hilbertian
> subspace with an unconditional basis?

## Result

The packet proves a sufficient condition. Let `X` have an unconditional FDD
`(E_n)`. If there is a constant `lambda` such that every tail of the FDD
contains finite-dimensional block subspaces with normalized `lambda`-
unconditional bases and arbitrarily large Banach-Mazur distance from Euclidean
space, then `X` has a non-Hilbertian subspace with an unconditional basis.

Equivalently, a counterexample to Question 6.17(2) cannot have uniform
tail failure of Pisier property (H) along the FDD. It must be tail-Hilbertian
for every fixed unconditionality constant, unless it already has a
non-Hilbertian block subspace with an unconditional basis.

## Files

- `main.tex`: partial-result packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source/open-problem paper.
- `figures/open_problem_crop.png`: crop of Question 6.17.

## Human Review Recommendation

Check the abstraction step carefully: the proof is a direct block-FDD
concatenation argument modeled on the source paper's proof of Theorem 6.15,
but with the MNH hypothesis replaced by the explicit uniform tail witness
condition. The main theorem is intentionally only a sufficient condition, not
a full solution of Question 6.17(2).
