# Separable Right-Support Nets Force UBCP

Status: likely valid partial result / positive bridge theorem for the
arXiv:2311.14257 C*-algebra BCP problem.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
C*-algebra version of the commutative `C(K)` BCP/UBCP criterion.

## Main Result

Let `A` be a C*-algebra. Suppose there are positive contractions
`e_n in A` such that each closed right ideal `cl(A e_n)` is separable and

```text
||a|| = sup_n ||a e_n||    for every a in A.
```

Then `A` has UBCP.

Equivalently, it is enough that for every `a in S_A` some `e_n` satisfies
`||a e_n|| > 7/8`.

## Proof Idea

For each `n`, take a countable dense set in the unit ball of `cl(A e_n)`.
Given `a in S_A`, choose `e_n` with `||a e_n|| > 7/8` and approximate
`a e_n` by some dense point `d` within `1/16`. Then `||d|| > 13/16`, and

```text
||a - 2d|| <= ||a(1 - 2e_n)|| + 2||a e_n - d|| < 9/8,
```

because `1 - 2e_n` is a contraction in the unitization. Thus the fixed-radius
balls `B(2d, 9/8)` cover `S_A`; their centers have norm `> 13/8`, so the
cover is uniformly separated from the origin.

## Why This Matters

This isolates the positive mechanism behind several previous lane-19
constructions:

- a separable essential ideal gives such a support net via a sequential
  approximate identity;
- a countable product of separable C*-algebras gives such a support net via
  its coordinate projections;
- any future pure-state pi-base proof needs, in effect, to manufacture this
  kind of countable separable support/direction net from pure-state topology.

The packet does **not** claim the full arbitrary C*-algebra classification.
Its value is that it makes the remaining bridge precise: pure-state topology
alone must be upgraded into countable separable right-support data.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Check the norming hypothesis, the use of separability of `cl(A e_n)`, and the
`a(1-2e_n)` contraction estimate in the unitization.
