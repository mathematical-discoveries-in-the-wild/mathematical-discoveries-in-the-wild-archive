# Partial solution packet: the two-dimensional case of `P(omega_1)`

Status: likely valid partial result.

Source paper: Andrew Swift, "Coarse embeddings into `c_0(Gamma)`", arXiv:1703.01891.

Target question: Problem 2 in Section 5 asks whether Theorem B is true for `omega_1`; equivalently, whether property `P(omega_1)` holds for every finite arity `n`.

Result proved here: the `n=2` instance of `P(omega_1)` holds in ZFC. Namely, every coloring of the two-element subsets of `omega_1` either has an infinite pairwise disjoint monochromatic family of pairs, or some vertex sees infinitely many colors.

Core idea: if every vertex sees only finitely many colors, assign to each ordinal the finite set of incident colors. These finite sets are pairwise intersecting. The Delta-system lemma gives an uncountable subfamily with a common nonempty finite root, and then the ordinary infinite Ramsey theorem gives an infinite monochromatic clique, hence an infinite monochromatic matching.

Limitations: this does not settle Problem 2 as stated, since Theorem B requires all arities `n`. The argument uses the special graph structure of the `n=2` case; the analogous higher-dimensional finite color sets live on `(n-1)`-faces and the same one-line Delta-system reduction no longer applies.

Files:
- `main.tex`: proof packet source.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:1703.01891.
- `figures/open_problem_crop.png`: crop of the source open-problem block.

Ledger: `runs/fa_banach_001/ledger/results/1703.01891_pomega1_n2_delta_system.json`.
