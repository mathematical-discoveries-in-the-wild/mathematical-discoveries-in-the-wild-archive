# Literature-Already-Answered Packet: `L_p` Monotonicity for `FL^p` and `a-FL^p`

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Indira Chatterji, Cornelia Drutu, Frederic Haglund, *Kazhdan and Haagerup
  properties from the median viewpoint*, arXiv:0704.3749v4.
- Local PDF: `source_paper.pdf`.
- Relevant place: Section "Current developments and open questions", first
  displayed question.

The source asks whether Corollary 3 can be generalized as follows: for every
`p >= q >= 2`, does property `FL^p` imply property `FL^q`, and does
`a-FL^q`-menability imply `a-FL^p`-menability?

## Supporting Answer Source

- Amine Marrakchi and Mikael de la Salle, *Isometric actions on Lp-spaces:
  dependence on the value of p*, arXiv:2001.02490v3.
- Local PDF: `supporting_paper_2001.02490.pdf`.
- Relevant place: Introduction, Theorem 1 and Corollary 2.

## Status

The question is answered affirmatively in later literature.

Marrakchi--de la Salle explicitly state that they are answering a question of
Chatterji--Drutu--Haglund. Their Theorem 1 proves that if a topological group
has a continuous affine isometric action on an `L_p` space, then for every
larger exponent `q` it has a continuous affine isometric action on an `L_q`
space with the orbit norm powers preserved. They then record that unbounded
actions and proper actions propagate to larger exponents.

Corollary 2 states that, for every topological group `G`, the set of exponents
admitting a continuous affine isometric `L_p` action with unbounded orbits is an
upper interval `(p_G,infty)` or `[p_G,infty)`, and the set of exponents
admitting a proper continuous affine isometric `L_p` action is likewise an
upper interval `(p'_G,infty)` or `[p'_G,infty)`.

Since `FL^p` in arXiv:0704.3749 means that every continuous affine isometric
action on an `L^p` space has bounded orbits, the complement of the unbounded
orbit set is downward closed. Hence `FL^p => FL^q` whenever `p >= q >= 2`.

Since `a-FL^p`-menability means existence of a proper continuous affine
isometric action on some `L^p` space, the upper-interval statement for proper
actions gives `a-FL^q => a-FL^p` whenever `p >= q >= 2`.

## Verification Notes

- Same-paper check: the `0704.3749` source asks the monotonicity question but
  does not answer it nearby.
- Later-source check: arXiv:2001.02490 explicitly says in the abstract that it
  answers a question by Chatterji--Drutu--Haglund, and after Corollary 2 says
  this corollary answers the question.
- Scope check: arXiv:2001.02490 states that throughout its paper an `L_p`
  space means `L_p(X,mu)` for a standard measure space. This matches the
  ordinary `L^p(X,mu)` action framework used in arXiv:0704.3749.
- Endpoint check: the original question only asks one-way monotonicity, so the
  open/closed endpoint ambiguity in the upper intervals is harmless.

## Search Bounds

- Checked run indexes for `0704.3749`, `Kazhdan and Haagerup`, `median
  viewpoint`, `FL^p`, `a-FL^p`, `fixed point spectrum`, `Drutu`, `Czuron`,
  `Lavy`, `Olivier`, `Marrakchi`, and `de la Salle`.
- Read the source around Definition 1.4 and Section "Current developments and
  open questions" in `data/parsed/arxiv_sources/0704.3749/source.tex`.
- Web searches on 2026-07-18 found the 2021 Lavy--Olivier `ell_p` fixed-point
  spectrum paper and, through its references plus the local registry, the full
  2020 Marrakchi--de la Salle answer for general `L_p` spaces.

## Limitations

This is not an original proof from the run. It resolves only the monotonicity
question in the first displayed question from Section "Current developments and
open questions" of arXiv:0704.3749. It does not settle the later question asking
whether different large `FL^p` properties are equivalent or whether arbitrary
threshold examples exist, and it does not compute the critical constants
`p_G` or `p'_G`.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: original/open-problem source.
- `supporting_paper_2001.02490.pdf`: later answer source.
- `tmp/`: LaTeX build intermediates.

## Human Review Recommendation

Check that the intended `FL^p` convention in arXiv:0704.3749 is the standard
all-`L^p(X,mu)` fixed-point/bounded-orbit convention. Under that reading,
Theorem 1 and Corollary 2 of arXiv:2001.02490 are exactly the requested
monotonicity theorem.
