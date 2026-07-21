# Verification report

Candidate: arXiv:1910.06369, Section 8.2 spectral-mapping question

Verdict: `likely valid`

Confidence: 98/100 for the final explicitly restated question; lower if the
opening reference to Theorem 8.8 is interpreted as retaining its additional
resolvent-decay hypothesis.

## Hypothesis and conclusion audit

| Item | Status | Check |
| --- | --- | --- |
| Hilbert space | valid | `X=ell_2(N)`. |
| Closed densely defined `A` | valid | Standard diagonal multiplication operator with domain `sum n^2 abs(x_n)^2 < infinity`. |
| `-A` generates a bounded `C_0`-semigroup | valid | `T(s)e_n=e^{-ins}e_n`; it is unitary and strong continuity follows by dominated convergence. |
| `f in B` | valid | `f'(z)=(1+z)^(-2)`, so the Besov derivative integral is exactly `1`; also `||f||_infinity=1`. |
| Calculus value | valid | Resolvent compatibility gives `f(tA)=I-(I+tA)^(-1)`. |
| Norm continuity | valid | The supremum of the exact scalar difference is bounded by `abs(t-s)/min(t,s)`. |
| Spectrum of `A` | valid | `sigma(A)={in:n>=1}`; outside this closed discrete set the diagonal resolvent is bounded. |
| Spectrum of `f(tA)` | valid | A bounded diagonal operator has spectrum equal to the closure of its entries; here the sole extra closure point is `1`. |
| Proposed equality | false | `1` lies on the left and is absent from `f(t sigma(A)) union {0}` for every `t>0`. |

## Adversarial checks

- The sign convention is correct: `-A` generates `T(s)e_n=e^{-ins}e_n`.
- Strong continuity is not uniform continuity at zero; only strong continuity
  is needed for the generator, and norm continuity of `f(tA)` is required
  only for `t>0`.
- The point `1` is genuinely spectral: the basis vectors are approximate
  eigenvectors because `||(f(tA)-I)e_n||=1/sqrt(1+t^2n^2)->0`.
- Adding `{0}` to both sides cannot hide the discrepancy because the missing
  point is `1`.
- No finite `n` gives `itn/(1+itn)=1`.
- The source's positive Theorem 7.3 does not apply because `f(infinity)=1`,
  whereas it assumes vanishing at infinity.
- The stronger Theorem 8.8 sufficient hypothesis fails: for fixed
  `alpha>0` and `beta=n`, the diagonal resolvent norm is `1/alpha`, while
  `abs(f(alpha+in))->1`.

## Deterministic audit

Run from the packet directory:

```text
conda run --no-capture-output -n sandbox python code/check_diagonal_spectral_mapping.py
```

The script checks exact algebraic identities numerically at deterministic
values of `s,t,n`, verifies the uniform continuity bound, and confirms the
rate at which the diagonal entries approach the extra spectral point.  It is
an audit of the scalar formulas, not a substitute for the diagonal-spectrum
argument.

## Literature check

The cheap run indexes contain no earlier result for arXiv:1910.06369.  A
bounded primary arXiv search used the exact question, source title, authors,
and the related papers arXiv:2311.18757, 2202.03143, and 2101.05083.  It found
no explicit resolution or this construction.  Novelty remains subject to
expert review.

## Human review recommendation

`send to human`

First decide whether the authors intended the final two-condition question
literally or intended to retain the extra sufficient condition from Theorem
8.8.  Under the literal final formulation, the counterexample is complete.
