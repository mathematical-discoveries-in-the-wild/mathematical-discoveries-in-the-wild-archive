# Partial clarification of the operator alpha-ratio/Reiter problems

Status: `partial_result_likely_valid_needs_human_review`

Source paper: arXiv:1701.05537, Nicolas Monod, *Fixed points in convex
cones*.

## Claim

Problems 47 and 48 ask to clarify when the operator `alpha`-ratio and
operator `alpha`-Reiter properties hold for unitary representations on Hilbert
space.

This packet proves:

- The operator `alpha`-ratio property is automatic for every unitary
  representation and every bounded non-zero operator `alpha`. Thus the ratio
  half of Problems 47/48 does not impose a real condition as stated.
- The operator `alpha`-Reiter property is exactly absence of an
  `alpha`-spectral gap:

```text
sum_{s in S} ||alpha(pi(s)v - v)||^2 >= c ||alpha v||^2 for all v
```

  must fail for every finite `S` and every `c>0`.
- If `alpha` is bounded below, `alpha`-Reiter is equivalent to the ordinary
  existence of almost invariant vectors for the representation.
- For a finite-rank orthogonal projection `P`, `P`-Reiter is equivalent to an
  exact finite-dimensional linear condition: for each finite `S` there is
  `v` with `Pv != 0` and `P(pi(s)v - v)=0` for all `s in S`.

## Key mechanism

The ratio property only compares `||alpha pi(s)v||` with `||alpha v||`.
Choosing `v` almost norm-attaining for `alpha` makes every numerator at most
`||alpha||`, hence less than `(1+epsilon)||alpha v||`.

For Reiter, all content is in the quadratic form
`A_S = sum (pi(s)-I)^* alpha^* alpha (pi(s)-I)` relative to
`B = alpha^* alpha`. The property says precisely that the generalized
Rayleigh quotient of `A_S` relative to `B` has infimum zero for every finite
`S`.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_problem_crop.png` - crop containing Problems 47 and 48.
- `code/crop_open_problem.py` - script used to create the crop.

## Novelty check

The local run indexes were searched for arXiv:1701.05537 and the terms
`operator alpha-ratio`, `operator alpha-Reiter`, `fixed points in convex cones`,
and `conical fixed-point property`; no existing packet for this endpoint was
found. Web searches for exact phrases such as `"operator alpha-ratio"`,
`"operator alpha-Reiter"`, and variants with `Fixed points in convex cones`
returned the source context but no later explicit solution of Problems 47/48.

This is intentionally filed as a partial result: it settles the ratio side and
gives sharp Reiter criteria, but it does not solve the broader group-theoretic
questions about products, supramenability, or finding finitely generated
exponential-growth examples with the fixed-point property for cones.
