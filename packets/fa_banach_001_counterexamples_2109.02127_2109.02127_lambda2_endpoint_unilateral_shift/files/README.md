# Counterexample packet: the `lambda_2` endpoint is sharp

- Source: K. Mahesh Krishna, "Improving Casazza-Kalton-Christensen-van Eijndhoven Perturbation with Applications", arXiv:2109.02127.
- Extracted question: Question 2.14 in the arXiv PDF asks whether the constant `lambda_2` can be improved further in Theorem 2.13.
- Packet status: `counterexample_likely_valid`.
- Packet path: `runs/fa_banach_001/solutions/counterexamples/2109.02127_lambda2_endpoint_unilateral_shift/`.

## Result

The endpoint `lambda_2 = 1` cannot be improved beyond `1`.

For any `lambda_2 > 1` and any `0 <= lambda_1 < 1`, choose `alpha >=
(1-lambda_1)/(lambda_2-1)` and let `U` be the unilateral shift on `ell_2`.
With `S = I` and `T = alpha U`, the perturbation inequality from Theorem 2.13
holds, but `T` is not onto and hence is not Lipschitz invertible.

The key estimate is

```text
||alpha U - I|| = alpha + 1 <= lambda_1 + lambda_2 alpha.
```

Thus any theorem allowing `lambda_2 > 1` under the same conclusion would be
false.

## Evidence And Verification

- `source_paper.pdf` is the source arXiv PDF.
- `figures/open_problem_crop.png` shows PDF page 10, containing the theorem
  endpoint discussion and Question 2.14.
- `code/make_open_problem_crop.py` creates the crop from the source PDF.
- The proof is analytic; no numerical verifier is needed.

## Novelty Check

Before promotion, the cheap run indexes were searched for the arXiv id and
core terms: Casazza, Kalton, Christensen, Eijndhoven, Paley-Wiener,
perturbation, `lambda_2`, frames, and atomic decomposition. No exact duplicate
was found.

A bounded web search on 2026-06-20 used the phrases:

- `"Can the constant" "lambda_2" "Theorem" "Casazza" "Kalton"`
- `"Improving Casazza-Kalton-Christensen-van Eijndhoven" "lambda_2"`
- `"Can the constant lambda_2 be improved" "Lipschitz" perturbation`
- `"Casazza-Kalton-Christensen-van Eijndhoven" perturbation lambda2 sharp`

The only relevant hit was the source arXiv page itself. This is therefore
recorded as a likely new sharpness counterexample, subject to human review.

## Human Review Focus

Check that the source's phrase "improved further" is intended as extending the
admissible upper endpoint for `lambda_2` past `1`. Under that standard reading,
the unilateral-shift example is a direct counterexample.
