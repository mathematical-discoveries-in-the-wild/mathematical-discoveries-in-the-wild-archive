# Literature Answer: Isom(QU) Reflexive Fixed-Point Question

status: literature_already_answered

## Source Question

- Source paper: Christian Rosendal, *Large scale geometry of metrisable
  groups*, arXiv:1403.3106.
- Source location: Problem 66, page 39 of the source PDF.
- Source question: whether `Isom(QU)`, the isometry group of the rational
  Urysohn metric space, admits a continuous affine isometric action on a
  reflexive Banach space without a fixed point.

## Answering Source

- Supporting paper: Christian Rosendal, *Equivariant geometry of Banach spaces
  and topological groups*, arXiv:1610.01070.
- Supporting location: Corollary 12, page 5, and Theorem 81, pages 47--48.
- Answer: no.  Theorem 81 proves that for `G = Isom(ZU)` or `Isom(QU)` and
  `E` reflexive, every quasi-cocycle `G -> E` is bounded; in particular every
  continuous affine isometric action `G` on `E` has a fixed point.

## Scope

This exactly answers Problem 66 of arXiv:1403.3106.  It does not answer the
broader Problem 67 from the same source about all non-Archimedean Polish
groups.  The supporting paper also explicitly leaves open the stronger
non-isometric affine-action variant for `Isom(QU)`, where the linear part may
be an unbounded subgroup of `GL(E)`.

## Provenance

This is not a new result of the run.  The run contribution is the identification
that the later Rosendal paper answers the earlier Rosendal Problem 66 exactly.

## Files

- [main.tex](main.tex): compact status note.
- [solution_packet.pdf](solution_packet.pdf): rendered status packet.
- [source_paper.pdf](source_paper.pdf): arXiv:1403.3106 source paper.
- [supporting_paper_1610.01070.pdf](supporting_paper_1610.01070.pdf):
  arXiv:1610.01070 supporting answer source.

## Checks

Cheap run indexes were searched for `1403.3106`, the source title,
`Isom(QU)`, `rational Urysohn`, `reflexive`, `fixed point`, `Rosendal`, and
`property (OB)`.  The only relevant existing run note was an attempt for
arXiv:1610.01070, which already observed that arXiv:1610.01070 answers the
older affine-isometric `Isom(QU)` problem.

Web/arXiv checks on 2026-06-16 confirmed the source metadata for arXiv:1403.3106
and arXiv:1610.01070.  Local PDF text extraction found Problem 66 in the source
PDF and Theorem 81/Corollary 12 in the supporting PDF.
