# Partial result: W.A.P. lifting for Lp-tight Bochner weakly compact sets

Status: `partial_likely_valid`

Source paper: Edward Odell and Hans-Olav Tylli, *Weakly compact approximation in Banach spaces*, arXiv:math/0309405.

## Claim

Problem 5.7 of the source asks whether
\[
  L^p([0,1];E)
\]
has the W.A.P. whenever \(E\) has the W.A.P. and \(1<p<\infty\), and asks the analogous question for the inner W.A.P.

This packet proves the W.A.P. conclusion for every weakly compact set \(D\subset L^p(\mu,E)\) satisfying the following \(L^p\)-tightness condition: for every \(\eta>0\) there is a weakly compact \(W\subset E\) such that
\[
  \sup_{f\in D}\left(\int \operatorname{dist}(f(\omega),W)^p\,d\mu(\omega)\right)^{1/p}<\eta.
\]
For such \(D\), any weakly compact approximant \(S:E\to E\) for \(W\) lifts to the Bochner operator
\[
  \widetilde S f(\omega)=S(f(\omega)),
\]
and \(\widetilde S\) is weakly compact on \(L^p(\mu,E)\).

Consequently, the W.A.P. half of Problem 5.7 reduces to proving this \(L^p\)-tightness condition for arbitrary weakly compact subsets of \(L^p([0,1];E)\), or to finding another way to handle the non-tight part.

## Scope

This is not a full solution of Problem 5.7. The supporting literature on \(\delta\mathcal S\)-sets shows that weak compactness in Bochner spaces does not generally imply simple weak-compact range control. In particular, Rodriguez notes that the stronger \(L^p\)-neighborhood condition fails for spaces such as \(X=\ell^1\) or \(X=L^1[0,1]\). The packet therefore records a genuine lifting lemma and a reduction, not a claimed full permanence theorem.

The same argument gives a concrete corollary for uniformly essentially bounded \(\delta\mathcal S\)-sets.

## Proof Idea

If \(f(\omega)\) is close in \(L^p\)-mean to a weakly compact set \(W\subset E\), and \(S\) approximates the identity on \(W\), then
\[
  \|f-\widetilde S f\|_p
  \le \sup_{w\in W}\|w-Sw\| + (1+\|S\|)\|\operatorname{dist}(f,W)\|_p.
\]
Weak compactness of \(\widetilde S\) follows from the Davis-Figiel-Johnson-Pelczynski factorization of \(S\) through a reflexive space \(R\), because \(L^p(\mu,R)\) is reflexive for \(1<p<\infty\).

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:math/0309405.
- `supporting_paper_1611.07199.pdf`: local copy of Rodriguez, *A class of weakly compact sets in Lebesgue-Bochner spaces*.

## Human Review Focus

Check the \(L^p\)-tightness formulation, the lifted-operator weak compactness via DFJP factorization, and the scope statement. The important open point is whether Problem 5.7 can be pushed beyond the tight/\(\delta\mathcal S\)-controlled regime.
