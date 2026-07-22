# Verification report

Status: `partial_result_likely_valid; human_review_needed`

## Proof audit

1. Cyclicity moves the unique auxiliary-unitary occurrence in every
   witness-degree-one trace monomial to the right, giving the trace-affine
   normal form.
2. Polar decomposition gives
   `sup_V Re tau(CV)=tau(|C|)` in matrices and in a finite factor. A polar
   partial isometry extends to a unitary because its initial and final
   complements have equal trace.
3. Haar-unitary *-moment convergence and a uniform polynomial norm bound let
   one approximate the square root on a common compact interval, proving
   convergence of `tau_N |C(U^(N))|`.
4. The matrix single-conjugation supremum is the classical eigenvalue
   rearrangement pairing.
5. In a diffuse finite factor, the Fack-Kosaki/Hardy-Littlewood inequality
   gives the upper rearrangement bound. Spectral step approximations and
   unitary equivalence of finite projection families with matching trace
   vectors give the reverse bound.
6. Weak convergence of uniformly compactly supported spectral measures gives
   almost-everywhere and L1 convergence of decreasing quantile functions.
   Their pairings therefore converge.
7. All optimized quantities are uniformly bounded by a constant depending
   only on the fixed polynomial, so almost-sure convergence implies the
   expectation limit in Conjecture 1.2.

No missing implication was found in this audit.

## Numerical smoke test

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2606.02985_trace_affine_and_rearrangement_witness_sectors/code/verify_unitary_optimizers.py
```

The test constructs the polar and eigenvector-alignment optimizing unitaries
for 180 random matrix pairs of orders 2 through 10 and verifies both formulas
to tolerance `1e-10`. This checks finite-dimensional formulas only; the proof
of the asymptotic statement is analytic.

## Reviewer focus

The highest-value human checks are the diffuse-factor lower rearrangement
bound and the passage from weak spectral convergence to convergence of the
quantile pairing. The full conjecture remains open outside the two stated
witness sectors.
