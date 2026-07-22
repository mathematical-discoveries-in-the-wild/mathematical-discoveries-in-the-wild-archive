# Verifier report

Status: `passed_exact_symbolic_verification`

Command:

```bash
conda run --no-capture-output -n sandbox python code/verify_c6_radial.py
```

Checks performed:

1. Derive `K_2`, `K_4`, and `K_6` from the source's Weyl-parametrix recurrence
   using the four rotational invariants.
2. Assert symbolically that the derived `K_2` equals the source's displayed
   formula specialized to `P(x)=|x|^2` in arbitrary dimension.
3. Assert that every monomial used in the `d=9,11` integration is separately
   integrable in the momentum variable; no analytic continuation of divergent
   monomial integrals is used.
4. Evaluate spherical averages, contour residues, and radial beta integrals in
   exact arithmetic.
5. Assert exact equality with both claimed rational multiples of `pi` and
   assert positivity.

Recorded output:

```text
d=9 grouped contributions:
  (x power, f derivative order)=(0, 0): -11951*pi/33822867456
  (x power, f derivative order)=(1, 1): 1802663*pi/789200240640
  (x power, f derivative order)=(2, 2): -6605027*pi/3156800962560
  (x power, f derivative order)=(3, 3): 7528807*pi/18940805775360
C_6^(9)((z+1)^-15) = 212857*pi/901943132160

d=11 grouped contributions:
  (x power, f derivative order)=(2, 0): 84227*pi/454579338608640
  (x power, f derivative order)=(3, 1): -84227*pi/545495206330368
C_6^(11)((z+1)^-18) = 84227*pi/2727476031651840
All exact assertions passed.
```

Human review should focus on the translation of the source's Weyl-product
convention into the invariant operators `S2` and `S4`, and on the normalized
contour-residue sign. The arbitrary-dimensional `K_2` identity is included as
a low-order convention check.
