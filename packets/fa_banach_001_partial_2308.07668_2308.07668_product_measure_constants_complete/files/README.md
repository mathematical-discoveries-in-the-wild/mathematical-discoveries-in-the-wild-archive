# Complete Product-Measure Lp Constants

Status: `partial` result for arXiv:2308.07668, with a literature-supported
finite extremal step.

This packet consolidates the previous product-measure constant packet and
finishes the remaining finite `1<p<2` case by identifying the finite atom
problem with the largest Rayleigh quotient of the complete graph `p`-Laplacian.
The needed complete-graph spectrum is Amghibech's theorem, quoted in Zhang,
arXiv:2110.06054, Section 4.3.

## Claims

For the constants `c_n` and `c` in Proposition 55 of the source paper, for
every `n >= 1`:

```text
c_n^p = 2 - (4 - 2^p)/2^n      for 1 < p <= 2,
c_n^p = 2^(p-1)                for 2 <= p < infinity.
```

Consequently:

```text
c = 2^(1/p)       for 1 < p <= 2,
c = 2^(1-1/p)     for 2 <= p < infinity.
```

At `p=2` the two formulas agree.

## Evidence

- Source paper: `source_paper.pdf`.
- Open-question crop: `figures/open_problem_crop.png`, page 25 of the arXiv PDF.
- Supporting paper: `supporting_paper_2110.06054.pdf`.
- Packet PDF: `solution_packet.pdf`.
- Numerical check script: `code/check_finite_atom_conjecture.py`.

## Method

The source constants reduce to finite complete-graph quotients

```text
sup_x sum_{i,j} |x_i-x_j|^p / sum_i |x_i|^p.
```

For `1<p<2`, Amghibech's complete-graph `p`-Laplacian spectrum shows that the
largest normalized quotient is attained by the `i=j=1` eigenvalue, giving the
two-opposite-spikes value. For `p>2` and `N=2^n`, the same spectrum is maximized
by a balanced bipartition, giving the Rademacher value.

Overlap patterns in the source paper are handled by conditioning on common
coordinates; the free part is a smaller finite cube, and the constants are
monotone in the needed direction.

## Scope

This completes the exact constant part of the source question. It does not
resolve the endpoint dichotomy of `S_{L_p({0,1}^kappa)}` for `p != 2`; that
remains the hard open core.

## Human Review Recommendation

Check the normalization between the ordered pair quotient and the normalized
graph `p`-Laplacian quotient, then check the elementary maximization of
Amghibech's formula over the integer parameters. The finite `1<p<2` step is
not claimed as newly discovered independent of the graph-spectrum literature.
