# Relative Two-Evaluation Criterion for Countable Capture

Status: likely valid partial criterion.

Source target: arXiv:2311.14257, Question 3.

## Result

Let `A` be a unital C*-algebra. Suppose that for every separable unital
C*-subalgebra `B subset A` there are a self-adjoint `u in A` with `||u||=1`
and two contractive maps from `C*(B,u)` into a unital C*-algebra which agree
isometrically on `B` and send `u` to `1` and `-1`, respectively. Then `A`
has countable capture and fails BCP.

A concrete sufficient condition is:

```text
for every separable B subset A there is a commuting self-adjoint u
with spectrum containing {-1,1}, and C*(B,u) is the minimal tensor
copy B tensor C*(u).
```

## Why It Matters

This abstracts the fresh-coordinate proof for uncountable tensor products.
It also isolates the missing lemma for the arbitrary simple nonseparable
C*-algebra case: if every separable subalgebra has such a fresh two-evaluation
direction, then the full conjectural negative side follows.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check the two-evaluation distance inequality and the formulation of the
tensorial sufficient condition.
