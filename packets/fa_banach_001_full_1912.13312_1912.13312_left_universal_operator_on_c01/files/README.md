# 1912.13312: A Left-Universal Operator on `C([0,1])`

Status: `candidate_full_solution_likely_valid`

Source paper: Joanna Garbulinska-Wegrzyn and Wieslaw Kubis,
*A note on universal operators between separable Banach spaces*,
arXiv:1912.13312.

Open question solved: after Proposition 1.3, the source states that there
exists a universal operator on `C([0,1])` and then says that the authors do not
know whether there exists a left-universal operator on `C([0,1])`.

Candidate answer: yes. Define

```text
U:C([0,1]) -> C([0,1]),     U(f)(t) = f((t+2)/3).
```

Then `||U||=1`, and `U` is left-universal for non-expansive operators into
`C([0,1])`. Given `T:X -> C([0,1])`, choose an isometric embedding
`e:X -> C([0,1])`. Put `e(x)` on the left third of `[0,1]`, put `T(x)` on the
right third, and interpolate linearly across the middle third. This gives a
linear isometric embedding `I:X -> C([0,1])` with `U I = T`.

Novelty check: local indexes contain no prior packet for arXiv:1912.13312 or
this left-universal `C([0,1])` question. Web searches on 2026-06-19 for exact
phrases around "left-universal operator" and "`C([0,1])`" surfaced the source
paper and no later explicit answer.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:1912.13312.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/make_open_problem_crop.py`: reproduces the crop.

Human review recommendation: check the piecewise embedding formula and verify
that the left third forces the norm equality `||I(x)||=||x||`.
