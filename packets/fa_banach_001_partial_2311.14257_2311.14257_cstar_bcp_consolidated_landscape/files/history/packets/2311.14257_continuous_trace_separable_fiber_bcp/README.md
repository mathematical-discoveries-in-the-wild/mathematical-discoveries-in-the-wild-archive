# Continuous-Trace C*-Algebras with Separable Fibres Have the Expected BCP Criterion

Status: `partial_result_likely_valid`.

Source target: Jinghao Huang, Karimbergen Kudaybergenov, Rui Liu, *The
ball-covering property of von Neumann algebras and noncommutative symmetric
spaces*, arXiv:2311.14257, Question 3.

Packet path:
`runs/fa_banach_001/solutions/partial/2311.14257_continuous_trace_separable_fiber_bcp/`

## Result

Let `A` be a continuous-trace C*-algebra and let `X = Prim(A)`. Assume the
local elementary fibres are compact operators on separable nonzero Hilbert
spaces. Then the following are equivalent:

- `A` has BCP;
- `A` has UBCP;
- `X` has a countable pi-basis.

This promotes the previous countably-generated continuous `C_0(X)` result to a
larger type-I class: countable generation is not needed once the local
continuous-trace charts have separable compact-operator fibres.

## Proof Intuition

The negative half is the already-packaged primitive pi-base obstruction.

For the positive half, use the local Dixmier-Douady/Fell description
`A_U ~= C_0(U, K(H))`. A countable pi-basis is refined to countably many
charted open patches. In each chart, separability of `K(H)` gives a countable
net of local operator directions, and local compactness supplies countably
many scalar bumps with arbitrarily small support. The centers are `4 h T`.

Given `a` in the unit sphere, pick a charted patch where `||a(x)|| > 3/4`,
choose `T` close to the local fibre direction of `a`, then choose the bump
support small enough that `||a - 4 h T|| < 7/2`. All centers have norm `4`, so
the fixed-radius balls avoid a uniform neighborhood of the origin. This is
UBCP.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2311.14257 source paper.
- `figures/open_problem_crop.png`: crop of the source question.

## Limitations

This is not a full arbitrary C*-algebra classification. It covers the
continuous-trace/separable-fibre side. Earlier packets show primitive topology
alone cannot characterize BCP: II_1 factors have one-point primitive ideal
space but fail BCP.

The main convention to check is the continuous-trace local-triviality input:
the proof is written for the standard locally trivial elementary-bundle model.

## Human Review Recommendation

Review as a strong partial theorem. The key checks are the charted-bump
construction, the cutoff `chi a` used to represent a general element locally,
and the constants `1/64`, `7/2`, and center norm `4`.
