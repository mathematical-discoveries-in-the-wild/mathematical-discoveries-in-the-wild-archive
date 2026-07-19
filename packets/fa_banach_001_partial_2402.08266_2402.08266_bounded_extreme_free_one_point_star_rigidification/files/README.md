# Bounded preserved-extreme-free one-point star rigidification

- Run: `fa_banach_001`
- Lane: 18
- Agent: `agent_lane_18`
- Date: 2026-07-03
- Source: Marek Cuth, Michal Doucha, and Tamas Titkos, *Isometries of Lipschitz-free Banach spaces*, arXiv:2402.08266.
- Source target: Question 3 in Section 8.2, asking whether every metric space embeds isometrically into a Lipschitz-free rigid space with only one additional point.
- Status: `partial_result_likely_valid`

## Result

Let `M` be a bounded metric space such that `F(M)` has no preserved-extreme
elementary molecules, equivalently `E_ext(M)` is empty.  Choose
`R > diam(M)` and add one point `p` with `d(p,x)=R` for all `x in M`.
Then `M union {p}` is Lipschitz-free rigid.

This gives an infinite-family positive answer to the one-point question,
covering bounded geodesic metric spaces and other bounded spaces with no
preserved-extreme pairs.

## Idea

The new preserved-extreme graph is exactly the star centered at `p`.  Any
admissible edge bijection from the source paper therefore corresponds to a
bijection of old points plus a sign on each spoke.  Applying the source wA3
norm identity to the path `x-p-y` shows that opposite spoke signs would force a
norm equal to `2R`, while `d(x,y) < R`.  Thus all signs are global.  With a
global sign, the same identity reduces to `d(x,y)=d(f(x),f(y))`; the induced
bijection is an isometry of `M`, extended by fixing `p`.

## Scope

This does not settle the full arbitrary-metric-space problem.  The obstruction
left open is the interaction between the new star and old preserved-extreme
edges of an infinite metric space.  The finite case is handled separately in
`solutions/partial/2402.08266_finite_metric_one_point_rigidification/`.

## Verification

- The packet uses the source paper's preserved-extreme criterion and weak
  Prague isometry correspondence.
- Later-literature searches on 2026-07-03 for exact one-point rigidification
  phrases and `2402.08266` found the source paper but no full settlement.
- `code/constant_cone_search.py` is scratch finite evidence for constant cones;
  the proof in the packet is not computational.

Human review should focus on the assertion that the preserved-extreme graph of
the extension is exactly the radial star when `E_ext(M)` is empty.
