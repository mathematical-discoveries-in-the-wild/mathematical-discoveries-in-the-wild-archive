# Literature-Already-Answered Packet: LD2P and D2P Are Different

Run: `fa_banach_001`

Agent: `agent_lane_08`

Result type: `literature_already_answered`

Status note: this is not a new result from the run. It records that a
nearby uncertainty in arXiv:1206.3539 was answered in later literature.
The two deterministic queue signals in arXiv:1206.3539 were same-paper
ask-and-answer passages and are not promoted as results.

## Source Problem

- Trond A. Abrahamsen, Vegard Lima, Olav Nygaard, *Almost isometric ideals in
  Banach spaces*, arXiv:1206.3539.
- Local PDF: `source_paper.pdf`.
- Exact location: Section 3, Definition 3.1 and the following paragraph,
  PDF page 7.

The source defines:

- local diameter 2 property (LD2P): every slice of the unit ball has diameter 2;
- diameter 2 property (D2P): every non-empty relatively weakly open subset of
  the unit ball has diameter 2.

Immediately after the definition the authors write that they do not know
whether properties (i) and (ii) are really different.

## Supporting Literature

- Julio Becerra Guerrero, Gines Lopez-Perez, Abraham Rueda Zoca, *Big slices
  versus big relatively weakly open subsets in Banach spaces*, arXiv:1304.4397,
  later J. Math. Anal. Appl. 428 (2015), 855--865.
- Local PDF: `supporting_paper_1304.4397.pdf`.
- Exact locations: introduction, PDF page 2; Theorem 2.4 and Corollary 2.5,
  PDF page 10.

The supporting paper says it proves the existence of a Banach space satisfying
the slice diameter 2 property and failing the diameter 2 property, answering
the equivalence problem negatively. In that paper's notation, `SD2P` means
the slice diameter 2 property, which is the same as LD2P in arXiv:1206.3539;
it is not the later/modern strong diameter 2 property.

## Literature Status

The answer is negative. LD2P and D2P are different properties. More strongly,
every Banach space containing an isomorphic copy of `c_0` admits an equivalent
norm for which every slice of the new unit ball has diameter 2, while the new
unit ball contains non-empty relatively weakly open subsets of arbitrarily
small diameter. Such a norm has LD2P and fails D2P.

The supporting authors explicitly frame their result as answering the open
problem about equivalence between slice/local D2P and D2P. The link to the
specific arXiv:1206.3539 passage is exact by matching definitions and the
same question, although the supporting paper cites the earlier ALN source for
the problem.

## Same-Paper False Positives In The Queue Hit

The deterministic queue hit also detected two passages that should not be
counted:

- Introduction line around source line 288 asks for an analogue of a theorem,
  and the same paper immediately proves the analogue.
- Section 3 line around source line 706 says the authors do not know an
  explicit reference for bidual-to-space inheritance of D2P, and the same paper
  immediately proves a stronger ai-ideal inheritance proposition.

Those passages are extraction false positives under the packet standard.

## Files

- `README.md`: this summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1206.3539.
- `supporting_paper_1304.4397.pdf`: arXiv:1304.4397.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Treat this as already answered in the literature. It should prevent future
agents from trying to solve the LD2P-vs-D2P separation from arXiv:1206.3539
as a new problem, while preserving that the queue's two counted signals were
same-paper false positives.
