# Finite Infimal Sums of Lambda Tensor Norms

Status: `partial_result_likely_valid`

Source paper: Alejandro Chavez-Dominguez, Veronica Dimant, Daniel Galicer,
*Operator space tensor norms*, arXiv:2302.03696v1.

Targeted source problem: Problem 1 asks for more examples of `lambda`-o.s.
tensor norms beyond the typical examples `proj`, `h`, `h^t`, and the
`odot^theta` family constructed in the source paper.

Result proved here: finite operator-space infimal sums of `lambda`-o.s. tensor
norms are again `lambda`-o.s. tensor norms. If `lambda^1,...,lambda^N` are
represented by bilinear matrix products `B^i_k`, the sum is represented by the
block-diagonal products
`(A,B) -> diag(B^1_k(A,B),...,B^N_k(A,B))`.

Main concrete corollary: the symmetrized Haagerup sum tensor norm `h+h^t` is
itself a `lambda`-o.s. tensor norm, induced by `(A,B) -> diag(AB,BA)`.

Why this is useful: Problem 1 asks for more examples of `lambda`-o.s. tensor
norms. The closure theorem gives a systematic supply of examples rather than a
single one. In particular, the source paper uses `h+h^t` in the natural
tensor-norm discussion, especially as the Banach-level model for
`\backslash min /`, but it does not list it as a `lambda` example.

Scope: this is a general closure result and concrete family of examples for
Problem 1, not a full classification of `lambda`-o.s. tensor norms and not a
solution to the other open problems in arXiv:2302.03696.

Files:
- `main.tex` / `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: local copy of arXiv:2302.03696v1.
- `figures/open_problem_crop.png`: source crop containing Problem 1.

Novelty check: searched the run indexes for `2302.03696`, `operator space
tensor norms`, `lambda-o.s.`, `h+h^t`, `symmetrized Haagerup`, `infimal sum`,
and `block diagonal`; searched the web for exact phrases including `"h+h^t"
"lambda" "operator space" tensor norm`, `"symmetrized Haagerup" "lambda" tensor
product`, `"lambda tensor product" "operator spaces" "direct sum"`, and
`"operator space" "lambda tensor norm" "block diagonal"`. No direct prior
statement of this closure result was found in the searched material.
