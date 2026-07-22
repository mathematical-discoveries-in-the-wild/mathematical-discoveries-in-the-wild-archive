# Verification report

Status: candidate full solution, likely valid.

## Formal audit

1. The source's Remark 2 (arXiv PDF page 3) reduces the CHD constant in an `n`-dimensional space to convex combinations of at most `n` points. This is the only finite-dimensional geometric input.
2. For the centering operator `T_alpha(x)_i = x_i - sum_j alpha_j x_j`, the Hilbert endpoint is the exact variance identity
   `sum alpha_i ||T_alpha(x)_i||_2^2 = sum alpha_i ||x_i||_2^2 - ||sum alpha_i x_i||_2^2`.
3. At the `ell_infinity` endpoint, the triangle inequality gives operator norm at most `C_alpha = 2(1-sum alpha_i^2)` from outer `ell_infinity` to weighted outer `ell_1`.
4. Mixed-norm Riesz-Thorin interpolation with `theta = 1-2/p` gives inner exponent `p` and outer exponent `p'`, since
   `1/p = (1-theta)/2` and `1/p' = (1-theta)/2 + theta`.
5. Hence the weighted `ell_{p'}` mean of the centered distances is at most `C_alpha^theta`; their minimum is no larger.
6. After deleting zero weights, a witness has `k <= n` positive weights. Cauchy-Schwarz gives `sum alpha_i^2 >= 1/k >= 1/n`, producing exactly `(2(n-1)/n)^(1-2/p)`.
7. For `p>2`, `|1/p-1/p'| = 1-2/p`, so this is precisely inequality (10) from the source.

## Computational stress test

`code/check_mixed_norm_bound.py` samples finite convex combinations across several dimensions and values of `p`. The development run used seed `150102596`, dimensions `2,3,4,6`, all `2 <= k <= n`, six values of `p`, and 20,000 samples per parameter triple. The largest ratio of left side to proved right side was approximately `0.9999999316`, near the two-point equality family.

This computation is not used in the proof.

## Novelty audit

The run indexes, local arXiv corpus, exact-title and keyword arXiv/web searches, and the author's later related arXiv paper 1904.06729 were checked through 22 July 2026. No explicit resolution of Question 1 was located. Novelty confidence: moderate.

## Human-review focus

- Confirm the standard interpolation identity for the two finite weighted mixed-norm couples.
- Confirm that the source's Remark 2 indeed supplies an at-most-`n`-point witness inside the unit ball.
- Perform a specialist citation search for an implicit interpolation proof of this exact CHD estimate.
