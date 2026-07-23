# Verification report

Verdict: likely valid candidate full negative answer, pending expert review.

## Proof audit

1. **Cone inclusion.** Every completely positive matrix has the form `BB^T`,
   hence is positive semidefinite. It is therefore enough to upper-bound the
   PSD part of the max cube.
2. **Measure convention.** Independent upper-triangular matrix entries differ
   from orthonormal Frobenius coordinates only by the fixed factor
   `sqrt(2)` in each off-diagonal direction. That factor cancels in the volume
   ratio with the same max cube.
3. **Diagonal/correlation parametrization.** Except on a null boundary, a PSD
   matrix with diagonal `d_i in (0,1]` is uniquely `D^{1/2} C D^{1/2}`, where
   `C` is a correlation matrix. Conversely every such pair lies in the max
   cube because `|c_ij| <= 1`.
4. **Jacobian.** For fixed diagonal, each off-diagonal coordinate is multiplied
   by `sqrt(d_i d_j)`. Their product is
   `product_i d_i^((n-1)/2)`, whose diagonal integral is
   `(2/(n+1))^n`.
5. **Elliptope recursion.** Over a positive-definite leading correlation block
   `B`, the Schur-complement fiber is the ellipsoid
   `x^T B^{-1} x <= 1`, of volume `v_(n-1) sqrt(det B)`. The singular boundary
   is null, and Hadamard's inequality gives `det B <= 1`.
6. **Asymptotics.** The standard ball-volume bound
   `v_k <= (2*pi*e/k)^(k/2)` and an integral estimate for
   `sum k log k` imply
   `log product_{k<n} v_k <= -(n^2/4) log n + O(n^2)`. Dividing by
   `d_n = n(n+1)/2` yields the `O(n^{-1/2})` normalized radius.
7. **Question interpretation.** If “portion” means raw volume probability,
   the negative answer is immediate because `CP_n subset NN_n` and the
   nonnegative orthant has probability `2^{-d_n}`. The packet addresses the
   stronger root-volume interpretation suggested by the source's notation
   `c^{dim S_n}` and its volume-radius discussion.

## Numerical sanity check

Run:

```bash
python code/verify_volume_bound.py
```

The script evaluates the explicit proved upper bound using log-gamma
arithmetic. For `n = 32, 64, 128, 256` it gives respectively approximately
`0.35886, 0.28352, 0.21441, 0.15768`. This is only a numerical check of the
closed formula, not evidence in place of the proof.

## Novelty check

Bounded searches through July 22, 2026 used the exact source title and arXiv
id, the phrases “CP_n B_n,max”, “max norm completely positive matrices
volume”, “correlation elliptope volume completely positive cone”, and close
variants. They found the source paper and general elliptope literature, but no
later paper stating this max-cube negative answer or this reduction. Novelty
confidence is moderate; a specialist convex-geometry check is recommended.
