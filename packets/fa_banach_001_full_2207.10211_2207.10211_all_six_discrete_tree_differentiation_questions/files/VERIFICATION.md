# Verification Report

Candidate: arXiv:2207.10211, all six open questions

## Claim checked

The norm conjecture has a weighted-Hilbert counterexample; differentiation is
never power-bounded; the backward composition operator is never surjective;
and differentiation is never compact on a discrete function space. In
addition, exact spectra are given for every bounded weighted Banach case and
every discrete Hardy space.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Weighted Hilbert space is functional | valid | Every weight is positive, evaluations have norm `w(v)^(-1/2)`, and point masses separate vertices. |
| Tree shift `U` is an isometry | valid | Summing squared child coefficients uses exactly `sum_child p_v = 1` at each parent. |
| `C_b = P_o + U` after conjugation | valid | The root coordinate is fixed; every nonroot coordinate receives the weighted parent value. |
| `||C_b|| = sqrt(2)` | valid | Root and nonroot supports are orthogonal, and equality occurs on the root unit vector. |
| `||D|| = 2` | valid | Triangle inequality gives the upper bound; the alternating orbit vectors give squared norms `4 - 3/N`. |
| Pointwise bounded iterates imply constancy | valid | At a child one level below an edge increment `a_m`, the iterate is `a_{m+1}-(n-1)a_m`; leaflessness supplies the child. |
| No isometric `D` | valid | Isometry makes all powers norm one; continuous evaluations then give pointwise bounded orbits, contradicting point separation. |
| No surjective `C_b` | valid | Every range function agrees at the root and each root child, directly contradicting the functional-space separation axiom. |
| No finite-dimensional invariant space | valid | The only possible eigenvalue is zero; nilpotence plus the root-zero range forces `D=0`, leaving only constants. |
| No compact `D` | valid | `C_b` is noninvertible, hence `1` lies in `sigma(D)`; leaflessness makes `C_b` injective, so `1` is not an eigenvalue, contradicting compact spectral theory in infinite dimension. |
| Path-tree consequence | valid | If `D` is unbounded it is not compact; if bounded, the universal obstruction applies. |
| Operator-weighted shift disk lemma | valid | A one-level input to a hypothetical resolvent yields `R_k <= C |lambda|^(k+1)`, contradicting every `|lambda|<rho`; the spectral-radius formula gives the reverse inclusion. |
| Weighted-space block decomposition | valid | After conjugation and splitting off the root, `C_b` has blocks `[[1,0],[B_1,S]]`. For `lambda != 1`, direct block elimination reduces invertibility to `S-lambda`; at `lambda=1`, the first range coordinate vanishes. Tail block products are exactly descendant/ancestor weight ratios. |
| Hardy-space level norms | valid | Normalized level counting makes every tail replication map an isometry, so all block-product norms and the spectral radius equal one. |
| Translation to `D` | valid | `D=I-C_b` gives `sigma(D)=1-sigma(C_b)` by elementary spectral mapping. |

## Counterexample search and computation

The script `code/verify_weighted_hilbert.py` checked the binary-tree
truncation through depth 10. It returned

```text
||C_b||=1.414213562373
||D|| on truncation=1.979642883762
||D y_N||^2=3.700000000000 (expected 3.700000000000)
```

The exact argument does not rely on finite truncation. No contradictory small
case was found.

## External dependencies

- The source definition of a discrete function space and `D = I - C_b`.
- The standard compact-operator spectral theorem on an infinite-dimensional
  complex Banach space.

The spectral completion uses only the self-contained operator-weighted shift
lemma proved in the packet and elementary spectral mapping.

Both are used in their standard stated scope.

## Gaps

No proof gap found. The bounded literature search does not establish
exhaustive novelty or priority.

## Confidence

Score: 94/100 for mathematical validity; moderate for novelty.

## Human review recommendation

Send to human. The all-six solution is short enough for independent
verification and strong enough to merit a priority search after the proof
audit. Give special attention to the uniform growth radius in Question 5.
