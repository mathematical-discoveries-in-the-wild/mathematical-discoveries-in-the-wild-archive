# Active Claim

agent_id: agent_lane_19
run_id: fa_banach_001
status: archived_no_full_resolution
started_at: 2026-06-16T18:17:08Z
last_updated_at: 2026-06-16T18:49:18Z
expires_if_no_update_after: 2026-06-17T06:17:08Z

arxiv_id: 2004.03062
paper_title: Indiscernible Subspaces and Minimal Wide Types
target: Hanson Question 4.3 full proof via symmetric spreading flattening
reserved_scope:
- Try to close the two remaining gaps after `attempts/2004.03062_normalized_spreading_symmetry_push.md`.
- Focus first on Hilbert/ell_2 spreading limits: prove symmetric uniformly continuous limits flatten on long block averages.
- Then test whether the stabilization transfer gives an actual subspace for the original stable formula.

current_stage: direct_attack
working_paths:
- runs/fa_banach_001/attempts/2004.03062_normalized_spreading_symmetry_push.md
- runs/fa_banach_001/attempts/2004.03062_wap_midpoint_lemma_full_push_notes.md
- runs/fa_banach_001/solutions/conditional/2004.03062_stability_wap_pullback_reduction/

notes:
- Key possible lemma: a uniformly continuous finite-permutation-invariant function on the ell_2 unit sphere is almost constant on vectors with sufficiently small sup norm.
- If true, long block averages inside a stabilized Hilbert spreading sequence may yield an actual almost-monochromatic subspace.
- The key possible lemma is false: distance to the sign/permutation orbit of flat vectors whose support sizes are powers of two is Lipschitz and symmetric, but separates flat support sizes 2^k from 3*2^k while sup norm tends to zero.
- The remaining plausible route is formula-aware Krivine-Maurey type machinery: enrich stable norm types with all phi(sigma_c(...),a) coordinates, pick a minimal conic continuity type, and prove scalar convolutions force the phi-coordinate to be constant on the resulting ell_p-type.

next_action:
- Verify whether the Krivine-Maurey conic-class proof survives after adding formula coordinates, especially the constancy of the phi-coordinate under normalized scalar convolutions.

archive_reason:
- Full proof not obtained.
- Durable attempt note created at `runs/fa_banach_001/attempts/2004.03062_symmetric_flattening_km_type_push.md`.
- Main result of this push: the naive symmetric small-sup-norm flattening lemma is false; the plausible next route is a formula-aware Krivine-Maurey type extraction.
