# Literature Answer: unbounded DGG lemma for Hodge Laplacians

Status: `literature_already_answered`.

## Source Question

- Source: Bobo Hua and Xin Luo, "Davies-Gaffney-Grigor'yan lemma on simplicial complexes", arXiv:1702.00529; published in Math. Z. 290 (2018), 1041--1053.
- Location: Remark 1.1, page 3 of the arXiv PDF.
- Question: after proving the Davies-Gaffney-Grigor'yan lemma for bounded discrete Hodge Laplacians on simplicial complexes, Hua--Luo ask whether the result also holds in the unbounded case.

## Answering Paper

- Supporting answer: Philipp Bartmann and Matthias Keller, "The heat equation and independence of the spectrum of the Hodge Laplacian on `ell^p`", arXiv:2602.18597.
- Exact answer location: Theorem 2.2 proves a DGG estimate for general positive magnetic Schrodinger operators on graphs, and Theorem 5.1 specializes it to weighted simplicial-complex Hodge Laplacians. The text before Theorem 5.1 explicitly says this answers Hua--Luo Remark 1.1.

## Identification

This is an explicit later-paper answer, not a new proof from the run. Hua--Luo's restriction was bounded Hodge Laplacians; Bartmann--Keller remove that boundedness obstruction by passing through positive magnetic Schrodinger operators with closable positive forms and then applying the signed-Schrodinger representation of weighted simplicial-complex Laplacians.

## Files

- `source_paper.pdf`: arXiv:1702.00529, original/open-question source.
- `supporting_paper_2602.18597.pdf`: arXiv:2602.18597, supporting answer source.
- `solution_packet.pdf`: compact status note.

Ledger: `runs/fa_banach_001/ledger/results/1702.00529_dgg_unbounded_hodge_answered_by_2602.18597.json`.
