# 1102.5082 Laakso-to-tree question: dual-space subcase

Status: `literature_implied_answer (partial subcase)`

## Source Question

Mikhail I. Ostrovskii, *On metric characterizations of some classes of
Banach spaces*, arXiv:1102.5082.

In the proof of Theorem `T:LaakTree`, after proving that bilipschitz
embeddability of the Laakso space `L_omega` into a Banach space `X`
implies that `X` has a bounded `delta`-semitree, the source says:

> We do not know whether bilipschitz embeddability of `L_omega` into
> `X` implies the existence of a bounded `delta`-tree in `X`.

The source proves the corresponding tree conclusion for the infinite
diamond `D_omega` in Theorem `T:DiamTree`.

## Supporting Literature

Mikhail I. Ostrovskii, *On metric characterizations of the
Radon-Nikodym and related properties of Banach spaces*, arXiv:1302.5968.

Theorem 1.10 of the supporting paper states that a dual Banach space
does not have the RNP if and only if it admits a bilipschitz embedding
of `D_omega`.

## Identification

For dual Banach spaces, the source question has a positive answer:

1. If `L_omega` embeds bilipschitzly into `X`, then by the source
   Theorem `T:LaakTree`, `X` does not have the RNP.
2. If `X` is a dual Banach space, then by arXiv:1302.5968, Theorem
   1.10, `D_omega` embeds bilipschitzly into `X`.
3. By the source Theorem `T:DiamTree`, bilipschitz embeddability of
   `D_omega` into `X` implies that `X` contains a bounded
   `delta`-tree.

This is an agent-identified implication; the supporting paper does not
explicitly present itself as answering the sentence in arXiv:1102.5082.

## Scope

This only settles the dual-space target case.  The original question for
arbitrary Banach spaces remains open in this packet.  In particular, the
argument uses the dual-space theorem in arXiv:1302.5968 and does not
produce a direct tree from the Laakso embedding in a general Banach
space.

## Files

- `main.tex`: compact status note.
- `solution_packet.pdf`: rendered status note.
- `source_paper.pdf`: arXiv:1102.5082.
- `supporting_paper_1302.5968.pdf`: arXiv:1302.5968.
