# Adversarial verification report

Status: passed symbolic audit; candidate full solution, likely valid.

## Claim-to-source match

- The source asks on PDF page 49 whether `||Phi||_{q->p}` equals its
  positive-input restriction for CP maps when `0<p,q<1`.
- The theorem proved in this packet is exactly that equality and allows all
  `0<p,q<=infinity`.
- The source separately asks about completely bounded mixed two-indexed
  quasi-norms. The packet explicitly does not claim to solve that question.

## Proof audit

1. **Canonical block positivity.** For `X=U|X|`, direct multiplication of
   `[U;I]|X|[U*,I]` gives diagonal blocks `|X*|, |X|` and off-diagonal blocks
   `X, X*`. Partial, rather than unitary, polar isometries cause no problem.

2. **Use of positivity.** Two-positivity, not merely positivity, is exactly
   what is needed to apply `id_2 tensor Phi` to the block matrix. CP implies
   two-positivity.

3. **Singular diagonal blocks.** The contraction factorization is not based
   on an invalid inverse. It is obtained from
   `(A+eps I)^(-1/2) B (D+eps I)^(-1/2)` and a finite-dimensional convergent
   subsequence, so it also covers singular `A,D`.

4. **Quasi-norm range.** No triangle inequality, convex duality, or
   Minkowski inequality is used. The only analytic inequality is generalized
   Schatten Holder
   `||YZ||_r <= ||Y||_s ||Z||_t`, `1/r=1/s+1/t`, which the source states for
   all positive exponents (Lemma 2.1). Taking `(r,s,t)=(p,2p,2p)` is valid
   even for `p<1`.

5. **Contraction insertion.** Ideal monotonicity gives
   `||K D^(1/2)||_{2p} <= ||K||_infinity ||D^(1/2)||_{2p}` for every
   `p>0`. This is another instance of generalized Holder with an infinity
   exponent.

6. **Denominators.** `X`, `|X|`, and `|X*|` have identical singular values,
   so their Schatten `q` quasi-norms agree for every positive `q`, including
   `q=infinity`.

7. **Endpoint and attainment.** The same factorization gives the operator
   norm estimate at `p=infinity`. Finite-dimensional Schatten unit spheres
   are compact and the objective is continuous, so both suprema are maxima.

## Failed overextensions deliberately excluded

- The proof does not automatically compare the source's mixed two-indexed
  input/output quasi-norms after ancilla amplification. No completely
  bounded claim is made.
- Infinite-dimensional compactness and approximation issues are not treated.
- The interpolation and multiplicativity questions on the same source page
  are untouched.

## Literature boundary

The source cites Watrous (2004) for the norm range and explicitly calls the
quasi-norm range open. Exact and keyword searches in the run indexes, plus a
bounded primary-source arXiv search, found no later paper stating the
all-positive-exponent extension or this proof. This is evidence for novelty,
not a certification.
