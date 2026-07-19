# Verification report

Candidate: arXiv:2601.17896, Remark 1.3, joint smooth approximation in the
uniformly positive weighted regime.

## Verdict

Likely valid full result under the `alpha >= c > 0` hypothesis explicitly
invoked immediately before the source question. Mathematical confidence:
86/100. Novelty confidence after a bounded search: 67/100.

If the source intended to include weights that may vanish, the result is a
strong partial rather than a full answer. The packet states this interpretive
boundary throughout.

## Claim checked

For every rough or unbounded `alpha in L^1` with `alpha >= c > 0` and every
positive Radon measure `mu` inducing a compact trace from `H^1(1,alpha)`, one
can jointly smooth the pair to strictly positive smooth densities while
preserving all variational eigenvalues in the limit. `L^r` convergence of the
weights holds whenever `alpha in L^r`, so normalized eigenvalues converge in
the range used by the source.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Compact trace implies the Ehrling estimate | valid | The contradiction normalization gives bounded energy, vanishing ordinary `L^2`, weak limit zero, and then strong convergence under the compact trace. |
| Global spanning-flow smoothing has a smooth kernel | likely valid | Finitely many global fields span every tangent space. The parameter-to-manifold map is a uniform submersion near zero; fiber integration gives a jointly smooth kernel. |
| Jointly averaged energy is comparable to the scalar smoothed energy | valid | The only discrepancy is `D Phi_z`; smooth closeness to the identity gives the multiplicative `1+O(t)` metric comparison, independent of the size of `alpha`. |
| The smoothed family inherits a uniform Ehrling estimate | valid | Apply the limiting estimate to `u o Phi_z`, average, and use the preceding comparison. The vanishing positive volume component is harmless. |
| Energy forms Mosco-converge | valid | Uniform lower ellipticity bounds gradients in ordinary `L^2`; `sqrt(alpha_n) -> sqrt(alpha)` in `L^2` identifies the weak flux limit. Smooth diagonal recovery follows from the definition of `H^1(1,alpha)`. |
| Moving mass norms converge on bounded-energy sequences | valid | Smooth approximation of the limit plus the uniform Ehrling estimate controls the residual. The order of choices is: bounded-energy approximants, then small epsilon, then sufficiently accurate approximation. |
| Uniform coercivity for smooth eigenfunctions | valid | Ordinary Poincare controls the mean-zero part; the uniform trace inequality controls its moving mass; total mass controls the constant part. |
| Eigenvalue limsup | valid | A finite-dimensional simultaneous recovery makes both energy and mass Gram matrices converge. |
| Eigenvalue liminf | valid | First smooth eigenfunctions are uniformly bounded, converge strongly in ordinary `L^2`, remain mass-orthonormal in the limit, and satisfy the limiting Rayleigh bound by energy lower semicontinuity. |
| Normalized convergence | valid | Total mass is preserved and `alpha_n -> alpha` in `L^{p/(p-2)}`. The `p=2` case keeps `alpha_n=1`. |

## Adversarial checks

- Weak-star smoothing by itself yields only `limsup lambda_n <= lambda`; the
  proof supplies the missing liminf through collective compactness.
- The construction does not require a pointwise upper bound on `alpha`.
  Metric distortion is multiplicative before integration.
- It does not claim operator-norm convergence of the energy forms, which can
  be false for rough coefficients. Mosco convergence is the correct input.
- It does not average finite-rank spectral exceptions. This avoids the
  infinite-rank obstruction that appears when exceptional eigenspaces rotate
  with the smoothing parameter.
- Point masses do not create an overlooked counterexample in the source's
  range. The theorem assumes the trace is compact; admissibility is not
  inferred merely from finiteness of the measure.

No finite-dimensional or model counterexample to the proof mechanism was
found.

## Literature-search bounds

- Local registry, solution, open-question, and source indexes: arXiv id,
  title, exact question wording, `compact trace`, `weighted Sobolev`, `smooth
  measures`, `Mosco`, and `spectral convergence`.
- Full local source of arXiv:2601.17896 and the relevant source of
  arXiv:2004.10784.
- Web search: the exact source phrase and combinations of joint
  mollification, compact weighted trace embeddings, Dirichlet-form Mosco
  convergence, and eigenvalue approximation.

The search found general Mosco-convergence papers but no exact theorem and no
later paper explicitly answering Remark 1.3. This is a bounded novelty check,
not a comprehensive priority determination.

## Remaining verifier focus

1. Write the spanning-flow smoothing kernel in local coordinates and check
   joint smoothness in `(x,y)` with uniform parameter support.
2. Confirm the source author's intended meaning of `H^1(M,alpha)` in Remark
   1.3 is `H^1(M,1,alpha)` under the immediately preceding `alpha >= c`
   hypothesis.
3. Check the diagonal finite-dimensional recovery construction explicitly if
   converting the packet into a journal proof.

## Human review recommendation

Promote for expert review as a candidate full solution in the uniformly
positive setting. Reclassify to partial only if authorial clarification shows
that the question was meant to include degenerate weights.

