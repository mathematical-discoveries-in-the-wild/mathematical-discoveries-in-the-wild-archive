# Full solution: LRP/ANEP is equivalent to NEP

status: full_solution_likely_valid

source: Antonin Dalet and Gilles Lancien,
*Some properties of coarse Lipschitz maps between Banach spaces*,
arXiv:1612.01364.

target: The remark after Proposition 4.4 asks whether the converse of
Proposition 4.4 is true. The source proves that NEP implies LRP and records
that LRP is equivalent to ANEP; it leaves open whether LRP/ANEP implies NEP.

packet: `runs/fa_banach_001/solutions/full/1612.01364_lrp_anep_nep_equivalence/`

ledger: `runs/fa_banach_001/ledger/results/1612.01364_lrp_anep_nep_equivalence.json`

## Result

For Banach spaces `X` and `Y`, the following are equivalent:

1. `(X,Y)` has the net extension property (NEP).
2. `(X,Y)` has the Lipschitz representation property (LRP) for some constant.
3. `(X,Y)` has the almost net extension property (ANEP) for some constant.

Thus the converse of Proposition 4.4 in the source paper is true.

## Main Idea

The only missing implication is `ANEP => NEP`.

Let `M` be the `(a,b)`-net witnessing ANEP. Given a Lipschitz map
`f:M -> Y`, ANEP gives a Lipschitz `g:X -> Y` such that `e=f-g` is bounded on
`M`. Since `M` is `a`-separated, any bounded `Y`-valued function on `M`
extends Lipschitzly to `X` by disjoint radius-`a/4` tent bumps. Applying this
to `e` gives a Lipschitz correction `E:X -> Y` with `E|_M=e`, so `g+E`
extends `f` exactly.

## Verification

- The source definition of net was checked: nets are `(a,b)`-nets with
  `a>0`, hence separated.
- The exact source remark after Proposition 4.4 was checked directly.
- Cheap run indexes were searched for `1612.01364`, `ANEP`,
  `almost net extension`, `LRP`, and `net extension property`.
- No existing packet for this converse target was found.

## Scope

This fully answers the local converse question after Proposition 4.4. It
does not solve the later general completeness conjecture for `CL(X,Y)`;
completeness might still hold or fail without being equivalent to LRP/NEP.

## Files

- `main.tex`: full solution packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/converse_remark_crop.png`: crop of Proposition 4.4 and the
  source remark.
