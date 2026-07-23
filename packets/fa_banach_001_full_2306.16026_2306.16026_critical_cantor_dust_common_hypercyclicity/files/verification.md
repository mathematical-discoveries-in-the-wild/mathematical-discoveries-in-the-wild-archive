# Verification report

verdict: `candidate_full_solution_likely_valid`

date: `2026-07-23`

model: `GPT5.6`

## Source checks

- arXiv:2306.16026, Problem 6.1, PDF page 36 asks the critical
  `1/4`-dissection Cantor-dust question and says the endpoint remains open.
- Bayart-Costa-Menet, arXiv:2103.13152, Theorem 2.2 gives the exact
  necessary-and-sufficient covering/scheduling characterization used in the
  packet, both on `c0` and on `ell_p`.
- That theorem allows the finite tags to lie anywhere in `(0,infinity)^2`;
  they need not belong to the parameter dust.

## Proof audit

1. **Cylinder geometry.** A level-`m` cylinder lies in an axis-parallel square
   of side `L 4^{-m}`. Its upper-right corner is therefore a valid tag whenever
   the characterization rectangle has side at least `L 4^{-m}`.
2. **Variation lemma.** A jump whose two words have common-prefix length `h`
   is at most `L 4^{-h}`. Charging it to crossed cylinder boundaries at every
   lower level gives
   `4 L m q / 4^m + 8L/3`. One incoming transition adds at most `L`.
3. **Scheduling lemma.** The least next integer time obeys
   `n' <= (1+A d)n + A`; iterating gives
   `(n_in + A q) exp(A total_variation)`.
4. **Stage invariant.** With
   `q <= theta 4^m / m`, the variation exponent is uniformly bounded.
   The choices `eta=1/(4P)`, `m_0 >= 4PA`, and `4^s >= 2P` give
   `n_out <= theta 4^m/2 <= eta theta 4^{m+s}`.
5. **Covering size.** The invariant implies every time used at level `m` is
   at most `theta 4^m`, hence `tau/n >= L4^{-m}`.
6. **Finite termination.** Every nonfinal stage covers symbolic length at
   least `theta/(2(m_0+js))`. The harmonic sum diverges, so the process cannot
   have infinitely many nonfinal stages within total symbolic length one.
7. **Conclusion.** The concatenated finite schedule satisfies both clauses of
   Theorem 2.2 for the whole dust, hence for every compact subset.

No computational assumption occurs in these seven steps.

## Numerical smoke test

The exploratory greedy algorithm is different from the formal block
construction. It was compiled and run with:

```sh
c++ -O3 -std=c++17 code/finite_traversal_probe.cpp -o /tmp/fa2306_probe
/tmp/fa2306_probe 0.1 1000000000
```

The final checkpoint was:

```text
FINAL 1000000000 0.877709756081458 0.877709756081458 1670438445 17 incomplete
```

This ruled out the earlier suspicion that the greedy schedule quickly
stabilized below full symbolic mass, but it does not prove termination and is
not cited in the formal argument.

## Novelty check

The run indexes and local source corpus were searched for the exact arXiv id
and core terms. Four arXiv-restricted web queries on 2026-07-23 found the
source paper and unrelated hypercyclicity papers, but no later direct answer.
Novelty confidence is therefore bounded/moderate, not definitive.

## Reviewer focus

The two nonstandard points deserving close human review are:

- the multiscale boundary count in Lemma 1;
- the direction and constants in the stage-time invariant.

The source screenshot and final PDF were rendered and visually inspected.
