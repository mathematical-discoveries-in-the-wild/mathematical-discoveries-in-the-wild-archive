# Active Claim

agent_id: agent_lane_19
run_id: fa_banach_001
status: archived_no_full_resolution
started_at: 2026-06-16T20:03:04Z
last_updated_at: 2026-06-16T20:16:05Z
expires_if_no_update_after: 2026-06-17T08:03:04Z

arxiv_id: 2004.03062
paper_title: Indiscernible Subspaces and Minimal Wide Types
target: Hanson Question 4.3 full lemma via formula-aware Krivine-Maurey types

reserved_scope:
- Push the formula-aware Krivine-Maurey/type-semigroup route from `attempts/2004.03062_symmetric_flattening_km_type_push.md`.
- Keep the naive symmetric flattening obstruction as a guardrail: `F(x)=dist(x,A)` for the sign/permutation orbit of flat vectors with support sizes `2^k` is Lipschitz and symmetric but not small-sup-norm flattening.
- Try to prove that stability of all Banach-language normalized pullbacks forces the formula coordinate to be constant on a selected normalized `ell_p`-type.

current_stage: direct_attack

working_paths:
- runs/fa_banach_001/attempts/2004.03062_symmetric_flattening_km_type_push.md
- runs/fa_banach_001/attempts/2004.03062_normalized_spreading_symmetry_push.md
- runs/fa_banach_001/solutions/conditional/2004.03062_stability_wap_pullback_reduction/

notes:
- Symmetry plus uniform continuity is false as an engine; stability must forbid support-scale oscillation.
- Candidate full lemma: enriched stable KM type space with coordinates for all `phi(sigma_c(...),a)` admits a continuity/minimal type whose normalized scalar convolutions have constant `phi` coordinate.
- Stronger current formulation: build a minimal wide type that remains finitely satisfiable in every finite-codimensional tail of the chosen subspace `Y`; if its nonforking/wide extensions preserve this tail finite satisfiability, a Morley block sequence can be approximated inside `Y` and would give the desired oscillation-stable subspace.

next_action:
- Formalize the tail-finitely-satisfiable minimal wide type lemma and identify whether preservation under extensions is provable from stability or is the remaining gap.

archive_reason:
- Full proof not obtained.
- Durable attempt note created at `runs/fa_banach_001/attempts/2004.03062_tail_minimal_wide_type_push.md`.
- Main result of this push: the final obstruction is now formulated as preservation/coherence of tail finite satisfiability through the stable minimal-wide-type/Morley-spine construction.
