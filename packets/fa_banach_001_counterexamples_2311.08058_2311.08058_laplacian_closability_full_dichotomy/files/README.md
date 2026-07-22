# Full-resolution packet: Laplacian closability and absolute continuity

Status: `candidate counterexample / full resolution`, likely valid, awaiting
human review.

## Source

- Giovanni Alberti, David Bate, and Andrea Marchese, *On the closability of
  differential operators*, arXiv:2311.08058v2, J. Funct. Anal. 289 (2025),
  111029.
- Source location: concluding Remark 1.7(iv), page 4.
- Source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

The source suggests that closability of the Laplacian from `L^p(mu)` to
`L^q(mu)` should force `mu << Lebesgue`.

## Full answer

Let `mu` be a positive Radon measure on `R^d` and let the Laplacian initially
act on `C_c^2(R^d)`.

- For every input exponent `1 <= p <= infinity` and every finite output
  exponent `1 <= q < infinity`, closability from `L^p(mu)` to `L^q(mu)` does
  force `mu << Lebesgue`.
- For output exponent `q=infinity`, the suggested implication is false.  For
  every `d >= 1`, the singular measure

  ```text
  mu = Lebesgue^d + delta_0
  ```

  makes the Laplacian closable from `L^p(mu)` to `L^infinity(mu)` for every
  `1 <= p <= infinity`.

Thus the source expectation has a complete endpoint dichotomy: it is true for
all finite output exponents and false at the strong `L^infinity` endpoint.

## Proof mechanism

For finite output exponent, closability makes the domain of the Banach adjoint
dense.  Every adjoint test function `phi` yields a measure
`nu=phi mu` whose distributional Laplacian is again a Radon measure.  A local
fundamental-solution argument then shows `nu` has a Lebesgue density.  Density
of the adjoint domain forces every compact restriction of `mu` to be
absolutely continuous.

At the `L^infinity` endpoint, adding Lebesgue measure changes the picture.
For continuous compactly supported functions, the `L^infinity(Lebesgue +
delta_0)` norm equals the ordinary supremum norm.  Hence convergence of the
Laplacians in the output is uniform.  Input convergence implies distributional
convergence to zero, so the uniform output limit must also be zero.

## Scope and supersession

This packet supersedes the earlier one-dimensional finite-output packet:

`solutions/partial/2311.08058_one_dimensional_constant_coefficient_closability_obstruction/`.

The result settles the necessary-condition question, not the converse:
absolute continuity by itself need not make the Laplacian closable for a
specified pair of exponents.

## Verification and novelty

The proof is analytic and uses no numerical computation.  A detailed logical
audit is in `verification.md`.  Local run indexes and bounded arXiv searches
through 2026-07-21 found the source paper but no later exact finite-output
theorem or `L^infinity` counterexample.  This is a bounded novelty check, not
an exhaustive bibliographic claim.

