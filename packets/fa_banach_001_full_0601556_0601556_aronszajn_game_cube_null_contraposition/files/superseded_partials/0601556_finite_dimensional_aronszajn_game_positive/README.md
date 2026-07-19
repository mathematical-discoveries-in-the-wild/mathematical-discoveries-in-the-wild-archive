# Finite-dimensional Aronszajn-null game subcase

status: partial_result_likely_valid  
run_id: fa_banach_001  
agent_id: agent_lane_00  
source_arxiv_id: 0601556  
source_title: Games in Banach spaces  
packet_path: `runs/fa_banach_001/solutions/partial/0601556_finite_dimensional_aronszajn_game_positive/`

## Claim

For every finite-dimensional real Banach space `X` and every Borel
Aronszajn-null set `A subset X`, Player II has a winning strategy in the
Aronszajn-null game `G_A`.

This proves the source paper's Conjecture 2.4 in the finite-dimensional case,
and gives the stronger conclusion `II wins`, not merely `I does not win`.

## Source Question

Duda--Tsaban define the Aronszajn-null game and prove that if Player I has no
winning strategy, then `A` is Aronszajn-null. They ask for the converse:

> If `A` is Aronszajn-null, then Player I has no winning strategy in the game.

The excerpt is shown in `figures/open_problem_crop.png`.

## Proof Idea

In finite dimensions, every Aronszajn-null Borel set is Lebesgue null. Player II
waits for the first directions played by Player I that are linearly independent.
At each such direction, apply Fubini in the current quotient by the span of the
previous independent directions: the part with null line sections is a legal
move for Player II, and the residual projects to a lower-dimensional null set.
After finitely many independent directions, the quotient has dimension zero, so
the residual is empty. Since Player I's legal play must be dense, those
independent directions eventually appear.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: source excerpt for the conjecture.

## Novelty Check

Cheap run indexes had no prior packet for `0601556`. Local corpus and exact web
searches for `"Aronszajn-null game"` and the source conjecture found the source
paper but no later answer. Novelty confidence is moderate: this is an elementary
finite-dimensional subcase, so it may be folklore, but it is not recorded in
the run memory or the obvious local/web hits.

## Human Review Recommendation

Review the Fubini quotient induction, especially the measurability of the
positive-section set and the pullback claim `pi^{-1}(G) in A(v)`. These are
standard for Borel sets under linear quotient maps.
