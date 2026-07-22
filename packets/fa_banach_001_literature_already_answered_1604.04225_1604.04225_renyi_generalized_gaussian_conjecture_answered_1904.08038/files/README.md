# Literature answer: generalized Gaussians do not minimize Rényi entropy of sums

Status: `literature_already_answered`.

## Original conjecture

Mokshay Madiman, James Melbourne, and Peng Xu, *Forward and Reverse
Entropy Power Inequalities in Convex Geometry*, arXiv:1604.04225, Section
2.3.3 (pp. 14--16), state the Wang--Madiman conjecture: if independent
random vectors `X_i` and suitably scaled generalized Gaussians `Z_i` have
matching order-`p` Rényi entropies, then

\[
  N_p(X_1+\cdots+X_n)\geq N_p(Z_1+\cdots+Z_n).
\]

The survey says that, apart from `p=1` and the known `p=infinity` cases, the
conjecture remained open.

## Explicit later answer

Benjamin Jaye, Galyna V. Livshyts, Grigoris Paouris, and Peter Pivovarov,
*Remarks on the Rényi Entropy of a sum of IID random variables*,
arXiv:1904.08038, explicitly identifies the Wang--Madiman conjecture as
Conjecture 1.1 and disproves it. The introduction states that the conjecture
already fails for `d=1`, `p=2`, `n=2`, with identically distributed
summands. Section 4 proves, by a first-variation argument, that the proposed
generalized Gaussian is not even a stationary point of the constrained
extremal problem and hence cannot be a minimizer.

This is therefore an exact later-literature answer, not a new result of this
run. The broader problem of identifying the actual minimizer remains open in
the answering paper.

## Files

- `main.tex`, `solution_packet.pdf`: compact theorem-level identification.
- `source_paper.pdf`: arXiv:1604.04225.
- `supporting_paper_1904.08038.pdf`: the answering paper.
- Ledger: `runs/fa_banach_001/ledger/results/1604.04225_renyi_generalized_gaussian_conjecture_answered_1904.08038.json`.

