# Dual DDD of an SBD Need Not Be an SBD

Status: candidate counterexample, likely valid.

Source paper: Steven F. Bellenot, "Skipped Blocking and other Decompositions in Banach spaces", arXiv:math/0408004.

Extracted question: Question 3.3 asks whether, if `(X_n)` is an SBD, the dual DDD `(X_n^*)` is already an SBD.

Answer claimed here: no.  In a separable Hilbert space, take an orthogonal sum of three-dimensional blocks with orthonormal coordinates `e_{r,1}, e_{r,2}, e_{r,3}` and parameters `eps_r -> 0`.  In block `r`, set

```text
X_{3r-2} = [e_{r,1}],
X_{3r-1} = [e_{r,1} + eps_r e_{r,2} + e_{r,3}],
X_{3r}   = [e_{r,3}].
```

The primal skipped before/after spaces are always orthogonal, so `(X_n)` is an SBD with constant 1.  But the dual lines in the same block contain

```text
u_r = e_{r,1} - eps_r^{-1} e_{r,2},
z_r = e_{r,3} - eps_r^{-1} e_{r,2}.
```

When the middle dual line is skipped, the dual skipped projection sends `u_r - z_r` to `u_r`, so its norm is at least

```text
||u_r|| / ||u_r - z_r|| = sqrt(1 + eps_r^{-2}) / sqrt(2),
```

which is unbounded.  Hence the dual DDD is not an SBD.

Novelty/literature check:
- Cheap run indexes searched for `0408004`, `skipped blocking`, `SBD`, `dual DDD`, and `predecomposition space`; no exact prior packet was found.
- The source paper itself gives Example 3.4 where a DDD has non-SBD dual DDD, but its original DDD is not an SBD; this does not answer Question 3.3.
- Web searches on June 19, 2026 for exact phrases including `"If (X_n) is a SBD" "dual DDD"`, `"Skipped Blocking" "dual DDD" "SBD"`, and `"predecomposition space" "SBD"` found the source paper and unrelated later uses of skipped blocking, but no later settlement of Question 3.3.

Files:
- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: locally rendered PDF of the arXiv source.
- `figures/open_problem_crop.png`: crop of Question 3.3.
- `code/check_three_block_constants.py`: numerical check of the finite three-block constants.

Human-review focus:
- Check the global SBD constant-1 claim: every skipped interval leaves orthogonal before/after pieces.
- Check the identification of the dual lines `X_n^*` in each three-dimensional Hilbert block.
- Check that the unbounded middle-skip constants in the dual DDD are exactly SBD constants for the dual sequence.
