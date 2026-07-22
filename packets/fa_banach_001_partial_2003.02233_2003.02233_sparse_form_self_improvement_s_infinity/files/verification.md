# Verification report

Verdict: candidate substantial partial result, likely valid.

## Claim audited

Conjecture 6.2 of arXiv:2003.02233 holds whenever `s = infinity`, uniformly
for all `m`, all `r_j > 0`, all `q_0 > 0`, and all `0 < q <= q_0`.

## Audit of the proof

1. The target sparse expression simplifies at `s = infinity` because
   `1/(1/q - 1/s) = q`; hence its local test-function factor is exactly
   `(<|g|^q>_Q)^(1/q)`.
2. The stopping lemma for `M_r(f)` is valid for every `q > 0`. In each dyadic
   grid, stop when one input average grows by its assigned large factor. The
   children occupy at most half the parent, and outside them every product of
   averages is controlled by the parent's product. The three-grid lemma then
   handles arbitrary cubes.
3. On the near set `F <= C_T M_r(f)`, the stopping lemma gives the desired
   `q`-sparse form directly.
4. On the far set, the truncated tests
   `h_N = min(N, F^(q/q_0-1)|g|^(q/q_0) 1_E)` are bounded and compactly
   supported. Applying the assumed `q_0` estimate is therefore legitimate.
5. For every selected cube with coefficient `A_Q > 0`, the far-set inequality
   `F > C_T M_r(f) >= C_T A_Q` and `q-q_0 <= 0` give
   `A_Q^q_0 F^(q-q_0) <= C_T^(q-q_0) A_Q^q`. Cubes with `A_Q=0` contribute
   zero.
6. Monotone convergence sends `N` to infinity. Taking a supremum over sparse
   families and then choosing a family within a factor two of that supremum
   preserves the existential formulation of the source conjecture.
7. Combining near and far pieces costs only a parameter-dependent factor and
   retains linear dependence on `C_T`.

No conditional lemma remains.

## Boundary cases

- `q = q_0` is immediate and is also covered by the proof.
- The original sparse constant may be enlarged so that `C_T >= 1`.
- For bounded compactly supported data the target supremum is finite: bounded
  cube scales are controlled by sparseness, and the input averages give a
  geometrically decaying tail on large cubes. A family within a factor two of
  the supremum therefore exists unless the supremum is zero, when the claim is
  immediate.
- Zeros of `F` cause no negative-power problem because the nonlinear test is
  supported on the far set, where `F > 0`, and is truncated before use.

## Remaining scope

For finite `s`, if `t_0=(1/q_0-1/s)^(-1)` and
`t=(1/q-1/s)^(-1)`, the same nonlinear test produces the local exponent
`u=q t_0/q_0`, and `u>t` when `q<q_0`. This is precisely the step that prevents
the endpoint proof from resolving the full conjecture.

## Novelty/literature bounds

- Local: all four cheap indexes and the deterministic source-signal corpus.
- External: exact conjecture-title and Conjecture 6.2 searches, quoted
  simplest-case text, Lorist/Nieraeth title searches, and arXiv variants using
  smaller exponents and `s = infinity`.
- Found: the 2022 paper and a later thesis that restates the conjecture as
  open.
- Not found: a proof of the full endpoint slice or the simplest case.

The search was bounded rather than exhaustive, so novelty confidence is
moderate.
