# Epsilon improvement for the large-entry matrix gap

Status: `partial_result_likely_valid`.

Source: Vladimir Muller and Yuri Tomilov, "On interplay between operators, bases, and matrices", arXiv:2010.09126.

## Result

The source paper's Theorem 2.8 constructs, for every bounded Hilbert-space operator \(T\) not of the form \(\lambda I+K\), an orthonormal basis with off-diagonal matrix entries bounded below by
\[
  c\,\frac{\min(n,j)^{1/2}}{\max(n,j)^{3/2}}
\]
and above by \(C/\max(n,j)^{1/2}\), then asks whether the gap between the lower and upper estimates can be removed "at least in a sense".

This packet proves a strengthened partial answer: for every \(\varepsilon>0\), the same construction can be tuned and the residual estimate sharpened to obtain
\[
  |\langle T u_n,u_j\rangle|
  \ge c_\varepsilon\,\frac{\min(n,j)^\varepsilon}{\max(n,j)^{1+\varepsilon}},
  \qquad n\ne j,
\]
while keeping the source's \(O(\max(n,j)^{-1/2})\) upper bound.

It also records a simple endpoint obstruction: one cannot literally replace the lower bound by \(c/\max(n,j)^{1/2}\) for all off-diagonal entries of any bounded operator matrix, because each column must be square-summable.

## Novelty Check

Cheap-index search found no exact packet for arXiv:2010.09126.  A bounded web/local primary-source check used the phrases `On interplay between operators, bases, and matrices`, `gap can be removed`, `large entries`, `matrix representations`, and the later same-author arXiv:2206.14266 paper.  The later paper prescribes arrays on admissible subsets under row/column \(\ell^1\) restrictions, but the full subdiagonal/all-entry lower-bound problem from Theorem 2.8 is not an admissible-set instance and was not found to contain this epsilon sharpening.

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source crop containing the gap passage and Theorem 2.8.

## Human Review

Recommended review focus: check that the refined residual product estimate is compatible with every induction step in the proof of source Theorem 2.8, especially the creation step for \(j=n\) and the density argument for the orthonormal system becoming a basis.
