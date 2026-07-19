# Partial packet: three-point `2d-1` projection obstruction

status: strengthened_partial_result

source: Nadav Dym, Matthias Wellershoff, Efstratios Tsoukanis, Daniel Levy,
and Radu Balan, *Quantitative Bounds for Sorting-Based
Permutation-Invariant Embeddings*, arXiv:2510.22186.

target: the source leaves open the sharpness of orbit-separation dimension
bounds for `n>2`; its numerical section reports failed searches at
`(n,d,D)=(3,2,3)`, `(3,3,5)`, and `(3,4,7)`.

packet: `runs/fa_banach_001/solutions/partial/2510.22186_planar_three_projection_threshold/`

## Result

For every `d >= 2`, if `D <= 2d-1`, no matrix `A in R^{d x D}` makes the
sorting embedding `beta_A` orbit separating on three-point multisets in
`R^d`.

Equivalently, any sorting key separating all three-point multisets in `R^d`
must use at least `2d` projections.  This improves the source lower bound in
the `n=3` row from `D <= 2d-2` to `D <= 2d-1`, and proves the source's
numerically negative cases `(3,3,5)` and `(3,4,7)` for every `A`.

For `d=2`, the source paper's full-spark upper theorem gives separation at
`D=4`, so this packet also gives the exact planar threshold for three points.

## Proof Mechanism

Normalize a full-rank key with `D=2d-1` to `[I_d | B]`, where
`B in R^{d x (d-1)}`.  Pick a nonzero vector `c in ker(B^T)`.

If `c` has at least two nonzero coordinates, choose different 3-cycles on two
coordinate columns and solve `(P_i-I)x_i=c_i w`; the extra projections change
by `sum_i b_ij c_i w = 0`.  If `c` has only one nonzero coordinate, the extra
columns ignore that coordinate, so cycle it while keeping another distinct
coordinate fixed.  In both cases sorted projections agree, but no single row
permutation can match all coordinate columns.

## Verification

- Cheap run indexes were searched for `2510.22186`, sorting-based
  permutation-invariant embeddings, orbit separation, and related keywords.
- A bounded web/literature check on 2026-07-18 found the arXiv source, the
  published/source predecessor by Balan-Haghani-Singh, and Matousek-
  Privetivy-Skovron's projection paper, but no later exact answer to the
  `n=3, D=2d-1` obstruction.
- `code/verify_three_projection_counterexample.py` checks sampled normalized
  cases for `2 <= d <= 8`, including full-support and singleton-support
  kernel cases.
- The packet PDF was rendered from `main.tex`; the source PDF was copied as
  `source_paper.pdf`.

## Scope

This is not a full solution of the source paper's general dimension or
distortion problems.  It proves the sharp lower obstruction `D >= 2d` for
three-point multisets.  Existence at `D=2d` for every `d` remains open in
this packet, although the source gives explicit positive examples for
`(n,d,D)=(3,3,6)` and `(3,4,8)`, and the `d=2` case follows from the source
upper theorem.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: crop of the open-bound statement.
- `figures/phase_diagram_crop.png`: crop of the planar phase diagram/caption.
- `code/verify_three_projection_counterexample.py`: lightweight verifier.
