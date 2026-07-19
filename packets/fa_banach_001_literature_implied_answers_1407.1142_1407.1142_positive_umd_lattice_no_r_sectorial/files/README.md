# Literature-Implied Answer: Positive UMD-Lattice Semigroups Need Not Be `R`-Sectorial

## Source Question

- Source paper: Stephan Fackler, *Regularity Properties of Sectorial
  Operators: Counterexamples and Open Problems*, arXiv:1407.1142.
- Target: the positivity-only UMD-Banach-lattice generalization suggested by
  the adjacent open problems on positive or contractive semigroup generators:
  does positivity of the generated `C_0`-semigroup force bounded
  `H^\infty` calculus, bounded imaginary powers, or `R`-analyticity?
- Screenshot: `figures/source_open_problems_crop.png`.
- Source PDF retained as `source_paper.pdf`.

## Status

This is filed as `literature_implied_answer`.  The supporting paper
arXiv:1411.4240 does not label itself as a solution of a numbered problem in
arXiv:1407.1142, but its Theorem 3.3 and Example 3.4 give a direct negative
answer to the positivity-only UMD-Banach-lattice version.

This packet is intentionally conservative: it does not claim to settle the
positive contractive UMD-lattice problem, the contractive `L_p` Matsaev
problem, the positive `L_p` problem, or the dilation questions from the source
paper.

## Answer

Let `p,q in (1,infty)` with `p != q`.  Fackler arXiv:1411.4240 proves that on
the UMD Banach lattice `ell_p(ell_q)` there is a sectorial operator `A` with
`omega(A)=0` such that `-A` generates a positive analytic `C_0`-semigroup, but
`A` is not `R`-sectorial.

Consequently this `A` cannot have bounded imaginary powers, because the source
paper recalls that BIP implies `R`-sectoriality on UMD spaces.  It also cannot
have a bounded `H^\infty` calculus, since bounded `H^\infty` calculus implies
BIP and hence `R`-sectoriality in this setting.  Thus positivity alone on a
UMD Banach lattice is insufficient for the regularity properties in the open
problem cluster.

## Limitations

- The semigroup in arXiv:1411.4240 is positive analytic, but no contractivity
  is asserted.  This does not refute the source paper's positive contractive
  UMD-Banach-lattice problem.
- The space `ell_p(ell_q)` with `p != q` is a UMD Banach lattice, not a
  classical scalar `L_p` space.  This does not settle the source paper's
  positive `L_p` problem.
- The packet records a literature-implied status update, not a new
  construction beyond Fackler's later theorem.

## Files

- `solution_packet.pdf`: rendered human-facing packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original source paper, arXiv:1407.1142.
- `supporting_paper_1411.4240.pdf`: supporting counterexample paper.
- `figures/source_open_problems_crop.png`: source open-problem cluster.
- `figures/supporting_theorem_3_3_crop.png`: supporting Theorem 3.3.
- `figures/supporting_example_3_4_crop.png`: supporting Example 3.4 start.
- `figures/supporting_example_3_4_continuation_crop.png`: Example 3.4
  conclusion across the page break.
- `code/crop_evidence.py`: regenerates the evidence crops.
