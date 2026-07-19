# Literature-implied answer: Banach-space Markov-to-fork subcase

- run: `fa_banach_001`
- agent_id: `agent_lane_11`
- date: 2026-06-15
- status: `literature_implied_answer (Banach-space subcase)`
- source arXiv id: `2103.16011`
- source paper: Florent P. Baudier and Chris Gartland, "Umbel convexity and the geometry of trees"
- supporting arXiv id: `0803.1697`
- supporting paper: Manor Mendel and Assaf Naor, "Markov convexity and local rigidity of distorted metrics"
- packet slug: `2103.16011_banach_markov_fork_subcase_0803_1697`

## Source question

In Section 6, Problem `pb:markov->fork`, Baudier--Gartland ask:

```text
Does Markov p-convexity imply fork p-convexity?
```

The surrounding paragraph explains the obstruction in the general metric-space
case: Markov convexity averages over all tree levels, whereas fork convexity
uses dyadic-level maxima/minima.

## Identification

For Banach spaces in the usual renorming range `p >= 2`, the answer is yes.
Mendel--Naor's Theorem 1.3 says that a Banach space is Markov `p`-convex if
and only if it admits an equivalent norm whose modulus of uniform convexity has
power type `p`. Baudier--Gartland recall this as Theorem `thm:MN-LNP`.

Baudier--Gartland also recall the `p`-fork point inequality and note, citing
Mendel--Naor Lemma 2.3, that a `p`-uniformly convex Banach norm satisfies the
`p`-fork inequality. Their Theorem `thm:fork` then gives fork `p`-convexity
from the relaxed fork inequality; the full `p`-fork inequality implies that
relaxed form. Since fork `p`-convexity is stable under bi-Lipschitz change of
metric, the original Banach-space norm is fork `p`-convex.

## Scope

This is not a solution of Problem `pb:markov->fork` for arbitrary metric
spaces. It records only the Banach-space subcase `p >= 2`.

The supporting authors did not explicitly answer Baudier--Gartland's later
Problem `pb:markov->fork`; the relation is an agent-identified implication
from their renorming theorem and the fork-inequality facts cited in the source
paper.

## Files

- `source_paper.pdf`: source/open-problem paper, arXiv:2103.16011.
- `supporting_paper_0803.1697.pdf`: Mendel--Naor supporting paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered compact status note.

## Ledger

Ledger record:
`runs/fa_banach_001/ledger/results/2103.16011_banach_markov_fork_subcase_0803_1697.json`

