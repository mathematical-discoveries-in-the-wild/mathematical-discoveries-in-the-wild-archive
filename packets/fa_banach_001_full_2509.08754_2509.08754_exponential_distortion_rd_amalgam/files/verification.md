# Verification Report

Candidate: arXiv:2509.08754, final high-distortion amalgam question

## Verdict

`likely valid`

Confidence: 98/100 for the mathematical construction. Residual uncertainty is
interpretive: whether the source intended an unstated restriction to word
lengths in this final question.

## Claim checked

There is an explicit nondegenerate amalgamated free product whose two vertex
groups have RD, whose universal length has RD, and for which a vertex length is
exponentially distorted relative to the restricted universal length.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Weighted formulas are length functions | valid | They are weighted word lengths on the Boolean group; symmetric difference can only cancel weights. Adding the `0/1` cyclic length preserves subadditivity. |
| Amalgam identification | valid | `A` is central in both factors, so the amalgam presentation is exactly that of `A x (C_2*C_3)`. |
| Nondegeneracy | valid | `A` has indices two and three in the respective vertex groups, hence is proper in both. |
| Universal-length upper bound | valid | Represent the `A` coordinate in the lighter `H` factor, then spell the reduced `C_2*C_3` word. |
| Universal-length lower bound | valid | Every factor cost dominates its `ell_0` contribution plus the length of its finite-cyclic projection. Summing and using both triangle inequalities gives `ell_0(a)+|q|`. |
| Polynomial decay for weighted `A` | valid | Binary expansion is a bijection from `A` to the nonnegative integers under `ell_0`, so the radius-`R` ball has exactly `R+1` elements. Cauchy-Schwarz yields decay `sqrt(R+1)`. |
| Vertex groups have RD | valid | `ell_1>=ell_0`, so its balls are smaller; adjoining a finite cyclic factor changes ball counts only by a fixed factor. |
| The amalgam has RD | valid | `C_2*C_3` has polynomial decay by the source's free-product Lemma 2.12. Lemma 2.11 multiplies the polynomial decay functions for the direct product with `(A,ell_0)`. |
| Exponential lower distortion | valid | The binary element of `ell_0`-length `r` has a leading digit `2^N>r/2`, contributing `2^(2^N)>2^(r/2)` to `ell_1`. |
| Exponential upper distortion | valid | If the leading digit is `2^N<=r`, the superincreasing weights sum to at most `2*2^(2^N)<=2^(r+1)`. |

## Adversarial checks

- The proof establishes equality for the universal length, not merely a
  quasi-isometry estimate.
- A factor element may contain both an `A` coordinate and a cyclic coordinate.
  Its cost still dominates the sum of the two lighter projected costs, so
  bundling coordinates cannot shorten the universal length.
- Cancellation in `A` only lowers `ell_0` of the total coordinate, exactly the
  direction needed for the lower bound.
- Cancellation in `C_2*C_3` only lowers reduced word length, again in the
  needed direction.
- The exponential comparison holds at every integer radius, not only on a
  sparse subsequence, because every integer has a binary expansion.
- The source's direct-product and free-product lemmas are stated for SD, but
  their displayed decay functions remain polynomial when the input functions
  are polynomial. Thus they prove RD in this specialization.
- No claim is made for finitely generated vertex groups or word lengths. The
  countable weighted-length setting is explicit in both the source and packet.
- The construction is not a degenerate identity amalgam: both vertex groups
  strictly contain `A`.

## Deterministic audit

Command:

```text
conda run --no-capture-output -n sandbox python code/check_weighted_amalgam.py
```

The checker verifies weighted-length subadditivity, exact binary ball counts,
the exponential distortion estimates, and the universal-length formula by a
finite Dijkstra search over truncated Boolean coordinates and reduced
`C_2*C_3` words. It audits the finite combinatorics; the written proof handles
the infinite group.

## Literature check

The cheap run indexes were searched by arXiv id, title, rapid decay, high
distortion and amalgamated free product. A bounded primary arXiv search using
the exact source and those terms found no later answer and no copy of the
weighted Boolean construction. Novelty remains subject to expert review.

## Human review recommendation

`send to human`

Ask a geometric group theorist to check the universal-length computation and
confirm that the source's final question is intended in its stated generality,
rather than only for finitely generated groups with word lengths.
