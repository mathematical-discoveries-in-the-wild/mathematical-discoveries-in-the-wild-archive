# 2503.06191 m=1 collection equality gap

Status: `superseded_by_full`

Superseded by:
`runs/fa_banach_001/solutions/full/2503.06191_collection_equality_gap_full`

Source: Julian Haddad, Dylan Langharst, Galyna V. Livshyts, and Eli Putterman, *On the polar of Schneider's difference body*, arXiv:2503.06191.

## Result

The source paper's Theorem 11 proves a polar Schneider inequality for a collection
`K_0,...,K_m` and notes a gap between the necessary and sufficient equality
conditions: equality is necessary only if all `K_i` are centered ellipsoids, and
sufficient when all `K_i` are the same centered ellipsoid.

This packet closed that equality gap in the subcase `m=1`: if `K_0` and `K_1`
are centered ellipsoids with `|K_0^o|=|K_1^o|`, equality in Theorem 11 holds if
and only if `K_0=K_1`.

Equivalently, two different centered ellipsoids cannot be equality cases in the
collection inequality when `m=1`.

## Scope

This is now historical: the full collection equality gap is handled in the
full packet linked above.  Neither packet addresses Schneider's higher-order
volume-minimizer conjecture.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local PDF compiled from the arXiv source bundle.
- `figures/equality_gap_crop.png`: source page crop containing Theorem 11 and the equality-gap sentence.

## Review Focus

Check the equality-case use of Brunn-Minkowski. The argument needs only the
standard equality characterization for full-dimensional convex bodies: equality
in `|A+B|^{1/n} >= |A|^{1/n}+|B|^{1/n}` forces homothety.
