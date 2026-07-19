# Partial result: boundary/corner manifold stability

Status: `partial_result_likely_valid`

Source paper: Giovanni S. Alberti, Angel Arroyo, Matteo Santacesaria, *Inverse problems on low-dimensional manifolds*, arXiv:2009.00574.

## Claim

The source concludes with the open direction of extending its abstract inverse-problem theory from fixed-dimensional manifolds without boundary to more general settings with boundary points, motivated by degenerate polygons and varying parameter regimes.

This packet proves a fixed-dimensional boundary/corner extension of the source's abstract stability theorems. If the local charts take values in closed convex finite-dimensional models such as
\[
  [0,\infty)^m\times \mathbb R^{n-m},
\]
and the charted forward maps admit \(C^1\) extensions to open Euclidean neighbourhoods with injective differentials, then the source's compact-set Holder/Lipschitz stability theorem remains valid. The same chart replacement also preserves the finite-measurement stability theorem for \(Q_NF\).

## Scope

This is a partial answer to the source's boundary-manifold open question. It covers fixed-dimensional manifolds with boundary and corners under the natural extendable-\(C^1\) chart hypothesis.

It does not solve the harder variable-dimension or stratified degeneration problem, for example a compact parameter family in which triangles collapse into edges and vertices with changing local dimension. It also does not address the separate higher-order-derivative or nonlinear compressed-sensing questions from the source conclusion.

## Proof Idea

The source proof uses only two local facts:

1. nearby points of a compact \(K\) lie in one chart;
2. inside a chart, short line segments stay in the parameter domain, so the fundamental theorem of calculus applies.

Boundary and corner charts still have these facts when their model domains are relatively open subsets of closed convex sets. The line segment between two nearby chart points stays in the closed convex model, and compactness keeps it away from the relative boundary of the chart domain where the chart is not defined. Thus the finite-dimensional stability lemma used by the source works unchanged.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2009.00574.
- `figures/open_question_crop.png`: crop of the source conclusion bullet about boundary/degenerate manifolds.

## Novelty Check

Cheap run indexes were searched for `2009.00574`, `low-dimensional manifolds`, `manifold with boundary`, `manifold with corners`, `degenerate polygons`, and `M-RIP`. No prior packet or attempt for this source or route was found.

Web searches for exact phrases around `Inverse problems on low-dimensional manifolds` with `manifolds with boundary`, `degenerate polygons`, and `M-RIP manifold with boundary` did not locate a separate later answer.

## Human Review Focus

Check the definition of the boundary/corner \(C^1\) chart class and the finite-dimensional relative-domain lemma. The theorem is intentionally scoped to charts with \(C^1\) extensions to open Euclidean neighbourhoods; weakening that hypothesis would need additional one-sided differentiability bookkeeping.

