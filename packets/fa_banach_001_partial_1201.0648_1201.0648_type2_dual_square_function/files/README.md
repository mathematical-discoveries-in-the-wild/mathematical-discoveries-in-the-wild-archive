# Type-2 replacement for the lattice step in the local non-homogeneous Tb theorem

Status: `partial_result_likely_valid`.

Source: Tuomas P. Hyt\"onen and Antti V. V\"ah\"akangas, "The local non-homogeneous Tb theorem for vector-valued functions", arXiv:1201.0648.

## Result

The source proves the randomized adjoint adapted martingale estimate

\[
  \left\|\sum_{k\in\mathbb Z}\varepsilon_k (D_k^a)^*f\right\|_{L^p(\mathbb R^N\times\Omega;\,X)}
  \lesssim
  \|f\|_{L^p(\mathbb R^N;\,X)}
\]

under the hypothesis that \(X\) is a UMD function lattice.  Immediately before Theorem 4.16, the authors write that proving or disproving this estimate without the lattice assumption is an interesting question.

This packet proves a positive subcase: the same estimate holds for every UMD Banach space \(X\) of Rademacher type \(2\).  The proof replaces the lattice-only Carleson embedding Proposition 4.18 by a type-2 embedding lemma.  The rest of the source proof of Theorem 4.16 is unchanged.

This shows that the lattice structure is not necessary for the adjoint square-function estimate itself, although it does not settle the estimate for arbitrary UMD spaces.

## Novelty Check

Cheap-index search found no prior packet for arXiv:1201.0648, the source title, the dual square-function estimate, or the type-2 Carleson replacement.  Web searches on 2026-07-18 for the exact source title, the exact phrase `Proving (or disproving) the dual square-function estimate`, and variants involving `type 2`, `Carleson embedding`, and `E_k(c_k f)` found the source paper and broader RMF/UMD literature, but no exact settlement of this type-2 subcase.

Novelty confidence is moderate: the argument is short and may be known folklore, but it is not already indexed in this run.

## Files

- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source crop containing the question before Theorem 4.16.
- `code/make_open_problem_crop.py`: reproducible crop script.

## Human Review

Recommended review focus: check that Proposition 4.18 is the only point in the source proof of Theorem 4.16 that uses the function-lattice structure, and that every subsequent invocation admits the harmless index shift used by the type-2 Carleson embedding lemma.
