# Partial result: a norm-null/c0 border for Question 5.15

## Status

`partial_result`

Source paper: Jorge Martínez, David Meza-Alcántara, Carlos Uzcátegui,
*Pathology of submeasures and \(F_\sigma\) ideals*, arXiv:2211.01544.

Question 5.15 asks which Banach spaces satisfy
\[
\mathcal R\le_K \mathcal B({\bf x})
\]
for every weakly null sequence \({\bf x}=(x_n)_n\).

## Result

This packet gives a stronger border result.

- For any Banach-space sequence \({\bf x}\), if \(\|x_n\|\to0\), then
  \(\mathcal R\le_K\mathcal B({\bf x})\).  Hence every Schur space satisfies
  Question 5.15.
- If \(X\) is isomorphic to a subspace of \(c_0\), then \(X\) satisfies Question 5.15.
- If \(X\) has a seminormalized weakly null sequence with no \(c_0\)-subsequence, then \(X\) fails Question 5.15.

In particular, every infinite-dimensional reflexive Banach space fails the
property.

The proof uses Proposition 4.8 of the source paper for norm-null sequences,
Theorem 5.14 for \(c_0\), invariance of \(\mathcal B({\bf x})\) under
isomorphic embeddings, and the classical Bessaga-Pelczynski \(c_0\) selection
principle for weakly unconditionally Cauchy series.

This is not promoted to a full characterization.  The remaining frontier is
non-Schur spaces where every seminormalized weakly null sequence has a
\(c_0\)-subsequence but no \(c_0\)-embedding is available.  At the sequence
level this runs into the paper's broader Katetov problem for nonpathological
tall \(F_\sigma\) ideals.

## Files

- `main.tex` - proof packet source.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of arXiv:2211.01544.
- `figures/open_problem_crop.png` - crop of Question 5.15.
- `code/crop_open_question.py` - crop-generation helper.

## Verification

LaTeX was compiled with `pdflatex`.  The source-question crop was generated
from page 20 of the PDF with PyMuPDF.
