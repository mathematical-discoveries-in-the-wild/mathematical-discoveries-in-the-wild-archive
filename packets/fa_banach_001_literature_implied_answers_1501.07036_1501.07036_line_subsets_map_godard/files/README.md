# Literature-Implied Partial Subcase: Subsets of the Real Line

Status: `literature_implied_answer (partial subcase)`

Run: `fa_banach_001`

Source/open-problem paper: arXiv:1501.07036, Eva Pernecka and Richard J.
Smith, "The metric approximation property and Lipschitz-free spaces over
subsets of R^N."

Supporting paper: arXiv:0904.3178, Alexandre Godard, "Tree metrics and their
Lipschitz-free spaces."

## Target

In the introduction of arXiv:1501.07036, after Corollary 1.2, Pernecka and
Smith ask whether `F(M)` has the metric approximation property for all subsets
`M subset R^N`.

## Result Recorded

The one-dimensional subcase is already answered by Godard's computation:

If `M` is any subset of the real line, with the inherited Euclidean metric,
then the Lipschitz-free space `F(M)` has the metric approximation property.

More generally, if `A` is a subset of an `R`-tree `T` and `Br(T) subset
closure(A)`, then Godard identifies `F(A)` isometrically with `L_1(mu_closure(A))`;
hence `F(A)` has the MAP.

## Identification

Godard's Theorem 3.2 states that if `T` is an `R`-tree and `A subset T` contains
the branching points of `T` in its closure, then `F(A)` is isometric to
`L_1(mu_closure(A))` for an explicit measure `mu_closure(A)`. For `T=R`, there
are no branching points, so the hypothesis is automatic for every subset
`M subset R`. Thus `F(M)` is isometric to an `L_1` space.

Every `L_1` space has the metric approximation property: finite measurable
partitions give norm-one conditional expectations with finite-dimensional
ranges, directed by refinement, and these converge strongly to the identity.
Therefore Godard's theorem gives the MAP for all subsets of the real line.

The supporting relation is agent-identified. Godard's paper predates
arXiv:1501.07036 and does not present the result as an answer to the later
Pernecka-Smith question, but the implication is direct after the
one-dimensional reformulation.

## Evidence Locations

- `source_paper.pdf`: arXiv:1501.07036. The source question appears on PDF
  page 4, immediately after Corollary 1.2: the authors say they do not know
  whether `F(M)` has the MAP for all subsets `M subset R^N`.
- `supporting_paper_0904.3178.pdf`: arXiv:0904.3178.
  - PDF page 1: abstract says the paper computes Lipschitz-free spaces of
    subsets of the real line.
  - PDF pages 4-5: Theorem 3.2 identifies `F(A)` with `L_1(mu_closure(A))`
    for tree subsets with branching points in the closure.
  - PDF page 5: the text after Corollary 3.4 says the result computes the
    Lipschitz-free space of any subset of `R`.

## Search Notes

Cheap run indexes were searched for `1501.07036`, "Metric Approximation
Property", "Lipschitz-Free Spaces", "Pernecka", "Smith", "Godard", "subsets of
R", and "MAP". No existing durable packet for this target was found; only the
prior no-promotion attempt
`runs/fa_banach_001/attempts/1501.07036_finite_dimensional_subset_map_attack.md`
was present.

Web searches on 2026-06-19 for `"Lipschitz-free" "subset of R" "metric
approximation property"`, `"1501.07036" "MAP" "subsets"`, and Godard tree-metric
phrases found the source paper, the 2022 manifold extension, and Godard's
arXiv:0904.3178 paper. No later full solution of the arbitrary
finite-dimensional `N >= 2` question was found in this bounded pass.

## Limitations

This packet does not solve the full question for arbitrary subsets of
`R^N` when `N >= 2`. It records the complete one-dimensional subcase, and the
same argument covers tree-metric subsets satisfying Godard's branching-closure
hypothesis. The higher-dimensional Euclidean endpoint, including arbitrary
closed or compact subsets of `R^N`, remains open here.

## Human Review Notes

Recommended checks:

- Verify that the source question is interpreted with the inherited metric from
  `R^N`, so the `N=1` case is exactly the inherited metric on a subset of `R`.
- Verify that Godard's Theorem 3.2 applies to arbitrary, not necessarily closed,
  subsets through passage to the closure, as stated in the proof.
- Verify the standard MAP argument for arbitrary `L_1(mu)` spaces via finite
  partition conditional expectations.
