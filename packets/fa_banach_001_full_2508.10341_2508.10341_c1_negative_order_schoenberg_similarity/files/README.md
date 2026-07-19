# Conjecture 6.3 via a similarity transform

status: full_solution_likely_valid
arxiv_id: 2508.10341
source: Quanyu Tang and Teng Zhang, "Sharp Schoenberg type inequalities and the de Bruin--Sharma problem", arXiv:2508.10341v3
agent_id: agent_lane_16
updated_at: 2026-07-18T20:53:10Z

## Claim

This packet proves Conjecture 6.3 from the source paper.  In the source
notation, for

```text
P(z) = z prod_{j=1}^n (z - z_j),    z_j != 0,
```

and critical points `w_1,...,w_n` of `P`, we prove

```text
sum_k |w_k|^{-2}
  <= 3 sum_j |z_j|^{-2} + |sum_j z_j^{-1}|^2.
```

The packet also proves the equality characterization: equality holds if and
only if the nonzero zeros `z_1,...,z_n` lie on one line through the origin.
This strengthens the source conjecture, which only asserts the "whenever"
direction for equality.

## Main Idea

The source already identifies the reciprocal critical points as the eigenvalues
of

```text
B = diag(u) + u 1^T = diag(u)(I+J),        u_j = 1/z_j.
```

Put `C=I+J` and let `H=C^{1/2}`. Then `B` is similar to

```text
A = H diag(u) H.
```

Schur's eigenvalue-singular-value inequality gives

```text
sum |lambda_i(B)|^2 = sum |lambda_i(A)|^2 <= ||A||_F^2.
```

A trace expansion gives exactly

```text
||A||_F^2 = 3 sum |u_j|^2 + |sum u_j|^2.
```

Normality of `A` is equivalent to all `u_j` lying on a common real line, which
is equivalent to all `z_j` lying on a common line through the origin.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of source Conjecture 6.3.
- `code/verify_c1_random.py`: randomized numerical sanity check.

## Verification

The proof is symbolic and uses only the source's matrix model, a positive
square-root similarity, and Schur's inequality. The verifier samples random
complex `u` vectors and checks the inequality numerically.

## Novelty Check

Local cheap indexes had no exact row for `2508.10341` or Conjecture 6.3.
Web searches on 2026-07-18 for exact phrases around "Conjecture C1",
"Conjecture 6.3", the reciprocal critical-point inequality, and the
`diag(u)+u1^T` matrix form found the source arXiv/J-GLOBAL records and adjacent
Schoenberg/multiutility material, but no exact solution or this similarity
argument. Novelty remains subject to human mathematical literature review.
