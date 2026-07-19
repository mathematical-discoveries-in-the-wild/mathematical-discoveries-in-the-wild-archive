# Primitive Pi-Base Is Not Sufficient: II_1 Factor Obstruction

Status: `partial_obstruction_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_primitive_pi_base_not_sufficient_ii1/`

## Result

The primitive-ideal pi-base condition from the earlier packet is not sufficient
for BCP among arbitrary C*-algebras.

Take any II_1 factor `M`, for instance the hyperfinite II_1 factor `R`. As a
C*-algebra, `M` is simple, hence `Prim(M) = {0}` has a countable pi-base. But
`M` is an atomless von Neumann algebra, so by the von Neumann algebra
classification in arXiv:2311.14257 it fails BCP.

Therefore:

`Prim(A)` has a countable pi-base `=>` `A` has BCP

is false, even when `Prim(A)` is a singleton.

## Why This Matters

The earlier packet proved the necessary condition:

if `A` has BCP, then `Prim(A)` has a countable pi-base.

This packet shows that the condition is strictly necessary, not a
characterization. The remaining C*-algebra classification must detect a
noncommutative size/atomicity obstruction invisible to the primitive topology.

## Proof Intuition

Finite factors have no nontrivial closed two-sided C*-ideals. A nonzero ideal
contains a nonzero positive element; a spectral cutoff gives a nonzero
projection in the ideal; trace comparison in a II_1 factor then uses finitely
many subequivalent copies of that projection to generate the unit.

Thus a II_1 factor has one-point primitive ideal space. The source paper's
von Neumann theorem supplies the other half: atomless von Neumann algebras
fail BCP. Combining the two gives the obstruction.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a sharp obstruction to the primitive-topology route. The key checks
are the C*-simplicity lemma for II_1 factors and the use of the source paper's
von Neumann classification/atomless failure theorem.
