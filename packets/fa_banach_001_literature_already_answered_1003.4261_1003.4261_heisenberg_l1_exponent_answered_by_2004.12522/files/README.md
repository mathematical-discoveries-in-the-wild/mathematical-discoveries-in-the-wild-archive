# Literature Answer: Heisenberg `L_1` Distortion Exponent in Naor ICM 2010

Status: `literature_already_answered`

Source/open-problem paper: Assaf Naor, *L_1 embeddings of the Heisenberg group
and fast estimation of graph isoperimetry*, arXiv:1003.4261.

Supporting answer paper: Assaf Naor and Robert Young, *Foliated corona
decompositions*, arXiv:2004.12522.

## Question Identified

In the Introduction of arXiv:1003.4261, after Theorem `ckn`, Naor says that
evaluating the supremum of exponents `c>0` for which the `L_1` distortion of
the `n x n x n` Heisenberg grid is at least `(log n)^c` remains an important
open question. The same paragraph says that `c=1/2` would be the upper limit
suggested by the known `sqrt(log n)` upper bound.

## Answer Located

Naor--Young, arXiv:2004.12522, explicitly lists `Nao10` among the sources
asking for the asymptotic evaluation of the `ell_1` distortion of word balls in
the discrete 3-dimensional Heisenberg group. Its Theorem 1.6 proves

```tex
c_{\ell_1}(\mathcal B_n) \asymp \sqrt[4]{\log n}
```

for every integer `n >= 2`. Thus the supremum exponent in the source question
is `1/4`, not `1/2`.

## Scope Notes

This packet clears only the Heisenberg `L_1` distortion exponent question in
the Introduction of arXiv:1003.4261. The later survey question about invariant
negative-type metrics on cyclic groups is a separate problem and is not answered
by this packet.

Local files:

- `supporting_paper_2004.12522.pdf`: decisive supporting paper, copied from the
  existing run packet for the same supporting theorem.
- `source_tex/source_1003.4261.tex`: parsed TeX for the source article.
- `source_tex/supporting_2004.12522.tex`: parsed TeX for the supporting paper.
- `main.tex` / `solution_packet.pdf`: compact status note.

The local arXiv source cache for `1003.4261` contains source TeX but no source
PDF; no `source_paper.pdf` is included.
