# Quantitative splitting under a sharp endpoint-similarity criterion

Status: `partial_result_likely_valid`

Source: J. Oliva-Maza and Y. Tomilov, *On similarity to contraction
semigroups and tensor products, I*, arXiv:2509.01005, Theorem 5.3 and the
question immediately following it on PDF page 18.

## Result

The source asks whether the zero-growth hypothesis in its sharp quantitative
splitting theorem is redundant.  This packet removes that hypothesis whenever
all but at most one factor have growth-normalized similarity constant at most
the tensor product's similarity constant.  The factors may be nonnormal and
need not be contractions in the original norm.  Growth-normalized contractions
and normal semigroups are important special cases.

For two factors, if
`beta = omega_0(T_2)` is finite and
`C(e_{-beta} T_2) <= C(T_1 tensor T_2)`, then the
zero-sum choice

`d_1 = beta`, `d_2 = -beta`

satisfies

`max(C(e_{d_1}T_1), C(e_{d_2}T_2)) <= C(T_1 tensor T_2)`.

The proof combines the source paper's sharp endpoint extraction estimate from
its complete-boundedness argument with the assumed endpoint similarity bound.
The same grouping argument treats finitely many factors.  A finite-dimensional
companion theorem proves constrained-Lyapunov superadditivity whenever either
factor attains its spectral abscissa within the distortion budget, by
compressing the product metric along a peripheral eigenvector.

## Scope and review

The general negative-growth case remains open.  The exact unresolved issue is
whether an optimal, possibly entangled, Hilbertian metric on the tensor product
can outperform every zero-sum collection of factor metrics with the same
distortion bound.  The accompanying attempt note gives a finite-dimensional
Lyapunov reformulation and convex SDP tests in dimensions two through four;
those tests are not used in the proof.

Human review recommendation: **verify and retain as a clean partial theorem**.
The main point to check is the endpoint similarity-constant estimate quoted
from the proof in Section 8 of the source paper.

Ledger: `ledger/results/2509.01005_growth_normalized_factor_quantitative_splitting.json`
