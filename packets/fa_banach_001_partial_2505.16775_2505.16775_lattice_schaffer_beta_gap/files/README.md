# Improved Gap for the Lattice Schaffer Constants

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Michael A. Rincon-Villamizar and Timur Oikhberg, "The lattice Schaffer
  constant", arXiv:2505.16775.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Source Problem Context

Remark 3.7 of the source paper asks for the maximal possible values of
`beta(X)/lambda^+(X)` and `beta(X)-lambda^+(X)` over Banach lattices. The paper
gives a 3-dimensional example with

`beta(X)=15/11` and `lambda^+(X) <= 4/3`,

which yields lower bounds `45/44` for the ratio and `1/33` for the difference
if the displayed upper bound on `lambda^+` is sharp.

## Claimed Contribution

This packet gives a simpler 3-dimensional Banach lattice with exact constants

`lambda^+(X)=4/3` and `beta(X)=3/2`.

Therefore the unknown global maxima satisfy

`sup beta/lambda^+ >= 9/8`

and

`sup (beta-lambda^+) >= 1/6`.

The construction is `R^3` with coordinatewise order and the lattice norm

`||(a,b,c)|| = max{|a|+2|c|/3, |b|+2|c|/3, |a|+|b|}`.

## Verification Notes

- `main.tex` contains a direct proof of both exact constant computations.
- `code/verify_constants_and_crop.py` enumerates active faces for this
  polyhedral norm and independently recovers `lambda^+=4/3` and `beta=3/2`.
  The proof in `main.tex` does not rely on the script.
- The same script can reproduce the crop from `tmp/source_page-06.png` if the
  page render is present.

## Novelty Caution

Cheap index searches for `2505.16775`, `lattice Schaffer`, `Riesz angle`,
`beta/lambda`, and nearby terms found no prior packet for this paper. No broad
external web/literature search was performed for this partial packet. The
claim should be reviewed as a new local construction improving the source
paper's displayed lower bounds, not as a proof of the exact maxima.

## Files

- `main.tex`: self-contained LaTeX packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: locally rendered source paper PDF from the arXiv TeX.
- `figures/open_problem_crop.png`: crop around Remark 3.7.
- `code/verify_constants_and_crop.py`: active-face verifier and crop helper.
- `tmp/`: build and render intermediates.

## Human Review Notes

Verifier focus:

- Check the definition of `beta(X)` uses disjoint positive unit vectors and
  that the support case split in `R^3` is exhaustive.
- Check the lower bound for `lambda^+`: every positive unit vector satisfies
  `x+y+2z/3 >= 1`, and the three defining functionals of a sum add to twice
  this quantity.
- Check that the result is properly scoped as a lower-bound improvement for
  the maximal-value problem, not a solution of the maxima.
