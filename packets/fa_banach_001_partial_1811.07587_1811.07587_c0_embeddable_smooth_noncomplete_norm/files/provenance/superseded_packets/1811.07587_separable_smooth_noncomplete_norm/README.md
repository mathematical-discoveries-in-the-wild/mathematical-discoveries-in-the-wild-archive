# Partial Result: Separable Smooth Non-Complete Norms

Status: `partial_result_likely_valid`

Source paper: Daniel Azagra, Tadeusz Dobrowolski, Miguel Garcia-Bravo,
*Smooth approximations without critical points of continuous mappings between
Banach spaces, and diffeomorphic extractions of sets*, arXiv:1811.07587.

Source question: On page 13, immediately before Lemma 2.10, the authors write
that it is not known whether every infinite-dimensional Banach space with a
`C^1` equivalent norm possesses a `C^1` smooth non-complete norm. They also
note that the answer is positive for `C^k`, `k >= 2`.

Partial answer: Every separable infinite-dimensional Banach space admits a
continuous `C^\infty` smooth non-complete norm. This is stronger than the
source question in the separable subcase, since it does not require the space
to have any smooth equivalent norm.

Idea: Choose a countable norm-one family of functionals separating points and
weight it rapidly to obtain a compact injective operator
`T:X -> ell_2`. Then `|x| = ||Tx||_2` is a continuous Hilbertian norm on `X`.
It is `C^\infty` off the origin because `T` is injective, and it cannot be
complete because a compact injective operator on an infinite-dimensional
Banach space cannot be bounded below.

Limitations: This does not answer the full nonseparable question. The central
obstruction is exactly the loss of a countable separating family of
functionals.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1811.07587.
- `figures/open_question_crop.png`: crop of the source question on page 13.

