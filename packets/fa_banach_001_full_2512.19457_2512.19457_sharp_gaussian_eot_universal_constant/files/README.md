# Sharp universal constant for Gaussian EOT coupling convergence

Status: `full_solution_likely_valid`

This packet resolves Conjecture 3.1 of Ho Yun, *Spectral Shrinkage of Gaussian Entropic Optimal Transport*, arXiv:2512.19457.

For positive-definite covariance matrices \(A,B\in\mathbb R^{d\times d}\), put

\[
Z=(A^{1/2}BA^{1/2})^{1/2}.
\]

The normalized squared Wasserstein distance has the exact limit

\[
\lim_{\varepsilon\downarrow0}
\frac{\mathcal W_2^2(\pi_\varepsilon,\pi_0)}{\varepsilon}
=\operatorname{tr}\!\left[(A+ZA^{-1}Z)^{-1}Z\right]
\le \frac d2.
\]

Equality holds exactly when \(A=B\). Thus the sharp universal constant is
\(C_d=d/2\), and the identity transport case is the unique worst case.

Files:

- `solution_packet.pdf`: rendered expert-facing proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: current arXiv paper PDF.
- `figures/open_problem_crop.png`: Conjecture 3.1 on source page 19.
- `verification.md`: proof audit and novelty-search bounds.
- `code/numerical_check.py`: reproducible non-proof finite-difference checks.
- `code/make_source_crop.py`: reproducible crop generator.

Run the numerical check with:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2512.19457_sharp_gaussian_eot_universal_constant/code/numerical_check.py
```

Human-review recommendation: check the source normalization in Theorem 3.10 and the aligned factorization \(M=A^{-1/2}Z\). The first-order expansion and sharp operator inequality are then self-contained.
