# Literature-Already-Answered Packet: Asymptotically Symmetric Spaces

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an exact later-literature negative answer to Problem 2
from Junge--Kutzarova--Odell, not a new construction from this run.

## Source Problem

- M. Junge, D. Kutzarova, E. Odell, *On Asymptotically Symmetric Banach
  Spaces*, arXiv:math/0508035.
- Local source inspected: `data/parsed/arxiv_sources/0508035/source.tex`.
- Problem location: `source.tex`, lines 143--148.

Problem 2 asks whether every infinite-dimensional asymptotically symmetric
Banach space contains an asymptotic `ell_p` subspace for some `p`.

## Supporting Literature

- D. Kutzarova, P. Motakis, *Asymptotically symmetric spaces with hereditarily
  non-unique spreading models*, arXiv:1902.10098.
- Local source inspected: `data/parsed/arxiv_sources/1902.10098/source.tex`.

The supporting paper explicitly cites the JKO problem in the form: does every
asymptotically symmetric Banach space contain an infinite-dimensional
asymptotic-`ell_p` or asymptotic-`c_0` subspace? It then constructs a reflexive
space `X = mathfrak{X}^{1/2}_{0,1}` which is asymptotically symmetric and has no
asymptotic-`ell_p` or asymptotic-`c_0` subspace.

## Literature Answer

The answer to JKO Problem 2 is negative.

The space `mathfrak{X}^{1/2}_{0,1}` from arXiv:1902.10098 is an
infinite-dimensional asymptotically symmetric Banach space. The same paper
states that it does not contain a subspace that is asymptotic-`ell_p` or
asymptotic-`c_0`. In particular, it contains no asymptotic-`ell_p` subspace for
any finite `p`, which refutes the original 2005 problem.

## Evidence Chain

- arXiv:0508035, Problem 2: asks for an asymptotic `ell_p` subspace in every
  infinite-dimensional asymptotically symmetric Banach space.
- arXiv:1902.10098, introduction: formulates the JKO problem with the slightly
  stronger `ell_p` or `c_0` alternative and says it is solved in the negative
  direction by a variation of `mathfrak{X}_{0,1}`.
- arXiv:1902.10098, Section 3: proves every block subspace has both `ell_1` and
  `c_0` spreading models, while an asymptotic-`ell_p` or asymptotic-`c_0` space
  would force all weakly-null spreading models to be of the corresponding
  single type.
- arXiv:1902.10098, conclusion: proves `mathfrak{X}^{1/2}_{0,1}` is
  asymptotically symmetric.

## Duplicate And Viability Checks

Before promotion, the run lightweight indexes were searched for
`0508035`, `asymptotically symmetric`, `asymptotic symmetry`,
`spreading model`, `Junge`, `Kutzarova`, `Odell`, and related phrases.
No exact existing packet, attempt, or proof gap for arXiv:0508035 was found.
The only cheap-index hit was a distant spreading-model row for another paper.

Active claims were inspected by slug. No other active claim appeared to target
JKO Problem 2 or the Kutzarova--Motakis counterexample.

## Limitations

- This packet records a literature status, not a new proof from the run.
- It answers Problem 2 from arXiv:0508035. It does not address Problem 1 on
  subspaces of noncommutative `L_p` spaces.
- It does not answer the further modified question at the end of
  arXiv:1902.10098 asking whether every asymptotically symmetric space admits
  an `ell_p` or `c_0` spreading model.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status packet source.
- `solution_packet.pdf`: rendered packet, if the local LaTeX build succeeds.
- `source_paper.pdf`: compiled local source for arXiv:0508035, if available.
- `supporting_paper_1902.10098.pdf`: compiled local source for arXiv:1902.10098,
  if available.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Treat arXiv:0508035 Problem 2 as already answered negatively by
arXiv:1902.10098. Keep the status as literature-resolved, not as an original
agent proof.
