# Free Gibbs centering under the printed growth hypothesis

- **Source arXiv id:** 2410.02715
- **Source title:** A sharp symmetrized free transport-entropy inequality for the semicircular law
- **Source author:** Charles-Philippe Diez
- **Run:** `fa_banach_001`
- **Agent:** `agent_lane_08`
- **Status:** counterexample likely valid, with corrected positive theorem

## Claim

The source asks whether for every continuous potential `f` satisfying the
one-dimensional free Gibbs growth condition
`f(x)-2 log |x| -> +infinity`, there is a real `lambda` such that the free
Gibbs measure for `f + lambda x` has barycenter zero.

As printed, this is false. Take

```text
V(x) = c log(1+x^2),   c > 1,
f_a(x) = V(x-a),       a != 0.
```

Then `f_a` satisfies the printed growth condition, but its equilibrium measure
is the translate by `a` of the symmetric equilibrium measure for `V`, hence has
barycenter `a`. For every nonzero `lambda`, the potential `f_a + lambda x` is no
longer confining in one direction and the free Gibbs variational functional is
unbounded above. Thus no admissible `lambda` exists.

The packet also records the natural repair: if `f` is two-sided superlinear,
then the free pressure `lambda -> eta(f + lambda x)` is coercive and convex; at
its minimizer, the envelope derivative is minus the barycenter of the tilted
equilibrium measure, so the barycenter is zero.

## Files

- `main.tex` - proof packet.
- `solution_packet.pdf` - rendered packet, if LaTeX compilation succeeds.
- `source_paper.pdf` - local copy of the source paper.
- `tmp/` - LaTeX build intermediates.

## Novelty Check

Cheap run indexes had no exact existing packet for `2410.02715`. Web searches
on 2026-07-03 for the exact barycenter/free-Gibbs linear-tilt phrases found the
source paper but no separate answer.

## Human Review Recommendation

Review as a literal counterexample to the printed conjecture, not as a negative
answer to the stronger superlinear version implicitly used in the surrounding
argument. The repair theorem should also be checked, especially the standard
pressure differentiability/envelope step under the chosen admissibility class.
