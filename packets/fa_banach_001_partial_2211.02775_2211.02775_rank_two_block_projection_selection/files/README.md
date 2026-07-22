# Rank-two block projection selection

Status: **partial result likely valid; subject to human review**.

The packet proves that every block projection p = SOT-sum p_n in a uniform
Roe algebra whose nonzero blocks all have rank two contains a block-rank-one
projection q = SOT-sum q_n with q_n <= p_n; moreover every subseries of the
q_n's belongs to the uniform Roe algebra.

Consequently, a noncompact rank-two block ghost projection always contains a
noncompact block-rank-one ghost projection. This affirmatively answers
Question 5.31 in Alessandro Vignati's 2026 habilitation and solves the
rank-two block-supported case of Question 6.1(1) in arXiv:2211.02775. The
broader question for arbitrary Boolean families of projections of rank
greater than one remains open.

## Contents

- solution_packet.pdf: human-readable theorem and proof.
- source_paper.pdf: Braga--Farah--Vignati, arXiv:2211.02775.
- supporting_context_vignati_hdr.pdf: the 2026 rank-two restatement.
- figures/open_problem_crop.png: Question 6.1 in the source paper.
- figures/rank_two_question_crop.png: Question 5.31 in the 2026 restatement.
- code/verify_rank_two_gap.py: finite numerical checks of the diagonal-gap
  lemma (not part of the proof).

Ledger:
runs/fa_banach_001/ledger/results/2211.02775_rank_two_block_projection_selection.json.
