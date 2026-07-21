# Verifier report

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/2310.14099_omega_backward_shift_all_suborbits_total/code/verify_full_spark_hankel.py
```

Output on 2026-07-21:

```text
PASS: 218 Hankel minors checked in exact integer arithmetic.
PASS: each determinant equals its row/column factors times Vandermonde.
PASS: every tested finite family of shift projections has full rank.
```

The audit used `q=2` and tested every row tuple of sizes one through five
chosen from indices `0,...,7`. Determinants were evaluated by fraction-free
Bareiss elimination and compared exactly with the closed Vandermonde product.
No floating-point arithmetic was used.

This computation checks the algebraic certificate only. The Baire-category
argument and the density conclusion are proved analytically in `main.tex`.
