# Counterexample packet: exterior winding-zero does not force closedness

status: counterexample_likely_valid

source_arxiv: 1012.5542

source_problem: Remark 3.7.2 of Harrison Pugh, "Applications of Differential
Chains to Complex Analysis and Dynamics", conjectures that the hypothesis that
\(J\) be closed in the generalized Cauchy residue theorem may be unnecessary,
and specifically says that \(\operatorname{Ind}_J(w)=0\) on \(U^c\) should
imply \(\partial J=0\).

counterexample: a compactly supported gradient-vector-field differential
1-chain \(J=\xi_{(1/2)\nabla\phi,dA}\) in a disk \(U\).

## Summary

Let \(U\subset\mathbb C\) be a bounded disk and choose a nonconstant real
bump function \(\phi\in C_c^\infty(U)\). Define the smooth compactly supported
vector field
\[
  X=\frac12(\phi_x\partial_x+\phi_y\partial_y)
\]
and let \(J\) be the differential 1-chain represented by \(X\) against planar
Lebesgue measure:
\[
  \int_J \omega=\int_U \iota_X\omega\,dA .
\]

For every \(w\in U^c\), the Cauchy kernel \(1/(z-w)\) is holomorphic near
\(\operatorname{supp}\phi\), and
\[
  \int_J \frac{dz}{z-w}
  =
  \int_U \frac{\partial_{\bar z}\phi(z)}{z-w}\,dA(z)
  =
  \int_U \partial_{\bar z}\!\left(\frac{\phi(z)}{z-w}\right)dA(z)
  =0 .
\]
Thus \(\operatorname{Ind}_J(w)=0\) for all \(w\in U^c\). However
\[
  \int_{\partial J}\phi=\int_J d\phi
  =\frac12\int_U |\nabla\phi|^2\,dA>0,
\]
so \(\partial J\ne0\). This disproves the stated implication
"exterior index zero should imply closedness".

## Scope

This packet does not claim to disprove the residue formula after removing
closedness. It only disproves the proposed route for removing closedness.
Also, if the theorem's existing assumption \(\partial K=J\) is kept, then
closedness is already automatic from \(\partial^2K=0\). The finite-mass
condition on \(K\) is not addressed here.

## Additional diagnostic

The source thesis and the later paper arXiv:1101.0385 state a generalized
Cauchy integral formula without explicitly assuming that \(J\) is closed,
while the proof invokes a Cauchy integral theorem that does assume
\(\partial J=0\). A classical oriented segment \(J=[a,b]\) and
\(f(\zeta)=\zeta-z\) give a simple failure of that formula as written:
the left side is \(0\), while the right side is \((b-a)/(2\pi i)\ne0\).
This diagnostic is included for human review context, not as the main result
counted by this packet.

## Evidence

- `source_paper.pdf`: Harrison Pugh, "Applications of Differential Chains to
  Complex Analysis and Dynamics", arXiv:1012.5542.
- `supporting_paper_1101.0385.pdf`: Jenny Harrison and Harrison Pugh,
  "Generalizations of the Cauchy Integral Theorems", arXiv:1101.0385.
- `figures/open_problem_crop.png`: crop of Remark 3.7.2 on thesis PDF page 45.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet, once compiled.

## Novelty Check

Bounded local and web search on 2026-07-18 found no duplicate packet for
arXiv:1012.5542 or for the phrase "Ind_J(w)=0" together with "partial J",
"closed", and "differential chains". Local registry search found only a
related metric-current/Banach-flat-chain packet for arXiv:2508.08017, not this
target. Web searches for the exact Remark 3.7.2 phrase and close variants
returned the source thesis or the later Cauchy-integral-theorems paper, but no
known counterexample to the implication.

## Human Review Recommendation

Check that the vector-field chain \(\xi_{X,dA}\) is accepted in the intended
\(\hat{\mathcal B}_1^1(\mathbb R^2)\) class in the local compact-support sense
used by the source. The proof uses only the source's standard vector-field
chain representation and Stokes boundary convention. If that membership is
accepted, the counterexample is direct.
