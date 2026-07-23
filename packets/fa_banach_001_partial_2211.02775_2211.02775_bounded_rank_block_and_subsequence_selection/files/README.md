# Bounded-rank block and subsequence selection

Status: **substantial partial result likely valid; subject to human review**.

The packet proves two extensions of the rank-two block theorem.

1. Every block projection in a uniform Roe algebra whose nonzero blocks have
   ranks in a fixed finite interval `[2,R]` contains a block-rank-one
   projection, and every Boolean subseries of the selected rank-one blocks
   remains in the uniform Roe algebra.
2. For an arbitrary Boolean family from Question 6.1, if some finite rank
   occurs infinitely often, an infinite subsequence admits rank-one
   subprojections with the required Boolean-subseries property. In particular,
   this settles Question 6.1(2) for every uniformly bounded-rank family and
   for arbitrary-support rank-two families.

The first theorem uses compactness of isotropic measures on complex
projective space to obtain finitely many uniformly separating diagonal tests.
The second uses a disjoint-support gliding hump, summable perturbations, and a
compactly perturbed partial isometry.

The remaining cases of Question 6.1 are unbounded finite ranks, infinite
ranks, and the all-indices conclusion for general non-block families.

## Contents

- `solution_packet.pdf`: theorem statements and complete proofs.
- `source_paper.pdf`: Braga--Farah--Vignati, arXiv:2211.02775.
- `supporting_context_vignati_hdr.pdf`: the 2026 rank-two restatement.
- `figures/open_problem_crop.png`: Question 6.1 in the source paper.
- `figures/rank_two_question_crop.png`: Question 5.31 in the habilitation.
- `code/verify_rank_two_gap.py`: numerical consistency check for the explicit
  two-dimensional gap lemma; it is not used as proof.

Ledger:
`runs/fa_banach_001/ledger/results/2211.02775_bounded_rank_block_and_subsequence_selection.json`.
