# Verification Report

Candidate: arXiv:2411.16010, Remark 5 general-\(L^2\) Poisson concentration
question.

## Claim Checked

For arbitrary \(L^2(\mathbb T)\) boundary data, the analytic concentration
bound extends with multiplicative factor \(2\); \(2\) is the least constant
uniform in hyperbolic area \(s>0\); and factor \(1\) fails at each fixed
\(s>0\).

## Verdict

**likely valid**

No logical gap or normalization contradiction was found. The result answers
the literal existence question and determines the best uniform multiple of
the source bound. It does not determine the optimal constant as a function of
each fixed \(s\).

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Fourier decomposition | valid | The constant mode is assigned only to \(f\), so the two \(H^2\) norms add to the boundary \(L^2\) norm without double counting. |
| Factor-\(2\) upper bound | valid | The source theorem applies separately to \(f\) and \(g\); the only loss is \(|a+b|^2\le2(|a|^2+|b|^2)\). |
| Kernel normalization | valid | Parseval gives \(\|p_\rho\|_2^2=(1+\rho^2)/(1-\rho^2)\). |
| Hyperbolic area | valid | \(dA/(1-|z|^2)^2\) is invariant under disk automorphisms and \(\mu(B(0,R))=\pi R^2/(1-R^2)\). |
| Pullback density | valid | Direct substitution yields equation (6) in the attempt/packet. No derivative factor is missing because the integrand is first written as a density against invariant \(d\mu\). |
| Boundary limit | valid | The pulled-back density converges uniformly on \(|w|\le R<1\), justifying passage to the limit. |
| Angular integral | valid | A residue/geometric-series computation gives the mean \(1-r^2/2\). |
| Failure of factor \(1\) | valid | The limit exceeds the analytic bound by \(\pi s/(s+\pi)>0\), so sufficiently large \(\rho<1\) gives an actual violation. |
| Uniform optimality | valid | The forced ratio tends to \(2\) as \(s\downarrow0\), matching the upper bound. |

## Counterexample And Numerical Checks

The reusable checker independently evaluates:

- the angular mean at \(r=0,0.2,0.6,0.9\);
- the pulled-back pre-limit mass for \(s=0.01,0.5,3,20\);
- for each \(s\), the values \(\rho=0.9,0.99,0.999\).

All four angular checks agree with \(1-r^2/2\) to the displayed precision.
All twelve masses converge monotonically in the tested cases to
\[
\pi\left[\log(1+s/\pi)+s/(s+\pi)\right].
\]

The numerical checks are not used as proof.

## External Dependency

The sole mathematical dependency is the source paper's qualitative sharp
\(H^2\) concentration inequality (Theorem 1.4 / the display immediately
preceding it). The packet copies the source PDF and cites the exact theorem.

## Novelty Check

Bounded searches on 2026-07-23:

- exact phrase from Remark 5;
- `Poisson extensions general L2 boundary unit disk concentration inequality`;
- `harmonic Hardy space concentration inequality`;
- the source authors paired with `Poisson`, `harmonic`, and `concentration`.

No later exact answer was found. This is not a comprehensive priority search.

## Confidence

Score: **94/100**

The proof is short and all delicate identities admit direct independent
checks. Remaining uncertainty is primarily literature priority and the
interpretive breadth of the source's informal word “a concentration
inequality,” not the stated theorem.

## Human Review Recommendation

**send to human**

Confirm the source normalization and whether the authors intended a fixed-\(s\)
sharp/extremizer classification rather than the literal existence question.
