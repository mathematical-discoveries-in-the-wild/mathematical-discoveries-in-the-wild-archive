# Five-cell counterexample to the e-bolt error formula

Status: candidate_counterexample_likely_valid

Source: Vugar E. Ismailov, Notes on ridge functions and neural networks,
arXiv:2005.14125, Theorem 3.8 and the e-bolt conjecture on article pages
140--141. The theorem first appeared in the 2006 paper On error formulas for
approximation by sums of univariate functions.

## Result

Theorem 3.8 is false under the printed definition of M(Q), and the same
example refutes the following e-bolt conjecture under the source's explicit
enumeration of the e-bolts.

Take the five-cell U-shaped polygon

Q = ([0,3] x [0,1]) union ([0,1] x [1,2]) union ([2,3] x [1,2])

and restrict to Q the continuous piecewise-bilinear function

f(x,y) = min(x,1) min(y,1)
         - min((x-1)_+,1) (y-1)_+.

Its mixed density is +1 on the occupied lower-left unit cell, -1 on the
missing top-middle unit cell, and zero elsewhere. Every rectangle contained
in Q avoids the negative cell, so f belongs to M(Q).

The three bolts printed in Theorem 3.8 have absolute values 0, 1/6, and 1/6.
The lower-left unit-square bolt has value 1/4 and annihilates every
approximant phi(x)+psi(y). Therefore E(f,Q) is at least 1/4, contradicting
the theorem's asserted value 1/6.

The paragraph after Definition 3.2 says the polygon in Theorem 3.8 has
exactly those three e-bolts. With that source enumeration, the same strict
inequality refutes the conjectured formula.

## Files

- main.tex and solution_packet.pdf: self-contained proof and review packet.
- source_paper.pdf: the arXiv source notes.
- figures/: source-page crops showing Theorem 3.8, Definition 3.2, the
  e-bolt enumeration, and the conjecture.
- code/check_five_cell_counterexample.py: exact rational arithmetic checker.
- code/crop_open_problem.py: reproducible crop script.
- verification_report.md: source, proof, scope, and novelty audit.

## Convention warning

The proof uses the source's literal condition: the whole axis-parallel
rectangle is contained in Q. If the author intended the stronger condition
that the mixed increment be nonnegative whenever merely the four vertices
belong to Q, the witness is excluded by the missing cell. That stronger
condition is not the printed definition.

The counterexample to Theorem 3.8 is independent of the general e-bolt
definition because the theorem explicitly lists its three functionals. The
conjecture corollary additionally uses the source's sentence that the same
three bolts are all the e-bolts of this polygon.

## Novelty check

Cheap run indexes and bounded web searches on 2026-07-22 used arXiv:2005.14125,
the 2006 article title, Ismailov, Theorem 3.8, e-bolts, extended bolts,
Conjecture 3.4, counterexample, and polygon. They found the source article,
the notes, and bibliographic mirrors, but no later resolution or discussion
of this construction. Novelty confidence is moderate pending specialist or
author review.

## Human review

Recommended verdict: likely valid literal counterexample. Check first the
printed definition of M(Q), the three alternating sums, and the standard
closed-bolt lower bound. Then audit the source's exact e-bolt enumeration for
the conjecture corollary.

