# Literature-Already-Answered Packet: Fixed Point Spectrum for `L_p` Actions

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Piotr W. Nowak, *Group Actions on Banach Spaces*, arXiv:1302.6609.
- Local PDF: `source_paper.pdf`.
- Relevant page: page 10.

Section 3.5 defines

```text
F(G) = { p in (1,infty) : H^1(G,pi)=0 for every isometric representation
         pi on an L_p-space }
```

and asks, for finitely generated property-(T) groups:

- Problem 14 (C. Drutu): is `F(G)` connected?
- Problem 15: is there a critical value `p>2` such that `F(G)=(1,p)`?

## Supporting Answer Source

- Amine Marrakchi and Mikael de la Salle, *Isometric actions on Lp-spaces:
  dependence on the value of p*, arXiv:2001.02490.
- Local PDF: `supporting_paper_2001.02490.pdf`.
- Relevant pages: pages 1-2.

## Status

The connectedness question and the critical-value question are answered by
arXiv:2001.02490.

Marrakchi--de la Salle prove that, for every topological group `G`, the set of
exponents `p` for which `G` admits an affine isometric action on an `L_p` space
with unbounded orbits is an interval of the form `(p_G,infty)` or
`[p_G,infty)`. They also record that, for second countable locally compact
property-(T) groups, `p_G>2` and there is such an action at `p=p_G`.

For `1<p<infty`, `L_p` is reflexive, and the source paper already recalls that
bounded orbits yield fixed points. Equivalently, an affine isometric action on
an `L_p` space has a fixed point exactly when its orbits are bounded in the
range relevant here. Thus Nowak's fixed point spectrum is the complement of
the unbounded-orbit interval inside `(1,infty)`.

Consequently, for every finitely generated property-(T) group covered by
Nowak's Problems 14 and 15,

```text
F(G) = (1,p_G)
```

for a critical value `p_G>2`. In particular `F(G)` is connected.

## Verification Notes

- Same-paper check: arXiv:1302.6609 states Problems 14 and 15 as open on
  page 10.
- Later-source check: arXiv:2001.02490 states in its abstract that it answers a
  question of Chatterji--Drutu--Haglund, and on page 2 says Corollary 2 answers
  the question sometimes referred to as Drutu's conjecture.
- Scope check: finitely generated discrete groups are second countable locally
  compact groups, so the endpoint statement quoted on page 2 of the supporting
  paper applies to the property-(T) groups in Nowak's question.
- Identification check: Nowak formulates the spectrum in cohomological/fixed
  point language, while Marrakchi--de la Salle formulate the result in
  unbounded-orbit language. For `1<p<infty`, these are equivalent for affine
  isometric actions on `L_p` spaces.

## Search Bounds

- Checked the run registry, solution index, attempt index, and proof-gap index
  for `1302.6609`, `Group actions on Banach spaces`, `fixed point spectrum`,
  `Drutu`, `critical value`, and related `L_p`/property-(T) terms.
- Read the parsed source around Section 3.5 in
  `data/parsed/arxiv_sources/1302.6609/handbook-arxi.tex`.
- Web literature search located arXiv:2001.02490 and neighboring results on
  `L_p` fixed point spectra and affine isometric actions.
- Downloaded the current arXiv PDF for arXiv:2001.02490 and inspected pages
  1-2.

## Limitations

- This is not an original proof from the run.
- This packet answers the structural spectrum questions, Problems 14 and 15.
  It does not compute `p_G` for a particular group.
- It does not address the other questions in arXiv:1302.6609, such as the
  `\tilde A_2` spectrum question, uniformly bounded Hilbert representations,
  reduced `l_p` cohomology, Yu's question, or Nica's mapping-class-group
  conjecture.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact review packet source.
- `solution_packet.pdf`: rendered packet, if LaTeX rendering succeeds.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2001.02490.pdf`: later answer source.
- `tmp/`: local render intermediates.

## Human Review Recommendation

Check the final equivalence step between `H^1(G,pi)=0` for all isometric
representations on `L_p` and fixed points/bounded orbits for affine isometric
actions. This is standard for `1<p<infty` and is also stated in the supporting
paper, but it is the only translation between the two formulations.
