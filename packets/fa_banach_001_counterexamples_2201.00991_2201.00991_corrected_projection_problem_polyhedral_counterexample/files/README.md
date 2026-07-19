# Counterexample to the corrected Banach projection problem

- Source: K. Mahesh Krishna, *Paulsen and Projection Problems for Banach Spaces*, arXiv:2201.00991.
- Target: Problem 2.14, "Projection problem for Banach spaces".
- Status: candidate counterexample likely valid to the corrected/intended projection-problem statement.
- Agent: agent_lane_06.
- Date: 2026-06-28.

## Claim

Even after repairing the apparent typo in Problem 2.14 by replacing the printed
conclusion's `|zeta_k(P u_k)| = n/d` with the natural intended condition
`|zeta_k(Q u_k)| = n/d`, the Banach projection problem is false.

Let

```text
a = sqrt(3/5),  b = sqrt(2/5)
```

and put on `R^2` the norm

```text
||x|| = max(|x1|, |x2|, |a x1 + b x2|).
```

The standard basis and coordinate functionals are an Auerbach basis.  Let
`u = (a,b)` and `phi(x) = a x1 + b x2`.  Then `||u|| = ||phi|| = phi(u) = 1`.
For the rank-one projection

```text
P x = phi(x) u
```

we have, for `k=1,2`,

```text
||P e_k||^2 = ||e_k^* P||^2 = |e_k^*(P e_k)|.
```

The common values are `3/5` for `k=1` and `2/5` for `k=2`, so with
`d=2`, `n=1`, and `epsilon=1/5`, the hypothesis of Problem 2.14 is satisfied.

But no rank-one projection `Q` can satisfy the corrected flat conclusion with
common value `1/2`.  If `Q = psi tensor v`, the column and diagonal equations
force

```text
|v_1| = |v_2| = ||v|| / sqrt(2).
```

After normalizing `v`, this would put a vector with coordinate moduli
`1/sqrt(2)` on the unit sphere.  In the norm above every such vector has norm
at most `(a+b)/sqrt(2) < 1`, a contradiction.

## Scope

This gives a full negative answer to the corrected projection problem for
Banach spaces, in the all-finite-dimensional/all-Banach-spaces form stated in
Problem 2.14.  It does not settle the separate Banach Paulsen problem for
approximate Schauder frames.

## Packet Contents

- `main.tex`: review packet with statement and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: stitched crop of Problem 2.14 from pages 7-8.
- `code/verify_polyhedral_counterexample.py`: arithmetic verifier for the example.

## Novelty Check

Cheap-index search found no prior packet for arXiv:2201.00991 before this lane's
work.  Web searches on 2026-06-28 for the exact title and projection-problem
phrases returned the source arXiv record and no correction or later answer.

## Human Review Recommendation

Review as a genuine counterexample to the corrected/intended Banach projection
problem.  The proof is two-dimensional and only uses a norm defined as the
maximum of three absolute values.
