# Literature-Already-Answered Packet: Diameter 2 Property Separations

Run: `fa_banach_001`

Agent: `agent_super_00`

Result type: `literature_already_answered`

Status note: this is not a new result from the run. It records that the
main separation question and the strong-D2P stability question raised in
arXiv:1304.7068 were answered in separate literature.

## Source Problem

- Trond A. Abrahamsen, Vegard Lima, Olav Nygaard, *Remarks on diameter 2
  properties*, arXiv:1304.7068; J. Convex Anal. 20 (2013), 439--452.
- Local PDF: `source_paper.pdf`.
- Exact locations: Definition 1.1 and the paragraph after it; Section 4,
  "Some concluding remarks and questions", items (a)--(e).

The source defines the local diameter 2 property, the diameter 2 property,
and the strong diameter 2 property. It says that it is not known whether any
of the reverse implications between these properties hold, conjectures that
the three properties are not equal, and asks in item (c) whether Theorem 3.2
-- stability of the local/D2P properties under all `ell_p` sums -- is true for
the strong diameter 2 property.

## Supporting Literature

- Julio Becerra Guerrero, Gines Lopez-Perez, Abraham Rueda Zoca, *Big slices
  versus big relatively weakly open subsets in Banach spaces*, arXiv:1304.4397;
  later J. Math. Anal. Appl. 428 (2015), 855--865.
- Local PDF: `supporting_paper_1304.4397.pdf`.
- Exact locations: introduction; Theorem 2.4 and Corollary 2.5; final
  discussion of strong D2P versus D2P.

This paper explicitly says that it answers negatively an open problem stated
in Abrahamsen--Lima--Nygaard. In its notation, `SD2P` means slice diameter 2
property, which is the same as local D2P in arXiv:1304.7068, not the strong
diameter 2 property.

- Rainis Haller, Johann Langemets, Rihhard Nadel, *Stability of average
  roughness, octahedrality, and strong diameter two properties of Banach spaces
  with respect to absolute sums*, arXiv:1702.03140.
- Local PDF: `supporting_paper_1702.03140.pdf`.
- Exact location: Theorem 3.3, labeled in the source as
  `thm: absolute sum has SD2P`.

This later paper gives a complete absolute-sum criterion: if `X` and `Y` have
the strong diameter 2 property and `N` is an absolute normalized norm on
`R^2`, then `X \oplus_N Y` has the strong diameter 2 property if and only if
`(R^2,N)` has the positive strong diameter 2 property.

## Literature Status

The broad separation question is already answered negatively:

- local D2P does not imply D2P. In arXiv:1304.4397, every Banach space
  containing an isomorphic copy of `c_0` is equivalently renormed so every
  slice of the unit ball has diameter 2 while some non-empty relatively weakly
  open subsets have arbitrarily small diameter.
- D2P does not imply strong D2P. The same supporting paper records that
  `c_0 \oplus_2 c_0` has D2P and fails strong D2P, citing the Acosta--Becerra
  Guerrero--Lopez-Perez result.

The source item (c) is also answered negatively for the literal all-`ell_p`
strong-D2P extension: the example `c_0 \oplus_2 c_0` consists of two spaces
with strong D2P, has D2P by the source Theorem 3.2, but fails strong D2P.
The 2017 Haller--Langemets--Nadel theorem supplies the broader absolute-sum
criterion.

## Scope Limitations

This packet clears the main "are the three properties different?" question
and the strong-D2P version of the `ell_p`-sum stability question in item (c).
It does not claim to answer source items (a), (b), (d), or (e), except where
they overlap with the cited absolute-sum theorem.

## Files

- `README.md`: this summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1304.7068.
- `supporting_paper_1304.4397.pdf`: arXiv:1304.4397.
- `supporting_paper_1702.03140.pdf`: arXiv:1702.03140.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Treat this as already answered in the literature. Future agents should not
try to solve the main D2P-separation question or the literal strong-D2P
`ell_p` stability question from arXiv:1304.7068 as new targets, but the
remaining concluding questions in that paper should not be marked closed by
this packet.
