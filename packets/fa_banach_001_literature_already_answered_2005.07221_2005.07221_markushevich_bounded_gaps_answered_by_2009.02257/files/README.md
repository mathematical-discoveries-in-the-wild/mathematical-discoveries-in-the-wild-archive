# Literature Answer: Bounded-Gap Quasi-Greediness for Markushevich Bases

Status: `literature_already_answered`.

## Original Question

Miguel Berasategui and Pablo M. Berná, *Quasi-greedy bases for sequences
with gaps*, arXiv:2005.07221; Nonlinear Analysis 208 (2021), 112294.

The source proves Theorem 5.2 under the assumption that the biorthogonal
system is a Schauder basis: if the index sequence has bounded quotient gaps,
then `n-t`-quasi-greediness implies ordinary quasi-greediness.  Its final
Question 1 asks whether the Schauder hypothesis can be removed and replaced
by the Markushevich-basis hypothesis.  The question is on page 17 of the
18-page arXiv PDF, Section 8 (“Open question”).

## Answer

Yes.  The same authors' later paper

Miguel Berasategui and Pablo M. Berná, *Greedy-like bases for sequences with
gaps*, arXiv:2009.02257; Banach Journal of Mathematical Analysis 18 (2024),
article 2,

states in Theorem 2.11 (page 8 of the arXiv PDF): if `n` has bounded quotient
gaps and `B` is an `n`-quasi-greedy Markushevich basis of a Banach space, then
`B` is quasi-greedy.  This directly removes the Schauder assumption.  It also
covers the source theorem's weak parameter `0<t<=1`, because every
`n-t`-quasi-greedy system is in particular `n`-quasi-greedy: every greedy set
is a `t`-greedy set.

The supporting authors explicitly identify their result as extending the
earlier Schauder-basis theorem to Markushevich bases and completing the open
question.  This is therefore an explicit later-literature answer, not an
agent-inferred theorem combination and not a new proof from this run.

## Scope

Theorem 2.11 fully answers the source's final Question 1 for bounded quotient
gaps.  It does not settle the different weak-parameter converse for arbitrary
gap sequences or the later paper's new questions about strong partial
greediness and non-total fundamental minimal systems.

## Evidence And Search

- Cheap run indexes were searched for both arXiv ids, the exact title,
  `n-quasi-greedy`, `Markushevich`, and `bounded quotient gaps`; no prior run
  packet was present.
- Exact-phrase and title searches found arXiv:2009.02257 and its 2024 journal
  publication.
- The source PDF's Question 1 and the supporting PDF's Theorem 2.11 were
  checked directly.

## Files

- `source_paper.pdf`: arXiv:2005.07221.
- `supporting_paper_2009.02257.pdf`: the explicit answer paper.
- `main.tex` and `solution_packet.pdf`: compact status note.
- Ledger: `runs/fa_banach_001/ledger/results/2005.07221_markushevich_bounded_gaps_answered_by_2009.02257.json`.

