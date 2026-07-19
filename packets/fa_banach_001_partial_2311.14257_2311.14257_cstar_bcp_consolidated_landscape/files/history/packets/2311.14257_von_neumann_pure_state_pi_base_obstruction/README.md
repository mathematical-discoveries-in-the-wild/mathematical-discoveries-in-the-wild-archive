# Von Neumann Negative Cases Have No Pure-State Countable Pi-Base

Status: likely valid partial result for the arXiv:2311.14257 C*-algebra BCP
classification program.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
C*-algebra version of the commutative `C(K)` BCP/UBCP criterion.

## Main Result

Let `M` be a von Neumann algebra. If the pure state space `P(M)` has a
countable pi-base in the weak-star topology inherited from `M*`, then `M` is
atomic and separably represented. Hence, by the source paper's von Neumann
classification, `M` has BCP and UBCP.

Equivalently, every von Neumann algebra failing BCP in the source theorem has
pure state space with no countable pi-base.

## Proof Idea

There are two obstructions.

For an atomless von Neumann algebra, every pure state is singular. Given
countably many proposed pure-state open sets, choose a pure state from each.
A standard singular-state projection lemma gives a nonzero projection `p`
annihilating all chosen states. The pure-state open set `{psi: psi(p)>1/2}`
is nonempty, but none of the proposed open sets is contained in it.

For an atomic nonseparably represented algebra, either there are uncountably
many atomic summands, giving uncountably many disjoint pure-state open sets,
or one summand is `B(H)` for nonseparable `H`, where uncountably many
orthogonal rank-one projections give uncountably many disjoint pure-state
open sets.

## Meaning

This does not solve the arbitrary C*-case, but it is an important stress-test:
the pure-state pi-base idea is compatible with the source's von Neumann
negative theorem in the necessary direction.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Check the singular-state common projection lemma, the extension of pure states
from `pMp` to `M`, and the uncountable disjoint-open-family arguments in the
atomic nonseparable cases.
