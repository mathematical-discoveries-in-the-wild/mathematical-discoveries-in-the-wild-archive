# Strongest Locally Convex Topology: Full Answer for Approximate Spectra

Status: `full_result_likely_valid`

Source: Karsten Kruse, *Spectral theory for semigroups on locally convex
spaces*, arXiv:2509.11931v2, J. Math. Anal. Appl. 564 (2026), Article
130889. Remark 5.17(a), PDF page 34, asks for useful sufficient conditions
beyond Banach spaces under which

```text
sigma_ap(B) = sigma_bap(B)
```

or the sequential analogue holds for every closed linear operator `B`.

## Full answer

If `X` carries its strongest Hausdorff locally convex topology, then for every
linear operator `(B,D(B))` on `X`—even without closedness—

```text
sigma_p(B)
  = sigma_ap(B)
  = sigma_ap^seq(B)
  = sigma_bap(B)
  = sigma_bap^seq(B).
```

The reason is hereditary maximality. Every subspace `R` of `X` inherits the
strongest locally convex topology: extend an arbitrary seminorm on `R` using
an algebraic projection `X -> R`. Therefore, whenever `lambda-B` is injective,
its algebraic inverse from `ran(lambda-B)` to `X` is automatically continuous.
Any approximate eigen-net must then converge to zero. Conversely, a genuine
eigenvector gives a bounded constant witness for all four approximate spectra.

The standard space

```text
phi = direct_sum_{n>=1} C
```

with its locally convex direct-sum topology is complete,
infinite-dimensional, and nonnormable, so the answer is genuinely outside the
Banach category.

## Sharp boundary

The earlier Montel obstruction remains part of the result. On the nuclear
Frechet--Montel space `s` of rapidly decreasing sequences, the closed diagonal
operator `(Bx)_n=exp(-n)x_n` satisfies

```text
0 in sigma_ap^seq(B) but 0 notin sigma_bap(B).
```

Thus completeness, metrizability, nuclearity, Frechet, Schwartz, and Montel
conditions do not suffice on their own, even jointly.

## Verification and novelty search

The spectral proof is exact and uses only the definition of the strongest
locally convex topology. `VERIFICATION.md` gives an adversarial check.

A bounded search through 2026-07-19 covered the run registry, local source
corpus, current source and references, arXiv, and exact web phrases combining
`approximate point spectrum` with `strongest/finest locally convex topology`
and `phi`. It found standard topology references but no prior statement of the
spectral-collapse theorem or its use to answer Remark 5.17(a). The topology
facts are classical; novelty of the spectral observation remains subject to
expert review.

Files:

- `source_paper.pdf`: current arXiv v2 PDF (revised 2026-06-24).
- `figures/open_problem_crop.png`: Remark 5.17(a) on PDF page 34.
- `main.tex`, `solution_packet.pdf`: complete proof packet.
- `VERIFICATION.md`: adversarial verification report.

Ledger:
`runs/fa_banach_001/ledger/results/2509.11931_strongest_locally_convex_full_answer.json`.
