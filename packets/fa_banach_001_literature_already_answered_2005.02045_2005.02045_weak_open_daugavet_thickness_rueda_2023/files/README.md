# Literature-Already-Answered Packet: Weakly Open Daugavet Thickness Question

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status note: this is an explicit later-literature negative answer to Question
`(b)` / Remark 3.9 from Haller--Langemets--Lima--Nadel--Rueda Zoca, not a new
construction from this run.

## Source Problem

- Rainis Haller, Johann Langemets, Vegard Lima, Rihhard Nadel, and Abraham
  Rueda Zoca, *On Daugavet indices of thickness*, arXiv:2005.02045.
- Local source inspected: `data/parsed/arxiv_sources/2005.02045/source.tex`.
- Question location: `source.tex:1184--1196`, PDF page 16; the follow-up
  status sentence is `source.tex:1399--1400`, PDF page 18.

Question `(b)` asks whether, for every Banach space `X`,
`\mathcal T(X) >= 1` implies that every nonempty relatively weakly open subset
of `B_X` has diameter two. The source paper states in Remark 3.9 that this
question remains open.

## Supporting Literature

- Abraham Rueda Zoca, *Diameter, radius and Daugavet index of thickness of
  slices in Banach spaces*, arXiv:2306.01467.
- Local source inspected: `data/parsed/arxiv_sources/2306.01467/source.tex`.

The supporting paper explicitly identifies the same question from
`[7, Remark 3.9]` and says it is precisely one of the questions addressed.
Its Theorem 1.2 and Remark 4.4 give the negative answer: for every
`\varepsilon>0` there is a Banach space `X` with
`\mathcal T(X)>2-\varepsilon` that still contains slices of diameter strictly
smaller than two.

## Literature Answer

Question `(b)` has a negative answer.

Indeed, choose `0<\varepsilon<1` in the supporting theorem. Then the produced
renormed Banach space has `\mathcal T(X)>2-\varepsilon>1`, but its unit ball
has a slice of diameter strictly smaller than two. A slice of `B_X` is a
nonempty relatively weakly open subset of `B_X`, so the conclusion asked in
Question `(b)` fails.

## Scope And Limitations

- This packet addresses only Question `(b)` from the Ivakhno-related list in
  arXiv:2005.02045.
- The source paper itself already answered Question `(a)` negatively and
  Question `(c)` negatively; those same-paper answers are extraction false
  positives and are not repackaged here.
- The still-open `\ell_1`-sum equalities for `\mathcal T` and
  `\mathcal T^{cc}` in Question `\ref{ques: 1-sum}` are not addressed.
- This packet records a literature status, not an original proof from the run.

## Evidence

- `source_paper.pdf`: arXiv:2005.02045.
- `figures/open_problem_crop.png`: PDF page 16, the list containing Question
  `(b)`.
- `supporting_paper_2306.01467.pdf`: arXiv:2306.01467.
- `figures/supporting_answer_crop.png`: PDF page 16 of the supporting paper,
  Remark 4.4 explicitly giving the negative answer.
- `main.tex` / `solution_packet.pdf`: review packet.

## Duplicate And Viability Checks

Before promotion, the lightweight indexes were searched for `2005.02045`,
`Daugavet index`, `Daugavet indices of thickness`, `weakly open`,
`Ivakhno`, `Rueda`, `oplus_1`, and related thickness-index phrases. No
existing packet or attempt covered this exact weakly-open question.

Nearby local papers were inspected. arXiv:2306.01467 explicitly answers the
weakly-open Question `(b)`. arXiv:2307.10647 and arXiv:2301.04433 are adjacent
Daugavet/Delta-point literature but do not supersede this exact status
identification.

## Human Review Recommendation

Treat this as an explicit literature-answer packet: negative answer to the
weakly-open Daugavet-index-of-thickness question. The main review check is the
simple implication from the supporting theorem's large `\mathcal T^{cc}` bound
to large `\mathcal T`, and the observation that the small slice is a relatively
weakly open subset.
