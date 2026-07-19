# Verification notes

Status: conditional counterexample reduction, likely valid.

## Audited steps

1. The matrix density `exp(-||A||_*)` is log-concave because the nuclear norm
   is convex. Left-right orthogonal invariance makes the covariance a scalar
   identity; scalar normalization therefore gives an isotropic law.
2. The real square SVD Jacobian has no individual singular-value power and has
   Vandermonde factor `prod_{i<j}|s_i^2-s_j^2|`.
3. The boundary density formula was checked directly for `n=1,2` and by two
   independent implementations (exact fractions and high precision).
4. After shifting every remaining singular value by `x`, every Vandermonde
   sum factor and every boundary factor increases. This gives the exact lower
   comparison `g_n(x) >= exp(-n x) g_n(0)`.
5. Radial integration in dimension `n^2` gives
   `E||A||_*^2=n^2(n^2+1)`. Since `||A||_* <= sqrt(n)||A||_F`, the common
   entry variance is at least `n+1/n`. This is enough for the isotropic scaling;
   no unquoted equilibrium asymptotic is used.
6. Exact outputs were obtained for every `1 <= n <= 40`; selected values agree
   with the high-precision implementation. The high-precision run was extended
   to `n=200`.

## Conditional dependency

The packet does **not** prove that `d_n=B_n/Z_n` is unbounded. This is the sole
unproved lemma. Numerical growth, an equilibrium-density heuristic, or a fit to
`sqrt(log n)` is not treated as proof.

## Most important verifier focus

Prove any lower bound `d_n -> infinity`, even arbitrarily slowly. A sharp
asymptotic is unnecessary. The normalized Pfaffian entries are

```text
q_ij = 2 I_{1/2}(2i+1,2j+1) - 1,
```

and the ratio deletes the index `0`, with the standard one-vector augmentation
for odd cardinality. This formulation may be approachable through
skew-orthogonal polynomials or a local central-limit comparison for gamma races.

## Novelty-search bounds

Bounded searches on 19 July 2026 used the exact arXiv id/title and the phrases
`smallest singular value Schatten 1 ball`, `nuclear norm random matrix hard
edge`, `Pfaffian exp(-x) singular values`, and `rectangular Schatten volume`.
The closest sources inspected were arXiv:1804.03467, arXiv:2111.07803,
arXiv:2209.07253, and arXiv:math-ph/0612007. None was found to state this
counterexample or the required real nuclear-Laplace boundary-ratio asymptotic.
