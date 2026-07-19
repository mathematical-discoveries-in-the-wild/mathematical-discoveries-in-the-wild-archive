# Active Claim: Referee Check of Formula-Aware KM Packet

Run: `fa_banach_001`

Agent: `agent_lane_19`

Started: 2026-06-16

Status: `archived_referee_expanded_full_claim`

Target: arXiv:2004.03062, Hanson Question 4.3, existing full packet
`runs/fa_banach_001/solutions/full/2004.03062_stability_implies_formula_oscillation_km/`.

Goal:

Perform a line-by-line stress test of the formula-aware Krivine--Maurey lemma.
If it survives, expand the packet into a self-contained proof. If it fails,
demote or annotate the packet with the precise obstruction.

Review focus:

1. Verify the enriched type space and convolution are well-defined.
2. Check whether the Raynaud/Krivine--Maurey exact conic-class proof transfers
   to enriched stable formula coordinates.
3. Check whether the resulting sequence controls all vectors in the closed
   span, not only rational finite block sums.
4. Update packet, ledger, indexes, and archive this claim.

Outcome:

- The earlier packet survived the main formula-aware KM transfer check, but
  the old final extraction was too compressed: a bare far-out subsequence does
  not automatically control vectors involving early elements of the closed
  span.
- The packet was expanded and repaired. The proof now uses a block extraction
  lemma that maintains approximate enriched type on finite nets of every
  initial span.
- The Raynaud/Krivine--Maurey transfer was expanded into explicit steps:
  enriched convolution, minimal conic class, common continuity point,
  spreading-model comparison, approximate eigenvectors, and multiplicative
  norm classification.
- Durable packet updated:
  `runs/fa_banach_001/solutions/full/2004.03062_stability_implies_formula_oscillation_km/`.
- Ledger status changed to
  `full_claimed_referee_expanded_human_review_needed`; indexes refreshed.
