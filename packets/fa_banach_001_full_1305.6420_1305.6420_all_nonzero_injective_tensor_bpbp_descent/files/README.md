# Full qualitative result: every nonzero injective tensor factor descends BPBp

Status: `full_solution_likely_valid` for the qualitative BPBp descent question.

Source paper: Richard Aron, Yun Sung Choi, Sun Kwang Kim, Han Ju Lee, and Miguel Martin, *The Bishop-Phelps-Bollobas version of Lindenstrauss properties A and B*, arXiv:1305.6420.

## Target

After Proposition 2.8, the source paper observes that if
`(X, C(K) \hat{\otimes}_\epsilon Y)` has the Bishop-Phelps-Bollobas property
with a function `eta`, then `(X,Y)` has the BPBp with the same function, and
asks what other spaces besides `C(K)` have this property.

## Result

Let `E` be any nonzero Banach space. For all Banach spaces `X` and `Y`, if
`(X, E \hat{\otimes}_\epsilon Y)` has the BPBp, then `(X,Y)` has the BPBp.
Quantitatively, if `(X, E \hat{\otimes}_\epsilon Y)` has BPBp modulus `eta`,
then `(X,Y)` has BPBp modulus `epsilon -> eta(epsilon/2)`.

This answers the qualitative descent problem for every possible nonzero
injective tensor factor `E`.

## Same-modulus refinement

The earlier stronger-modulus result remains useful: if `E` has a state-norming
unit, equivalently a spear-vector style unit / isometric closed unital
`C(K)`-subspace representation, then the descent holds with the same modulus
`eta(epsilon)`. For arbitrary nonzero `E`, the proof currently gives a factor-2
loss in the modulus.

## Proof idea

Choose `e in S_E` and embed `Y` into `E \hat{\otimes}_\epsilon Y` by
`y -> e \otimes y`. Represent `E \hat{\otimes}_\epsilon Y` inside
`C(B_{E^*},Y)`. A norm-attaining approximant into the tensor product has a
value function that attains its norm at some `e_1^* in B_{E^*}`. Since the
approximant is close to `e \otimes T`, the scalar `alpha=e_1^*(e)` must satisfy
`|alpha|` close to one. Evaluation at `e_1^*`, followed by a scalar rotation,
gives a norm-attaining operator into `Y`; the closeness error is the tensor
approximation error plus `1-|alpha|`.

## Novelty check

Cheap run indexes had no exact entry for arXiv:1305.6420 or this all-nonzero
tensor-factor formulation. Web/literature search found the later related
preprint arXiv:2506.17762, which proves a `C_0(L,Y)` descent theorem and
related stability statements, but the downloaded source inspected here did not
state this all-nonzero injective-tensor descent theorem. Spear-vector
terminology and the same-modulus refinement were checked against
arXiv:1701.02977.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local source paper PDF.
- `figures/open_problem_crop.png`: source crop showing the open question.
- `history/`: archived partial and strong-partial packets superseded by this
  full result.
