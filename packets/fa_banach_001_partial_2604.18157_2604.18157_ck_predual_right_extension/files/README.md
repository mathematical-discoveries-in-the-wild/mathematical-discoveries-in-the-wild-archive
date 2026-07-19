# C(K)-Predual Subcase of the Right-Topology Extension Question

Status: `partial_result_likely_valid`

Source paper: Stepan Ondrej and Jiri Spurny, *Operators on injective tensor
products of L1-preduals*, arXiv:2604.18157v1.

## Target

Question 6.7 asks whether Theorem 6.5(b) remains true without assuming that
the `L1`-predual `X` is separable.  In the notation of the paper, if

```text
T : X \hat{\otimes}_epsilon E -> F
```

is strongly bounded and `S:C(B_{X^*},E)->F` is its canonical extension, does
`T` being pseudo weakly compact, respectively Right completely continuous,
imply that `S` has the same property for arbitrary nonseparable `X`?

## Result

Yes for the concrete subclass `X=C(K)`, with `K` an arbitrary compact
Hausdorff space.  No separability or metrizability of `K` is needed.

This is independent of the earlier partial packet
`2604.18157_metrizable_boundary_support_right_extension`: nonmetrizable
compact spaces can carry measures not tight on compact metrizable subsets, so
the present `C(K)` result is not merely a corollary of that support condition.

## Mechanism

For `X=C(K)`, identify `B_{X^*}` with the unit ball of `M(K)`.  There is a
norm-one projection

```text
P : C(B_{M(K)},E) -> A_hom(B_{M(K)},E) = C(K) \hat{\otimes}_epsilon E
```

obtained by taking the homogeneous part on the extreme boundary
`{alpha delta_t : alpha in S_F, t in K}` and extending it affinely:

```text
(P f)(mu) = int_K [ int_{S_F} alpha^{-1} f(alpha delta_t) d alpha ] d mu(t).
```

The source's canonical extension satisfies `S = T P`.  Since bounded operators
preserve Right-null and Right-Cauchy sequences, the pseudo weakly compact and
Right completely continuous properties pass from `T` to `S`.

## Files

- `main.tex`: expert-facing partial proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2604.18157v1.
- `figures/open_problem_crop.png`: crop of Question 6.7 from the source paper.

## Review Notes

The proof hinges on checking that the concrete projection `P` is the
function-side version of the source paper's antihomogeneous boundary
projection `D` in the special case `X=C(K)`.  Once this factorization is
accepted, the Right-topology part is formal.
