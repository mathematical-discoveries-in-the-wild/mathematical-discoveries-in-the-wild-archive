# Full solution packet: convex concentration forces the HJ condition

Status: likely valid full answer.

Source paper: Radoslaw Adamczak and Dominik Kutek, *On Orlicz spaces
satisfying the Hoffmann-Jorgensen inequality*, arXiv:2310.04163.

Targeted question: Remark 4.9 asks whether, under the additional growth
assumption `Psi(x) <= C exp(Cx)`, condition `(HJ)` is necessary for the
convex-Lipschitz concentration inequality (4.9).

Result: yes. If the convex concentration inequality (4.9), with constants
depending only on `Phi`, holds for `Phi(t)=Psi(t^2)` and all product random
vectors, then `Psi` satisfies `(HJ)`.

Idea: test (4.9) on the sparse Bernoulli array used in the source's proof of
Proposition 4.5, but use the convex 1-Lipschitz map `x -> ||x||_2` instead of a
linear sum. The event of at least `s` rare hits gives a deviation of order
`sqrt(s)`. The maximum coordinate has `Phi`-norm of order `u^{-1/2}`, so the
Orlicz tail term in (4.9) becomes `exp(-psi(csu))`. Comparing with the Poisson
lower bound for the rare-hit event yields `(HJ)`.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv source paper.
- `figures/open_problem_crop.png`: crop of Remark 4.9.

Novelty check: local run indexes and bounded web search on 2026-06-29 found no
duplicate packet or later exact resolution.
