# Literature-Already-Answered Packet: Conditional Bases with Property (A)

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Fernando Albiac, José L. Ansorena, Vladimir Temlyakov, *Twenty-five years
  of greedy bases*, arXiv:2405.20939.
- Local PDF: `source_paper.pdf`.
- Location: Section 4, "Isometric almost greediness", PDF page 11, Problem 6.

The source asks: "Does Property (A) imply unconditionality?" The same page also
asks whether there is a Banach space with a conditional
`1`-suppression quasi-greedy basis.

## Supporting Answer Source

- Fernando Albiac, José L. Ansorena, Miguel Berasategui, Pablo M. Berná,
  *Conditional bases with Property (A)*, arXiv:2409.04883.
- Local PDF: `supporting_paper_2409.04883.pdf`.
- Location: introduction, PDF page 4, citing arXiv:2405.20939 as `AAT2024`
  Problem 6; Theorem 3.3 and Corollary 3.7 around PDF pages 14--15.

## Status

Problem 6 of arXiv:2405.20939 is already answered negatively by
arXiv:2409.04883. The supporting paper explicitly says that the problem was
raised in arXiv:2405.20939 and that it answers the question negatively. Its
construction yields Banach spaces with Schauder bases that have Property (A)
but fail to be unconditional.

The same supporting paper also records that the construction answers the
nearby `1`-suppression quasi-greedy question negatively: it builds a
conditional `1`-suppression quasi-greedy basis.

## Limitations

- This is not an original counterexample produced by this run.
- The durable claim here is the literature status of the 2405.20939 question.
- The packet does not analyze the later paper's remaining open questions about
  reflexive spaces or Hilbert-space renormings.

## Files

- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2409.04883.pdf`: supporting answer paper.

## Human Review Recommendation

Verify that the citation `AAT2024` in arXiv:2409.04883 is the same paper as
arXiv:2405.20939, and that "Problem 6" there is exactly the Property (A)
unconditionality problem on PDF page 11 of the source paper.
