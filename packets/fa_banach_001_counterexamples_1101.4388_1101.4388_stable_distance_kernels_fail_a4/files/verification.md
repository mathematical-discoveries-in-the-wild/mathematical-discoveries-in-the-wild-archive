# Verification record

Date: 2026-07-22

Status: all deterministic checks passed.

## Command

    conda run --no-capture-output -n sandbox python \
      runs/fa_banach_001/solutions/counterexamples/\
      1101.4388_stable_distance_kernels_fail_A4/code/\
      verify_symmetric_counterexamples.py

## Checked cases

- Cross-polytope scalar formulas for p=1 and p=2 at
  gamma = 0.05, 0.10, 0.25, 0.50, 0.75, 0.95.
- Planar regular-polygon powered-chord sums and A4 quotients at the same
  six gamma values.
- One direct 6-by-6 Euclidean Gram solve at gamma=1/2.

The direct solve reported:

    min_eigenvalue=7.793905347407e-03
    solve_residual_inf=1.110223024625e-16
    coefficient_spread=1.693090112553e-15
    A4_norm=1.000065821370

The final line was:

    ALL SYMMETRIC COUNTEREXAMPLE CHECKS PASSED

The proof in main.tex is analytic; these computations are independent sanity
checks and are not used to establish the universal quantifiers.

## PDF checks

- solution_packet.pdf compiled in two LaTeX passes with no warnings,
  overfull boxes, underfull boxes, or undefined references.
- The final 5-page PDF was rendered at 150 dpi.
- All five rendered pages and the page-25 source crop were visually inspected.
- No clipped text, overlap, broken glyphs, or unreadable formulas were found.
