# Full Endpoint Solution: No Bounded-Kernel RKHS at the Critical Holder Endpoint in Any Dimension

Status: `full_bounded_kernel_endpoint_solution_likely_valid`

Source paper: Max Scholpple and Ingo Steinwart, "Which Spaces can be Embedded in Reproducing Kernel Hilbert Spaces?", arXiv:2312.14711.

## Result

The source proves that a bounded-kernel RKHS sandwich

```text
Hol^alpha(X) -> H -> ell_infty(X)
```

is impossible when `alpha < d/2`, and it leaves the endpoint `alpha=d/2`
as a border case. This packet proves the critical endpoint is also impossible
on cubes in every dimension:

```text
For every d >= 1, there is no bounded-kernel RKHS H on [0,1]^d with
Hol^{d/2}([0,1]^d) -> H -> ell_infty([0,1]^d).
```

For non-integer `d/2`, this is the usual classical Holder class. At integer
endpoints, the proof applies to the standard endpoint conventions used in this
area, including Lipschitz at smoothness 1, classical `C^k`, `C^{k-1,1}`, and
Holder-Zygmund/Besov `B^k_{infty,infty}` versions.

## Proof Mechanism

The proof uses only Fourier characters. If such a sandwich exists, each
periodic character

```text
e_m(x)=exp(2 pi i m.x),  m in Z^d
```

has a Hilbert feature vector. For a finite frequency set, project the bounded
evaluation vectors onto the span of those feature vectors. Vector-valued
Bessel/Parseval gives

```text
sum_m ||u_m||^2 <= constant.
```

But reproducing `e_m`, together with the critical norm estimate

```text
||e_m||_{Hol^{d/2}} <= C (1+|m|)^{d/2},
```

forces

```text
||u_m|| >= c (1+|m|)^{-d/2}.
```

Thus the finite sums of `(1+|m|)^{-d}` over `Z^d \ {0}` would be uniformly
bounded, contradicting the critical lattice-sum divergence.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2312.14711.
- `figures/open_problem_crop.png`: source crop showing Theorem 12 and the
  border-case sentence.
- `companion_partial_results/2312.14711_holder_border_no_rkhs/`: related
  one-dimensional Holder-to-Holder border classification packet. This remains
  a companion partial result for the broader Holder-to-Holder problem.

## Companion Results

The bundled companion packet records the earlier one-dimensional
Holder-to-Holder classification. The promoted full result here is the
all-dimensional bounded-kernel endpoint theorem; it does not classify every
Holder-to-Holder endpoint `Hol^alpha -> H -> Hol^beta` with
`alpha - beta = d/2`.

## Novelty Check

The local run indexes were searched for arXiv id `2312.14711`, `Hol^d/2`,
`alpha=d/2`, `bounded-kernel`, `Holder-Zygmund`, `B_{infty,infty}^{d/2}`, and
`Hilbert factorization`. The exact hits were the earlier two-dimensional packet,
the bundled one-dimensional companion packet, and the superseded attempt note.

Bounded web searches for the source title plus `border`, for `bounded-kernel
RKHS alpha=d/2 Holder`, for `Holder-Zygmund d/2 RKHS`, and for
`B_{infty,infty}^{d/2} RKHS bounded kernel` found the source arXiv record but
no exact later answer to this endpoint.

## Human Review Recommendation

Review the finite character lemma. The key checks are: bounded point
evaluations give the Bessel upper bound, the Fourier coefficient convention is
correct, and the chosen endpoint Holder norm has the stated character growth
`||e_m|| <= C(1+|m|)^{d/2}`.
