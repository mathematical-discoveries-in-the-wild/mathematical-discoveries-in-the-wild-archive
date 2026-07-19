# Candidate Full Solution: Weak-star Delta-points For Duals Of Subspaces

Source paper: Trond A. Abrahamsen, Ramon J. Aliaga, Vegard Lima,
Andre Martiny, Yoel Perreau, Antonin Prochazka, and Triinu Veeorg,
*Delta-points and their implications for the geometry of Banach spaces*,
arXiv:2303.00511.

Result type: `full`

Status: candidate full solution, likely valid, pending human review.

## Open Question

Question 5.18 asks whether, if `X` is a subspace of a Banach space with a
shrinking `k`-unconditional basis for `k<2`, one can conclude that `X^*`
contains no weak-star `Delta`-points.

## Candidate Contribution

Yes. More generally, the compact-approximation obstruction used in the source
paper is stable under passing from an ambient dual `Y^*` to a restriction
quotient `X^*`, where `X` is a closed subspace of `Y`.

The proof lifts a weak-star convergent net in `B_{X^*}` to `B_{Y^*}`, passes to
a weak-star convergent subnet by compactness, applies the ambient `k<2`
distance bound in `Y^*`, and descends the bound through the quotient norm.
Thus `X^*` has no weak-star super `Delta`-points, and Theorem 5.6 of the
source paper rules out weak-star `Delta`-points.

## Files

- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: crop of PDF page 23 showing Corollary 5.17
  and Question 5.18.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX build intermediates and the rendered source page image.

## Literature Check

Local run indexes were searched for `2303.00511`, the paper title,
`Delta-points`, `Daugavet`, `weak* Delta`, `subspace`, and
`shrinking k-unconditional basis`; no duplicate packet, prior attempt, or
proof-gap packet was found. A bounded web search on June 14, 2026 for exact
phrases from Question 5.18 and close variants found the source paper but no
separate later paper explicitly resolving the question. A local corpus search
found the source question and later/background mentions of the source paper,
but no exact answer packet or later explicit resolution.

## Human Review

Recommended check: verify the quotient-lifting lemma, especially the subnet
argument that lifts an arbitrary weak-star convergent net in `B_{X^*}` through
the restriction map `Y^* -> X^*` and descends the strict `<2` ambient distance
bound to the quotient norm.
