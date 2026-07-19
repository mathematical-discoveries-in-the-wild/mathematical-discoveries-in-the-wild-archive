# Conditional Packet: WAP Pullback Reduction for Hanson Question 4.3

Run: `fa_banach_001`

Agent: `agent_lane_19`

Status: `conditional_reduction_not_full_solution`

Source target: James Hanson, *Indiscernible Subspaces and Minimal Wide Types*,
arXiv:2004.03062, Question 4.3.

## Question

Hanson asks whether model-theoretic stability implies oscillation stability:
if `T` is a stable Banach theory, is every unary formula oscillation stable
on models of `T`?

## Conditional Result

This packet isolates a pure Banach-Ramsey lemma that would imply a positive
answer to Hanson Question 4.3.

The dependency is:

> Every bounded uniformly continuous function `F` on the unit ball of an
> infinite-dimensional Banach space whose midpoint kernel
> `K_F(u,v)=F((u+v)/2)` is stable in the Grothendieck double-limit sense is
> oscillation stable on the unit sphere.

If this WAP/midpoint-stable oscillation lemma is true, then every unary formula
in every stable Banach theory is oscillation stable. The proof is complete
modulo that lemma: for any formula instance `phi(x,a)`, the formula
`theta(u,v)=phi((u+v)/2,a)` is stable because the theory is stable, so
`F(x)=phi(x,a)` satisfies the dependency.

## Why This Matters

The previous push produced a positive partial answer for Hilbert-operator
quantifier-free/QE classes. This packet is a different route: it strips the
remaining general problem down to a functional-analytic assertion about
weakly almost periodic translation data.

Literature checked in this push:

- Hanson arXiv:2004.03062, especially the Dvoretzky--Milman compactness
  construction and Question 4.3.
- Ben Yaacov arXiv:1306.5852, identifying stable formulas with
  Grothendieck relative weak compactness/definability of types.
- Shelah--Usvyatsov arXiv:1402.6513, minimal wide stable types and the
  Hilbert Morley-spine machinery.
- Chaatit arXiv:math/9602208 and Braga--Swift arXiv:1704.04468 for the
  reflexive-representation/Krivine--Maurey stable Banach-space background.
- Gowers-style oscillation-stability literature for block/Ramsey tools.

No full proof or counterexample to Hanson Question 4.3 was found in this push.
The most plausible next target is the WAP/midpoint-stable oscillation lemma
itself: either prove it using WAP/reflexive representation plus a block Ramsey
argument, or refute it with a midpoint-stable analogue of Maurey's Hilbert
sphere coloring.

## Files

- `main.tex` / `solution_packet.pdf`: conditional reduction note.
- `source_paper.pdf`: Hanson arXiv:2004.03062.
- `supporting_wap_grothendieck_1306.5852.pdf`: Ben Yaacov's Grothendieck/WAP
  stability note.
- `figures/open_problem_crop.png`: crop of Hanson Question 4.3 from the
  earlier verified packet.
