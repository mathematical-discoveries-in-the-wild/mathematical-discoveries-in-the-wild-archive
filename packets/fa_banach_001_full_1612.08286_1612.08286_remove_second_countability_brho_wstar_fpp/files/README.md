# Full solution candidate: removing second countability from Naderi Theorem 3.1

Status: `full_solution_candidate_likely_valid`

Source: Fouad Naderi, *C*-algebraic approach to fixed point theory generalizes Baggett's theorem to groups with discrete reduced duals*, arXiv:1612.08286.

Target: Question 5 on page 9 asks whether Theorem 3.1 can be proved for weak* fpp without the second countability assumption on the locally compact group `G`.

Result: Yes. For every locally compact group `G`, if the reduced Fourier-Stieltjes algebra `B_rho(G)=C*_r(G)^*` has the weak* fixed point property, then `G` is compact. Together with the source paper's compact-group converse, this gives the countability-free equivalence.

Proof idea: If `G` is noncompact, choose a noncompact sigma-compact open subgroup `H`. Kakutani-Kodaira gives a compact normal subgroup `N` of `H` such that `H/N` is second countable and still noncompact. Weak* fpp passes from `B_rho(G)` to `B_rho(H)` via the open-subgroup compression `C*_r(G) -> C*_r(H)`, and from `B_rho(H)` to `B_rho(H/N)` via the compact-normal quotient map `C*_r(H) -> C*_r(H/N)`. Naderi's second-countable theorem then forces `H/N` compact, contradiction.

Files:

- `main.tex` - full proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - arXiv source paper PDF.
- `figures/open_problem_crop.png` - crop of the page 9 question list.
- `code/make_open_problem_crop.py` - reproducible crop script.

Novelty check: cheap indexes and web searches on 2026-07-19 found the source paper and adjacent separable/reduced-dual background but no later explicit removal of the second countability assumption.

Human review: focus on the reduced group C*-algebra functoriality steps for open subgroups and compact normal quotients.
