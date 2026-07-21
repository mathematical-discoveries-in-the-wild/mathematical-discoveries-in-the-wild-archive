# Full result: a contractible counterexample of infinite type

status: `full_solution_likely_valid`

source: Hiroshi Ando, Yasumichi Matsuzawa, Andreas Thom, and Asger
Törnquist, *Unitarizability, Maurey--Nikishin factorization, and Polish
groups of finite type*, arXiv:1605.06909v3.

target: Question 4.5 asks whether there is a connected, unitarily
representable SIN Polish group which is not of finite type.

## Result

Yes; in fact there is a contractible example. Let `G_0` be any
unitarily representable SIN Polish group which is not of finite type, such
as the semidirect-product example supplied by the source from a uniformly
bounded non-unitarizable representation. Then

`L^0([0,1],G_0)`

with pointwise multiplication and convergence in measure is a contractible,
unitarily representable SIN Polish group which is not of finite type.

## Proof idea

- A bounded bi-invariant metric on `G_0` integrates to a bi-invariant
  convergence-in-measure metric on `L^0`, so the new group is Polish and SIN.
- Cutting a measurable function off on a terminal interval gives an explicit
  contraction to the identity.
- A faithful strong-operator representation of `G_0` acts pointwise by
  multiplication on `L^2([0,1],H)`. Testing on constant vector fields proves
  that this is a topological embedding of the convergence-in-measure group.
- Constant functions form a closed subgroup isomorphic to `G_0`. Finite type
  passes to closed subgroups, so the `L^0` group cannot be of finite type.

## Verification and novelty

- The current source is v3 and still contains the question.
- Cheap run indexes contained no prior result for arXiv:1605.06909.
- Bounded searches for the exact question and for `L^0` measurable-function
  groups found the source and general work on `L^0(G)`, but no stated answer
  to the finite-type question.
- The proof is self-contained apart from the source's existence of `G_0` and
  standard elementary facts about convergence-in-measure groups.

## Files

- `main.tex` / `solution_packet.pdf`: full proof and scope statement.
- `source_paper.pdf`: official arXiv v3 PDF.

