# Partial Result: Better Bounds for the Midpoint Constant

## Source Question

- Source paper: Rafal Gorak, *Perturbations of isometries between Banach spaces*, arXiv:1105.0854.
- Location: Section 4, "Final remarks", page 11.
- Question: determine the exact value of the asymptotic midpoint constant
  `K = limsup_{epsilon -> 0} K_epsilon`, where `K_epsilon` is the supremum of
  the normalized midpoint defect over all `mu`-isometries with
  `mu(t)=(1+epsilon)t`.

The source records the bounds `0.5 <= K <= 3`.

## Result

This packet improves the source bounds to

```text
1 <= K <= exp(sqrt(2))/sqrt(2) < 3.
```

The lower bound comes from a concrete nonlinear shear on the Hilbert plane:

```text
T(s,t) = (s + eta |t|, t),   eta = M - M^{-1},   M=1+epsilon.
```

This map is an `M`-bi-Lipschitz bijection, hence a `mu`-isometry for
`mu(t)=Mt`, and its midpoint defect gives
`K_epsilon >= (M+1)/(2M)`, so `K >= 1`.

## Files

- `main.tex`: partial-result packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source open problem.
- `code/check_midpoint_bounds.py`: numerical/symbolic sanity check.

## Review Focus

Review should check the global bi-Lipschitz estimate for the shear. The key
observation is that every difference is acted on by a matrix
`[[1,a],[0,1]]` with `|a| <= eta`, whose Euclidean operator norm is at most
`M` when `eta=M-M^{-1}`.
