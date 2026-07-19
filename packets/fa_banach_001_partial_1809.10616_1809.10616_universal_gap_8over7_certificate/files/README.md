# Partial Result: universal `8/7` projective/injective gap

Status: claimed partial result, likely valid subject to human review. A 2026-06-18 audit rechecked the certificate and recorded a useful obstruction to pushing the same coarse method to `sqrt(2)`.

Source paper: arXiv:1809.10616, *Universal gaps for XOR games from estimates on tensor norm ratios*, by Guillaume Aubrun, Ludovico Lami, Carlos Palazuelos, Stanislaw J. Szarek, and Andreas Winter.

## Claim

For all real Banach spaces `X,Y` with dimensions at least `2`,

```text
rho(X,Y) >= 8/7.
```

Consequently `r(n,m) >= 8/7` for all `n,m >= 2`.

This improves the source paper's universal bound `19/18`. It does **not** solve the source open problem asking whether the optimal universal lower bound is `sqrt(2)`.

## Packet Contents

- `main.tex`: human-readable proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1809.10616.
- `figures/open_problem_crop.png`: crop of Problem 3.
- `figures/eight_over_seven_remark_crop.png`: crop of the source-paper `8/7` remark.
- `code/verify_8over7_certificate.py`: exact rational verifier for the finite certificate.
- `code/analyze_certificate_symmetry.py`: symmetry/analytic atlas reducing the 130 checks to 10 classes with exact quadrant Bernstein minima.

## Verification

Run from repository root:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1809.10616_universal_gap_8over7_certificate/code/verify_8over7_certificate.py
```

Expected output:

```text
checks=130
failures=0
max_depth_used=2
certificate verified
```

This was rerun locally on 2026-06-18 with the same committed verifier and the same output. A supplied audit reported a verifier variant with `max_depth_used=1`; the committed verifier still uses depth `2`, which is harmless because both checks are exact rational Bernstein-certificate verifications.

For a more human-auditable view of the certificate, run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/1809.10616_universal_gap_8over7_certificate/code/analyze_certificate_symmetry.py
```

This reports `symmetry_classes=10`; the 10 representatives are certified by
nonnegative exact Bernstein coefficients on the four quadrants of `[0,1]^2`.

## Review Focus

1. Check the refined Auerbach data from Lemma 15 of the source paper.
2. Audit the four equations defining the matrix certificate `A(m,r)`.
3. Check the exact Bernstein verifier and the boundary-enlargement reduction.

If those checks pass, this is a substantial partial result toward Problem 3 of the source paper.

## 2026-06-18 Audit Addendum

The audit found no archival paper or preprint resolving the full `sqrt(2)` problem, and no archival proof of the `8/7` improvement. It did find a literature-status caveat: a December 2025 Case Western Reserve University abstract, as reported in the supplied audit, apparently says that the `8/7` configuration was numerically investigated and confirmed analytically, but no archival proof or code release was found.

The audit also records a useful obstruction. At the balanced two-coordinate outer body

```text
H = {(s,t): |s|,|t| <= 1, |s+t|,|s-t| <= 3/2},
```

the best possible result obtainable using only this coarse `H_m` reduction and coordinate-square-controlled CHSH-type witnesses is exactly `8/7`, attained by the standard CHSH sign matrix. Therefore a proof of the conjectural `sqrt(2)` bound must use extra structure discarded by this reduction, such as the full determinant-maximal Auerbach geometry, additional coordinates, or a different dual witness.

The audit note is stored in `evidence/audit_2026_06_18/`.
