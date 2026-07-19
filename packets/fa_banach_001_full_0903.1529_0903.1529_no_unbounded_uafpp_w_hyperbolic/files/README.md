# No unbounded convex W-hyperbolic set has UAFPP

- Source: Laurentiu Leustean, `Proof mining in metric fixed point theory and ergodic theory`, arXiv:0903.1529.
- Target: open problem on page 44 asking whether there are unbounded convex subsets of some W-hyperbolic space with the uniform approximate fixed point property for all nonexpansive self-maps.
- Status: `full_solution_likely_valid`
- Agent: `agent_lane_14`
- Updated: `2026-07-18T21:31:56Z`

## Result

The answer to the source open problem is negative. If `C` is an unbounded
convex subset of a W-hyperbolic space, then `C` fails the UAFPP for the class
of all nonexpansive maps `T:C -> C`.

Given a base point `a in C` and any proposed UAFPP radius `D` for
`epsilon=b=1`, choose `y in C` with `L=d(a,y)>D+1`. Along the geodesic segment
`gamma:[0,L]->C` from `a` to `y`, define

```text
T(z) = gamma(min(d(a,z)+1, L)).
```

The radial coordinate map is 1-Lipschitz and the segment is parametrized by
arc length, so `T` is nonexpansive. Also `d(a,T(a))=1`. But every
`z` with `d(a,z)<=D` is moved by at least one unit, since
`d(a,T(z))=d(a,z)+1`. Thus there is no `1`-fixed point in the `D`-ball about
`a`, contradicting UAFPP.

## Packet Contents

- `main.tex`: full proof packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: local copy of arXiv:0903.1529.
- `figures/open_problem_crop.png`: crop of the source open problem.
- `code/render_open_problem_crop.py`: reproducible crop script.

## Novelty Check

Cheap run indexes had no exact packet for `0903.1529`. A bounded web search
for UAFPP, unbounded convex subsets, W-hyperbolic spaces, and the exact open
problem found the source survey and the original Kohlenbach--Leustean article,
both presenting the question as open, but no later resolution.

Human review should check only the very short radial-map argument, especially
the use of the W-hyperbolic arc-length axiom.
