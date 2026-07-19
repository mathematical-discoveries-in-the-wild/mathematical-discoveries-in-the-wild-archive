# Partial Packet: UALS Problem 2, Unconditional-Saturation Reduction

Status: likely valid partial result.

Source problem: Argyros--Georgiou--Lagos--Motakis, "Joint spreading models and uniform approximation of bounded operators", arXiv:1712.07638, Section 5.5, Problem 2.

Result proved here: over complex scalars, any Banach space with no unconditional basic sequence contains an infinite-dimensional subspace satisfying the UALS property. Consequently, any complex Banach space answering Problem 2 positively must be unconditionally saturated: every infinite-dimensional subspace must contain an unconditional basic sequence.

Main inputs:

- Gowers dichotomy: every infinite-dimensional Banach space has a subspace with an unconditional basic sequence or a hereditarily indecomposable subspace.
- Ferenczi's theorem for complex HI spaces: every operator from a subspace of a complex HI space into the ambient HI space is a scalar multiple of the inclusion plus a strictly singular operator.
- The source paper's theorem: scalar-plus-strictly-singular spaces are UALS-saturated.

Scope limitation: this does not solve Problem 2. It eliminates the no-unconditional-basic-sequence side of the search over complex spaces. The remaining hard case is an unconditionally saturated space all of whose subspaces fail UALS.

Novelty/literature check: exact web searches for the source problem, "Uniform Approximation on Large Subspaces", "UALS property", and combinations with "complete separation" surfaced only the source UALS paper in the bounded pass. The packet is an agent-identified implication from known theorems, not a later paper explicitly answering the problem.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source UALS paper.
- `supporting_paper_math_9502207.pdf`: Ferenczi support.
- `supporting_paper_2106.10728.pdf`: modern arXiv statement/proof of Gowers dichotomy.
- `figures/open_problem_crop.png`: crop of the source open problem.
