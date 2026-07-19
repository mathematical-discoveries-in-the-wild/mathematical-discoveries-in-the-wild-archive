# Adaptive Diagonal Criterion for BCP Failure

Status: `partial_criterion_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_adaptive_diagonal_bcp_criterion/`

## Result

This packet abstracts the recurring diagonal-escape mechanism into a Banach
space criterion.

If every countable family of proposed centers in a normed space `X` admits
adaptive coordinate retractions

`R_k : X -> E_k`

onto an isometric `ell_infty(E_k)` diagonal inside `X`, and the assigned
coordinate `R_k x_{pi(k)}` nearly norms the center `x_{pi(k)}`, then `X`
fails BCP.

For C*-algebras this gives a clean orthogonal-corner version: if countable
center families can be nearly normed on pairwise orthogonal two-sided corners
`q_k A p_k`, and bounded corner data can be glued back into `A` as an
`ell_infty` diagonal, then `A` fails BCP.

## Why This Matters

The previous II_1 factor obstruction showed that primitive topology alone is
too coarse. This packet identifies the next structural obstruction: adaptive
`ell_infty` diagonal/corner retractions.

It also clarifies the relation among earlier packets:

- atomless von Neumann algebras have exact two-sided corner diagonals, as in
  the source paper's proof;
- reduced products, sigma-unital coronas, and Hilbert-module coronas use
  approximate/asymptotic versions of the same mechanism.

## Files

- `main.tex`: self-contained criterion packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of Corollary 3.9 and Question 3.

## Human Review Recommendation

Review as a reusable abstraction/criterion. The core theorem is Banach-space
formal. The main mathematical judgment is whether the exact diagonal property
is the right next invariant, and where an approximate version should be
developed for reduced products and multiplier coronas.
