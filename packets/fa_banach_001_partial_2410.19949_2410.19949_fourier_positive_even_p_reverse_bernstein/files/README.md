# Fourier-Positive Even-Exponent Reverse Bernstein Subcase

Status: `partial` candidate result for arXiv:2410.19949, likely valid.

For every even exponent `p = 2m`, this packet proves the sharp reverse Bernstein estimate

```text
||Delta f||_p >= 2 d ||f||_p
```

for every real hypercube tail function whose Walsh coefficients become nonnegative after a cube translation. The factor `2` is from the Laplacian normalization in the source paper. A single level-`d` Walsh character gives equality.

The general problem for arbitrary Fourier signs and arbitrary `p != 2` remains open.

## Evidence

- Source paper: `source_paper.pdf`.
- Source location: Section 1.3, page 3; source TeX line 314.
- Open-problem crop: `figures/open_problem_crop.png`.
- Proof packet: `solution_packet.pdf`.
- Finite theorem checks: `code/verify_fourier_positive_even_p.py` (600 random cases through `n=6`, `p=4,6,8`; no violation beyond floating-point roundoff).
- Unrestricted exploratory probe: `code/finite_tail_inverse_probe.py`.

## Proof mechanism

Expand both `E f^(2m)` and `E[f^(2m-1) Delta f]` over `2m` Walsh frequencies with empty symmetric difference. Coefficientwise positivity makes every summand nonnegative. Permutation symmetry averages the Laplacian weight over all frequencies, and the tail condition makes that average at least `2d`. Holder's inequality finishes the norm estimate.

## Novelty status

A bounded local-corpus and web search on 2026-07-19 found the general partial-bound literature (arXiv:1902.02406, arXiv:1907.11359, and arXiv:2401.07699) but no exact match for this Fourier-positive even-exponent theorem. Novelty confidence is moderate, not definitive.

## Human review recommendation

Check the permutation averaging in the multilinear Walsh sum and the factor `2` in the source normalization. Then check whether the coefficientwise-positive subcase is already known under positive-definite functions on the Boolean group.
