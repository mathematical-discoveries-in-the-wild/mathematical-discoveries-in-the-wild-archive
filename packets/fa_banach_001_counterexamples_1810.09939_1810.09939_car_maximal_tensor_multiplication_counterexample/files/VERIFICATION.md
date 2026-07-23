# Verification Report

Candidate: arXiv:1810.09939, maximal-C*-tensor multiplication-extension
question in Section 2 (PDF page 5), with the original discussion in
arXiv:1405.0863, Section 3.1.

## Claim checked

For the CAR algebra `A=M_{2^infinity}`, every nontrivial finite-fold algebraic
multiplication map is unbounded for the maximal C*-tensor norm.  The associated
contraction map therefore cannot extend in the joint maximal-tensor sense
proposed in the sources.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | Liu says the maximal-tensor extension status is "still inconclusive" on PDF page 5 and cites Lesch Section 3; Lesch explicitly suspects non-extension examples. |
| Indexing normalization | valid | The packet writes `m_k` for `k`-fold multiplication and then translates back to Lesch's `mu_n` on `n+1` factors, avoiding Liu's shifted display. |
| CAR structure | valid | `A` is the inductive limit of `M_{2^r}` with unital embeddings and is nuclear. |
| Tensor-norm transfer | valid | Nuclearity gives `A tensor_max A = A tensor_min A`; injectivity of the minimal tensor product makes `M_d tensor_min M_d -> A tensor_min A` isometric. |
| Witness norm | valid | `z_d=sum_j e_{1j} tensor e_{j1}` maps `xi_j tensor xi_1` to `xi_1 tensor xi_j` and vanishes on the orthogonal complement, hence is a norm-one partial isometry. |
| Multiplication blow-up | valid | Multiplication maps `z_d` to `d e_11`, of norm `d`, for unbounded `d=2^r`. |
| Higher degrees | valid | Tensoring the witness with identity factors preserves norm one and leaves the multiplication image `d e_11`. |
| Contraction consequence | valid | Evaluation at `1 tensor ... tensor 1` is bounded and composes the proposed contraction extension to the forbidden multiplication extension. |
| Numerical sanity check | valid | `code/verifier.py` passes for `d=2,4,8,16` with exact zero residuals and the predicted norms. |

## Reproduction

Command:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/1810.09939_car_maximal_tensor_multiplication_counterexample/code/verifier.py
```

Observed output:

```text
d=2:  tensor norm 1.0, multiplication norm 2.0
d=4:  tensor norm 1.0, multiplication norm 4.0
d=8:  tensor norm 1.0, multiplication norm 8.0
d=16: tensor norm 1.0, multiplication norm 16.0
```

The script also checks `z_d z_d^* z_d=z_d` and
`m(z_d)=d e_11`, both with zero residual.  The finite computation does not
prove the infinite family; the displayed matrix-unit calculation does.

## Bounded literature audit

Search date: 2026-07-22.

Searched:

- local registry, solution, attempt, and proof-gap indexes;
- exact arXiv ids `1810.09939`, `1405.0863`, and the source titles;
- web/arXiv phrases combining `multiplication map`, `maximal C*-tensor
  product`, `CAR algebra`, `UHF algebra`, `nuclear C*-algebra`, and
  `subhomogeneous`;
- Vaes--Van Daele, arXiv:math/9907030;
- Van Daele, *From Hopf algebras to topological quantum groups* (2020);
- a 2021 MathOverflow thread about multiplication on `B(H)` and the spatial
  tensor product.

Findings:

- Lesch (2017) says he does not know the maximal-tensor answer and suspects
  interesting failures; Liu (2018/2020 version) still calls it inconclusive.
- Vaes--Van Daele (1999) states the general minimal-tensor failure but does not
  provide the CAR/maximal construction in the inspected discussion.
- Van Daele (2020) explicitly points to growth of the finite-dimensional
  multiplication norms on `M_d`, but again does not state the fixed simple
  nuclear CAR example in the inspected passage.
- No explicit CAR/UHF maximal-tensor counterexample was found.

This is bounded evidence, not a novelty certificate.  Because the construction
is an elementary synthesis of standard facts, priority should not be claimed
without a specialist search.

## Gaps and limitations

No mathematical gap was found.  The result is an existence counterexample,
not a classification.  It does not settle whether multiplication extends for
every fixed nuclear non-subhomogeneous algebra, nor the case of the irrational
rotation algebra that motivates Liu's applications.

## Confidence

- Mathematical validity: 98/100.
- Novelty as an explicit CAR/maximal example: 68/100.

## Human review recommendation

Send to an operator-algebra specialist.  Check the two tensor-norm transfer
sentences first, then search the older Hopf-C*-algebra/operator-space
literature for an explicit fixed nuclear example.

