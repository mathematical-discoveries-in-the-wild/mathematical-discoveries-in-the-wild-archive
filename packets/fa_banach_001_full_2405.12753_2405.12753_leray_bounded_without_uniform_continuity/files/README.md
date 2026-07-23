# Full candidate: uniform continuity is unnecessary for Leray boundedness

Status: `candidate_full_solution_likely_valid` (awaiting human review).

For the convex Reinhardt domains \(\Omega\in\widetilde{\mathcal R}\) studied
in arXiv:2405.12753, this packet proves

```text
L_b is bounded on L^2(boundary Omega, mu_Omega)
if and only if
kappa_3/(kappa_1 kappa_2) is bounded above and bounded away from zero.
```

This fills the precise case isolated in Section 4.3 of the current source PDF:
the curvature ratio is bounded above and below but is not uniformly
continuous and has no endpoint limit.

The proof avoids the regular-variation asymptotics that break down in the
source.  The primal and dual monomial kernels have the same maximizer
`s = m/(m+n)`.  Bounds on the exponent function dominate both kernels by
fixed powers of the elementary beta kernel
`s^(2m)(1-s)^(2n)`.  Uniform beta-function and binomial estimates then cancel
exactly in the source rank-one norm formula.

Files:

- `solution_packet.pdf`: review-ready full proof.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2405.12753.
- `figures/open_problem_crop.png`: the exact Section 4.3 omitted case.
- `figures/rank_one_criterion_crop.png`: the source rank-one norm criterion.
- `code/verify_beta_kernel_bounds.py`: bounded numerical sanity checks.
- `code/crop_source_pages.py`: reproducible source-evidence crops.
- `verification_report.md`: explicit proof and artifact checks.

Primary verifier focus: check the two one-line logarithmic comparison
inequalities on both sides of `s=m/(m+n)`, and the uniform Stirling estimate
for `J_c(m,n)` when one index is zero.

