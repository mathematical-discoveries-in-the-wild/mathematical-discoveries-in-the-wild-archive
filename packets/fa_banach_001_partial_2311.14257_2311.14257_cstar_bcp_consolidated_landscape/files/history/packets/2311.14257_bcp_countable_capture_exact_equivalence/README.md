# BCP Is Exactly the Negation of Countable Capture

Status: likely valid exact BCP characterization / partial answer to the
C*-algebra BCP/UBCP classification question.

Source target: arXiv:2311.14257, Question 3, asking for a
noncommutative C*-algebra version of the commutative BCP/UBCP criterion.

Non-duplication note: this packet settles the qualitative BCP/countable-capture
question for all normed spaces.  Future work on arXiv:2311.14257 should treat
that as done and focus on intrinsic C*-criteria and the possible upgrade from
BCP to UBCP.

## Result

For every nonzero real or complex normed space `X`,

```text
X fails BCP  <=>  X has countable capture.
```

Equivalently, `X` has BCP if and only if there is a countable set
`C subset X` such that every unit vector `u` is strictly closer than `||c||`
to the line `F u` for some `c in C`:

```text
exists countable C such that for every u in S_X,
exists c in C with dist(c, F u) < ||c||.
```

The proof is a scalar-rescaling observation missing from the previous
one-way obstruction packet. If `dist(c, F u)<||c||`, then for some nonzero
scalar `lambda`,

```text
||c - lambda u|| < ||c||.
```

Dividing by `lambda` gives

```text
||u - lambda^{-1} c|| < ||lambda^{-1} c||,
```

so `u` lies in a standard BCP ball. A rational approximation to
`lambda^{-1}` makes the resulting center set countable.

## C*-Algebra Consequence

For every C*-algebra `A`, BCP is equivalent to failure of countable capture
for the underlying Banach space.

Thus the lane-19 conjecture

```text
C*-algebra BCP failure iff countable capture
```

is true, and in fact it is true for all normed spaces.

## Scope

This is an exact BCP characterization, not a full structural UBCP
classification. The quantitative gap between BCP and UBCP remains a separate
problem. In all C*-algebra classes handled by the earlier packets, positive
BCP examples were upgraded to UBCP, but this packet does not prove BCP=UBCP
for arbitrary C*-algebras.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the negation of countable capture;
- the scalar-rescaling step from `dist(c, F u)<||c||` to a BCP ball;
- the use of a countable dense scalar subfield to keep the centers countable;
- the scope distinction between BCP and UBCP.
