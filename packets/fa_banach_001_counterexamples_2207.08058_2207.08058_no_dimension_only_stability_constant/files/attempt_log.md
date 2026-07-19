# Attempt log

Target: Problem 1 in Section 5 of arXiv:2207.08058.

## Selection

The paper contains one precise open problem among broader suggestions.  It
asks for a Hyers-Ulam-type approximation with error `k_N delta`, explicitly
stating that `k_N` depends only on the ambient dimension.

## Direct attack

The first test was the value at the origin for `0<m<1`.  Exact
`m`-star-convexity forces `Psi(0)<=0`, because the weights on the right-hand
side sum to `1-lambda(1-m)<1`.  This suggested testing positive constants.

For the constant `Phi=delta/(1-m)`, the missing mass in those weights creates
an error `lambda delta`, which is always bounded by the permitted `delta`.
Hence `Phi` is approximately `m`-star-convex but is at uniform distance at
least `delta/(1-m)` from every exact function.

Using `C=R^N` removes any concern about a singleton or a domain not closed
under the star-convex combinations.  Taking `omega=0` removes any modulus
regularity issue.

## Outcome

Candidate counterexample, likely valid, to the dimension-only statement.
The example gives a quantitative lower bound on every possible corrected
`m`-dependent constant.

