# Literature-Already-Answered Packet: Quasi-Greedy Democracy in ell_p

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Fernando Albiac, Jose L. Ansorena, Przemyslaw Wojtaszczyk,
  *On certain subspaces of ell_p for 0<p<=1 and their applications to
  conditional quasi-greedy bases in p-Banach spaces*, arXiv:1912.08449;
  later Math. Ann. 379 (2021), no. 1-2, 465--502.
- Local PDF: `source_paper_1912.08449.pdf`.
- Location: parsed source `data/parsed/arxiv_sources/1912.08449/source.tex`,
  lines 731--735.

The source asks whether every quasi-greedy basis in `ell_p` for `0<p<1` is
democratic.

## Answer Source

- Fernando Albiac, Jose L. Ansorena, Przemyslaw Wojtaszczyk,
  *Quasi-greedy bases in the spaces ell_p (0<p<1) are democratic*,
  arXiv:2004.05206; later J. Funct. Anal. 280 (2021), no. 7, 108871.
- Local PDF: `answer_paper_2004.05206.pdf`.
- Locations: abstract, parsed source line 125; Theorem 1, parsed source
  lines 266--271.

The answer paper proves that all quasi-greedy bases of `ell_p` for `0<p<1`
are democratic, with lower and upper democracy functions both equivalent to
`m^(1/p)`.

## Corroborating Source

- Fernando Albiac, Jose L. Ansorena, Glenier Bello,
  *Democracy of quasi-greedy bases in p-Banach spaces with applications to the
  efficiency of the TGA in the Hardy spaces H_p(D^d)*, arXiv:2208.09342.
- Local PDF: `supporting_paper_2208.09342.pdf`.
- Locations: parsed source lines 112--115 and 944--957.

The 2022 paper cites the 2021 JFA article by title, confirming the later
literature status and using it as the basis for a further Hardy-space
question.

## Status

The ell_p democracy question from arXiv:1912.08449 is already answered in the
later literature. The answer is positive: every quasi-greedy basis in `ell_p`
for `0<p<1` is democratic.

## Limitations

- This is not a new proof produced by the run.
- This packet records only the literature status of the `ell_p` question from
  arXiv:1912.08449.
- It does not address the separate `q`-envelope question for `SL_p` spaces
  that appears later in arXiv:1912.08449.
- A nearby existing packet,
  `solutions/literature_already_answered/2004.05206_hp_hardy_democracy_answered_by_2208.09342/`,
  handles the distinct Hardy-space Question 3.8 from arXiv:2004.05206.

## Files

- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper_1912.08449.pdf`: original/open-problem source.
- `answer_paper_2004.05206.pdf`: direct answer paper.
- `supporting_paper_2208.09342.pdf`: corroborating later paper.

## Human Review Recommendation

Verify that the question at lines 731--735 of arXiv:1912.08449 is exactly the
ell_p democracy question, and that Theorem 1 of arXiv:2004.05206 gives the
positive answer for every quasi-greedy basis of `ell_p`, `0<p<1`.
