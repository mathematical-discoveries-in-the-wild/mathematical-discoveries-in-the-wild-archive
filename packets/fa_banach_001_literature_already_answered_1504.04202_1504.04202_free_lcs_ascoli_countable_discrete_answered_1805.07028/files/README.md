# Free locally convex spaces with the Ascoli property

Status: `literature_already_answered`

Source/open-problem paper: S. Gabriyelyan, J. Kakol, and G. Plebanek,
*The Ascoli property for function spaces and the weak topology of Banach and
Frechet spaces*, arXiv:1504.04202.

Supporting answer paper: S. Gabriyelyan, *On reflexivity and the Ascoli
property for free locally convex spaces*, arXiv:1805.07028.

## Identification

In the final section of arXiv:1504.04202, the source paper asks whether
`L(X)` (or `F(X)` or `A(X)`) being Ascoli forces `X` to be Ascoli
(`q:Ascoli-Free`), and then asks the sharper free locally convex space
question: if `L(X)` is Ascoli, must `X` be countable and discrete
(`q:Ascoli-Free-Discr`)?

The later paper arXiv:1805.07028 explicitly cites this as a question posed in
GKP and answers it. Its abstract states that, answering a question posed in
GKP, it proves that `L(X)` is Ascoli if and only if `X` is countable discrete.
Theorem 1.2 gives the precise statement for every Tychonoff space `X`.

## Scope

This fully answers `q:Ascoli-Free-Discr`. It also answers the `L(X)` branch of
`q:Ascoli-Free`, because a countable discrete space is Ascoli. The same theorem
also gives the expected consequence for the stronger `k_R` variant mentioned
right after the source question, since every `k_R`-space is Ascoli.

This packet does not answer the `F(X)` or `A(X)` parts of `q:Ascoli-Free`, nor
the separate question `q:Ascoli-Free-F` about free topological groups over
metrizable spaces.

## Search Evidence

The lane-1 queue selected arXiv:1504.04202. Cheap run indexes were searched for
`1504.04202`, the source title, `Ascoli property`, `function spaces`,
`free locally convex`, `L(X)`, `Question 3.6`, and related terms; no duplicate
packet for this target was found. Local source search then found arXiv:1805.07028,
whose abstract and introduction explicitly identify the GKP question and whose
Theorem 1.2 supplies the exact answer.

## Files

- `source_paper.pdf`: arXiv:1504.04202.
- `supporting_paper_1805.07028.pdf`: arXiv:1805.07028.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.
