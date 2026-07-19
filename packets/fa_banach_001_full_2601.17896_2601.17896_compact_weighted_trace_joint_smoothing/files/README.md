# Joint smoothing of compact weighted traces

Source: Denis Vinokurov, *Eigenvalue optimization in higher dimensions and
p-harmonic maps*, arXiv:2601.17896v3, Remark 1.3 on PDF page 4.

Status: candidate full result, likely valid, for the uniformly positive
setting explicitly invoked immediately before Remark 1.3.

## Result

Let `M` be closed, let `alpha in L^1(M)` satisfy `alpha >= c > 0`, and let
`mu` be a nonzero positive Radon measure such that

```text
H^1(M,1,alpha) -> L^2(M,mu)
```

is compact. Then there are smooth strictly positive `alpha_n` and
`mu_n = rho_n dv_g` such that

```text
alpha_n -> alpha in L^1,
mu_n -> mu weak-star with mu_n(M) = mu(M),
lambda_k(alpha_n,mu_n) -> lambda_k(alpha,mu) for every k.
```

If `alpha in L^r`, `1 <= r < infinity`, the convergence of the weights is in
`L^r`. Hence all of Vinokurov's normalized eigenvalues converge when
`2 < p <= m` and `r=p/(p-2)`. For `p=2`, where the source fixes `alpha=1`,
one may keep `alpha_n=1`.

The proof smooths `alpha dv_g` and `mu` by the same small global flows. A
compact-trace Ehrling inequality survives this averaging uniformly, while the
energy forms Mosco-converge. A direct two-sided min--max argument then gives
the spectral convergence.

## Scope caveat

The theorem retains `alpha >= c > 0`, the hypothesis in the sentence
immediately preceding the open question. It removes continuity and any upper
bound on `alpha`. If the source question is interpreted as also allowing a
degenerate weight that vanishes, that broader variant remains open and this
packet should be treated as a sharp partial result.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `verification.md`: adversarial verification report.
- `source_paper.pdf`: the original arXiv paper.
- `figures/open_problem_crop.png`: source question and immediate context.
- `code/make_open_problem_crop.py`: reproducible crop helper.
- `tmp/`: LaTeX and page-rendering intermediates.

## Human review recommendation

Send to a specialist in weighted Dirichlet forms or spectral geometry. The
critical checks are the common-flow smoothing lemma, the averaged Ehrling
estimate, and the finite-dimensional recovery step in the eigenvalue limsup.

