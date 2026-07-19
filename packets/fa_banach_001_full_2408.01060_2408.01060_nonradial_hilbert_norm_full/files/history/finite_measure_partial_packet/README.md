# Partial Result: finite non-radial measures in Question 8.1

Status: candidate partial result, likely valid; human review recommended.

Source paper: Carlo Bellavita and Georgios Stylogiannis, "Hilbert matrix
operator Acting between conformally invariant spaces", arXiv:2408.01060.

Open question: Question 8.1 asks for the exact norm of the Hilbert matrix
operator
\[
\mathcal H:H^\infty\to M(\mathcal D_\mu)
\]
for non-radial positive Borel measures \(\mu\).

## Result

For every finite nonzero positive Borel measure \(\mu\) on \(\mathbb D\),
radial or not,
\[
\|\mathcal H\|_{H^\infty\to M(\mathcal D_\mu)}
=1+\frac{\pi}{\sqrt2}\sqrt{\mu(\mathbb D)}.
\]

This gives an exact non-radial subcase of Question 8.1. The infinite
non-radial case remains open.

## Packet Contents

- `main.tex`: review packet with theorem and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2408.01060.
- `figures/open_problem_crop.png`: screenshot crop of Question 8.1 from page 18.

## Verification

The proof is analytic, not computational. The main points for review are:

- the Green-potential identity
  \[
  \int |g'|^2 U_\mu(\phi(z))\,dA(z)
  =\int \mathcal D_{\phi^{-1}(w)}(g)\,d\mu(w);
  \]
- the boundary limits of the local BMOA seminorms for
  \(L(z)=\log(1/(1-z))\) and \(K(z)=\mathcal H(1)(z)\);
- the use of finite measure to pass the boundary limit through the
  \(\mu\)-integral by dominated convergence.

## Novelty Check

Local indexes had no exact prior record for arXiv:2408.01060. A bounded web
search on June 18, 2026 for the arXiv id, the paper title, and phrases around
"non-radial", "Hilbert matrix", and \(M(\mathcal D_\mu)\) found the source
paper and nearby Hilbert-matrix papers/surveys, but no later exact answer to
Question 8.1.
