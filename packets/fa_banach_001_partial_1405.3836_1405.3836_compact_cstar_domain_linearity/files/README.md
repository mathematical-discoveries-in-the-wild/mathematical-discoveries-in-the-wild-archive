# Partial Result: Compact C*-Algebra Domains

Source: M. J. Burgos, F. J. Fernandez-Polo, J. J. Garces, and
A. M. Peralta, *2-local triple homomorphisms on von Neumann algebras and
JBW*-triples*, arXiv:1405.3836; J. Math. Anal. Appl. 426 (2015), 43-63.

Result type: `partial`

Status: likely valid, new deduction relative to the source paper, pending
human review.

## Source Question

Problem 1.1 asks whether every 2-local triple homomorphism between C*-algebras
is automatically linear. Problem 1.2 asks the analogous question for
JB*-triples. The source paper proves this when the domain is a von Neumann
algebra or, more generally, a JBW*-triple.

## New Subcase

Let

```text
A = c0-direct-sum_i K(H_i)
```

be a compact C*-algebra, and let `F` be any JB*-triple. Every 2-local triple
homomorphism `T:A -> F` is linear and hence a triple homomorphism.

This goes beyond the source theorem because infinite-dimensional `K(H)` is
not a dual Banach space and therefore is not a JBW*-triple.

The proof first handles `K(H)`. For fixed unit vectors, the rank-one column
and row spaces are Hilbertian JBW*-subtriples, so the source theorem forces
the restriction of `T` to each row and column to be linear. After composing
with a functional on the range, this produces a bounded sesquilinear form on
rank-one tensors. Singular-value decompositions and the source paper's
finite-orthogonal-tripotent lemma show that the induced algebraic functional
is bounded in operator norm, hence extends linearly to all of `K(H)`. Range
functionals separate points, so `T` is linear. Norm approximation then joins
the elementary summands in a `c0`-sum.

## Files

- `main.tex`: complete proof and verification notes.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: local copy of arXiv:1405.3836.
- `figures/open_problem_crop.png`: source-page crop containing Problem 1.1
  and adjacent scope context.
- `tmp/`: LaTeX intermediates and rendered QA pages.

## Scope and Novelty

The result settles neither Problem 1.1 for arbitrary C*-algebras nor Problem
1.2 for arbitrary JB*-triples. Exact-phrase searches in the run's parsed arXiv
corpus and bounded web/arXiv searches for combinations of "2-local triple
homomorphism", "compact C*-algebra", and `K(H)` found the source paper and
citation records, but no statement of this compact-domain extension. Novelty
confidence is moderate, not definitive.

## Human Review

Recommended checks:

1. verify that restriction to every rank-one row and column is a 2-local
   triple homomorphism on a Hilbertian JBW*-triple;
2. verify well-definedness and operator-norm boundedness of the functional
   induced by the resulting sesquilinear form;
3. verify the passage from elementary summands to an arbitrary `c0`-sum.
