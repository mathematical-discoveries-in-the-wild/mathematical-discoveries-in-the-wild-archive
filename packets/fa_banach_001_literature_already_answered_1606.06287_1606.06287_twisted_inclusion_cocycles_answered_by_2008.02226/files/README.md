# Literature-Already-Answered Packet: Twisted Inclusion And Alternating 2-Cocycles

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this packet records that the future-work application announced in
Choi's historical note arXiv:1606.06287 was written up in the separate later
paper arXiv:2008.02226. It is not a new proof from this run.

## Source Future-Work Item

- Y. Choi, *A twisted inclusion between tensor products of operator spaces*,
  arXiv:1606.06287v2.
- Local source inspected:
  `data/parsed/arxiv_sources/1606.06287/twist-os-ptp_v4.tex`.
- Source locations: author comments added 20 May 2020; abstract; introduction
  around Theorem `t:mainthm`.

The source note proves the twisted inclusion theorem: for operator spaces `V`
and `W`, the identity map on `V tensor W` extends to a contraction
`V \widehat{\otimes} W -> V \otimes_min \widetilde W`. The abstract says that
in future work this will be applied to construct antisymmetric `2`-cocycles on
certain Fourier algebras. The author comments also say that the cocycle
application has been removed from the note and will be written separately in
fuller detail.

## Supporting Literature

- Y. Choi, *Constructing alternating 2-cocycles on Fourier algebras*,
  arXiv:2008.02226v4.
- Local source inspected:
  `data/parsed/arxiv_sources/2008.02226/Z2alt-AG-ostp_arX4.tex`.

The supporting paper's abstract says it provides the first examples of locally
compact groups whose Fourier algebras support non-zero alternating
`2`-cocycles, and identifies the twisted inclusion result for operator-space
tensor products as one of the two main technical ingredients. Its arXiv
metadata explicitly says it includes an improved version of material from
arXiv:1606.06287v2.

The theorem-level support is:

- Theorem `t:headline`: for `n >= 4` and `G` equal to `SU(n)`,
  `SL(n,R)`, or `Isom(R^n)`, there is a non-zero continuous alternating
  `2`-cocycle on `A(G)`.
- Theorem `t:twisted inclusion`: restates and proves the twisted inclusion
  result in the later paper.
- Theorem `t:mainthm`: constructs a non-zero alternating `2`-cocycle on
  `A(H x L)` from non-zero co-completely bounded derivations
  `A(H) -> A(H)^*` and `A(L) -> A(L)^*`, then transfers it to groups
  containing `H x L` as a closed subgroup.
- Theorem `t:underyournoses`: supplies the co-cb derivations needed for the
  headline examples.

## Literature Answer

The future-work application promised in arXiv:1606.06287 is answered by
arXiv:2008.02226. The latter paper gives the announced cocycle construction in
fuller detail and uses the twisted inclusion theorem as a key ingredient.

## Scope And Limitations

- This packet records a later-literature status relation, not a new result.
- The scope is the exact `1606.06287` future-work application: applying the
  twisted inclusion theorem to construct antisymmetric/alternating `2`-cocycles
  on certain Fourier algebras.
- The final section of arXiv:2008.02226 asks new follow-up questions, such as
  whether the headline theorem remains true for smaller dimensions and how to
  understand higher matrix levels of the comparison map. Those later questions
  are outside this packet and remain potential targets only if claimed
  separately.

## Evidence

- `source_paper.pdf`: arXiv:1606.06287v2, compiled from local source.
- `supporting_paper_2008.02226.pdf`: arXiv:2008.02226v4, compiled from local
  source.
- `main.tex` / `solution_packet.pdf`: compact literature-status note.

## Duplicate And Viability Checks

The cheap run indexes were searched for `1606.06287`, `twisted inclusion`,
`operator spaces`, `opposite operator space`, `2-cocycle`, `alternating
2-cocycle`, `antisymmetric 2-cocycle`, `Fourier algebras`, and
`2008.02226`. No existing durable row recorded this exact future-work answer
link.

## Human Review Recommendation

Treat as a scoped later-literature answer. Verify mainly that the author
comments and arXiv metadata correctly identify arXiv:2008.02226 as the
separate write-up promised in arXiv:1606.06287.
