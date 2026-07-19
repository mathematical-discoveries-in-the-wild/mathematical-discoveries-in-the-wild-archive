# Literature-Already-Answered Packet: `j=2` Santaló / many-body Blaschke-Santaló

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is a partial later-literature answer to the `j`-Santaló
program in arXiv:2203.14815. It records the `j=2` case only; the higher
`j>2` cases are not claimed solved here.

## Source Problem

- Pavlos Kalantzopoulos and Christos Saroglou, *On a `j`-Santaló
  Conjecture*, arXiv:2203.14815.
- Local PDF: `source_paper.pdf`.

The source formulates the `j`-Santaló conjecture for symmetric convex bodies
and its functional version. In the case `j=2`, the functional conjecture is
the Kolesnikov--Werner many-function Blaschke-Santaló conjecture, and the
geometric conjecture asks for

```text
prod_i |K_i| <= |B_2^n|^k
```

under the pairwise polarity condition
`S_2(x_1,...,x_k) <= binom(k,2)` for all `x_i in K_i`.

## Supporting Literature

- Shibing Chen, Yuanyuan Li, Dongmeng Xi, and Zhe-Feng Xu,
  *The many-body Blaschke-Santaló type inequality via optimal transport*,
  arXiv:2606.30579, dated July 1, 2026.
- Local PDF: `supporting_paper_2606.30579.pdf`.

The supporting paper explicitly says it proves the sharp many-body
Blaschke-Santaló type inequality proposed by Kalantzopoulos and Saroglou and,
using their geometric-functional equivalence, establishes the functional
Kolesnikov--Werner inequality.

## Literature Status

The `j=2` case is now answered. Chen--Li--Xi--Xu prove a slightly stronger
geometric theorem: origin-symmetric measurable sets of finite volume satisfying
the pairwise condition already obey the sharp product-volume bound, with
equality characterized. Their Theorem 1.2 then gives the corresponding
functional many-body Blaschke-Santaló inequality.

## Scope

- Answered: arXiv:2203.14815 Conjecture 1.2 / geometric `j`-Santaló
  conjecture in the `j=2` case.
- Answered: the functional `j=2` case, equivalently the Kolesnikov--Werner
  many-function conjecture.
- Not answered by this packet: the source paper's higher `j>2` conjectures,
  including odd or non-`j=k` cases outside the already-proved classes.
- Not original to this run: this is a literature-status identification.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered note.
- `source_paper.pdf`: original arXiv:2203.14815 paper.
- `supporting_paper_2606.30579.pdf`: later supporting paper.
- `tmp/`: LaTeX build intermediates.

## Verification And Search Notes

The run lightweight indexes were searched for `2203.14815`, `Santaló`,
`Santalo`, `j-Santalo`, `Kolesnikov Werner`, `many functions`, `Blaschke`,
`Mahler`, and related convex-geometric keywords. No exact prior packet for
arXiv:2203.14815 was found, though nearby convex-geometry off-scope triages
were present.

Web search on 2026-07-03 found arXiv:2606.30579, posted June 29, 2026. The
supporting arXiv page and PDF were checked for its explicit claims.

## Human Review Recommendation

Treat the pairwise `j=2` component of the `j`-Santaló target as already
answered by arXiv:2606.30579. Keep the higher `j` cases from arXiv:2203.14815
separate.
