# Verification report

Verdict: `likely valid candidate partial`.

## Logical audit

1. A non-absolutely-continuous Radon measure on `R` has a nonzero singular
   part.  Inner regularity supplies a compact null set `K` with
   `0 < mu(K) < infinity`.
2. Simultaneous outer regularity for Lebesgue measure and `mu` gives bounded
   open neighborhoods `U_n` of `K` with both `|U_n| -> 0` and
   `mu(U_n \ K) -> 0`.
3. Smooth Urysohn cutoffs `g_n` satisfy `g_n=1` on `K`,
   `0 <= g_n <= 1`, and `supp(g_n) subset U_n`.  Their first `m` Lebesgue
   moments tend to zero.
4. Fixed smooth bumps away from `K` can be chosen with an invertible
   `m`-by-`m` moment matrix (approximate point masses at distinct points, so
   the matrix is a perturbation of a Vandermonde matrix).  The correction
   coefficients therefore tend to zero.
5. The corrected functions `h_n` have moments zero through order `m-1` and
   `||h_n||_{L^1(dx)} -> 0`.
6. The `m`-fold primitive has derivative `u_n^(m)=h_n`.  To the right of the
   common support, the binomial expansion involves only the vanished moments;
   to the left it is zero by definition.  Hence `u_n` is smooth and compactly
   supported.
7. Every derivative below order `m` is bounded uniformly by a constant times
   `||h_n||_1`, hence converges uniformly to zero.  Common compact support and
   local finiteness of `mu` give `u_n -> 0` in all input `L^p(mu)`, including
   `p=infinity`.
8. The cutoff error is supported in `U_n \ K`, while the fixed bump
   corrections have coefficients tending to zero.  Thus
   `h_n -> 1_K` strongly in every finite `L^q(mu)`.
9. The lower-order terms in `P(D)u_n` converge to zero in `L^q(mu)`, while
   the leading term converges to `a_m 1_K`, which is nonzero because
   `a_m != 0` and `mu(K)>0`.  This is exactly a failure of sequential
   closability at zero.

## Edge cases checked

- The argument works for infinite Radon measures because every function in
  the construction has support in one fixed compact set of finite `mu`-mass.
- It works for input exponent `p=infinity` because convergence is uniform.
- It deliberately excludes output exponent `q=infinity`; shrinking
  `mu`-measure of an error set does not imply convergence in essential
  supremum.
- For the source Laplacian, the witnesses lie in `C_c^infinity(R)`, hence also
  in the stated domain `C_c^2(R)`.
- The theorem is only a necessary condition.  No converse is asserted.

## Human-review focus

The highest-value independent check is the moment-cancellation step: verify
that vanishing moments `0,...,m-1` make the one-sided `m`-fold primitive and
all of its lower derivatives vanish identically beyond the right edge of the
support.

