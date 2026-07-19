# Intersection-body fixed points from arXiv:1006.1546

Status: `literature_already_answered`

Source/open-problem paper: Jaegil Kim, Vladyslav Yaskin, and Artem Zvavitch,
*The geometry of p-convex intersection bodies*, arXiv:1006.1546.

Supporting answer paper: Emanuel Milman, Shahar Shabelman, and Amir Yehudayoff,
*Fixed and Periodic Points of the Intersection Body Operator*,
arXiv:2408.08171.

## Identification

On PDF page 2, arXiv:1006.1546 recalls the fixed-point problem for the
intersection body operator `I`, citing Lutwak and Gardner.  It says that the
Euclidean ball is mapped to a Euclidean ball, asks whether there are other
fixed points of `I`, and notes that only a local result near the ball was known.

arXiv:2408.08171 explicitly answers this fixed-point problem for star bodies in
dimension `n >= 3`.  Its Theorem 1.1 proves that `I^2 K = cK` holds only for
centered ellipsoids, and Corollary 1.2 gives the fixed-point consequence:
`IK = cK` if and only if `K` is a centered Euclidean ball.  The paper states
that this is a complete answer to Gardner's fixed-point question and the
Fish-Nazarov-Ryabogin-Zvavitch question.

## Scope

This packet records the later literature answer to the fixed-point branch
quoted in arXiv:1006.1546.  The source paper's next question, whether `IK` must
be closer to the Euclidean ball than `K`, is answered negatively in the source
paper itself and is treated here only as context.  The dimension-two case is a
separate exceptional case: arXiv:2408.08171 notes that `I^2K=4K` for every
origin-symmetric star body in `R^2`, and `IK=2K` for bodies invariant under a
quarter-turn.

## Search Evidence

The lane-3 queue selected arXiv:1006.1546.  Cheap run indexes were searched for
`1006.1546`, `2408.08171`, `intersection body fixed points`, `p-convex
intersection bodies`, `Lutwak`, and `Gardner`; no duplicate packet for this
source relation was found.  Local corpus search and web search for `fixed
points intersection body operator` identified arXiv:2408.08171 as the decisive
later source.

## Files

- `source_paper.pdf`: arXiv:1006.1546.
- `supporting_paper_2408.08171.pdf`: arXiv:2408.08171.
- `source_1006.1546.tex`: local parsed source TeX used to locate the question.
- `supporting_2408.08171.tex`: local parsed source TeX used to locate the answer.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.
