# Conditional split-module lift criterion for Read's ordinary Calkin algebra

Status: `conditional_reduction`.

Source target: Richard Skillicorn, arXiv:1507.08118, Remark 2.6, asking
whether the ordinary Calkin algebra
`B(E_R)/K(E_R)` of Read's space has a unique complete norm.

## Result

This packet proves an abstract lifting criterion for strongly split extensions
of the form
\[
0\to J\to A\to \widetilde E\to 0,
\]
where \(E\) has zero product.  If a non-equivalent complete norm on the
radical coordinate \(E\) makes the two \(E\)-module actions on \(J\) bounded,
then the split algebra \(A\) has a non-equivalent complete algebra norm.

Applied to Read's ordinary Calkin algebra, Laustsen--Skillicorn's split theorem
gives
\[
0\to W(E_R)/K(E_R)\to B(E_R)/K(E_R)\to \ell_2^\sim\to 0.
\]
Thus Skillicorn's question has a negative answer if the split \(\ell_2\)
coordinate admits a non-equivalent complete norm that still controls the left
and right module actions on \(W(E_R)/K(E_R)\).  A particularly checkable
subcase is: if the common annihilator in \(\ell_2\) of those two module
representations is infinite-dimensional, then \(B(E_R)/K(E_R)\) lacks a unique
complete norm.

## Literature status

- Skillicorn proves the weak Calkin algebra \(B(E_R)/W(E_R)\) has at least two
  non-equivalent complete algebra norms, and explicitly leaves the ordinary
  Calkin case open.
- Laustsen--Skillicorn later prove the strong split exact sequence
  \(B(E_R)\to \ell_2^\sim\) with kernel \(W(E_R)\).
- Ware's thesis shows the quotient norm on \(B(E_R)/K(E_R)\) is not maximal,
  hence the ordinary Calkin algebra does not have a unique algebra norm.  This
  uses a discontinuous derivation and does not by itself produce a non-equivalent
  complete norm.
- Arnott--Laustsen record that Read's weak Calkin algebra fails both maximality
  and incompressibility; this again concerns the weak Calkin quotient rather
  than the ordinary Calkin algebra.

No later literature located in this push answers Remark 2.6 outright.

## Conditional dependencies

The packet does not prove the module-boundedness hypothesis for Read's space.
The verifier should focus on the maps
\[
\xi\mapsto (j\mapsto \rho(\xi)j),\qquad
\xi\mapsto (j\mapsto j\rho(\xi))
\]
from \(\ell_2\) into operators on \(W(E_R)/K(E_R)\), where \(\rho\) is the
Laustsen--Skillicorn splitting.  Proving an infinite-dimensional common kernel,
or proving boundedness after a weaker complete renorming of \(\ell_2\), would
upgrade this conditional packet into a full negative answer.

## Files

- `main.tex`: conditional theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: Skillicorn, arXiv:1507.08118.
- `supporting_paper_1602.08963.pdf`: Laustsen--Skillicorn split theorem.
- `supporting_thesis_ware_2014.pdf`: Ware thesis, used for the ordinary
  Calkin non-maximality literature status.
- `figures/open_problem_crop.png`: crop of Skillicorn Remark 2.6.

Human-review recommendation: check the abstract lifting proof first; then
inspect the Read-space module action for the common-kernel or weaker-norm
boundedness condition.
