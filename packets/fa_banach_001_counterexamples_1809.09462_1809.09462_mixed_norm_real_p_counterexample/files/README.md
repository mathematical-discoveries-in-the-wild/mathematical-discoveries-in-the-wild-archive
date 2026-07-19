# 1809.09462 mixed-norm real-p extension counterexample

Status: `counterexample_likely_valid`

Source paper:

- Ashwin Sah, Mehtaab Sawhney, David Stoner, Yufei Zhao, *A reverse Sidorenko inequality*, arXiv:1809.09462.
- Target passage: Section 3.1, Remark after Lemma 3.1, PDF page 12.

Question answered:

The source proves
`||A^T B||_{L_{1,q}}^2 <= ||A^T A||_{L_{q,q}} ||B^T B||_{L_{1,1}}`
for nonnegative matrices, and asks whether the extension
`||A^T B||_{L_{p,q}}^2 <= ||A^T A||_{L_{q,q}} ||B^T B||_{L_{p,p}}`
holds for all real `1 <= p <= q`, noting that it is true for positive integer
`p` by a tensor-power argument.

Result:

The proposed extension is false already for `p=q=3/2`, with nonnegative
`2 x 2` matrices.

Let `t=1/4`, `r=7/8`, `alpha=r^{2/3}`, and

```text
A = [[0,      1],
     [alpha,  t]]

B = [[t, alpha],
     [1, 0    ]]
```

Equivalently the columns are `alpha e_2`, `(1,t)` for `A`, and `(t,1)`,
`alpha e_1` for `B`. For `p=q=3/2`, the proposed inequality would reduce to
`S <= X`, where

```text
S = 2r + (2t)^(3/2)
X = r^2 + 2r t^(3/2) + (1+t^2)^(3/2).
```

At `t=1/4`, `r=7/8`,

```text
S = (7 + sqrt(2))/4,
X = (63 + 17 sqrt(17))/64,
```

and `S > X`, so the inequality fails.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source paper, arXiv:1809.09462.
- `figures/open_problem_crop.png`: page-12 source crop containing the proposed extension.
- `code/verify_counterexample.py`: exact/numerical verification script.
- Ledger record: `runs/fa_banach_001/ledger/results/1809.09462_mixed_norm_real_p_counterexample.json`.

Novelty check:

Bounded search on 2026-07-03 found no exact duplicate in the run registry or
local parsed arXiv sources. Web searches for exact phrases including
`"A^T B" "L_{p, q}" "A^T A" "B^T B"`,
`"mixed L^{p,q} matrix norm" "A^T B"`, and the source sentence returned no
visible later answer.

Scope:

This disproves only the proposed extension to all real `p`. It does not affect
the source paper's proved `p=1` inequality, the positive-integer `p` cases, or
the graph-theoretic reverse Sidorenko results.
