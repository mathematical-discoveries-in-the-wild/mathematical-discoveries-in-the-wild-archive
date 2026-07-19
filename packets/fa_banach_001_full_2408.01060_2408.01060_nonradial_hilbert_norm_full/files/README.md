# Full Candidate: non-radial Hilbert-matrix norm

Status: candidate full solution, likely valid; human review recommended.

Source paper: Carlo Bellavita and Georgios Stylogiannis, "Hilbert matrix
operator Acting between conformally invariant spaces", arXiv:2408.01060.

Open question: Question 8.1 asks for the exact norm of
\[
\mathcal H:H^\infty\to M(\mathcal D_\mu)
\]
for non-radial positive Borel measures \(\mu\).

## Result

For positive Borel measures \(\mu\) satisfying the source paper's standing
assumption
\[
\int_{\mathbb D}(1-|w|^2)\,d\mu(w)<\infty,
\]
the Hilbert matrix operator is bounded
\[
\mathcal H:H^\infty\to M(\mathcal D_\mu)
\]
if and only if \(\mu(\mathbb D)<\infty\). In that case
\[
\|\mathcal H\|_{H^\infty\to M(\mathcal D_\mu)}
=1+\frac{\pi}{\sqrt2}\sqrt{\mu(\mathbb D)}.
\]

Thus the non-radial exact norm is the same finite-mass formula; infinite-mass
measures in the source class do not give bounded targets for \(\mathcal H\)
under the displayed \(U_\mu\)-based \(M(\mathcal D_\mu)\) norm.

## Packet Contents

- `main.tex`: review packet with theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2408.01060.
- `figures/open_problem_crop.png`: screenshot crop of Question 8.1 from page 18.
- `history/finite_measure_partial_packet/`: the earlier partial packet, if
  present after consolidation.

## Verification

The proof is analytic, not computational. The key review points are:

- Green-kernel invariance and Tonelli/Fubini:
  \[
  \int |g'|^2 U_\mu(\phi(z))\,dA(z)
  =\int \mathcal D_{\phi^{-1}(w)}(g)\,d\mu(w).
  \]
- The boundary-local BMOA limits for
  \(L(z)=\log(1/(1-z))\) and \(K(z)=\mathcal H(1)(z)\).
- The sigma-finite truncation argument showing that \(\mu(\mathbb D)=\infty\)
  forces \(\mathcal H(1)\notin M(\mathcal D_\mu)\).

## Novelty Check

Local indexes had only the earlier finite-measure partial packet for
arXiv:2408.01060. A bounded web search on June 18, 2026 for the arXiv id, the
paper title, "Question 8.1", "non-radial", "Hilbert matrix", and
\(M(\mathcal D_\mu)\) found the source paper and nearby Hilbert-matrix
papers/surveys, but no later exact answer to Question 8.1.
