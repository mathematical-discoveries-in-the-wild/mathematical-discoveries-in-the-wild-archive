# Counterexample Packet: BD Polyhedrality vs convex-DLD2P

Status: candidate counterexample, likely valid.

## Source Problem

- Source paper: Miguel Martin and Abraham Rueda Zoca, *Daugavet property in projective symmetric tensor products of Banach spaces*, arXiv:2010.15936.
- Location: Problem 3.12, page 12 of `source_paper.pdf`.
- Extracted question: whether a real `L_1`-predual has the convex-DLD2P if and only if it fails to be (BD) polyhedral.

## Result

The answer is negative.  The real hyperplane

```text
X = { x in c : 2 lim_n x_n = x_1 + x_2 }
```

is an `L_1`-predual, fails to be (BD) polyhedral, and does not have the
convex-DLD2P.

The `L_1`-predual fact follows from the hyperplane classification of Casini,
Miglierina, and Piasecki, applied to
`f=(1/2,-1/4,-1/4,0,...)`.  The rest is elementary once Theorem 3.2 of the
source paper identifies Delta-points of real `L_1`-preduals through the extreme
points of the dual ball.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv:2010.15936 PDF.
- `supporting_paper_1410.7801.pdf`: hyperplane/predual reference.
- `figures/open_problem_crop.png`: crop of the source problem.
- `code/verify_counterexample.py`: small arithmetic verifier for the displayed witnesses.

## Novelty / Duplicate Check

Local lightweight indexes were searched for `2010.15936`, `convex-DLD2P`,
`BD polyhedral`, `Problem 3.12`, and the explicit hyperplane pattern.  No prior
packet or attempt for this counterexample was found.

Web searches on 2026-06-18 for exact and close phrases including
`"convex-DLD2P" "BD polyhedral"`, `"Problem 3.12" "convex-DLD2P"`,
and `"2 lim" "x_1" "x_2" "convex-DLD2P"` did not surface a later paper
answering the problem or this construction.

## Human Review Recommendation

Review the indexing convention for the hyperplane `W_f` and confirm that
Theorem 4.3 of arXiv:1410.7801 applies exactly to
`f=(1/2,-1/4,-1/4,0,...)`.  The geometric obstruction after that is short:
all Delta-points lie in the closed convex set `x_1=x_2=lim x`, but the unit
ball contains `(1,-1,0,0,...)` with limit `0`.
