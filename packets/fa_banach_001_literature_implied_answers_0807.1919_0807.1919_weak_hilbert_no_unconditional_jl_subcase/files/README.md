# Literature-Implied Partial Answer: Weak Hilbert JL Beyond Unconditional Bases

Run: `fa_banach_001`

Result type: `literature_implied_answer (partial subcase)`

Status: later literature gives a positive weak-Hilbert Johnson-Lindenstrauss
example outside the unconditional-basis class singled out by Johnson--Naor.
It does not settle the full question whether every weak Hilbert space is
log-Hilbertian, `h`-Hilbertian with `h(n)=o(n)`, or satisfies the J-L lemma.

## Original Problem Source

- William B. Johnson and Assaf Naor, *The Johnson-Lindenstrauss lemma almost
  characterizes Hilbert space, but not quite*, arXiv:0807.1919; Discrete
  Comput. Geom. 43 (2010), 542--553.
- Local source: `data/parsed/arxiv_sources/0807.1919/source.tex`.

In Section 4, Remark/Open Problem 1, Johnson--Naor record that weak Hilbert
spaces are the natural class around their positive Tsirelson example. They
state that it was not known whether every weak Hilbert space is
log-Hilbertian, or even `h`-Hilbertian for some `h(n)=o(n)`. They also note
the known positive result of Nielsen--Tomczak-Jaegermann for weak Hilbert
spaces with an unconditional basis.

## Supporting Source

- Jesus Suarez de la Fuente, *A space with no unconditional basis that
  satisfies the Johnson-Lindenstrauss lemma*, arXiv:2501.13524.
- Local source: `data/parsed/arxiv_sources/2501.13524/source.tex`.

The supporting paper explicitly returns to the Johnson--Naor question. Its
introduction states that the Johnson--Naor result extends to weak Hilbert
spaces with an unconditional basis, but that arbitrary weak Hilbert spaces
were not known to satisfy the J-L lemma. It then uses the twisted Hilbert weak
Hilbert space `Z(T^2)`, notes that this space has no unconditional basis by
Kalton's theorem, and proves:

- Theorem `log`: `Z(T^2)` satisfies the J-L lemma.
- The proof first proves that `Z(T^2)` is log-Hilbertian, then invokes
  Johnson--Naor's implication from log-Hilbertian to J-L.

## Status Match

This gives a clean partial answer to the Johnson--Naor weak-Hilbert direction:

```text
There exists a weak Hilbert space with no unconditional basis that satisfies
the Johnson-Lindenstrauss lemma; namely Z(T^2).
```

It also gives a concrete log-Hilbertian example beyond the unconditional-basis
case mentioned in the original open-problem discussion.

## Limitations

The packet should not be read as resolving the full Johnson--Naor problem.
The following remain outside the scope of this result:

- whether every weak Hilbert space is log-Hilbertian;
- whether every weak Hilbert space is `h`-Hilbertian for some `h(n)=o(n)`;
- whether every weak Hilbert space satisfies the J-L lemma;
- the separate Johnson--Naor questions about the optimal `Delta(n)` rate and
  non-trivial linear dimension reduction in `L_p`.

## Verification Notes

- Cheap duplicate search found no existing packet for `0807.1919`,
  `2501.13524`, `Z(T^2)`, or this weak-Hilbert/J-L implication.
- Nearby previous attempts involving weak Hilbert spaces mention `Z(T^2)` in
  different contexts, but they do not package this Johnson--Naor partial
  answer.
- The arXiv raw source downloads are local gzip-compressed source files, not
  PDFs. Copies are attached as `source_0807.1919.tex.gz` and
  `supporting_2501.13524.tex.gz`.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact human-readable packet source.
- `solution_packet.pdf`: rendered packet.
- `source_0807.1919.tex.gz`: gzip-compressed source download for the original
  paper.
- `supporting_2501.13524.tex.gz`: gzip-compressed source download for the
  supporting paper.
- `tmp/`: LaTeX build products.

## Human Review Recommendation

Check the scope line carefully. The supporting theorem is a positive example
outside the unconditional-basis subclass, not a theorem for arbitrary weak
Hilbert spaces. If accepted, index it as a literature-implied partial answer
to the weak-Hilbert/J-L direction in arXiv:0807.1919.
