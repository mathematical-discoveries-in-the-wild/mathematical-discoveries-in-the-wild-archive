# Partial Result: One-Dimensional Holder Border Classification

Status: `companion_partial_result_likely_valid`

Packet placement: bundled under
`solutions/full/2312.14711_bounded_kernel_endpoint_all_dimensions/companion_partial_results/`
as a companion partial result to the promoted all-dimensional bounded-kernel
endpoint packet.

Source paper: Max Scholpple and Ingo Steinwart, "Which Spaces can be Embedded in Reproducing Kernel Hilbert Spaces?", arXiv:2312.14711.

## Result

The source proves that for Holder spaces on bounded subsets of `R^d`, an RKHS
sandwich

```text
Hol^alpha(X) -> H -> Hol^beta(X)
```

is impossible when `alpha - beta < d/2`, and that a bounded-kernel sandwich
`Hol^alpha(X) -> H -> ell_infty(X)` is impossible when `alpha < d/2`. It then
states that these bounds are tight up to the border cases.

This packet gives a one-dimensional classification of the first-order Holder
border cases:

- If `0 < beta < 1/2` and `alpha = beta + 1/2`, there is no RKHS `H` on
  `[0,1]` with `Hol^alpha([0,1]) -> H -> Hol^beta([0,1])`.
- There is no bounded-kernel RKHS `H` on `[0,1]` with
  `Hol^{1/2}([0,1]) -> H -> ell_infty([0,1])`.
- The remaining one-dimensional Lipschitz endpoint is positive:
  `Hol^1([0,1]) -> H^1([0,1]) -> Hol^{1/2}([0,1])`, and `H^1([0,1])`
  is a bounded-kernel RKHS.

## Proof Mechanism

The source's one-scale packing argument is sharp at the border. The new
ingredient is to use all dyadic scales at once. Dyadic tent functions of height
`2^{-j alpha}` have uniformly bounded `alpha`-Holder Rademacher sums when
`alpha < 1`, but their `beta`-Holder norms contribute a fixed amount to the
target `ell_2` sequence norm at every scale when `alpha - beta = 1/2`.
Consequently the cotype-2 constant of the inclusion grows like `sqrt(m)` over
the first `m` scales. Since every RKHS sandwich would make the inclusion
2-factorable, and hence cotype 2, this is impossible. The endpoint
`alpha=1`, `beta=1/2` escapes exactly because Lipschitz functions on an
interval are absolutely continuous with bounded derivative, so the classical
Sobolev RKHS `H^1([0,1])` sits between `Hol^1` and `Hol^{1/2}` by
Cauchy-Schwarz.

## Relation to the Bounded-Kernel Endpoint

This packet itself is focused on the one-dimensional first-order border. The
parent lane-7 packet settles the bounded-kernel endpoint negatively in every
dimension:

```text
solutions/full/2312.14711_bounded_kernel_endpoint_all_dimensions/
```

The higher-smoothness Besov/Triebel border cases discussed later in the source
paper remain outside this packet.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2312.14711.
- `figures/open_problem_crop.png`: source crop showing Theorem 12 and the
  border-case sentence.

## Novelty Check

Before the original promotion, the cheap run indexes were searched for arXiv id
`2312.14711`, title keywords, `RKHS`, `Holder`, `Hölder`, `border cases`,
`alpha=d/2`, and `2-factorable`; no duplicate packet or attempt was found.
Bounded web searches for the source title plus `border cases`, `Holder spaces
2-factorable RKHS`, and `C^{1/2} RKHS bounded kernel` found the source arXiv
record but no separate answer to this border case.

For this upgrade, the direct literature pass additionally checked nearby RKHS
regularity, Sobolev-RKHS, and all-continuous-function obstruction papers. These
provided context and sanity checks, but the one-dimensional positive endpoint
uses only the elementary Sobolev embedding argument written in the packet.

## Human Review Recommendation

Review the dyadic tent-function lemma, especially the uniform
`alpha`-Holder bound for signed sums when `alpha < 1`, and confirm that the
cotype-2 obstruction is applied with the same conventions as the source paper.
Also verify the endpoint embedding
`Hol^1([0,1]) -> H^1([0,1]) -> Hol^{1/2}([0,1])`; it is short, but it is the
piece that turns the previous non-Lipschitz obstruction into a clean
one-dimensional border classification.
