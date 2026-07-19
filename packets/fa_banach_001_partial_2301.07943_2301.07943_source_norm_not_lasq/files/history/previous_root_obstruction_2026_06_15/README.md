# Candidate Partial Result: Source Renorming Is Not LASQ

Source paper: Jose Rodriguez and Abraham Rueda Zoca, *On weakly almost
square Banach spaces*, arXiv:2301.07943.

Result type: `partial`

Status: candidate partial obstruction, likely valid, pending human review.

## Open Question

The paper asks whether there exists a locally almost square (LASQ) Banach
space which fails the diameter two property (D2P).  It then proves that every
Banach space containing a complemented copy of `c0` admits an equivalent norm
with slice-D2P, arbitrarily small relatively weakly open subsets of the unit
ball, and `(r,s)`-SQ for all `r,s < (1-epsilon)/(1+epsilon)`.

The packet does not answer the full LASQ-versus-D2P question.

## Candidate Contribution

For every fixed `0 < epsilon < 1`, the concrete `c0`-renorming used in the
source proof is not LASQ.  More precisely, in the source unit ball

```text
B = closure conv((A x {0}) union (-A x {0})
    union ((1-epsilon) B_Z + epsilon B_{c0(tree)} x {0})),
```

the point `(x_empty,0)` is strongly extreme.  Hence no sequence witnessing
LASQ can exist at that point.

## Why This Is Only Partial

This rules out the most direct route of upgrading the paper's fixed-epsilon
construction into the desired LASQ counterexample.  It does not rule out a
different renorming, a variable-epsilon construction, or another Banach space.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_question_crop_page3.png`: crop containing the LASQ/D2P
  question.
- `figures/theorem_1_2_crop_page4.png`: crop containing the source theorem
  whose construction is being obstructed.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates.

## Literature Check

Local run indexes were searched for `2301.07943`, `weakly almost square`,
`locally almost square`, `LASQ`, `WASQ`, `D2P`, and `diameter two`.  No
duplicate packet for this paper or exact obstruction was found.  A bounded web
search on June 15, 2026 for `"locally almost square" "diameter two property"`,
`"LASQ" "D2P" Banach space`, and close variants found the source paper and
nearby LASQ lattice/transfinite-ASQ papers, but no later explicit solution of
the full LASQ-fails-D2P question.

## Human Review

Recommended check: verify the inequality

```text
||P_2 w|| <= ((1-epsilon)/epsilon)(1 + L(w)),  w in B,
```

where `L=(lim,0)` and `P_2` is the second-coordinate projection.  This is the
whole mechanism behind the strong-extreme-point argument.
