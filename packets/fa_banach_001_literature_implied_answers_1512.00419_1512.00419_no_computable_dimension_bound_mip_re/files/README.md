# Literature-Implied Answer: No Computable Uniform Dimension Bound

Status: `literature_implied_answer (Open Problem 5.3, computable-bound obstruction)`

Source question: Carlos Palazuelos and Thomas Vidick, *Survey on Nonlocal
Games and Operator Space Theory*, arXiv:1512.00419.  Section 5.4.1, Open
Problem 5.3 asks for an explicit bound `d(epsilon,n)` such that every game
with at most `n` questions and answers per player has a `d`-dimensional
strategy with success probability at least `omega^*(G)-epsilon`.

## Answer

No computable bound of this uniform kind can exist.

More precisely, there is no total computable function `D(epsilon,n)` on
positive rational `epsilon` and natural `n` such that for every finite
two-player nonlocal game with at most `n` questions and answers per player
there is a strategy of local dimension at most `D(epsilon,n)` achieving
success probability at least `omega^*(G)-epsilon`.

This does not contradict the compactness statement in the source paper:
for each fixed `epsilon,n` some finite bound exists.  The point is that the
bound cannot be made algorithmically explicit/computable.

## Literature Input

Ji--Natarajan--Vidick--Wright--Yuen, *MIP* = RE*, arXiv:2001.04383, state in
their abstract that there is an efficient reduction from the Halting Problem
to deciding whether a two-player nonlocal game has entangled value `1` or at
most `1/2`.

## Proof Summary

Assume a computable uniform dimension bound `D` existed.  Given a game `G`
from the MIP* = RE reduction, let `n` bound its question and answer sets and
put `d = D(1/6,n)`.

If `omega^*(G)=1`, the bound gives a dimension-`d` strategy with value at
least `5/6`.  If `omega^*(G)<=1/2`, every finite-dimensional strategy has
value at most `1/2`.

For fixed `G` and fixed `d`, the value restricted to `d`-dimensional
strategies is a compact real semialgebraic optimization problem: the variables
are a finite-dimensional state and finitely many POVM matrices, and the payoff
is polynomial in their real and imaginary parts.  Hence it can be approximated
effectively enough to distinguish `>=5/6` from `<=1/2`.  This would decide the
Halting Problem, contradicting MIP* = RE.

## Scope

- This packet records a literature-implied obstruction to an explicit
  computable version of Open Problem 5.3.
- It does not deny the non-effective compactness existence of a finite
  `d(epsilon,n)` for each fixed `epsilon,n`.
- It is separate from the existing packet for Open Problem 5.2, which records
  finite games whose optimal value is achieved only in the infinite-dimensional
  limit.

## Files

- `main.tex`: compact proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: Palazuelos--Vidick source survey.
- `supporting_paper_2001.04383.pdf`: MIP* = RE source.
