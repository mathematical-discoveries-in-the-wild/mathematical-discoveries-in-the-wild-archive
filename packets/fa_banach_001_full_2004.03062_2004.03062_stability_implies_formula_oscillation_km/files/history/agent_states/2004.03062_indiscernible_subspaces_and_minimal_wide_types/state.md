# Active Claim

agent_id: agent_lane_19
run_id: fa_banach_001
status: archived
started_at: 2026-06-16T16:06:17.133995+00:00
last_updated_at: 2026-06-16T16:18:36+00:00
expires_if_no_update_after: 2026-06-17T04:06:17.133995+00:00

arxiv_id: 2004.03062
paper_title: Indiscernible Subspaces and Minimal Wide Types
target: paper scan from deterministic lane queue
reserved_scope:
- paper-level scan until an exact question/route is selected

current_stage: partial_result_packet_completed
working_paths:
- runs/fa_banach_001/solutions/partial/2004.03062_hilbert_operator_qf_oscillation_stability/
- runs/fa_banach_001/ledger/results/2004.03062_hilbert_operator_qf_oscillation_stability.json

queue_context:
- lane: 19 of 20
- mode: new
- rank: 590
- signals: 1
- dominant_signals: natural_question:1

notes:
- Claim created by scripts/agent_target_queue.py.
- Update this claim once an exact problem, route, or attempt retry is chosen.
- Question 4.3 asks whether model-theoretic stability implies oscillation stability for unary formulas.
- The source preprint was absorbed into arXiv:2011.00610; the corrected absorbing paper keeps the question.
- Promoted a scoped partial result: quantifier-free unary formulas in Hilbert structures expanded by bounded linear operator symbols are oscillation stable on infinite-dimensional subspaces, via simultaneous quadratic-form flattening.
- This is not a full answer for arbitrary stable Banach theories or arbitrary quantified unary formulas.

next_action:
- Human review of the partial packet; possible future push is to combine this with quantifier-elimination results for specific stable Hilbert operator theories, or to attack quantified formulas directly.
