# Bounded semivariation implies analyticity in the locally convex setting

Status: `candidate_full_solution_likely_valid`.

Source paper: Karsten Kruse and Felix L. Schwenninger, *Continuous maximal
regularity in locally convex spaces*, arXiv:2408.11437.

Extracted problem: Problem 4.17 asks whether a strongly continuous locally
equicontinuous semigroup on a sequentially complete complex Hausdorff locally
convex space is analytic if it has bounded semivariation on some interval
`[0,r]`.

Packet result: yes, using the Dembart analyticity criterion cited in the
source. Bounded semivariation gives, by the source paper, positive-time
classical differentiability of orbits. A telescoping partition estimate then
shows that the family `{ t A T(t) : 0 < t <= R }` is equicontinuous for every
`R > 0`. Together with `T(t)X subset D(A)` for `t > 0`, this is one of
Dembart's equivalent formulations of analyticity for locally convex
semigroups.

Key files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2408.11437.
- `figures/open_problem_crop.png`: crop of Problem 4.17 from PDF page 25.

Novelty check: searched the run indexes for arXiv:2408.11437, continuous
maximal regularity, locally convex spaces, bounded semivariation, analytic
semigroup, and Dembart. No prior run packet or attempt for this exact problem
was found. A bounded web search on 2026-06-29 for exact phrases around
`bounded semivariation`, `analytic semigroup`, `locally convex`, and Dembart
did not reveal a separate later answer.

Human-review focus: confirm that the Dembart Theorem 1 formulation cited by
Kruse--Schwenninger indeed matches the criterion used here: positive-time
domain inclusion plus local equicontinuity of `{tAT(t)}`.
