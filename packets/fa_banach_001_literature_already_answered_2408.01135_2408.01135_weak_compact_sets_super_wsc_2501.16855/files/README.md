# Literature-already-answered packet: weak compact sets super weakly compact imply WSC

Status: `literature_already_answered`

This packet records an exact later-literature answer found during the
Banach/functional-analysis search. It is not claimed as a new proof. The later
paper explicitly cites Silber's Question 1 from arXiv:2408.01135 and gives a
negative answer.

## Source

- arXiv:2408.01135
- Title: *Weak compactness in Lipschitz-free spaces over superreflexive spaces*
- Author: Zdenek Silber
- Local PDF: `source_paper.pdf`

## Target question

Silber asks whether there is a Banach space in which every relatively weakly
compact set is relatively super weakly compact, but which is not weakly
sequentially complete.

The exact source location is shown in `figures/open_problem_crop.png`, cropped
from page 11 of `source_paper.pdf`.

## Later answer

- arXiv:2501.16855
- Title: *On weak sequential completeness of spaces where weakly compact sets are super weakly compact*
- Author: Zdenek Silber
- Local PDF: `supporting_paper_2501.16855.pdf`

The answer is negative: no such Banach space exists. The later paper proves
that if relatively weakly compact sets in `X` are relatively super weakly
compact, then `X` is weakly sequentially complete.

## Files

- `solution_packet.pdf`: human-readable packet.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: original arXiv PDF containing the open question.
- `supporting_paper_2501.16855.pdf`: later arXiv PDF containing the explicit answer.
- `figures/open_problem_crop.png`: full-width crop showing the original question.
- `figures/supporting_answer_crop.png`: crop showing the later paper citing and answering the question.
- `figures/supporting_theorem_crop.png`: crop showing the later theorem statement.
- `code/crop_evidence.py`: reproducible crop generator.
- `tmp/`: build artifacts only.

## Human review note

This is a complete status answer to Question 1, but it belongs in the
literature-answer lane because the supporting paper explicitly knows it is
answering the earlier question. The human check should focus on the exact
identification between the source question's relative formulation and Theorem
2.8 in arXiv:2501.16855.
