# Unitizations of Separable-Fibre Continuous-Trace Algebras Have BCP

Status: likely valid partial result.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let `I` be a continuous-trace C*-algebra whose elementary fibres are
`K(H_x)` with each `H_x` separable and nonzero. Let `A = I~` be the minimal
unitization when `I` is nonunital; if `I` is unital, take `A = I`.

Then

```text
A has BCP  <=>  A has UBCP  <=>  Prim(I) has a countable pi-basis.
```

## Key Idea

The old continuous-trace proof localizes compact-operator sections by scalar
bumps. Unitization adds local fibre terms of the form `lambda I + k(x)`, and
the scalar identity cannot be localized in infinite-dimensional fibres.

The new proof adds a rank-one compact ballast spike in a direction where the
local compact part is almost zero:

```text
c = mu 1 + h(T + M omega Q).
```

The spike makes `||c||` about `M + |lambda|`, while the distance from
`lambda 1 + i` to `c` is only about `M`. This scalar margin replaces the
missing localization of the identity.

## Why It Matters

This is the first positive packet beyond the compact-chart continuous-trace
case that handles an actual multiplier direction. It is a strong template for
the next target: finite-dimensional quotients of positive continuous-trace
ideals.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check the scalar-ballast estimate, especially:

- the finite-rank approximation `T` and rank-one projection `Q` with `TQ=QT=0`;
- the lower bound `||c|| >= M + eta - 2 epsilon`;
- the distance bound `||a-c|| < M + 3 epsilon`;
- the finite-dimensional fibre branch, where the scalar identity is compact.

If this survives review, the next serious push should try to replace the scalar
ballast by matrix-block ballast for finite-dimensional quotients.
