# Active Claim

agent_id: agent_lane_19
run_id: fa_banach_001
status: completing
started_at: 2026-06-16T17:48:22Z
last_updated_at: 2026-06-16T18:05:44Z
expires_if_no_update_after: 2026-06-17T05:48:22Z

arxiv_id: 2004.03062
paper_title: Indiscernible Subspaces and Minimal Wide Types
target: Hanson Question 4.3 via normalized-sum/Gowers extraction
reserved_scope:
- Attack the strengthened route isolated in `attempts/2004.03062_wap_midpoint_lemma_full_push_notes.md`.
- Try to prove that stable normalized linear-combination pullbacks force oscillation stability.
- In particular, test whether stable pullbacks imply symmetric spreading models and whether symmetric uniformly continuous Hilbert-sphere colorings flatten on block subspaces.

current_stage: structural_lemma_recorded
working_paths:
- runs/fa_banach_001/attempts/2004.03062_wap_midpoint_lemma_full_push_notes.md
- runs/fa_banach_001/attempts/2004.03062_normalized_spreading_symmetry_push.md
- runs/fa_banach_001/solutions/conditional/2004.03062_stability_wap_pullback_reduction/
- data/parsed/arxiv_sources/2004.03062/Indiscernible_Subspaces_and_Minimal_Wide_Types.tex

notes:
- Key new observation: Hanson's Banach language has normalized maps `sigma_c`; stable unary formulas therefore yield stable pullbacks along normalized finite sums, not only midpoint kernels.
- Candidate proof skeleton: stabilize a uniformly continuous coloring to a spreading model, use stability of normalized-sum pullbacks to force permutation symmetry, then use a block-flat/permutation-invariant coloring lemma to get an almost monochromatic Hilbert subspace.
- Proved and recorded the first skeleton step: stable normalized pullbacks force block-symmetric spreading limits.
- Remaining gaps are uniform spreading-to-subspace transfer and flattening of symmetric spreading colorings allowed by stable pullbacks.

next_action:
- Rebuild indexes and archive this active claim.
