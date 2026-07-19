# Verification Report

Candidate: arXiv:2601.17896, Remark 1.3, uniformly elliptic partial theorem.

## Claim checked

For continuous `alpha` with `0 < c <= alpha <= C`, every positive Radon
measure `mu` inducing a compact trace `H^1(M,alpha) -> L^2(M,mu)` admits
smooth positive approximants `(alpha_n,mu_n)` for which all fixed finite
variational eigenvalues converge.

## Verdict

Likely valid partial result. Confidence: 84/100.

The proof does not settle the rough or degenerate `alpha` case in the source
question, and the packet labels that limitation consistently.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Compact trace implies vanishing local capacity ratio | external/valid | This is Maz'ya's compactness criterion, also quoted in Girouard--Karpukhin--Lagace. Uniform ellipticity identifies `H^1(M,alpha)` with ordinary `H^1(M)`. |
| Localized diffeomorphism averaging yields smooth densities | valid | The vector fields span the tangent bundle on the localized support, so averaging over their small flows gives a smooth density. Positivity and mass preservation are immediate. |
| Uniform capacity modulus survives smoothing | likely valid | Small diffeomorphisms are uniformly bi-Lipschitz, hence distort diameter and `2`-capacity by fixed constants. Applying the original modulus to each inverse image and averaging gives `omega_{mu_n}(r) <= C omega_mu(Cr)`. |
| Uniform modulus implies collective compactness | likely valid | The proof localizes to finitely many balls, uses the capacitary trace inequality on `mu_n|_B`, subtracts a volume average, and applies Poincare. Fixed ball averages vanish for a weakly null sequence. |
| Weak-star plus collective compactness implies form-norm convergence | valid | A contradiction sequence has a weakly convergent subsequence; the residual is small in both moving and limiting `L^2` norms, while the fixed weak limit is handled by smooth approximation and weak-star convergence. |
| Form convergence implies eigenvalue convergence | valid | The packet conjugates the generalized form pencil to compact positive self-adjoint operators on one fixed Hilbert space. Operator-norm convergence gives convergence of ordered eigenvalues. |

## Counterexample search

- Ordinary weak-star smoothing without the uniform capacity estimate fails to
  give the needed lower-semicontinuity direction; the packet does not make
  that mistake.
- Point masses in dimension at least two do not contradict the theorem because
  evaluation is not a bounded `H^1` trace for a uniformly elliptic energy.
- Hypersurface measure, weighted volume measures in the critical integrability
  class, and finite sums of such measures are consistent with the conclusion
  and with known spectral convergence results.
- A possible failure mode would be a compact trace measure whose localized
  diffeomorphism averages lose the capacitary modulus. The uniform
  bi-Lipschitz capacity comparison rules this out.

No counterexample was found.

## External dependencies

- Maz'ya's capacitary trace inequality and compactness criterion.
- Standard quasi-invariance of Sobolev `2`-capacity under uniformly
  bi-Lipschitz diffeomorphisms.
- Standard norm perturbation theory for compact self-adjoint operators.

## Remaining verifier focus

1. Check the smoothing construction in a chart or via compactly supported
   vector-field flows, including smooth extension across chart boundaries.
2. Check that the localized capacitary trace inequality has constants uniform
   over the finite covering.
3. Confirm the source's intended meaning of "smooth measures" when both
   `alpha` and `mu` vary; the theorem handles that meaning for continuous
   uniformly positive `alpha` by also smoothing `alpha` uniformly.

## Human review recommendation

Send to a spectral geometry or Sobolev-capacity expert. The result is strong
enough to preserve as a partial packet, but should not be promoted to a full
solution unless the rough/degenerate weighted-capacity obstruction is removed.

