# Candidate Counterexample: `G`-RNP Does Not Imply RNP For General Groups

Run: `fa_banach_001`

Source paper: Sheldon Dantas, Michal Doucha, Mingu Jung, Tomas Raunig,
"Group equivariant Radon-Nikodym Property and its characterizations",
arXiv:2510.23100.

Target: Problem 8.2, specifically the dotted implication

```text
G-RNP => RNP.
```

Status: candidate counterexample, likely valid pending human review.

## Claim

For the topological group `G = Homeo_+([0,1])`, acting by composition on
`X = C_0((0,1))`, the space `X` has the `G`-RNP but does not have the
classical RNP. The key mechanism is that `G` is unitarily trivial by
Megrelishvili's theorem, so every admissible continuous positive isometric
`L_1` action becomes trivial after applying the Mazur map to `L_2`. Thus
`G`-RNP reduces to the RNP of the fixed-point subspace `X^G`, which is zero,
while `X` contains an isometric copy of `c_0`.

The packet also records positive coverage: the supplied finite-group partial
extends to locally compact sigma-compact groups, so the counterexample is only
for the unrestricted general-topological-group implication.

## Packet Files

- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of Problem 8.2.
- `main.tex`: consolidated counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `evidence/2026-06-22_g_rnp_counterexample/`: supplied TeX/PDF report.
- `history/packets/partial_packet_2510.23100_finite_group_grnp_implies_rnp_2026_06_14/`: earlier finite-group partial packet, now absorbed as history.

## Human Review Recommendation

Review as a likely valid counterexample packet. The main checks are the
definition repair around the source paper's vector-measure/operator
formulation, the Mazur-map transfer from positive `L_1` actions to Hilbert
representations, Megrelishvili's unitarily triviality theorem for
`Homeo_+([0,1])`, and whether Problem 8.2 was intended to include arbitrary
topological groups beyond the locally compact sigma-compact setting.
