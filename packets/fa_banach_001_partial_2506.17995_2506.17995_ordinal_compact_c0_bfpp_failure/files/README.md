# Ordinal compacta give negative C(K,p) BFPP examples

Status: likely valid partial result, pending human review.

Source paper: Antonio Aviles, Maria Japon, Christopher Lennard, Gonzalo Martinez-Cervantes, Adam Stawski, "The ball fixed point property in spaces of continuous functions", arXiv:2506.17995.

Question addressed: final Question (i) asks whether there exists an infinite compact space `K` and a non-isolated point `p in K` such that

```text
C(K,p) = {f in C(K): f(p)=0}
```

has the ball fixed point property.

Partial result:

For every nonzero limit ordinal `kappa`, with `K=[0,kappa]` and `p=kappa`, the space `C(K,p)=C_0([0,kappa))` fails the BFPP.  The fixed-point-free map on the unit ball is explicit:

```text
(Tf)(0) = 1,
(Tf)(alpha+1) = f(alpha),
(Tf)(lambda) = f(lambda)       for nonzero limit lambda < kappa,
(Tf)(kappa) = 0.
```

It is nonexpansive and maps the unit ball into itself.  A fixed point would be identically `1` on `[0,kappa)`, contradicting continuity and the condition `f(kappa)=0`.

In particular, for every uncountable regular cardinal `kappa`, the endpoint `kappa` is a non-isolated `P`-point of `[0,kappa]`, but `C([0,kappa],kappa)` still fails BFPP.

Files:

- `main.tex`: full write-up.
- `solution_packet.pdf`: rendered partial-result packet.
- `source_paper.pdf`: local copy of the source paper.
- `figures/open_question_i_crop.png`: crop of the source final questions.
- `code/render_open_problem_crop.py`: regenerates the crop.

Novelty checks:

- Cheap run indexes were searched for arXiv `2506.17995`, BFPP, ball fixed point property, `C(K,p)`, `P-point`, and spaces of continuous functions. No exact prior packet or attempt for this source target was found.
- A bounded web search on 2026-06-14 for exact BFPP / `C(K,p)` / `ell_infty/c_0` phrases found the source paper and no later explicit answer to the final questions.

Human review recommendation:

Check the continuity of the shift map at limit ordinals and at the endpoint `kappa`; that is the only real proof point.
