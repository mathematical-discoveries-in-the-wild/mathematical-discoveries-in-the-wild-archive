# 2606.02040 - branch-regular tree reduction for large AD families on N*

Status: conditional reduction, likely valid conditional proof.

Source paper: Chris Lambie-Hanson and David Schrittesser, "Generalized almost disjoint families and injective Banach spaces", arXiv:2606.02040.

## Conditional Result

If there exists a binary branch-regular Hausdorff tree in \(\mathcal P(\omega)/\mathrm{Fin}\), then Question 4.3 of the source paper has a positive answer at the first requested cardinal: there is an almost disjoint family on \(\mathbb N^*\) of cardinality \(2^{\aleph_1}\).

The tree dependency is explicit in `main.tex`. It asks for sets \(a_s\subseteq\omega\), indexed by \(s\in2^{<\omega_1}\), with mod-finite monotonicity, controlled intersections \(a_s\cap a_t={}^*a_{s\wedge t}\), genuine splitting, and a branch-regularity condition ensuring that each branch union is a regular open subset of \(\mathbb N^*\).

## Why This Matters

The previous packet `2606.02040_zfc_continuum_ad_family_nstar` gives a ZFC family of size \(2^{\aleph_0}\). The obstacle to reaching \(2^{\aleph_1}\) is producing many noncompact regular open sets whose pairwise intersections collapse to compact clopen sets. This packet isolates a precise combinatorial object that would do exactly that.

The source paper proves a stronger-looking tree under \(\mathfrak b=2^{\aleph_0}\). The conditional packet strips the implication down to the tree property itself, making the remaining target: prove the binary branch-regular tree in ZFC, or show that it implies a non-ZFC cardinal-invariant principle.

## Scope

This is not a full ZFC solution. The unproved dependency is the existence of the branch-regular tree. The proof from that dependency to a \(2^{\aleph_1}\)-sized generalized almost disjoint family is complete.

## Files

- `main.tex` - conditional reduction packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2606.02040.
- `figures/open_problem_crop.png` - crop of Question 4.3.

