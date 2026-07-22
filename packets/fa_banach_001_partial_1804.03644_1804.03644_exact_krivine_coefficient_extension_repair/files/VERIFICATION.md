# Verification notes

- The open conjecture was checked on physical PDF page 20 (paper page 18) of
  the source. The readable full-width crop is
  `figures/open_problem_crop.png`.
- The advertised theorem and final numerical step were checked on physical
  PDF page 22 (paper page 20). The readable crop is
  `figures/source_constant_gap_crop.png`.
- The source line
  `asinh(0.974202) >= asinh(1)/(1+0.00863)` is false: its sides are
  approximately `0.863013` and `0.873832`.
- `code/verify_exact_certificates.py` constructs the hypergeometric
  coefficients and inverse coefficients from exact rational recurrences. It
  does not use sampled parameter values or floating-point polynomial tests.
- For every required odd degree through 39 except 7, the target polynomial is
  converted to the tensor-product Bernstein basis on `[0,1]^2`; every
  Bernstein coefficient is asserted nonnegative as a SymPy rational.
- In degrees congruent to 3 modulo 4, the verifier first removes the
  nonnegative edge factor `(1-a)(1-b)`. Degree 7 is deliberately deferred to
  the exact analytic factorization in the packet.
- The degree-7 proof was checked in the two feasible regimes
  `a+b <= 11/100` and `a+b >= 11/100`. In the second regime, the polynomial is
  decreasing in `ab`, so the minimum occurs at `a=b`; the resulting quartic
  is an explicit square plus positive terms.
- The tail uses the source estimate `|d_k| <= 6.1831/k` and only odd powers,
  giving exactly
  `E=(6.1831/41)*delta^41/(1-delta^2)` at `delta=439/500`.
- The robust defect step was checked with an upper bound `E`, not with an
  assumed equality for the unknown tail: the residual term is
  `2(h_err(41,rho)-E) <= 0` because `rho <= delta` and
  `h_err(41,delta) <= E`.
- The inequalities `0.874 <= asinh(1-2E) <= 0.878` and
  `asinh(1) <= 0.874*1.0085` are reduced to exact rational lower and upper
  Taylor bounds for `sinh` with a geometric remainder bound.
- The exact verifier was run in the repository's `sandbox` environment and
  ended with `ALL EXACT CERTIFICATES PASSED`.
- The final PDF was compiled with intermediates under `tmp/`; every rendered
  page was visually inspected.

Highest-value human audit: rerun the exact verifier, check the degree-7
factorization, and compare equations (4.1)--(4.4) with Lemmas 4.1 and 4.7 of
the source.
