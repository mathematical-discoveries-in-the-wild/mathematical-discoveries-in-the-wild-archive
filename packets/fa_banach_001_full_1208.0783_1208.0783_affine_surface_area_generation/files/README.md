# Full solution packet: p-affine surface areas generate curvature integrals

Status: `candidate_full_solution_likely_valid` (full positive answer to the
precise integral-generation conjecture on p. 12 of arXiv:1208.0783, pending
human review).

Source: Alina Stancu, *Some Affine Invariants Revisited*, arXiv:1208.0783,
Section 3, p. 12 of the arXiv PDF.

## Result

For a `C^2_+` convex body `K` containing the origin, let `kappa_0` be its
positive centro-affine curvature and `mu_K` its cone measure. The source uses

\[
\Omega_p(K)=\int_{\partial K}
\kappa_0^{p/(n+p)}\,d\mu_K,\qquad p\ne-n.
\]

For every continuous `phi:(0,infinity)->R`, there is a sequence of finite
linear combinations of p-affine surface areas, with coefficients independent
of `K`, converging to

\[
I_\phi(K)=\int_{\partial K}\phi(\kappa_0)\,d\mu_K
\]

for every such body `K`. The convergence is uniform on every family with
`a <= kappa_0 <= b` and bounded volume. After normalization by
`Omega_0(K)=n Vol(K)`, the volume bound is unnecessary.

Only the countable parameters

\[
p_0=0,\qquad p_k=-\frac{2kn}{2k-1}\quad(k\ge1)
\]

are needed. Thus the result lies in the closure of the linear span of the
p-affine surface areas, a stronger conclusion than generation by their full
algebra.

## Proof mechanism

The chosen parameter satisfies `p_k/(n+p_k)=2k`, so `Omega_(p_k)` is the
`2k`-th moment of `kappa_0` under cone measure. Given `phi`, approximate
`psi(y)=phi(sqrt(y))` locally uniformly on `(0,infinity)` by ordinary
polynomials `Q_m(y)`. Then

\[
\int Q_m(\kappa_0^2)\,d\mu_K
\]

is a finite linear combination of the `Omega_(p_k)` and converges to
`I_phi(K)`. Positivity and continuity of `kappa_0` make its range compact for
each fixed body.

## Packet contents

- `main.tex`, `solution_packet.pdf`: self-contained theorem and proof.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: full-width crop of the source conjecture.
- `code/make_open_problem_crop.py`: reproducible crop script.
- `code/verify_parameter_map.py`: exact rational-arithmetic check of the
  parameter/exponent identity.
- `verification_report.md`: proof audit, novelty bounds, and reviewer focus.

## Novelty and scope

The four lightweight run indexes and two bounded web-search rounds were
searched using the arXiv id, exact conjecture sentence, title/author, and close
variants involving Stone-Weierstrass approximation, moments, centro-affine
curvature, and closure of p-affine surface areas. No matching later proof was
located. Novelty confidence is moderate, not definitive.

The theorem answers the paper's precise conjecture about integrals
`integral phi(kappa_0) dmu_K`. It does not classify arbitrary `SL(n)`
invariants outside this integral class, a broader informal phrasing appearing
in the abstract.
