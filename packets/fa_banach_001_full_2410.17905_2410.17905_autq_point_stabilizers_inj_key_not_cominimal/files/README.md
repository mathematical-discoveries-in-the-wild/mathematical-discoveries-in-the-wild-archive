# Full solution packet: point stabilizers in `Aut(Q,<)` are inj-key but not co-minimal

status: candidate_full_solution_likely_valid_needs_human_review

source_arxiv: 2410.17905

source_problem: Section 4 of Michael Megrelishvili, *Key subgroups in the Polish group of all automorphisms of the rational circle*, says that the linearly ordered rational case is expected and that the same method should show that every point stabilizer in `Aut(Q,<)` is inj-key but not co-minimal.

result: For the pointwise Polish topology on `G = Aut(Q,<)` and every `a in Q`, the stabilizer `G_a` is inj-key and is not co-minimal.

## Summary

Identify `Q` with the rational points of `(0,1)`. Every order automorphism extends uniquely to an increasing homeomorphism of `[0,1]`; let `tau_I` be the induced compact-open topology. This is the minimum Hausdorff group topology on the abstract group `G`, while the original pointwise topology is `tau_0`.

The proof adapts the source's circular argument to a finite chain. The six-orbit description of the greatest equivariant compactification of `G/G_a` implies that every Hausdorff group topology `sigma <= tau_0` gives one of exactly two quotient topologies on `G/G_a`: the discrete topology `tau_0/G_a` or the order topology `tau_I/G_a`. A localized factorization lemma shows that the mixed case `sigma|G_a = tau_0|G_a` and `sigma/G_a = tau_I/G_a` is impossible. Merson's lemma then proves injectivity of the restriction map on all coarser Hausdorff group topologies. Finally, `tau_I/G_a` is nondiscrete, so `G_a` is not co-minimal.

## Evidence

- `source_paper.pdf`: source paper, arXiv:2410.17905v3.
- `figures/source_problem.png`: exact Section 4 passage on PDF page 16.
- `main.tex`: full theorem and proof.
- `solution_packet.pdf`: compiled proof packet.

No computation is used.

## Novelty Check

A bounded check on 2026-07-22 searched the local run indexes and source corpus for arXiv:2410.17905, `Aut(Q,<)`, `inj-key`, `co-minimal`, and point stabilizers. No prior run result was found. Web searches restricted to mathematical source pages used the exact phrases `"Aut(Q,<)" "inj-key" point stabilizer`, `"Aut(Q,<=)" "co-minimal" stabilizer`, and `"linearly ordered rational" "inj-key" subgroup`. They found the source paper and the earlier general paper *Key subgroups in topological groups*, whose rational-circle result points back to the source; no proof of the linearly ordered case was found. The source version downloaded on 2026-07-22 still states the line case only as expected.

## Human Review Recommendation

High-priority topology review. Check the orbit-factor argument in the two-coset-topologies lemma, especially the assertion that every non-interval factor makes a point stabilizer open. Then check the localized `W^4` factorization and the use of the supremum of two group topologies in the final Merson argument. The remainder is formal.

