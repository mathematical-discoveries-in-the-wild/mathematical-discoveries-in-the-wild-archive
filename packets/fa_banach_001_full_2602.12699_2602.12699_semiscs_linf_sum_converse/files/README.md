# Candidate Full Solution: Semi SCS Points in an `ell_infty` Sum

Status: candidate full positive answer, likely valid.

Source paper: arXiv:2602.12699, Sudeshna Basu, Priyanka Priyadarshini Behera, Susmita Seal, *Semi denting points and related notions in Banach spaces*.

Target: Question 4.6 asks whether, for Banach spaces `X` and `Y`, `x in semi SCS(B_X)` and `y in semi SCS(B_Y)` imply `(x,y) in semi SCS(B_{X \oplus_\infty Y})`.

Answer: yes.

## Proof Idea

Choose a small convex combination of slices around `x` in `B_X` and one around `y` in `B_Y`. For every pair of slices, form the slice of `B_{X \oplus_\infty Y}` defined by the average functional `(x_i^*,y_j^*)/2`. With a small enough slice aperture, this product-indexed slice lies inside the Cartesian product of the two original slices. Weight these product slices by `lambda_i mu_j`. Grouping first over `j` and then over `i` puts the first coordinate in the original convex combination around `x`; grouping in the other order puts the second coordinate in the original convex combination around `y`.

## Verification

- Cheap run indexes were searched for `2602.12699`, `semi SCS`, `semi denting`, and nearby terms. The only relevant hit was a separate prior counterexample packet for arXiv:2307.03621 about semi `w*`-denting and extreme points, not this stability question.
- Web searches on 2026-06-28 for exact phrases from Question 4.6 found only the source arXiv page and no later answer.
- The proof uses only the source definitions and the elementary identity `(X \oplus_\infty Y)^* = X^* \oplus_1 Y^*`.

## Files

- `main.tex`: full solution packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2602.12699.
- `figures/open_problem_crop.png`: crop of Theorem 4.5 and Question 4.6 from page 8.
