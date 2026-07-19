# Literature Status: arXiv:1107.2810 Question 1

Run: `fa_banach_001`

Status: `literature_already_answered (Question 1 only)`

This packet records a literature-status match, not a new proof from the run.

## Original Problem Source

- Denka Kutzarova, Antonis Manoussakis, Anna Pelczar-Barwacz,
  *Isomorphisms and strictly singular operators in mixed Tsirelson spaces*,
  arXiv:1107.2810; J. Math. Anal. Appl. 388 (2012), no. 2, 1040--1060.
- Local PDF: `source_paper.pdf`.

In Section 3.3, "Remarks and questions", on page 27 of the local rendered
source PDF, the authors ask:

> Does there exist a space in which all subsymmetric basic sequences are
> equivalent to one basis, and that basis is not symmetric?

The same paragraph also asks a separate exactly-two-subsymmetric-bases question.
That second question is not claimed as answered in this packet.

## Supporting Answer Source

- S. J. Dilworth, D. Kutzarova, B. Sari, S. Stankov,
  *Duals of Tirilman spaces have unique subsymmetric basic sequences*,
  arXiv:2210.15744.
- Local PDF: `supporting_paper_2210.15744.pdf`.

The supporting paper cites the 2012 JMAA version of arXiv:1107.2810 as `KMP`
and says the unique non-symmetric subsymmetric basic sequence question posed
there was answered by the `Su(T*)` construction of Casazza--Dilworth--
Kutzarova--Motakis. It then gives further examples: for `1 < p < infinity`
and sufficiently small `gamma > 0`, Theorem 10 proves that every subsymmetric
basic sequence in `Ti*(p,gamma)` is equivalent to its canonical basis, and
that canonical basis is subsymmetric but not symmetric.

## Status Match

This is an exact affirmative literature answer to Question 1 from
arXiv:1107.2810. The later paper explicitly knows the source question through
its `KMP` citation, and its own Tirilman-dual theorem also supplies spaces with
the requested property.

The packet is scoped to Question 1. It does not settle Question 2 from the
same source, which asks for a space with exactly two subsymmetric bases that
are not symmetric. It also does not address the neighboring Tzafriri-space
uniform saturation or `T^(2)` containment questions.

## Search Bounds

- Cheap run indexes were searched for `1107.2810`, `mixed Tsirelson`,
  `subsymmetric basic sequences`, `exactly two subsymmetric bases`, and
  related Tsirelson/strictly singular terms.
- Local source lines around Section 3.3 of arXiv:1107.2810 were inspected to
  isolate Question 1 and Question 2.
- Exact web/literature search for the Question 1 phrasing and core keywords
  surfaced arXiv:2210.15744.
- Local source lines around the abstract, introduction, Theorem 10, and the
  bibliography of arXiv:2210.15744 were inspected to verify the source chain.

## Files

- `README.md` - this packet summary.
- `main.tex` - compact status-note source.
- `solution_packet.pdf` - rendered status note, if LaTeX rendering succeeds.
- `source_paper.pdf` - local rendered PDF of arXiv:1107.2810.
- `supporting_paper_2210.15744.pdf` - local rendered PDF of arXiv:2210.15744.
- `figures/open_problem_crop.png` - readable crop of the source questions.

## Human Review Recommendation

Verify that arXiv:2210.15744 is accepted as a separate supporting answer source
for Question 1 of arXiv:1107.2810: its bibliography identifies `KMP` as the
2012 JMAA version of the source paper, its introduction says that question was
answered, and Theorem 10 provides additional Tirilman-dual examples with a
unique non-symmetric subsymmetric basic sequence.
