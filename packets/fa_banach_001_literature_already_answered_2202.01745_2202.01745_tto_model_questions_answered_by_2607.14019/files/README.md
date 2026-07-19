# Literature Status: TTO Model Questions

Status: literature_already_answered.

Original source:
- Ryan O'Loughlin, "Symmetric matrix representations of truncated Toeplitz operators on finite dimensional spaces", arXiv:2202.01745; later Linear Algebra Appl. 666 (2023), 11--28.
- Local PDF: `source_paper.pdf`.

Supporting answer:
- Ryan O'Loughlin, "Semialgebraic Dimension and Truncated Toeplitz Models for Complex Symmetric Matrices", arXiv:2607.14019, submitted 2026-07-15.
- Local PDF: `supporting_paper_2607.14019.pdf`.

Identification:
- The source paper restates the finite-dimensional model question: "Is every symmetric matrix unitarily equivalent to a direct sum of TTOs?" It also poses a refined representation conjecture in Section 3, Conjecture `newconj`, asking whether every existing unitary equivalence between a complex symmetric matrix and a TTO can be realised by a `C_theta`-real matrix representation.
- The supporting paper explicitly cites the 2023 source and resolves the same program. Its Corollary 4.2 says that for every `n >= 10`, the direct-sum question is false. Its Section 5 restates the refined conjecture as Conjecture 5.1 and proves the finite-dimensional case immediately afterward.

Scope:
- Negative answer: not every `n x n` symmetric matrix is unitarily equivalent to a direct sum of truncated Toeplitz operators for `n >= 10`.
- Positive answer: if a complex symmetric matrix is already unitarily equivalent to a single finite-dimensional TTO, then the equivalence can be realised with respect to a conjugation-invariant orthonormal basis.
- The packet records literature status only; it is not an original run proof or counterexample.

Ledger:
- `runs/fa_banach_001/ledger/results/2202.01745_tto_model_questions_answered_by_2607.14019.json`
