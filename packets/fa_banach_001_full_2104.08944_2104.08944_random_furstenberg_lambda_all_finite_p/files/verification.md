# Verification report

Candidate: arXiv:2104.08944, random-Furstenberg `Lambda(q)` question

## Claim checked

For independent selectors with `P(n in T)=log(n)/n`, the random set `T` is
almost surely a `Lambda(q)`-set for every finite `q>2`, simultaneously.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Comparable pair in a relation | valid | If `M` is the largest entry of a fixed integer relation, the triangle inequality forces another entry to be at least a coefficient-dependent multiple of `M`. |
| Expected fixed-core count | valid | Fixing the maximum and all but the comparable entry determines the latter. The bound is `O((log M)^(2r-2)/M^2)`, which is summable. |
| Use of independence | valid | Core entries are required to be distinct, so the membership expectation is the product of selector means. Repetitions are handled only after reduction. |
| Almost-sure simultaneous event | valid | Each relation type has finite count almost surely; integer coefficient vectors form a countable family. |
| Moment reduction | valid | Equal multiplicities on the two sides are canceled. For fixed `m`, only finitely many signed coefficient patterns remain, and every surviving core has finitely many realizations. |
| Diagonal padding | valid | Arbitrary common multiplicities are allowed. An ordered list of `m-s` common entries contributes exactly a factor bounded by `||a||_2^(2m-2s)`; slot permutations cost at most `(m!)^2`. |
| Core coefficient bound | valid | The core monomial has total degree `2s` and each coefficient is at most `||a||_2`, so it is at most `||a||_2^(2s)`. |
| Passage to all finite exponents | valid | `Lambda(2m)` for all integers `m>=2`, plus `||f||_q<=||f||_(2m)` on normalized Haar measure, covers every finite `q>2`. |

## Counterexample search

The two main failure modes were checked directly in the proof:

1. Full moment relations need not be finite because a fixed nontrivial core can
   be padded by arbitrary common entries. The proof does not use such a false
   finiteness claim; it sums the padding by the `ell^2` norm.
2. Repeated indices invalidate a naive product-of-probabilities calculation.
   The proof first compresses to distinct support values and uses independence
   only for that injective support.

No computational experiment is an ingredient of the proof.

## External dependencies

- The source paper supplies the definition of `T` and the open question.
- The proof otherwise uses only independence, Tonelli's theorem for a
  nonnegative count, Fourier orthogonality, and monotonicity of `L^p` norms on
  the probability space `Torus`.
- The 2023 follow-up is used only for literature status, not for the proof.

## Novelty bounds

Local run indexes and bounded web/arXiv searches were checked on 2026-07-19.
The latest directly relevant source found was the authors' 2023 follow-up,
which still states that the whole-set `Lambda(q)` property is unknown. No later
resolution was found. The search was bounded and is not an exhaustive
bibliographic guarantee.

## Human review recommendation

Send to a harmonic analyst. The highest-value review is to audit the
coefficient-dependent comparable-entry bound in Lemma 1 and the combinatorial
overcount by an ordered diagonal list in the even-moment proof.
