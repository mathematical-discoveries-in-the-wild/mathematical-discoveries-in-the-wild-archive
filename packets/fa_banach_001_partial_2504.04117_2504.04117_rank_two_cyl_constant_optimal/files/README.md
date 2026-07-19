# Rank-two and finite-set cylinder constant results

Status: `partial_result_likely_valid`

Source: Michael Dymond and Olga Maleva, *Extreme non-differentiability of
typical Lipschitz mappings*, arXiv:2504.04117.

This packet records two sharp observations around the optimality question
following Definition 4.2 and Lemma 4.4 of the source paper. The authors define
a finite-rank constant `C(T)` controlling the Lipschitz constant in their
purely-unrectifiable prescribed-derivative lemma, note that `C(T) >= ||T||`,
and ask whether the upper bound `C(T)+theta` is optimal.

## Result

For every bounded linear operator `T` of rank at most two,
`C(T) = ||T||`. Hence the source lemma achieves the hoped-for bound
`Lip(g) <= ||T|| + theta` for all compact purely unrectifiable sets in this
rank-one/rank-two range.

If the compact set `E` is nonempty, the bound is sharp in the asymptotic sense:
any map satisfying the source lemma's derivative requirement with error
`theta` must have Lipschitz constant at least `||T|| - theta`.

For finite compact sets, the hoped-for bound is also attainable for every
finite-rank `T`, in every rank. Disjoint logarithmic radial cut-offs around the
points give `Lip(g) <= ||T|| + epsilon`, arbitrarily small support, small sup
norm, and exact derivative `T` near every point.

Consequently, because the source notes that `C(Id_X)>1` for some
three-dimensional-and-higher norms, `C(T)` is not the pointwise optimal constant
for every individual instance `(E,U,T)`. Any genuine obstruction to the
hoped-for constant must use infinite, nontrivial purely unrectifiable sets, not
finite sets.

## Packet contents

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2504.04117.
- `figures/open_problem_crop.png`: crop of PDF page 14 containing the
  optimality question, Definition 4.2, Remark 4.3, and Lemma 4.4.
- `code/make_open_problem_crop.py`: reproducible crop script.

Human review should focus on three elementary points: the rank-two projection
argument, the logarithmic radial cut-off estimate
`Lip(x -> beta(||x||)x) <= 1 + epsilon` in an arbitrary normed space, and the
cross-ball estimate in the finite-set construction.
