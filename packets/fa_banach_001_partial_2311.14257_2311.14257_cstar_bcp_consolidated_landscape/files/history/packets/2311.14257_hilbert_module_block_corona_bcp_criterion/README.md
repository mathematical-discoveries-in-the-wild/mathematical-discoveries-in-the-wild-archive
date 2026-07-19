# Hilbert-Module Block Coronas Fail BCP Under Tail Recovery

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergenov Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_hilbert_module_block_corona_bcp_criterion/`

## Result

Let `E` be a Hilbert C*-module. If the corona `L(E)/K(E)` has a projectional
block system with:

- compact block projections escaping compact operators;
- finite block equivalences and strict gluing of disjoint block partial
  isometries;
- tail recovery of every quotient norm on arbitrarily late finite blocks;

then `L(E)/K(E)` fails BCP.

The stabilized unital corona theorem is recovered by taking
`E = H tensor D` for nonzero unital `D`, where the compact coordinate
projections form such a block system.

## Why This Matters

This is the clean abstract form of the stabilized-corona diagonal proof. It
also explains the exact obstruction to simply removing unitality from the
coefficient algebra: for nonunital `D`, the coordinate projections on the
standard module over `D` live in the multiplier algebra, but need not be compact
module projections. So the previous proof needs a replacement compact block
system rather than a cosmetic rewrite.

## Proof Intuition

The proof is the same diagonal escape, but expressed in Hilbert-module terms.
For each proposed center, tail recovery supplies a compact finite block where
the center nearly realizes its quotient norm. Compact-vanishing lets us choose
a fresh equivalent range block almost disjoint from the finite-column image.
Strict gluing then assembles the finite-block partial isometries into a single
norm-one adjointable operator whose corona class avoids all proposed BCP balls.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as an abstract partial theorem/criterion. The proof is complete under
the stated block-system axioms; the main future work is verifying those axioms
for broader nonunital stable multiplier coronas.
