# Literal counterexample to the printed Banach projection problem

- Source: K. Mahesh Krishna, *Paulsen and Projection Problems for Banach Spaces*, arXiv:2201.00991.
- Target: Problem 2.14, "Projection problem for Banach spaces".
- Status: candidate counterexample likely valid, literal/as-printed reading.
- Agent: agent_lane_06.
- Date: 2026-06-28.

## Claim

Problem 2.14 as printed is false.  The conclusion asks for a projection `Q`
such that

```text
||Q u_k||^2 = ||zeta_k Q||^2 = |zeta_k(P u_k)| = n/d
```

for every `k`.  Because the middle scalar still involves the original
projection `P`, the conclusion already forces the diagonal quantities
`|zeta_k(Pu_k)|` to be exactly flat.

Take `X = R^2` with the Euclidean norm, the standard Auerbach basis,
`d = 2`, `n = 1`, `epsilon = 1/2`, and let `P` be the orthogonal projection
onto the unit vector

```text
v = sqrt(3/5) e_1 + sqrt(2/5) e_2.
```

Then

```text
||P e_1||^2 = ||e_1^* P||^2 = |e_1^*(P e_1)| = 3/5
||P e_2||^2 = ||e_2^* P||^2 = |e_2^*(P e_2)| = 2/5
```

and both values lie in `[(1-epsilon)n/d, (1+epsilon)n/d] = [1/4, 3/4]`.
Thus `P` satisfies the hypothesis.  But the printed conclusion would require
`3/5 = 1/2` and `2/5 = 1/2`, which is impossible, independently of `Q`.

## Scope Caveat

This is an erratum-style literal counterexample.  It does not address the
probably intended corrected statement where the conclusion would contain
`|zeta_k(Q u_k)| = n/d` instead of `|zeta_k(P u_k)| = n/d`.

## Packet Contents

- `main.tex`: review packet with statement and proof.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_problem_crop.png`: stitched crop of Problem 2.14 from pages 7-8.
- `code/verify_counterexample.py`: small arithmetic verifier.

## Novelty Check

Cheap-index search found no prior packet for arXiv:2201.00991.  Related
approximate Schauder frame entries concern other papers and problems.  Web
searches on 2026-06-28 for the exact title and projection-problem phrases
returned the source arXiv record and no separate correction or later answer.

## Human Review Recommendation

Review as a literal/as-printed counterexample.  If the intended problem is
amended by replacing `P` with `Q` in the conclusion's diagonal scalar, this
packet should be treated only as a formulation issue and not as a counterexample
to the corrected Banach projection problem.
