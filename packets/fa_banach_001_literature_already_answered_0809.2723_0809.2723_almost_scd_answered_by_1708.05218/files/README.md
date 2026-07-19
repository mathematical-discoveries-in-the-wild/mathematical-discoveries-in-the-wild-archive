# Literature Status: almost-SCD sets need not be SCD

- Run: `fa_banach_001`
- Source paper: Antonio Avilés, Vladimir Kadets, Miguel Martín, Javier Merí, Varvara Shepelska, *Slicely Countably Determined Banach spaces*, arXiv:0809.2723.
- Source location: Question 7.5, page 27 of the source PDF; TeX source lines 2425--2428.
- Supporting paper: Vladimir Kadets, Antonio Pérez, Dirk Werner, *Operations with slicely countably determined sets*, arXiv:1708.05218.
- Supporting location: abstract and Section 4; especially page 4, Section 4 on page 16, and Theorem 4.3 on page 18 of the supporting PDF.
- Result type: `literature_already_answered`.
- Status: exact later literature answer; not a new run proof.

## Source Question

Question 7.5 of arXiv:0809.2723 asks whether the concepts of SCD sets and
almost-SCD sets are equivalent, referring to Remark 4.5 for the definition.

## Supporting Answer

Kadets--Pérez--Werner explicitly identify the question as
`[2, Question 7.5]` and state that almost-SCD and SCD are not equivalent for
general bounded closed convex sets. Their Theorem 4.3 proves the decisive
negative example: if `X` has the Daugavet property, then there is a convex
closed bounded set `C` which is aSCD but not SCD.

They also prove a positive balanced-set refinement: every convex closed
bounded balanced aSCD set is SCD. Thus the general equivalence question is
answered negatively, while the balanced case relevant to many unit-ball
applications has an affirmative answer.

## Scope Notes

This packet records the exact later-literature answer to Question 7.5 only.
It does not claim a new proof or cover the other open questions in Section 7
of the source paper.

The source paper's Remark 4.5 phrases almost-SCD using a sequence of subsets.
The supporting paper uses the standard later formulation with a sequence of
slices and explicitly cites the source question; under this stronger slice
formulation it still gives a negative answer for general convex closed
bounded sets.

## Verification

- `source_paper.pdf`: local copy of arXiv:0809.2723.
- `supporting_paper_1708.05218.pdf`: local copy of arXiv:1708.05218.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.
- Search evidence: local run indexes had no existing packet for
  `0809.2723`, `1708.05218`, `almost-SCD`, or `aSCD`; web search for
  `"almost slicely countably determined"` surfaced arXiv:1708.05218, whose
  abstract explicitly says it demonstrates that almost SCD sets need not be
  SCD and answers Avilés et al.
