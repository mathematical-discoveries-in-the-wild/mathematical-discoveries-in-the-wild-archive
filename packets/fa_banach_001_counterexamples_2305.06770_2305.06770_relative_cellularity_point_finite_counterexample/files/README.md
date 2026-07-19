# Counterexample: compact relative point-finite families can exceed relative cellularity

Status: `counterexample_likely_valid_needs_human_review`.

## Source target

Source: Jakub Rondos, *On isomorphisms of C(K) spaces and cardinal invariants
of derivatives of K*, arXiv:2305.06770.

The source asks whether, if `U` is a point-finite family of open sets meeting a
subset `A` of a compact space `K`, then `|U| <= c(A,K)`.  It notes that a
positive answer for compact `A` would unify parts of the paper's Banach-space
results for target spaces `E` not containing `c0`.

## Result

The expected inequality is false, even with `A` compact.

For every uncountable cardinal `kappa`, there is a compact Hausdorff space `K`,
a compact subset `A subset K`, and a point-finite family `U` of open subsets of
`K` meeting `A` such that:

```text
|U| = kappa, but c(A,K) = omega.
```

The construction is a one-point compactification of a Psi-space built from the
almost disjoint family `{D_i : i < kappa}` on `[kappa]^2`, where
`D_i = {{i,j}: j != i}`.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of the source paragraph.
- `source_2305.06770.tex`: parsed source TeX inspected locally.
- `code/crop_open_problem.py`: crop helper.
- `code/check_finite_incidence.py`: finite incidence sanity check.

## Verification

Commands used:

```sh
conda run --no-capture-output -n sandbox python code/crop_open_problem.py
conda run --no-capture-output -n sandbox python code/check_finite_incidence.py
conda run --no-capture-output -n sandbox latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

The proof is set-theoretic/topological and does not rely on computation.  The
script only checks the finite incidence pattern of the construction.

Ledger: `runs/fa_banach_001/ledger/results/2305.06770_relative_cellularity_point_finite_counterexample.json`.
