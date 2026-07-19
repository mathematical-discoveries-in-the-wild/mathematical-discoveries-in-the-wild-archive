# Papathanasiou generators are not C*-minimal

Status: `full_result_likely_valid`

Source target: Willian Franca and Jorge J. Garces, *Applications of compact multipliers to algebrability of `(ell_infty \ c_0) union {0}` and `(B(ell_2(N)) \ K(ell_2(N))) union {0}`*, arXiv:2508.19174v1.

## Result

The source paper says, in Section 4 after constructing a copy `A_3` of `ell_infty` inside `(ell_infty \ c_0) union {0}`:

> Although it is even possible to find a dense subalgebra of `A_3` as in [D.P], we do not know if that system of generators is minimal when generating `ell_infty` (or `A_3`) as a C*-algebra.

This packet gives a negative answer for the generator system supplied by Papathanasiou's construction. If

`H = { h_(A,j) : A subset N, j in N }`

is the family used in arXiv:2102.03199, then for every one generator `h_(A0,j0)`,

`C*(H \ {h_(A0,j0)}) = ell_infty`.

Thus `H` is not a minimal C*-generating system for `ell_infty`; after applying any *-isomorphism `ell_infty -> A_3`, its image is not minimal for `A_3` either.

## Idea

Papathanasiou makes the algebra dense by including, for every subset `A` of `N`, a whole sequence of perturbations `h_(A,j)` with `h_(A,j) -> chi_A`. Deleting one element leaves the tail for the same `A`. Hence every characteristic function `chi_A` is still in the C*-closure of the remaining family. Characteristic functions of subsets of `N` uniformly generate all finite-valued bounded sequences, and finite-valued bounded sequences are dense in `ell_infty`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: rendered source arXiv paper from the local TeX source.
- `supporting_paper_2102.03199.pdf`: rendered Papathanasiou source paper from the local TeX source.
- `figures/open_problem_crop.png`: source passage around the extracted question.
- `code/make_open_problem_crop.py`: reproducible crop script.

## Novelty Check

The run indexes were searched for `2508.19174`, the paper title, `compact multipliers`, `algebrability`, `Papathanasiou`, `dense subalgebra`, and generator-minimality phrases. No exact prior packet was found. A bounded web search on 2026-07-01 for the exact source sentence, the source title, and close phrases involving Papathanasiou, `ell_infty \ c_0`, minimal generators, and C*-algebras did not surface an exact duplicate answer in the returned snippets.

## Human Review Recommendation

Review the quantifier match with Papathanasiou's family: the argument uses the fact that the cited dense strongly `c`-algebrable construction has generators indexed by `(A,j)` and satisfies `||h_(A,j)-chi_A|| <= 1/j`. Once that is confirmed, the non-minimality proof is immediate.
