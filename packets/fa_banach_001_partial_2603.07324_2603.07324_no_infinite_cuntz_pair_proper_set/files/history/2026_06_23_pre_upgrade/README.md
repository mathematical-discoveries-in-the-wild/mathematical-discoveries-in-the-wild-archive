# No Infinite Cuntz-Pair Proper-Set Swindle

Status: candidate partial / route no-go

Source: arXiv:2603.07324, Question 2.15 asks whether there is a square stable
Banach space failing to be hyperplane stable.

## Result

Inside the ordinary Gowers--Maurey proper-set-of-spreads framework, a proper
set cannot contain countably many exact binary Cuntz pairs.  In fact, it can
contain only finitely many.

This rules out the previously isolated "fresh commuting Cuntz pair" strategy:
one cannot solve Question 2.15 by building a proper set of spreads with an
infinite reserve of exact binary decompositions and then applying the
finite-algebra Fredholm-index swindle.

## Why the proof is short

For an exact binary pair, the range projections of the two isometries are
spreads in the same proper set and form a binary partition of the basis
indices.  If there were infinitely many such partitions, then among any three
fixed indices some fixed pair of indices would lie in the same side for
infinitely many partitions.  The corresponding infinitely many coordinate
projections would all have nonzero entries at the same two distinct diagonal
matrix positions, contradicting properness.

## Limitation

This is not a full solution or counterexample for Question 2.15.  It only
eliminates one natural upgrade of the binary modified Gowers--Maurey tree
construction.  The source question remains open in this packet.

## Files

- `main.tex`: formal proof packet.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: cached source paper.
- `figures/source_question_page_15.png`: rendered source page containing
  Question 2.15.
