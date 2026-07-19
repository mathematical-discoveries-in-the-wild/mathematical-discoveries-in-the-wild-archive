# Counterexample packet: duplicate synthesis atoms for operator-valued Feichtinger conjectures

status: candidate_counterexample_likely_valid

Source: K. Mahesh Krishna and P. Sam Johnson, "Operator-Valued p-Approximate Schauder Frames", arXiv:2201.03955.

Target: Conjectures 7.1 and 7.2, page 24, ask whether lower- and upper-norm bounded operator-valued p-ASFs or p-ABSs can be partitioned into finitely many operator-valued p-approximate Riesz sequences.

Result: Both conjectures are false as stated. For `p=1`, there is an operator-valued 1-ASF in `B(ell_1, K)` with all `A_n` and `Psi_n` of norm `1`, but every finite partition contains two identical synthesis atoms in one part. Such a part cannot be an operator-valued approximate Riesz sequence because Riesz subcollections have injective synthesis.

Files:
- `main.tex`: full counterexample packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2201.03955.
- `figures/open_problem_crop.png`: crop of Conjectures 7.1 and 7.2 from page 24.
- `code/make_open_problem_crop.py`: reproduces the crop from `source_paper.pdf`.

Novelty check: checked the run lightweight indexes for arXiv:2201.03955 and core terms including `operator-valued p-approximate Schauder frame`, `operator-valued p-ASF`, `Feichtinger conjecture`, and `p-approximate Riesz sequence`. External web/arXiv searches on 2026-06-19 for the exact title and for `"operator-valued p-approximate Schauder frame" "Feichtinger conjecture" counterexample` found the source paper and adjacent frame-conjecture papers, but no direct counterexample to Conjectures 7.1-7.2.

Scope: The example is for `p=1`, so it refutes the conjectures under their written quantification over arbitrary `p in [1,infty)`. It does not settle possible repaired versions for fixed `p>1`, Hilbert/G-frame subcases, or hypotheses excluding duplicate synthesis atoms.

Human review recommendation: verify the source definition of operator-valued p-approximate Riesz sequence on the closed span `Z`, and in particular the consequence that `P_{A,Psi}=I` forces the synthesis operator of a Riesz subcollection to be injective.
