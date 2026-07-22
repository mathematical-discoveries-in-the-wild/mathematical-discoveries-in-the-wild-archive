# Full candidate: the finite-dimensional CHD bound for p > 2

Status: `candidate_full_solution_likely_valid`

Source: Grigory Ivanov, *Convex hull deviation and contractibility*, arXiv:1501.02596. Question 1 on arXiv PDF page 8 asks whether

\[
\zeta_{\ell_p^n}\le
\left(2\frac{n-1}{n}\right)^{|1/p-1/p'|}
\]

continues to hold for `2 < p < infinity`.

## Result

The answer is yes. In fact, if `x_0 = sum alpha_i x_i`, `max_i ||x_i||_p <= 1`, and `p' = p/(p-1)`, then

\[
\left(\sum_i\alpha_i\|x_i-x_0\|_p^{p'}\right)^{1/p'}
\le
\left(2\left(1-\sum_i\alpha_i^2\right)\right)^{1-2/p}.
\]

This follows by mixed-norm Riesz-Thorin interpolation of the centering operator. The source's finite-support reduction (Remark 2, PDF page 3) then gives the claimed CHD bound because an extremal witness uses at most `n` points and `sum alpha_i^2 >= 1/n`.

## Scope

This fully answers Question 1. It does not answer Question 2, which asks whether the dimension-free `L_p` estimate is exact.

## Files

- `main.tex`: complete proof and novelty record.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source formula and Questions 1-2.
- `verification.md`: line-by-line audit and review targets.
- `code/check_mixed_norm_bound.py`: deterministic randomized stress test; evidence only, not part of the proof.

## Novelty check

A bounded search on 22 July 2026 covered the run registry and solution/attempt indexes, the local arXiv corpus, arXiv/web searches by title, author, `CHD-constant`, `convex hull deviation`, and the displayed finite-dimensional `ell_p^n` bound, plus Ivanov's later arXiv:1904.06729. No explicit answer to Question 1 was found. Novelty confidence is moderate because the proof is short and could be implicit in interpolation literature.

Human review should focus on the exact mixed-norm interpolation identity and on the use of the source's at-most-`n`-point reduction.
