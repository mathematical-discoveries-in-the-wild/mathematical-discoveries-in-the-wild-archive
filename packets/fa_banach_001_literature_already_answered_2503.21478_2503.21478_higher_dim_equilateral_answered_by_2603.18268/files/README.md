# Higher-Dimensional Equilateral Sets In Banach-Mazur Compacta

Status: `literature_already_answered`

Source/open-problem paper: Tomasz Kobos and Konrad Swanepoel,
*Equilateral dimension of the planar Banach--Mazur compactum*,
arXiv:2503.21478; later listed as Proc. Amer. Math. Soc. 153(10)
(2025), 4423-4436.

Supporting answer paper: Florian Grundbacher and Tomasz Kobos,
*Exact Banach--Mazur distances of certain ell_p-sums and cones*,
arXiv:2603.18268.

## Identification

The source paper's Concluding remarks, PDF page 13, say that it is not clear
whether the planar construction generalizes to higher dimensions and state
that most likely the `n`-dimensional Banach--Mazur compactum contains
arbitrarily large equilateral sets for every `n >= 2`.

The supporting paper explicitly knows it is using this same source: its
abstract says that it lifts the recent planar construction to all higher
dimensions, and Corollary 1.9 states that for every pair of integers
`n,m >= 2`, the symmetric `n`-dimensional Banach--Mazur compactum has an
equilateral set of cardinality `m`.

## Scope

This answers the source paper's higher-dimensional existence question for the
symmetric Banach--Mazur compactum. It does not answer the source paper's
separate planar-distance question asking whether the construction can work for
all distances in an interval `(1,c]`, nor the broader finite-metric-space
universality speculation.

## Files

- `source_paper.pdf`: arXiv:2503.21478 source paper.
- `supporting_paper_2603.18268.pdf`: arXiv:2603.18268 supporting answer.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status packet.
- `tmp/`: LaTeX build intermediates and temporary rendered page images.

## Search Evidence

The cheap run indexes were searched for arXiv:2503.21478, the paper title,
`equilateral dimension`, `planar Banach-Mazur`, `Banach-Mazur compactum`, and
`equilateral`. No duplicate packet for this exact source question was found.
A local parsed-source search then found arXiv:2603.18268, whose abstract,
Corollary 1.9, and proof of Corollary 1.9 explicitly answer the
higher-dimensional existence question.
