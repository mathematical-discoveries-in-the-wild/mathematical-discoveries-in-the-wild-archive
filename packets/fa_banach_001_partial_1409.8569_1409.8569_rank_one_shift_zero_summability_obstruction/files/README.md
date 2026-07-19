# Partial result: the rank-one shift model has no gap divergence above exponent 1

Status: `partial_result_likely_valid`.

## Source target

Source: Michael Demuth, Franz Hanauska, Marcel Hansmann, and Guy Katriel,
*Estimating the number of eigenvalues of linear operators on Banach spaces*,
arXiv:1409.8569.

The final section asks whether, for compact perturbations of bounded operators
on general Banach spaces, the optimal eigenvalue-gap exponent is `q_B(p)=p`
for `p>=1`, whether it is strictly larger, or whether the paper's upper bound
`p+1` is sharp.

## Result

The paper's own finite-rank example is based on the unilateral shift on
`ell_1` and a rank-one perturbation encoded by
`h(w)=1-sum b_k w^k` with bounded coefficients. For every such bounded
coefficient sequence, the zeros of `h` in the disk satisfy
`sum (1-|w|)^q < infinity` for every `q>1`. Consequently the eigenvalue gaps
in this rank-one shift model satisfy
`sum (|lambda|-1)^q < infinity` for every `q>1`.

Thus this model cannot improve the lower bound in the source paper beyond the
endpoint exponent `1`; in particular it cannot show `q_B(p)>p` for any
`p>=1` and cannot witness sharpness of the `p+1` upper bound.

## Mechanism

Bounded coefficients imply the radial growth estimate
`|h(re^{it})| <= C/(1-r)`. Jensen's formula then bounds the number of zeros
inside `|w| <= 1-2^{-m}` by `O(m 2^m)`. Summing over dyadic annuli gives
`sum (1-|w|)^q < infinity` exactly for `q>1`.

## Scope

This is not a full solution of the `q_B(p)` problem. It rules out one natural
route: pushing the source paper's rank-one `ell_1` shift construction to
produce divergence at exponents greater than `1`.

## Files

- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv PDF.
- `figures/open_problem_crop.png`: crop of the final open-problems passage.
- `source_1409.8569.tex`: parsed source TeX used for local inspection.
- `code/crop_open_problem.py`: reproducible crop helper.

## Verification

Rendered with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp
main.tex`. The source crop and final PDF were visually spot-checked.

Ledger: `runs/fa_banach_001/ledger/results/1409.8569_rank_one_shift_zero_summability_obstruction.json`.
