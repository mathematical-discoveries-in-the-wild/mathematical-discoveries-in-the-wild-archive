# Partial Result Packet: Finite-Codimensional Invariance for Norming M-Bases

Run: `fa_banach_001`

Result type: `partial`

Status: likely valid, finite-codimensional invariance theorem and positive
finite-codimensional subcase of the heredity problem for norming Markushevich
bases.

## Source Problem

- Petr Hajek and Tommaso Russo, *Norming Markushevich bases: recent results
  and open problems*, arXiv:2402.18442.
- Local source inspected:
  `data/parsed/arxiv_sources/2402.18442/manuscript.tex`.
- Open problem: Problem 6.1, parsed source `manuscript.tex:685--691`,
  PDF page 24.

Problem 6.1 asks:

```text
Let X be a Banach space with norming M-basis and Z be a subspace of X.
Must Z admit a norming M-basis as well?
```

## Result

Let `Z` be a closed finite-codimensional subspace of a Banach space `X`.
Then `X` admits a norming M-basis if and only if `Z` admits a norming M-basis.
In particular, if `X` has a norming M-basis, then every closed
finite-codimensional subspace `Z` of `X` admits a norming M-basis.

The proof first establishes the coordinate-annihilator lemma: if `X` has a
`lambda`-norming M-basis `{e_gamma; phi_gamma}_{gamma in Gamma}`, `E` is a
finite-dimensional subspace of `span{phi_gamma}`, and

```text
W = intersection_{f in E} ker f,
```

then `W` admits a `lambda`-norming M-basis. An arbitrary finite-codimensional
`Z` is then shown to be isomorphic to such a coordinate-annihilator subspace
`W`. The reverse finite-dimensional extension direction follows by choosing a
finite-dimensional complement and adjoining a finite biorthogonal system.

## Proof Idea

For the coordinate-annihilator lemma, only finitely many coordinates occur in
`E`. Choose pivot coordinates, eliminate them, and restrict the remaining
coordinate functionals. The finite-rank correction is a continuous projection,
so the corrected vectors are fundamental; the pivot equations express the
omitted coordinate restrictions through the retained ones, preserving the
norming span.

For a general finite-codimensional `Z`, choose finitely many original basis
vectors whose quotient images form a basis of `X/Z`. Since the coordinate span
is norming, its restrictions to this finite-dimensional complement give all
linear coordinate functionals. These functionals define a coordinate model
`W`, and explicit finite-rank formulas give inverse isomorphisms `Z <-> W`.
Conversely, finite-dimensional extensions preserve norming M-bases because a
finite-dimensional complement can simply be added to the biorthogonal system,
and the resulting finite direct-sum norming subspace remains norming.

## Scope And Limitations

- This does not solve Problem 6.1 for arbitrary infinite-codimensional
  subspaces.
- This does not settle the complemented-subspace version mentioned later in
  the source paper.
- The result is independent of WLD/separability assumptions and so is not just
  a restatement of the known positive theorem for WLD subspaces quoted in the
  source paper.

## Novelty / Literature Check

Cheap run indexes had no entry for `2402.18442`, the heredity problem, or this
finite-codimensional subcase.

Bounded web searches on 2026-06-15 for exact phrases around
`norming M-basis finite codimensional`, `norming Markushevich basis finite
codimensional`, `norming M-basis hyperplane subspace`,
`norming M-bases heredity problem`, `finite-codimensional`,
`finite codimension`, `separable quotient`, and `quotient` did not reveal a
later paper answering this subcase. The search did find unrelated or broader
Markushevich-basis material, but nothing that made this packet duplicate.

## Evidence

- `source_paper.pdf`: arXiv:2402.18442.
- `figures/open_problem_crop.png`: crop of Problem 6.1 on PDF page 24.
- `main.tex` / `solution_packet.pdf`: formal statement and proof.

## Human Review Recommendation

Review as a finite-codimensional invariance result and, in particular, as a
positive finite-codimensional partial result for the heredity problem. The main
points to check are the coordinate-annihilator lemma and the finite-rank
isomorphism reducing arbitrary finite codimension to that lemma.
