# Weighted product metrics have an explicit metric infimal convolution

Status: `candidate_full_likely_valid`

Source: Nicolò De Ponti, Giacomo Enrico Sodini, and Luca Tamanini,
*The infimal convolution structure of the Hellinger-Kantorovich distance*,
arXiv:2503.12939v1 (2025).

Source location: Introduction, page 5. The authors ask whether there are other
purely metric examples, beyond the Hellinger-Wasserstein case, for which their
metric infimal-convolution construction produces meaningful distances.

## Full affirmative answer to the existential question

Let `(X_k,d_k)`, `k=1,...,m`, be arbitrary geodesic metric spaces and put
`Z=prod_k X_k`. For two positive weight arrays define

```text
rho_j(z,z')^2 = sum_k a_jk^2 d_k(z_k,z'_k)^2,   j=1,2.
```

Set the coordinatewise parallel-sum weights

```text
a_*k = (a_1k^(-2)+a_2k^(-2))^(-1/2)
     = a_1k a_2k / sqrt(a_1k^2+a_2k^2).
```

Then the source's metric infimal convolution satisfies the exact formula

```text
rho_1 nabla rho_2 = rho_*,
rho_*(z,z')^2 = sum_k a_*k^2 d_k(z_k,z'_k)^2.
```

More strongly, the minimum `N`-path energy equals `rho_*^2` for every
discretization level `N`, so the defining liminf causes no loss or subtlety.
The result is finite, nondegenerate, and geodesic.

## Genuinely nonlinear example

Let `T` be a metric tripod and consider `Z=T x [0,1]`. Define

```text
rho_1^2 = d_T^2 + 4 |s-t|^2,
rho_2^2 = 4 d_T^2 + |s-t|^2.
```

Then

```text
rho_1 nabla rho_2 = (2/sqrt(5)) sqrt(d_T^2+|s-t|^2).
```

The space has branching and no vector-space structure. The two input metrics
are not proportional: one is twice as large in the tripod direction and the
other is twice as large in the interval direction. Both contribute to the
effective metric.

## Proof mechanism

For every alternating step, the scalar identity

```text
a^2 A^2+b^2 B^2
  >= (a^2 b^2/(a^2+b^2))(A+B)^2
```

and the coordinate triangle inequalities give a lower bound by the effective
product metric. Cauchy-Schwarz and the triangle inequality then bound every
`N`-path energy below by the endpoint distance squared. Coordinatewise
geodesics, with the intermediate point placed at fraction
`a_2k^2/(a_1k^2+a_2k^2)` in coordinate `k`, attain equality.

## Scope and novelty

This fully answers the source's existential question in the affirmative. It
does not classify all pairs with meaningful infimal convolution, address the
paper's separate `p`-Hellinger-Kantorovich question, or assert that every pair
of geodesic metrics behaves well.

Cheap run indexes were searched using the arXiv id, source title, exact
question terms, product metrics, geodesic products, and parallel sums. A
bounded arXiv/web search used the exact source question and close metric
infimal-convolution/product terms. It found the source and unrelated
functional infimal-convolution literature, but no separate statement of this
weighted-product theorem. This is not an exhaustive novelty certification.

## Packet contents

- `main.tex`: theorem, full proof, nonlinear example, and scope audit.
- `solution_packet.pdf`: rendered human-review packet.
- `source_paper.pdf`: official arXiv source paper.
- `figures/open_problem_crop.png`: full-width source crop from page 5.
- `code/check_parallel_sum.py`: exact symbolic and rational arithmetic checks.
- `verification.md`: adversarial verifier report.

Human review recommendation: **send to a metric geometer**. The key checks are
the interpretation of the source's broad existential question and the exact
per-coordinate equality construction.
