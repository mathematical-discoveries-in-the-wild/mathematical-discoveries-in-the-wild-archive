# Counterexample to the Infinite `ell_1`-Sum Zero APEP Question

Result type: `counterexample`

Status: candidate counterexample, likely valid pending human review.

Source paper:

- Ramon J. Aliaga, Luis C. Garcia-Lirola, Juan Guerrero-Viu, Matias Raja,
  Abraham Rueda Zoca, "Almost preserved extreme points", arXiv:2510.21234.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Question 8.1 asks whether, for an arbitrary infinite family of Banach
spaces `X_i` and its `ell_1`-sum `X`, the condition that `0` is an APEP of
`B_X` forces `0` to be an APEP of `B_{X_i}` for some coordinate.

The packet gives a negative answer. Let `H_n = R^n` with the Euclidean
norm and set

`X = (oplus_{n>=1} H_n)_1`.

No coordinate `H_n` has `0` as an APEP, because finite-dimensional weak
neighbourhoods of `0` can be chosen inside a small norm ball and no slice
of the unit ball is contained there.

Nevertheless, `0` is an APEP of `B_X`. Given finitely many weak tests in
`X* = (oplus H_n)_infty`, choose a coordinate `H_n` of dimension larger
than the number of tests and a unit vector orthogonal to all test
coordinates. A thin slice around that vector is contained in the original
weak neighbourhood of `0`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of Question
  8.1 from page 37 of the source paper.
- `code/check_slice_estimate.py`: numerical sanity check for the Hilbert
  slice estimate used in the proof.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Human Review Notes

The proof uses the definition of APEP directly, not an extreme-point
description of the bidual of an infinite `ell_1`-sum. This is intentional:
the direct slice argument avoids a possible source of unnecessary
technical fragility.

