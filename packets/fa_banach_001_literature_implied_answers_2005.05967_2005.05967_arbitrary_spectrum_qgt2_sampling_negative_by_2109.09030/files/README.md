# Literature-Implied Answer: Arbitrary-Spectrum `q>2` Sampling Is Not `N polylog N`

## Source Question

- Source paper: V. N. Temlyakov, *Sampling discretization of integral norms of the hyperbolic cross polynomials*, arXiv:2005.05967.
- Location: Section 4, Open problem 3, lines 682-690 in the parsed source.
- Question: for each `q in (2,infty)` and `d`, whether every finite spectrum `Q subset Z^d` satisfies a Marcinkiewicz discretization theorem for `Tr(Q)` with only `|Q| polylog |Q|` sampling points.

## Status

`literature_implied_answer`.

The later paper F. Dai and V. N. Temlyakov, *Sampling discretization of integral norms and its application*, arXiv:2109.09030, records in Remark 1.2 (`AR2` in the TeX) a lacunary lower bound: for a lacunary set `Lambda_n` of `n` frequencies and every fixed `p>2`, `Tr(Lambda_n) in M(m,p,C1,C2)` forces

`m >= c(p,C1,C2) n^{p/2}`.

Taking `p=q>2`, `d=1`, and `Q=Lambda_n` contradicts the hoped-for `n (log n)^c` sufficient bound for large `n`. Thus Open problem 3 has a negative answer.

## Scope

- This answers Open problem 3 from arXiv:2005.05967.
- It does not answer the hyperbolic-cross near-linear sampling Open problem 1.
- It does not settle Open problem 2 on improving the logarithmic entropy exponent.
- The answer is literature-implied: arXiv:2109.09030 states the lower bound, and the contradiction with the 2005 open problem is immediate.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.tex`: local parsed TeX for arXiv:2005.05967 when available.
- `supporting_paper_2109.09030.tex`: local parsed TeX for arXiv:2109.09030 when available.
