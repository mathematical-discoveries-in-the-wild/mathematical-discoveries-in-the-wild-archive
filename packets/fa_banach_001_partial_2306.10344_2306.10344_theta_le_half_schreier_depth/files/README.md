# Partial solution packet: the fixed-theta Tsirelson depth problem for theta <= 1/2

## Source

- Paper: Jakub Hodor, *The depth of Tsirelson's norm*
- arXiv: `2306.10344`
- Local source PDF: `source_paper.pdf`

## Classification

- Status: `partial`
- Target question: Problem 2 asks, for fixed `0 < theta < 1`, for the order of
  magnitude of `j_{T[theta,S_1]}(n)`.
- Packet claim: for every fixed `0 < theta <= 1/2`,
  `j_{T[theta,S_1]}(n) = Theta_theta(sqrt(n))`.

This is not a full solution of Problem 2 because the range `1/2 < theta < 1`
remains open in this packet.

## Files

- `main.tex`: LaTeX source for the proof packet.
- `solution_packet.pdf`: compiled review packet.
- `source_paper.pdf`: original source paper.
- `figures/open_problem_page24_crop.png`: crop showing Problems 2 and 3.
- `code/theta_chain_lp_probe.py`: optional finite-dimensional LP probe for the
  unpromoted `theta > 1/2` chain route.
- `tmp/`: LaTeX build output.

## Proof Summary

The lower bound is a theta-version of Hodor's nested full-Schreier-set forcing
argument. The only change is to start with full Schreier sets of size larger
than `1/theta + 1`, and to put a sufficiently large theta-dependent value on
the outer coordinates.

The upper bound repeats Hodor's upper-bound proof. The single coefficient
sensitive step is the insertion-property lemma. For `theta <= 1/2`, the
functional that Hodor writes as an average at `theta=1/2` is instead a convex
combination with weights `1-2theta`, `theta`, and `theta`. This keeps the
maximal-minimum-support contradiction intact.

## Verification Notes

The human verifier should focus on:

- the generalized lower-bound induction, especially the inequalities using
  the outer scale `L > 1/(1-theta)`;
- the modified insertion lemma and the convex-combination identity;
- confirming that the later realizing-sequence and recursive upper-bound
  arguments use only the insertion lemma and Schreier combinatorics.

The packet deliberately does not claim anything for `theta > 1/2`. A simple
finite LP probe of the most tempting linear-chain witnesses is included only as
diagnostic evidence that this route is not immediately proof-grade.
