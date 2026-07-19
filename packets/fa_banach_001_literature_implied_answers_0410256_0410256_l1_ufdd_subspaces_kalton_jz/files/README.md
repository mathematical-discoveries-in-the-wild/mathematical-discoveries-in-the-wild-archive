# Literature-Implied Partial Subcase: UFDD Subspaces of `ell_1`

Status: `literature_implied_answer (partial subcase)`

Run: `fa_banach_001`

Source/open-problem paper: arXiv:math/0410256, Jesus M. F. Castillo and
Yolanda Moreno, "Extensions by spaces of continuous functions."

Supporting paper: arXiv:math/9911144, N. J. Kalton, "On subspaces of `c_0`
and extension of operators into `C(K)`-spaces."

## Target

Section 4, item 6 of arXiv:math/0410256 asks:

`Is Ext(M,C[0,1])=0 for every subspace M of ell_1?`

The same source also asks whether `Ext(X,c_0)=0` is equivalent to the existence
of a scalar metric projection on `Z(X,R)` that is `w*`-continuous at zero.

## Result Recorded

For the UFDD branch of the `ell_1`-subspace question, the answer is yes:

If `M` is a closed subspace of `ell_1` and `M` has an unconditional
finite-dimensional decomposition, then

`Ext(M,C(K))=0`

for every compact Hausdorff space `K`. In particular,
`Ext(M,C[0,1])=0`.

By Castillo--Moreno's Theorem 3, this also gives a fully `w*`-continuous
metric projection for such `M`, which is stronger than continuity at zero.

## Identification

Kalton proves that every separable Banach space with a UFDD and the very strong
Schur property is isomorphic to the dual of a subspace of `c_0`
(Theorem 5.3 in the arXiv PDF). A closed subspace of `ell_1` inherits the
strong Schur property from `ell_1`; and Kalton records that, for closed
subspaces of `L_1`, the strong Schur property is equivalent to the very strong
Schur property. Therefore a UFDD subspace `M` of `ell_1` is isomorphic to the
dual of a subspace of `c_0`.

Johnson--Zippin's theorem, as recalled in both Castillo--Moreno and Kalton,
says that spaces isomorphic to duals of subspaces of `c_0` have
`Ext(X,C(K))=0` for every compact `K`. Applying this to `M` gives the stated
positive subcase.

## Evidence Locations

- `source_paper.pdf`: arXiv:math/0410256. The source question is on PDF page 7,
  Section 4, item 6.
- `supporting_paper_9911144.pdf`: arXiv:math/9911144.
  - PDF page 12: Kalton notes the equivalence of strong and very strong Schur
    for closed subspaces of `L_1`.
  - PDF page 17: Theorem 5.3 states that separable UFDD spaces with the very
    strong Schur property are duals of subspaces of `c_0`.
  - PDF page 1 and Theorem 5.2 recall the Johnson--Zippin weak-star-closed
    extension framework.

## Search Notes

The cheap run indexes had no durable packet for arXiv:math/0410256, only a
prior failed attempt on the metric-projection-at-zero question. Local source
searches and web searches on 2026-06-19 for the exact metric projection
phrases, `Ext(M,C[0,1])`, subspaces of `ell_1`, Johnson--Zippin, and Kalton's
extension theorem did not find a later full solution of the arbitrary
subspace-of-`ell_1` question.

The supporting relation is agent-identified: Kalton does not present Theorem
5.3 as an explicit answer to the final question in arXiv:math/0410256, but the
implication is direct once `M` is assumed to be a UFDD subspace of `ell_1`.

## Limitations

This packet does not solve the arbitrary subspace case. The hard remaining
case is a closed subspace of `ell_1` without UFDD/unconditional structure. It
also does not solve the broad metric-projection-at-zero equivalence for all
spaces with `Ext(X,c_0)=0`, or the separable-space question.

## Human Review Notes

Recommended checks:

- Verify the hereditary strong Schur step for closed subspaces of `ell_1`.
- Verify that Kalton's "strong Schur iff very strong Schur" observation applies
  to closed subspaces of `ell_1`.
- Verify that the source's recalled Johnson--Zippin theorem is being used only
  after Kalton identifies `M` as a dual of a subspace of `c_0`.
