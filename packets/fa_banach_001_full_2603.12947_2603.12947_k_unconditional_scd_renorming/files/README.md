# Full Solution Packet: arXiv:2603.12947 k-Unconditional Non-SCD Renormings

## Classification

`full`

## Source

- arXiv:2603.12947
- Title: "A Banach space with an unconditional basis which is not slicely
  countably determined"
- Authors: Marcus Loo and Yoel Perreau
- Source PDF: `source_paper.pdf`
- Open-question screenshot: `figures/open_problem_crop.png`

## Targeted Question

Question 5.4 asks whether one can produce a Banach space with a
`k`-unconditional basis for `k in (1,2)` whose unit ball is not SCD.

## Result

Yes. For every `k in (1,2)`, the binary tree space `X_T` from the source
paper admits an equivalent norm whose canonical basis is `k`-unconditional
and whose unit ball is not SCD.

The construction interpolates the source paper's non-SCD renorming

`C = closed convex hull(B_X^+ union B_X^-)`

with the original 1-unconditional unit ball. For `t in (1/2,1)`, set

`C_t = closed convex hull(B_X^+ union B_X^- union t B_X)`.

Then `C_t` is the unit ball of an equivalent norm. Sign changes send `C_t`
into `B_X`, while `B_X subset t^{-1} C_t`, so the unconditional constant is
at most `1/t`. Choosing `t = 1/k` gives a `k`-unconditional basis.

The unit ball `C_t` remains non-SCD for every `t < 1`. If an element
`x in Omega^+` were an SCD point of `C_t`, then the same branch-functional
argument used by Loo--Perreau shows that the intersections of a determining
sequence with `B_X^+` would determine `x` inside `B_X^+`. This contradicts
their Proposition 3.9, which says that no element of `Omega^+` is an SCD
point of the positive unit ball.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width screenshot crop of Question 5.4.
- `code/check_interpolation_constants.py`: small sanity checker for the
  parameter inequalities used in the proof.
- `code/make_open_problem_crop.py`: reproduces the screenshot crop.
- `tmp/`: LaTeX build intermediates and disposable render outputs.

## Literature Check

Web check on 2026-06-08 found the arXiv page and mirrors for arXiv:2603.12947,
but no later paper or public note explicitly answering Question 5.4.

