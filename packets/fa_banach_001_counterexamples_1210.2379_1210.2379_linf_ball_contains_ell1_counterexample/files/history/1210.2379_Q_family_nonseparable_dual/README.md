# Partial Result: Nonseparable Duals for Ball Families in `JF(Q(Omega))`

## Status

`partial_result_likely_valid`

This packet proves part (ii) of Problem 1 in Argyros--Manoussakis--Petrakis,
`Function spaces not containing ell_1` (arXiv:1210.2379), for the two ball
families explicitly mentioned as open in the paper: Euclidean balls and
`ell_infty^{d_0}` balls contained in `Omega`.

The packet does **not** prove part (i). Whether the corresponding
`JF(Q(Omega))` spaces fail to contain `ell_1` for these ball families remains
open from this loop.

## Claim

Let `Omega` be a nonempty bounded open subset of `R^d`, and let `Q(Omega)` be
the family of Euclidean balls contained in `Omega`, or the family of
`ell_infty^d` balls contained in `Omega`. Then `JF^*(Q(Omega))` is
nonseparable.

More generally, if `Q` contains an uncountable subfamily of positive-measure
measurable sets that are pairwise distinct modulo null sets, then the
integration functionals `{V^*: V in Q}` contain an uncountable 1-separated
subfamily in the dual.

## Proof Mechanism

For any positive-measure measurable set `A`, the normalized indicator
`chi_A / mu(A)` has `JF(Q)` norm at most 1, because intersections with any
finite disjoint family from `Q` have total measure at most `mu(A)`. Hence every
`V in Q` gives a norm-one functional `V^*(f)=int_V f`.

If `U` and `V` differ modulo null sets, either `U \ V` or `V \ U` has positive
measure. Testing `U^*-V^*` on the normalized indicator of that difference gives
norm at least 1. An uncountable mod-null distinct family in `Q` therefore gives
an uncountable 1-separated subset of the dual.

For balls, fix a point of `Omega` and a small radius whose corresponding ball
or cube is still contained in `Omega`; varying the radius over an interval gives
continuum many pairwise mod-null distinct members of `Q`.

## Files

- `main.tex` - full proof packet source.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - local copy of arXiv:1210.2379.
- `figures/open_problem_crop.png` - crop of Problem 1 and the ball-family
  remark from the source paper.
- `code/crop_open_problem.py` - reproducible crop script using PyMuPDF.

## Verification

The proof is deterministic and uses only elementary measure estimates and the
definition of the `JF(Q)` norm. The main human-review point is scope: the
argument proves nonseparability of the dual, not absence of `ell_1` in the
space.

Cheap run indexes and a bounded web search found no exact prior packet or
obvious later exact answer for arXiv:1210.2379 Problem 1. The result is
presented as a new partial theorem for review, not as a full solution of the
problem.
