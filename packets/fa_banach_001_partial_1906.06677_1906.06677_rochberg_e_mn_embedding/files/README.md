# Rochberg \(E_{m,n}\) embeddings

Status: `partial_result_likely_valid`

Source target: Felix Cabello Sanchez, Jesus M. F. Castillo, and Willian H. G. Correa, *Higher order derivatives of analytic families of Banach spaces*, arXiv:1906.06677.

## Result

The source paper defines natural maps

```text
E_{m,n}: F_z^{(m+n-1)} -> F[m,n]
```

from the ordinary Rochberg space of order `m+n-1` into the `n`-th Rochberg space of the analytic family of order-`m` Rochberg spaces. It proves the complemented-range statement when `m=2` or `n=2`, then records that it is not even known whether `E_{3,3}` is an embedding or whether `F[3,3]` contains a subspace isomorphic to `F_z^{(5)}`.

This packet proves the embedding half for all `m,n` and also identifies the quotient:

> For every acceptable analytic-function space `F`, base point `z`, and integers `m,n >= 1`, the natural map `E_{m,n}` is an isomorphic embedding. For `m,n >= 2`, the quotient `F[m,n] / E_{m,n}(F_z^(m+n-1))` is naturally isomorphic to `F[m-1,n-1]`. In particular, `F[3,3]` contains a closed subspace isomorphic to `F_z^(5)`.

## Scope

This does not prove the remaining complemented-range assertion. The quotient is identified by a bounded first-order defect map, but no bounded linear section of that quotient map is claimed.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: source passage around the extracted open question, if rendering tools are available.

## Novelty check

The run indexes were searched for `1906.06677`, the source title, `Rochberg`, `E_{3,3}`, `F[3,3]`, `F[m,n]`, `centralizer`, `differential process`, and related complex interpolation phrases. Web searches for the exact `E_{3,3}`/`F[3,3]` Rochberg phrases found only the source paper or unrelated material. Existing run work on arXiv:1406.6723 covers a different reciprocal centralizer question, not this embedding lemma.

Human review should focus on the commutative exact diagram used in the embedding induction, the first-order defect map `c_j'-(j+1)c_{j+1}`, and the finite jet exactness argument identifying its kernel with the image of `E_{m,n}`.
