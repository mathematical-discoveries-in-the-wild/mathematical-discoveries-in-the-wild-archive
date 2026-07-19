# Verification Report

Candidate: arXiv:2409.20372, Remark 2.7 boundary local-Lipschitz question.

## Claim checked

For the explicit rank-two matrix A=V V^T in the packet,
gamma_+(A)=125 and gamma_+ is not locally Lipschitz at A relative to
the positive-semidefinite cone.

## Verdict

likely valid

## Step check

| Step | Status | Notes |
| --- | --- | --- |
| Source match | valid | Remark 2.7 on PDF page 7 asks exactly whether local Lipschitzness extends to the entire PSD cone. |
| PSD and rank | valid | A=V V^T and the exact checker gives rank two. |
| Real quadratic minorant | valid | The five sign intervals give explicit nonnegative factorizations. |
| Complex extension | valid | The Euclidean triangle inequality gives the required complex lower bound from the two real lower bounds. |
| Exact value | valid | The contact directions form a positive weighted tight frame of cost 125; the quadratic minorant gives the matching lower bound for every complex factorization. |
| Lipschitz-to-support lemma | valid | The infimal-convolution extension is finite and convex on the ambient Hermitian space, agrees locally with gamma_+, and therefore has an ambient subgradient. Homogeneity calibrates it at A. |
| Dual obstruction | valid | Positive frame weights force equality at all three contacts. Real and imaginary coordinate perturbations fix the second coordinates of Tx; linearity contradicts x_+-x_-=2x_0. |
| Symbolic check | valid | code/verify_counterexample.py passes all exact identities. |

## Counterexample search

The construction was checked over complex factorizations, not only real ones.
The known dimension-two identity gamma_+(B)=||B||_{1,1} is consistent with
the counterexample first appearing here in dimension four. No contradiction
was found.

## External dependencies

- The source paper is used for the definition and exact open question.
- The convex-analytic implication needed by the proof is proved inside the
  packet; it is not left as an external assumption.

## Gaps

No mathematical gap found. The proof does not provide an explicit divergent
Lipschitz-ratio sequence; instead it disproves local Lipschitzness by showing
that the supporting form forced by local Lipschitzness cannot exist. This is a
complete logical negation, not a conditional step.

## Confidence

Score: 94/100.

The remaining review risk is concentrated in the local
Lipschitz-to-ambient-subgradient lemma, although the packet supplies a direct
finite-dimensional proof.

## Human review recommendation

Send to a convex-analysis or matrix-factorization reviewer. Check the
infimal-convolution lemma first, then the three-contact derivative
contradiction.

