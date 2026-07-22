# Candidate full solution: classification of two-block q-balls

Status: **candidate full solution, likely valid, needs expert review**

Source: Boris Rubin, *Intersection Bodies and Generalized Cosine
Transforms*, arXiv:0704.0061v2 (2007), Section 7, printed page 34.

## Result

Let (1\leq \ell<n), (q>2), (0<\lambda<n), and

\[
B^n_{q,\ell}=\{(x',x'')\in\mathbb R^{n-\ell}\oplus\mathbb R^\ell:
|x'|^q+|x''|^q\leq 1\}.
\]

The packet proves the full classification

\[
B^n_{q,\ell}\in\mathcal I^n_\lambda
\quad\Longleftrightarrow\quad
\lambda\geq \max(n-\ell,\ell)-2.
\]

In particular, Rubin's open problem has an affirmative answer throughout
the stated interval

\[
\max(n-\ell,\ell)-2<\lambda<n-3.
\]

Rubin's Proposition 7.5 already gives non-membership below the threshold.
The new direction has two ingredients:

1. The norm power ((|x'|^q+|x''|^q)^{-\lambda/q}) is an exact positive
   mixture of anisotropic copies of
   \(\max(|x'|,|x''|)^{-\lambda}\).
2. A Weber--Schafheitlin calculation shows that the latter distribution is
   positive definite precisely in the needed range.  Euler's transformation
   turns the relevant hypergeometric factor into a power series with positive
   coefficients.  At the threshold, positivity follows by closure in the
   tempered-distribution topology.

## Files

- `solution_packet.pdf`: complete theorem, proof, source evidence, checks,
  limitations, and references.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: Rubin's original paper.
- `supporting_paper_1004.5518.pdf`: Wrochna's Weber--Schafheitlin reference.
- `figures/open_problem_crop.png`: real crop of printed page 34.
- `code/verifier.py`: reproducible numerical and algebraic sanity checks.
- `VERIFICATION.md`: verification transcript and reviewer checklist.

## Human-review priority

The principal item to audit is Lemma 2 in the packet: the use of the
Weber--Schafheitlin formula by Abel regularization/analytic continuation and
the assertion that, because its exponent is (<1), the resulting
distribution has no additional cone-supported term.  The displayed formula,
its Gamma signs, the local-integrability exponents, the mixture identity, and
the endpoint closure have all been independently checked in the packet.

## Novelty status

A bounded search on 2026-07-22 covered exact formula fragments, the source
title and arXiv id, the author's related papers, citation titles attached to
the source DOI, and combinations of "(q,l)-ball", "lambda-intersection
body", and the threshold `max(n-l,l)-2`.  It found the original question and
nearby intersection-body literature, but no later solution or this product
mixture argument.  This is evidence only, not a claim of exhaustive novelty.

