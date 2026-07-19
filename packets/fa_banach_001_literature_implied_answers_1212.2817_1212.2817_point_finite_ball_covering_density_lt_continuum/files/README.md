# Literature-implied answer: point-finite ball coverings below the continuum

Status: `literature_implied_answer (partial strengthened subcase)`

Source question: Fonf, Levin, and Zanco, *Covering L^p spaces by balls*,
arXiv:1212.2817, Question 1.1 asks:

```text
Which infinite-dimensional Banach spaces admit point-finite coverings by balls
(each of positive radius)?
```

## Identification

The source paper proves the negative answer for separable infinite-dimensional
Banach spaces that are both uniformly rotund and uniformly smooth, and hence
for separable infinite-dimensional `L^p(mu)`, `1<p<infty`.

De Bernardi, *A note on point-finite coverings by balls*, arXiv:2007.05242,
explicitly cites the source paper and extends this negative side:

- if `X` is infinite-dimensional, uniformly rotund and uniformly smooth, and
  `dens(X)<2^{aleph_0}`, then `X` admits no point-finite covering by open or
  closed balls of positive radius;
- any cover of such an `X` by open balls is not point-finite;
- in particular, the open-ball version of Klee's problem is negative for
  `ell_p(Gamma)`, `1<p<infty`.

## Scope

This is not a full answer to Question 1.1. The later paper explicitly leaves
open whether the density restriction can be removed, even for Hilbert spaces.
The packet records a substantial known partial answer so later lane work does
not re-derive the same density-below-continuum theorem.

## Files

- `main.tex` - compact status note.
- `solution_packet.pdf` - rendered note.
- `source_paper.pdf` - arXiv:1212.2817.
- `supporting_paper_2007.05242.pdf` - arXiv:2007.05242.
