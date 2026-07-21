# Verification report

## Mathematical status

`partial_result_likely_valid`

The packet proves a complete theorem under the additional hypothesis that the
predual has weak-star Fr\u00e9chet-Urysohn dual ball. It does not claim to solve the
unrestricted PCP/RNP question.

## Proof audit

1. **Failure of weak-star PCP to a sequential tree.** The standard
   nonfragmentability subset gives
   \(b\in\overline{B\setminus B(b,\delta)}^{w^*}\) at every node. The
   Fr\u00e9chet-Urysohn property of a bounded weak-star ball supplies a sequence
   converging to the specified point. Parent-child differences are uniformly
   separated, weak-star null, and telescope.
2. **Finite-codimensional selection.** Each constructed \(M_n\) is an
   intersection of finitely many kernels of predual vectors, hence weak-star
   closed and finite-codimensional. The quotient has its unique
   finite-dimensional Hausdorff vector topology, so a weak-star-null sequence
   has quotient norm tending to zero.
3. **Basicity.** Finite norming sets give
   \(\|e\|\le (1-\eta)^{-1}\|e+m\|\) for \(e\in E_n\), \(m\in M_n\).
   All later perturbation vectors lie in \(M_n\), yielding uniformly bounded
   partial-sum projections. The displayed summability bound satisfies the
   classical small perturbation criterion.
4. **Fullness and telescoping.** The subtree map sends children to children and
   therefore maps the complete ancestor chain at a node onto the complete
   ancestor chain of its image. Partial sums remain in the original unit ball.
5. **Failure passes to the basis subspace.** The norm closure of the partial
   sums is contained in the basis subspace's unit ball and every nonempty
   relatively weak-star open subset has a fixed positive diameter.

## Literature/novelty audit

- Cheap run indexes: no prior packet for arXiv:1309.3862 or this theorem.
- Exact and close web/arXiv searches: no explicit weak-star-angelic or WLD
  extension found.
- arXiv:1612.05948 confirms the standard terminology and that WLD spaces have
  weak-star angelic dual.
- Novelty confidence: moderate. Validity does not depend on the search result.

## Artifact checks

- `source_paper.pdf` is the arXiv source paper.
- `figures/open_problem_crop.png` is rendered from the source PDF and includes
  the entire open-problem paragraph and the source's separable-predual scope.
- `solution_packet.pdf` was compiled from `main.tex` with build intermediates
  confined to `tmp/`.
- Final packet pages and the crop were rendered to PNG and visually inspected
  for clipping, overlap, missing glyphs, and unreadable text.

