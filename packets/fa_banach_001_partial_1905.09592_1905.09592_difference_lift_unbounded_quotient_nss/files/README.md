# Difference lifts give unbounded-quotient NSS Jamison sequences

Status: `partial_result_likely_valid`.

Source: Catalin Badea, Vincent Devinck, and Sophie Grivaux, *Escaping a
neighborhood along a prescribed sequence in Lie groups and Banach algebras*,
Canadian Mathematical Bulletin 63(3) (2020), 484--505, arXiv:1905.09592,
DOI: 10.4153/S0008439519000560.

## Source problems

Problem 2.6 asks whether every Jamison sequence is NSS for all Banach--Lie
groups.  Problem 2.8 asks the analogous question for groups with a minimal
metric.  Both occur on source PDF page 8; exact crops are stored in `figures/`.
The source's Theorem 2.9 answers both positively when the sequence has bounded
consecutive quotients.

## Partial result

Let `Q` and `M=(m_j)` be sequences of positive integers.  Suppose that for
every `j` there are `a_j,b_j in Q` with `m_j=a_j-b_j>0`.  For every class of
topological groups:

- if `M` is NSS for that class, then `Q` is NSS for that class;
- if `(M,epsilon)` is a Jamison pair, then `Q` has Jamison constant at least
  `epsilon/2`.

Indeed, if all `x^q`, `q in Q`, lie in a sufficiently small identity
neighborhood `U`, then
`x^{m_j}=(x^{b_j})^{-1}x^{a_j}` lies in `U^{-1}U`.  The scalar estimate is the
same triangle inequality on the unit circle.

## Explicit sequence beyond the source theorem

Set
\[
 A_j=2^{2^{j+1}},\qquad
 Q=\{1\}\cup\{A_j,A_j+2^j:j\ge0\},
\]
enumerated increasingly.  Then:

- `Q-Q` contains `(2^j)_{j>=0}`;
- `Q` is a Jamison sequence with Jamison constant at least `sqrt(3)/2`;
- the consecutive quotients of `Q` are unbounded;
- nevertheless, `Q` is NSS for every Banach--Lie group and every group with a
  minimal metric.

Thus the positive part of Problems 2.6 and 2.8 extends strictly beyond the
bounded-quotient family treated in source Theorem 2.9.

## Scope

This does not prove that every Jamison sequence has the NSS property.  It
proves the result for every sequence whose difference set contains a known NSS
sequence, and gives an explicit Jamison example with unbounded consecutive
quotients.

## Novelty check

The run's lightweight indexes contained no match for arXiv:1905.09592, either
problem, or the difference-set transfer.  Bounded searches on 2026-07-19 used
the exact problem wording and combinations of `Jamison sequence`, `NSS`,
`difference set`, `unbounded quotients`, `Banach-Lie`, and `minimal metric`.
They found the source and mirrors but no later resolution or exact statement
of this transfer.  The result is labeled likely valid, not
literature-certified novel.

## Human-review recommendation

Promote as a substantial partial result after checking the neighborhood
orientation in the transfer lemma and the indexing of the explicit sequence.
The core proof is elementary; its value is that it yields a genuinely new
unbounded-quotient class covered simultaneously by both source problems.

## Files

- `main.tex` and `solution_packet.pdf`: complete proof packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_2_6_crop.png` and
  `figures/open_problem_2_8_crop.png`: exact source evidence.
- `attempt_log.md`: full and failed routes tried.
- `verification_report.md`: adversarial proof audit.

