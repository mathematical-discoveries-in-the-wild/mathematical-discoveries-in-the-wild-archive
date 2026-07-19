# Partial packet: Conjecture 5.2 for \(k=1\)

status: partial_result_likely_valid

source_arxiv: 2512.17706

source_problem: Conjecture 5.2 of Bluhm--Evert--Klep--Magron--Nechita, asking for the all-level optimum of a free-spectrahedral inclusion optimization for the Cartesian product of a line and a \(k\)-simplex.

result: the conjecture holds for \(k=1\), i.e. for the matrix square and its dual matrix diamond.

## Summary

For \(k=1\), the source free spectrahedron \(\mathcal D_{A(1)}\) is the two-variable matrix cube:
\[
  \mathcal C_2(n)=\{(X_1,X_2): X_i=X_i^*,\ -I\le X_i\le I\}.
\]
Its dual free polytope is the matrix diamond:
\[
  \mathcal D_2(n)=\{(Y_1,Y_2): \pm Y_1\pm Y_2\preceq I
  \text{ for all signs}\}.
\]
The packet proves
\[
  \sup_{X\in\mathcal C_2,\ Y\in\mathcal D_2}
  \lambda_{\max}(X_1\otimes Y_1+X_2\otimes Y_2)=\sqrt2,
\]
which is exactly \(\gamma(1)=2/(0+\sqrt2)=\sqrt2\) in Conjecture 5.2.

The upper bound is a two-line operator Cauchy-Schwarz estimate: write
\[
  A=Y_1+Y_2,\quad B=Y_1-Y_2,\quad
  P=(X_1+X_2)/2,\quad Q=(X_1-X_2)/2.
\]
Then \(A,B\) are contractions and \(P^2+Q^2\le I\), so
\[
\|P\otimes A+Q\otimes B\|
\le \|P^2+Q^2\|^{1/2}\|A^2+B^2\|^{1/2}\le \sqrt2.
\]
Equality is achieved by the usual Pauli/CHSH choice.

## Evidence

- `source_paper.pdf`: Bluhm--Evert--Klep--Magron--Nechita, "Inclusion constants for free spectrahedra with applications to quantum incompatibility", arXiv:2512.17706.
- `figures/conjecture_5_2_crop.png`: crop of source Conjecture 5.2 on PDF page 31.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, once compiled.

## Novelty Check

Bounded search on 2026-07-18 found no exact prior run packet for arXiv:2512.17706. The result is a modest subcase and sits close to known matrix cube / matrix diamond dilation facts and the standard two-observable Tsirelson bound. Web searches for the source arXiv id, `kSimplexPlusLineOptimum`, `matrix square inclusion constant sqrt(2)`, `matrix cube matrix diamond sqrt 2 inclusion constant`, and two dichotomic compatibility degree phrases did not find a later paper explicitly resolving Conjecture 5.2, but did find adjacent known matrix convexity literature. The packet therefore claims only a small partial subcase, not novelty for the broader conjecture.

## Human Review Recommendation

Check that the source's \(k=1\) specialization is indeed the matrix square and that the displayed sign constraints are exactly the matrix diamond. The operator inequality itself is elementary; equality is the Pauli/CHSH calculation.
