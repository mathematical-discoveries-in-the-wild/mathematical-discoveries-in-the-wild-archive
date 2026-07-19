# Literature-implied partial answer: `L_r` finite Lipschitz into `L_s`

status: literature_implied_answer (partial subcase)

source_arxiv: 0912.1912

supporting_arxiv: 1601.03332

source_problem: Yun, final Section 7 question asking whether, for `r,s >= 2` and `r <= s`, `L_r` finitely Lipschitz embeds into `L_s`, and furthermore whether `E(L_r,p) <=_B E(L_s,p)`

packet_verdict: negative for the finite-Lipschitz part when `2 < r < s < infinity`

## Summary

Yun asks whether `L_r` finitely Lipschitz embeds into `L_s` for `r,s >= 2`, `r <= s`. The endpoint cases `r=s` and `r=2` are not the issue: the identity handles `r=s`, and Hilbertian embeddings handle `r=2`.

For the strict super-Hilbertian range `2 < r < s < infinity`, Naor's sharp metric `X_p` theorem implies that the maximal bi-Holder exponent for embedding `L_r` into an `L_s` space is `r/s < 1`. Hence there is no bi-Lipschitz embedding of `L_r` into any `L_s` space.

Yun proves in the same source paper that finite Holder embeddability into a Banach space is equivalent to Holder embeddability into an ultrapower of that Banach space. An ultrapower of `L_s` is again an `L_s` space. Therefore a hypothetical finite Lipschitz embedding `L_r -> L_s` would give a bi-Lipschitz embedding `L_r -> (L_s)_U`, contradicting Naor's exponent bound.

## Evidence

- `source_paper.pdf`: Yun, arXiv:0912.1912.
- `supporting_paper_1601.03332.pdf`: Naor, arXiv:1601.03332.
- Source TeX locations:
  - `data/parsed/arxiv_sources/0912.1912/source.tex`, final questions around lines 1208--1262.
  - Yun's ultraproduct theorem around lines 744--785.
- Supporting theorem:
  - Naor, arXiv:1601.03332, abstract and main theorem: for `2 < q < p < infinity`, the maximal bi-Holder exponent for embedding `L_q` into `L_p` is `q/p`.

## Scope

This packet answers only the finite-Lipschitz part of Yun's final Question (1), and only in the strict range `2 < r < s < infinity`.

It does not prove or disprove the associated Borel reducibility assertion `E(L_r,p) <=_B E(L_s,p)`. It also does not address the self-Holder question `E(L_r,p) <=_B E(L_r,q)` from Yun's Question (2).

This is a literature-implied answer: Naor does not appear to identify Yun's question, but the implication follows by combining Naor's theorem with Yun's own ultraproduct characterization.

Human-review recommendation: accept as a lightweight literature-implied partial answer with the scope above preserved.
