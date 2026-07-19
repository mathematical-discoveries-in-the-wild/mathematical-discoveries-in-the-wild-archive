# Arbitrary `l1`-Sum Extension for `CWO-S`

Status: likely valid partial result for arXiv:2503.09182.

Source question: Haller--Kuuseok--Poldvere ask whether their theorem
`L_1(mu,X)` has property `CWO-S` for weakly uniformly rotund `X` remains true
when `X` is merely assumed to have property `CWO-S`; they also ask the
corresponding injective tensor-product stability question.

Result: If `(X_i)_{i in I}` is any family of Banach spaces with property
`CWO-S`, then the arbitrary `l1`-sum

```text
( direct sum_{i in I} X_i )_1
```

has property `CWO-S`. The source paper proves this for countable sums. The
new step is to reduce an arbitrary sum locally to the countable support of the
two summands representing a sphere point, use the source theorem on that
countable one-complemented summand, and absorb the off-support perturbation
equally into both decomposing vectors.

Corollary: For arbitrary purely atomic measure spaces whose finite-measure
atoms generate the `L_1` space, `L_1(mu,X)` has `CWO-S` whenever `X` has
`CWO-S`.

Scope caveat: This does not settle the non-atomic case in the source
question, and it does not settle the injective tensor-product question.

Packet contents:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:2503.09182.
- `figures/open_problem_crop.png`: crop of the source question.
- `code/crop_open_problem.py`: crop-generation script.

Novelty check: Cheap indexes and local corpus search found the source
paper's countable sum theorem and a prior partial tensor packet for
arXiv:1806.10693, but no arbitrary-index `l1`-sum packet. Bounded web searches
for arbitrary/direct `l1`-sum `CWO-S` variants found no exact match. Novelty
confidence is moderate because the argument is a short extension of the
source proposition.
