# No uniform finite modularity testers for partition lattices

**Status:** counterexample / full negative answer to Question 6.47 of
Contreras Mantilla--Sinclair; likely valid, pending human review.

The source asks whether constants `C,K` can be chosen so that every finite
partition lattice `P_n` admits `K` testers controlling distance to the singular
partitions by the sum of the modular-pair defects.  The answer is **no**.

For arbitrary `K` tester partitions, color each unordered pair of ground-set
points by the `K`-bit vector recording whether its endpoints lie in the same
block of each tester.  Finite Ramsey gives four points on which all pair colors
agree.  For each tester, those four points therefore lie either in one block or
in four distinct blocks.  Pair the four points into two two-element blocks and
leave all remaining points singleton.  This partition is non-singular, but it
forms a metrically modular pair with every tester.  Consequently every defect
on the proposed right-hand side is zero while the distance on the left is
`1/(n-1)>0`.

The stronger proved statement is: for every `K`, once
`n >= R_{2^K}(4)`, *every* `K`-tuple of testers has a common non-singular
modular partner.

Files:

- `solution_packet.pdf`: review-ready proof packet.
- `main.tex`: packet source.
- `source_paper.pdf`: arXiv:2507.10932.
- `figures/open_problem_crop.png`: Question 6.47 on source PDF page 51.
- `code/verify_ramsey_witness.py`: finite rank-equality checker for a supplied
  homogeneous four-set.
- `code/compute_small_gamma.py`: exact small-`n` exploration that led to the
  Ramsey obstruction; it is not used as proof.

The result does **not** decide whether `Pi_infty` or all models of `T_FPL` have
property Gamma.  The Ramsey witness has distance `1/(n-1)` from the singular
set, so that distance vanishes along the resulting large finite lattices.

