# Verification report

Status: `candidate_full_result_likely_valid; human_review_needed`

## Formal audit

1. A compactly supported `C^1` orthonormal wavelet basis supplies
   `N_j=2^(j-q)` wavelets of scale `j` supported in each of two fixed open
   intervals. The selected families remain orthonormal across all scales.
2. With `A_j=gamma_j H_{N_j}` and
   `gamma_j=2^(-j(1+alpha))`, the Hadamard identity gives `N_j` singular
   values `gamma_j sqrt(N_j)=2^(-q/2)2^(-j(alpha+1/2))`.
3. At any point and scale only boundedly many compactly supported wavelets
   are active. Hence the kernel piece has sup norm `O(2^(-j alpha))` and
   first-variable and second-variable Lipschitz constants
   `O(2^(j(1-alpha)))`.
4. Summing `min(2^(-j alpha), 2^(j(1-alpha)) delta)` below and above
   `2^j delta asymp 1` gives `O(delta^alpha)` with no endpoint logarithm.
5. The kernel is supported in a fixed rectangle separated from the diagonal.
   Its uniform and global Holder bounds therefore imply the source's
   denominator-weighted standard estimates.
6. The Hilbert--Schmidt mass is
   `sum_j N_j s_j^2 = 2^(-2q) sum_j 2^(-2j alpha)`, which is finite for every
   `alpha>0`. This also justifies the integral-kernel limit.
7. A single compactly supported smooth symbol is one on every output wavelet
   and zero on every input wavelet. It belongs to `B_p(R)`, and the
   commutator equals `-T`.
8. The Schatten `p` mass is a constant multiple of
   `sum_j 2^(j[1-p(alpha+1/2)])`, which diverges exactly when
   `alpha<=1/p-1/2`, including equality.
9. Section 5.1 of the source supplies sufficiency in the complementary strict
   range `alpha>1/p-1/2`, yielding the claimed classification.

No missing implication was found in this audit.

## Exact finite smoke test

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2411.05810_sharp_schatten_commutator_threshold/code/verify_hadamard_blocks.py
```

The script checks Sylvester matrices of orders `2,4,8,16,32,64` exactly in
SymPy, verifies `H H^T=N I`, and verifies the repeated eigenvalue of
`A^T A` for an exact rational block coefficient.

## Reviewer focus

The highest-value checks are the availability and counting of supported
wavelets inside fixed intervals, the low/high frequency Holder sum, and
whether the positive estimate in Section 5.1 of the source has exactly the
same operator hypotheses used by the counterexample.
