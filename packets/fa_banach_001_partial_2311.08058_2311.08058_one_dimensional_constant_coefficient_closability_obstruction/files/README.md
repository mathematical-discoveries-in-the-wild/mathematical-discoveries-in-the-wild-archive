# Partial Solution Packet: one-dimensional higher-order closability obstruction

Status: `candidate partial`, likely valid, awaiting human review.

**Superseded:** the source question has now been fully resolved, including all
dimensions for finite output exponent and a counterexample at the strong
`L^infinity` endpoint.  See
`solutions/counterexamples/2311.08058_laplacian_closability_full_dichotomy/`.

## Source question

- Giovanni Alberti, David Bate, and Andrea Marchese, *On the closability of
  differential operators*, arXiv:2311.08058v2, J. Funct. Anal. 289 (2025),
  111029.
- Source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`, page 4, concluding
  Remark 1.7(iv).

The source suggests that closability of the Laplace operator
`C_c^2(R^d) -> L^q(mu)`, with input topology from `L^p(mu)`, should force
`mu << Lebesgue`, but notes that this does not follow easily from the paper's
first-order methods.

## Claimed partial result

In dimension one the suggested necessary condition holds for every input
exponent `1 <= p <= infinity` and every finite output exponent
`1 <= q < infinity`.  More strongly, it holds for every nonzero
constant-coefficient scalar differential operator of every positive order:
if

```text
P(D) = a_0 + a_1 D + ... + a_m D^m,  m >= 1,  a_m != 0,
```

is sequentially closable from `L^p(mu)` to `L^q(mu)` on
`C_c^infinity(R)`, then `mu` is absolutely continuous with respect to
Lebesgue measure.

## Proof idea

If `mu` has a nonzero singular part, choose a compact Lebesgue-null set `K`
with `mu(K)>0`.  Smooth cutoffs `g_n` can equal one on `K` while having
arbitrarily small Lebesgue support and arbitrarily small `mu`-mass off `K`.
Correct `g_n` by tiny fixed bumps away from `K` so that its first `m` moments
vanish.  The `m`-fold primitive `u_n` is then compactly supported.  Its lower
derivatives converge uniformly to zero, while `u_n^(m)` converges in
`L^q(mu)` to `1_K`.  Consequently `u_n -> 0` in every `L^p(mu)`, but
`P(D)u_n -> a_m 1_K != 0`, contradicting closability.

## Scope

This resolves the one-dimensional, finite-output-exponent subcase of the
source's Laplacian question.  It does not address dimensions `d >= 2`, the
output space `L^infinity(mu)`, or sufficiency when `mu` is absolutely
continuous.

## Verification

The proof is analytic; no numerical computation is used.  The detailed audit
is in `verification.md`.  The main review points are the invertible moment
matrix, compact support of the moment-corrected primitive, and strong
`L^q(mu)` convergence of the corrected cutoffs.

## Novelty check

The local run indexes were searched for arXiv:2311.08058, second-order
closability, Laplacians, and higher-order constant-coefficient operators.  A
bounded arXiv search through 2026-07-21 used the phrases “second derivative
closable Radon measure”, “Laplacian closable absolutely continuous measure”,
“higher order differential operator weighted Lp closability”, and close
variants.  It found the source paper but no later exact answer.  This is a
bounded search, not a claim of exhaustive bibliographic novelty.
