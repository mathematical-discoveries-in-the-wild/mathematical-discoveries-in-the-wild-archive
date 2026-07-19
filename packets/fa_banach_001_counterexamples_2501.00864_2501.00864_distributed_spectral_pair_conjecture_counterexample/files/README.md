# Counterexample to the Distributed Spectral Pair Conjecture in arXiv:2501.00864

Run: `fa_banach_001`  
Agent: `agent_lane_02`  
Status: `counterexample_likely_valid`  
Date: 2026-07-03

## Source Problem

Chun-Kit Lai and Ruxi Shi, *When is the fractal uncertainty principle for discrete Cantor sets most uncertain?*, arXiv:2501.00864.

Conjecture 5.1 asks whether every distributed spectral pair `(A,B)` in `{0,1,...,M-1}` is either a spectral pair in `Z_M` or a spectral pair in `Z_{M^2}`.

## Counterexample

Take

```text
M = 24,
A = {0, 3, 18, 21},
B = {0, 4, 16, 20}.
```

Then `(A,B)` is a distributed spectral pair in the sense of Theorem 1.3 / Conjecture 5.1 of the source, but it is neither a spectral pair in `Z_24` nor a spectral pair in `Z_576`.

The key factorization is

```text
P_A(x)=1+x^3+x^18+x^21=(1+x^3)(1+x^18)
      = Phi_2 Phi_4 Phi_6 Phi_12 Phi_36.
```

Thus `P_A` vanishes exactly on roots of unity whose order is one of `2,4,6,12,36`. The difference set `B-B` is `{0, +/-4, +/-12, +/-16, +/-20}`. The first-level distributed condition covers `+/-4`, `+/-12`, and `+/-20`; for the remaining differences `+/-16`, every second-level translate has order `36` modulo `24^2`.

## Verification

Run:

```bash
python runs/fa_banach_001/solutions/counterexamples/2501.00864_distributed_spectral_pair_conjecture_counterexample/code/verify_counterexample.py
```

The script uses only integer gcd/order checks.

## Novelty Check

Bounded local search for `2501.00864`, `distributed spectral pair`, the title, and the explicit sets found only the source paper and queue snippets. Web searches for the explicit sets and close phrases such as `"distributed spectral pair" "counterexample" "Z_{M^2}"` found no prior answer. A bounded brute-force check found no counterexample for `M <= 15`; the displayed example was found in a targeted `M=24`, four-point search.

## Files

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: source arXiv PDF.
- `figures/open_problem_crop.png`: crop of Conjecture 5.1.
- `code/verify_counterexample.py`: exact verifier.

## Human Review Recommendation

This is a compact finite counterexample. Review should focus on the definition of distributed spectral pair in the source and the convention for spectral pairs in `Z_{M^2}` when `A,B` are digit subsets of `{0,...,M-1}`.
