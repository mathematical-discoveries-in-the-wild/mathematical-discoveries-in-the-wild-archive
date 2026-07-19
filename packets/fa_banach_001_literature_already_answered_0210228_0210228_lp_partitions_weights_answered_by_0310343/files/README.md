# `L_p` and partition-and-weight norms

Status: `literature_already_answered`

Source/open-problem paper: Dale E. Alspach and Simei Tong,
*Subspaces of `L_p`, `p>2`, Determined by Partitions and Weights*,
arXiv:math/0210228.

Supporting answer paper: Dale E. Alspach and Simei Tong,
*Subspaces of `L_p`, `p>2`, with unconditional bases have equivalent
partition and weight norms*, arXiv:math/0310343.

## Identification

In the final "Remarks and Open Problems" section of arXiv:math/0210228,
Alspach and Tong ask:

> Is `L_p` isomorphic to a space with norm given by partitions and weights?

The later note arXiv:math/0310343 answers this question affirmatively for the
same range `2<p<infty`. Its main theorem states that every subspace of `L_p`
with an unconditional basis has an equivalent norm given by partitions and
weights. The immediately following corollary states that `L_p[0,1]`,
`2<p<infty`, has an equivalent norm given by partitions and weights.

Since the Haar system is an unconditional basis of `L_p[0,1]` for
`1<p<infty`, the corollary gives exactly the requested sequence-space
realization up to isomorphism in the paper's `p>2` setting.

## Scope

This packet records only the answer to the `L_p` question in the source
paper's open-problems list. It does not resolve the separate envelope-property
question, the general necessary-and-sufficient-condition problem, the tensor
product question, the transfinite `X_p^alpha` versus `R_p^alpha` problem, or
the best-constants question for the alternate Rosenthal inequality.

## Search Evidence

Lane 6 selected arXiv:math/0210228 from the sparse deterministic queue. Cheap
run indexes were searched for `0210228`, title words, `partitions and
weights`, `envelope property`, `X_p^alpha`, `R_p^alpha`, and Rosenthal
keywords; no duplicate packet for this source was found. A local full-source
search for the named constructions and exact open-problem phrases found
arXiv:math/0310343, whose abstract, theorem, and corollary directly answer
the `L_p` question.

## Files

- `source_paper.tex` and `source_paper.pdf`: cached TeX source for
  arXiv:math/0210228 and a local PDF build from that source.
- `supporting_paper_0310343.tex`, `supporting_paper_0310343.bbl`, and
  `supporting_paper_0310343.pdf`: cached TeX source, bibliography, and local
  PDF build for arXiv:math/0310343.
- `main.tex` and `solution_packet.pdf`: compact literature-status note.
