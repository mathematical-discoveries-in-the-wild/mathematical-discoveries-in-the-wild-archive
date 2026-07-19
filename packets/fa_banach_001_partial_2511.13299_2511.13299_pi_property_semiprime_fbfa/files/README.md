# Partial Packet: MAP subcase for free Banach f-algebras

status: strengthened_partial_result_likely_valid
arxiv_id: 2511.13299
source: David Munoz-Lahoz and Pedro Tradacete, "Free Banach f-algebras"

## Result

This packet gives a partial positive answer to Question 5.10 of the source
paper:

```text
Is FBfA[E] semiprime for every Banach space E?
```

The proved subcase is:

```text
If E has the metric approximation property, equivalently if E admits a net of
finite-rank contractions R_lambda:E->E with R_lambda x -> x for every x in E,
then FBfA[E] is semiprime. Consequently FBfA[E] is representable in C(B_{E^*}).
```

This includes, for example, Banach spaces with a monotone Schauder basis or a
monotone finite-dimensional decomposition. It strictly improves the earlier
projection-approximation packet: the finite-rank approximants do not need to be
projections. The full source question remains open for Banach spaces without
MAP.

## Packet Contents

- `main.tex`: human-readable proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the arXiv source paper.
- `figures/open_problem_crop.png`: crop of PDF page 66 containing Question 5.10.

## Verification Notes

The proof is non-computational. It uses:

- the source universal property of `FBfA[E]`,
- the source finite-dimensional semiprimeness result,
- the source equivalence between semiprimeness and representability,
- a direct continuity lemma for the induced free algebra maps.

No full solution is claimed. The argument uses contractivity in an essential
way through the universal property, so it does not immediately extend from MAP
to the bounded approximation property.
