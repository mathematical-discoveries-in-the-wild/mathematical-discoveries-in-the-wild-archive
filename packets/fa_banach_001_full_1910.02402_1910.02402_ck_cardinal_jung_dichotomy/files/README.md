# Full packet: cardinal Jung dichotomy for `C(K)` spaces

status: full_solution_likely_valid

source: Jesus M. F. Castillo and Pier Luigi Papini, *The separable
Jung constant in Banach spaces*, arXiv:1910.02402.

target: Section 2 asks whether, for spaces of continuous functions, the
cardinal Jung condition `J_aleph(C(K)) < 2` forces
`J_aleph(C(K)) = 1`.

packet: `runs/fa_banach_001/solutions/full/1910.02402_ck_cardinal_jung_dichotomy/`

## Result

This packet proves the source question.

For every uncountable cardinal `aleph` and every compact Hausdorff space
`K`,

```text
J_aleph(C(K)) = 1  if K is an F_aleph-space,
J_aleph(C(K)) = 2  otherwise.
```

Consequently, `J_aleph(C(K)) < 2` implies `J_aleph(C(K)) = 1`.

## Proof Mechanism

The positive direction is Castillo--Papini's characterization
`J_aleph(X)=1` iff `X` is `(1,aleph)`-injective, combined with
Aviles--Cabello Sanchez--Castillo--Gonzalez--Moreno's characterization
that `C(K)` is `(1,aleph)`-injective iff `K` is an `F_aleph`-space.

For the converse, if `K` is not an `F_aleph`-space, there are disjoint
open sets `G,H`, each a union of fewer than `aleph` closed sets, whose
closures meet. For every closed piece of `G` choose a continuous
`[0,1]`-valued function equal to `1` there and supported in `G`; do the
same on `H`. The set consisting of all positive-side functions and the
negatives of all negative-side functions has cardinal and density
`< aleph`, diameter `1`, and radius `1`. Any center of radius `<1` would
be forced to have real part at least `1-rho` on `cl G` and at most
`-1+rho` on `cl H`, impossible at a common closure point.

## Verification

- Cheap run indexes were searched for `1910.02402`, `separable Jung`,
  `J_s(C(K))`, `J_aleph(C(K))`, `Jung constant C(K)`, `F_aleph`, and
  related keywords.
- The exact arXiv id had only the earlier partial packet from this lane,
  now upgraded in place to this full packet.
- The cited cardinal source arXiv:1406.6733 was inspected locally for the
  exact `F_aleph` definition and the `C(K)` characterization.
- Web searches on 2026-07-03 for exact phrases including
  `"J_aleph(C(K))" "Jung"`, `"F_aleph" "Jung constant" "C(K)"`, and
  `"The separable Jung constant in Banach spaces" "J_aleph"` found the
  source/cited arXiv records and no close exact resolution.

## Scope

This answers the `C(K)` cardinal Jung question stated in the source
paper. It does not address unrelated stability questions about biduals,
ultrapowers, or non-`C(K)` Banach spaces discussed nearby.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: locally compiled copy of the arXiv source paper.
- `supporting_paper_1406.6733.pdf`: cited cardinal-injectivity source used
  for the `F_aleph` characterization.
- `figures/open_problem_crop.png`: crop of the source passage containing the
  question.
