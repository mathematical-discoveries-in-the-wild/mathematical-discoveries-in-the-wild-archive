# Verification Report

Status: passed internal adversarial audit; independent human review requested.

## Claim audited

NSS and quantitative Jamison separation transfer from a difference sequence
`M` to any exponent sequence `Q` containing pairs whose positive differences
are all terms of `M`.  The explicit sequence
`Q={1} union {A_j,A_j+2^j}`, `A_j=2^(2^(j+1))`, is Jamison, has unbounded
consecutive quotients, and is NSS for both classes in source Problems 2.6 and
2.8.

## Checks

1. **Neighborhood orientation.**  If `V` witnesses that `M` is NSS, continuity
   of `(u,v) -> u^{-1}v` at `(e,e)` gives an identity neighborhood `U` with
   `U^{-1}U subset V`.  If `x^{a_j},x^{b_j} in U` and `a_j>b_j`, then
   `x^{m_j}=x^{a_j-b_j}=(x^{b_j})^{-1}x^{a_j} in V`.

2. **No commutativity assumption on the group.**  The two factors are powers
   of the same element, so the displayed exponent identity holds in every
   group.

3. **Quantitative Jamison estimate.**  For `lambda` on the unit circle,
   `|lambda^{m_j}-1|=|lambda^{a_j}-lambda^{b_j}|` and hence is at most the sum
   of the two selected-power deviations.  For every `eta<epsilon`, some term
   of `M` has deviation greater than `eta`; the selected-power supremum is
   therefore at least `eta/2`.  Letting `eta` increase to `epsilon` handles
   the possibility that the supremum defining a Jamison pair is not attained.

4. **Indexing of the example.**  With `A_j=2^(2^(j+1))`, the increasing
   enumeration is
   `1,4,5,16,18,256,260,...`.  Each pair difference is exactly `2^j`, including
   `2^0=1`.

5. **Unbounded quotients.**  `A_{j+1}=A_j^2`, and `2^j<=A_j`, so
   `A_{j+1}/(A_j+2^j) >= A_j/2 -> infinity`.  These are consecutive terms of
   the increasing enumeration.

6. **Jamison constant.**  The source records that `(2^j)` has Jamison constant
   `sqrt(3)`.  For every `eta<sqrt(3)`, an index `j` has
   `|lambda^{2^j}-1|>eta`; the triangle inequality forces one selected
   deviation to exceed `eta/2`.  Passing to the supremum and then letting
   `eta` increase to `sqrt(3)` gives the stated bound.

7. **Application of the source theorem.**  `(2^j)` has consecutive quotient
   two.  Source Theorem 2.9 therefore makes it NSS for every Banach--Lie group
   and every group with a minimal metric.  The transfer lemma gives the same
   conclusion for `Q`.

## Failure modes checked

- The proof does not claim that `Q` itself has bounded quotients.
- The proof does not assume a metric, linearity, or local compactness in the
  abstract transfer lemma.
- The result is a strict extension of the source's sufficient family, not a
  complete answer to either problem.

## Recommended human focus

Verify that source Theorem 2.9 applies to the exact indexing `(2^j)_{j>=0}`
and that the increasing enumeration has no omitted terms between
`A_j+2^j` and `A_{j+1}`.  The remaining proof is the identity-neighborhood
calculation in Check 1.
