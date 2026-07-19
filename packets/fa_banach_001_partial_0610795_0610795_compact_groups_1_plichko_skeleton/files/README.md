# Partial Result: Compact Groups Have 1-Plichko `C(G)`

Status: `partial_result_likely_valid`

Target: arXiv:0610795, Banakh--Kubis, *Spaces of continuous functions over
Dugundji compacta*

## Result

For every compact Hausdorff group `G`, of arbitrary weight, `C(G)` admits a
commutative norm-one projectional skeleton.  Hence `C(G)` is 1-Plichko.

Since compact groups are Dugundji compacta, this proves the compact-group
subcase of the source question asking whether `C(K)` is 1-Plichko for
Dugundji compacta of weight greater than `aleph_1`.

## Proof Idea

For each closed normal subgroup `N` with metrizable quotient `G/N`, average a
function over right cosets of `N` using Haar measure.  This gives a norm-one
projection from `C(G)` onto the copy of `C(G/N)`.

Closed normal subgroups with metrizable quotient are directed by reverse
inclusion.  The corresponding Haar averaging projections commute: averaging
over `N` and then `M` is averaging over `NM`.  Countable decreasing
intersections keep metrizable quotient, and Stone-Weierstrass gives the
required closure condition.  Density follows from Peter-Weyl, because matrix
coefficients of finite-dimensional representations factor through metrizable
quotients.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - rendered local copy of arXiv:0610795.
- `tmp/` - LaTeX build outputs.

## Limitations

This does not solve the full arbitrary Dugundji compact problem.  The proof
uses the group structure essentially through Haar averaging over normal
subgroups and Peter-Weyl density.
