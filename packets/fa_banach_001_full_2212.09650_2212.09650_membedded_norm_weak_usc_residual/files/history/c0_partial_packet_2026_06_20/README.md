# Partial Result: Category-Large Norm-Weak USC Points in `c0**`

Status: `partial_result_likely_valid`

Source paper: T. S. S. R. K. Rao, "Computing sub differential limits of operators on Banach spaces", arXiv:2212.09650.

Source question: after Proposition 9, the paper says:

> We do not know how to determine the largeness of points of norm-weak usc for the preduality map on `X**` in the category sense, when `X` is a `M`-ideal in its bidual.

## Result

For the prototypical non-reflexive M-embedded space `X=c0`, the norm-weak upper-semicontinuity points for the preduality map on `X** = ell_infty` are residual. More precisely, they contain the dense open set of all real bounded sequences `a` whose supremum norm is attained with a strict gap:

```text
max |a_n| > sup { |a_n| : |a_n| < max |a_k| }.
```

This gives a positive category-largeness answer for `c0`.

## Idea

Identify `ell_infty` with `C(beta N)` and `ell_infty*` with the regular measures on `beta N`. If `a in ell_infty` has a strict maximum plateau, then the points of `beta N` where the continuous extension of `a` has norm value are exactly the Stone-Cech closures of the coordinate sets where `a_n = ||a||` or `a_n = -||a||`. Atomic probability measures on a dense subset of a compact space are weak-star dense in all probability measures on that compact space. Therefore the `ell_1` state space of `a` is weak-star dense in the full `ba(N)` state space of `a`, which is exactly norm-weak usc by the source paper's criterion.

The strict-maximum-plateau sequences form a dense open subset of `ell_infty`: any bounded sequence can be perturbed by an arbitrarily small spike in one coordinate.

## Scope

This does not solve the source question for all Banach spaces that are M-ideals in their biduals. It gives a complete Baire-category positive answer for the central example `c0`.

## Evidence

- Source definition/criterion: arXiv:2212.09650, Introduction, page 3.
- Source category question: arXiv:2212.09650, page 9, before Proposition 9.
- Local source search found no exact prior packet for arXiv:2212.09650.
- Web searches for `"norm-weak usc" "c0" "preduality map"`, `"norm-to-weak upper semi-continuity" "duality" "c0"`, and related exact phrases did not find a pre-existing resolution of this `c0` category subcase.

Local files:

- `source_paper.pdf`
- `figures/definition_context_page3.png`
- `figures/open_problem_context_page9.png`
- `solution_packet.pdf`
