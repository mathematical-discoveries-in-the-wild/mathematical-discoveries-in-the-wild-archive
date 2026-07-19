# Strong Partial Result: Better Bounds for the Midpoint Constant

## Source Question

- Source paper: Rafal Gorak, *Perturbations of isometries between Banach spaces*, arXiv:1105.0854.
- Location: Section 4, "Final remarks", page 11.
- Question: determine the exact value of the asymptotic midpoint constant
  `K = limsup_{epsilon -> 0} K_epsilon`, where `K_epsilon` is the supremum of
  the normalized midpoint defect over all `mu`-isometries with
  `mu(t)=(1+epsilon)t`.

The source records the bounds `0.5 <= K <= 3`.

## Result

This packet improves the source bounds to

```text
e/2 <= K <= e.
```

It also proves that the defining `limsup` is an actual limit.

The lower bound comes from an absolute-value shear on a specially renormed
copy of `R^2`.  The upper bound comes from a reflection-orbit inequality for
the midpoint modulus `A(M)`, combined with Gorak's dyadic estimate.

The exact value remains open.  The previous active packet proved only
`1 <= K <= exp(sqrt(2))/sqrt(2)`; it is preserved in
`history/previous_packet_2026_06_19/`.

## Files

- `main.tex`: active strengthened partial-result packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source open problem.
- `evidence/supplied_improved_midpoint_bounds_2026_06_18/`: supplied improved proof note.
- `history/previous_packet_2026_06_19/`: previous active packet and sanity-check code.

## Review Focus

Review should check:

1. the renormed shear lower-bound construction;
2. the reflection-orbit inequality, especially the reversible orbit
   identities and the telescoping estimate;
3. the limiting argument proving existence of `lim A(e^h)/h`;
4. the use of Gorak's dyadic theorem in the upper bound.
