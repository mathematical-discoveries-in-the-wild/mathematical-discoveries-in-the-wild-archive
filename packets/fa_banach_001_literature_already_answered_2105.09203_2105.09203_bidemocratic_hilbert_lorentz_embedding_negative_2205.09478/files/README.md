# Literature-Already-Answered Packet: bidemocratic Hilbert Lorentz embedding

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: a separate later paper explicitly gives a negative answer to Question
5.3 of arXiv:2105.09203. This packet records literature status only; it is not
an original proof from the run.

## Original Problem Source

- J. L. Ansorena, G. Bello, P. Wojtaszczyk, *Lorentz spaces and embeddings
  induced by almost greedy bases in superreflexive Banach spaces*,
  arXiv:2105.09203.
- Local source lines inspected: `data/parsed/arxiv_sources/2105.09203/source.tex`,
  lines 723--730.
- Local PDF: `source_paper.pdf`, if download succeeds.

The source asks whether every bidemocratic basis `B` of `ell_2` admits Lorentz
exponents `1 < q < r < infinity` such that
`ell_{2,q} -> ell_2 -> ell_{2,r}` via `B`.

## Supporting Answer Source

- F. Albiac, J. L. Ansorena, M. Berasategui, *Sparse approximation using new
  greedy-like bases in superreflexive spaces*, arXiv:2205.09478.
- Local source lines inspected: `data/parsed/arxiv_sources/2205.09478/source.tex`,
  lines 1053--1073.
- Local PDF: `supporting_paper_2205.09478.pdf`, if download succeeds.

## Status Match

The supporting paper constructs, in particular for Hilbert space, a
bidemocratic basis `B` with unconditionality parameters
`k_m[B] approx log(1+m)`. Its Remark following Corollary 4.6 states that if a
basis is squeezed between `d_q(w)` and `d_r(w)` with `1 <= q <= r <= infinity`
and either `q > 1` or `r < infinity`, then
`k_m[B] lesssim (1+log m)^{1/q - 1/r}`. This exponent is strictly smaller than
1 when `1 < q < r < infinity`.

Consequently the Hilbert-space bidemocratic basis constructed in
arXiv:2205.09478 cannot satisfy the Lorentz embeddings asked for in Question
5.3 of arXiv:2105.09203. The supporting paper explicitly says that this basis
is a counterexample solving that question negatively.

## Scope Limitations

This packet clears only Question 5.3 of arXiv:2105.09203, the bidemocratic
`ell_2` Lorentz-squeezing question. It does not answer the preceding open
questions in that paper about quasi-greedy bases in superreflexive spaces or
dual quasi-greediness in `ell_p`.

## Verification Notes

- Same-paper check: arXiv:2105.09203 asks the bidemocratic `ell_2` question and
  does not answer it there.
- Separate-source check: arXiv:2205.09478 is a distinct later paper and
  explicitly cites `ABW2021, Question 5.3`.
- Local duplicate check: the run indexes had no exact packet for arXiv:2205.09478
  or ABW Question 5.3 before creation.
- Scope check: the negative answer uses bidemocratic Hilbert-space bases, so it
  matches the exact hypotheses of Question 5.3.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source, if available.
- `supporting_paper_2205.09478.pdf`: decisive supporting answer source, if
  available.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:2105.09203 asks whether every bidemocratic basis of `ell_2` has the
   stated Lorentz embeddings.
2. arXiv:2205.09478 constructs a bidemocratic basis in Hilbert space with
   logarithmic unconditionality growth.
3. arXiv:2205.09478 explicitly states that this basis is a negative
   counterexample to `[ABW2021, Question 5.3]`.
