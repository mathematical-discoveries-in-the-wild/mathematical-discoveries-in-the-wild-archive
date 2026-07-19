# Partial Result: separable strongly Rosenthal compacta are admissible

status: likely_valid_partial_result_full_separable_case_and_envelope_reduction
agent_id: agent_lane_16
source_arxiv: 0803.2320
packet: runs/fa_banach_001/solutions/partial/0803.2320_separable_strongly_rosenthal_admissible/

## Result

Every separable strongly Rosenthal compactum is admissible.

Additionally, for an arbitrary compact space `K`,

```text
K is admissible
iff
K is homeomorphic to a compact subspace of a separable strongly Rosenthal compactum.
```

Equivalently, if `K` is a separable compact subspace of `B_1(X)` for compact
metrizable `X`, then `K` embeds into the pointwise closure of a countable
bounded Rosenthal family of continuous functions on a compact metrizable
space.

This fully settles the separable version of the Glasner--Megrelishvili
strongly-Rosenthal-versus-admissible question.  It does not settle the
nonseparable version.  After the equivalence above, the remaining full problem
is exactly the separable-envelope problem: whether every strongly Rosenthal
compactum embeds into a separable strongly Rosenthal compactum.

## Main Idea

First build the graph compactification cover from the previous packet:
for a countable dense sequence `(f_n)` in `K`, compactify

```text
x |-> (x, f_0(x), f_1(x), ...)
```

and let `(g_n)` be the coordinate functions on the compactified graph.  The
family `(g_n)` is Rosenthal, and `L=cl_p({g_n})` is admissible with a natural
continuous surjection `pi:L -> K`.

The new step avoids trying to split `pi` topologically.  Use the
Glasner--Megrelishvili representation theorem for the admissible compactum
`L`, embedding `L` into `V**` for a separable Rosenthal Banach space `V`.
Then quotient `V` by the closed subspace of vectors that vanish on the
original graph points.  The induced map on second duals collapses exactly the
fibers of `pi`, so `K` embeds as a weak-star compact subset of the second dual
of a separable Rosenthal quotient of `V`.  Glasner--Megrelishvili's
second-dual characterization of admissibility then gives the result.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of the source question on PDF page 3.

## Human Review Focus

Check the quotient step:

1. `N = intersection_x ker(alpha(e(x)))` has annihilator equal to the closed
   linear span of the graph evaluation functionals.
2. The induced map `q**:V** -> (V/N)**` identifies exactly the fibers of
   `pi:L -> K`.
3. The quotient `V/N` is still a separable Rosenthal Banach space.

The second theorem is a short but useful reduction.  One direction uses the
separability of `C(X)` to replace an arbitrary witnessing Rosenthal family by a
countable norm-dense subfamily with the same pointwise closure.  The other
direction uses the first theorem plus heredity of admissibility for compact
subspaces.
