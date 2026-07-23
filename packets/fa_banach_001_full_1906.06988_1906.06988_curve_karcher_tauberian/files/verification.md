# Verification report

Verdict: `likely_valid_candidate_full`

## Claim-by-claim audit

1. **Existence of the mean.** On each compact time interval, a continuous
   curve has bounded image. The averaged squared-distance functional is
   strongly convex on a complete CAT(0) space, so it has a unique minimizer.

2. **Barycenter inequality.** For `D=d(sigma_T,z)`, strong convexity and
   minimality give

   ```text
   D^2 <= G_T(z)-G_T(sigma_T).
   ```

   The triangle inequality gives pointwise

   ```text
   d(c(t),z)^2-d(c(t),sigma_T)^2
   <= 2 D d(c(t),z)-D^2.
   ```

   Integration and combination yield `D<=average d(c(t),z)` when `D>0`;
   the case `D=0` is immediate. No linear structure or differentiability of
   the Hadamard space is used.

3. **Upper-gradient step.** Local absolute continuity supplies
   `d(c(t),c(T))<=integral_t^T g`. Tonelli's theorem gives

   ```text
   integral_0^T integral_t^T g(s) ds dt
   = integral_0^T s g(s) ds.
   ```

   This proves the advertised quantitative estimate.

4. **Pointwise corollary.** If `t g(t)->0` (or has essential limit zero),
   split the Cesaro integral at a fixed large time. The initial part divided
   by `T` vanishes, while the tail is bounded by the chosen epsilon.

5. **Unit-lag counterexample.** In `R`, the Karcher mean is the arithmetic
   integral mean. For `c(t)=sin(2 pi t)`,

   ```text
   sigma_T=(1-cos(2 pi T))/(2 pi T) -> 0,
   c(t)-c(t-1)=0.
   ```

   Yet the values at `n+1/4` and `n+3/4` are `1` and `-1`, so `c` has no
   limit.

## Edge cases checked

- Division by `D` is isolated from the trivial case `D=0`.
- Only local integrability of `g` is needed for each finite `T`.
- No boundedness of the full curve is assumed.
- The counterexample is smooth, so adding mere continuity, local absolute
  continuity, boundedness, or uniform continuity does not rescue unit lag.

No computational dependency remains.
