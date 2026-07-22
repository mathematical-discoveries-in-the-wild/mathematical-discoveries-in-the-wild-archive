# Critical Gaussian sparsity: bipartite-block counterexample

Status: `candidate_full_likely_valid`

Source: Afonso S. Bandeira and Ramon van Handel, *Sharp nonasymptotic
bounds on the norm of random matrices with independent entries*,
arXiv:1408.6185, Remark 4.5.

## Result

For every fixed `a>0`, there is a sequence of symmetric Gaussian matrices
supported on exactly `k`-regular graphs with `k/log(n) -> a` such that

```text
||X||/sqrt(k) -> t_a > 2  in probability,
integral_2^{t_a} sqrt(x^2-4) dx = 1/a.
```

Take the support graph to be a disjoint union of `m_k=floor(exp(k/a))`
copies of `K_{k,k}`. Each random `2k`-vertex block is
`[[0,G],[G^T,0]]`, so its norm is the largest singular value of a square
Gaussian matrix. The square-Wishart right-tail LDP has speed `k` and rate
`J(t)=integral_2^t sqrt(x^2-4) dx`. Maximizing over exponentially many
independent blocks yields the stated limit.

This fully refutes the universal possibility raised in Remark 4.5 that a
sufficiently large finite `a` might force convergence to the semicircle edge
`2` under the paper's stated regular-support assumptions. It does not
classify all regular support graphs.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `supporting_wishart_ldp.pdf`: primary supporting LDP paper,
  arXiv:1810.01188.
- `figures/remark_4_5_part*.png`: source-question crop spanning pages 25--26.
- `code/verify_rate_extremes.py`: deterministic checks of the rate function,
  roots, and extreme-value exponents.
- `verifier_report.md`: verifier output and interpretation.

## Literature note

The separate Gaussian row/column-norm conjecture in Remark 3.16 was later
settled by arXiv:1711.00807 and was already indexed in this run. A bounded
search found no paper explicitly stating the critical `K_{k,k}` block
consequence above.

## Human review focus

Check the normalization translating Theorem 1.7 of arXiv:1810.01188 to
`J(t)=integral_2^t sqrt(x^2-4) dx`. The rest is an elementary direct-sum and
independent-maximum argument.
