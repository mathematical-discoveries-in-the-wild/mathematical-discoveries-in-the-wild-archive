# Higher-Smooth Coordinate Embeddings for the Lp Branch

Status: `absorbed_into_full_solution`

Superseded by:
`runs/fa_banach_001/solutions/full/2401.00831_lp_higher_smooth_coordinates_full/`.
The full packet observes that the source question only asks for higher
smoothness in the `p >= 2` `L_p` case, so the `C^2` consequence below gives a
full answer.

Run: `fa_banach_001`  
Agent: `agent_lane_15`  
Source paper: P. Hajek, M. Johanis, and T. Schlumprecht, *Remarks on the point character of Banach spaces and non-linear embeddings into c_0(Gamma)*, arXiv:2401.00831.

## Target

After Corollary 28, the source paper asks whether, in the case `p >= 2`, the bi-Lipschitz embedding into `c_0(Gamma)` can be chosen so that its coordinate functions have higher smoothness than `C^1`.

## Result

For the `L_p` branch of the corollary, yes:

```text
Let X be a closed subspace of L_p(mu), 2 <= p < infinity, with dens X < omega_omega.
If m is a positive integer with m < p, then X admits a bi-Lipschitz embedding
into some c_0(Gamma) whose coordinate functions are C^m smooth.
If p is an even integer, the conclusion holds for every finite m.
```

In particular, every such `L_p` subspace with `p >= 2` has a higher-than-`C^1`
coordinate embedding; for non-even `p`, the available order is the usual
smoothness range of the `L_p` norm.

## Proof Mechanism

The source obtains `C^1` coordinates by combining its metric embedding theorem
with the Hajek-Johanis coordinate-smoothing theorem and a `C^1` scalar
approximation theorem. The upgrade replaces the `C^1` approximation input by
Fry-Keener's `C^m` Lipschitz approximation theorem for WCG spaces with a `C^m`
smooth norm. The Hajek-Johanis coordinate-smoothing argument is order-free:
where it uses `C^1` Lipschitz scalar approximants, the same construction gives
`C^m` coordinates when the scalar approximants are `C^m`.

## Files

- `main.tex`: expert-facing proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2401.00831.
- `supporting_paper_0907.0241.pdf`: Fry-Keener supporting paper.
- `figures/open_problem_crop.png`: source crop of Corollary 28 and the higher-smoothness question.

## Scope

This packet upgrades the earlier conditional packet
`solutions/conditional/2401.00831_cm_smooth_coordinate_upgrade/` for the
`L_p` subcase. It does not settle the super-reflexive Banach lattice branch of
the source corollary unless those spaces are separately known to have the
corresponding `(*^m)` Lipschitz smooth approximation property.
