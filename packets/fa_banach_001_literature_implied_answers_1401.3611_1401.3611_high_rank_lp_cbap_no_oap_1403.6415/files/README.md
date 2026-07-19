# Literature-Implied Partial Answer: High-Rank CBAP/OAP Endpoint

Status: `literature_implied_answer (partial high-rank subcase)`

Source paper: Tim de Laat and Mikael de la Salle, *Strong property (T) for higher rank simple Lie groups*, arXiv:1401.3611.

Supporting paper: Tim de Laat and Mikael de la Salle, *Approximation properties for noncommutative Lp-spaces of high rank lattices and nonembeddability of expanders*, arXiv:1403.6415.

## Identification

In the introduction of arXiv:1401.3611, de Laat--de la Salle note that their
estimates improve the known failure of CBAP/OAP for noncommutative
`L^p(L(Gamma))` spaces attached to lattices in connected higher-rank simple Lie
groups from the range
`[1,12/11) union (12,infty]` to `[1,10/9) union (10,infty]`. They ask whether
this failure can be extended to all `p != 2`.

The later arXiv:1403.6415 does not settle the fixed low-rank case, but it gives
a strong high-rank partial answer. Its Theorem 1.1 proves that if `n >= 3` and
`r >= 2n-3`, then `L^p(L(SL(r,Z)))` fails CBAP for
`p in [1,2-2/n) union (2+2/(n-2),infty]`; the paper also states that the same
argument gives failure of OAP. Its Theorem 1.3 gives the corresponding
statement for lattices in connected simple real Lie groups of sufficiently high
real rank.

Consequently, for every fixed `p != 2`, choosing `n` large enough places `p`
in the above interval, so sufficiently high rank lattices have
`L^p(L(Gamma))` without CBAP and without OAP. This directly addresses the
`p != 2` endpoint direction in the high-rank-as-rank-varies regime.

## Scope

This is not a new proof from the run. It is a literature-implied partial
answer to one signal in arXiv:1401.3611. The broad fixed-lattice problem
remains open, especially the essential question recorded in arXiv:1403.6415:
whether `L^p(L(SL(3,Z)))` has CBAP for some `p != 2`.

The other source signal about whether the classes `E_r` contain all Banach
spaces of nontrivial type is not resolved by this packet.

## Files

- `source_paper.pdf`: arXiv:1401.3611.
- `supporting_paper_1403.6415.pdf`: arXiv:1403.6415.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered packet note.

## Search Notes

The cheap run indexes had no exact `1401.3611` packet. They did have nearby
memory for the BFGM higher-rank fixed-point conjecture, already answered by
arXiv:2303.01405, so that signal was not duplicated. Web/arXiv search for the
CBAP/OAP endpoint found arXiv:1403.6415, whose abstract and Theorems 1.1/1.3
give the high-rank partial answer above.
