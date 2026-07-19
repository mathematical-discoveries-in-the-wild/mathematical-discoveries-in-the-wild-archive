# Literature-Already-Answered Packet: Superreflexive Delta-Point Subcases

Run: `fa_banach_001`

Result type: `literature_already_answered (partial subcase)`

Status note: this is an explicit later-literature answer to part of Question
7.7 from Martin--Perreau--Rueda Zoca, not a new construction from this run.

## Source Problem

- Miguel Martin, Yoel Perreau, and Abraham Rueda Zoca, *Diametral notions for
  elements of the unit ball of a Banach space*, arXiv:2301.04433.
- Local source inspected: `data/parsed/arxiv_sources/2301.04433/source.tex`.
- Question location: `source.tex:1753--1757`, PDF page 44.

Question 7.7 asks for isomorphic restrictions on Banach spaces containing
`\Delta`-points or other diametral notions, and in particular asks whether a
reflexive or even super-reflexive Banach space can contain `\Delta`-, super
`\Delta`-, ccs `\Delta`-, Daugavet, or super Daugavet points.

## Supporting Literature

- Trond A. Abrahamsen, Ramon J. Aliaga, Vegard Lima, Andre Martiny, Yoel
  Perreau, Antonin Prochazka, and Triinu Veeorg, *Delta-points and their
  implications for the geometry of Banach spaces*, arXiv:2303.00511.
- Local source inspected: `data/parsed/arxiv_sources/2303.00511/source.tex`.

The supporting paper explicitly cites `MPRZ` Question 7.7 and says that it
answers negatively the question whether finite-dimensional nonexistence of
`\Delta`-points extends to superreflexive spaces. Its Theorem 3.1 constructs
an equivalent renorming `Y` of `\ell_2` such that `e_1` is a super
`\Delta`-point. Its Corollary 3.6 further shows that `e_1` is a ccw
`\Delta`-point, hence a ccs `\Delta`-point.

## Literature Answer

Question 7.7 has an affirmative superreflexive subcase for the `\Delta`,
super `\Delta`, and ccs `\Delta` notions.

The supporting space `Y` is an equivalent renorming of `\ell_2`, so it is
superreflexive. In `Y`, the point `e_1` is a super `\Delta`-point and a ccw
`\Delta`-point. Since every slice is relatively weakly open, ccw `\Delta`
implies ccs `\Delta`; and super `\Delta` implies ordinary `\Delta`.

## Scope And Limitations

- This packet does not answer the Daugavet-point or super-Daugavet-point
  parts of Question 7.7. The supporting theorem explicitly says its marked
  points are not Daugavet points.
- This packet records a literature status, not an original proof from the run.
- The answer is a partial subcase of a broad multi-part question.

## Evidence

- `source_paper.pdf`: arXiv:2301.04433.
- `figures/open_problem_crop.png`: PDF page 44, Question 7.7.
- `supporting_paper_2303.00511.pdf`: arXiv:2303.00511.
- `figures/supporting_theorem_3_1_crop.png`: Theorem 3.1, giving super
  `\Delta`-points in a renorming of `\ell_2`.
- `figures/supporting_ccw_corollary_crop.png`: Corollary 3.6, upgrading the
  same points to ccw `\Delta`-points.
- `main.tex` / `solution_packet.pdf`: review packet.

## Duplicate And Viability Checks

Before promotion, the lightweight indexes were searched for `2301.04433`,
`diametral notions`, `Delta point`, `Daugavet point`, `superreflexive`,
`ccs Delta`, and related phrases. No exact packet, attempt, or proof-gap entry
covered this source question. The only nearby registry hit for arXiv:2303.00511
concerned a different weak-star `\Delta`-point question from the same
supporting paper.

Active claims were inspected by slug. No visible active claim overlapped
Question 7.7, the superreflexive renorming of `\ell_2`, or the ccs/super
`\Delta` subcase.

## Human Review Recommendation

Treat this as an explicit literature-answer packet for a partial subcase:
`yes` for superreflexive spaces with `\Delta`, super `\Delta`, and ccs
`\Delta` points; no claim for Daugavet or super Daugavet points.
