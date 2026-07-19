# Literature Status: Question 5.2 Answered by Later Positive-Topology Paper

Status: `literature_already_answered` for Question 5.2; adjacent `q=2` similarity subcase also answered.

Source paper: arXiv:2409.14481, Valentin Gillet, *Typical properties of positive contractions and the invariant subspace problem*.

Later paper: arXiv:2412.11587, Valentin Gillet, *Similar operator topologies on the space of positive contractions*.

## Question Identified

In Section 5, "Further remarks and questions", arXiv:2409.14481 asks:

- Question 5.2: whether the point spectrum of an SOT-typical positive contraction on `ell_2` is the open unit disk.
- Final Section 5 question: whether SOT and SOT* are similar on `P_1(ell_q)` for `1 < q <= 2`.

## Resolution by Later Literature

The later paper arXiv:2412.11587 explicitly says that it gives a negative answer to `Question 5.2` from arXiv:2409.14481. Its theorem labeled `introthvpspos`, restated in the applications section as `corvpspostopotau`, proves that for every Polish operator topology on `P_1(ell_2)` lying between WOT and SOT*, a typical positive contraction `T` has no eigenvalue and `T*` has no eigenvalue. In particular, for the SOT topology, the point spectrum is empty, not the open unit disk.

The same later paper also proves the `q=2` case of the source paper's final similarity question: theorem `introthtoposimsurl2` says that WOT, SOT_*, SOT, and SOT* are all similar on `P_1(ell_2)`.

## Scope Notes

This is not new mathematical progress; it is a later-literature status packet.

The source paper is not completely cleared. The following remain outside this packet:

- the invariant-subspace question for typical positive contractions on `ell_q`, `1 < q != 2 < infinity`;
- the hypercyclicity question for `(2T)*` when `1 < q < 2`;
- the non-Hilbert similarity problem for `1 < q < 2` in the source question, and the broader `p != 2` similarity problem later isolated in arXiv:2412.11587;
- the SOT version of the reflexive-monotone-basis AAB theorem;
- the compact-commutant question for typical positive contractions on `ell_2`.

## Evidence Checked

- Local source `data/parsed/arxiv_sources/2409.14481/main.tex`, Section 5 question block.
- Local source `data/parsed/arxiv_sources/2412.11587/main.tex`, introduction/main results and applications.
- Web search for the exact source title and exact question phrases found arXiv:2412.11587 as the relevant later answer.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:2409.14481.
- `supporting_paper_2412.11587.pdf`: later paper giving the answer.
