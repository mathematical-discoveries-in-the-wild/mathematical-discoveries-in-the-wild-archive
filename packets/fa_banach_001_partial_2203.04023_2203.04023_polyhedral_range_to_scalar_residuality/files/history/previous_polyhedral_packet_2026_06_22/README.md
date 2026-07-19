# Polyhedral Range Residuality Forces Scalar Residuality

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Mingu Jung, Miguel Martin, Abraham Rueda Zoca, "Residuality in the set of
  norm attaining operators between Banach spaces", arXiv:2203.04023.
- Local source PDF: `source_paper.pdf`.
- Open-problem evidence crop: `figures/open_problem_crop.png`.

## Source Question

Remark 4.2 asks whether residuality of `NA(X,Y)` for a non-trivial range
space `Y` implies residuality of scalar `NA(X,K)`, as density of
`ASE(X,Y)` does.

## Claimed Contribution

The packet proves an affirmative answer for finite-boundary range spaces.
In particular, if `Y` is a nonzero finite-dimensional real polyhedral Banach
space and `NA(X,Y)` is residual in `L(X,Y)`, then `NA(X,K)` is residual in
`X*`.

The proof works more generally when `Y` has a finite norming boundary modulo
rotations with a non-redundant exposed coordinate.  On an open region of
`L(X,Y)` where that coordinate strictly dominates all other boundary
coordinates, norm-attainment of an operator is exactly scalar norm-attainment
of the dominant coordinate.  Product Baire category then transfers residuality
back to `X*`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2203.04023.
- `figures/open_problem_crop.png`: screenshot crop of Remark 4.2.
- `tmp/`: LaTeX build intermediates and rendered page image used for cropping.

## Human Review Notes

Verifier focus:

- Check the domination equivalence
  `T in NA(X,Y) <=> phi_0 o T in NA(X,K)` on the open set where `phi_0`
  strictly dominates the finite boundary.
- Check the Baire product reflection lemma used to pass residuality from
  `NA(X,Y)` on open product regions to residuality of scalar `NA(X,K)` on
  annuli `{||f||>1/m}`.
- Check that the finite-boundary hypothesis is correctly specialized to
  finite-dimensional real polyhedral spaces using dual vertices modulo sign.

No computational verification is needed; the argument is purely analytic.

## Limitations

This does not settle the full question in Remark 4.2.  The proof depends on
an isolated boundary coordinate and therefore does not cover smooth or
strictly convex finite-dimensional ranges such as the Euclidean plane.
