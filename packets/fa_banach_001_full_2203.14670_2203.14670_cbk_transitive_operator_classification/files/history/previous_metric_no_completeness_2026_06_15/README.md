# Metric `C_b(K)` Classification Without Completeness

Status: `partial_result` / theorem-adjacent strengthening.

Source paper: Lixin Cheng, Junsheng Fang, Chunlan Jiang, "On the third problem of Halmos on Banach spaces", arXiv:2203.14670v2.

Target passage: Theorem 1.9 / Theorem 16.1 states that for a complete metric space `K` with infinite-dimensional `C(K)` of bounded continuous scalar functions, `C(K)` admits an operator without nontrivial invariant subspaces if and only if `K` is compact.

Result: the completeness hypothesis is unnecessary. For every metric space `K` such that `C_b(K)` is infinite-dimensional, `C_b(K)` admits a bounded operator without nontrivial closed invariant subspaces if and only if `K` is compact.

Scope: this does not solve Halmos's third problem for invertible operators. It strengthens the source paper's final `C(K)` classification by removing an extra topological hypothesis.

Proof mechanism: compact metric spaces are already handled by the source theorem. If `K` is noncompact metric, choose a sequence with no convergent subsequence. Its range is a closed discrete subset `D`; restriction maps `C_b(K)` onto `C_b(D) = ell_infty` by Tietze extension. Hence `C_b(K)` is nonseparable. Every bounded operator on a nonseparable Banach space has a nontrivial invariant subspace, because the closed orbit of any nonzero vector is separable.

Novelty/literature check: local run indexes were searched for `2203.14670`, `C(K)`, `C_b(K)`, `complete metric`, `bounded continuous`, and invariant-subspace keywords. Web searches were also run for the Halmos third problem and for `C_b(X)`/noncompact metric/separability variants. No existing run packet or later source explicitly recording this exact removal of completeness was found. The argument uses standard topology and may be folklore; human review should check novelty expectations.

Files:
- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: source theorem statement crop.
- `figures/source_proof_tail_crop.png`: source proof tail showing where completeness was used.
- `code/crop_source.py`: reproducible crop helper.
