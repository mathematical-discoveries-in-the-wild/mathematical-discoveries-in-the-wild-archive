# Partial solution packet: CH weakly discrete overcomplete set in C([0,omega_1])

## Source

- Paper: Tommaso Russo and Jacopo Somaglia, *Overcomplete sets in
  non-separable Banach spaces*
- arXiv: `1912.08690`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target question: Section 4.1 asks whether one can find an overcomplete set
  in `C([0,omega_1])` with no weak cluster point, and then asks whether,
  say under CH, overcomplete sets can be made discrete in the weak topology.
- Packet claim: assuming CH, `C([0,omega_1])` contains an overcomplete set
  with no weak cluster point. In fact the construction gives a weakly
  closed-discrete overcomplete set.

This is a full answer to the highlighted `C([0,omega_1])` example under CH,
but it does not settle the ZFC version or the corresponding question for all
non-WLD Banach spaces.

## Proof Intuition

Let `u_alpha=1_[0,alpha]` in `C([0,omega_1])`. The family of small norm balls
around the `u_alpha`'s is weakly locally finite: any pointwise cluster of the
step functions would have a jump at a countable limit ordinal or at `omega_1`,
so it cannot be a continuous function. Under CH, enumerate all hyperplanes of
`C([0,omega_1])` as `(H_alpha)_{alpha<omega_1}`. Pick
`x_alpha` inside the small ball around `u_alpha`, while avoiding all earlier
hyperplanes. The hyperplane avoidance makes every uncountable subfamily
linearly dense; the small-ball localization keeps the set weakly
closed-discrete.

## Files

- `main.tex`: LaTeX source for the packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_question_page10_crop.png`: crop showing the source question.
- `code/crop_open_question.py`: reproduces the crop.
- `tmp/`: LaTeX build output.

## Verification Notes

The proof is set-theoretic and functional-analytic; no computational verifier
is needed. The main review point is Lemma 1 in the packet: small norm
neighborhoods of the clopen initial-segment indicators form a weakly locally
finite family. Once this is checked, the CH hyperplane-avoidance argument is
the same mechanism as Russo--Somaglia Theorem 3.1, with the extra localization
constraint.

Bounded novelty check: cheap run indexes had no exact `1912.08690` packet or
attempt. A later paper of Koszmider, arXiv:2006.00806, proves the stronger
background existence fact that `C([0,omega_1])` has overcomplete sets in ZFC.
The present packet is therefore not novel for existence. Its candidate new
content is the added weak-topological strengthening: under CH the
overcomplete set can be chosen with no weak cluster point, indeed weakly
closed-discrete. Local and web phrase searches for `weak cluster point`,
`weakly discrete`, and the exact `C([0,omega_1])` overcomplete-set question did
not reveal an obvious existing answer to this strengthening.
