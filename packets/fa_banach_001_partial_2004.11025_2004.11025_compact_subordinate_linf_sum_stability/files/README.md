# Partial result: compact-subordinate range-sum stability for QNA operators

- **Run:** `fa_banach_001`
- **Source:** arXiv:2004.11025, *On quasi norm attaining operators between Banach spaces*, Geunsu Choi, Yun Sung Choi, Mingu Jung, Miguel Martin.
- **Problem targeted:** Problem 7.3 in the source paper asks whether density of `QNA(X,Y_j)` in `L(X,Y_j)` for `j=1,2` implies density of `QNA(X,Y_1 \oplus_\infty Y_2)` in `L(X,Y_1 \oplus_\infty Y_2)`.
- **Status:** `partial_result_likely_valid`
- **Packet:** `solution_packet.pdf`
- **Source PDF:** `source_paper.pdf`
- **Open-problem crop:** `figures/open_problem_crop.png`

## Results

The packet now records two positive subcases.

First, if an operator
`T=(T_1,T_2):X -> Y_1 \oplus_\infty Y_2` has a maximal coordinate, say
`||T_1||=||T||`, with `T_1` in the norm-closure of `NA(X,Y_1)`, then
`T` lies in the norm-closure of `QNA(X,Y_1 \oplus_\infty Y_2)`, with no
condition on the other coordinate. The proof perturbs and slightly scales a
norm-attaining approximant of the dominant coordinate; strict dominance makes
the whole sum norm attaining.

Second, the packet proves a compact-subordinate positive subcase. If an operator
`T=(T_1,T_2):X -> Y_1 \oplus_\infty Y_2` has a maximal coordinate, say
`||T_1||=||T||`, with `T_1` in the norm-closure of `QNA(X,Y_1)`, and the other
coordinate `T_2` in the norm-closure of the compact operators `K(X,Y_2)`, then
`T` lies in the norm-closure of `QNA(X,Y_1 \oplus_\infty Y_2)`. The symmetric
statement also holds.

The mechanism is simple but useful: make the QNA coordinate strictly dominant.
Along its quasi-norming sequence, the compact subordinate coordinate has a
norm-convergent subsequence, so the pair has a convergent image sequence at the
full operator norm.

## Scope and limitations

This does not solve Problem 7.3 in full. It does not handle the hard case where
both coordinates are merely QNA-approximable and neither subordinate coordinate
can be compactly approximated or made norm-attaining at the dominant coordinate.
It also does not by itself produce the source paper's desired endomorphism
example with `QNA(Z,Z)` dense and `NA(Z,Z)` not dense.

## Novelty check

Cheap run indexes had only a prior hard-triage attempt for arXiv:2004.11025 and
no durable result. Local source inspection covered arXiv:2004.11025 and the
later weak-star paper arXiv:2209.07763. Web searches on 2026-06-19 for exact
phrases around `"quasi norm attaining" "ell_infty"`, `"QNA(X,Y_1"` and
`"Problem 7.3" "QNA"` found the source paper and the weak-star variant, but no
ordinary-QNA resolution of the range-sum problem.

## Human review recommendation

Review as a modest but complete partial theorem. The proof is short; the main
check is the epsilon bookkeeping that creates a strictly dominant QNA coordinate
while keeping the perturbation arbitrarily small.
