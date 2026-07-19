# Partial result: bounded-excess Gaussian polytopes have cotype 2

Status: `partial_result_likely_valid`.

## Source target

Source: Han Huang and Konstantin Tikhomirov, *Cotype of random polytopes*,
arXiv:2603.04749.

The source Open Problems section asks whether the cotype estimates for
Gaussian convex hulls can be made uniform for every `N >= n`, and also asks
the analogous question for random projections of the `N`-dimensional
cross-polytope.

## Result

For every fixed `M`, the subcase `N-n <= M` has a deterministic positive
answer: whenever the vectors `X_1,...,X_N` span `R^n`, the space
`(R^n, ||.||_{P_{N,n}})` has cotype 2 with constant depending only on `M`.
The same bounded-codimension conclusion holds for projections of the standard
cross-polytope.

For Gaussian vectors the spanning assumption holds almost surely, so this
covers the bounded-excess near-square regime excluded by the source theorem.

## Mechanism

Write `A: ell_1^N -> R^n` for `A e_i = X_i`. Then
`P_{N,n}=A(B_{ell_1^N})`, so `(R^n, ||.||_{P_{N,n}})` is the quotient
`ell_1^N / ker A`. If `dim ker A = N-n <= M`, an Auerbach-basis projection
complements `ker A` with norm at most `M`. Hence the quotient is
`(M+1)`-isomorphic to a subspace of `ell_1^N`. Since `ell_1` has cotype 2 and
cotype passes to subspaces and isomorphs with the distortion loss, the quotient
has cotype 2 with constant controlled by `M`.

## Scope

This does not solve the full arbitrary-`N` problem, because the constant grows
with the excess `M=N-n`. It also does not address the difficult regimes where
`N-n -> infinity`, including the polynomial and high-aspect windows discussed
in the previous attempt.

## Files

- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv PDF.
- `figures/open_problem_crop.png`: crop of the Open Problems section.
- `source_2603.04749.tex`: parsed source TeX.
- `code/crop_open_problem.py`: reproducible crop helper.

## Verification

Rendered with `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp
main.tex`. The source crop and final PDF pages were visually inspected.
