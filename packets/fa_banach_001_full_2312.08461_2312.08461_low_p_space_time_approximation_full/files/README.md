# Full packet: low-p space-time shallow-network approximation

Status: candidate full result likely valid for the source's stated low-`p`
future-work line; needs human review of the pointwise sampling lemma against
the source's scaled-dictionary derivative bounds.

Source paper: Ahmed Abdeljawad and Thomas Dittrich, "Space-Time Approximation
with Shallow Neural Networks in Fourier Lebesgue spaces", arXiv:2312.08461.

Targeted future-work line: the introduction says the analysis is limited to
Bochner-Sobolev error with `p >= 2`, because the method uses a type-2 Banach
space; for `p < 2` the Bochner-Sobolev space has type `p`, and the authors
leave this line for future projects.

Result: the source's two-block shallow-network theorem extends to
`1 <= p_1 <= p_2 <= 2` with the same `N^{-1/2}` rate.  In particular, the
single-block case `1 <= p < 2` mentioned by the source is covered, including
the endpoint `p=1`.

Mechanism: the source proof already proves a uniform pointwise bound for all
relevant derivatives of the scaled neurons.  Sampling the explicit signed
measure representation of `f` and estimating the scalar pointwise sampling
error before passing through the mixed `L^{p_1}(U;L^{p_2}(V))` norm gives
`N^{-1/2}` for `1 <= p_1 <= p_2 <= 2`.  This bypasses Banach-space type
entirely in the low-`p` range.

Scope: this fully covers the specific low-`p` obstruction for the source's
same theorem.  It does not address separate future directions in the paper,
such as Bochner-Besov targets or arbitrary Bochner-Banach spaces.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2312.08461.
- `source_paper.tex`: parsed source TeX used to verify labels and passages.
- `figures/open_problem_crop.png`: crop of the source's `p<2` future-work
  passage.
- `code/make_open_problem_crop.py`: reproduces the crop.

Novelty check: local run indexes were searched for `2312.08461`, the title,
`Fourier Lebesgue`, `Bochner-Sobolev`, `type-p`, `p<2`, and neural-network
approximation terms.  Web searches on 2026-07-18 found the source and generic
related material, but no later low-`p` extension with this endpoint-inclusive
sampling argument.
