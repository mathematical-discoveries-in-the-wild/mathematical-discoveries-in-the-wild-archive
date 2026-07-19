# Smooth shift counterexample to the Faulkner-Huneycutt orthogonal-complement problem

Status: counterexample_likely_valid.

Source target: Kobos and W\'ojcik, *On non-linear mappings preserving the
semi-inner product*, arXiv:2204.06281, Remark 4.2.

## Result

The Faulkner-Huneycutt problem quoted in the source paper has a negative
answer. There is a smooth, strictly convex, reflexive Banach space `X` and a
closed subspace `Y` isometric to `X` such that the semi-inner-product
orthogonal complement `Y^\perp` is not a linear subspace.

The example works over both `R` and `C`. The space is an equivalent renorming
of `ell_4`; the isometric copy is the range of the two-step shift.

## Idea

Encode the norm of a sequence by overlapping three-coordinate windows. The
two-step shift preserves the window list exactly, so its range is a closed
isometric copy of the whole space. The overlap is chosen so that the support
functional at `e_1` and at `e_2` annihilates the shifted range, but the support
functional at `e_1+e_2` does not.

Thus `e_1,e_2 in Y^\perp` while `e_1+e_2 notin Y^\perp`.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2204.06281.
- `figures/open_problem_crop_page10.png` and
  `figures/open_problem_crop_page11.png`: source Remark 4.2 across two pages.
- `code/verify_counterexample.py`: exact arithmetic check of the witness
  support-functional coefficients and the shift isometry on finite samples.
- Ledger: `runs/fa_banach_001/ledger/results/2204.06281_faulkner_huneycutt_smooth_shift_counterexample.json`.

## Novelty Check

The run's cheap indexes had no exact prior packet or attempt for arXiv:2204.06281
or the Faulkner-Huneycutt `Y^\perp` question. Local/source-corpus searches
found related work on isometric ranges and non-complemented isometric subspaces,
especially Pelczar-Barwacz arXiv:2309.15261 and later discussion in
arXiv:2407.15112, but not the smooth semi-inner-product orthogonal-complement
counterexample constructed here.

Web/arXiv spot checks on 2026-06-30 for phrases around "Faulkner Huneycutt",
"smooth reflexive", "Y^\perp linear", "orthogonal complement", and
"semi-inner product" found the source question and related one-complemented
range literature, but no exact later resolution.

## Human Review

Recommended review focus: check the support-functional formula for the
pullback `ell_4` norm and the direction convention for the source paper's
orthogonality relation. Once those are confirmed, the nonlinearity of
`Y^\perp` is witnessed by the three explicit coordinate vectors above.
