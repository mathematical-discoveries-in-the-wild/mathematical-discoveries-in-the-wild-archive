# Literature-Already-Answered Packet: DOS Problem 1.13

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: a separate later paper explicitly answers Problem 1.13 of
arXiv:math/0508650. This packet records literature status only; it is not an
original proof from the run.

## Original Problem Source

- S. J. Dilworth, E. Odell, B. Sari, *Lattice structures and spreading
  models*, arXiv:math/0508650.
- Local source lines inspected: `data/parsed/arxiv_sources/0508650/source.tex`,
  lines 399--404.
- Local PDF: `source_paper.pdf`, if download succeeds.

Problem 1.13 asks whether, if `SP_w(X)` is uncountable, there must be an
`omega_1`-indexed family of weakly-null spreading models that is either
strictly increasing, strictly decreasing, or pairwise incomparable in the
domination order.

## Supporting Answer Source

- Pandelis Dodos, *On antichains of spreading models of Banach spaces*,
  arXiv:0805.2038.
- Local source lines inspected: `data/parsed/arxiv_sources/0805.2038/source.tex`,
  lines 59--66 and 84--129.
- Local PDF: `supporting_paper_0805.2038.pdf`, if download succeeds.

## Status Match

Dodos explicitly says that the paper is motivated by the problem posed in
`[DOS, Problem 1.13]`. The abstract states the dichotomy: for every separable
Banach space `X`, either `SP_w(X)` is countable or `SP_w(X)` contains an
antichain of cardinality continuum, and says this answers a question of
Dilworth, Odell, and Sari. Theorem 1 constructs continuum many branches whose
generated spreading models are mutually incomparable, and Corollary 1 states
that uncountable `SP_w(X)` contains an antichain of size continuum.

Thus Problem 1.13 has a positive answer, indeed through the third alternative
of the requested trichotomy: there is an `omega_1`-sized mutually incomparable
subfamily, since continuum has cardinality at least `omega_1`.

## Scope Limitations

This packet clears only Problem 1.13 of arXiv:math/0508650. It does not answer
Problem 1.6 on countable weakly-null spreading models in reflexive spaces, nor
the later set-theoretic semilattice Problem 1.14.

## Verification Notes

- Same-paper check: the source paper asks Problem 1.13 and does not answer it
  there.
- Separate-source check: arXiv:0805.2038 is a distinct later paper and
  explicitly cites `[DOS, Problem 1.13]`.
- Local duplicate check: the run indexes had no exact entry for arXiv:math/0508650
  or this Problem 1.13 status packet before creation.
- Literature evidence: local parsed sources for arXiv:0805.2038 and a later
  remark in arXiv:2112.09602 both point to the continuum-antichain theorem.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source, if available.
- `supporting_paper_0805.2038.pdf`: decisive supporting answer source, if
  available.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:math/0508650 Problem 1.13 asks for an uncountable monotone or
   incomparable family when `SP_w(X)` is uncountable.
2. arXiv:0805.2038 cites `[DOS, Problem 1.13]`.
3. arXiv:0805.2038 Corollary 1 gives a continuum-sized antichain, which
   directly supplies the mutually incomparable alternative.
