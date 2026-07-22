# One-factor association of disjoint Wishart principal minors

Status: partial_result_likely_valid; human_review_needed

Source: Christian Genest, Frederic Ouimet, and Donald Richards,
*On the Gaussian product inequality conjecture for disjoint principal minors
of Wishart random matrices*, arXiv:2311.00202v3 (2024).

## Result

Both Conjecture 1.1 (positive determinant moments) and Conjecture 3.8
(lower-orthant correlation) hold for every real degree of freedom
\(\alpha>p-1\), arbitrary block sizes, all nonnegative real powers, and all
positive thresholds whenever the Wishart scale matrix has the coherent
one-factor form

\[
  \Sigma=\operatorname{diag}(D_1,\ldots,D_d)+aa^\mathsf T,
  \qquad D_i>0.
\]

The proof is stronger: every split product inequality holds for nonnegative
monotone functions of the block determinants, provided all functions have the
same monotonicity direction.

## Mechanism

The matrix determinant lemma gives an exact common-\(\chi^2_\alpha\) mixture
of independent rank-one noncentral Wishart blocks. A rank-one noncentral
Bartlett/Schur factorization shows that each conditional block determinant is
stochastically increasing in the common scalar. Chebyshev association on that
one scalar then proves both conjectures.

## Scope

The unrestricted conjectures remain open. For several latent factors the
mixing parameter is matrix-valued and has no total order compatible with the
argument; the present proof does not reduce a general positive definite scale
matrix to the one-factor case.

## Packet contents

- main.tex and solution_packet.pdf: theorem, proof, scope, and audit.
- source_paper.pdf: arXiv:2311.00202v3.
- figures/: readable source crops of Conjectures 1.1 and 3.8.
- code/verify_one_factor_mixture.py: noninteger-degree Monte Carlo checks.
- code/make_source_crops.py: reproducible source-crop generator.
- verification_report.md: proof and computation audit.

