# Full Solution Packet: Pointwise Convergence Is the Least Locally Solid Hausdorff Topology

- status: candidate full solution, likely valid
- run: `fa_banach_001`
- source arXiv id: `2411.09430`
- source paper: Tadeusz Kiwerski and Pawel Kolwicz, *Direct sums and abstract Kadets--Klee properties*
- target passage: PDF page 37 / source lines 2361--2373, Question 6.c.1.

## Claim

For every Banach sequence space `X` over a countable set `Gamma`, the topology
of pointwise convergence on `X` is the least Hausdorff locally solid vector
topology on `X`.

Since, for the counting measure on `Gamma`, pointwise convergence is exactly
local convergence in measure, this gives an affirmative answer to Question
6.c.1 of Kiwerski--Kolwicz: local convergence in measure is the coarsest
locally solid Hausdorff topology in the class of Banach sequence spaces.

## Method

Let `tau` be any Hausdorff locally solid vector topology on `X`.  Fix a
coordinate `gamma`.  Hausdorffness gives a balanced `tau`-neighborhood `N` of
zero with `e_gamma` not in `N`.  After scaling, every point of `epsilon N` on
the one-dimensional coordinate axis has scalar coefficient of modulus
`< epsilon`.

Choose a solid neighborhood `V subset epsilon N`.  If `x in V`, then the
coordinate truncation `x(gamma)e_gamma` satisfies
`|x(gamma)e_gamma| <= |x|`, so solidity puts it in `V`.  Hence
`|x(gamma)| < epsilon`.  Thus every coordinate functional is
`tau`-continuous.  Therefore `tau` is finer than the pointwise topology.

The pointwise topology itself is Hausdorff and locally solid, with finite
coordinate solid neighborhoods.  Hence it is the least such topology.

## Files

- `main.tex`: proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:2411.09430
- `figures/open_problem_crop.png`: crop of Question 6.c.1

## Novelty Check

The run indexes were searched for `2411.09430`, `Kadets`, `Kadec`, `Klee`,
`direct sums`, `abstract Kadets`, `coarsest locally solid`, `minimal locally
solid`, `local convergence in measure`, and related phrases.  No existing
packet or attempt addresses this target.

External web searches on 2026-06-19 for exact phrases around Question 6.c.1,
Banach sequence spaces, locally solid Hausdorff topologies, pointwise
convergence, and Labuda's theorem found the source paper and adjacent
literature, especially Kandić--Taylor, *Metrizability of minimal and unbounded
topologies*, arXiv:1709.05407, but no later paper explicitly resolving this
Banach sequence space question.

Human review should focus on the interpretation of "locally solid Hausdorff
topology" as a vector topology with a base of solid zero-neighborhoods, and on
the one-dimensional balanced-neighborhood step.  Under that standard
interpretation the argument is direct.
