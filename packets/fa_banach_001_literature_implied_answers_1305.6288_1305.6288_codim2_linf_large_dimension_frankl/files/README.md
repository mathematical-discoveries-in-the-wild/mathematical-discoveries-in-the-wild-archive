# Literature-implied answer: codimension-2 subspaces of `ell_infty^n` in large ambient dimension

Status: `literature_implied_answer (partial subcase)`

Source question: Tomasz Kobos, *Equilateral dimension of some classes of normed spaces*, arXiv:1305.6288v2, concluding remarks, final problem.  The source asks whether every `(n-2)`-dimensional subspace `X` of `ell_infty^n` satisfies `e(X) >= n-1`.

Supporting theorem: Nora Frankl, *Large Equilateral Sets in Subspaces of `ell_infty^n` of Small Codimension*, Discrete Comput. Geom. 67 (2022), 882-893, DOI `10.1007/s00454-020-00272-2`, Theorem 1.2 and the sentence immediately after Corollary 1.3.

Identification: Frankl cites Kobos' codimension-2 problem and states that Theorem 1.2 solves it when the ambient dimension is at least 9.  In source notation, if `X` is an `(n-2)`-dimensional subspace of `ell_infty^n`, Frankl's theorem gives `e(X) >= n-1` for `n >= 9`.

Scope limitations: This is not a full answer to the source problem.  The cases `n <= 6` follow from the known Petty/Makeev low-dimensional result because `dim X <= 4`; Frankl covers `n >= 9`.  The ambient cases `n=7,8` are not settled by this packet.

Files:

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: Kobos source paper.
- `supporting_paper_frankl_2022.pdf`: Frankl supporting paper.

Ledger: `runs/fa_banach_001/ledger/results/1305.6288_codim2_linf_large_dimension_frankl.json`.

