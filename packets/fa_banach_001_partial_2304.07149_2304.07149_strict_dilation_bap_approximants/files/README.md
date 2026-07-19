# Partial result: strict dilation approximants under BAP

Status: candidate partial result, likely valid.

Source: arXiv:2304.07149, R. Aron, V. Dimant, L. C. Garcia-Lirola, and M. Maestre, *Linearization of holomorphic Lipschitz functions*.

## Source Question

Question 1 asks whether `G_0(B_X)` has the BAP whenever `X` has the BAP.  The source notes the scaling obstruction: a bounded finite-rank approximation to `Id_X` may send `B_X` into a larger ball, so the MAP proof no longer controls the holomorphic-Lipschitz norm.

## Result

Let `X` have `lambda`-BAP.  For every `0 < r < 1/lambda`, the dilation operator

```tex
D_r delta(x) = delta(r x)
```

on `G_0(B_X)` lies in the strong operator closure of finite-rank operators of norm at most `r lambda`.

The proof factors `D_r` through finite-dimensional ranges of a `lambda`-BAP net.  For each finite-rank `A_alpha`, the map `x -> r A_alpha x` lands in the unit ball of the finite-dimensional range `E_alpha`.  The induced operator factors through `G_0(B_{E_alpha})`, and that middle space has MAP by the source theorem because `E_alpha` is finite-dimensional.

## Scope

This does not answer the endpoint `D_1 = Id`, so it does not solve Question 1.  It records a precise positive result below the boundary where the source obstruction disappears.  If `lambda=1`, letting `r` tend to `1` recovers the source MAP implication.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2304.07149.
- `figures/open_problem_crop.png`: crop of the source obstruction and Question 1.
- `code/make_open_problem_crop.py`: script used to generate the crop.

## Review Focus

Check the factorization through `G_0(B_{E_alpha})` and the strong-closure argument that replaces the middle identity by finite-rank MAP approximants without losing the `r lambda` norm bound.
