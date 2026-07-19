# Partial packet: uniformly atomic type-I stability

- Source: M. M. Czerwinska and A. Kaminska, “Geometric properties of noncommutative symmetric spaces of measurable operators and unitary matrix ideals,” arXiv:1704.02033.
- Extracted target: Problem 9 on PDF page 55 asks whether stability of `E` and type I of `M` imply stability of `E(M,tau)`.
- Packet status: `candidate_partial_likely_valid` (upgraded 2026-07-19).
- Packet path: `runs/fa_banach_001/solutions/partial/1704.02033_atomic_typeI_commensurable_stability/`.

## Result

Let `E` be a stable, separable symmetric Banach function space on
`[0,infinity)` with order-continuous norm.  Let

```text
M = direct_sum_n B(H_n),
tau((x_n)) = sum_n w_n Tr_{H_n}(x_n),
```

where the sum is countable, the `H_n` are separable Hilbert spaces, and the
positive weights satisfy `inf_n w_n > 0`.  Then `E(M,tau)` is stable.  No
commensurability of the weights is required.

The first step proves the commensurable case by amplifying the `n`th factor by
an integer multiplicity.  For arbitrary weights bounded below, round all
weights upward to multiples of a sufficiently small common `delta`.  The old
and rounded norms differ by at most `1+epsilon`; the rounded space is stable by
the amplification theorem.  Arbitrarily small-distortion embeddings into
stable spaces force the original norm to be stable.

In the symmetric-space framework used by the source survey, the separability
and order-continuity condition is the standard consequence attached to a
stable symmetric space; it is stated explicitly in the theorem to expose the
only function-space permanence property used in constructing the step
sequence space.

## Scope

This is a genuine positive subcase of Problem 9.  It covers type-I factors and
all countable atomic direct sums whose factor trace weights are uniformly
bounded below, including incommensurable weights.  It does not solve the
diffuse-center case or atomic weights tending to zero.

## Evidence and verification

- `source_paper.pdf` is the original arXiv PDF.
- `figures/open_problem_crop.png` shows Theorems 20.5--20.6 and Problem 9 on PDF page 55.
- `code/make_open_problem_crop.py` regenerates the evidence image given Poppler's `pdftoppm` and Pillow.
- `code/check_finite_distribution.py` checks the integer-amplification distribution identity on six finite deterministic cases.  This is a sanity check, not a proof.
- The formal verifier report is included in `main.tex` and `solution_packet.pdf`.

## Novelty check

Before promotion, the cheap run indexes were searched for the arXiv id, exact
title, and core terms around stability, type-I algebras, noncommutative
symmetric spaces, and unitary matrix ideals.  No exact duplicate was found.

A bounded web search on 2026-07-19 used the exact question and combinations of
`stable symmetric space`, `atomic type I`, `commensurable trace`, uniformly
positive trace weights, and `unitary matrix ideal`.  It surfaced the source
survey and the classical sequence-ideal theorem, but no later resolution or
this precise trace-perturbation reduction.
This is a bounded novelty check, not a claim of exhaustive bibliographic
novelty.

## Human review focus

Check the source's convention linking stability, separability, and
order-continuity for symmetric function spaces; the generalized-inverse
scaling in the commensurable proof; and the trace-comparison/dilation estimate
in the upgraded theorem.  The result should remain classified as a candidate
partial until that review is complete.
