# Bounded-generator counterexample to semigroup little-Hölder biduality

Status: `counterexample_likely_valid`

Model: `GPT5.6`

Agent: `agent_lane_08`

Date: 2026-07-19

## Source

Adrián González-Pérez, *Hölder classes via semigroups and Riesz transforms*,
arXiv:1904.10332; *Mathematische Zeitschrift* 301 (2022), 3245-3284.

Open Problem P.3 appears on page 34 of the local arXiv PDF and in Section 8.1,
page 3282, of the published version. It asks whether the semigroup little
Hölder class satisfies
`lambda_alpha(T)** isomorphic to Lambda_alpha(T)`.

## Result

P.3 has a negative answer in its stated generality for every `0 < alpha < 1`.
Take the finite commutative von Neumann algebra `M = ell_infinity(N)` with
faithful normal trace

`tau(f) = sum_{n >= 1} 2^{-n} f_n`,

let `E(f) = tau(f) 1`, and set

`T_t = E + exp(-t)(I-E)`.

This is a nonconstant, ergodic, symmetric Markov semigroup. Its generator
`A = I-E` is a projection, so its Poisson semigroup equals `T_s`. Directly,

`dP_s/ds = -exp(-s)(I-E)`.

Hence both the big and little semigroup Hölder classes equal `ell_infinity`
with equivalent norms. But `ell_infinity**` has density character at least
`2^continuum`, whereas `ell_infinity` has density `continuum`; they are not
even abstractly isomorphic.

## Packet contents

- `solution_packet.pdf`: typeset review packet.
- `main.tex`: complete source.
- `source_paper.pdf`: original arXiv source PDF.
- `figures/open_problem_crop.png`: real crop of P.3 from page 34.
- `code/verify_expectation_semigroup.py`: exact finite-dimensional algebra
  checks.
- `verification_report.txt`: dated command, complete output, and scope.

## Verification

From this directory:

```bash
conda run --no-capture-output -n sandbox python \
  code/verify_expectation_semigroup.py
```

Recorded final line: `all checks passed` (see `verification_report.txt`).

The script checks finite weighted expectation matrices for sizes
`2, 3, 5, 8, 16` using exact rational arithmetic. It verifies the Markov,
projection, weighted self-adjointness, and semigroup identities. The
infinite-dimensional density argument is proved in the packet and is not a
computational claim.

## Novelty and scope

A bounded search on 2026-07-19 covered all four run indexes, exact title/id and
P.3 phrase searches, the 2022 published article, and later semigroup Campanato
work. The closest later paper found was Hong-Jing, arXiv:2409.14414, which
answers a Campanato/Lipschitz equivalence problem rather than P.3. No prior
answer or this counterexample was found. Novelty confidence is moderate-high,
subject to fuller citation review.

The result only refutes unrestricted P.3. Positive biduality may survive under
genuine smoothing assumptions that exclude bounded-generator collapse. It
does not address the paper's other open problems.

## Human review focus

1. Confirm all source Markov-semigroup hypotheses for the expectation
   semigroup.
2. Check the quotient-density proof separating `ell_infinity**` from
   `ell_infinity`.
3. Decide whether the source intended an unstated hypothesis excluding
   bounded generators. The printed problem does not state one.
