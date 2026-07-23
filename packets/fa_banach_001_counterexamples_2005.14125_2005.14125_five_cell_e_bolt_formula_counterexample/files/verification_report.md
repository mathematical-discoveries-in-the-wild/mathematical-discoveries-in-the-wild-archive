# Verification report

## Verdict

candidate_counterexample_likely_valid

The packet gives an exact literal counterexample to Theorem 3.8. It also
gives a counterexample to the subsequent conjecture when the source's own
statement that the theorem's three bolts are exactly the e-bolts is used.

## Source audit

- Source checked: arXiv:2005.14125, article pages 139--141.
- The definition of M(H) on article page 133 requires nonnegative mixed
  increment for every rectangle contained in H.
- Theorem 3.8 on article page 140 asserts a maximum over exactly r, r12,
  and r13 for the five-cell U-shaped polygon.
- Definition 3.2 is on article pages 140--141.
- The paragraph following Definition 3.2 explicitly says that the polygon
  of Theorem 3.8 has three e-bolts: r, r12, and r13.
- The conjecture immediately following that paragraph asserts the maximum
  over all e-bolts for every axis-parallel polygon and every f in M(S).

## Proof audit

1. The polygon Q is exactly Theorem 3.8 with parameters
   a = (0,1,2,3) and b = (0,1,2).
2. The displayed f is continuous and piecewise bilinear on the bounding
   rectangle.
3. Its mixed density is +1 on (0,1) x (0,1), -1 on the missing cell
   (1,2) x (1,2), and zero elsewhere.
4. A rectangle contained as a set in Q has interior disjoint from the
   missing cell. Its mixed increment is therefore the nonnegative area of
   its intersection with the positive cell. Hence f is in M(Q).
5. Exact vertex substitution gives l(f,r)=0,
   l(f,r12)=l(f,r13)=1/6.
6. The lower-left unit-square bolt q lies in Q and has l(f,q)=1/4.
7. Every closed-bolt functional annihilates phi(x)+psi(y), and its
   normalized coefficient absolute values sum to one. Therefore
   |l(f,q)| is at most the uniform approximation error of every such sum.
8. Thus E(f,Q) is at least 1/4, strictly larger than the 1/6 asserted in
   Theorem 3.8.

## Computational check

The exact checker uses fractions, not floating point. It verifies the four
displayed bolt values and tests all rational-grid rectangles of mesh 1/8
contained in Q. The grid test is a sanity check only; the density calculation
in the proof handles every real rectangle.

Command:

python code/check_five_cell_counterexample.py

## Convention and scope audit

- The result is literal: rectangle containment means the whole rectangle is
  a subset of Q.
- If the intended class required the inequality whenever all four vertices
  lie in Q, the missing-cell rectangle would violate that stronger property.
- No such stronger condition appears in the printed definition.
- The theorem counterexample does not depend on interpreting the general
  e-bolt containment relation.
- The conjecture corollary uses the source's explicit three-e-bolt
  enumeration. A reviewer should audit this point separately because the
  general definition's geometric conventions are terse.

## Literature check

Cheap indexes and bounded exact-phrase web searches on 2026-07-22 found the
2006 source paper, the 2020 notes, and bibliographic mirrors, but no proof,
counterexample, correction, or later discussion of this obstruction. Search
terms included the arXiv id, both source titles, author, Theorem 3.8,
e-bolts, extended bolt, Conjecture 3.4, counterexample, and polygon.
Novelty confidence is moderate pending specialist or author review.

