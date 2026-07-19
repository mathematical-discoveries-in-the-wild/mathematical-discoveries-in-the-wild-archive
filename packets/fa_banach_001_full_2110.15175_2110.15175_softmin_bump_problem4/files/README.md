# Soft-min bump solution for Problem 4 of arXiv:2110.15175

Status: candidate full solution likely valid.

Source paper: Y. A. Prykarpatskyy, P. Ya. Pukach, M. I. Vovk, and M. Gregus,
"Some remarks on smooth mappings of Hilbert and Banach spaces and their local
convexity property", arXiv:2110.15175v2, Axioms 13(4), 227, 2024.

Problem solved: the published Problem 4 asks whether, for the class `F_n` of
functions `f_n:l_infty(n)->[0,1]` supported in the open cube and satisfying
`omega(f;t)<=t` and `omega_2(f;t)<=t^2`, one has
`lim_n (1+epsilon_n)^n=infinity`, where
`epsilon_n=sup{||f_n||_infty:f_n in F_n}`.

Result: yes. For every `n>=2` the packet constructs an explicit
`f_n in F_n` with

```text
||f_n||_infty >= 1 / (8(6+8 log n)).
```

Therefore `n log(1+epsilon_n)` diverges, and so
`(1+epsilon_n)^n -> infinity`.

Construction: with `beta=2 log n`, set

```text
M_n(x) = -(1/beta) log sum_i exp(beta(x_i^2-1))
G_n(x) = (1/2) (max(M_n(x),0))^2
f_n(x) = G_n(x)/(6+4 beta).
```

The log-sum-exp term is a smooth lower approximation to the wall-distance
minimum `min_i(1-x_i^2)`. Positivity of `M_n` forces all coordinates to lie
strictly inside `(-1,1)`. On the positive set, the soft-min weights give
`|DM_n[h]| <= 2||h||_infty` and
`|D^2M_n[h,h]| <= (2+4 beta)||h||_infty^2`; composing with
`u -> (u_+)^2/2` and scaling proves the two modulus bounds.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: rendered page containing Problem 4.
- `code/check_softmin_bump.py`: deterministic numerical sanity check.

Novelty check: exact arXiv id/title, DOI, Problem 4 phrase, and the displayed
`epsilon_n` limit were searched in the local indexes/corpus and on the web on
2026-07-19. The hits found were the arXiv/MDPI/source versions and mirrors, not
a separate solution.

Human review recommendation: check the a.e. second-derivative argument for the
`C^{1,1}` cutoff `u_+^2/2` and the constants in the Hessian estimate. These are
standard one-dimensional absolutely-continuous estimates, but they are the main
technical point of the packet.
