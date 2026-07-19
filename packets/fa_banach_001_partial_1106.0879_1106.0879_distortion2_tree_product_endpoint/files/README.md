# Partial result: the source's random-graph fractals are endpoint-positive at distortion 2

Status: `partial_result_likely_valid`

This packet records a narrow endpoint result for the distortion-2 question in
Mendel--Naor, arXiv:1106.0879. The source proves that for every
`delta > 0`, compact metric spaces of finite Hausdorff dimension contain
positive-dimensional subsets embedding into ultrametrics with distortion
`2 + delta`, and that below distortion `2` no positive-dimensional theorem is
possible. It explicitly says that the exact distortion `2` case remains open.

## Result

The tree-product spaces used in Section 10.3 of the source to prove the
strictly-below-2 obstruction are themselves 2-equivalent to ultrametric
spaces. Consequently, for those `G(n,1/2)` fractals:

- every positive-dimensional subset has Hilbert distortion at least `2`, by
  the source theorem;
- the whole compact fractal embeds into an ultrametric, hence into Hilbert
  space, with distortion at most `2`.

Thus the source's natural lower-bound family is exactly endpoint-sharp, not an
endpoint counterexample.

More generally, for the source's tree-of-finite-metrics construction, if each
level metric has diameter `1` and minimum nonzero distance at least `eta`, then
the whole tree product is `1/eta`-equivalent to an ultrametric by replacing
each level metric by its diameter.

## Scope

This does not solve the full distortion-2 nonlinear Dvoretzky problem for
Hausdorff dimension. It only settles an important family: the actual
random-graph fractals used in the source to show sharpness below `2`, plus the
same bounded-aspect tree-product class.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper arXiv:1106.0879.
- `figures/open_problem_crop.png`: PDF crop showing the source's distortion-2
  open-problem sentence.
- `code/crop_open_problem.py`: crop generation script.
- `tmp/`: LaTeX build intermediates.

## Human review note

The key check is the normalization in Section 10.3: after rescaling the
`G(n,1/2)` block metrics to diameter one, their minimum distance is `1/2`.
Then the canonical tree ultrametric lies between the source metric and twice
the source metric.
