# Literature-Already-Answered Packet: Schreier Strictly Singular Operators

Run: `fa_banach_001`

Result type: `literature_already_answered (partial subcase)`

Status note: this is a later-literature status packet, not a new proof from
this run.

## Source Problem

- Kevin Beanland, Tomasz Kania, Niels Jakob Laustsen, *Closed ideals of
  operators on the Tsirelson and Schreier spaces*, arXiv:1907.10645; J. Funct.
  Anal. 279 (2020), 108668.
- Local PDF: `source_paper.pdf`.
- Evidence image:
  - `figures/open_problem_crop.png` (page 22, Section 5).

For `X = X[S_n]`, the Schreier space of finite order `n >= 1`, the source
paper asks whether

```text
S(X) subset overline(G_{c0}(X)),
```

where `S(X)` is the ideal of strictly singular operators and
`overline(G_{c0}(X))` is the norm-closure of the ideal of operators factoring
through `c0`.

## Supporting Literature

- Antonis Manoussakis, Anna Pelczar-Barwacz, *Small operator ideals on the
  Schlumprecht and Schreier spaces*, arXiv:2008.12362.
- Local PDF: `supporting_paper_2008.12362.pdf`.
- Evidence images:
  - `figures/supporting_answer_setup_crop.png` (page 14, Section 4.2: explicit
    statement that the reverse inclusion fails for `N >= 2`, answering one of
    the questions of Beanland--Kania--Laustsen, while `N = 1` remains open).
  - `figures/supporting_answer_crop.png` (page 16, Corollary 4.7).

## Literature Status

The question has a known negative answer for Schreier spaces of order at least
two:

```text
S(X[S_N]) is not contained in overline(G_{c0}(X[S_N])) for every N >= 2.
```

This is Corollary 4.7 of Manoussakis--Pelczar-Barwacz. Their Section 4.2
explicitly identifies this as an answer to one of the questions of
Beanland--Kania--Laustsen and says the case `N = 1` remains open.

## Proof Idea

The later paper studies the formal identity
`R_N: X[S_N] -> X[S_{N-1}]`. Proposition 4.6 proves that `R_N` is strictly
singular and, when `N >= 2`, stays at distance at least one from every
operator that factors through `c0`. Therefore `R_N` is a strictly singular
operator that cannot belong to the closed `c0`-factorization ideal. This gives
the advertised negative inclusion.

## Limitations

- This packet only answers the `S(X) subset overline(G_{c0}(X))` question for
  finite-order Schreier spaces `X[S_N]` with `N >= 2`.
- It does not settle the case `N = 1`; the supporting paper explicitly leaves
  that case open.
- It does not answer the source paper's separate question about whether
  `overline(G_{c0}(X))` is properly contained in the intersection of all
  non-trivial spatial ideals.
- It does not answer the separate less precise question about explicit maximal
  ideals in `B(T)` or `B(X[S_n])`.

## Files

- `README.md`: this packet summary.
- `main.tex`: literature-status packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: original open-problem source.
- `supporting_paper_2008.12362.pdf`: later supporting paper.
- `figures/open_problem_crop.png`: source question crop.
- `figures/supporting_answer_setup_crop.png`: supporting setup and explicit
  answer-status crop.
- `figures/supporting_answer_crop.png`: supporting corollary crop.
- `tmp/`: LaTeX build intermediates and disposable page renders.

## Verification And Search Notes

Before packaging, the run lightweight indexes were searched for `1907.10645`,
the source title, `closed ideals of operators`, `Tsirelson`, `Schreier`,
`operator ideals`, and related terms. No exact prior packet or attempt was
found. Broad Tsirelson/Schreier registry hits were unrelated.

Local source search surfaced arXiv:2008.12362 as a later paper on small
operator ideals on Schreier spaces. The supporting source and PDF were checked
directly, and a web search for the exact title and core phrases confirmed the
same later-paper match.

## Human Review Recommendation

Treat the source question `S(X) subset overline(G_{c0}(X))` as already
answered negatively for `X = X[S_N]`, `N >= 2`, by arXiv:2008.12362. Keep the
order-one case and the other Section 5 questions separate.
