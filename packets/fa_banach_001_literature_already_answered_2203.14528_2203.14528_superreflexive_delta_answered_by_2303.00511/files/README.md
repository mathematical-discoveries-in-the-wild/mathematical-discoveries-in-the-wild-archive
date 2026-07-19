# Literature-Already-Answered Packet: Superreflexive Spaces With `Delta`-Points

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an explicit later-literature answer to Question 6.1 of
Abrahamsen--Lima--Martiny--Perreau, not a new construction from this run.

## Source Problem

- Trond A. Abrahamsen, Vegard Lima, Andre Martiny, and Yoel Perreau,
  *Asymptotic geometry and delta-points*, arXiv:2203.14528; published as
  Banach J. Math. Anal. 16 (2022), Paper No. 57.
- Local source inspected: `data/parsed/arxiv_sources/2203.14528/source.tex`.
- Question location: `source.tex:2164--2169`.

Question 6.1 asks:

```text
Do all superreflexive Banach spaces fail to contain Delta-points?
```

The paper also restates the issue at `source.tex:2450--2464` in terms of
almost `Delta`-points and asks in particular whether a renorming of `ell_2`
with almost `Delta`-points or almost Daugavet-points exists.

## Supporting Literature

- Trond A. Abrahamsen, Ramon J. Aliaga, Vegard Lima, Andre Martiny, Yoel
  Perreau, Antonin Prochazka, and Triinu Veeorg, *Delta-points and their
  implications for the geometry of Banach spaces*, arXiv:2303.00511.
- Local source inspected: `data/parsed/arxiv_sources/2303.00511/source.tex`.

The supporting paper explicitly cites `ALMP` Question 6.1 at
`source.tex:260--265` and states that it answers it negatively. In Section 3,
it defines an equivalent norm on `ell_2`, calls the resulting space `Y`, and
states Theorem 3.1:

```text
Let Y be the renorming of ell_2 above.
Both e_1 in S_Y and e_1^* in S_{Y^*} are super Delta-points,
but neither is a Daugavet point.
```

## Literature Answer

Question 6.1 has a negative answer.

Since `Y` is an equivalent renorming of Hilbert space `ell_2`, it is
superreflexive. Theorem 3.1 of arXiv:2303.00511 gives a super `Delta`-point
in `Y`, hence a `Delta`-point. Therefore not all superreflexive Banach spaces
fail to contain `Delta`-points.

The same supporting theorem also answers the source paper's `ell_2`
renorming variant positively for `Delta`-points, and even for super
`Delta`-points.

## Scope And Limitations

- This packet records a known later answer, not an original proof.
- The supporting theorem says the constructed points are not Daugavet points.
  Thus this packet does not settle the Daugavet-point part of the nearby
  almost-Daugavet question.
- Existing run packets already record the same supporting theorem as an answer
  to related questions from arXiv:2301.04433. This packet exists to connect
  the exact source arXiv id `2203.14528` and Question 6.1 to the same later
  answer.

## Evidence

- `source_paper.pdf`: arXiv:2203.14528.
- `supporting_paper_2303.00511.pdf`: arXiv:2303.00511.
- `main.tex` / `solution_packet.pdf`: compact literature-status note.

## Duplicate And Viability Checks

The cheap run indexes were searched for `2203.14528`, the source title,
`delta points`, `asymptotic geometry`, and later for `superreflexive` and
`ALMP`. No prior packet recorded `2203.14528` as the source question. Nearby
registry entries for `2301.04433;2303.00511` cover a related but distinct
source question.

## Human Review Recommendation

Treat as an explicit literature answer: negative for Question 6.1 as stated.
Do not count it as new mathematical progress.
