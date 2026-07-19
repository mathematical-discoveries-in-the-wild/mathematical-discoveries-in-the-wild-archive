# Counterexample: frontier strata need separation data

Status: `counterexample_likely_valid_scoped`

Source paper: Giovanni S. Alberti, Angel Arroyo, Matteo Santacesaria, *Inverse problems on low-dimensional manifolds*, arXiv:2009.00574.

## Claim

The existing boundary/corner packet for this source covers fixed-dimensional
charts with boundary and corners.  It cannot be promoted to an unrestricted
variable-dimensional stratified theorem by simply asking for injectivity and
injective differentials on each stratum.

There is a compact stratified parameter set
\[
  K=[0,1]\subset\mathbb R
\]
with one open one-dimensional stratum and zero-dimensional endpoint strata, and a
continuous forward map
\[
  F(0)=0,\qquad F(t)=e^{-1/t}\quad (0<t\le 1),
\]
which is injective, smooth on each stratum, and has injective differential at
every point of the one-dimensional stratum.  Nevertheless no estimate
\[
  |s-t|\le C|F(s)-F(t)|^\alpha
\]
can hold on \(K\) for any \(C>0\) and any \(\alpha>0\).

## Scope

This is a scoped counterexample to the naive stratified extension, not a
counterexample to the source paper's stated theorems.  The source already has a
finite-union theorem for pairwise disjoint compact pieces; those pieces are
separated, so the frontier collapse displayed here is outside that theorem.

The result identifies the extra hypothesis needed for a true full stratified
extension: some quantitative inter-stratum separation, or an equivalent lower
rate controlling how measurements separate points approaching lower-dimensional
frontiers.

## Proof Idea

Along the one-dimensional stratum \((0,1)\), the derivative
\[
  F'(t)=t^{-2}e^{-1/t}
\]
is positive, so all usual per-stratum injectivity tests pass.  But as
\(t\downarrow0\), the measurement distance from the frontier point is
\(e^{-1/t}\), far smaller than any power of the parameter distance \(t\).
Thus \(t\le C e^{-\alpha/t}\) eventually fails for every \(C,\alpha>0\).

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2009.00574.
- `figures/open_question_crop.png`: crop reused from the boundary/corner packet, showing the source conclusion bullet about boundary points and degenerate polygons.

## Novelty Check

Cheap run indexes were searched for `2009.00574`, `stratified frontier`,
`variable-dimensional degeneracies`, `degenerate polygons`, and the existing
boundary/corner packet slug.  The only direct hit was the prior fixed-dimensional
partial result.

Web searches on 2026-06-28 for `2009.00574 stratified Holder stability`,
`Inverse problems on low-dimensional manifolds degenerate polygons`, and
`per-stratum injective differential Holder stability stratified` did not locate
a separate later answer or this obstruction.

## Human Review Focus

Check that the stratified class being refuted is stated narrowly enough:
continuous on the compact union, smooth on strata, injective on strata and
globally, with injective per-stratum differentials, but with no quantitative
frontier compatibility condition.
