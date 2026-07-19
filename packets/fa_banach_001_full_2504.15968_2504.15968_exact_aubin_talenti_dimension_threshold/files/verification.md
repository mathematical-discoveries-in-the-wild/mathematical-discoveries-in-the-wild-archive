# Verification Report

Candidate: `2504.15968` exact Aubin-Talenti dimension threshold

## Claim checked

The localized family from arXiv:2504.15968 lies uniformly below the second
critical level for all sufficiently large cutoffs exactly when the explicit
Gamma ratio `Q_(N,s)` in the packet satisfies
`Q_(N,s) < 2^(2/N)-1`; the exact eventual dimension threshold is recoverable
by a finite scan because the normalized ratio decreases along both parity
classes from dimension 7 onward.

## Verdict

`likely valid`

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Reduction from the cutoff family to the uncut bubble | valid | Uses the source paper's uniform convergence in the local gradient, fractional seminorm, and critical norm. The maximum scale is `t=0`. |
| Fourier transform of the bubble | valid | Re-derived from the Gamma/Laplace representation of `(1+|x|^2)^(-(N-2)/2)`. |
| Raw Gagliardo-to-Fourier constant | valid | Audited against the standard multiplier normalization and the `s->1` BBM limit. |
| Mellin integral of `K_1^2` | valid | Parameter condition is satisfied for `N>=5`, `0<s<1`; constants agree with direct quadrature. |
| Gradient energy | valid | Independent radial beta-integral and Euler-Lagrange computations agree. |
| `N->N+2` recurrence | valid | Algebraic cancellation checked symbolically/numerically to 80 digits. |
| Parity monotonicity | valid | The recurrence is bounded by `2*pi/(N+2)` and the elementary barrier comparison is strict for `N>=7`. |
| Exact finite stopping rule | valid | Two consecutive successes control both parity classes; the stored earlier values identify the last failing dimension. |

## Counterexample search

Representative `s` values `0.05, 0.1, 0.25, 0.5, 0.75, 0.9, 0.99` were
checked through dimension 500 at 80-digit precision. No recurrence mismatch or
post-threshold failure occurred. This computation supports but is not needed
for the proof.

## External dependencies

- The source's uniform cutoff convergence and definition of the localized
  family, arXiv:2504.15968v2, Section 4.
- Standard modified-Bessel integral identities, recorded in NIST DLMF,
  Section 10.43. The packet states the exact identity and its parameter range.

## Gaps

No internal mathematical gap identified. Novelty search was bounded rather
than exhaustive.

## Confidence

Score: 91/100.

Reason: the proof is an exact special-function calculation with two independent
normalization checks and an elementary recurrence argument. The main human
review risk is a convention mismatch between the paper's raw Gagliardo
seminorm and the fractional-Laplacian multiplier constant.

## Human review recommendation

Send to a functional-analysis/PDE reviewer; prioritize the constant audit in
the exact seminorm formula and the iff passage from the uncut limit to the
large-cutoff family.

