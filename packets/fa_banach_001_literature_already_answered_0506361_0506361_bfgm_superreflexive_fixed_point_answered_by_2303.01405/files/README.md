# Literature-Already-Answered Packet: BFGM Superreflexive Fixed-Point Conjecture

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this packet records an explicit later-literature answer to
Conjecture 1.6 of Bader--Furman--Gelander--Monod, not a new proof from this
run.

## Source Problem

- Uri Bader, Alex Furman, Tsachik Gelander, and Nicolas Monod,
  *Property (T) and rigidity for actions on Banach spaces*,
  arXiv:math/0506361.
- Local source inspected: `data/parsed/arxiv_sources/0506361/source.tex`.
- Conjecture location: `source.tex:477--481`, label
  `C:higherrankFB`.

The source conjecture asks whether the higher rank groups considered in
Theorem B of the paper, and their lattices, have property
`\bar F_B`, and hence `\bar T_B`, for every superreflexive Banach space `B`.

## Supporting Literature

- Tim de Laat and Mikael de la Salle,
  *Actions of higher rank groups on uniformly convex Banach spaces*,
  arXiv:2303.01405.
- Local source inspected: `data/parsed/arxiv_sources/2303.01405/source.tex`.

The supporting paper explicitly identifies the source problem. Its
introduction says that Bader--Furman--Gelander--Monod conjectured a stronger
statement and that the paper proves it. The statement is Theorem A, cited as
`\cite[Conjecture 1.6.]{MR2316269}`, at `source.tex:80--82`:

```text
Higher rank groups and their lattices have property F_E for every
super-reflexive Banach space E.
```

The proof appears in Section 7 at `source.tex:1259--1268`. It combines the
paper's Archimedean theorem with Lafforgue--Liao strong Banach property (T) in
the non-Archimedean case, and notes that BFGM Proposition 2.13 makes the
original `\bar F_E` formulation equivalent to Theorem A's `F_E` formulation.

## Literature Answer

Conjecture 1.6 of arXiv:math/0506361 has an affirmative answer in the later
literature.

The supporting authors explicitly knew they were proving the BFGM conjecture:
the theorem is labeled as BFGM Conjecture 1.6, the abstract says the result
confirms a long-standing conjecture of Bader--Furman--Gelander--Monod, and
the final proof checks both Archimedean and non-Archimedean higher rank
factors before passing to lattices.

## Scope And Limitations

- This is not an original solution packet from the run.
- The answer covers the source conjecture's higher rank groups and their
  lattices for all superreflexive Banach spaces, via the equivalence between
  the original barred fixed-point property and the unbarred property recorded
  by BFGM Proposition 2.13.
- No part of this exact source conjecture remains open within the stated
  scope, according to the supporting paper.

## Evidence

- `source_paper.pdf`: arXiv:math/0506361.
- `supporting_paper_2303.01405.pdf`: arXiv:2303.01405.
- `main.tex` / `solution_packet.pdf`: compact literature-status note.

## Duplicate And Viability Checks

The cheap run indexes were searched for `0506361`, `2303.01405`, the source
title, `Bader Furman Gelander Monod`, `Conjecture 1.6`, `higher rank groups`,
`superreflexive`, and fixed-point/property `(F_B)` keywords. No existing run
packet recorded this exact source conjecture or the later answer.

## Human Review Recommendation

Treat as an explicit literature answer: affirmative for BFGM Conjecture 1.6
as stated. Do not count it as new mathematical progress.
