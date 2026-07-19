# Order-Convex Affine Envelope Theorem

Result type: `full`

Status: candidate full solution, likely valid pending human review.

Source paper:

- Mario Ghossoub, Giulio Principi, and Ruodu Wang, "Allocation Mechanisms in
  Decentralized Exchange Markets with Frictions", arXiv:2404.10900.
- Local source PDF: `source_paper.pdf`, rebuilt from the downloaded arXiv
  source bundle with `xelatex`.
- Open-question evidence crop: `figures/open_problem_crop.png`.

## Claimed Contribution

Section 6 of the source paper says: "To the best of our knowledge, the
generalization of our results toward convex operators remains an open
question."

This packet answers the direct finite-valued algebraic version of that
question in the same order-theoretic setting as Appendix A of the source
paper. If `V` is a real vector space, `W` is a Dedekind complete Riesz space,
and `f: V -> W` is order-convex, then

```text
f(x) = sup { a(x) : a is affine and a <= f }
```

for every `x in V`. Moreover, if `V` is ordered and `f` is monotone, the affine
minorants can be chosen with positive linear parts. The proof uses the source
paper's Hahn-Banach-Kantorovich extension theorem on the order-valued
directional derivative of `f` at each base point.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper, rebuilt from arXiv
  source because no PDF was locally cached.
- `figures/open_problem_crop.png`: full-width crop of the Section 6 open
  question on page 22 of the rebuilt source PDF.
- `tmp/`: LaTeX build intermediates.

## Novelty Check

Local run indexes were searched for arXiv id `2404.10900`, the source title,
`convex operators`, `order-convex`, `affine minorants`, `affine envelope`,
`Hahn-Banach-Kantorovich`, and `Dedekind complete Riesz`.

Bounded web searches on July 3, 2026 for exact and close phrases around
`generalization of our results toward convex operators remains an open
question`, `Dedekind complete Riesz space convex operators affine envelope`,
`order-convex affine minorants Dedekind complete Riesz`, and
`Hahn-Banach-Kantorovich convex operators affine` did not find a matching
answer. Novelty confidence is still limited: scalar affine-minorant
representations are classical, and this packet claims the order-valued
finite-valued formulation prompted by this paper, not a literature census of
all vector-valued convex-duality variants.

## Human Review Notes

The proof depends on:

- The source paper's Hahn-Banach and Hahn-Banach-Kantorovich extension
  theorems for maps into Dedekind complete Riesz spaces.
- The lower boundedness of the order-valued directional quotient
  `(f(x+ty)-f(x))/t`.
- The lattice fact that the infimum of a decreasing directed family commutes
  with addition in the form used in Lemma 2.1 of the packet.

The theorem is finite-valued: it does not treat proper extended-valued convex
operators, topological closure questions, or conditional-expectation penalty
representations.
