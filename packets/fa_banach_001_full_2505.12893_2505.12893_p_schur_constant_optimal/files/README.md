# Sharp constant for Proposition P:schur

Status: likely valid full solution, pending human review.

Source paper: Ondrej F. K. Kalenda, "Quantitative Schur property and measures of weak non-compactness", arXiv:2505.12893.

Question addressed: the final Question 9.2 asks whether the implication
`(iii_c) -> (ii_{2c+1})` in Proposition P:schur is optimal.

Result:

- For every `c >= 1`, the constant `2c+1` is sharp.  There is a Banach space satisfying `(iii_c)` but failing `(i_C)`, equivalently `(ii_C)`, for every `C < 2c+1`.
- For `0 < c < 1`, `(iii_c)` forces finite dimensionality.  Hence the best possible conclusion is `(ii_1)`, and `1` is sharp for nonzero finite-dimensional spaces.

The sharp examples for `c >= 1` are explicit.  Over `K = R` or `C`, set
`X_c = K + ell_1` with

```text
||(t,x)||_c = max{ ||x||_1, |t| + 2c ||x||_infty }.
```

Then `X_c` satisfies `(iii_c)`.  The sequence `y_n = (1,e_n)` has norm
`2c+1`, but every weak-star cluster point of `(y_n)` in `X_c**` has norm
exactly `1`.  Thus no smaller constant than `2c+1` can follow from `(iii_c)`.

Files:

- `main.tex`: full write-up.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/check_one_parameter_norm.py`: small arithmetic check for the norm and constants used in the construction.

Novelty and duplicate checks:

- Local run indexes were searched for arXiv `2505.12893`, `P:schur`, `2c+1`, `iii_c`, and "quantitative Schur"; only the earlier partial finite-sum lower-bound packet was found.
- Bounded web searches on 2026-06-14 for exact phrases around `(iii_c)`, `(ii_{2c+1})`, `P:schur`, `2c+1`, and Kalenda found no explicit later solution to Question 9.2.

Human review recommendation:

- Check the gliding-hump estimate proving `(iii_c)` for `X_c`.
- Check the averaging argument bounding the weak-star cluster norm of `(1,e_n)`.
- Check the use of Rosenthal's `ell_1` theorem and James' distortion theorem in the small-constant `0 < c < 1` case.
