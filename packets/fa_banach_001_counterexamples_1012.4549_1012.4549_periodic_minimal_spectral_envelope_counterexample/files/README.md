# A period-two counterexample to Question 3.4 of arXiv:1012.4549

Status: `candidate_counterexample_likely_valid`

Source: Wayne Lawton, *The Feichtinger Conjecture for Exponentials*,
arXiv:1012.4549; published in *Journal of Nonlinear Analysis and Optimization:
Theory & Applications* 2(1) (2011), 131--140. The rendered source PDF asks
Question 3.4 on page 5 (the TeX source label is `qn:3.1`).

## Full literal negative answer

Question 3.4 asks, for a set `F` whose characteristic sequence is minimal,
whether every extreme point of its spectral envelope `S(F)` belongs to the
correlation-measure class `Sigma(F,zeta)`.

Take the nonconstant periodic minimal set

\[
F=2\mathbb Z.
\]

Its symbolic orbit consists of the even and odd indicator sequences, and its
unique invariant probability `zeta` assigns mass `1/2` to each. The cylinder
`X_1(F)` contains only the even indicator. Consequently every function
supported on `X_1(F)` has correlations equal to a constant on even lags and
zero on odd lags. Therefore

\[
\Sigma(F,\zeta)
=\left\{a\,\frac{\delta_0+\delta_{1/2}}2:a\geq0\right\}.
\]

On the other hand,

\[
\mu_* = \frac{\delta_{1/4}+\delta_{3/4}}2
\]

belongs to `S(2Z)`: it is the weak-star limit of squared moduli of normalized
polynomials

\[
f_N(t)=\frac1{\sqrt N}\sum_{k=0}^{N-1}e^{2\pi i k(2t-1/2)}
\]

whose frequencies all lie in `2Z`. Every measure in `S(2Z)` is invariant
under translation by `1/2`, and `mu_*` is extreme among all such invariant
probabilities because it is the uniform probability on a single two-point
orbit. Hence `mu_*` belongs to `S_e(F)` but not to `Sigma(F,zeta)`.

Thus Question 3.4 is false as written, even for a nonconstant minimal
sequence.

## Scope

This counterexample uses a periodic minimal sequence. If the intended question
was restricted to aperiodic systems, or specifically to the Thue--Morse
sequence motivating the surrounding discussion, that stronger variant is not
answered here.

## Files and review

- `solution_packet.pdf`: self-contained proof packet with source evidence.
- `main.tex`: packet source.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: complete source definition and question.
- `VERIFICATION.md`: stepwise independent proof check.

A bounded search through 2026-07-22 covered the run indexes, local source
corpus, exact formulas and wording from Question 3.4, the title and author, and
the later arXiv:1204.4904 spectral-envelope report. No prior explicit answer
was found. This supports but does not certify novelty.

Recommended human review: confirm that the quantifier in Question 3.4 is
literal and does not carry an unstated aperiodicity convention from the
Thue--Morse motivation.

