# Literature-Already-Answered Packet: continuous-parameter Besov KT theorem

Run: `fa_banach_001`

Result type: `literature_already_answered`

Status: a separate companion/later paper proves the continuous-parameter
version of the Besov-calculus Katznelson-Tzafriri theorem that arXiv:2204.13411
records as undetermined. This packet records literature status only; it is not
an original proof from the run.

## Original Problem Source

- C. Batty and D. Seifert, *Some developments around the
  Katznelson-Tzafriri theorem*, arXiv:2204.13411; published as Acta Sci. Math.
  (Szeged) 88 (2022), 53--84.
- Local source lines inspected: `data/parsed/arxiv_sources/2204.13411/source.tex`,
  lines 701--704.
- Local PDF: `source_paper.pdf`, if download succeeds.

In Section 5.1, after discussing the Besov algebra `B(C_+)` and the
continuous-parameter calculus for generators of bounded `C_0`-semigroups, the
survey says that one can formulate a continuous-parameter version of the
discrete Besov theorem (Theorem 2.7 / `BSthm`), but that the authors had not
yet determined whether it is true.

## Supporting Answer Source

- C. Batty and D. Seifert, *A continuous-parameter Katznelson-Tzafriri theorem
  for algebras of analytic functions*, arXiv:2204.13416; published in Studia
  Math. 270 (2023), 229--239.
- Local source lines inspected:
  `data/parsed/arxiv_sources/2204.13416/source.tex`, lines 129--130,
  155--166, 210--214, and 335--341.
- Local PDF: `supporting_paper_2204.13416.pdf`, if download succeeds.

## Status Match

The supporting paper states in its abstract that it proves a
continuous-parameter version of the recent discrete Katznelson-Tzafriri
theorem for power-bounded operators with bounded analytic Besov calculus. Its
introduction cites the survey as `BS21` and says that after the discrete paper
was written the authors were able to prove the corresponding
continuous-parameter result.

Theorem 1.2 (`KTB`) of arXiv:2204.13416 proves the Besov case: if `-A`
generates a bounded `C_0`-semigroup `(T(t))`, `A` has a bounded `B`-calculus on
the right half-plane, and `f in B` vanishes on `sigma(A) cap iR` and at
infinity, then `||T(t) f(A)|| -> 0`. Theorem 2.1 (`KTA`) proves a larger
algebra version where `f` lies in the closure of Laplace transforms in the
chosen algebra.

## Scope Limitations

This clears the specific survey signal at arXiv:2204.13411, Section 5.1: the
continuous-parameter analogue of the discrete analytic-Besov theorem. The
supporting theorem includes the necessary vanishing-at-infinity/closure
hypothesis, which the supporting authors explain is natural and needed in the
unbounded-generator setting. This packet does not claim any result beyond the
scope of arXiv:2204.13416.

## Verification Notes

- Same-paper check: arXiv:2204.13411 records the continuous-parameter Besov
  question as undetermined and does not answer it there.
- Separate-source check: arXiv:2204.13416 is a distinct paper with the same
  authors, cites the survey as `BS21`, and explicitly proves the
  continuous-parameter theorem.
- Local duplicate check: the lightweight indexes had no exact durable packet
  for arXiv:2204.13411 or arXiv:2204.13416 before this packet.
- External check: web search for the exact title returned arXiv:2204.13416 and
  its abstract, matching the local source.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf`: original survey/open-problem source, if available.
- `supporting_paper_2204.13416.pdf`: decisive supporting answer source, if
  available.

## Human Review Recommendation

Verify the exact source chain:

1. arXiv:2204.13411, Section 5.1, lines 701--704, isolates the undetermined
   continuous-parameter analogue of Theorem 2.7.
2. arXiv:2204.13416, abstract and introduction, says it proves that
   continuous-parameter version.
3. Theorem 1.2 of arXiv:2204.13416 gives the precise Besov `B(C_+)` theorem,
   and Theorem 2.1 gives the larger-algebra extension.
