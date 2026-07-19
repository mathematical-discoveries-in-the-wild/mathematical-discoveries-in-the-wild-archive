# Literature-Implied Partial Subcase: Finite-Dimensional Net Extensions

Status: `literature_implied_answer (partial subcase)`

Source problem paper: A. Naor, *Uniform nonextendability from nets*,
arXiv:1506.05391.

Supporting papers:

- R. J. Aliaga and R. Medina, *Lipschitz extension and Lipschitz-free spaces
  over nets in normed spaces*, arXiv:2601.03131.
- D. Freeman and C. Gartland, *Lipschitz functions on unions and quotients of
  metric spaces*, arXiv:2212.08707.

## Target

Naor proves that Rosendal's proposed net-extension property fails for some
pair of Banach spaces `X,Y`: there are Banach spaces `X,Y`, a `1`-net
`N` in `X`, and a Lipschitz map `f:N -> Y` with no uniformly continuous
extension to `X`.

After the theorem, the source paper asks for an understanding of the pairs
`X,Y` for which Rosendal's question has a positive answer, namely those pairs
for which every `Y`-valued Lipschitz map on every `1`-net `N` of `X` has a
uniformly continuous extension to `X`.

## Result

If the domain Banach space `X` is finite-dimensional, then Rosendal's
net-extension property holds for every Banach target `Y`.

More precisely, if `X` is finite-dimensional, `N` is a `1`-net in `X`, and
`Y` is any Banach space, then every Lipschitz map `f:N -> Y` has a Lipschitz,
hence uniformly continuous, extension `F:X -> Y`.

The same argument applies to any closed subset `S` of a metric ambient space
`M` when `S` has finite Nagata dimension and the relevant extension theorem
is available; for Naor's question, `S=N` is closed because a `1`-net is
uniformly discrete.

## Identification

Freeman--Gartland arXiv:2212.08707, Lemma 3.1, records that doubling metric
spaces have finite Nagata dimension and that finite Nagata dimension is
preserved under bi-Lipschitz embeddings. Finite-dimensional normed spaces,
and their subsets, are doubling after identifying the space with `R^n`.

Freeman--Gartland Lemma 3.2 states that if `Z` is a metric space and
`S subset Z` is closed with finite Nagata dimension, then there is a
weak-star continuous bounded linear extension operator
`Lip_0(S) -> Lip_0(Z)`.

Aliaga--Medina arXiv:2601.03131, Fact 2.2(c), identifies the Banach-valued
extension constant `e(S,M)` with the infimum of constants for weak-star
Lipschitz extendability. In particular, a weak-star bounded extension
operator for scalar Lipschitz functions implies that every Banach-valued
Lipschitz map on `S` extends Lipschitz to `M`, with a finite constant.

Taking `M=Z=X` and `S=N`, where `X` is finite-dimensional and `N` is any
`1`-net, gives `e(N,X)<infty`. Thus every Lipschitz map `N -> Y` into any
Banach target `Y` extends Lipschitz to `X`.

## Evidence

- `source_paper.pdf`: local copy of arXiv:1506.05391. The open question is in
  the introduction immediately after Theorem 1.
- `supporting_paper_2601.03131.pdf`: local copy of arXiv:2601.03131. Its
  introduction defines `e(S,M)` for Banach-valued extension, and Fact 2.2(c)
  gives the weak-star/free-space characterization of `e(S,M)`.
- `supporting_paper_2212.08707.pdf`: local copy of arXiv:2212.08707. Lemma
  3.1 gives finite-Nagata examples; Lemma 3.2 gives the weak-star continuous
  Lipschitz extension operator from finite-Nagata closed subsets.
- `solution_packet.pdf`: compact human-readable status note built from
  `main.tex`.

## Search Bounds

Before packaging, the cheap run indexes were searched for `1506.05391`,
`Uniform nonextendability from nets`, `Rosendal`, `1-net`, `Lipschitz
extension`, `finite Nagata`, `weak* Lipschitz extendable`, and `e(S,M)`.
No prior packet or attempt for this exact finite-dimensional-domain subcase
was found. Adjacent Lipschitz-extension packets in the registry concern
different Naor/Rabani extension constants or unrelated Lipschitz-free-space
questions.

The supporting paper arXiv:2601.03131 cites Naor's arXiv:1506.05391 while
discussing nonexistence of extension operators, but it does not explicitly
frame the finite-dimensional-domain implication as an answer to Rosendal's
positive-pairs question. This packet therefore records an agent-identified
literature implication, not an original theorem and not an explicit
literature answer.

## Scope Limitations

This packet does not address the infinite-dimensional domain case. It also
does not solve the coarse-versus-uniform embeddability implications discussed
in Naor's introduction. It only records the positive Rosendal net-extension
property for finite-dimensional domains, and more generally for finite
Nagata-dimension net domains where the cited extension theorem applies.

## Human Review Notes

Recommended review focus:

- Confirm the convention that Naor's `1`-net is uniformly discrete, hence
  closed.
- Confirm that finite-dimensional normed spaces and their subsets fall under
  the doubling/finite-Nagata examples used by Freeman--Gartland.
- Confirm that Aliaga--Medina Fact 2.2(c) converts weak-star scalar extension
  operators into Banach-valued Lipschitz extension constants exactly as used
  here.
