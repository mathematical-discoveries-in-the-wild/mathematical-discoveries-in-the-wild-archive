# Counterexample Packet: literal `FC_alpha` stabilization can fail

Run: `fa_banach_001`

Result type: `counterexample`

Status: promoted counterexample, likely valid. This packet gives a negative
answer to the literal stabilization question in Remark 2.15 of arXiv:2406.05004.
The source's Proposition 2.13, which proves stabilization modulo a negligible
set, remains intact and is essentially sharp.

## Source Problem

- Tey Berendschot, Soham Chakraborty, Milan Donvil, Se-Jin Kim, and Mario
  Klisse, *The Choquet-Deny Property for Groupoids*, arXiv:2406.05004.
- Local source inspected: `data/parsed/arxiv_sources/2406.05004/main.tex`,
  especially Definition `HypercenterDefinition`, Proposition
  `proposition: eventually negligible`, and Remark 2.15 around lines 477--511.
- Local PDF: `source_paper.pdf`.
- Open-problem crop: `figures/open_problem_crop.png`.

The source defines a transfinite sequence `FC_alpha(G)` for a discrete Borel
field of groups. It proves that the sequence stabilizes outside a negligible
set, then remarks that it is unknown whether the sequence itself must
eventually stabilize.

## Result

There is a discrete measured field of countable groups `(G,mu)` for which the
sequence `FC_alpha(G)`, `alpha<omega_1`, does not eventually stabilize.

The counterexample can be chosen so that all non-stabilizing fibers lie in a
`mu`-null part of the unit space. Thus the measured modulo-null statement in
the source is the right level of generality.

## Construction

Let `LO` be the standard Borel space of strict linear orders on `N`. For
`L in LO`, let `M(L)` be the McLain finitary unitriangular group over `F_2`
associated with the ordered set `(N,L)`. Its elements are finite `F_2`-valued
functions on pairs `(i,j)` with `i <_L j`, with the usual finitary
unitriangular multiplication.

These groups form a discrete Borel field over `LO`: the total space is the
Borel set of pairs `(L,a)` where `a` is a finite function supported on
`<_L`-increasing pairs, and multiplication/inversion are computed by finite
formulas using the relation `<_L`.

Equip the unit space `LO` with any probability measure, for instance a point
mass at one fixed order. This gives a discrete measured field of groups.

McLain's construction realizes arbitrary infinite ordinal FC-ranks. For every
countable ordinal `xi`, there is a countable linear order `L_xi` such that
`M(L_xi)` has FC-rank `xi`; this is the McLain fact cited in the source just
before Definition 2.12/Remark 2.15.

The source recursion is fiberwise for fields of groups:

```tex
FC_alpha(G)_{L} = FC_alpha(M(L)).
```

If the global sequence stabilized at some countable ordinal `alpha`, choose
`xi>alpha` and a McLain fiber of FC-rank `xi`. In that fiber some element lies
outside `FC_alpha` but inside `FC_xi`; by the fiberwise identity this gives an
element of the global field lying in `FC_xi(G) \ FC_alpha(G)`, contradicting
stabilization.

## Verification

- `main.tex` contains the proof in manuscript form.
- `solution_packet.pdf` is the rendered counterexample note.
- No computation is used.

## Novelty Check

Local cheap indexes were searched for `2406.05004`, `FC_alpha`, McLain groups,
FC-rank, and Choquet-Deny groupoids; no prior packet for this target was found.
A bounded web search on 2026-07-19 for exact phrases around `"FC_alpha"
"discrete measured field of groups" stabilizes` and `"The Choquet-Deny
Property for Groupoids" "eventually stabilize"` found the source paper and no
later resolution of the remark.

Human-review focus: confirm the standard uniform McLain construction over
`LO` and the source-cited rank fact that McLain groups realize arbitrary
countable FC-ranks.
