# Conditional C^m Smooth Coordinate Upgrade for the c0(Gamma) Embedding

Status: `absorbed_into_full_solution`

Superseded by:
`runs/fa_banach_001/solutions/full/2401.00831_lp_higher_smooth_coordinates_full/`.
This earlier packet isolated the `C^m` coordinate-smoothing route; the later
full packet promotes the `L_p`, `p >= 2`, source question by taking `C^2`
coordinates.

Run: `fa_banach_001`  
Agent: `agent_lane_15`  
Source paper: P. Hajek, M. Johanis, and T. Schlumprecht, *Remarks on the point character of Banach spaces and non-linear embeddings into c_0(Gamma)*, arXiv:2401.00831.

## Target

After Corollary 28, the source paper asks whether, for `p >= 2`, the bi-Lipschitz embedding into `c_0(Gamma)` can be chosen so that its coordinate functions have higher smoothness than `C^1`.

## Conditional Result

This packet isolates a narrow upgrade route:

```text
If the Hajek-Johanis/Johanis smooth-coordinate c0 embedding theorem used
for Corollary 28 has the formal C^m analogue whenever X has Lipschitz
C^m scalar approximation, then Corollary 28 improves from C^1 to C^m
for WCG spaces with a C^m smooth norm.
```

Combining that formal `C^m` coordinate-smoothing lemma with Fry-Keener's
Lipschitz `C^m` approximation theorem gives the concrete conditional subcase:

```text
For X subset L_p(mu), dens X < omega_omega, and integer m with m < p
(or arbitrary finite m when p is an even integer), the c_0(Gamma)
embedding can be chosen with C^m smooth component functions.
```

This gives genuine higher smoothness for every `p > 2` at least up to
`m = floor(p)` when `p` is not an integer and up to `m = p-1` when `p` is an
odd integer, subject to the coordinate-smoothing dependency above. For
Hilbertian/even-power cases the smooth-norm input supports all finite orders.

## Why It Matters

The source paper already obtains `C^1` coordinates by combining its embedding
theorem with smooth approximation machinery. Fry-Keener proves the matching
Lipschitz `C^m` approximation theorem on WCG spaces admitting a `C^m` smooth
norm. Thus the only remaining check is whether the c0-valued coordinate
smoothing construction is order-free in the differentiability class. The packet
states that dependency explicitly for human review.

## Files

- `main.tex`: expert-facing conditional proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2401.00831.
- `supporting_paper_0907.0241.pdf`: Fry-Keener supporting paper.
- `figures/open_problem_crop.png`: crop of Corollary 28 and the higher-smoothness question.

## Verification

No numerical verification is needed. The mathematical work is a dependency
isolation plus a checked chain of known hypotheses:

- subspaces of `L_p(mu)`, `1<p<infty`, are reflexive, hence WCG;
- such subspaces inherit a `C^m` smooth norm for the usual allowed orders;
- Fry-Keener gives Lipschitz `C^m` scalar approximation on WCG spaces with a
  `C^m` smooth norm;
- the source paper already supplies the underlying bi-Lipschitz embedding into
  `c_0(Gamma)` for density below `omega_omega`.

Novelty check: run indexes had no entry for `2401.00831` or the smooth
coordinate question. Exact web searches for the source title plus "higher
smoothness" and the unit-ball problem found the source paper but no later
answer.

## Limitations

This is not a full solution of the smoothness question. It is conditional on a
specific `C^m` version of the smooth-coordinate c0 embedding theorem, and it
does not address all super-reflexive spaces, all Banach lattice cases, or
orders beyond those supported by smooth norms on `L_p`.
