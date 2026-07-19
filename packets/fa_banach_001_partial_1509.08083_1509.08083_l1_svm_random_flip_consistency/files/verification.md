# Verification report

Verdict: `partial_result_likely_valid`; human review recommended.

## Mathematical checks

1. **Gaussian reduction.** For `w=u a+v`, `v perpendicular a`, multiplication
   of the orthogonal Gaussian coordinate by `sign(<g,a>)` preserves a standard
   Gaussian independent of `|<g,a>|`. Hence the signed margin is exactly
   `r(u|G|+||v||_2 Z)`.

2. **Strict Jensen step.** For `p in (1/2,1)`, the noisy hinge profile
   `phi_p(t)=p(1-t)_+ +(1-p)(1+t)_+` is convex and not affine on `R`. If
   `||v||_2>0`, the conditional Gaussian margin has full real support, so the
   Jensen inequality is strict.

3. **Derivative and scale.** For `u>0`, direct differentiation gives

   ```text
   J'(u)=r sqrt(2/pi) [1-2p+p exp(-1/(2r^2u^2))].
   ```

   This is strictly increasing from a negative to a positive limit and
   vanishes exactly at
   `u=1/(r sqrt(2 log(p/(2p-1))))`. For `u<0`, all relevant slopes are
   negative, so no second minimizer is missed.

4. **Separation modulus.** The two-dimensional risk `H(u,s)` has the unique
   minimizer `(mu,0)`. The stated parameter domain is compact and excludes a
   Euclidean ball about `(mu,0)`, hence `Delta_delta>0` by continuity.

5. **Empirical lift.** On the event `sup_K |L_m-L| <= Delta_delta/4`, empirical
   optimality gives population excess risk at most `Delta_delta/2`; therefore
   no empirical minimizer can lie at distance at least `delta` from `mu a`.
   Substituting `q=Delta_delta/8` into the source concentration theorem gives
   the displayed exponent denominators `2048`.

6. **Normalization.** If `delta<mu/2`, every accepted minimizer is nonzero and
   the standard normalization inequality gives directional error below
   `2 delta/mu`.

## Source and literature checks

- Source question: arXiv:1509.08083, Section VI, PDF page 15; local TeX lines
  1052--1061.
- Later noisy unit-ball theorem: arXiv:1804.04846, Theorem 2.10 and Corollary
  2.11, PDF pages 9--10.
- Random flips: arXiv:1804.04846, Example 3.4(2) and Proposition 3.5, PDF page
  21.
- Pure ell_1 limitation of later work: arXiv:1804.04846, beginning of Section
  2.3, where the noisy arbitrary-convex-set extension is described as not
  straightforward.
- The later paper explicitly identifies Kolleck--Vybiral as a special case in
  Remark 2.16(1), PDF page 14.

## Remaining verifier focus

- Audit the transfer of Theorem II.1 from the source to independently flipped
  labels line by line. The key absorption step is valid, but it is the only
  imported proof component.
- Check whether a post-2020 paper supplies an explicit arbitrary-convex noisy
  hinge theorem that subsumes this result.
- No computation is used as proof.
