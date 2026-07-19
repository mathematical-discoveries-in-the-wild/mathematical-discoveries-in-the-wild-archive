# Partial Result: An `\ell_1`-Sum Obstruction To Property `D(s,c_1)`

Status: `historical_partial_superseded_by_full`

This packet has been packed into the full result
`solutions/full/1909.13536_nonuniform_smooth_D_property_positive_example/`.
It is kept here only as historical context for the successful positive answer.

Source paper: S. Dilworth, G. Garrigos, E. Hernandez, D. Kutzarova, and V. Temlyakov, *Lebesgue-type inequalities in greedy approximation*, arXiv:1909.13536.

## Source Question

Remark 2.11 of the source paper asks whether property `D(s,c_1)` could hold for some non-uniformly smooth Banach space and some dictionary. The property requires

```tex
dist(f,[\varphi]) <= ||f|| (1 - c_1 |F_f(\varphi)|^s)
```

for all nonzero `f` and all dictionary atoms `\varphi`, where `F_f` is an associated norming functional.

## Result

This packet proves a partial negative result: no nontrivial `\ell_1` direct sum `E \oplus_1 F` can have property `D(s,c)` with respect to any nonempty dictionary, for any `s>1` and `c>0`.

In fact, every unit vector `\varphi` in `E \oplus_1 F` fails the required one-atom inequality. Thus the common attempt to obtain a non-uniformly smooth example by hiding a nonsmooth `\ell_1` sum component cannot work.

## Scope

This does not fully answer Remark 2.11. It rules out a broad and natural class of non-uniformly smooth Banach spaces, namely nontrivial `\ell_1` sums and spaces whose proposed construction reduces to such an atom-level obstruction. Other non-uniformly smooth norms or very thin dictionaries remain possible.

## Verification Notes

- The proof is elementary and uses only the geometry of `E \oplus_1 F`.
- The obstruction is independent of the choice of norming functional selection: the test vectors force every norming functional to take value `1` on the chosen atom.
- A source-question crop is included at `figures/open_problem_crop.png`.
- Bounded novelty check: the run indexes were searched for `1909.13536`, `Lebesgue-type inequalities`, `D(s,c_1)`, `non-uniformly smooth`, and related greedy-approximation terms. Web search surfaced the source arXiv page but no later exact answer; Semantic Scholar API was rate-limited during citation probing.

## Human Review Recommendation

Check the two-distance minimization in the proof, especially the complex-scalar case. The result is intended as a partial obstruction, not as a complete answer to Remark 2.11.
