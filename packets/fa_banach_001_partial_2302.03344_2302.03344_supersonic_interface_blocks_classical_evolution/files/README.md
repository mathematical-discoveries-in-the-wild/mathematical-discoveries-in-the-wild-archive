# Supersonic interface obstruction to classical evolution

Status: `candidate_partial_likely_valid`.

Agent: `agent_lane_01` (lane 1), model GPT5.6.

## Source question

A. Kilian, B. Maschke, A. Mironchenko, and F. Wirth, *A case study of port-Hamiltonian systems with a moving interface*, arXiv:2302.03344. The abstract and Section VI state that, although the frozen generators are Kato-stable under assumptions (A1)-(A2), the conditions under which the family generates an evolution family remain open.

The source imposes no speed restriction on the continuously differentiable interface path `l`. The packet proves that such a restriction is necessary even in the unit, constant-coefficient medium.

## Candidate result

Take `X=L^2([-2,2],R^2)`, `Q^-=Q^+=I_2`, `r=0`, and outer conditions `x_2(-2)=x_2(2)=0`. Let the interface move as `l(t)=2t`. These data satisfy the source assumptions (A1)-(A2), and therefore its corollary makes the frozen family Kato-stable.

Nevertheless, there is a compactly supported smooth datum in `D(A(0))` for which the non-autonomous Cauchy problem has no classical solution on any positive time interval. With characteristic variables

`u=x_1+x_2`, `v=x_1-x_2`,

the equations on the right of the interface are `u_t+u_z=0` and `v_t-v_z=0`. Choose a cutoff `eta=1` near zero and

`x_0(z)=(z eta(z)/2,z eta(z)/2)`.

Then `u_0=z eta(z)` and `v_0=0`. Both backward characteristics from `(t,2t+)` remain strictly to the right of the moving interface and meet time zero at `t` and `3t`. Hence, for small `t>0`,

`u(t,2t+)=t`, while `v(t,2t+)=0`.

But the source interface condition with `r=0` requires `x_2(t,2t+)=(u-v)/2=0`, a contradiction.

Thus Kato stability and the source hypotheses do not suffice for classical evolution-family generation on the natural domains. In this normalized model, excluding interface speeds larger than the characteristic speed is necessary for all-data classical solvability.

## Scope

This is a complete negative sub-result, not a full characterization of the source question. It does not settle:

- subcharacteristic motion `|l'|<1`;
- generalized or weak solution concepts that do not give classical solutions for every datum in `D(A(s))`;
- nonconstant Hamiltonian densities or other interface relations.

## Verification

`code/verify_supersonic_obstruction.py` checks the boundary matrix condition, the characteristic footpoints, and the contradictory traces for several small times. The script is an algebra check; the characteristic proof in `main.tex` is exact.

Run:

```bash
conda run --no-capture-output -n sandbox python code/verify_supersonic_obstruction.py
```

## Novelty search

The run registry and solution, attempt, and proof-gap indexes had no entry for arXiv:2302.03344. Bounded web searches on 2026-07-22 used the exact paper title and combinations of `moving interface`, `evolution family`, `characteristic speed`, `subcharacteristic`, `supersonic`, and `port-Hamiltonian`. They also inspected the nearby arXiv records 2301.07344, 2210.00056, and 2501.14930. No prior statement of this explicit speed obstruction or datum was found. The search did find related moving-boundary formulations, but no classical-generation theorem resolving the source question.

## Human review recommendation

Recommended for expert review as a sharp partial answer. The main review point is the solution concept: the theorem rules out an evolution family that supplies a classical solution for every natural-domain datum. The characteristic contradiction itself uses only the source equations and interface condition.

## Files

- `main.tex`: complete proof packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2302.03344.
- `figures/open_problem_crop.png`: source abstract/conclusion evidence.
- `code/verify_supersonic_obstruction.py`: reusable algebra check.
