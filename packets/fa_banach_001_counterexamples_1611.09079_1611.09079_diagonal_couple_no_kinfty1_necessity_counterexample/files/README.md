# Diagonal-couple counterexample to pairwise necessity of \(K_{\infty,1}\)

Status: likely valid counterexample, with an explicit scope limitation.

Source paper: Yves Raynaud and Pedro Tradacete, *Calderon-Lozanovskii interpolation on quasi-Banach lattices*, arXiv:1611.09079.

## Source question

Remark 5.8 of the source paper asks whether the \(K_{\infty,1}\) hypothesis in Corollaries 5.1 and 5.6 is actually necessary. Those corollaries say that if the target endpoint lattices \(Y_0,Y_1\) have \(K_{\infty,1}\), then the Calderon-Lozanovskii methods \(\varphi^c\) and \(\varphi^0\) are interpolation functors for endpoint-bounded operators.

## Counterexample

The literal pairwise necessity statement is false. Let \(E\) be the non-\(K_{\infty,1}\) quasi-Banach lattice constructed in Example 4.3 of the source paper. Take the target couple to be the diagonal couple
\[
(Y_0,Y_1)=(E,E).
\]
Then, for every normalized \(\varphi\in\mathcal P\),
\[
\varphi(E,E)\simeq E,\qquad
\varphi^c(E,E)\simeq E,\qquad
\varphi^0(E,E)\simeq E.
\]
Consequently every endpoint-bounded operator
\[
T:(X_0,X_1)\to(E,E)
\]
is automatically bounded from \(X_0+X_1\) to \(E\), hence bounded
\[
T:\varphi^c(X_0,X_1)\to\varphi^c(E,E)
\]
and, by restriction,
\[
T:\varphi^0(X_0,X_1)\to\varphi^0(E,E).
\]
Thus the conclusions of Corollaries 5.1 and 5.6 hold for this target couple although neither endpoint has \(K_{\infty,1}\).

## Scope limitation

This is deliberately a diagonal-couple counterexample. It disproves the literal statement that \(K_{\infty,1}\) is necessary for each target couple satisfying the corollary conclusions. It does not settle a stronger non-degenerate or category-level necessity problem, for example a classification of all target couples for which these functoriality conclusions hold, or a condition excluding diagonal collapse.

## Novelty and duplicate checks

Cheap run indexes were searched for `1611.09079`, `Calder`, `Lozanovskii`, and `K_{\infty,1}`. No existing packet for this question was found. A bounded web search on 2026-06-20 for the exact \(K_{\infty,1}\)/Calderon-Lozanovskii necessity phrases only surfaced the source paper.

## Files

- `main.tex`: self-contained proof note.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: compiled local source paper.
- `figures/open_problem_crop.png`: crop of Remark 5.8 from the source PDF.
- `code/crop_open_problem.py`: reproducibility helper for the crop.
