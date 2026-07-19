# Literature-Already-Answered Packet: Strictly Singular Borel Converse

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an exact later-literature negative answer to the
converse question in Beanland's arXiv:0908.1113, not a new proof from this run.

## Source Problem

- Kevin Beanland, *An Ordinal Index on the Space of Strictly Singular
  Operators*, arXiv:0908.1113.
- Local PDF: `source_paper.pdf`.
- Source location: Section 4.5, "Future Research and Concluding Remarks",
  Question at `StrictlySingularBorel.tex` lines 337--341.

The source asks whether the converse of Theorem 3.4 holds: if separable Banach
spaces `X` and `Y` satisfy `SS_xi(X,Y) = SS(X,Y)` for some countable ordinal
`xi`, must `B(SS(X,Y))` be a Borel subset of `B(L(X,Y))` in the strong-operator
topology?

## Supporting Literature

- Kevin Beanland and Pandelis Dodos, *On strictly singular operators between
  separable Banach spaces*, arXiv:1006.2672.
- Local PDF: `supporting_paper_1006.2672.pdf`.
- Supporting location: Introduction, lines 187--205, especially Theorem 4.

The supporting paper explicitly identifies the conjecture from arXiv:0908.1113
Section 4.5 and says its second main result answers the question negatively.

## Literature Status

The answer is negative.  Theorem 4 of arXiv:1006.2672 states that for every
`1 <= p < infinity` there is a Banach space `Y_p` with an unconditional basis
such that `SS(ell_p,Y_p)` is complete coanalytic, hence non-Borel, while every
strictly singular operator `T: ell_p -> Y_p` satisfies `varrho(T) <= 2`.

By Definition 1 in the same paper, `varrho(T)` is the least ordinal `xi` for
which `T` is `S_xi`-strictly singular.  Therefore `varrho(T) <= 2` for all
strictly singular `T` gives

```text
SS_2(ell_p,Y_p) = SS(ell_p,Y_p),
```

but `SS(ell_p,Y_p)` is not Borel.  This is precisely a counterexample to the
source question.

## Limitations

- This is a status packet, not an original solution from this run.
- It answers the global converse question negatively; it does not classify
  which pairs `(X,Y)` with bounded Schreier strictly singular index do have
  Borel `SS(X,Y)`.
- The source paper works on the unit ball `B(L(X,Y))`; the supporting paper
  states the non-Borel result in the standard Borel space `L(ell_p,Y_p)`.
  Restricting/scaling gives the same obstruction for the unit-ball formulation.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: original open-problem paper.
- `supporting_paper_1006.2672.pdf`: later paper answering the problem.
- `tmp/`: LaTeX build intermediates.

## Verification And Search Notes

Before packaging, the lightweight indexes were searched for `0908.1113`, the
title phrase, `ordinal index`, `strictly singular`, `Borel`, `SS_xi`, and
related keywords.  No existing exact packet was found.  Web/arXiv search for
the source question found arXiv:1006.2672, whose abstract and introduction
explicitly state the negative answer to the conjecture from arXiv:0908.1113.

## Human Review Recommendation

Treat arXiv:0908.1113 Section 4.5 as already answered negatively by
arXiv:1006.2672.  Keep this packet as literature-status memory to prevent
duplicate work on this target.

