# Counterexample: unweighted sampling of continuous Schauder frames

Status: `counterexample_likely_valid`

Source problem paper: Joseph Eisner and Daniel Freeman, *Continuous Schauder frames for Banach spaces*, arXiv:1812.08360.

## Target

Problem 6.1 asks for Banach spaces where every bounded continuous Schauder frame may be sampled to obtain a discrete Schauder frame, and spaces where some bounded continuous Schauder frame cannot be sampled.

## Result

On the literal unweighted definition of sampling in the source paper, the one-dimensional Banach space already has a bounded continuous Schauder frame which cannot be sampled to obtain a discrete Schauder frame.

Take `X = R`, `M = [0,1]` with Lebesgue measure, and `x_t = 1`, `f_t = Id_R` for all `t`. Then

```text
x = integral_0^1 f_t(x) x_t dt
```

for every scalar `x`, so this is a bounded continuous Schauder frame. But any infinite sampling sequence `(t_j)` gives the discrete pair `(1, Id_R)` at every index, and the reconstruction series for `x=1` is `sum_j 1`, which diverges.

## Scope

This packet answers the second alternative of Problem 6.1 as written, and shows that unweighted sampling is too rigid even in dimension one.

It does **not** refute the intended Hilbert-frame discretization theorem with quadrature weights. If the problem is amended to allow positive sampling weights, the one-dimensional example is no obstruction.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1812.08360.
- `figures/open_problem_crop.png`: crop of Problem 6.1 from the source PDF.
- `solution_packet.pdf`: proof packet.

## Human Review Notes

Recommended review focus:

- Confirm that the source's formal definition of sampling uses the raw pairs `(x_{t_j}, f_{t_j})` with no weights.
- Decide whether the intended reading of Problem 6.1 should include sampling weights; under that amended reading this packet is only a wording counterexample, not a counterexample to weighted discretization.
