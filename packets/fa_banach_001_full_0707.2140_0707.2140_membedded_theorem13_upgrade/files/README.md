# M-embedded upgrade of Rao's Theorem 13

Status: candidate full result, likely valid

Source paper: T. S. S. R. K. Rao, "Nice surjections on spaces of operators", arXiv:0707.2140.

Target: Remark 14 asks whether the preceding theorem remains true when \(Y\) is assumed only to be an \(M\)-embedded space with strictly convex dual. The source says the proof would be completed if every into isometry of \(Y^*\) were weak-star continuous.

Result: yes, in the natural bidual formulation. If \(Y\) is \(M\)-embedded, then \({\mathcal K}(X,Y)^{**}\) is identified with \({\mathcal L}(X,Y^{**})\), so the upgraded conclusion is that the relevant surjection on \({\mathcal L}(X,Y^{**})\) is the bitranspose of a nice surjection on \({\mathcal K}(X,Y)\), hence has the form
\[
\Phi(S)=U^{**}SV .
\]
When \(Y\) is reflexive this reduces exactly to Rao's displayed conclusion on \({\mathcal L}(X,Y)\).

## Main Claim

Let \(X\) be reflexive and let \(Y\) be \(M\)-embedded. Assume \(X\) and \(Y^*\) are strictly convex, \(X\) is not isometric to a subspace of \(Y^*\), and \(Y^*\) is not isometric to a subspace of \(X^*\). Assume also the tensor identifications used in Rao's theorem:
\[
{\mathcal K}(X,Y)^* = X\widehat{\otimes}_{\pi}Y^*,
\qquad
{\mathcal K}(X,Y)^{**} = {\mathcal L}(X,Y^{**}),
\]
for instance under the metric-approximation and RNP hypotheses cited in the source.

If \(\Phi:{\mathcal L}(X,Y^{**})\to{\mathcal L}(X,Y^{**})\) is a bounded linear surjection whose adjoint preserves weak-star-continuous extreme points, then there are operators \(U\in{\mathcal L}(Y)\) and \(V\in{\mathcal L}(X)\), with \(U^*\) and \(V\) into isometries, such that
\[
\Phi(S)=U^{**}SV\qquad(S\in{\mathcal L}(X,Y^{**})).
\]
Equivalently, \(\Phi\) is the bitranspose of the nice surjection \(T\mapsto UTV\) on \({\mathcal K}(X,Y)\).

## Packet Contents

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of Remark 14.

## Verification Notes

The key new lemma is that if \(Y\) is \(M\)-embedded and \(Y^*\) is strictly convex, every into isometry \(J:Y^*\to Y^*\) is \(\sigma(Y^*,Y)\)-continuous. The proof uses the \(L\)-summand decomposition
\[
Y^{***}=Y^* \oplus_1 Y^\perp .
\]
This removes exactly the obstruction named in Remark 14. The rest of the argument is Rao's proof of Theorem 13, with \({\mathcal L}(X,Y)\) replaced by the correct bidual space \({\mathcal L}(X,Y^{**})\).

Human review should focus on the tensor-identification hypotheses. The packet states them explicitly rather than trying to sharpen the approximation-property assumptions beyond those used in the source.
