# Verification Report

Candidate: arXiv:2503.12939, introduction question on other purely metric
examples with meaningful infimal convolution

## Claim Checked

For weighted `l2`-product metrics `rho_1,rho_2` on any finite product of
geodesic metric spaces, their metric infimal convolution equals the weighted
product metric whose coordinate weights are the parallel sums

```text
a_*k = (a_1k^(-2)+a_2k^(-2))^(-1/2).
```

The minimum energy equals `rho_*^2` for every discretization level `N`.

## Verdict

`likely valid`

Confidence: 97/100.

The mathematical proof is elementary and exact. The modest residual
uncertainty concerns scope and novelty: the source question is intentionally
broad, and a human should decide whether this product class matches the
authors' intended meaning of an example "similar" to Hellinger-Wasserstein.

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Weighted product functions are metrics | valid | Coordinate triangle inequalities followed by finite-dimensional Minkowski; positive weights give nondegeneracy. |
| Effective product is geodesic | valid | Run constant-speed coordinate geodesics with a common parameter. |
| Scalar weighted-square inequality | valid | The defect is the explicit square `(a^2 A-b^2 B)^2/(a^2+b^2)`. |
| Per-step lower bound | valid | Apply the scalar inequality in each coordinate and then use `C_ik <= A_ik+B_ik`. |
| Whole-path lower bound | valid | Cauchy-Schwarz gives `N sum step_i^2 >= (sum step_i)^2`; the effective metric triangle inequality finishes. |
| Equality construction | valid | Coordinate `k` places its intermediate point at fraction `a_2k^2/(a_1k^2+a_2k^2)`. Product coordinates may use different fractions because `y_i` is an arbitrary product point. |
| Liminf passage | valid | Stronger statement proved: equality of the minimum energy for every `N`. |
| Tripod example | valid | Weights `(1,2)` and `(2,1)` both produce effective coefficient `2/sqrt(5)`; the two input metrics are not proportional. |

## Counterexample Search

Potential failure modes checked:

- Zero coordinate displacement: the corresponding coordinate geodesic is
  constant and all formulas remain valid.
- Different optimal fractions across coordinates: allowed, since an
  intermediate product point is chosen coordinatewise.
- Nonunique geodesics: only existence is used.
- Noncomplete or nonseparable factors: neither property is used; geodesicity
  suffices.
- Finite versus infinite products: the theorem is explicitly finite-product
  only, so no convergence issue is hidden.

The exact checker verifies the scalar identity symbolically, 300 deterministic
rational path lower bounds, 200 exact attaining paths, and the tripod
coefficient.

Command:

```text
conda run --no-capture-output -n sandbox python code/check_parallel_sum.py
```

Expected final line: `all checks passed`.

## External Dependencies

- Original source and definition: De Ponti--Sodini--Tamanini,
  arXiv:2503.12939v1.
- No external mathematical theorem is required beyond elementary metric
  inequalities and existence of the assumed coordinate geodesics.
- Bounded novelty search found no separate statement of this exact product
  formula. This is not an exhaustive literature certification.

## Scope

The result is a full affirmative answer to the existential question. It is
not a classification, a theorem for arbitrary pairs of metrics, or progress
on the separate `p`-Hellinger-Kantorovich problem.

## Human Review Recommendation

`send to human`

Mathematically, review the equality construction. For classification, decide
whether the source's phrase "similar to the Hellinger-Wasserstein case" was
intended to require additional optimal-transport structure not stated in the
question.
