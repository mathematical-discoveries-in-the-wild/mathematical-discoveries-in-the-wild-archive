# Verification Report

Status: `candidate_counterexample_likely_valid`

## Analytic audit

The proof was checked at the following points.

1. The piecewise upper boundary is concave: on `(-1,0)` its derivative
   decreases from infinity to one, and at zero it drops from one to zero.
   The reflected lower boundary is convex. Thus the proposed unit ball is
   compact, convex, centrally symmetric, and has the origin in its interior.
2. The only nonsmooth points are `A=(0,1)`, `B=(1,1)`, and their negatives.
   The supporting sets at the two positive corners are computed explicitly.
3. Kernel lines from every support at `A` or `B` meet either the strictly
   curved boundary (where the unique support is outside the signed original
   support segment) or the other corner (which has an explicit extra support).
   This proves local property (P) at the only points where it is nonautomatic.
4. At `x_r`, the tangent vector is parallel to `y_r`, proving exact
   Birkhoff-James orthogonality. At `y_r`, the unique support is the second
   coordinate functional, so the optimal reverse constant is exactly `2r-1`.

## Deterministic numerical check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2012.08162_property_p_not_uniformly_c_symmetric/code/verify_geometry.py \
  --figure runs/fa_banach_001/solutions/counterexamples/2012.08162_property_p_not_uniformly_c_symmetric/figures/unit_ball_geometry.png
```

The script samples 20,001 points on each boundary representation, checks the
three named support functionals, verifies five tangent pairs, and samples
2,000 kernel directions at each of the two positive corners. Final output is
as follows.

```text
max_named_support_error=0.000e+00
max_tangent_annihilation_residual=1.110e-16
max_boundary_residual=0.000e+00
max_reverse_constant_residual=0.000e+00
min_sampled_support_distance_at_A=4.714e-01
min_sampled_support_distance_at_B=7.454e-01
largest_sampled_reverse_constant=0.9998000
PASS
```

The computation is a regression check and figure generator. The proof of
property (P) and failure of uniform C-symmetry is analytic.

## Packet build and visual QA

`main.tex` was compiled with `latexmk -pdf -interaction=nonstopmode
-halt-on-error`. The final `solution_packet.pdf` has five letter-sized pages.
The log contains no LaTeX warnings, overfull or underfull boxes, or undefined
references. All five pages were rasterized with `pdftoppm` and inspected at
full resolution. The source-problem crop, theorem statement, displayed
formulae, unit-ball figure, proof ending, verification notes, and bibliography
are legible; no clipping, overlap, or malformed glyphs were found.

## Novelty bounds

The cheap run indexes were searched for arXiv:2012.08162, the title,
`C-approximately symmetric`, `local property (P)`, and Birkhoff-James terms.
A bounded primary-source web/arXiv search used the exact conjecture language,
paper title, and author combinations. It found the source and nearby work but
no later resolution or matching square-root-arc construction. This is not an
exhaustive novelty claim.

## Human review recommendation

Recommended focus: verify the two corner property-(P) checks, especially the
endpoint kernel directions, and confirm that the support-functional
characterization gives the *least* reverse epsilon as `2r-1`. Retain candidate
status until human mathematical review.
