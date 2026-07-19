# Literature-Already-Answered Packet: Hardy-Space Quasi-Greedy Democracy

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Fernando Albiac, Jose L. Ansorena, Przemyslaw Wojtaszczyk,
  *Quasi-greedy bases in the spaces ell_p (0<p<1) are democratic*,
  arXiv:2004.05206; later J. Funct. Anal. 280 (2021), no. 7, 108871.
- Local PDF: `source_paper.pdf`.
- Location: Question 3.8, PDF page 16; parsed source
  `data/parsed/arxiv_sources/2004.05206/source.tex`, lines 555--557.

The source asks whether, for `0<p<1` and `d in N`, all quasi-greedy bases in
`H_p(D^d)` are democratic.

## Supporting Answer Source

- Fernando Albiac, Jose L. Ansorena, Glenier Bello,
  *Democracy of quasi-greedy bases in p-Banach spaces with applications to the
  efficiency of the TGA in the Hardy spaces H_p(D^d)*, arXiv:2208.09342.
- Local PDF: `supporting_paper_2208.09342.pdf`.
- Locations: abstract and introduction, PDF pages 1 and 4; Corollary 4.3,
  PDF page 21; Corollary 4.6, PDF page 22.

## Status

Question 3.8 of arXiv:2004.05206 is already answered by arXiv:2208.09342.
The supporting paper explicitly says it is solving a problem raised in the
source paper, cited there as `AAW2021`, and its bibliography identifies
`AAW2021` as the JFA version of arXiv:2004.05206.

The answer is split by dimension: all quasi-greedy bases of `H_p(D)` for
`0<p<1` are democratic, while for `d>=2` no quasi-greedy basis of
`H_p(D^d)` is democratic. Thus the universal question over `d in N` has a
positive one-variable case and a negative multivariable case.

## Limitations

- This is not a new proof or counterexample produced by this run.
- The durable claim is only the literature status of Question 3.8 from
  arXiv:2004.05206.
- The packet does not analyze any new problems raised by arXiv:2208.09342.

## Files

- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2208.09342.pdf`: supporting answer paper.

## Human Review Recommendation

Verify that `AAW2021` in arXiv:2208.09342 is the JFA publication of
arXiv:2004.05206, and that Question 3.8 on PDF page 16 is exactly the
Hardy-space democracy question addressed on PDF pages 1, 4, 21, and 22 of the
supporting paper.
