# One-zone counterexample to Conjecture 8 of arXiv:2006.02192

Status: candidate counterexample, likely valid, for human review.

## Result

Conjecture 8 of Alexandr Polyanskii's *A cap covering theorem* is false as
literally printed.

Take one zone of width \(\beta\), where \(0<\beta<\pi\). Its complement is
the pair of antipodal open caps, each of inradius
\[
\gamma=\frac{\pi-\beta}{2}.
\]
Thus the conjectured left-hand side is
\[
\beta+\gamma+\gamma=\pi,
\]
not at least \(2\pi\). Every nondegenerate single zone supplies a
counterexample.

The factor-of-two gap suggests a typo or normalization issue in the source.
This packet disproves only the literal statement and does not propose the
intended correction.

## Files

- `solution_packet.pdf`: compiled proof packet.
- `main.tex`: proof source.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: full-width crop of the printed conjecture.
- `code/verify_one_zone.py`: exact arithmetic sanity check.

## Reproduce

From this directory:

```bash
conda run --no-capture-output -n sandbox python code/verify_one_zone.py
mkdir -p tmp/pdfs
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp/pdfs main.tex
```

The compiled `tmp/pdfs/main.pdf` is copied to `solution_packet.pdf` after
visual inspection.

## Review priority

Confirm with the author whether the \(2\pi\) constant or a width/inradius
normalization was intended differently. Under the definitions printed in
arXiv:2006.02192, the counterexample is complete.
