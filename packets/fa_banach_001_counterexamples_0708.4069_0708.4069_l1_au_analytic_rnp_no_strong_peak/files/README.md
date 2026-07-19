# Counterexample: analytic RNP does not force strong peak density in `A_u(B_X)`

## Status

`counterexample_likely_valid`, scoped to the uniformly continuous analytic
algebra `A_u(B_X)`.

Choi-Lee-Song ask in `arXiv:0708.4069` whether the strong peak functions in
`A(B_X)` or in the weak analytic variants are dense when `X` has the analytic
Radon-Nikodym property. Their paper notes the weak variant is negative for
`X=L_1[0,1]`.

This packet gives the corresponding negative answer for the uniformly
continuous analytic algebra:

> For `X=L_1[0,1]`, the algebra `A_u(B_X)` has no strong peak functions.

Since `L_1[0,1]` has the analytic Radon-Nikodym property, the strong peak
functions are not dense in `A_u(B_X)`.

## Scope

- Settled here: the `A_u(B_X)` version of the analytic-RNP density question is
  false.
- Not claimed here: the same conclusion for the larger algebra `A_b(B_X)`.
- The proof is scalar-valued. Vector-valued and numerical strong peak variants
  are not claimed beyond the cited known weakly-uniform negative results.

## Proof Mechanism

Every scalar continuous polynomial on `L_1[0,1]` is weakly sequentially
continuous, because `L_1` has the Dunford-Pettis property. Since polynomials
are uniformly dense in `A_u(B_X)`, every `f in A_u(B_X)` is weakly sequentially
continuous on the ball.

For each `x in S_{L_1}`, the normalized Rademacher sequence

```text
y_n = (1+r_n)x / ||(1+r_n)x||_1
```

converges weakly to `x` but stays a fixed positive norm distance from `x`.
Thus a weakly sequentially continuous function cannot strongly peak at `x`.
Strong peak points for analytic functions on the ball must lie on the sphere,
so no strong peak function exists.

## Novelty Check

Cheap run indexes were searched for `0708.4069`, Bishop/differentiability,
analytic Radon-Nikodym, strong peak, and `A_u(B_X)` variants. Web searches for
the exact `A_u(B_{L_1})` obstruction found the source paper and nearby
weakly-uniform/numerical results, but no exact prior record of this scalar
`A_u` counterexample in the run.

## Files

- `main.tex`: full proof packet.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: Choi-Lee-Song source paper.
- `figures/open_problem_crop.png`: source question crop from page 16.

