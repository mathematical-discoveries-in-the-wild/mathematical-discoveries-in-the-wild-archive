# Literature status: Problem 14 on coarse embeddability of ell_2

status: literature_already_answered

source_arxiv: 1207.2958

supporting_arxiv: 1705.06797

source_problem: Godefroy--Lancien--Zizler, Problem 14

packet_verdict: negative answer already in later literature

## Summary

Problem 14 in arXiv:1207.2958 asks:

> Does `ell_2` coarsely embed into every infinite dimensional Banach space?

Baudier--Lancien--Schlumprecht, arXiv:1705.06797, explicitly cites this as
Problem 14 of the Godefroy--Lancien--Zizler survey and restates the same
question as its Main Problem. The later paper answers it negatively. In
particular, it proves that `ell_2` does not coarsely embed into Tsirelson's
original space `T^*`, and more generally that there is no coarsely minimal
infinite-dimensional Banach space.

Thus the source problem is not a finite-dimensional question: the source crop
and the supporting paper both say "infinite dimensional Banach space".

## Evidence

- `source_paper.pdf`: original survey, arXiv:1207.2958.
- `supporting_paper_1705.06797.pdf`: later answer paper.
- `figures/open_problem_crop.png`: source Problem 14.
- `figures/supporting_restatement_crop.png`: later paper citing Problem 14
  and restating the question.
- `figures/supporting_answer_crop.png`: later paper's negative answer via
  nonexistence of coarsely minimal infinite-dimensional Banach spaces.

## Scope

This packet only records the answer to arXiv:1207.2958 Problem 14. It does not
claim an answer to the later and stronger-looking follow-up question in
arXiv:1705.06797 asking whether `ell_2` coarsely embeds into every
super-reflexive Banach space. The run registry records a human-rejected packet
for a finite-dimensional literal reading of that later super-reflexive
question; this packet does not reuse that reading and does not inspect the
human-only archive.

## Verification Notes

- Cheap-index search found no prior packet for arXiv:1207.2958 or this exact
  `ell_2`/every infinite-dimensional Banach-space question.
- The only relevant registry hit was the separate human-rejected
  arXiv:1705.06797 Problem 5.1 finite-dimensional-reading pitfall, which is a
  different later super-reflexive question.
- Active-claim check found nearby Kalton graph/Hamming metric work but no
  active claim on Problem 14 of arXiv:1207.2958.
- External search used exact phrases including "Does ell_2 coarsely embed
  into every infinite dimensional Banach space" and found arXiv:1705.06797.
  The local supporting TeX confirms it cites Problem 14 and answers it.

Human-review recommendation: accept as a literature-already-answered packet,
with the finite-versus-infinite wording checked directly from both sources.

