# Partial Result: ordinal intervals below omega_1 omega

Status: `candidate_partial_result_likely_valid`

Source paper: Piotr Koszmider, *On the existence of overcomplete sets in some classical nonseparable Banach spaces*, arXiv:2006.00806.

Target question: Question 48 asks whether one can prove in ZFC that `C([0, xi])` admits an overcomplete set for every ordinal `xi < omega_2`.

Claim proved in this packet: in ZFC, `C([0, xi])` admits an overcomplete set for every ordinal `xi < omega_1 * omega`.

This is a genuine partial result for the source question. It extends the source paper's `C([0, omega_1])` case through all finite ordinal sums of `omega_1`-blocks, but it does not reach arbitrary ordinals below `omega_2`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2006.00806.
- `figures/open_problem_crop.png`: crop of Question 48 from page 25.
- `code/make_open_problem_crop.py`: crop reproduction script.

## Verification

The proof uses only the source paper's Theorem 10 (`yes-zfc`) and the same finite-codimensional hyperplane-isomorphism step used in the source proof for `C([0, omega_1])`.

The packet was rendered with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Human review should focus on the finite clopen decomposition of `[0,xi]` for `xi < omega_1 * omega` and on the finite-sum preservation of the source paper's countable-support criterion.
