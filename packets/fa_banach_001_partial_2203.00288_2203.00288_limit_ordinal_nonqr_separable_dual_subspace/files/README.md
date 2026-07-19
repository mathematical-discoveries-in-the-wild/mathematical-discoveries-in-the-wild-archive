# Limit-Ordinal Weak-Star Derived Sets: the Non-Quasi-Reflexive Separable-Dual Subspace Case

Status: `partial_result (likely valid; answers Silber Question 1 when X contains a non-quasi-reflexive subspace with separable dual)`.

Source paper: Zdenek Silber, *On subspaces whose weak* derived sets are proper and norm dense*, arXiv:2203.00288.

## Result

Let `alpha` be a countable limit ordinal.  If a Banach space `X` contains a subspace `Y` such that `Y` is non-quasi-reflexive and `Y*` is separable, then there is a subspace `A` of `X*` such that

```text
A^(alpha) proper subset of norm-closure(A^(alpha)) = X*.
```

This gives a positive partial answer to Silber's limit-ordinal question.  It strictly strengthens the previous `c0` packet, since `c0` is one example of a non-quasi-reflexive space with separable dual.

## Idea

Silber's construction already defines the recursive pieces `K(alpha,A,z+a f_k)` for limit ordinals.  In the general proof, the density step fails because finite-support approximants converge only weak-star, so a key vector lands in `K^(alpha+1)` rather than `K^(alpha)`.

If the non-quasi-reflexive part has separable dual, the Davis-Johnson/Ostrovskii minimal-system construction can be run with a dense sequence in the whole ambient dual.  The resulting finite-dimensional decomposition is then shrinking, so the adjoint coordinate projections converge in norm.  That norm convergence upgrades Silber's limit-stage obstruction into norm density of `K^(alpha)`.

Properness is preserved by using a cofinal sequence `alpha_n -> alpha`: every element of `K^(alpha)` satisfies all but finitely many tail equations, while a norm-convergent series in the biorthogonal `u_n`-functionals violates infinitely many of them.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source/open-problem paper.
- `figures/open_problem_crop.png`: crop of Silber's Question 1 on page 11.

## Scope And Limitations

This is not a full solution of Silber's question.  The remaining case is when `X` is non-quasi-reflexive and contains an infinite-dimensional subspace with separable dual, but no non-quasi-reflexive subspace with separable dual is known or available.  Ostrovskii's general construction combines a non-quasi-reflexive basic sequence from `X` with a separate separable-dual subspace; in that setting the relevant FDD is only known to have weak-star convergent adjoint projections.

## Search Evidence

Before promotion, local indexes were searched for `2203.00288`, `weak* derived`, `proper norm dense`, and `limit ordinal`; no prior packet for this target was found except the immediately previous `c0` subcase packet produced by this lane and now strengthened here.  Web searches for exact phrases from the question and close variants found Silber's paper, Ostrovskii's older transfinite-order paper, Ostrovskii's first-derivative norm-dense paper, and Ostrovskii's convex successor-order paper, but no later explicit answer to the limit-ordinal subspace question.
