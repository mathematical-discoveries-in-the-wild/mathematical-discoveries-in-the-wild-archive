# Literature-Implied Variant: dual quotient-hereditary c0 index

Status: `literature_implied_answer (strengthened dual-quotient variant; original problem still open)`

## Source Problem

- Source: S. A. Argyros, A. Manoussakis, A. M. Pelczar, *On the hereditary proximity to ell_1*, arXiv:0907.4317v2; J. Funct. Anal. 261 (2011), 1145-1203.
- Location: Remark 13.8, PDF p. 39; source line 3132 in `source_0907.4317.tex`.
- The remark asks whether, if `X` is reflexive and every subspace of `X^*` has Bourgain `c_0`-index greater than `omega^xi`, there is a subspace `Y` such that every subspace of `X/Y` has Bourgain `ell_1`-index greater than `omega^xi`.

## Supporting Literature

- Supporting theorem: R. M. Causey, *Proximity to ell_p and c_0 in Banach spaces*, arXiv:1502.05753; J. Funct. Anal. 269 (2015), 3952-4005.
- Relevant locations: Theorem 5.2 and the following quantitative paragraph, PDF pp. 27-28; Theorem 8.1 on subspace/quotient estimates, PDF pp. 46-47.
- Causey's Theorem 5.2 says that large Bourgain `c_0` structure in a dual space forces corresponding large Bourgain `ell_1` structure in any predual.

## Identification

The source problem is not fully answered by the cited theorem, because the source hypothesis is hereditary for subspaces of `X^*`, while a subspace `Z` of a quotient `X/Y` has dual

```text
Z^* = Y^\perp / Z^\perp,
```

a quotient of the annihilator `Y^\perp`, not merely a subspace of `X^*`.

However, Causey's dualization gives a clean strengthened variant:

If `Y^\perp` is quotient-hereditarily large for the Bourgain `c_0`-index, i.e. every quotient of `Y^\perp` has `c_0`-index greater than `omega^xi`, then every subspace of `X/Y` has Bourgain `ell_1`-index greater than `omega^xi`.

In particular, if every quotient of `X^*` has Bourgain `c_0`-index greater than `omega^xi`, then the original conclusion holds with `Y=0`.

## Scope Limitation

This packet does not solve Remark 13.8 as stated. The remaining missing step is a stabilization principle converting the source assumption

```text
every subspace of X^* has large c_0-index
```

into the existence of an annihilator subspace `Y^\perp` all of whose quotients have large `c_0`-index. Causey's subspace/quotient estimates are useful around this boundary, but they do not by themselves provide that hereditary quotient stabilization.

## Files

- `source_paper.pdf`: arXiv:0907.4317 PDF.
- `supporting_paper_1502.05753.pdf`: arXiv:1502.05753 PDF.
- `source_0907.4317.tex`: parsed source TeX for the open-problem paper.
- `supporting_1502.05753.tex`: parsed source TeX for the supporting paper.
- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered compact status note.

## Search Notes

Cheap run indexes had no existing entry for `0907.4317` or the final hereditary-proximity problem. Local and web searches for the exact problem phrases, `hereditary c_0-index`, `quotient Bourgain ell_1-index`, and `dualization Bourgain c_0 index` located Causey's 2015 paper. No source located in this bounded search explicitly claims to solve Remark 13.8 under the original subspace-hereditary hypothesis.
