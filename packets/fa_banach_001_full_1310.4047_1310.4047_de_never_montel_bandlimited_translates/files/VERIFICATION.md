# Verification report

## Verdict

**Likely valid full solution**, pending human review.

The result is a full negative answer to Remark 6 of arXiv:1310.4047: for every
translation-invariant Banach space of tempered distributions `E` satisfying
the source hypotheses, `D_E` is not Montel.

## Proof audit

1. **Band-limited vector.** Choose nonzero `hat(phi) in C_c^infty`. Then
   `phi in S subset E`.
2. **Derivative factorization.** If `chi = 1` on `supp hat(phi)`, set
   `hat(u_alpha) = chi (i xi)^alpha`. This gives
   `partial^alpha phi = u_alpha * phi`, with `u_alpha in S`.
3. **Weighted integrability.** The source proves
   `omega(x) <= M(1+|x|)^tau`, so every `u_alpha in S` belongs to
   `L^1_omega`.
4. **Uniform seminorm bounds.** Translation commutes with convolution, and
   the source module estimate gives
   `||partial^alpha T_x phi||_E <= ||u_alpha||_(1,omega)||T_x phi||_E`.
   Dividing by `||T_x phi||_E` controls every derivative of `g_x` uniformly.
5. **Denominator audit.** With the source convention
   `omega(x)=||T_{-x}||`, the identity `T_{-x}T_x phi=phi` gives
   `1/||T_x phi||_E <= omega(x)/||phi||_E`. The sign is correct.
6. **Distributional limit.** For every `psi in S`, the correlation
   `x -> <T_x phi,psi>` is Schwartz. Multiplication by the polynomial upper
   bound for `1/||T_x phi||_E` still tends to zero. Thus `g_x -> 0` weakly in
   `S'` as `|x| -> infinity`.
7. **Montel contradiction.** `D_E` is Fréchet. If it were Montel, a bounded
   sequence `g_(x_j)`, `|x_j| -> infinity`, would have a convergent
   subsequence. The continuous map `D_E -> S'` forces the limit to be zero,
   contradicting `||g_(x_j)||_E=1`.

No computational experiment is used as mathematical evidence.

## Source checks

- arXiv:1310.4047, Definition 1: `omega(x)=||T_{-x}||`.
- arXiv:1310.4047, Lemma 1 / Proposition 1: the `L^1_omega` convolution-module
  estimate.
- arXiv:1310.4047, Proposition 7: `D_E` is Fréchet and embeds continuously in
  `E` and `S'`.
- arXiv:1310.4047, page 17, Remark 6: the exact Montel question.
- arXiv:1901.10041, Problem 5.8 and Theorem 5.9: non-Montelness for solid
  TIBDs, together with the explicit statement that the general case was not
  proved there.

## Novelty search

Bounded search date: **22 July 2026**.

Searched arXiv and general web indexes using:

- exact phrases `Can D_E be Montel`, `D_E is never Montel`, and the later
  paper's sentence about general TIBDs;
- arXiv ids `1310.4047` and `1901.10041`;
- both paper titles, the relevant authors, `Problem 5.8`, `general TIBD`,
  `solid TIBD`, and `translation-invariant Banach space of distributions
  Montel`.

The search recovered Debrouwere's 2019 solid-space theorem but no later
general theorem. This supports **moderate-to-high novelty confidence**. It is
not an exhaustive MathSciNet/zbMATH/citation-graph review.

## Scope and reviewer focus

- The result answers only the Montel question. It does not settle the separate
  barreledness question for the strong dual.
- Primary review focus: the Fourier multiplier identity, the source's
  translation-sign convention, and the standard sequential compactness step
  in a metrizable Montel space.
- Recommendation: **verify and circulate**.
