# Full solution packet: KB-dual domination necessity

Status: likely valid full answer.

Source paper: Eduard Emelyanov, Nazife Erkursun-Ozcan, Svetlana Gorokhova, "d-Operators in Banach Lattices", arXiv:2401.08792.

Targeted question: after Theorem 3, the authors ask whether the hypothesis that `E'` is a KB-space is necessary for the domination conclusions for d-compact and d-weakly compact operators.

Result: yes, in the natural quantified sense.  For a Banach lattice `E`, `E'` is a KB-space iff positive domination preserves d-compactness for all Banach lattice ranges, and iff positive domination preserves d-weak compactness for all Banach lattice ranges.

Construction for the converse: if `E'` is not KB, choose a bounded disjoint positive sequence `(x_n)` in `E` and `u in E'_+` with `u(x_n)` bounded away from zero.  Split `u` into disjoint positive components `phi_n` carried by the `x_n`.  Define `T x = u(x) 1` in `c` and `S x = (sum_{i>=k} phi_i(x))_k`.  Then `0 <= S <= T`, `T` is rank-one compact, but the sequence `S x_n` consists of initial-segment vectors of positive height and has no weakly convergent subsequence in `c`.  Therefore `S` is neither d-weakly compact nor d-compact.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered source paper.
- `figures/open_problem_crop.png`: source crop of the theorem and question.

Novelty check: local run indexes and bounded web search on 2026-06-29 found no duplicate packet or later exact resolution.
