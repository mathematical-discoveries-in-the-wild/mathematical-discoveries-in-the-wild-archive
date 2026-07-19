# Consolidated Partial Result: Smooth Non-Complete Norms

Status: `partial_result_likely_valid`

Source paper: Daniel Azagra, Tadeusz Dobrowolski, Miguel Garcia-Bravo,
*Smooth approximations without critical points of continuous mappings between
Banach spaces, and diffeomorphic extractions of sets*, arXiv:1811.07587.

Source question: On page 13, immediately before Lemma 2.10, the authors write
that it is not known whether every infinite-dimensional Banach space with a
`C^1` equivalent norm possesses a `C^1` smooth non-complete norm. They also
note that the answer is positive for `C^k`, `k >= 2`.

Consolidated partial answer:

- Every separable infinite-dimensional Banach space admits a continuous
  `C^\infty` smooth non-complete norm, by pulling back the Hilbert norm along
  a compact injective operator into `ell_2`.
- More generally, if an infinite-dimensional Banach space `X` admits a bounded
  linear injection into some `c0(Gamma)`, then `X` admits a continuous
  `C^\infty` smooth non-complete norm.
- In particular this holds for every infinite-dimensional Banach space with a
  Markusevich basis, since such spaces admit a continuous injection into
  `c0(Gamma)`. This includes the separable case.

Idea: Embed `X` into `c0(Gamma)`. On every infinite-dimensional subspace of
`c0(Gamma)`, choose a block-like sequence and damp its finite coordinate
supports by a positive diagonal multiplier. The multiplier stays injective
but is not bounded below on the image of `X`. Pulling back a known
`C^\infty` smooth equivalent norm on `c0(Gamma)` gives a smooth norm on `X`;
non-completeness follows from the open mapping theorem.

Limitations: This expands the earlier separable packet substantially, but it
does not settle the full source question. The remaining gap is the absence of
a known implication from `C^1` smooth renormability to a `c0(Gamma)` injection,
an M-basis, or enough projectional/coordinate structure to run the diagonal
argument.

Consolidation note: The older packet
`1811.07587_separable_smooth_noncomplete_norm` has been superseded by this
packet. Its proof is now summarized here as the separable subcase.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1811.07587.
- `figures/open_question_crop.png`: crop of the source question on page 13.
- `provenance/superseded_packets/1811.07587_separable_smooth_noncomplete_norm/`:
  earlier separable-only packet retained as provenance.
