# 2503.06191 collection equality gap full

Status: `full_solution_likely_valid`

Source: Julian Haddad, Dylan Langharst, Galyna V. Livshyts, and Eli Putterman, *On the polar of Schneider's difference body*, arXiv:2503.06191.

## Result

This packet closes the equality-condition gap in Theorem 11 of the source
paper.

Theorem 11 proves a polar Schneider inequality for a collection
`K_0,...,K_m` of centered convex bodies satisfying
`|K_i^o| = |K_0^o|`.  The source states that equality is necessary only if each
`K_i` is a centered ellipsoid, and sufficient when all `K_i` are the same
centered ellipsoid; it explicitly leaves open whether different centered
ellipsoids can also give equality.

The result here: equality holds if and only if
`K_0 = K_1 = ... = K_m` is a centered ellipsoid.

## Method

For centered ellipsoids `E_i`, write
`h_{E_i}(u)^2 = u^T Q_i u`.  Equal polar volumes give `det Q_i` independent of
`i`.  The polar volume is an integral of `exp(-h_{D^m(E_0,...,E_m)})`.  Each
factor `exp(-sqrt(u^T Q_i u))` is a positive mixture of centered Gaussians.

After the mixture expansion, the inner Gaussian integral has the block
determinant

```text
det M = prod_i det(t_i Q_i) * det(sum_i (t_i Q_i)^(-1)).
```

Minkowski's determinant inequality gives a pointwise lower bound for this
determinant, with equality only when all `Q_i` are equal.  Hence different
ellipsoid tuples give strictly smaller polar volume than the identical
ellipsoid tuple, and source Theorem 11 supplies the non-ellipsoid exclusion.

## Relation To Prior Partial

This supersedes the earlier narrow packet
`solutions/partial/2503.06191_m1_collection_equality_gap`, which closed only
the case `m=1`.

## Scope

This solves only the equality characterization for the source paper's polar
Schneider collection inequality.  It does not solve Schneider's original
higher-order volume-minimizer conjecture for `|D^m(K)| |K|^{-m}`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local source-paper PDF compiled from the arXiv source bundle.
- `figures/equality_gap_crop.png`: source page crop containing Theorem 11 and the equality-gap sentence.

## Review Focus

Check the Gaussian-mixture representation of `e^{-sqrt(q)}` and the strict
equality condition in Minkowski's determinant inequality for positive-definite
matrices.
