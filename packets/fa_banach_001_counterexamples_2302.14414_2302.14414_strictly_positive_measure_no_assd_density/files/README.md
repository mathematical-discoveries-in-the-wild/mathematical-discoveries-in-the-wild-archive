# Counterexample packet: strictly positive measure obstruction to `ASSD2P_d(X)`

Status: likely valid counterexample.

Source paper: Stefano Ciaci, "On the transfinite symmetric strong diameter two property", arXiv:2302.14414.

Targeted source question: Question 3.2 asks, in part, whether every `T_4` locally compact space `X` with `d(X) > aleph_0` has `C_0(X)` enjoying `1-ASSD2P_{d(X)}`.

Result: no.  Let `Gamma` have cardinality larger than `2^{aleph_0}` and let `K = [0,1]^Gamma`.  Then `K` is compact Hausdorff, hence `T_4` locally compact, and `d(K) > aleph_0`.  However, `C_0(K)=C(K)` fails `1-ASSD2P_{d(K)}`.

Proof mechanism: the product Lebesgue probability measure `mu` has full support.  If `B +/- y` lies in the unit sphere of `C(K)`, then for every `f in B` one has `|f(t)| + |y(t)| <= 1` pointwise.  Since full support gives `int |y| dmu > 0` for every nonzero continuous `y`, all such `f` satisfy `mu(f) <= 1 - int |y| dmu < 1`.  Hence `B` cannot norm the singleton `{mu}`, which is an admissible test family because `d(K)` is uncountable.

This packet answers only the second half of Question 3.2.  It does not address the separate `SSD2P_{c(X)^+}` question.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local rendered copy of the source paper.
- `figures/open_problem_crop.png`: crop of the original question.

Novelty check: local run indexes and bounded web search on 2026-06-29 found no duplicate packet or later exact answer for this counterexample.
