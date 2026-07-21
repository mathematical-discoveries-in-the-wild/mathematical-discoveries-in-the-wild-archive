# Partial result: weak-star angelic preduals

## Status

`partial_result_likely_valid`

Source paper: Gin\u00e9s L\u00f3pez-P\u00e9rez and Jos\u00e9 A. Soler-Arias,
*Weak-star point of continuity property and Schauder bases*,
arXiv:1309.3862, Studia Mathematica 219 (2013), 225-236.

## Result

The source proves that weak-star PCP is determined by subspaces with a
Schauder basis when the ambient dual has a **separable predual**. This packet
replaces separability by the strictly broader topological hypothesis that the
predual has a weak-star Fr\u00e9chet-Urysohn dual ball (also called a weak-star
angelic dual).

Precisely, if \((B_{Y^*},w^*)\) is Fr\u00e9chet-Urysohn and \(X\) is a norm-closed
subspace of \(Y^*\), then
\[
X\text{ has }w^*\text{-PCP}
\quad\Longleftrightarrow\quad
\text{every closed subspace of }X\text{ with a Schauder basis has }w^*\text{-PCP}.
\]
In particular, this holds for every weakly Lindel\u00f6f determined (WLD)
predual \(Y\), and hence for every weakly compactly generated predual.

The proof also extends the source's closed-bounded-set tree characterization:
failure of weak-star PCP is equivalent to the existence of a seminormalized
**weak-star-null** tree whose branchwise partial sums stay in the set.

## Proof mechanism

Weak-star Fr\u00e9chet-Urysohn compactness turns each closure witness in a
nonfragmented set into a convergent sequence, producing an actual weak-star
null tree rather than only a topologically weak-star-null tree. A separate
finite-codimensional perturbation lemma extracts a full subtree which is a
Schauder basic sequence. Its branchwise partial sums remain bounded, forcing
the generated basis subspace to fail weak-star PCP.

## Scope

This is a substantial partial result, not a solution of Bourgain's unrestricted
question asking whether intrinsic PCP or RNP is determined by subspaces with a
Schauder basis. It also does not cover preduals whose weak-star dual ball is
non-Fr\u00e9chet or merely sequential of higher sequential order. That
nonsequential closure obstruction is exactly where the construction stops.

## Files

- `main.tex` - theorem and proof.
- `solution_packet.pdf` - rendered proof packet.
- `source_paper.pdf` - local copy of arXiv:1309.3862.
- `supporting_paper_1612.05948.pdf` - background source for weak-star angelic
  dual balls and the inclusion of WLD spaces.
- `figures/open_problem_crop.png` - source-paper crop of the open-problem
  passage.
- `verification.md` - proof and artifact audit.

## Novelty check

The run indexes were searched for arXiv:1309.3862 and the core phrases
`topologically weak-star null`, `weak-star PCP`, `WLD`, `weak-star angelic`,
and `determined by subspaces with a Schauder basis`. Bounded web/arXiv searches
used the exact open-problem wording and close variants combining those terms.
They found the 2013 source, its 2011/2012 tree precursor, and later work on
weak-star sequential and Fr\u00e9chet-Urysohn dual balls, but no explicit statement
of this WLD/weak-star-angelic extension. Novelty confidence is therefore
moderate, while the mathematical-validity claim is independent of novelty.

