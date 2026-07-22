# Degree and positive-root obstructions for generalized Laguerre divisibility

Status: `partial_result_likely_valid; human_review_needed`

Source: Luis Daniel Abreu, Ulysse Chabaud, Nuno Costa Dias, and Joao
Nuno Prata, *Inverse problems for the zeros of the Wigner function*,
arXiv:2504.20324 (2025).

## Source conjectures

Conjecture 2 on page 7 asks whether

```text
L_k divides L_n^(m)  =>  L_n^(m)=L_k
```

for `n,k>=1` and `m>=0`. The paper proves its Wigner nodal-rigidity
Conjecture 1 conditionally on this Laguerre divisibility statement.

## New partial results

For `n<=2k`, Conjecture 2 is true:

```text
If L_k divides L_n^(m) and n<=2k, then n=k and m=0.
```

More generally, if `L_n^(m)=L_k R`, comparison of the two Laguerre
differential equations gives

```text
L_k divides 2x R'(x)+mR(x).
```

The right-hand side has degree `n-k`. This immediately rules out
`k<n<2k`. At the boundary `n=2k`, comparison of its constant and leading
coefficients yields an impossible binomial-coefficient identity.

Using the reduction in Section 6 of the source paper, the result proves the
Hermite-Wigner nodal-rigidity conjecture whenever the finite Hermite normal
form of `f` has top degree `N<=2k+1`.

The full-result push produced a second obstruction. For `m>=1`, all roots of
the quotient `R` are positive. The polynomial

```text
B=2xR'+mR=L_k T
```

also has only simple positive roots: its logarithmic derivative is strictly
decreasing between consecutive roots of `R`. Hence `T` has positive roots,
and its reciprocal-root sum must be positive. Exact coefficient comparison
gives

```text
sum_{T(beta)=0} 1/beta
  = ((m+2)n-2(m+1)^2 k)/(m(m+1)) > 0.
```

Therefore every nontrivial divisibility with `m>=1` satisfies

```text
n > 2(m+1)^2 k/(m+2).
```

Combining this with cases already summarized in the source paper leaves any
unknown counterexample only in

```text
k>=4,  m>max(50,5k),  n>2(m+1)^2 k/(m+2).
```

The direct Wigner range improves to `N<=1+8k/3`. Using the known
factorization ranges, put `M_k=max(50,5k)`. For `k>=4`, Wigner rigidity holds
whenever

```text
N <= M_k+1 + 2(M_k+2)^2 k/(M_k+3).
```

For `k=1,2,3`, the source paper's proved Laguerre cases give the Wigner
conclusion for every finite `N` under the same source hypotheses.

## Scope

This does not prove the full Laguerre or Wigner conjecture. The second
positive-root quotient is not known to preserve the factor `L_k`, so the
argument cannot simply be iterated. The Wigner corollaries use the finite
Hermite normal form and coefficient induction established in the source
paper.

## Verification and novelty

The proof is purely algebraic. The included exact-arithmetic checker tests all
`1<=k<=12`, `1<=n<=2k`, and `0<=m<=80`. These computations are a smoke test,
not part of the proof.

Cheap run indexes had no hit for arXiv:2504.20324 or the conjecture. Bounded
web searches for exact divisibility phrases, common-zero theorems, quotient
differential identities, and the degree range found the source paper and the
older generalized-Laguerre factorization literature, but no statement of
either obstruction. The source paper's own list of proved regions does not
include them.

## Packet contents

- `main.tex` and `solution_packet.pdf`: theorems, proofs, and Wigner
  corollaries.
- `source_paper.pdf`: the arXiv source paper.
- `figures/open_problem_crop.png`: Conjecture 2 on source page 7.
- `code/verify_degree_obstruction.py`: exact finite symbolic check.
- `verification_report.md`: audit points and checker result.

Human review should focus on the product-rule differential identity, the
`n=2k` coefficient normalization, positive-root interlacing for `B`, the
reciprocal-root sum of `T`, and the index shifts in the Wigner corollaries.
