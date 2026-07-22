# Coordinate sweeps have no extra fixed points

Status: `candidate_full_solution_likely_valid_needs_human_review` for
Question 1 in Remark 4.6 of arXiv:1102.1478.

## Result

The paper defines `U_k = J_k o R_k`. Equations (62)--(63) show that `U_k`
changes only coordinate `k` of the product space. A general coordinate-sweep
lemma gives

```text
Fix(U_m o ... o U_1) = intersection_k Fix(U_k).
```

If a full sweep returns `x` to itself, the first updated coordinate cannot
be repaired later, so `U_1` already fixes `x`. The same argument applies
successively to coordinates `2,...,m`. Equation (64) identifies the
intersection on the right with `S`. Consequently

```text
S = Fix(T) = Fix(J_m o R_m o ... o J_1 o R_1),
```

an affirmative full answer to Question 1. The argument works for every
positive integer `m` and for arbitrary one-coordinate update maps; the
Hilbert-space, monotonicity, and nonexpansiveness assumptions are not used
in the final step.

## Packet contents

- `solution_packet.pdf`: standalone statement, proof, audit, scope, and
  novelty notes.
- `source_paper.pdf`: arXiv:1102.1478v1.
- `figures/open_problem_crop.png`: source screenshot containing Remark 4.6.
- `VERIFICATION.md`: independent line-by-line structural audit.
- `tmp/`: LaTeX build artifacts.

## Verification and scope

The proof was checked directly against source equations (62), (63), (64),
and (66), including the order of composition. It remains valid if any
fixed-point set is empty. It settles only Question 1: it does not provide
the convergence conditions requested in Questions 2 and 3.

Cheap corpus indexes and bounded arXiv/web searches by identifier, title,
the displayed equality, and core terminology found no later general answer.
The follow-up arXiv:1206.3610 proves convergence in a special case, not this
general fixed-point equality. This is not an exhaustive bibliographic proof
of novelty, so independent mathematical and literature review is recommended
before external use.
