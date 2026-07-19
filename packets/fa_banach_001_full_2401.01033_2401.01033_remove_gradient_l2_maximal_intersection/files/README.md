# Removing the gradient-L2 hypothesis in maximal intersection position

**Status:** `candidate_full_likely_valid`, pending human review.

This packet answers Remark 13 of Hoehner--Roysdon,
arXiv:2401.01033v3, affirmatively: the condition

```text
integral_{K_g} |grad g|^2 < infinity
```

is an artifact of the proof and can be removed from their Theorem 11.  All
other support/boundary regularity assumptions are retained.

The replacement is an automatic weighted-BV fact for integrable log-concave
functions:

```text
integral (1+|x|) d|Dg|(x) < infinity.
```

It follows from coarea and the convex scaling of sublevel sets.  In the compact
part of the source proof, this weighted `L1` bound replaces the sole
Cauchy--Schwarz estimate involving `grad g`.  In the unbounded-support
truncation, it gives dominated convergence for every bulk term; the Gaussian
correction is bounded by
`C delta integral |x|^2 g(x) dx`, which tends to zero.  The source's boundary
term convergence uses only the remaining support regularity and is unchanged.

The strengthening is strict: for `0 < alpha <= 1/2`, the one-dimensional
log-concave function `g(x)=x^alpha` on `(0,1]`, extended by zero, has interior
gradient in `L1` but not `L2`.

Contents:

- `solution_packet.pdf`, `main.tex`: full proof and verifier report
- `source_paper.pdf`: arXiv:2401.01033v3
- `figures/open_problem_crop.png`: source Remark 13 on PDF page 6
- `code/make_open_problem_crop.py`: reproducible crop helper
- ledger: `runs/fa_banach_001/ledger/results/2401.01033_remove_gradient_l2_maximal_intersection.json`

