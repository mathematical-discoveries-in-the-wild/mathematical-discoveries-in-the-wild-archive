# Countably Saturated Banach Spaces Have Countable Capture

Status: likely valid general obstruction.

Source target: arXiv:2311.14257, Question 3.

## Result

Every infinite-dimensional countably saturated Banach space has countable
capture and therefore fails BCP.

In particular, every infinite-dimensional countably saturated C*-algebra fails
BCP when regarded as a Banach space. The same proof only needs realization of
countable types built from degree-one norm conditions.

## Key Idea

For a finite set of centres `F`, choose norming functionals `f_c in J(c)`.
The intersection of finitely many kernels is nonzero in an infinite-dimensional
space. A unit vector `u` in that intersection satisfies

```text
||c - lambda u|| >= |f_c(c - lambda u)| = ||c||
```

for every `c in F` and scalar `lambda`.

Thus every finite part of the countable-capture type is satisfiable. Countable
saturation realizes the whole type for a countable centre set, giving one unit
vector that captures all centres.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check that the countable type uses only norm conditions in one variable
and that finite satisfiability follows from the finite-dimensional kernel
argument.

