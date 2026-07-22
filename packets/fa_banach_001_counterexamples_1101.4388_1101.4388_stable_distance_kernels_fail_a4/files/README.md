# Stable Distance Kernels Fail the RKBS Admissibility Condition (A4)

Run: fa_banach_001

Agent: agent_lane_12

Status: candidate_counterexample_likely_valid

## Source question

At the end of Section 6 (PDF page 25) of Song--Zhang--Hickernell,
*Reproducing Kernel Banach Spaces with the l1 Norm*, arXiv:1101.4388, the
authors report numerical evidence that

    K(x,y) = exp(-||x-y||_p^gamma),  p=1,2,  0<gamma<1,

may satisfy condition (A4) for small gamma and moderate node counts, and leave
the search for more (A4) kernels open. Condition (A4) requires

    ||K[x]^{-1} K_x(t)||_1 <= 1

for every finite distinct node set and every target outside it.

## Counterexample theorem

For every 0<gamma<1:

- the p=2 kernel fails (A4) already on R^2, hence on every R^d, d>=2;
- the p=1 kernel fails (A4) on every R^d from an explicit finite dimension
  onward.

The violations occur at arbitrarily small spatial scales. Cross-polytopes
give elementary counterexamples for both values of p. Regular polygons
strengthen the Euclidean result to dimension two.

## Main mechanism

Put all nodes at the same distance from the target and use a transitive
symmetric configuration. The kernel vector and all Gram row sums are then
constant, so K[x]^{-1}K_x(0) is explicit. Its l1 norm is a quotient of two
scalar exponential sums. Both sides agree at scale zero, while a suitable
configuration makes the derivative of the numerator larger. The quotient is
therefore strictly greater than one at all sufficiently small positive scales.

## Scope

This is a full negative answer for the named multidimensional kernel
candidates. It does not classify all admissible kernels, settle the
one-dimensional kernels for 0<gamma<1, or determine optimal relaxed Lebesgue
constants.

## Files

- main.tex: complete proof, novelty bounds, and review recommendation.
- solution_packet.pdf: rendered packet.
- source_paper.pdf: local copy of arXiv:1101.4388v3.
- figures/open_problem_crop.png: source statement from PDF page 25.
- code/verify_symmetric_counterexamples.py: deterministic high-precision
  checks and a direct Gram-system solve.
