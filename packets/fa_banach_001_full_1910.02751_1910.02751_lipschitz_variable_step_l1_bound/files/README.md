# Lipschitz variable-step mollifiers have the missing L1 bound

status: full_solution_likely_valid

source_arxiv: 1910.02751

source_paper: Michael Hintermuller, Kostas Papafitsoros, and Carlos N.
Rautenberg, *Variable step mollifiers and applications*

## Result

The source leaves open whether estimates (5.12)/(5.13), which give
`L^1`-boundedness of the variable-step mollifiers `T_n`, hold without the
quadratic boundary comparability condition

```text
kappa dist(x, boundary Omega)^2 <= eta(x) <= dist(x, boundary Omega)^2.
```

This packet proves a positive answer for the standard Whitney-type steps used
in the paper.  If `eta` is globally `L`-Lipschitz with `L < 1`, positive in
`Omega`, and small enough that the balls `B_{eta(x)/n}(x)` remain in `Omega`,
then

```text
sup_n sup_y int_Omega n^N / eta(x)^N 1_{B_{eta(x)/n}(x)}(y) dx < infinity.
```

Consequently the source estimate (5.12) holds and `T,T_n` are uniformly
bounded on `L^1(Omega)`.  The source's Whitney construction can be scaled so
that `||grad eta||_infty <= L < 1`, so no quadratic lower bound is needed.

## Evidence

- `main.tex` contains the proof packet.
- `solution_packet.pdf` is the rendered review packet.
- `source_paper.pdf` is a local render of the arXiv source.
- `figures/source_estimates_crop.png` shows source condition (5.11) and
  estimates (5.12)/(5.13).
- `figures/open_problem_crop.png` shows the source open-question note.
- `code/verify_lipschitz_kernel_bound.py` checks the one-dimensional formula
  for linear steps with `L<1` and illustrates failure at the borderline
  `L=1`.

## Human Review Recommendation

Review as a claimed full solution of the Section 5 open estimate in the
intended Whitney-step setting.  The key point to check is the two-sided
comparability of `eta(x)` and `eta(y)` on the set
`|x-y| < eta(x)/n`; everything else is an immediate volume estimate.
