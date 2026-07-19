# Counterexample packet: no universal spherical logarithmic Sobolev constant

Status: candidate counterexample likely valid.

Source paper: Matthieu Fradelizi, Nathael Gozlan, Shay Sadovsky, and Simon
Zugmeyer, "Transport-entropy forms of direct and converse Blaschke-Santalo
inequalities", arXiv:2307.04393.

Targeted open question: in the introduction, the authors ask whether the
underlying spherical log-Sobolev inequality

`H(e^{-V} sigma | sigma) <= (a/2) int log(1 + |grad V|^2/a^2) e^{-V} d sigma`

can hold for all regular enough potentials `V` and some constant `a > 0`.

Result: no such constant exists on `S^n` for any `n >= 1`.

Mechanism: small first-harmonic perturbations force any admissible constant to
satisfy `a <= n`.  Large von Mises-Fisher tilts
`d eta_t = exp(t x_1) d sigma / Z_t` then rule out all `a < n` by the leading
`log t` coefficient.  In the remaining critical case `a = n`, the constant
term in the Laplace asymptotics is positive:

`D_n = log 2 + (1/2)log pi - n/2 - log Gamma((n+1)/2)
       + n log(n/2) - (n/2) psi(n/2) > 0`.

The positivity follows from standard gamma and digamma bounds, and the script
`code/verify_critical_constant.py` prints representative values as a numerical
sanity check.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: locally compiled source paper PDF.
- `source_paper.tex`: local source TeX.
- `figures/open_problem_crop.png`: crop of the source open question.
- `code/make_open_problem_crop.py`: reproduces the crop.
- `code/verify_critical_constant.py`: numerical sanity check for `D_n`.

Novelty check: local run indexes were searched for `2307.04393`, the paper
title, Blaschke-Santalo, spherical log-Sobolev, transport entropy, and related
terms.  Web searches on 2026-07-18 found the arXiv paper, the published
listing, and unrelated spherical/von Mises-Fisher material, but no later answer
to this exact open question.
