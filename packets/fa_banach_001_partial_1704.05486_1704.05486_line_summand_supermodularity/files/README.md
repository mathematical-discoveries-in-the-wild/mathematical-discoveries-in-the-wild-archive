# Candidate Partial Result: line-summand supermodularity

Status: `partial_result_likely_valid`

This packet addresses arXiv:1704.05486, Fradelizi-Madiman-Marsiglietti-Zvavitch, "The convexification effect of Minkowski summation."

Targeted source question: Remark 4.16(1), asking whether

```text
Vol_n(A+B+C) + Vol_n(A) >= Vol_n(A+B) + Vol_n(A+C)
```

holds in higher dimensions when `A` is convex and `B,C` are arbitrary compact sets.

Result: the inequality holds in all dimensions whenever `B` and `C` are compact subsets of a common affine line. More generally, it holds if the fibers of `A` parallel to that line are intervals.

Main mechanism: reduce to one-dimensional fibers parallel to the common line and apply Proposition 4.15 of the source paper on each fiber, then integrate by Fubini.

Files:

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet.
- `source_paper.pdf` - local copy of the source paper.
- `figures/open_problem_crop.png` - crop of Remark 4.16(1).
- `code/rectangle_union_smoke.py` - optional exploratory smoke check for finite translate examples; not used as proof.

Remaining open: the full case where `B` and `C` are arbitrary compact subsets of `R^n`.
