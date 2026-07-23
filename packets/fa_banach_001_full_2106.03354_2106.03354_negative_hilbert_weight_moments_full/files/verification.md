# Verification report

Status: `full_solution_likely_valid`, awaiting independent human review.

## Exact target match

- Source: Mitra--Sire, arXiv:2106.03354, PDF page 31.
- Target: for `-1 < beta < 0`, prove that equation (29) remains valid
  whenever the moment exists and that `kappa_beta(x) < infinity` is necessary.
- Packet theorem: proves both statements under the same local assumptions
  `rho(x)>0` and continuity of `rho` at `x`.

## Mathematical audit

1. For `Y=||x-X||^{-d}`, continuity at `x` gives
   `t P(Y>t) -> V_d rho(x)` by averaging `rho` over shrinking balls.
2. Truncation at `b_n=V_d rho(x) n log n` gives
   `S_n/b_n -> 1` in probability:
   the truncated mean is asymptotic to `V_d rho(x) log b_n`, its normalized
   variance is `O(1/log n)`, and the probability of any omitted term is
   asymptotic to `1/log n`.
3. For every `q<1`, layer cake and
   `P(S_n>t) <= C n(1+log t)/t` imply
   `E[S_n^q] <= C_q b_n^q`.
4. Choosing `a<q<1` makes `(S_n/b_n)^a` uniformly integrable, hence
   `E[S_n^a] ~ b_n^a`.
5. The identity
   `w_0^{-a}=(1+||x-X_0||^d S_n)^a`, independence, and
   `z^a <= (1+z)^a <= 1+z^a` yield the exact constant.
6. Sufficiency of `kappa_{-a}<infinity` follows from
   `S_n^a <= sum Y_i^a`. Necessity follows from the lower bound using only
   `Y_1`; the expectation factors as `kappa_{-a} kappa_a`.
7. `kappa_a` is finite for `0<a<1` because the local singularity
   `||y||^{-ad}` is integrable in dimension `d`, and it is strictly positive.

No unproved dependency remains in the argument.

## Computational sanity check

`code/check_uniform_example.py` tests `d=1`, `x=0`,
`rho=1/2` on `[-1,1]`, and `beta=-1/2`. Here
`V_1 rho(0)=1` and `kappa_{-1/2}=2/3`, so the predicted equivalent is
`(2/3) sqrt(n log n)`. The simulation is finite and has slow convergence
because the limiting moment has infinite variance; it is not part of the
proof. The command

```text
conda run --no-capture-output -n sandbox python \
  code/check_uniform_example.py --repetitions 50000 --batch-size 500
```

gave observed/predicted ratios `1.4417, 1.3434, 1.3055, 1.2563` at
`n=64, 256, 1024, 4096`, respectively, consistent with slow convergence
toward one and showing no normalization or reciprocal-power contradiction.

## Novelty audit

On 23 July 2026, the run indexes and bounded web/arXiv searches were checked
using the exact source id, conjecture phrase, notation, authors, and close
heavy-tail variants. No claimed resolution was found. The latest local source,
dated 7 June 2024, still states the conjecture. Novelty is not certified and
requires specialist review.
