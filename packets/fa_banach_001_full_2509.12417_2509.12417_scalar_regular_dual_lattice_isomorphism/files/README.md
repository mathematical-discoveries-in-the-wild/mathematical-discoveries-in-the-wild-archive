# Scalar regular polynomial lattices under dual lattice isomorphism

Status: `full_result_likely_valid`

Source target: Christopher Boyd and Vinicius C. C. Miranda, *Lattice isomorphic Banach lattices of polynomials*, arXiv:2509.12417.

## Result

The source paper asks, in scalar form:

> Given two dual isomorphic Banach lattices `E` and `F`, that is `E^*` and
> `F^*` are lattice isomorphic, under which conditions are `P^r(^n E)` and
> `P^r(^n F)` lattice isomorphic for every `n in N`?

This packet gives the strongest possible scalar answer:

> If `E^*` and `F^*` are lattice isomorphic Banach lattices, then for every
> `n >= 1`, the Banach lattices `P^r(^n E)` and `P^r(^n F)` of scalar-valued
> regular `n`-homogeneous polynomials are lattice isomorphic.

Thus no extra order-continuity hypothesis is needed in the scalar-valued
regular-polynomial question. This upgrades the earlier orthogonally additive
partial packet for the same target.

## Idea

The source proof uses the whole bidual and therefore assumes that the dual norm
is order continuous. For the scalar problem, it is enough to work on the
order-continuous bidual band

`E^diamond = (E^*)_n^*`.

For any scalar regular multilinear form `A`, all Arens extensions restrict to
separately order-continuous multilinear forms on `(E^diamond)^n`. They agree on
the order-dense canonical copy of `E`, so they agree on all of `(E^diamond)^n`.
Consequently a symmetric regular form has a canonical symmetric regular
extension `A^diamond` to the order-continuous bidual band.

Given a lattice isomorphism `phi:E^* -> F^*`, the adjoint `phi^*` maps
`F^diamond` onto `E^diamond`. Transfer a polynomial `P`, with associated form
`A`, by

`Psi_phi(P)(y) = A^diamond(phi^* J_F y, ..., phi^* J_F y)`.

The same order-density argument gives the functorial identity on
`F^diamond`, so `Psi_{phi^{-1}}` is the inverse of `Psi_phi`. Positivity is
preserved because Arens extensions of positive regular multilinear forms are
positive.

## Scope

This is a full answer to the extracted scalar question in the source passage.
It does not claim the corresponding vector-valued `G^*` theorem without the
source paper's order-continuity assumptions, nor does it settle the classical
Banach-space Díaz-Dineen problem for arbitrary linear dual isomorphisms.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: rendered source arXiv paper from the local TeX source.
- `figures/open_problem_crop.png`: source passage around the extracted question.
- `code/make_open_problem_crop.py`: reproducible crop script.

## Novelty Check

Before the full upgrade, the cheap run indexes were searched for `2509.12417`,
the exact title, `dual lattice isomorphic`, `scalar regular polynomials`,
`order-continuous bidual`, and close polynomial-lattice phrases. The only
existing run hit was the earlier scalar orthogonally additive partial packet
created by this lane, now upgraded. A bounded web search on 2026-06-29 for
the exact source title and close variants of `regular homogeneous polynomials`,
`dual lattice isomorphic`, and `order continuous bidual` surfaced the source
paper itself and no exact duplicate of this scalar upgrade.

## Human Review Recommendation

Review the order-density lemma: separately order-continuous Arens-side forms
that agree on `J_E(E)^n` are identified on `(E^*)_n^*`. This is standard
Fremlin/Buskes-Roberts order-bidual machinery, and it is the key step that
removes the source paper's order-continuous-dual hypothesis in the scalar case.
