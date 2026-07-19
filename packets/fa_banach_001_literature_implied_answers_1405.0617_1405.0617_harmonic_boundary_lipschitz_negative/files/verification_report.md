# Verification Report

Candidate: Remark 13 of arXiv:1405.0617, boundary-Lipschitz harmonic
extensions on convex domains.

## Claim Checked

The unit disk admits a harmonic function continuous on the closed disk whose
boundary restriction is 1-Lipschitz but whose interior Lipschitz seminorm is
infinite.  There is also a smooth family with boundary Lipschitz seminorm at
most 1 and interior Lipschitz seminorm tending to infinity.

## Verdict

`likely valid`

## Step Check

| Step | Status | Notes |
| --- | --- | --- |
| Boundary datum is well-defined | valid | `|t|` agrees at `t=-pi` and `t=pi`, so it defines a continuous function on the circle. |
| Euclidean boundary Lipschitz bound | valid | Difference of distances is bounded by angular distance; `(2/pi) delta <= 2 sin(delta/2)` for `0 <= delta <= pi`. |
| Fourier series | valid | Standard cosine series for `|t|`, scaled by `2/pi`; coefficients are absolutely summable. |
| Harmonic extension | valid | Replacing each cosine coefficient by `r^k` is the Poisson extension; compact convergence permits termwise differentiation for `r<1`. |
| Radial derivative formula | valid | The odd-power identity is `sum r^(2m+1)/(2m+1)=atanh(r)=(1/2)log((1+r)/(1-r))`. |
| Failure of interior Lipschitz regularity | valid | A globally Lipschitz differentiable function has directional derivatives bounded by its Lipschitz seminorm; the radial derivative diverges. |
| Smooth-family boundary norm | valid | Poisson convolution is an average of rotations and is therefore a contraction for the ambient chordal Lipschitz seminorm. |
| Smooth-family interior norm | valid | `H_rho` is harmonic past the closed disk and its inward radial derivative at `1` equals `(4/pi^2)log((1+rho)/(1-rho))`. |
| Match to source scope | valid with interpretation note | The disk is smooth, strictly convex, and two-dimensional. The family addresses the uniform-estimate reading even if the source keeps only functions smooth up to the boundary. |
| Literature classification | likely valid | Known endpoint theory implies the negative phenomenon, but no searched supporting source explicitly identifies Remark 13; `literature_implied_answer` is the conservative bucket. |

## Counterexample Search

The exact series identity was checked numerically at radii `0.2`, `0.5`,
`0.9`, `0.99`, and `0.999`, using 200,000 terms.  No discrepancy exceeding
floating-point/truncation tolerance was found.  Boundary contraction and
smooth-family growth were also sampled.

## External Dependencies

- Poisson extension/Fourier series on the disk: standard and also directly
  represented in the packet.
- Hile--Stanoyevitch (1999), Theorem 2: local PDF inspected; used for
  literature context, not for the exact proof.
- Olofsson (2020), Theorem 6.7 and Proposition 6.8: open full text inspected;
  used for provenance/classification, not for the exact proof.

## Gaps

- No mathematical proof gap found.
- Semantic point for human review: whether Remark 13 intended a uniform
  estimate, mere finiteness for every boundary-Lipschitz harmonic function, or
  only functions smooth on the closed domain.  The packet treats all three via
  the single function and smooth approximating family.

## Confidence

Score: 98/100.

Reason: every mathematical step reduces to an explicit Fourier identity and a
one-line Poisson-convolution contraction.  The remaining uncertainty is only
the source remark's informal quantifier and the provenance label.

## Human Review Recommendation

Send to human as a lightweight literature-implied negative answer.  Review the
source-quantifier interpretation and, secondarily, the decision not to count
the explicit witness as a new counterexample because the endpoint phenomenon
is classical.
