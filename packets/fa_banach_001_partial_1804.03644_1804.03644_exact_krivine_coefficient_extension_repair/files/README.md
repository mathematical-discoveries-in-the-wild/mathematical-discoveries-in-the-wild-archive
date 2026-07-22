# Exact Krivine coefficient extension and constant repair

Status: `partial_result_computer_assisted_likely_valid`

Source: V. Bhattiprolu, M. Ghosh, V. Guruswami, E. Lee, and M. Tulsiani,
*Approximating Operator Norms via Generalized Krivine Rounding*,
arXiv:1804.03644.

## Result

For all source parameters `a,b in [0,1]`, the paper's sufficient inverse
coefficient conditions (C1) and (C2) hold in every odd degree through 39.
The certificate is exact over the rationals: Lagrange inversion produces the
coefficient polynomials, and nonnegative tensor-product Bernstein
coefficients certify them on the full parameter square. Degree 7, the only
case where the direct Bernstein certificate fails, has a separate elementary
factorization proof.

Combining this degree-39 extension with the paper's analytic tail and defect
lemmas gives

`h_{a,b}^{-1}(1) >= 0.874 >= asinh(1)/1.0085`.

This repairs and slightly improves the paper's advertised factor `1.00863`.
The source's final displayed implication
`asinh(0.974202) >= asinh(1)/(1+0.00863)` is numerically false; the packet
uses the smaller degree-41 tail and exact rational Taylor inequalities
instead.

## Reproduce

From the repository root, run:

```bash
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python \
  runs/fa_banach_001/solutions/partial/1804.03644_exact_krivine_coefficient_extension_repair/code/verify_exact_certificates.py
```

Expected final line:

```text
ALL EXACT CERTIFICATES PASSED
```

The verifier requires SymPy and takes a few minutes because the exact inverse
polynomials grow rapidly.

## Scope

This is a quantitative partial result, not a proof of the full endpoint
conjecture `h_{a,b}^{-1}(1) >= asinh(1)`. No all-orders coefficient sign
claim is made. The analytic inverse-coefficient tail estimate and monotonicity
used by the defect lemma are dependencies from the source paper.

A bounded search on 2026-07-22 found no later resolution or counterexample and
no erratum repairing the source constant. This is novelty evidence, not a
definitive certification.

Human review recommendation: **verify and retain as an exact
computer-assisted quantitative partial result**.
