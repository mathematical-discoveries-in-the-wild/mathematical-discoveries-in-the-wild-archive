# Literature-Implied Answer: Uniformly Discrete Free Spaces and Isometric `ell_1`

## Source Question

- Source paper: Marek Cuth and Michal Johanis, *Isometric embedding of `ell_1` into Lipschitz-free spaces and `ell_infty` into their duals*, arXiv:1604.04131.
- Question 2 asks whether, for every uniformly discrete metric space `M`, the Lipschitz-free space `F(M)` contains a subspace isometric to `ell_1`.
- Screenshot: `figures/open_question_crop.png`.
- Source PDF retained as `source_paper.pdf`.

## Status

This is not counted as a new original pipeline proof. It is filed as a
`literature_implied_answer` because Ostrovskii's later paper
arXiv:1910.03625 gives a necessary and sufficient matching criterion and
explicitly applies it to the concrete metric examples from Cuth--Johanis'
Remark 10. Applying that criterion to one uniformly discrete example gives a
negative answer to Question 2.

## Counterexample

Let `M={v_n : n in N}` and, for `n>k`, define

```text
d(v_k, v_n) = 1 + 1/n.
```

Equivalently, for distinct indices `i,j`, `d(v_i,v_j)=1+1/max(i,j)`.
Then `M` is uniformly discrete because all nonzero distances are larger than
`1`.

Ostrovskii's criterion says that `F(M)` contains an isometric copy of `ell_1`
if and only if there are disjoint pairs `(x_i,y_i)` such that every finite
initial family of edges is a minimum-weight perfect matching on its vertices.
For the metric above, no such sequence exists: from any infinite sequence of
disjoint pairs choose two pairs whose four indices satisfy
`q1<q2<q3<q4`. The original two-pair matching has weight

```text
d(v_q1,v_q2)+d(v_q3,v_q4) = 2 + 1/q2 + 1/q4,
```

while the crossed matching has weight

```text
d(v_q1,v_q3)+d(v_q2,v_q4) = 2 + 1/q3 + 1/q4,
```

which is strictly smaller. Hence the original matching is not minimal, so the
criterion fails and `F(M)` contains no isometric `ell_1`.

## Files

- `solution_packet.pdf`: rendered human-facing packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original Cuth--Johanis paper.
- `supporting_paper_1910.03625.pdf`: later Ostrovskii paper.
- `code/verify_metric_and_matching.py`: finite checks for the metric and the crossing inequality.
- `code/crop_open_question.py`: recreates the screenshot crop.
