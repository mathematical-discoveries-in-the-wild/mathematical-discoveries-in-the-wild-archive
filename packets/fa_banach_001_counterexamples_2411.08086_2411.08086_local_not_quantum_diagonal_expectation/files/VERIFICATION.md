# Verification report

Status: `counterexample_likely_valid`

## Mathematical checks

1. The strongly convergent diagonal sum
   `U = sum_n e_nn tensor z^n` is a unitary in
   `ell^infinity(N_0) bar-tensor L^infinity(T)`.
2. Haar orthogonality gives
   `(id tensor integral)(U^*(e_ij tensor 1)U) = delta_ij e_ij`,
   so the resulting map is exactly the normal diagonal expectation.
3. The ancilla in this construction is abelian, so the map is locally factorisable (indeed locally exact).
4. For a standard masa, the proof of Corollary 3.5 in the source explicitly asserts type-preserving exactness for `t` in `{loc,q,qa,qc}`. Hence a hypothetical quantum factorisation can be represented by a unitary sequence `(v_n)` in one finite-dimensional tracial von Neumann algebra.
5. Comparing the Schur symbols forces
   `tau(v_i^*v_j)=delta_ij`; this is an infinite orthonormal family in finite-dimensional `L^2(M,tau)`, which is impossible.

No numerical or computer-assisted mathematical step is used.

## Literature/novelty checks

- Searched the run indexes for arXiv:2411.08086, the title, local/quantum factorisability, the infinite-dimensional inclusion, Schur multipliers, and diagonal conditional expectation.
- Searched the web for the exact question, the notation around equation (28), the paper title with “local quantum infinite dimensional,” and diagonal-expectation/finite-ancilla variants.
- Checked the 2025 IMRN published version; it still states the question as unknown.
- No later answer, erratum, or matching diagonal-expectation counterexample was found in the bounded search.

Novelty confidence: moderate. Proof confidence: high, conditional only on reading the source's type-preserving exactness sentence in its literal stated scope.

## Render checks

- Compiled `main.tex` with `latexmk` using `pdflatex`; the build completed successfully.
- The final `solution_packet.pdf` has three pages.
- Both source-question crops were inspected for completeness and legibility; together they include equation (28) and the paper's statement that its infinite-dimensional validity is unknown.
- Rendered every final page at 150 dpi and visually inspected all three pages. No clipping, overlap, missing glyphs, or unreadable content was found.
- The final log has no overfull boxes, undefined references, or LaTeX warnings. One harmless underfull bibliography line was reported during compilation.
