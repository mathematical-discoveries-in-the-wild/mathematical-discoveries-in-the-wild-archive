# Counterexample Packet: `2602.15525_unit_ball_embedding_extension_counterexample`

Status: `candidate_counterexample_likely_valid_literal_extension_statement`

Source: S.A. Bogaty and A.A. Tuzhilin, *Mazur-Ulam Theorem With
Gromov-Hausdorff Distance*, arXiv:2602.15525.

## Result

Problem 22 asks whether an isometric embedding \(f:B_V\to W\) of the unit ball
of a Banach space must extend to a linear isometric embedding
\(F:V\to W\) with \(F|_{B_V}=f\).

The literal extension statement is false. For any nonzero Banach space \(V\),
set \(W=V\oplus_\infty \mathbb R\) and
\[
  f(v)=(v,\|v\|),\qquad v\in B_V .
\]
Then \(f\) is an isometric embedding, but no linear map \(F:V\to W\) can agree
with \(f\) on \(B_V\), because for \(\|u\|=1\) linearity would force
\(F(-u)=-F(u)\), whereas \(f(u)=(u,1)\) and \(f(-u)=(-u,1)\).

## Scope

This packet only refutes the literal parenthetical extension requirement
`such that \(F|_{B_V}=f\)`. It does not refute the weaker reading that asks
only whether \(W\) contains some linear isometric copy of \(V\) whenever
some isometric embedding \(B_V\to W\) exists. In the example above, the weaker
conclusion is true via \(v\mapsto(v,0)\).

This is also closely related to the same source paper's preceding nonlinear
norm-graph construction. Human review should decide whether to count this as a
counterexample to Problem 22 as written, or as a same-paper/internal wording
issue rather than a new mathematical discovery.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2602.15525.
- `figures/open_problem_crop.png`: source statement of Problem 22.
- `code/verify_scalar_example.py`: small sanity check for the scalar
  \(V=\mathbb R\) instance.

## Verification

The proof is analytic. The scalar script checks the concrete example
\([-1,1]\ni t\mapsto(t,|t|)\in\ell_\infty^2\) on a finite grid; this is only a
sanity check and not used as proof.

Bounded novelty check: local indexes were searched for arXiv:2602.15525,
`pr:boll`, `unit ball embedding`, and exact extension phrases. Web searches on
2026-06-21 for exact variants of the Problem 22 statement found the source
arXiv record and no separate later answer.

## Human Review Recommendation

Review as a literal counterexample to the extension clause in Problem 22. The
main mathematical check is the elementary identity
\[
  \max\{\|v-w\|,\ |\|v\|-\|w\||\}=\|v-w\|
\]
for \(v,w\in B_V\), using the reverse triangle inequality.
