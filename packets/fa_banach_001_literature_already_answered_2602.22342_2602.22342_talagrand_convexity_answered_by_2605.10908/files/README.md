# Talagrand convexity and subgaussian-vector problems answered by arXiv:2605.10908

Status: `literature_already_answered`

## Source questions

Antoine Song, *Sum of Gaussian vectors and large sets*, arXiv:2602.22342.

- Problem 0.1 on arXiv PDF page 1 asks for a universal number of Minkowski
  summands that forces every Gaussian-large closed set to contain a
  Gaussian-large convex body.
- Problem 0.2 on the same page asks whether every centered 1-subgaussian
  vector in every dimension is a sum of a universal number of standard
  Gaussian vectors.
- Theorem 0.3 on page 2 states that the two problems are equivalent.

The source PDF is the current v2.  Its page 2 `Added May 2026` note itself
points to the subsequent answer.

## Explicit later answer

Dongming (Merrick) Hua, Antoine Song, and Stefan Tudose, *On Talagrand's
Convexity Conjecture*, arXiv:2605.10908.

The separate later paper explicitly cites arXiv:2602.22342 and says that it
resolves the subgaussian-vector problem and hence Talagrand's convexity
problem.  On arXiv PDF page 2:

- Theorem 1.1 proves that every random vector dominated in convex order by a
  standard Gaussian is a sum of three standard Gaussian vectors.
- Corollary 1.2 combines this with the universal convex-order domination of
  centered 1-subgaussian vectors (after scaling).
- The paragraph after Corollary 1.2 obtains a universal finite number of
  standard Gaussian summands, exactly answering Problem 0.2.
- Corollary 1.3 and the equivalence from the source then settle Problem 0.1.

This is an author-explicit full literature answer, not a new proof produced by
the run.  The supporting paper notes that a constructive version remains open;
that is a different question.

Files:

- `source_paper.pdf`: arXiv:2602.22342v2.
- `supporting_paper_2605.10908.pdf`: arXiv:2605.10908v2.
- `main.tex`, `solution_packet.pdf`: compact literature-status note.

Ledger record:
`runs/fa_banach_001/ledger/results/2602.22342_talagrand_convexity_answered_by_2605.10908.json`.
