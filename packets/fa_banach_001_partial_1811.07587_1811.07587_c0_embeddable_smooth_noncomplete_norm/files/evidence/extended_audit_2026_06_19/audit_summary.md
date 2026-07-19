# Extended Audit Summary

Date integrated: 2026-06-19

The external audit reported that the active packet's mathematical arguments
for the separable case, the `c0(Gamma)`-injectable case, and the
Markusevich-basis corollary are correct.

The audit also corrected the novelty status: the `c0(Gamma)`-injectable case
already appears in T. Dobrowolski, *Smooth and R-analytic negligibility of
subsets and extension of homeomorphism in Banach spaces*, Studia Math. 65
(1979), Proposition 5.1, via condition (L).

Additional surviving partial results from the audit:

- If `X` has a closed infinite-dimensional separable subspace `Y` such that
  `X/Y` admits a `C^1` smooth equivalent norm, then `X` admits a continuous
  `C^1` smooth non-complete norm.
- In particular, this covers spaces with complemented infinite-dimensional
  separable subspaces.
- A reflexive-subspace route was proposed via an infimal-convolution norm; this
  is included in the packet as likely valid but explicitly marked for human
  review.

The audit and subsequent push did not obtain a full proof or counterexample
for the original `C^1` question. Failed routes included symmetrizing the source
paper's asymmetric functional, trying to build an M-basis from the smooth
duality map, and an actual-normal lemma. A finite-energy normal implication is
false even in a coordinate model on `c0`.
