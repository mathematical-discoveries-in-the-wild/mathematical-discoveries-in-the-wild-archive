# Extreme non-McCann barycenter in infinite-dimensional Gaussian OT

Status: `counterexample_likely_valid`

Source paper: Ho Yun and Yoav Zemel, *Gaussian Optimal Transport Beyond
Brenier's Theorem*, arXiv:2512.21464.

## Result

The packet gives a counterexample to the infinite-dimensional converse left
open on PDF page 38 of the source paper: not every extreme point of the
Gaussian barycenter set `K_t(A,B)` is a McCann interpolant.

The construction takes `H = H_1 \oplus H_2`, with both summands copies of
`ell_2`.  The covariance `A` is injective trace class on `H_1` and zero on
`H_2`.  The covariance `B` is block diagonal: its `H_1` block vanishes on an
infinite-dimensional odd-coordinate subspace `K`, and its Schur complement
`B/A` is an injective trace-class covariance on `H_2`.

The source parametrizes the barycenter set by operators

```text
N : H_2 -> H_1,   range(N) subset K,   N^* N <= B/A.
```

The counterexample chooses `N = W (B/A)^{1/2}` where `W : H_2 -> K` is a
coisometry that is not an isometry.  Such a `W` is an extreme contraction, so
the associated `N` and barycenter are extreme.  But
`N^* N < B/A`, hence the source's own Schur-complement criterion says that the
barycenter is not McCann.

## Files

- `main.tex`: self-contained counterexample packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: full-page evidence image from source PDF
  page 38, showing the open converse and Proposition 6.12 context.

## Verification

No numerical computation is used.  The verification is operator-theoretic:

- `A` and `B` are positive trace-class covariance operators.
- `A \leadsto B` holds because the Schur-complement support and the defect
  space are both infinite-dimensional separable Hilbert spaces.
- The coisometry `W` is proved directly to be an extreme contraction.
- Since `(B/A)^{1/2}` has dense range, extremality transfers from `W` to
  `N = W(B/A)^{1/2}`.
- The source's affine parametrization transfers extremality from `N` to the
  barycenter.
- `N^*N != B/A`, so the barycenter is not a McCann interpolant.

## Novelty Check

Cheap run indexes were searched for `2512.21464`, the source title, `Gaussian
optimal transport`, `Brenier`, `Bures-Wasserstein`, `McCann interpolant`, and
`extreme geodesics`.  No exact packet for this source or converse was found.
Bounded web search for the exact arXiv id, title, `McCann`, and `extreme`
surfaced the source paper and mirrors only, not a later resolution.
