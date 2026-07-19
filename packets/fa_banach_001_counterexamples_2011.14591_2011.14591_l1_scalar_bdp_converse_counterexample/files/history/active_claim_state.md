# Active Claim State At Promotion

Canonical archive path:
`runs/fa_banach_001/agents/archive/2026-06-16/2011.14591_l1_scalar_bdp_converse_counterexample_agent_lane_17/state.md`

```text
# Active Claim

agent_id: agent_lane_17
run_id: fa_banach_001
status: promoted_counterexample
started_at: 2026-06-16T16:50:05.409140+00:00
last_updated_at: 2026-06-16T16:57:00+00:00
expires_if_no_update_after: 2026-06-17T04:50:05.409140+00:00

arxiv_id: 2011.14591
paper_title: Stability Results Of Small Diameter Properties In Banach Spaces
target: paper scan from deterministic lane queue
reserved_scope:
- paper-level scan until an exact question/route is selected

current_stage: packet_created
working_paths:
- runs/fa_banach_001/solutions/counterexamples/2011.14591_l1_scalar_bdp_converse_counterexample/
- runs/fa_banach_001/ledger/results/2011.14591_l1_scalar_bdp_converse_counterexample.json

queue_context:
- lane: 17 of 20
- mode: new
- rank: 466
- signals: 1
- dominant_signals: we_do_not_know:1

notes:
- Claim created by scripts/agent_target_queue.py.
- Exact signal: source remark after Lebesgue-Bochner BDP proposition asks whether converses of BHP/BDP propositions hold in general.
- Promoted packet records that the p=1 scalar example also refutes the BDP converse: R has BDP, while every slice of B_{L^1[0,1]} has diameter 2.
- The source already states the BHP converse fails for the same p=1 scalar example.

next_action:
- Archive active claim and refresh run indexes.
```
