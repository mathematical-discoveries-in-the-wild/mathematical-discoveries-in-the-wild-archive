# Verification report

Packet: `1208.0783_affine_surface_area_generation`

Date: 2026-07-22

Verdict: `candidate_full_solution_likely_valid`, suitable for human review.

## Analytic proof audit

1. **Source identity.** On `C^2_+` bodies with the origin in the interior,
   the source formula is
   `Omega_p=integral kappa_0^(p/(n+p)) dmu_K` for `p != -n`.
2. **Allowed parameter sequence.** For
   `p_k=-2kn/(2k-1)`, one has `p_k<-n`, so the singular parameter `-n` is
   avoided, and exact algebra gives `p_k/(n+p_k)=2k`.
3. **Polynomial realization.** If
   `Q(y)=sum c_k y^k`, then
   `integral Q(kappa_0^2)dmu_K=sum c_k Omega_(p_k)(K)`, with the constant
   term represented by `Omega_0=n Vol(K)`.
4. **Universal approximation.** For
   `psi(y)=phi(sqrt(y))`, choose `Q_m` approximating `psi` within `1/m` on
   `[m^(-2),m^2]`. These polynomials depend only on `phi`, not on `K`, and
   converge locally uniformly on `(0,infinity)`.
5. **Passage under the integral.** For each fixed body, continuous positive
   `kappa_0` has range in a compact interval `[a_K,b_K]` contained in
   `(0,infinity)`. Uniform convergence on that interval gives convergence of
   the finite cone-measure integrals. The same estimate is uniform on the
   stated curvature/volume-controlled strata.
6. **Normalized version.** Division by `Omega_0` turns cone measure into a
   probability measure, eliminating the volume factor in the error estimate.

No computational assertion closes an analytic gap.

## Exact arithmetic check

Command run from the packet directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_parameter_map.py
```

The script checked 570 pairs `(n,k)` using rational arithmetic. It verified
`p_k<-n`, `p_k!=-n`, and `p_k/(n+p_k)=2k` exactly. Result:

```text
PARAMETER DOMAIN CHECK: PASS
EXPONENT IDENTITY CHECK: PASS
tested exact parameter pairs = 570
ALL VERIFICATION CHECKS: PASS
```

## Novelty bounds

The cheap registry, solution, attempt, and proof-gap indexes were searched for
arXiv:1208.0783, the title, affine-surface-area generation, centro-affine
curvature integrals, moments, and closure. Two bounded web searches used the
exact conjecture phrase and variants with `Stone-Weierstrass`, `Omega_p`, and
`p-affine surface areas`. Results returned the source and surrounding affine
surface-area literature, but no matching resolution. This was not an
exhaustive MathSciNet/zbMATH or complete citation-graph search.

## Human-review focus

- Confirm that the source's extension of `Omega_p` includes all real
  `p != -n` on `C^2_+` bodies, in particular the sequence `p_k<-n`.
- Confirm that pointwise closure plus uniform closure on controlled strata is
  the intended rigorous interpretation of the source's unspecified word
  `closure`.
- Confirm the scope distinction between the precise integral-form conjecture
  on p. 12 and the broader informal abstract wording about arbitrary
  `SL(n)` invariants.
