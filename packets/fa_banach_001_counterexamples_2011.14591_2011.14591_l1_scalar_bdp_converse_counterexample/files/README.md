# Counterexample: the BDP converse for Lebesgue-Bochner spaces fails at p=1

Status: `candidate_counterexample_likely_valid_needs_human_review`

Source paper: arXiv:2011.14591, Sudeshna Basu and Susmita Seal, *Stability
results of small diameter properties in Banach spaces*.

## Claim

The converse of Proposition `bochner bdp` in the source is false in general.
Take `X = R`, `p = 1`, and Lebesgue measure on `[0,1]`. Then `X` has BDP, but
`L^1([0,1], X) = L^1[0,1]` does not have BDP.

The same source remark already notes that the converse of Proposition
`bochner bhp` fails for this example, since `R` has BHP but `L^1[0,1]` does
not. Thus both converse questions in the remark have negative answers in the
unrestricted “in general” sense.

## Key mechanism

Finite-dimensional spaces have BDP. On the other hand, every slice of the unit
ball of non-atomic scalar `L^1` has diameter two: choose two disjoint subsets
where the defining `L^\infty` functional is almost norm-attaining, and put
opposite unit masses on them.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper.
- `figures/open_problem_crop.png` - page 12 crop containing the source remark.
- `history/` - triage notes, archived claim state, and search provenance.

## Scope

This closes the general BDP converse question by a p=1 counterexample and
records the source's p=1 BHP counterexample. It does not settle positive
stability for `1 < p < infinity`, atomic measure spaces, or the later
Kothe-Bochner BSCSP question in arXiv:2307.03631.

## Novelty check

Local run indexes were searched for `2011.14591`, `BDP`, `BHP`,
`Lebesgue-Bochner`, `L^p(mu,X)`, and `converse`; no existing packet for this
specific BDP-converse counterexample was found. Local arXiv sources show the
same source remark and the later arXiv:2307.03631 Kothe-Bochner paper, which
leaves the BSCSP analogue open but does not record this BDP consequence.
Web searches for exact phrases around the source remark and close variants
returned the source paper and the 2023 sequel, but no separate explicit answer
to the BDP converse.

## History

No earlier partial packet existed for this exact result. The history folder
records the lane-17 triage: the original extraction signal was the source's
general converse remark; the 2023 sequel was checked and found to leave a
different BSCSP question open; the final promotion is the p=1 scalar BDP
counterexample above.
