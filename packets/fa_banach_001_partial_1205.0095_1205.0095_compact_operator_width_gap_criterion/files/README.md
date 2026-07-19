# Compact Operator Width Gap Criterion

Status: `partial_result_likely_valid`

Source: Timur Oikhberg and Mikhail Ostrovskii, "Dependence of Kolmogorov widths on the ambient space", arXiv:1205.0095.

## Target

The packet addresses Problem 8.1 of the source paper:

> Let \(K\) be a compact in a Banach space \(X\) and \(T:X\to Y\) be
> a compact operator. Does it follow that \(d_n(TK)=o(d_n(K))\)?

## Contribution

Let
\[
\beta_r(T)=d_r(TB_X,Y)
\]
be the \(r\)-th Kolmogorov width of the compact image of the unit
ball. For every compact \(K\subset X\) and \(0\le r\le n\),
\[
d_n(TK,Y)\le \beta_r(T)\,d_{n-r}(K,X).
\]
Consequently, Problem 8.1 has a positive answer for every pair
\((T,K)\) satisfying
\[
\inf_{0\le r\le n}
\frac{\beta_r(T)d_{n-r}(K,X)}{d_n(K,X)}\longrightarrow 0.
\]

This strictly repackages and extends the mechanism of Proposition 8.3:
the source's slow finite-shift decay condition is the special case where
one fixes \(r\) after making \(\beta_r(T)\) small.

## Limitation

This is not a full solution of Problem 8.1. It isolates a precise
operator-adapted sufficient condition. The remaining obstruction is the
possible failure of the displayed infimum to tend to zero when the widths
of \(K\) have very large finite gaps.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1205.0095.
- `figures/open_problem_crop.png`: crop of Problem 8.1 from page 18.
- `code/crop_open_problem.py`: script that generated the crop.

