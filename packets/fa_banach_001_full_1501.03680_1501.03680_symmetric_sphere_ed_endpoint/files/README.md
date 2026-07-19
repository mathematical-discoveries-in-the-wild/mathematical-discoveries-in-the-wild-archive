# Candidate Full Solution: Symmetric-Sphere Entropy Endpoint

Source paper: Aicke Hinrichs and Sebastian Mayer, *Entropy Numbers of
Spheres in Banach and quasi-Banach spaces*, arXiv:1501.03680; Journal of
Approximation Theory 200 (2015), 144-152, DOI
10.1016/j.jat.2015.05.004.

Result type: `full`

Status: candidate full solution, likely valid, pending human review.

## Open Problem Signal

Remark 14, immediately after Corollary 13 in the source paper, says that the
symmetric-Banach-space estimate in Corollary 13 is not extended to `k >= d`
because the authors do not know how `e_d(S_X,Y)` behaves.

## Candidate Contribution

For symmetric `d`-dimensional Banach spaces `X` and `Y` with normalized
canonical bases, the same two-sided estimate from Corollary 13 extends to every
`k >= d`:

```text
e_k(S_X,Y) asymp 2^{-k/(d-1)} lambda_Y(d-1)/lambda_X(d-1),
```

with absolute constants independent of `d`, `k`, `X`, and `Y`.

The lower estimate is already implicit in the source paper: combine its
hyperplane lower bound with Schuett's ball entropy estimate in dimension
`d-1`. The finite endpoint window is handled by
`e_k(S_X,Y) <= e_d(B_X,Y)` and Schuett's ball estimate in dimension `d`,
followed by the elementary symmetric-basis inequalities
`lambda_X(d) >= lambda_X(d-1)` and `lambda_Y(d) <= 2 lambda_Y(d-1)`.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: crop of page 9 showing Remark 14.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates and rendered source page images.

## Novelty Check

Cheap run indexes were searched for arXiv:1501.03680, the paper title,
`entropy numbers of spheres`, `symmetric Banach spaces`, and nearby endpoint
phrases; no duplicate packet, prior attempt, or proof-gap packet for this
endpoint was found. Bounded web searches on July 19, 2026 for exact phrases
from Remark 14, `e_d(Sphere_X,Y)`, and the title found bibliographic/source
pages for the Hinrichs--Mayer paper but no separate later answer to the
endpoint question.

## Human Review

Recommended check: verify the finite-window upper bound, especially the
factorization through `ell_infty^d` and the use of Schuett's Theorem 5(2) in
dimension `d` for `e_d(B_X, ell_infty^d)`. Also note that the source paper's
upper-bound discussion writes an operator norm in the opposite orientation in
one place; the factorization used here is explicitly `ell_infty^d -> Y`.
