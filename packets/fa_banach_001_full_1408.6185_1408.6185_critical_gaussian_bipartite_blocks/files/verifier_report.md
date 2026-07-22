# Verifier report

Run:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/full/1408.6185_critical_gaussian_bipartite_blocks/code/verify_rate_extremes.py
```

The script checks:

1. the closed form for `J` vanishes at 2 and is increasing;
2. for representative `a`, the computed root `t_a` is strictly above 2 and
   satisfies `J(t_a)=1/a`;
3. perturbing below/above `t_a` gives respectively positive/negative
   exponents `1/a-J(t)`, exactly as used in the proof;
4. the large-`a` expansion
   `t_a-2 ~ (3/(4a))^(2/3)`;
5. `n_k=2k exp(k/a)` indeed gives `k/log(n_k) -> a`.

This is a sanity check of the scalar computations. The Wishart LDP itself is
the cited analytic input, not a numerical claim.

Representative output:

```text
a        t_a          J(t_a)
0.25      3.91380525   4.00000000
1         2.79519514   1.00000000
4         2.32248560   0.25000000
10        2.17630586   0.10000000
100       2.03824251   0.01000000
large-a check a=100000: asymptotic ratio=0.9999808434
all deterministic checks passed
```
