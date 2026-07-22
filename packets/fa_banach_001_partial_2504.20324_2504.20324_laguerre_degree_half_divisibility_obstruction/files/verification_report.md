# Verification report

Status: `partial_result_likely_valid; human_review_needed`

## Formal audit

1. Substituting `Q=PR` into the generalized Laguerre equation and using the
   ordinary Laguerre equation gives

   ```text
   P[xR''+(m+1-x)R'+(n-k)R] + P'[2xR'+mR] = 0.
   ```

2. `L_k` has simple positive zeros, hence `gcd(P,P')=1`, so
   `P | (2xR'+mR)`.
3. If `r=n-k>0`, the latter polynomial has leading coefficient
   `(2r+m)` times the leading coefficient of `R`, so its degree is exactly
   `r`. This rules out `k<n<2k`.
4. For `n=2k`, the scalar multiple `2xR'+mR=cL_k` gives

   ```text
   c=(2k+m)/binom(2k,k)
   c=m binom(2k+m,2k),
   ```

   and these are incompatible for every nonnegative integer `m`.
5. In the source paper's Wigner induction, the generalized Laguerre degree is
   `j=ell+1=N-m`, where `m>=1`.
6. For `m>0`, if the positive roots of `R` are `beta_i`, then

   ```text
   B/R = m + 2x sum_i 1/(x-beta_i)
   ```

   is strictly decreasing on every complementary interval because the
   derivative of `2x/(x-beta_i)` is `-2 beta_i/(x-beta_i)^2`. It has exactly
   one root before every root of `R`; hence `B=L_k T` and `T` have only
   simple positive roots.
7. Reciprocal-root sums from the constant and linear coefficients are

   ```text
   sigma(L_n^(m)) = n/(m+1),  sigma(L_k)=k,
   sigma(B) = (m+2)/m * (n/(m+1)-k),
   sigma(T) = ((m+2)n-2(m+1)^2 k)/(m(m+1)).
   ```

   Since `deg(T)=n-2k>0`, strict positivity of `sigma(T)` gives the new
   obstruction.
8. The function `2(m+1)^2/(m+2)` is increasing for `m>=1`. This gives the
   direct Wigner cutoff `N<=1+8k/3`. Combining the same monotonicity with the
   known ranges `m<=50` and `m<=5k` gives the larger literature-assisted
   cutoff stated in the packet.

No missing implication was found in this audit.

## Exact symbolic smoke test

Command:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2504.20324_laguerre_degree_half_divisibility_obstruction/code/verify_degree_obstruction.py
```

Scope: all `1<=k<=12`, `1<=n<=2k`, `0<=m<=80`, with exact rational
polynomial division in SymPy.

Result: `PASS`; 12,636 exact triples were checked, and divisibility occurred
only for `(n,k,m)=(k,k,0)` with `1<=k<=12`.

This finite check is not part of the proof.

## Reviewer focus

The highest-value checks are the product-rule identity, the normalization of
the leading coefficient of `R` at `n=2k`, the endpoint behavior of `B/R`,
the subtraction `sigma(T)=sigma(B)-sigma(L_k)`, and the two Wigner index
shifts.
