# Isolated Norming Orbit Residuality Forces Scalar Residuality

Result type: `partial`

Status: candidate strengthened partial result, likely valid pending human review.

Source paper:

- Mingu Jung, Miguel Martin, Abraham Rueda Zoca, "Residuality in the set of
  norm attaining operators between Banach spaces", arXiv:2203.04023.
- Local source PDF: `source_paper.pdf`.
- Open-problem evidence crop: `figures/open_problem_crop.png`.

## Source Question

Remark 4.2 asks whether residuality of `NA(X,Y)` for a non-trivial range
space `Y` implies residuality of scalar `NA(X,K)`, as density of
`ASE(X,Y)` does.

## Upgrade Incorporated

The supplied report
`evidence/supplied_residuality_isolated_norming_2026_06_22/residuality_isolated_norming.tex`
audits the previous finite-boundary packet and strengthens it.

The earlier packet claimed an affirmative answer for finite-boundary and
finite-dimensional real polyhedral ranges, using a Baire product step.  The
report correctly flags that the unrestricted Kuratowski--Ulam section theorem
was not justified in the possibly nonseparable setting.  The active packet now
uses the special cylinder-reflection theorem for completely metrizable spaces
instead, and explicitly records the domination-region equality
`||T|| = ||phi_0 o T||`.

## Claimed Contribution

If `Y` has a norming set with one isolated norming orbit, witnessed by
`(phi_0,y_0)`, and if a closed operator subspace contains all rank-one
operators `y_0 tensor f`, then residuality of `NA(X,Y)` in that subspace
forces residuality of scalar `NA(X,K)` in `X*`.

Consequences include:

- the previous finite-boundary result;
- nonzero finite-dimensional real polyhedral ranges;
- ranges with property quasi-beta;
- finite-dimensional ranges whose dual ball has only countably many extreme
  point orbits modulo unimodular scalars.

For the last class, the source paper's forward implication gives an equivalence
between scalar and vector-valued residuality.

## Files

- `main.tex`: consolidated strengthened LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2203.04023.
- `figures/open_problem_crop.png`: screenshot crop of Remark 4.2.
- `evidence/supplied_residuality_isolated_norming_2026_06_22/`: supplied TeX
  and PDF report.
- `history/previous_polyhedral_packet_2026_06_22/`: previous active
  finite-boundary packet snapshot.
- `tmp/`: LaTeX build intermediates and rendered verification pages.

## Human Review Notes

Verifier focus:

- Check the cylinder-reflection theorem used in place of the unrestricted
  Kuratowski--Ulam section argument.
- Check the domination equivalence on the open region where the isolated orbit
  dominates all other norming functionals.
- Check the quasi-beta and countably-many-extreme-orbits corollaries.

No computational verification is needed; the argument is purely analytic.

## Limitations

This remains a partial answer to Remark 4.2.  The proof depends on a geometric
gap isolating one norming orbit.  Smooth ranges such as the Euclidean plane
remain outside the method, and no full proof or counterexample for arbitrary
nonzero `Y` is claimed.
