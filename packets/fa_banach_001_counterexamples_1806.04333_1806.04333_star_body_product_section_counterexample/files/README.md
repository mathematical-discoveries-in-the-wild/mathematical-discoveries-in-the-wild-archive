# A star-body counterexample to the product-section inequality

Status: `candidate_counterexample_likely_valid (star-body strengthening)`.

Question 12 of Alexandros Eskenazis, *On extremal sections of subspaces of
L_p*, arXiv:1806.04333, asks in particular whether every symmetric convex,
"or even star," body `K` satisfies

\[
|K|^{n-1}\le |K^n\cap H_\theta|.
\]

The star-body strengthening is false. Let `delta=1/100` and take the planar
thin cross

\[
K=([-1,1]\times[-\delta,\delta])
\cup([-\delta,\delta]\times[-1,1]).
\]

For `n=3` and the diagonal block hyperplane,

\[
\frac{|K^3\cap H_{\rm diag}|}{|K|^2}
=\frac{547083}{633616}\approx0.86343<1.
\]

The calculation is exact: inclusion-exclusion reduces the section volume to
27 products of elementary one-dimensional interval-convolution areas.

## Scope

This is a complete counterexample to the explicit star-body strengthening in
Question 12. The body is not convex. The convex-body and `L_p`, `p>2`, parts
remain open in the checked scope.

## Files

- `solution_packet.pdf`: proof and source evidence.
- `main.tex`: packet source.
- `source_paper.pdf`: original paper.
- `figures/open_problem_crop.png`: Question 12 crop from PDF page 13.
- `figures/thin_cross_and_ratio.png`: construction and exact ratio curve.
- `code/verify_star_counterexample.py`: exact rational verifier and figure.
- `verification.md`: analytic, computational, novelty, and visual audit.

