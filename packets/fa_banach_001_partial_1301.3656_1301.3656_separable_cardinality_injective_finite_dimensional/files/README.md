# Partial packet: separable cardinality-injective spaces are finite-dimensional

status: partial_result

source: Lingxin Bao, Lixin Cheng, Qingjin Cheng, and Duanxu Dai,
*On universal left-stability of epsilon-isometries*, arXiv:1301.3656.

target: Remark 3.6 asks whether every cardinality injective Banach space is
injective, beyond the dual-space case proved in the source.

packet: `runs/fa_banach_001/solutions/partial/1301.3656_separable_cardinality_injective_finite_dimensional/`

## Result

This packet proves the separable case of the source question.

If `X` is separable and cardinality injective in the sense of the source
paper, then `X` is finite-dimensional. In particular, every separable
cardinality injective Banach space is injective in the source's bounded
extension sense.

## Proof Mechanism

If `X` is infinite-dimensional and separable, then every separable superspace
`Y` has the same cardinality as `X`, namely the continuum. Cardinality
injectivity therefore makes `X` separably injective. Zippin's theorem then
forces `X` to be isomorphic to `c_0`. Cardinality injectivity is invariant
under isomorphism by Proposition 3.2 of the source paper, so `c_0` would be
cardinality injective. But `c_0` sits isometrically in `ell_infty`, the two
spaces have the same cardinality, and Phillips' theorem says that `c_0` is
not complemented in `ell_infty`. This contradiction rules out the infinite
separable case.

Finite-dimensional spaces are injective in the source's sense by the usual
Auerbach-basis/Hahn-Banach projection argument.

## Verification

- Cheap run indexes were searched for `1301.3656`, `cardinality injective`,
  `universally left-stable`, and related epsilon-isometry keywords.
- The exact arXiv id had no prior promoted packet in the run.
- A neighboring attempt for arXiv:1301.3396 was inspected; it concerns broader
  epsilon-isometry stability questions and does not cover this final
  cardinality-injective problem.
- Local source `2605.06003` was inspected; it cites the same cardinality
  injective condition but does not answer the source question.
- Web searches for exact phrases around `cardinality injective Banach space
  injective` found the source paper and no later exact resolution during this
  pass.

## Scope

This is not a full solution of Remark 3.6. The nonseparable case remains open
in this packet.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of Remark 3.6 in the source paper.
