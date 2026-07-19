# Active Claim

agent_id: agent_lane_19
run_id: fa_banach_001
status: archived
started_at: 2026-06-16T16:34:19+00:00
last_updated_at: 2026-06-16T16:41:00+00:00
expires_if_no_update_after: 2026-06-17T04:34:19+00:00

arxiv_id: 2004.03062
paper_title: Indiscernible Subspaces and Minimal Wide Types
target: Hanson Question 4.3, promotion push after quantifier-free Hilbert-operator partial result
reserved_scope:
- Attempt to promote, obstruct, or sharply reduce whether stability implies oscillation stability for unary formulas in stable Banach theories.

current_stage: strengthened_partial_packet_completed
working_paths:
- runs/fa_banach_001/solutions/partial/2004.03062_hilbert_operator_qf_oscillation_stability/
- runs/fa_banach_001/attempts/2004.03062_stability_oscillation_full_push_notes.md
- runs/fa_banach_001/ledger/results/2004.03062_hilbert_operator_qf_oscillation_stability.json

queue_context:
- lane: 19 of 20
- mode: revisit current partial result

notes:
- Existing packet proves oscillation stability for quantifier-free unary formulas in Hilbert structures expanded by bounded linear operator symbols.
- Main pressure points: quantified formulas, quantifier elimination for stable Hilbert-operator classes, and possible stable Banach counterexamples outside Hilbert/operator-linear settings.
- Strengthened the packet with a QE-transfer corollary.
- Added named stable Hilbert-operator classes: bounded normal operators in the language with T and T*, self-adjoint/unitary one-operator cases, and finite-group unitary representations.
- Supporting literature: arXiv:2507.21894 and arXiv:2409.03923.
- Direct full-proof route via block high/low vectors did not yield an order-property witness.
- Counterexample route via Maurey/Odell-Schlumprecht wild Hilbert colorings lacks stability of the expanded predicate theory; known stable predicate/operator examples found reduce to operator-linear/subspace-distance cases.

next_action:
- Human review of the strengthened partial packet; future full push needs either a Ramsey-to-order-property lemma for stable formulas or a genuinely stable non-operator Hilbert/Banach predicate counterexample.
