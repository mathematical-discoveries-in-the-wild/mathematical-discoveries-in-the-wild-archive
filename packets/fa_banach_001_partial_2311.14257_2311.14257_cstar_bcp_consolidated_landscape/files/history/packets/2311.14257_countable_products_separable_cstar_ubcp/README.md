# Product Dichotomy for Separable C*-Algebras and BCP

Status: likely valid product classification.

Source target: arXiv:2311.14257, Question 3.

## Result

If `(A_gamma)` is a family of separable C*-algebras, then the product

```text
prod_gamma A_gamma
```

has BCP, equivalently UBCP, if and only if at most countably many factors are
nonzero.

The positive direction is the explicit countable-product cover: if `(A_n)` is
a countable family of separable C*-algebras, then `prod_n A_n` has UBCP.

The negative direction is direct countable capture: if uncountably many factors
are nonzero, then for any countable center set one can delete a coordinate that
preserves all old center norms and put the escaping unit vector in that
coordinate.

This gives large nonseparable positive examples, including

```text
ell_infty(O_2) = prod_n O_2,
```

which is non-Type-I and nonseparable but has UBCP.

## Key Idea

Given a unit-sphere element `x=(x_n)`, choose a coordinate `k` with
`||x_k|| > 3/4`. A countable dense net in the unit sphere of `A_k` gives
a center supported only at coordinate `k`, of the form `2d`. The distance
in all other coordinates is at most `1`, and in coordinate `k` it is less
than `3/2`. The center has norm `2`, so the balls are uniformly off the
origin.

For the uncountable negative direction, each fixed old product center has at
most one coordinate whose deletion lowers its norm. Avoiding the countable
union of these exceptional coordinates gives a coordinate-deletion contraction
which kills the new vector and preserves all old center norms.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check the coordinate estimate, the uniform off-origin constants, and the
essential-coordinate deletion argument.
