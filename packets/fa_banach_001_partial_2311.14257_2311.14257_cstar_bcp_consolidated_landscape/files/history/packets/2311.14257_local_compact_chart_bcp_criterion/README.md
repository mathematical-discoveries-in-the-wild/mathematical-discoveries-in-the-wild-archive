# Local Compact-Chart Criterion for C*-Algebras with UBCP

Status: `partial_criterion_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_local_compact_chart_bcp_criterion/`

## Result

If a C*-algebra `A` has a countable pi-basis of primitive-open charts on which
every ambient element is represented by a norm-continuous compact-operator
section over a separable Hilbert fibre, then `A` has UBCP.

Combined with the primitive pi-base obstruction, this gives

`BCP ⇔ UBCP ⇔ Prim(A) has a countable pi-basis`

for all C*-algebras satisfying this compact-norming chart hypothesis.

## Why This Matters

The previous wall was that continuous-trace ideals do not automatically control
ambient elements: an element can act on such an ideal only as a multiplier, as
in `B(H)` acting on `K(H)`.

This packet isolates the exact local regularity needed to bypass that wall. If
the multiplier problem disappears locally, the same countable bump-center proof
works without requiring a global `C_0(X)`-algebra structure.

## Proof Intuition

For `a` in the unit sphere, the primitive set where `||a+P|| > 3/4` is open.
Pick one of the countable compact-norming charts inside it. In that chart,
`a` is a norm-continuous compact-operator field. A countable dense net in the
local compact operators supplies a direction `T`, and a compactly supported
bump `h` inside the chart gives the center `4hT`.

The usual convexity estimate gives distance `< 7/2`; the centers have norm
`4`, so the balls are uniformly off the origin.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Limitations

This is not a full arbitrary C*-algebra classification. The chart hypothesis is
the new burden. It is meant to be checked in concrete local-compact/type-I
classes, or used to prove that a proposed class still has a genuine multiplier
obstruction.

## Human Review Recommendation

Review as a reusable partial criterion. The core check is Definition 1: once
the local representatives `a_hat_n` exist with the stated compact
norm-continuity and quotient-norm recovery, the covering proof is direct.
