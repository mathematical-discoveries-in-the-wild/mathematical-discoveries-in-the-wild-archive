# Verification report

Status: partial_result_likely_valid; human_review_needed

## Proof audit

1. For block-diagonal Laplace variables, the matrix determinant lemma
   factors the transform of the scale
   \(\Sigma=\operatorname{diag}(D_i)+aa^\mathsf T\) into the product of
   central-block factors and one scalar factor.
2. Mixing conditionally independent rank-one noncentral Wishart blocks over
   \(S\sim\chi^2_\alpha\) reproduces that scalar factor. Laplace-transform
   uniqueness therefore identifies the complete joint law of the diagonal
   blocks. This works for real \(\alpha>p-1\).
3. In identity scale and rank-one noncentrality
   \(\lambda e_1e_1^\mathsf T\), the noncentral density is the central
   density tilted by a function of the first diagonal entry only.
4. The central Schur-complement change of variables makes that entry
   \(\chi^2_\alpha\), independent of a
   \(\mathcal W_{r-1}(\alpha-1,I)\) Schur complement. The tilt replaces only
   the first factor by \(\chi'^2_\alpha(\lambda)\), proving the determinant
   factorization for noninteger degrees of freedom.
5. The Poisson-mixture coupling makes noncentral chi-square stochastically
   increasing in its noncentrality. Hence every conditional increasing
   observable of a block determinant increases with the common scalar, and
   every decreasing observable decreases.
6. Conditional independence followed by the one-variable Chebyshev
   covariance identity proves every split product inequality. Powers give
   Conjecture 1.1; lower-tail indicators give Conjecture 3.8.

No missing implication was found in this audit. The unrestricted,
several-factor scale-matrix case is not claimed.

## Numerical smoke test

Command:

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/partial/2311.00202_one_factor_wishart_minor_association/code/verify_one_factor_mixture.py

The test used 12 randomized one-factor models, each with three or four blocks,
total dimension four through six, a genuinely noninteger degree of freedom,
and 60,000 samples from both:

- the direct SciPy central Wishart law; and
- the common-chi-square/noncentral-chi-square determinant mixture.

The largest discrepancy was 2.341 standard errors for a fractional moment
and 2.197 standard errors for a lower-tail event. No claimed inequality failed
beyond the 4.5-standard-error audit threshold. This checks normalization and
detects simple contradictions; it is not part of the proof.

## PDF audit

The five-page packet compiled without warnings, undefined references,
overfull boxes, or underfull boxes. All five pages were rendered with Poppler
and visually inspected. Both source-question crops, the theorem, formulas,
proof, limitations, and references are readable and unclipped.

## Reviewer focus

The highest-value checks are the noncentral-Wishart transform convention,
the rank-one density tilt, and the uniqueness step for the product-cone
Laplace transform. If these pass, retain the packet as a substantial partial
answer to both source conjectures.

