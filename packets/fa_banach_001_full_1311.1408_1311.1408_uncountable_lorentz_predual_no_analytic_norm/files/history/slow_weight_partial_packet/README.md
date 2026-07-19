# Partial packet: slow Lorentz weights obstruct analytic renorming

Source paper: Victor Bible, *Using boundaries to find smooth norms*,
arXiv:1311.1408.

Status: claimed partial result, likely valid, pending human review.

## Source question

Remark 3.10 says that for uncountable `A`, the Lorentz predual
`X = d_*(w,1,A)` is a new example with a `C^\infty` smooth renorming, and it
is not yet known whether `X` has an analytic renorming.

## Result

The packet proves a negative answer for slow Lorentz weights:

> If `A` is uncountable and the standard decreasing Lorentz weight `w` satisfies
> `w notin ell_q` for every finite `q >= 1`, then `d_*(w,1,A)` has no
> equivalent analytic norm.

This covers weights such as `w_j = 1 / log(j+2)`. It does not settle weights
that belong to some finite `ell_q`, for example `w_j = 1/(j+1)`.

## Proof mechanism

Under the slow-weight hypothesis, every continuous homogeneous polynomial on
`d_*(w,1,A)` is countably supported. If a multilinear form had uncountably many
nonzero coordinate coefficients, a Delta-system argument and sign averaging
would force bounded inputs to produce values growing like `sum_j w_j^r` for
some finite `r`, contradicting continuity.

An analytic function is locally a countable sum of homogeneous polynomials, so
near the origin it can depend on only countably many coordinates. An analytic
norm would produce an analytic separating function; a fresh coordinate outside
that countable support gives the contradiction.

## Files

- `main.tex`: source for the proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the arXiv source paper.
- `figures/open_problem_crop.png`: crop of Example 3.9 and Remark 3.10.
- `code/crop_open_problem.py`: crop-generation script.

## Novelty and duplicate check

The run indexes were searched for `1311.1408`, `Using boundaries to find smooth
norms`, `d_*(w,1,A)`, `Lorentz predual`, and `analytic renorming`; no previous
packet was found. Web searches on 2026-06-20 for the exact analytic-renorming
question and close Lorentz-predual phrases did not locate a full later answer.

The later Dantas-Hajek-Russo paper gives a model obstruction for dense
subspaces of `c0(omega_1)`, but it does not directly answer Bible's question
because the `d_*(w,1,A)` norm is stronger than the inherited `c0(A)` norm.

## Review focus

- Check the Delta-system/sign-averaging proof of countable support for
  homogeneous polynomials.
- Check the monotone-weight convention. If the source is read literally for
  nonmonotone positive weights, the theorem should retain the explicit
  monotonicity assumption or pass to the nonincreasing rearrangement.
- Check that the analytic-separation fact is applied with respect to an
  equivalent analytic norm, so the continuous polynomial spaces are unchanged.
