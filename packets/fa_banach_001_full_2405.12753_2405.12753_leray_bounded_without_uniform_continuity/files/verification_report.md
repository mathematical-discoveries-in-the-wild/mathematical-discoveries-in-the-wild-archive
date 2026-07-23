# Verification report

Verdict: `candidate_full_solution_likely_valid`.

## Mathematical checks

- Re-derived the source identities for `r_1`, `r_2`, `r_1^*`, and `r_2^*`.
- Re-derived the logarithmic derivatives of `F`, `F^*`, and the beta kernel.
- Checked the comparison inequality independently on both sides of the common
  maximizer `s_0=m/(m+n)`; the reversal caused by the negative derivative for
  `s>s_0` is accounted for.
- Checked the exact beta-function formula for `J_c(m,n)`.
- Treated `m=0` and `n=0` directly in both uniform estimates.
- Checked that the factorial-height and two beta-width powers cancel with no
  residual dependence on `m,n`.
- Checked that the `(0,0)` rank-one mode has norm one.
- Verified the geometric equivalence between compact exponent range and
  two-sided curvature-ratio bounds using the explicit source formula and
  two-sided bounds for the factor `Q(s)`.

## Computational check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2405.12753_leray_bounded_without_uniform_continuity/code/verify_beta_kernel_bounds.py
```

Scope: every `(m,n)` in `[0,300]^2` and beta exponents
`c=0.05,0.1,0.25,0.5,0.9`.

The script evaluates exact log-gamma formulas and prints the maxima of the
normalized quantities from the two Stirling lemmas.  All values were finite
and the check passed.  This finite check is not used as proof.

Observed normalized maxima:

```text
c=0.05: 9.70967741935
c=0.10: 5.56564079092
c=0.25: 3.53314282685
c=0.50: 2.50142369866
c=0.90: 1.86548544895
factorial-height normalization: 1
```

## Source and rendering checks

- `source_paper.pdf` is the official arXiv PDF for 2405.12753.
- `open_problem_crop.png` comes from source page 20 and contains the complete
  Section 4.3 remark.
- `rank_one_criterion_crop.png` comes from source page 16 and contains the
  complete norm formula and boundedness criterion.
- `solution_packet.pdf` was compiled with build artifacts confined to `tmp/`.
- Every rendered packet page was visually inspected.

## Novelty check

Bounded web searches on 2026-07-23 used:

- `2405.12753 uniformly continuous Leray`
- the exact Section 4.3 phrase
- the exact paper title with citation/answer terms
- `Leray transform bounded exponent p(s) Reinhardt`

No later paper explicitly resolving the omitted case was found.  This is
evidence of plausible novelty, not a comprehensive literature certification.
