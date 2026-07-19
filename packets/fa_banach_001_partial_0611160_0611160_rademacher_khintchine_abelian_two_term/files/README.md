# Partial Result: Rademacher \(p=1\) noncommutative Khintchine constants in abelian and two-term cases

Status: `partial_result_likely_valid`

Source paper: Uffe Haagerup and Magdalena Musat, *On the best constants in noncommutative Khintchine-type inequalities*, arXiv:math/0611160.

## Target

Haagerup--Musat prove the \(p=1\) Rademacher noncommutative Khintchine inequality with lower constant \(1/\sqrt{3}\), while the scalar Khintchine inequality gives the upper obstruction \(1/\sqrt{2}\).  They state that they do not know whether the \(\sqrt{3}\) constant is sharp.

## Packet Claim

The packet proves that the sharper lower constant \(1/\sqrt{2}\) holds in two natural subcases:

1. arbitrary finite families of commuting normal coefficient matrices;
2. arbitrary matrix coefficient families with at most two nonzero terms.

The constant \(1/\sqrt{2}\) is sharp already for scalar two-term coefficients.

## Scope

This does not solve the full Haagerup--Musat Rademacher constant problem.  It shows that any obstruction to the conjectural \(1/\sqrt{2}\) lower constant must use at least three genuinely noncommuting coefficients.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the original arXiv paper.
- `figures/open_problem_crop.png`: rendered source page containing the open sharpness sentence.
- `code/verify_subcases.py`: small numerical sanity checker for the two proof inequalities.

## Verification

Rendered with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Sanity checker:

```sh
conda run --no-capture-output -n sandbox python code/verify_subcases.py
```
