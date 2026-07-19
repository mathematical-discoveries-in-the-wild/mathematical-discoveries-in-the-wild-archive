# Counterexample: finite-complexity-rate inductive limits

Status: candidate counterexample, likely valid, pending expert review.

Source paper: Geng Tian and Guoliang Yu, *Embedding complexity into Banach
spaces and the strong Novikov conjecture*, arXiv:2605.12930v1.

Targeted question: after proving the strong Novikov conjecture for countable
groups with finite complexity rate, Tian and Yu ask whether every countable
discrete group is an inductive limit of groups with finite complexity rates.

Result: the answer is negative under both standard readings recorded here. A
finitely presented group whose Cayley geometry coarsely contains a bounded-degree
expander sequence has infinite complexity rate. Osajda's construction of
fundamental groups of closed aspherical manifolds containing coarsely embedded
expanders supplies such a finitely presented group. Therefore this group is not
a directed union of finite-complexity-rate groups, and finite presentability also
rules out expressing it as a filtered colimit of finite-complexity-rate groups
with arbitrary bonding homomorphisms.

Main ingredients:

- subgroup heredity of finite complexity rate;
- the direct-union reduction from the previous partial packet;
- the linear-in-`q` expander Poincare inequality for maps into `ell_q`;
- Osajda's finitely presented groups coarsely containing expanders;
- the standard fact that a finitely presented filtered colimit retracts from
  one finite stage.

Files:

- `main.tex` / `solution_packet.pdf`: consolidated counterexample packet.
- `source_paper.pdf`: local copy of arXiv:2605.12930.
- `supporting_paper_1005.4084.pdf`: Naor--Silberman Poincare reference.
- `supporting_paper_1406.5015.pdf`: Osajda expander-group reference.
- `figures/open_problem_crop.png`: crop of the source question from page 6.
- `evidence/supplied_finite_complexity_rate_counterexample_2026_06_22/`:
  supplied TeX/PDF report.
- `history/previous_inductive_limit_reduction_2026_06_16/`: absorbed earlier
  partial packet.

Review focus: check the exact constants and quantifiers in the expander
Poincare obstruction, and verify that the cited Osajda corollary supplies a
finitely presented group with the needed coarse expander containment. With
those inputs, the counterexample is formal.
