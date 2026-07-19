# Candidate Full Solution: Tandori Weakly Compact Multipliers

Run: `fa_banach_001`

Source paper: Tomasz Kiwerski and Jakub Tomaszewski, "Essential norms of
pointwise multipliers in the non-algebraic setting", arXiv:2212.06723.

Target: Problem 7.5, asking what can be said about weakly compact and compact
multipliers between abstract Tandori function spaces.

Status: candidate full solution, likely valid pending human review.

## Claim

For `I=(0,1)` or `I=(0,infinity)` with Lebesgue measure and Kothe function
spaces `X,Y`, every bounded multiplication operator

```text
M_lambda : \widetilde X -> \widetilde Y
```

has

```text
dist(M_lambda, weakly compact operators)
= dist(M_lambda, compact operators)
= ||M_lambda||.
```

Consequently `M_lambda` is weakly compact iff compact iff zero iff
`lambda=0` almost everywhere. In fact every nonzero multiplier fixes an
isometric copy of `ell_infinity` and is not strictly singular.

## Packet Files

- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of Problem 7.5.
- `main.tex`: consolidated proof packet.
- `solution_packet.pdf`: rendered packet.
- `evidence/2026-06-21_tandori_compact_multipliers_full/`: supplied TeX/PDF report.
- `history/packets/partial_packet_2212.06723_compact_multipliers_zero_2026_06_14/`: earlier compact-only partial packet, now absorbed as history.

## Human Review Recommendation

Review the tail-preserving disjointization lemma, the exact least-decreasing
majorant identities for the adapted `ell_infinity` copy, and the source
paper's conventions on Kothe function spaces and indicator functions. The
novelty check relies on the supplied report's June 21, 2026 search and should
be independently checked against the 2026 published version and later
multiplier papers.
