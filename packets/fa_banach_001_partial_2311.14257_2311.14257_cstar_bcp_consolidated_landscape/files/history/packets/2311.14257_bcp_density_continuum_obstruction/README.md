# BCP Forces Density at Most Continuum

Status: likely valid general obstruction.

Source target: arXiv:2311.14257, Question 3.

## Result

Every Banach space with BCP has cardinality, hence density character, at most
the continuum.

Consequently, every C*-algebra with density character strictly larger than the
continuum fails BCP. In particular, the remaining simple nonseparable C*-core
case can be restricted to density exactly continuum.

## Key Idea

Suppose the unit sphere is covered by balls `B(c_n,r_n)` with
`r_n < ||c_n||`. For each nonzero center choose a norming functional `f_n`.
If the `f_n` had a nonzero common kernel vector `u`, then after normalizing
`u` we would have

```text
||u - c_n|| >= |f_n(u-c_n)| = ||c_n|| > r_n
```

for every `n`, contradicting the cover. Thus the countable family `(f_n)`
separates points, and the map `x -> (f_n(x))` injects the space into
`C^N`, which has cardinality continuum.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check the separation argument from BCP centers to a countable
point-separating family of norming functionals.

