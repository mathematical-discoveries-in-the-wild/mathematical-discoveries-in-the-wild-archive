# Partial result: semialgebraic stratified Hölder stability

Status: `partial_result_likely_valid`

Source paper: Giovanni S. Alberti, Angel Arroyo, Matteo Santacesaria, *Inverse problems on low-dimensional manifolds*, arXiv:2009.00574.

## Claim

The source asks whether its low-dimensional manifold stability theory can be
extended to generalized settings with boundary points and variable parameter
number, such as degenerate polygons.  A previous packet proves fixed-dimensional
boundary/corner stability, and a companion counterexample shows that arbitrary
smooth stratified frontier contact is too broad.

This packet proves a positive tame replacement.  Let \(P\subset\mathbb R^m\) be
a compact semialgebraic parameter set, let \(\iota:P\to X\) be a Hölder
parameterization into a Banach unknown space, and let \(G:P\to\mathbb R^N\) be a
continuous semialgebraic finite-measurement map.  If \(G\) is injective, then
there are \(C>0\) and \(\beta>0\) such that
\[
  \|\iota(p)-\iota(q)\|_X\le C |G(p)-G(q)|^\beta,\qquad p,q\in P.
\]

Thus compact semialgebraic stratified degeneracies admit Hölder stability from
injective finite measurements.  The proof does not require per-stratum
differential injectivity.

## Scope

This is a partial answer, not a full solution to the source's broad generalized
setting.  It applies to finite-dimensional semialgebraic measurement maps.
It does not cover arbitrary Banach-valued measurements, non-tame \(C^\infty\)
frontier flattening such as \(e^{-1/t}\), or analytic/o-minimal structures with
exponential flatness.

## Proof Idea

Apply the semialgebraic Łojasiewicz inequality on \(P\times P\) to
\[
  f(p,q)=|p-q|^2,\qquad g(p,q)=|G(p)-G(q)|^2.
\]
Injectivity gives \(g^{-1}(0)\subset f^{-1}(0)\), so \(f\le A g^\theta\) on the
compact semialgebraic set \(P\times P\).  Taking square roots and composing with
the Hölder parameterization gives the stated stability estimate.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2009.00574.
- `supporting_paper_1412.5088.pdf`: local copy of Kurdyka--Spodzieja--Szlachcinska on semialgebraic metric estimates.
- `figures/open_question_crop.png`: crop of the source conclusion bullet about boundary points and degenerate polygons.

## Novelty Check

Cheap run indexes were searched for `2009.00574`, `semialgebraic`,
`stratified`, `Lojasiewicz`, and `degenerate polygons`.  Existing hits are the
fixed-dimensional boundary/corner packet and the scoped frontier counterexample.

Web searches on 2026-06-28 for semialgebraic injective maps with Hölder inverse
and Łojasiewicz inequalities found standard semialgebraic metric results,
including Kurdyka--Spodzieja--Szlachcinska, but no packet or later answer
applying this directly to arXiv:2009.00574's stratified finite-measurement
question.

## Human Review Focus

Check that the semialgebraic finite-measurement hypothesis is explicit and that
the conclusion is not overstated beyond finite-dimensional/tame measurement
maps.
