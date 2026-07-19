# Active Claim: Hanson Q4.3 Tail Finite Satisfiability Push

Run: `fa_banach_001`

Agent: `agent_lane_19`

Started: 2026-06-16

Status: `archived_full_claimed_likely_valid_human_review_needed`

Target: arXiv:2004.03062, James Hanson, *Indiscernible Subspaces and Minimal Wide Types*, Question 4.3.

Question: Does model-theoretic stability of a Banach theory imply oscillation stability of every unary formula?

This claim focuses on the remaining bottleneck isolated in prior attempts:
whether a stable minimal-wide-type construction can be made compatible with
finite satisfiability in every finite-codimensional tail of a fixed original
subspace `Y`.

Current plan:

1. Re-check the prior partial/conditional packets and attempt notes for exact
   duplicate status.
2. Search source/literature snippets for definable/finitely satisfiable
   Morley sequence facts that might give the missing tail coherence.
3. Try to prove or refute the tail finite-satisfiability preservation lemma.
4. Package any full proof, counterexample, conditional theorem, or serious
   obstruction, then refresh indexes and archive this claim.

Outcome:

- The tail finite-satisfiability/minimal-wide-type route still looks circular:
  Shelah--Usvyatsov gives unique wide extensions finitely satisfiable in the
  original model/sequence, but does not by itself push the extension through
  every finite-codimensional tail after normalized block combinations.
- A stronger formula-aware Krivine--Maurey/Raynaud route produced a claimed
  full solution packet:
  `runs/fa_banach_001/solutions/full/2004.03062_stability_implies_formula_oscillation_km/`.
- The proof reduces oscillation stability to an enriched stable type semigroup
  containing the chosen unary formula as a coordinate, then applies the exact
  stable Krivine--Maurey/Raynaud minimal conic-type argument to obtain a type
  whose normalized finite block sums have identical enriched type.
- Main human-review focus: verify that the exact Raynaud/Krivine--Maurey
  theorem transfers without loss to the enriched formula-aware fragment.
- Indexes were refreshed after packet creation.
