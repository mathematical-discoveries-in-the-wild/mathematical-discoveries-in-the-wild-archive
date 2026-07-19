# Full Characterization of Interior APEPs in `ell_p`-Sums

Result type: `full`

Status: candidate full solution, likely valid pending human review.

Source paper:

- Ramon J. Aliaga, Luis C. Garcia-Lirola, Juan Guerrero-Viu, Matias Raja,
  Abraham Rueda Zoca, "Almost preserved extreme points", arXiv:2510.21234.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper asks Question 8.2: for an `ell_p`-sum
`X=(oplus_i X_i)_p`, `1<p<infty`, characterize the interior APEPs of
`B_X`.

This packet gives an exact characterization using coordinate admissible
radii. If

`C_i = closure^{w*}(ext B_{X_i**})`,

then a radius `r` is admissible for `x_i` when `x_i in r C_i`. In finite
nonzero sums, excluding the trivial zero direct sum, the admissible radii
must be chosen with `p`-sum exactly one. In infinite nonzero sums, the
`p`-sum of the least admissible radii must be at most one, because any
remaining mass can be placed outside the finite weak-star test.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of the
  open question from page 37 of the source paper.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The proof depends on:

- the source paper's APEP characterization by weak-star closure of
  extreme points;
- the standard extreme-point formula for `ell_p`-sums;
- compactness of coordinate weak-star closures;
- finite-support approximation in the dual
  `X*=(oplus_i X_i*)_q`, used only in the infinite-summand sufficiency
  direction.

This packet supersedes the earlier partial result
`solutions/partial/2510.21234_infinite_summand_lpsums_apep/`.
