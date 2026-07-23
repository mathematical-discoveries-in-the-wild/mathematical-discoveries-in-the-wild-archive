# All-support optimal one-level test functions

Status: `candidate_full_solution_likely_valid_needs_human_review`

This packet gives an exact finite matrix algorithm for the coefficient
problem left open in:

- Jesse Freeman and Steven J. Miller, arXiv:1507.03598, Section 6.
- Jesse Freeman, arXiv:1708.01588, Section 12.1.

After shifting the support interval to `[0,L]`, the algorithm partitions at
the breakpoints `(Z union (L+Z)) intersect [0,L]`. Translation by one
organizes the cells into one or two chains. On each chain, the differentiated
Fredholm equation is a constant-coefficient ODE with a skew tridiagonal
matrix. Matrix exponentials, cell-boundary continuity, and one
undifferentiated normalization equation give a square linear system.
Fredholm invertibility proves that the system is nonsingular for every
`L>0`.

Consequences:

- The normalized optimal factor and hence the optimal test function are
  computable for every positive support and all four classical compact
  symmetry types.
- Off integer `L`, the system has `2 floor(L)+1` unknowns; at integer `L`, it
  has `L` unknowns. With `L=2 sigma`, these dimensions exactly match
  Freeman's Corollary 9.9.
- The optimal infimum is continuous for all positive `sigma` and
  real-analytic away from integers and half-integers. This proves
  arXiv:1708.01588, Conjecture 12.1.

Files:

- `main.tex` and `solution_packet.pdf`: full proof and review packet.
- `source_paper.pdf`: arXiv:1507.03598.
- `supporting_paper_1708.01588.pdf`: the later finite-dimensional reduction
  and sharpened open problem.
- `figures/open_problem_crop.png`: source conjecture, page 16.
- `figures/supporting_open_problem_crop.png`: 2017 open coefficient problem
  and Conjecture 12.1, printed page 62.
- `code/verify_algorithm.py`: independent numerical residual checker.
- `VERIFICATION.md`: proof audit, numerical scope, and novelty bounds.

The bounded literature search found the 2017 partial result and the
restricted two-level extension arXiv:2011.10140, but no later all-support
coefficient algorithm or proof of Conjecture 12.1. Novelty therefore remains
subject to expert citation review.
