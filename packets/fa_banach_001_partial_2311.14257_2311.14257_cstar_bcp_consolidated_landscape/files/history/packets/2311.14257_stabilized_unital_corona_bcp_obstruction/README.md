# Stabilized Unital Coronas Fail BCP

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergenov Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_stabilized_unital_corona_bcp_obstruction/`

## Result

Let `H` be an infinite-dimensional separable Hilbert space and let `D` be a
nonzero unital C*-algebra. Then the stabilized Calkin-type corona

`(B(H) tensor_min D) / (K(H) tensor_min D)`

fails BCP.

For unital `D`, this is the multiplier corona of `K(H) tensor_min D`.

## Why This Matters

This pushes the corona-diagonal program beyond literal product/reduced-product
quotients. It gives a broad concrete C*-corona family on the negative side of
the source question. The case `D = C` recovers the Calkin algebra obstruction,
while arbitrary unital coefficients show that the same obstruction survives
stabilized coefficient algebras.

## Proof Intuition

For `T` in `B(H) tensor D`, the quotient norm modulo `K(H) tensor D` is visible
on finite-rank right tails. Given countably many proposed centers, choose
finite-dimensional domain projections where each center nearly realizes its
quotient norm. Then choose fresh finite-dimensional range projections almost
orthogonal to the corresponding finite-column image, and define a partial
isometry from each domain block to its fresh range block. The strong sum of
these partial isometries is a norm-one multiplier element whose corona class
stays outside every proposed BCP ball.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a concrete negative partial theorem for the C*-algebra question. The
main checks are the quotient-norm formula, the finite-rank right-tail recovery
step, and the range-avoidance construction for the partial isometries.
