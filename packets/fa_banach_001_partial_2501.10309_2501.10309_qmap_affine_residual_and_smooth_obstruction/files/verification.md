# Verification report

Candidate: arXiv:2501.10309, Remark 9 / equation (18)

## Claim checked

The source Qmap is concave on the common-affine independent-residual class
when one residual is Gaussian, but unrestricted concavity fails even for iid
random vectors with positive smooth densities.

## Verdict

**Likely valid; candidate partial result; send to human review.**

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Quotient equals conditional entropy power | valid | Expand the definitions \`N_d(W)^d = exp(2h(W))\` and use the entropy chain rule. |
| Common-affine residual reduction | valid | The residual sum is independent of the summed first block because the two block/residual pairs and the vectors are independent. |
| One-Gaussian positive result | external/valid | Costa concavity plus the standard concave perspective transformation gives the stated lambda-concavity. |
| Small-noise entropy lemma | valid | Mutual information identity plus nearest-neighbor decoding and Fano's inequality proves convergence to the discrete entropy. |
| Four-mode versus three-mode entropy | valid | At \`1/4\` the four values \`±2 ± 2 sqrt(3)\` are distinct and equiprobable; at \`1/2\` the weights are \`1/4,1/2,1/4\`. |
| Midpoint violation | valid | The entropy-power ratio tends to \`exp(2((3/2)log2-2log2))=1/2\`, while iid symmetry equates the two endpoints. |

## Counterexample search and computation

The accompanying script first found a generic two-Gaussian-mixture violation,
then simplified it to iid symmetric mixtures. With component means \`±4\`,
component standard deviation \`0.1\`, and 80,001-point quadrature, it returned

\`f(1/4)=2.7327149513\`, \`f(1/2)=1.3663574756\`,
\`f(3/4)=2.7327149513\`.

This computation is only a sanity check; the proof uses the small-noise limit
and does not rely on a numerical error bound or on the specific threshold
\`sigma=0.1\`.

## External dependencies and novelty

- Costa's 1985 entropy-power concavity theorem is used only in the positive
  class.
- A bounded search checked the exact source phrase, entropy-power concavity
  with iid Gaussian mixtures/Rademacher smoothing, arXiv:1904.02314, and the
  Gaussian-scale-mixture literature around arXiv:2308.15997. No exact match
  for the conditional quotient reduction or this two-weight mode-collision
  obstruction was found. This is not a claim of exhaustive novelty.

## Human reviewer focus

1. Confirm the regularity assumptions under the preferred statement of
   Costa's theorem.
2. Check that the packet's positive class is not already an immediate stated
   corollary in a later version of arXiv:2501.10309.
3. Decide whether the partial result is strong enough for external circulation;
   the negative example is elementary and the positive extension is concise.

