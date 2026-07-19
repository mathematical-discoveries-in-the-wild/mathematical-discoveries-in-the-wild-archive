# Literature-already-answered packet: vector-valued Heisenberg maximal bounds

Status: `literature_already_answered`

This packet records a later-literature answer to the closing question in
Deleaval--Kriegler. It is not claimed as a new automatic-discovery proof.

## Source

- arXiv: 1703.08327
- Title: *Dimension free bounds for the vector-valued Hardy-Littlewood maximal operator*
- Authors: Luc Deleaval and Christoph Kriegler
- Local source: `data/parsed/arxiv_sources/1703.08327/source.tex`

## Target question

At the end of the source paper, the authors point to the centered
Hardy--Littlewood maximal operator on the Heisenberg group and say they do not
know whether it admits dimension-free `ell^q` or UMD-lattice-valued estimates.

## Later answer

- arXiv: 2503.15291
- Title: *Dimension free estimates for the vector-valued Hardy--Littlewood maximal function on the Heisenberg group*
- Authors: Pritam Ganguly and Abhishek Ghosh
- Local supporting source: `source_tex/supporting_2503.15291.tex`

Ganguly--Ghosh explicitly identify the Heisenberg-group analogue left open by
Deleaval--Kriegler as the motivation for their paper. Their Theorem 1.1 proves
dimension-free Fefferman--Stein `ell^q` estimates for the centered
Hardy--Littlewood maximal operator over Koranyi balls on `H^n`, with constants
independent of `n`. Their Theorem 1.2 gives the corresponding UMD Banach
lattice-valued estimate, again with constants independent of `n`.

Their concluding remarks additionally state and prove the same dimension-free
`ell^q` and UMD-lattice estimates for Hardy--Littlewood maximal averages over
Carnot--Caratheodory balls on the Heisenberg group.

## Classification

This is a complete later-literature answer to the source paper's explicit
"we do not know" signal. It belongs in `solutions/literature_already_answered/`
rather than in a new-proof lane.

## Files

- `solution_packet.pdf`: human-readable packet.
- `main.tex`: LaTeX source for the packet.
- `source_tex/supporting_2503.15291.tex`: supporting later arXiv source.
