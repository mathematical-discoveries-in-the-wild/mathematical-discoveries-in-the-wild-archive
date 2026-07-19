# 2605.25037 Finite-p Hausdorff Spaceability

- Result type: candidate full solution.
- Source paper: Jia Liu, Saisai Shi, Zhenliang Zhang, *On strong spaceability of continuous functions and fractal dimensions*, arXiv:2605.25037v2.
- Target: Question 3.19, asking whether `H_s[0,1]` is `(p,c)`-spaceable for integers `3 <= p < aleph_0`.
- Packet PDF: `solution_packet.pdf`.
- Source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.
- Colleague-supplied draft retained as `provided_solution_draft.tex` and `provided_solution_draft.pdf`.

## Claim

For every `1 < s <= 2`, the set

```text
H_s[0,1] = { f in C[0,1] : dim_H G_f([0,1]) = s }
```

is `(p,c)`-spaceable for every finite `p`. This gives an affirmative answer to Question 3.19.

## Proof Idea

Given a finite-dimensional starting subspace `E subset H_s[0,1] union {0}`, use Liu--Shi--Zhang Proposition 3.10 with `m=1` to find a compact set `K_0` of dimension `s-1` such that every nonzero `w in E` still has graph dimension `s` on the complement of `K_0`.

Construct a closed `c_0`-subspace `X_0` of `C[0,1]` whose nonzero elements have graph dimension `s` on `K_0` and are affine on every component of `[0,1] \ K_0`. Then `E cap X_0 = {0}` because nonzero elements of `E` have dimension `s` on the complement while elements of `X_0` have dimension at most `1` there. The direct sum `Y=E direct-sum X_0` is closed, has dimension `c`, contains `E`, and every nonzero element has graph dimension exactly `s`.

## Verification Notes

- The packet corrects the provided draft's source pointer from Proposition 3.4 to Proposition 3.10 with `m=1`.
- The proof is analytic; no numerical verifier is used.
- The screenshot crop is reproducible with:

```bash
conda run --no-capture-output -n sandbox python code/make_open_problem_crop.py
```

- Bounded novelty search was performed on 2026-06-13 using exact phrases around `Question 3.19`, `2605.25037`, `Hs[0,1]`, `(p,c)-spaceable`, and the source-paper title. It found the source arXiv page and no separate later answer. Because the source paper is very recent, novelty confidence is moderate.

## Human Review Focus

Check the compact `c_0`-subspace lemma, especially continuity at the accumulation point and the closed isometric `c_0` embedding. Also check the transfer step using affine interpolation on `[0,1] \ K_0` and the imported use of Liu--Shi--Zhang Proposition 3.10 with `m=1`.
