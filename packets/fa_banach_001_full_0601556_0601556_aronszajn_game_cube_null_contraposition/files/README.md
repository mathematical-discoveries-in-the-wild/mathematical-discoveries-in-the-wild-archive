# Aronszajn-null game cube-null contrapositive

status: candidate_full_solution_likely_valid_needs_human_review  
run_id: fa_banach_001  
agent_id: agent_lane_00  
source_arxiv_id: 0601556  
source_title: Null sets and games in Banach spaces  
packet_path: `runs/fa_banach_001/solutions/full/0601556_aronszajn_game_cube_null_contraposition/`

## Claim

Let `X` be a separable real Banach space and let `A subset X` be Borel. If
Player I has a winning strategy in Duda--Tsaban's Aronszajn-null game on `A`,
then `A` is not cube-null.

By Csornyei's theorem, Borel Aronszajn-null sets and cube-null sets coincide in
separable real Banach spaces. Therefore Duda--Tsaban Conjecture 2.4 has an
affirmative answer:

`A` Aronszajn-null implies Player I has no winning strategy.

## Proof idea

Assume Player I has a winning strategy. Player II plays one specially designed
legal counterplay. At inning `n`, Player II takes the countable union of all
Csornyei-style one-step bad sets for all finite rational cube-prefixes available
up to that inning. Each bad set is null on lines parallel to Player I's current
direction, so the union is legal.

The winning strategy leaves a point `a in A` outside all these bad sets. Because
Player II included every finite rational prefix at each stage, `a` can
afterwards thread an infinite sequence of rational cube widths and Borel
approximation indices. The associated translated cube measure gives positive
mass to `A`.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: Duda--Tsaban source paper.
- `figures/open_problem_crop.png`: source excerpt containing Conjecture 2.4.
- `superseded_partials/`: the earlier finite-dimensional and cylindrical
  pullback partial packets, retained as provenance only. They are no longer
  separate current run packets for this target.

No computational verifier is included; the proof is analytic/descriptive-set
theoretic.

## Consolidation note

This is the single canonical packet for arXiv:0601556 in the run. The two
earlier lane-0 partial packets were useful stepping stones, but the full
cube-null contrapositive does not depend on them and supersedes them for final
reporting.

## Novelty check

Local run indexes for `0601556`, `Aronszajn-null game`, `Duda Tsaban`,
`Conjecture 2.4`, `cube null`, `Pawlikowski`, and `Rothberger` found only the
two earlier lane-0 partial packets and the prior unfinished attempt.

External searches on 2026-06-15 for the exact conjecture and nearby game/null
keywords found the source paper and background cube-null/Csornyei material, but
no later paper claiming to solve the game conjecture.

## Human review recommendation

Review as a candidate full solution. The key audit point is the fusion step:
at each actual inning, Player II plays the countable union over all finite
rational cube-prefix bad sets, allowing the final surviving point to choose its
cube prefix after the play is known.
