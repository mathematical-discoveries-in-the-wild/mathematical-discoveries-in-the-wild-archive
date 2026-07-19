# Norm-Attaining Operators of Every Finite Rank on Martin's Space

Result type: `full`

Status: `full_solution_likely_valid`

Run: `fa_banach_001`

Source paper:

- Miguel Martin, "A Banach space whose set of norm-attaining functionals is
  algebraically trivial", arXiv:2406.07273.
- Local source PDF: `source_paper.pdf`.
- Open-problem evidence crop: `figures/open_problem_crop.png`.

## Incorporation Check

The existing registry entry for arXiv:2406.07273 pointed to
`solutions/partial/2406.07273_fixed_kernel_rank_two_nowhere_dense/`, whose
README stated explicitly that it did not solve Open Problem 7.  It proved only
that, after fixing a codimension-two kernel, norm-attainment is nowhere dense
in the corresponding operator fibre.

The submitted report is therefore not already incorporated.  It contains the
previous fixed-kernel result as an audited partial theorem, but also adds a
positive construction of norm-attaining operators of every prescribed finite
rank.  In particular it answers Open Problem 7 affirmatively for
`NA(X, ell_2^2)`.

## Claimed Contribution

Let `X` be Martin's smooth renorming of `c0` from arXiv:2406.07273.  For every
integer `n >= 1` and every real Banach space `Y` with `dim Y >= n`, the packet
constructs an operator `T : X -> Y` such that:

- `T` attains its norm,
- `rank T = n`,
- hence, for `n = 2` and `Y = ell_2^2`, `NA(X, ell_2^2)` contains a rank-two
  operator.

The mechanism is a graph-sum lifting argument for the final norm
`p(x) = ||x||_0 + lambda ||Rx||`.  A finite-rank norm-attaining operator for
the old norm is perturbed by one rank-one term using a functional in
`R^*(W^*)`; Martin's range-separation property keeps this new functional
outside the old finite-dimensional adjoint range, preserving rank.

## Upgrade History

- Previous active packet:
  `history/2026-06-23_previous_fixed_kernel_partial/2406.07273_fixed_kernel_rank_two_nowhere_dense/`.
- Submitted upgrade evidence:
  `evidence/2026-06-23_martin_rank_two_solution/martin_rank_two_solution.tex`
  and
  `evidence/2026-06-23_martin_rank_two_solution/martin_rank_two_solution.pdf`.

## Files

- `main.tex`: upgraded LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2406.07273.
- `figures/open_problem_crop.png`: crop showing Open Problem 7.
- `history/`: previous partial packet, preserved verbatim.
- `evidence/`: submitted TeX/PDF report.
- `tmp/`: LaTeX build outputs and rendered review pages.

## Human Review Notes

Verifier focus:

- Check that the structural properties of Martin's construction are cited with
  the correct scope: `NA(X_0,R)=c00`, injectivity of `R` and `R^*`, inclusion
  `R^*(W^*) subset Yop`, and separation `Yop cap NA(X_0,R) = {0}`.
- Check the graph-sum lifting lemma, especially the rank-preservation step
  using `R^*w^* notin ran S^*`.
- Check that the theorem proves only existence of rank-two norm-attaining
  operators, not the broader density problem for `NA(X, ell_2^2)`.

No computational verification is needed; the argument is analytic.
