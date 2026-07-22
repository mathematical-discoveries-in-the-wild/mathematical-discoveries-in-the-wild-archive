# Verification report

## Claim checked

For coordinatewise injective `Phi:[4]x[4]->L`, the SAP-lunar equivalence holds
when `|im Phi|<=5`, and every map with `|im Phi|>=14` is lunar.

## Verdict

Likely valid partial result. Confidence: 92/100.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Coordinatewise injective maps are proper colorings | valid | A color class is exactly a matching in `K_4,4`. |
| Restricted-growth enumeration is complete | valid | Each unlabeled color partition has a unique first-occurrence labeling; every compatible old color and the next new color are explored. |
| Four-color census | valid | 24 canonical tables, all lunar. |
| Five-color census | valid | 4,896 canonical tables; 144 lunar and 4,752 non-lunar. |
| Orbit quotient | valid after repair | 17 classes total, one lunar. An earlier non-contiguous-array relabeling bug was found, fixed, and all counts were recomputed. |
| Norm certificates | valid | All 16 non-lunar classes have integer scalar coefficients bounded by 3. |
| Exact norm comparison | valid | Exact characteristic polynomials and Sturm root counts put the top eigenvalues of `A^T A` and `B^T B` on opposite sides of a rational threshold. |
| High-color obstruction | valid | Three distinct equality edges have equivalence-rank at least three, so non-lunar maps use at most 13 colors. |

## Counterexample search

Exploratory scalar and matrix-valued searches were performed before the exact
classification. No counterexample to the promoted boundary theorem was found.
The exact verifier supersedes those numerical searches.

## External dependencies

- NumPy is used for candidate filtering only.
- SymPy exact integer characteristic polynomials and Sturm counts are the
  acceptance gate.
- The source theorem lunar implies SAP is cited from arXiv:2407.01048v1.

## Remaining gaps

- This result leaves color counts 6 through 13 open.
- Novelty should be checked with the authors because a 2024 talk announcement
  mentions unspecified progress without a public theorem statement.

## Human review recommendation

Send to human review, with emphasis on auditing the finite enumeration and the
three-edge argument for the 14-color cutoff.

