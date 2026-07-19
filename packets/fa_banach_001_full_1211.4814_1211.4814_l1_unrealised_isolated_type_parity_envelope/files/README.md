# Candidate full solution: an unrealised isolated type over `ell_1`

Status: `candidate_full_solution_subquestion_human_review_needed`

Source paper: Itai Ben Yaacov and C. Ward Henson, *Generic orbits and type isolation in the Gurarij space*, arXiv:1211.4814, Fund. Math. 237 (2017), 47--82.

## Claim

Question 6.8 asks whether there is an infinite-dimensional Banach space over
which unrealised isolated types exist, and specifically asks what happens for
`E = ell_1`, `E* = ell_infty`.

This packet gives a positive answer to that subquestion:

```text
Over E = ell_1 there is an isolated 1-type that is not realised in E.
```

It does not claim that isolated types are dense over `ell_1`, and therefore it
does not settle the separate existence/classification problem for `G[ell_1]`.

## Proof Idea

Identify the weak-star unit ball of `ell_infty = ell_1*` with the product cube
`[-1,1]^N`.  On its extreme sign sequences set
`p(epsilon) = epsilon_1 epsilon_2 epsilon_3`, and let `h` be the convex envelope
of `p` on the whole cube.  The odd parity choice is the smallest finite cube
pattern that is not affine.

The envelope `h` is continuous, convex, satisfies the antipode inequality, and
is maximal among convex functions compatible with those extreme-point parity
values.  By the Ben Yaacov-Henson criterion, `h` is the conjugate of a convex
Katetov function `f`, hence of a 1-type over `ell_1`.  Continuity makes `f`
local, maximality makes it boundary-extreme, and Theorem 5.7 of the source
paper then makes `f` isolated.  Finally `h(0) = -1`, whereas realised types have
conjugate value `0` at the origin, so this isolated type is unrealised.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1211.4814.
- `figures/open_question_crop.png`: crop of Question 6.8.
- `code/parity_envelope_check.py`: small finite check for the parity pattern at the origin.

## Novelty Check

Checked the run indexes for `1211.4814`, title terms, `Gurarij`, `generic orbit`,
`type isolation`, `prime model`, `G[E]`, and `ell_1`; no exact prior packet was
present.  Later local citation hits to arXiv:1211.4814 were inspected at keyword
level and did not show a closure of Question 6.8.  Web searches for the exact
title and for `Gurarij isolated types ell_1`, `G[E] Gurarij ell_1`, and
`unrealised isolated types Gurarij` found the source paper but no obvious later
answer.

## Human Review Focus

Review as a focused full solution to the unrealised-isolated-type subquestion.
The key points are:

1. the convex envelope on the infinite product cube is weak-star continuous
   because it depends only on the first three coordinates;
2. the envelope's extreme-point maximality indeed gives boundary-extremality in
   the Ben Yaacov-Henson sense;
3. `h(0) = -1` correctly invokes the source paper's realised-type criterion.
