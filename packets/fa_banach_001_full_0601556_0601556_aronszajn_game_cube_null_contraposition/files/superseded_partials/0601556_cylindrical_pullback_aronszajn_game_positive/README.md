# Cylindrical pullback positive cases for the Aronszajn-null game

status: partial_result_likely_valid  
run_id: fa_banach_001  
agent_id: agent_lane_00  
source_arxiv_id: 0601556  
source_title: Games in Banach spaces  
packet_path: `runs/fa_banach_001/solutions/partial/0601556_cylindrical_pullback_aronszajn_game_positive/`

## Claim

Let `T:X -> Y` be a continuous linear surjection between separable real Banach
spaces. If `B subset Y` is Borel and Player II wins the Aronszajn-null game on
`B`, then Player II wins the Aronszajn-null game on `T^{-1}(B)` in `X`.

Combining this with the earlier finite-dimensional packet, if `Y` is
finite-dimensional and `N subset Y` is Borel Lebesgue null, then
`T^{-1}(N)` is II-winning in `X`. Countable unions of such cylindrical null
sets are II-winning as well.

## Why this matters

The previous packet solved only the finite-dimensional ambient case. This
packet lifts that result into arbitrary separable Banach spaces for all
finite-dimensional cylindrical null sets. It does not solve the full
Duda--Tsaban conjecture, but it gives a stable way to manufacture infinite
dimensional II-winning Aronszajn-null sets that are not merely subsets of
proper closed subspaces.

## Proof idea

Given a play in `X`, apply `T` to Player I's directions. The image of a dense
sequence under a continuous surjection is dense in `Y`. Feed the nonzero image
directions into the winning strategy for `B` in `Y`; pull back Player II's
responses. A line in `X` parallel to `x` maps onto a line in `Y` parallel to
`Tx`, so null sections pull back to null sections.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: source excerpt for the conjecture.

## Human review recommendation

Check the pullback legality when `Tx != 0`, and the treatment of innings with
`Tx = 0`. The proof only uses continuity, surjectivity, density of images, and
one-dimensional null preservation under a nonconstant affine map of lines.
