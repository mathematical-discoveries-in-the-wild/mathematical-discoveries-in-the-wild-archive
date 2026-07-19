# `C_b(K)` Transitive-Operator Classification

Status: `candidate_full_solution_theorem_adjacent_classification`.

Source paper: Lixin Cheng, Junsheng Fang, Chunlan Jiang, "On the third problem of Halmos on Banach spaces", arXiv:2203.14670v2.

Target passage: Theorem 1.9 / Theorem 16.1 states that for a complete metric space `K` with infinite-dimensional `C(K)` of bounded continuous scalar functions, `C(K)` admits an operator without nontrivial invariant subspaces if and only if `K` is compact.

Result: the completeness hypothesis is unnecessary. For every metric space `K` such that `C_b(K)` is infinite-dimensional, `C_b(K)` admits a bounded operator without nontrivial closed invariant subspaces if and only if `K` is compact.

Stronger formulation: for an arbitrary topological space `K`, let `K_cr` be the reflection seen by bounded continuous scalar-valued functions. Then `C_b(K)` admits a bounded operator without nontrivial closed invariant subspaces if and only if `K_cr` is compact metrizable and is either a singleton or infinite. Under the source paper's infinite-dimensional hypothesis this is equivalent to separability of `C_b(K)`.

Scope: this does not solve Halmos's third problem for invertible operators. It is a full theorem-adjacent classification of the final `C(K)`/`C_b(K)` result in the source paper.

Proof idea: if `C_b(K)` has a transitive operator, every nonzero vector is cyclic, so `C_b(K)` is separable. Conway's theorem identifies separable `C_b(K)` for Tychonoff spaces with compact metrizability. The compact-metric existence direction uses the source paper's Read-Sobczyk route: infinite compact metric `K` contains a complemented `c_0` inside `C(K)`, and Read gives a transitive operator on `c_0 \oplus Y`. The arbitrary topological case is handled by replacing `K` with its bounded-continuous-function reflection `K_cr`.

History:
- `history/previous_metric_no_completeness_2026_06_15/` contains the earlier metric-only packet.

Evidence:
- `evidence/supplied_cb_invariant_subspace_classification_2026_06_22/` contains the supplied TeX audit that motivated this promotion. The supplied PDF in Downloads could not be copied because macOS denied access, but the active packet was rebuilt from the TeX source.

Review notes:
- Check the citation to Conway's separability theorem for `C_b(K)` and the reflection reduction for arbitrary topological spaces.
- Treat novelty conservatively: the result is packaged here as a full classification using classical ingredients, not as an asserted new literature contribution.
