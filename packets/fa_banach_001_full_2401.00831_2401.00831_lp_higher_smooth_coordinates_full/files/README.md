# Full Answer: Higher-Smooth Coordinates in the Lp Case

Status: `full_solution_likely_valid`

Run: `fa_banach_001`  
Agent: `agent_lane_15`  
Source paper: P. Hajek, M. Johanis, and T. Schlumprecht, *Remarks on the point character of Banach spaces and non-linear embeddings into c_0(Gamma)*, arXiv:2401.00831.

## Target

After Corollary 28, the source paper asks:

```text
We do not know whether in the corollary above in the case p >= 2
the component functions can be of higher smoothness.
```

The phrase `in the case p >= 2` refers to the `L_p(mu)` branch of the preceding
corollary, since `p` is the parameter in that branch.

## Result

Yes.  If `X` is a closed subspace of `L_p(mu)`, `2 <= p < infinity`, and
`dens X < omega_omega`, then the source embedding into `c_0(Gamma)` can be
chosen with `C^2` smooth coordinate functions.

More strongly, the coordinates can be chosen `C^m` for every integer `m < p`;
if `p` is an even integer, for every finite `m`.

## Mechanism

The source already supplies the metric `c_0(Gamma)` bi-Lipschitz embedding.
The smoothness upgrade uses the same Hajek-Johanis coordinate-smoothing
mechanism as the source's `C^1` corollary, but with the scalar approximation
input upgraded from `(*^1)` to `(*^m)`.  Fry-Keener gives `(*^m)` for WCG
spaces with a `C^m` smooth norm, and closed subspaces of `L_p(mu)` have the
needed smooth norms in the stated orders.

## Files

- `main.tex`: expert-facing full solution packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2401.00831.
- `supporting_paper_0907.0241.pdf`: Fry-Keener supporting paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Verification

The packet was rendered with `latexmk`; no computational verification is
needed.  The main review point is the order-`m` version of the coordinate
smoothing lemma, which is the same construction used in the source's `C^1`
case with `C^m` scalar approximants.

