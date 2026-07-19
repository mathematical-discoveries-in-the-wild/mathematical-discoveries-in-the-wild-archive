# Literature-Already-Answered Packet: `L_infty` HI Space With No Reflexive Subspace

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this packet records a later-literature answer to a future-work
problem announced in Argyros--Motakis, not a new proof from this run.

## Source Problem

- S. A. Argyros and P. Motakis, *A dual method of constructing hereditarily
  indecomposable Banach spaces*, arXiv:1504.01564.
- Local source inspected: `data/parsed/arxiv_sources/1504.01564/source.tex`.
- Source location: introduction, PDF page 2; parsed source lines 159--161.

The source paper first asks whether there is a norming-set method producing a
space with shrinking basis and no subspace with boundedly complete basis. It
then says this is directly related to the existence of a
`\mathcal L_\infty` space that is HI and has no reflexive subspace. The paper
answers the first problem and announces the second as a forthcoming result:
there exists an `\mathcal L_\infty` HI space with no reflexive subspace.

## Supporting Literature

- S. A. Argyros and P. Motakis, *The scalar-plus-compact property in spaces
  without reflexive subspaces*, arXiv:1608.01962.
- Local source inspected: `data/parsed/arxiv_sources/1608.01962/source.tex`.

The supporting paper cites arXiv:1504.01564 in its bibliography as the dual
method paper. Its abstract constructs a hereditarily indecomposable
`\mathscr L_\infty` space `X_{nr}` which contains no `c_0`, no `ell_1`, and no
reflexive subspace, and which satisfies the scalar-plus-compact property.

The theorem-level support is:

- Theorem 6.12: `X_{nr}` contains no reflexive subspace.
- Theorem 6.10: every strictly singular operator on `X_{nr}` is compact; hence
  `X_{nr}` satisfies the scalar-plus-compact property.
- The introduction explicitly states that `X_{nr}` is the first
  `\mathscr L_\infty` HI space not containing a reflexive subspace.

## Literature Answer

The source future-work/existence problem has a separate later-literature
answer. Argyros--Motakis 2016 supplies the announced
`\mathcal L_\infty` HI space with no reflexive subspace, and in fact proves the
stronger scalar-plus-compact property for it.

## Scope And Limitations

- This packet is not a new proof.
- It records the later answer to the `\mathcal L_\infty` HI/no-reflexive
  subspace existence problem connected to arXiv:1504.01564.
- The source paper's first norming-set problem is answered inside
  arXiv:1504.01564 itself and is not counted here as a separate
  literature-answer packet.
- The 2016 paper also discusses broader Bourgain/Rosenthal questions; this
  packet only records the exact 1504.01564-to-1608.01962 future-work link.

## Evidence

- `source_paper.pdf`: arXiv:1504.01564.
- `supporting_paper_1608.01962.pdf`: arXiv:1608.01962.
- `main.tex` / `solution_packet.pdf`: compact literature-status note.

## Duplicate And Viability Checks

The cheap run indexes were searched for `1504.01564`, `dual method`,
`hereditarily indecomposable`, `boundedly complete basic sequence`,
`L_infty HI space with no reflexive subspace`, `scalar-plus-compact`, and
`1608.01962`. No existing packet recorded this exact source future-work
problem. A prior attempt for arXiv:1608.01962 correctly rejected same-paper
Bourgain signals, but did not record the separate 1504.01564 source link.

## Human Review Recommendation

Treat as an explicit later-literature status packet. Do not count it as new
mathematical progress. Verify mainly that the announced "forthcoming paper" in
arXiv:1504.01564 is correctly identified with arXiv:1608.01962.
