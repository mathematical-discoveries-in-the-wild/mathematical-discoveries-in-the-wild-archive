# Internal appendix: six-dimensional values of `dim Z(X)`

Source paper: arXiv:math/0605781, *Recent progress and open questions on the
numerical index of Banach spaces*.

Result type: candidate partial answer to the general Problem 27, solving the
six-dimensional subcase.

Canonical packet: `solutions/full/0605781_dim_zx_five_classification/`.
This file is an internal appendix to that packet, not a separate indexed
solution packet.

## Target

Problem 27 asks for the possible values of the Lie-algebra dimension
`\dim Z(X)` for an `n`-dimensional real Banach space `X`. The source paper says
the cases `n=3,4` were known and that the first open case was `n=5`.

After the run's existing five-dimensional packet, the next subcase is `n=6`.

## Packet result

If `X` is a six-dimensional real Banach space, then

```text
dim Z(X) in {0, 1, 2, 3, 4, 6, 7, 10, 15}.
```

Conversely, every value in this set is attained.

Rosenthal's gap theorem leaves only `5,8,9` to exclude below the Hilbert value
`15`. The packet excludes them by a compact Lie algebra and representation
analysis inside `so(6)`:

- dimension `5` forces an `su(2)+R^2` action. The only faithful six-dimensional
  orthogonal possibility has a `4+2` splitting; invariance under the action
  automatically enlarges the Lie algebra to `so(4)+so(2)`, dimension `7`.
- dimension `8` forces the standard real representation of `su(3)` on `C^3`,
  which is sphere-transitive, so any invariant norm is Euclidean and the Lie
  algebra enlarges to `so(6)`.
- dimension `9` either reduces to impossible `su(2)`-factor representations or
  to `u(3)` on `C^3`, again sphere-transitive and hence Euclidean.

The remaining values are realized by `ell_infty`-sums of Euclidean blocks:

```text
0:  ell_infty^6
1:  H_2 +_infty ell_infty^4
2:  H_2 +_infty H_2 +_infty ell_infty^2
3:  H_3 +_infty ell_infty^3
4:  H_3 +_infty H_2 +_infty R
6:  H_4 +_infty ell_infty^2
7:  H_4 +_infty H_2
10: H_5 +_infty R
15: H_6
```

## Files

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop of the source problem
  context.
- `code/check_six_dimension_values.py`: sanity script for construction values
  and Rosenthal's remaining finite exclusion list.

## Novelty Check

Bounded local search over the parsed corpus and run artifacts found only the
source problem, the five-dimensional packet, and adjacent numerical-index
material. Bounded web searches on 2026-06-13 for exact phrases around
`dim Z(X)`, `six-dimensional real Banach space`, `skew-hermitian`, and
Rosenthal's Lie algebra paper found no direct later classification.

## Human Review Focus

Check the representation-theoretic exclusions of compact subalgebras of
`so(6)` of dimensions `5`, `8`, and `9`, especially the automatic enlargement
from `su(2)+R^2` on a `4+2` decomposition to `so(4)+so(2)`.
