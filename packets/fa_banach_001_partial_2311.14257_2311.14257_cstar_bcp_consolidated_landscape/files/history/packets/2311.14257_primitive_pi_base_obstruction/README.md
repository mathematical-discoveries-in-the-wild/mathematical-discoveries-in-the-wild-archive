# Primitive-Ideal Pi-Base Obstruction for C*-Algebra BCP

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_primitive_pi_base_obstruction/`

## Result

For every C*-algebra `A`, if `A` has the ball-covering property, then
`Prim(A)` has a countable pi-base.

Equivalently, if `Prim(A)` has no countable pi-base, then `A` fails BCP.

Consequences:

- If `A` has an uncountable family of pairwise orthogonal nonzero closed
  ideals, then `A` fails BCP.
- For commutative algebras `C0(X)`, this recovers the necessary topological
  side: BCP forces `X` to have a countable pi-base.

## Why This Matters

This is the first broad necessary condition for arbitrary C*-algebras in the
2311.14257 Question 3 program. It pushes beyond continuous `C0(X)`-algebras:
no continuity of a field, type I hypothesis, separability, or central
structure is assumed. The invariant is the primitive ideal topology itself.

## Proof Intuition

Given a countable proposed BCP cover with centers `a_j`, form the primitive
open sets where each quotient norm `||a_j + P||` is almost `||a_j||`. If
`Prim(A)` has no countable pi-base, there is a nonempty open set `V` containing
none of these near-norm sets. Pick a norm-one element `x` in the ideal
corresponding to `V`. Outside `V`, the image of `x` in every primitive quotient
is zero. Since every near-norm set for `a_j` has a point outside `V`, primitive
quotients force `||x-a_j|| >= ||a_j||` for every `j`. Thus no countable
ball-cover can cover the unit sphere.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a major necessary-condition theorem. The key checks are the openness
of the near-norm sets in `Prim(A)`, the open-set/ideal correspondence, and the
final quotient-norm escape estimate.
