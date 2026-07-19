# Lower 1-estimates imply the quantitative DN-S inequality

Status: `candidate_partial_likely_valid`

Source: Manuel Gonzalez and Antonio Martinon, *A quantitative approach to
disjointly non-singular operators*, arXiv:2108.01052, Section 7.1, Question 1
(PDF page 11).

The source asks whether there is a universal constant `D > 0` such that
`kappa_d(T) <= D beta(T)`. This packet proves the inequality on every Banach
lattice with a uniform lower 1-estimate:

`kappa_d(T) <= C beta(T)`

when the lattice admits an infinite disjoint sequence and disjoint finite families satisfy
`sum ||x_i|| <= C ||sum x_i||`. In particular, every abstract `L_1` (AL)
space in this nontrivial setting satisfies the source inequality with the
optimal constant `D = 1`.

The proof takes a normalized disjoint sequence whose individual image norms
approach `beta(T)`. The lower 1-estimate turns the pointwise image bound into
an operator-norm bound on the whole disjoint span. Since `kappa_d` is bounded
above by the corresponding restriction norm, the desired estimate follows.

This is a partial result. The universal inequality for arbitrary order
continuous Banach lattices remains open. A bounded local and web search for
the exact question, title, and notation found the source paper and adjacent
DN-S papers, but no explicit later answer to this quantitative subcase.

Artifacts:

- `main.tex` and `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: original arXiv paper.
- `figures/open_problem_crop.png`: source PDF page 11, Section 7.1, Question 1.
- `verification_report.md`: adversarial step check.

Human review focus: verify the passage from the lower 1-estimate to the norm
bound on the closed disjoint span and confirm the published notation
`kappa_d = i_d tau_d` is matched exactly.
