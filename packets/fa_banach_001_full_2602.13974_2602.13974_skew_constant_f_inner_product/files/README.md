# Full Answer: The Skew Constant F Characterizes Inner Product Spaces

## Source Problem

- Source paper: J. Qi, Q. Li, Z. Yin, Q. Liu, J. Bi, Y. Fu, and Y. Li, *Generalized geometric constants related to Birkhoff orthogonality in Banach spaces*, arXiv:2602.13974.
- Location: final open questions, Problem 2.
- Problem signal: the authors propose
  `F(X)=sup_{t>0}{(||x+t y||-||t x+y||)/2 : x,y in S_X}`
  as a way to improve the proof of their Lemma 6/Ficken inner-product characterization.

## Result

For every real normed space `X` with dimension at least two,
`0 <= F(X) <= 1`, and

`F(X)=0` if and only if `X` is an inner product space.

Thus the proposed constant gives exactly the desired skew-equality characterization: its vanishing is equivalent to the Ficken condition used in the source paper.

## Idea of the Proof

Swapping `x` and `y` changes the sign of the displayed difference, so `F(X)` is one half of the supremum of the absolute skew defect
`|||x+t y||-||t x+y|||`. If `F(X)=0`, both orientations force equality
`||x+t y||=||t x+y||` for all unit `x,y` and all `t>0`. Replacing `y` by `-y` gives the same equality for negative `t`. Homogeneity then gives Ficken's equality for all equal-norm vectors, so the norm is induced by an inner product. The converse is immediate from the parallelogram computation in an inner product space.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: rendered source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source problem.
- `code/make_crop.py`: reproducible crop script.
