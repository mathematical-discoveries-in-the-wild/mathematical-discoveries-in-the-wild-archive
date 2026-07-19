# Literature-implied answer: partial Hilbert-matrix norm range from arXiv:2601.13672

Status: `literature_implied_answer (partial subcase)`.

Source paper: Mikael Lindstrom, Santeri Miihkinen, David Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, arXiv:2201.09591v1, published 2022-01-24.

Supporting paper: Guanlong Bao, Liu Tian, Hasi Wulan, *The norm of the Hilbert matrix operator on Bergman spaces*, arXiv:2601.13672v1, published 2026-01-20.

## Identification

The source paper records, in Section 9, "Behavior of norm and essential norm of the Hilbert matrix operator", page 22 of the arXiv PDF, that it is still open to determine the exact norm of the classical Hilbert matrix operator `H` on standard weighted Bergman spaces in the range

```text
2 + alpha < p < 2 + alpha + sqrt((2 + alpha)^2 - (sqrt(2) - 1/2)(2 + alpha)).
```

Immediately after this open-problem sentence, the source gives Theorem 9.3 and Corollary 9.4: if `H:A^p_alpha -> A^p_alpha` does not attain its norm, then the operator norm equals the essential norm, namely `pi/sin((2+alpha)pi/p)`.

The supporting paper proves Karapetrovic's conjectured norm formula on a later explicit parameter region. Its abstract and Theorem 4.1, labeled `corr` in the TeX source and appearing on page 15 of the arXiv PDF, state that if

```text
0 <= alpha <= (6p^3 - 29p^2 + 17p - 2 + 2p sqrt(6p^2 - 11p + 4))/(3p - 1)^2,
```

then

```text
||H||_{A^p_alpha} = pi/sin((alpha+2)pi/p).
```

## Scope

This is not new mathematical progress. It records a later literature theorem that answers part of the source paper's open norm problem after identifying the source's open interval with Karapetrovic's conjecture.

The answer is partial. The supporting paper itself says the conjecture was not fully settled for `alpha > 0` and `alpha+2 < p < 2(alpha+2)`, and remains open for `-1 < alpha < 0` in the corresponding strip. It improves the known positive-indexed range, especially when `alpha > 1/47` and `alpha != 1`, but it does not clear all parameters in the source's open range.

The supporting paper cites the source paper as Lindstrom--Miihkinen--Norrbo but does not frame Theorem 4.1 as an explicit answer to the source's page-22 open-problem sentence. The relation is therefore recorded as `literature_implied_answer`, not `literature_already_answered`.

## Evidence Checked

- Cheap indexes showed no prior durable row for `2201.09591` or `2601.13672`; the only nearby Hilbert-matrix rows concern a different conformally invariant-space problem for arXiv:2408.01060.
- Local source `data/parsed/arxiv_sources/2201.09591/source.tex`, lines 1554--1605.
- Local source `data/parsed/arxiv_sources/2601.13672/BTW2026arXiv.tex`, abstract lines 101--103, introduction lines 190--198, and Theorem `corr` lines 662--671.
- Local queue metadata for arXiv publication dates and abstracts.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: source paper arXiv:2201.09591.
- `supporting_paper_2601.13672.pdf`: supporting paper arXiv:2601.13672.

