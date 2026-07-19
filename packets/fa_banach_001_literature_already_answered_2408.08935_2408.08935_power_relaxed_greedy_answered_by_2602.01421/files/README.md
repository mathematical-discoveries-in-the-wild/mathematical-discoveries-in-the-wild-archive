# 2408.08935 Question 1 answered by 2602.01421

status: literature_already_answered

Source paper: Andrea Garcia, *Greedy algorithms: a review and open problems*,
arXiv:2408.08935.

Supporting paper: Pablo M. Berna and Andrea Garcia, *Convergence Analysis of
Greedy Algorithms with Adaptive Relaxation in Hilbert Spaces*,
arXiv:2602.01421.

## Identification

The source paper introduces the Power-Relaxed Greedy Algorithm by replacing the
relaxation parameter `1/m` in the relaxed greedy algorithm with `1/m^alpha`.
After proving the standard estimate for `alpha <= 1`, it asks Question 1:
whether there is some `alpha_0 > 1` and a constant giving the corresponding
faster decay for every `f in A_1(D)`.

The supporting paper explicitly cites this as
`[Greedy algorithms: a review and open problems (2025), Question 1]`, restates
it as Question 2.3, and answers it negatively in Theorem 2.4.

## Answer

For every `alpha > 1`, the supporting paper constructs a dictionary in
`R^2` and an element `f in A_1(D)` for which the Power-Relaxed Greedy
Algorithm does not satisfy the hoped-for decay. In fact, the proof obtains a
positive lower bound on the error using the positive infinite product
`prod_{k >= 2} (1 - k^{-alpha})`.

## Scope

This packet clears only the Power-Relaxed Greedy Algorithm Question 1 from
arXiv:2408.08935. It does not answer the source paper's Question 2 about other
step functions, nor Questions 3--5 on semi-greedy bases and renorming.

## Files

- `source_paper.pdf`: source/open-problem paper, arXiv:2408.08935.
- `supporting_paper_2602.01421.pdf`: supporting answer paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.

