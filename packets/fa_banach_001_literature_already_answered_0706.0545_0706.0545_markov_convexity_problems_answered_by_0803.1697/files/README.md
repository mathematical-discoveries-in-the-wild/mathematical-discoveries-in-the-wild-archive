# Literature Answer: Two Markov Convexity Problems Answered by Mendel-Naor

Status: `literature_already_answered`

Source problem paper: James R. Lee, Assaf Naor, and Yuval Peres, *Trees and Markov convexity*, arXiv:0706.0545.

Supporting answer paper: Manor Mendel and Assaf Naor, *Markov convexity and local rigidity of distorted metrics*, arXiv:0803.1697.

## Source Questions

In Section "Some open problems" of arXiv:0706.0545, Problems 1 and 2 ask two Markov-convexity questions.

Problem 1 asks about the relation between Banach-space Markov `p`-convexity and uniform `p`-convexity beyond the Banach-lattice case. The source proves that `p`-uniform convexity implies Markov `p`-convexity, and proves a converse only for Banach lattices up to every exponent `q>p`; it says the general Banach-space relation is unclear.

Problem 2 asks whether the tree result extends to arbitrary metric spaces: if a metric space is not Markov `p`-convex for any finite `p`, must it contain arbitrarily large complete binary trees with distortion arbitrarily close to `1`?

## Later Answer

Mendel--Naor arXiv:0803.1697 explicitly cites Lee--Naor--Peres arXiv:0706.0545 as `LNP-markov-convex`. On PDF page 3, it says that Lee--Naor--Peres asked whether the Banach converse is true and answers this positively: Theorem `convexity-coincide` states that a Banach space is `p`-convex if and only if it is Markov `p`-convex. The later renorming Theorem `renorming` gives the equivalent norm quantitatively.

On PDF page 4, the same supporting paper addresses the general-metric analogue behind Problem 2. It says that the question was asked in Lee--Naor--Peres and answers it negatively: Theorem `doubling` constructs a metric space that is not Markov `p`-convex for any finite `p`, while `c_X(B_n)` tends to infinity, indeed exponentially. Thus the space cannot contain arbitrarily large complete binary trees with distortion close to `1`.

## Scope

This packet records already-known literature answers to Problems 1 and 2 from the source paper. It does not claim a new proof. Problems 3 and 4 from the same source introduction are not resolved by this packet.

## Files

- `source_paper.pdf`: arXiv:0706.0545.
- `supporting_paper_0803.1697.pdf`: decisive later answer source.
- `main.tex`, `solution_packet.pdf`: compact status note.
- Ledger: `runs/fa_banach_001/ledger/results/0706.0545_markov_convexity_problems_answered_by_0803.1697.json`.
