# A preserved-extreme tensor counterexample

Status: `candidate_counterexample_likely_valid`

Source: Luis C. Garcia-Lirola, Guillaume Grelier, Gonzalo
Martinez-Cervantes, and Abraham Rueda Zoca, *Extremal structure of
projective tensor products*, arXiv:2211.13559, Question 3.9.

## Result

Question 3.9 has a negative answer. There is an equivalent norm on real
`ell_2` and a preserved extreme point `e_0` of its unit ball such that
`e_0 tensor e_0` is not a preserved extreme point of the projective tensor
unit ball.

The new unit ball is the closed convex hull of a half-sized Hilbert ball and
the signed points

`p_n^+ = (1-epsilon_n)e_0+e_n`,
`p_n^- = (1-epsilon_n)e_0-e_n`,

where `epsilon_n=1/(n+1)`. The coordinate functional at `e_0` weakly strongly
exposes `e_0`, so `e_0` is preserved extreme. On the other hand, take

`U_n=p_n^+ tensor p_n^+`,
`V_n=p_n^- tensor p_n^+`.

Simultaneous weak-star cluster points `U,V` belong to the bidual projective
unit ball and satisfy

`(U+V)/2=e_0 tensor e_0`.

They are distinct: the original Hilbert inner product has limiting values
`2` on `U_n` and `0` on `V_n`.

## Scope and novelty check

This fully disproves Question 3.9. It does not answer Question 3.10, concerning
whether every (preserved) extreme point of a projective tensor ball is basic.

A bounded arXiv search on 22 July 2026 used the exact source-question phrase,
the source arXiv id, and combinations of `preserved extreme`, `projective
tensor`, `counterexample`, and `weak-strongly exposed`. It found the source and
arXiv:2510.21234, which gives a different positive partial theorem, but no
counterexample or later full resolution. Novelty is plausible but not
certified.

## Packet contents

- `main.tex`, `solution_packet.pdf`: complete construction and proof.
- `source_paper.pdf`: arXiv:2211.13559.
- `figures/open_problem_crop.png`: source Question 3.9 on PDF page 13.
- `VERIFICATION.md`: mathematical, literature, and rendering checks.

Human review should focus on the slice-convergence proof for `e_0` and the
simultaneous weak-star cluster-point argument.
