# Verification Report

Candidate: arXiv:2504.21479, first sharpness conjecture on page 3

## Claim checked

The gapless and positive-gap spherical wave kernels have nonzero locally
uniform leading terms of orders `t^{-nu}` and `t^{-nu/2}`, respectively, for
spectral amplitudes nonzero at the bottom of the spectrum.

## Verdict

`likely valid`

Confidence: 97/100.

The proof is a direct endpoint-asymptotic calculation.  Residual uncertainty
is primarily novelty/positioning, not the power calculation.

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Factor the Plancherel density | valid | Each reciprocal `Gamma(i x)` contributes an exact factor `x`; after modulus square every positive reduced root contributes `x^2` times a positive even analytic unit. |
| Angular coefficient is positive | valid | The product of squared root forms is nonnegative and positive off finitely many great subspheres, a set of positive surface measure. |
| Include the polar Jacobian | valid | Degree `2d` plus `r^{l-1}` gives endpoint order `r^{2d+l-1}=r^{nu-1}`. |
| Replace `phi_{r omega}` by `phi_0` | valid | Spherical functions are analytic in the spectral parameter.  Odd first-order terms cancel in the full-sphere angular integral; only the leading term is needed. |
| Gapless endpoint lemma | valid | A half-line Fourier endpoint of order `r^{nu-1}` has coefficient `exp(i*pi*nu/2) Gamma(nu) t^{-nu}`. |
| Positive-gap substitution | valid | For `s=sqrt(r^2+epsilon)-sqrt(epsilon)`, `r^2=s(s+2sqrt(epsilon))` and `dr/ds=(s+sqrt(epsilon))/r`. |
| Positive-gap coefficient | valid | The transformed leading amplitude is `2^{nu/2-1} epsilon^{nu/4}s^{nu/2-1}` times the original angular coefficient. |
| Gapless high-frequency tail | valid | Schwartz decay and polynomial derivative bounds make repeated integration by parts legitimate. |
| Bessel high-frequency tail | valid | On `r>=delta`, the phase derivative is bounded below.  The source's derivative bound for `c^{-1}` gives radial derivatives of the density at most polynomial order `n-1`; `Re(alpha)>n` makes every term integrable. |
| Local uniformity in `x` | valid | All spherical-function bounds are uniform on compact spatial sets, and `phi_0` has a positive minimum there. |
| Answers exact source scope | valid | The source asks for pointwise optimality at small `x^+`; a uniform nonzero asymptotic on every compact set is stronger in that regime. |

## Adversarial checks

- Root hyperplanes do not kill the constant: they have surface measure zero.
- Complex phases do not permit cancellation of the leading coefficient: the
  angular coefficient and `phi_0(x)` are positive, while the remaining factors
  are explicitly nonzero.
- Odd `nu` causes no problem in the gapped case: the endpoint lemma allows the
  half-integer exponent `nu/2-1`.
- The unshifted wave multiplier corresponds to `epsilon=|rho|^2>0`, exactly
  the positive-gap specialization discussed by the source.
- No operator-norm lower bound is inferred from a pointwise value; the packet
  is deliberately limited to the pointwise conjecture.
- The result is not asserted for `psi(0)=0`; in that case the first nonzero
  Taylor coefficient changes the endpoint order.

## Deterministic audit

Command:

```text
conda run --no-capture-output -n sandbox python code/check_wave_endpoint_constants.py
```

The script checks exact gapless model integrals for several integer values of
`nu`, verifies the positive-gap Jacobian limit symbolically, and numerically
checks positivity of the angular factor for the `A_2` root system.  It is an
audit of the algebra, not a proof of the spherical inversion facts.

## Literature check

The run indexes contain no result for arXiv:2504.21479.  Bounded primary arXiv
searches used the exact source title, exact conjecture phrase, authors, and the
Anker-Zhang paper arXiv:2010.08467.  They found no later paper claiming the
same endpoint asymptotics.  Novelty remains subject to expert review.

## Human review recommendation

`send to human`

Ask a harmonic analyst to check the smooth radial factorization across root
hyperplanes and whether `Re(alpha)>n` is the cleanest stated threshold for the
uncut Bessel corollary.

