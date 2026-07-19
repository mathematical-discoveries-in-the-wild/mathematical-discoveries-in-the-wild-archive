# Literature-Already-Answered Packet: positive Schauder bases in the L2 case

Run: `fa_banach_001`

Result type: `literature_already_answered` / partial subcase

Status: a later paper gives a positive answer to the `p=2` case of the
nonnegative Schauder-basis question mentioned in arXiv:1812.06313. This packet
records literature status only; it is not an original proof from the run.

## Original Problem Source

- N. Nikolski and A. Volberg, *On the Sign Distributions of Hilbert Space
  Frames*, arXiv:1812.06313.
- Local source inspected: `data/parsed/arxiv_sources/1812.06313/source.tex`,
  lines 1148--1154.
- Local PDF: `source_paper.pdf`.

After constructing a positive uniformly minimal complete normalized sequence
in `L^2_R(0,1)` which is not a basis, the source says that the existence of a
nonnegative Schauder basis in `L^p`, `p>1`, is open to the authors' knowledge.
It also recalls the known positive `p=1` construction of Johnson--Schechtman.

## Supporting Answer Source

- D. Freeman, A. M. Powell, and M. A. Taylor, *A Schauder basis for L2
  consisting of non-negative functions*, arXiv:2003.09576; Math. Ann. 383
  (2022), 181--208.
- Local supporting source inspected from arXiv e-print:
  `tmp/supporting_source_2003.09576.tar`.
- Local PDF: `supporting_paper_2003.09576.pdf`.

## Status Match

The supporting paper explicitly states that the conditional positive
Schauder-basis problem had remained open for all `1<p<infinity` after the
Johnson--Schechtman `L_1` construction. Its Theorem 2.2 proves that, for every
`epsilon>0`, `L_2(R)` has a positive Schauder basis with basis constant at most
`1+epsilon`.

The supporting paper also records that the same conclusion extends to all
separable `L_2(mu)` spaces. Thus the Hilbert-space/L2 case of the source's
`p>1` question is answered positively.

## Scope Limitations

This is not a full answer to the source's entire `L^p`, `p>1`, sentence. The
same supporting paper states as Problem 5.1 that the cases
`1<p<infinity`, `p != 2`, remain open. It also proves a weaker result for
those exponents: a nonnegative Schauder basic sequence whose closed span
contains an isomorphic copy of `L_p(R)`.

## Verification Notes

- Same-paper check: arXiv:1812.06313 does not build a nonnegative Schauder
  basis; it builds a positive uniformly minimal complete sequence which is not
  a basis, then states the Schauder-basis question.
- Separate-source check: arXiv:2003.09576 is a later paper devoted to the
  positive Schauder-basis question.
- Exact-scope check: Theorem 2.2 answers `p=2`; Problem 5.1 in the supporting
  paper leaves `p != 2` open.
- Local duplicate check: the cheap run indexes contained a failed attempt on
  later Markushevich-basis questions from arXiv:2003.09576, but no packet
  recording the literature answer to arXiv:1812.06313's `L_2` subcase.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2003.09576.pdf`: decisive supporting answer source.
- `tmp/supporting_source_2003.09576.tar`: downloaded arXiv e-print payload
  used to inspect theorem statements.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:1812.06313 says that the existence of nonnegative Schauder bases in
   `L^p`, `p>1`, was open to the authors' knowledge.
2. arXiv:2003.09576, Theorem 2.2, constructs a positive Schauder basis for
   `L_2(R)`.
3. arXiv:2003.09576, Problem 5.1, explicitly leaves the non-Hilbert cases
   `1<p<infinity`, `p != 2`, open.
