# `RW(1,X)=1` plus WORTH implies Property(M)

Status: `partial_result` / likely valid.

Source target: Tim Dalby, *Properties of `R(X), R(a,X)` and `RW(a,X)`*, arXiv:2005.08492.

Open question addressed: Section 5 asks whether either `R(1,X)=1` or `RW(1,X)=1` implies Property(M).

## Result

If a Banach space `X` has WORTH and `RW(1,X)=1`, then `X` has Property(`m_infty`) and hence Property(M).

Equivalently, the `RW(1,X)=1` half of Dalby's question has an affirmative answer inside the WORTH class. Any counterexample to `RW(1,X)=1 => Property(M)` must therefore fail WORTH.

## Proof Idea

`RW(1,X)` only controls the better of the two signs `x_n + x` and `x_n - x`. WORTH removes this sign ambiguity by forcing the two signs to have the same asymptotic norm. On a subsequence realizing `limsup ||x_n+x||`, normalize by `max(limsup ||x_n||, ||x||) + eps`; WORTH makes both signs converge to the same value, and `RW(1,X)=1` gives the upper bound. Weak lower semicontinuity and the triangle inequality give the matching lower bound.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled packet.
- `source_paper.pdf`: local copy of arXiv:2005.08492.
- `figures/open_problem_crop.png`: crop of the open-question passage.

## Search Notes

Checked exact phrases around `RW(1,X)=1`, WORTH, Property(M), and the source title in web search and the local parsed arXiv corpus. No later explicit statement of this WORTH subcase was found. The result is presented as a new partial theorem, not as a full solution of the original open problem.

## Limitations

This does not settle `RW(1,X)=1` without WORTH, does not settle the weaker `R(1,X)=1` hypothesis, and does not settle the dual variants in the source paper.
