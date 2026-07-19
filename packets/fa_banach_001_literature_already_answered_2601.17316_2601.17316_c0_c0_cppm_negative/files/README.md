# Literature-already-answered packet: `(c_0,c_0)` fails CPPm

Status: `literature_already_answered`

This packet records an exact later-literature answer found during the
Banach/functional-analysis search. It is not claimed as a new proof. The later
paper explicitly cites Han's Question 3.6 and says it gives a negative answer.

## Source

- arXiv:2601.17316
- Title: *Weak minimizing property on pairs of classical Banach spaces*
- Author: Manwook Han
- Local PDF: `source_paper.pdf`

## Target question

Han asks whether the pair `(c_0,c_0)` has the compact perturbation property for
the minimum modulus (CPPm).

The exact source location is shown in `figures/open_problem_crop.png`, cropped
from page 13 of `source_paper.pdf`.

## Later answer

- arXiv:2605.01397
- Title: *Weak Minimizing Property and the Compact Perturbation Property for the Minimum Modulus*
- Authors: Anselmo Raposo Jr. and Geivison Ribeiro
- Local PDF: `supporting_paper_2605.01397.pdf`

The answer is no. Raposo--Ribeiro construct a non-minimum-modulus-attaining
operator `T:c_0 -> c_0` with `m(T)=1/2` and a rank-one compact operator `K` such
that `T+K=I`, hence `m(T+K)=1>m(T)`.

## Files

- `solution_packet.pdf`: human-readable packet.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: original arXiv PDF containing the open question.
- `supporting_paper_2605.01397.pdf`: later arXiv PDF containing the explicit answer.
- `figures/open_problem_crop.png`: full-width crop showing the open question.
- `code/crop_open_question.py`: reproducible crop generator.
- `code/verify_cppm_example.py`: finite sanity checks for the construction.
- `tmp/`: build artifacts only.

## Human review note

This is a complete answer to the open problem, but it belongs in the literature
answer lane because the supporting paper explicitly knows it is answering Han's
question. The human check should focus on the later paper's Theorem 1 and the
rank-one perturbation construction.
