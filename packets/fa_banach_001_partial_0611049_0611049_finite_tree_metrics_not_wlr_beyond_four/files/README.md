# Partial Packet: Finite Tree Metrics Are Not WLR Beyond Four Points

## Source Question

- Source paper: J. Melleray, F. V. Petrov, and A. M. Vershik, *Linearly rigid metric spaces and the embedding problem*, arXiv:math/0611049.
- Target: Question 5 in Section 3.3, asking whether there exists a finite weakly linearly rigid (WLR) metric space with more than four points.
- Source PDF retained as `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Result

This packet proves a negative answer for the natural class of finite tree
metrics whose tree vertices are exactly the metric points. If `T` is a finite
weighted tree and `rho` is its path metric on `V(T)`, then `(V(T),rho)` is not
WLR whenever `|V(T)| >= 5`. For four tree vertices, the only WLR case is the
weighted tripod `K_{1,3}`, which is exactly the four-point family already
listed in the source paper.

## Scope

This is a partial result, not a complete answer to Question 5. It rules out
all finite tree metrics on more than four tree vertices, but it does not rule
out arbitrary non-tree finite metrics with five or more points.

## Verification

The script `code/check_tree_wlr.py` checks the combinatorial vertex-count
mechanism for labeled trees up to six vertices and distinguishes the four-point
path from the four-point tripod.

Run:

```bash
conda run --no-capture-output -n sandbox python code/check_tree_wlr.py
```

Expected output:

```text
Tree WLR combinatorial checks passed.
```

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_crop.png`: crop of Question 5.
- `code/check_tree_wlr.py`: finite combinatorial verifier.
- `code/crop_open_problem.py`: regenerates the source-question crop.
