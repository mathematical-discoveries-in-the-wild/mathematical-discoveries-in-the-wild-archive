# Literature-Implied Answer: Relative Expanders for Ostrovskii's Bounded-Geometry Question

Status: `literature_implied_answer (bounded-geometry version; group version remains open)`

Source paper: M. I. Ostrovskii, *Coarse embeddability into Banach spaces*,
arXiv:0802.3666.

Supporting paper: G. Arzhantseva and R. Tessera, *Relative expanders*,
arXiv:1402.1481.

## Target

In Section 2, after discussing expander obstructions to coarse Hilbert
embeddability, Ostrovskii writes that it would be very interesting to know
whether every bounded-geometry metric space that does not coarsely embed into
Hilbert space contains an expander-like substructure. He then quotes the
Gromov--Kasparov problem asking whether a finitely presented group whose
Cayley graph is not coarsely embeddable into `ell_2` must weakly contain a
family of expanders.

This packet records an answer only to the broader bounded-geometry
metric-space version.

## Identification

Arzhantseva--Tessera construct a finitely generated group `G` and a sequence
of finite-index normal subgroups `N_n` such that, for every finite generating
set `S`, the sequence of finite Cayley graphs `(G/N_n,S)`:

- has bounded degree, hence bounded geometry;
- does not coarsely embed into any `L^p`, `1 <= p < infinity`, and more
  generally not into any uniformly curved Banach space;
- admits no weakly embedded expander.

Taking the coarse disjoint union of these finite Cayley graphs gives a
bounded-geometry metric space that does not coarsely embed into Hilbert space
but has no weakly embedded expander. This is a negative answer to the
bounded-geometry version of Ostrovskii's question.

## Scope Limitations

This is not a full answer to the narrower group problem printed in
Ostrovskii's source. Arzhantseva--Tessera explicitly list as open the problem
of constructing a finitely generated group whose Cayley graph does not
coarsely embed into Hilbert space and yet has no weakly embedded expander.
Ostrovskii's quoted problem asks an even narrower finitely presented version.

The separate `ell_2` question in Section 5 of Ostrovskii's paper is already
covered in run memory by the `1207.2958_l2_not_coarsely_minimal_bls_2017`
literature packet: Baudier--Lancien--Schlumprecht arXiv:1705.06797 answer
negatively using Tsirelson's space `T^*`.

## Packet Contents

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: local copy of arXiv:0802.3666.
- `supporting_paper_1402.1481.pdf`: local copy of arXiv:1402.1481.

## Search Bounds

Cheap run indexes were searched for `0802.3666`, `Coarse embeddability into
Banach spaces`, `weakly embedded expander`, `relative expanders`, bounded
geometry non-embeddability, and `ell_2` coarse minimality. No exact packet for
arXiv:0802.3666 was present. Nearby memory covers the later `ell_2` question
and a different literal graph-tail counterexample to a final question in
arXiv:1402.1481.

Web search on 2026-06-28 found Arzhantseva--Tessera as the decisive
bounded-geometry answer and found no later settlement of the finitely
generated/finitely presented group version.

## Human Review Notes

Recommended review focus: verify that the coarse disjoint union of the
Arzhantseva--Tessera finite Cayley graphs is the intended bounded-geometry
metric-space object, and confirm that the packet's limitation excludes the
single Cayley-graph group formulation.
