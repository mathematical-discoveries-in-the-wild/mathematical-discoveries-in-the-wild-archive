# Parity-separated unconditional L2 lower bound

Status: `partial_result_likely_valid`.

## Source Target

- Source: Itay Glazer and Dan Mikulincer, "Anti-concentration of polynomials: `L^p` balls and symmetric measures", arXiv:2603.22664.
- Targeted source questions: Conjecture 1.4 and Question 1.5 in the "Discussion and further questions" subsection.
- Source asks for dimension-free `L^2` lower bounds for degree-`d` homogeneous polynomials with normalized top-degree coefficient vector under isotropic log-concave `H_n`-invariant measures, and suggests the cube may be extremal.

## Result

This packet proves a broad structural subcase of Conjecture 1.4.

If `mu` is any isotropic unconditional log-concave probability measure on `R^n`, then every degree-`d` homogeneous polynomial whose monomial support is parity-separated satisfies
`int f^2 dmu >= c_d ||coeff_d(f)||_2^2`.

Here parity-separated means no two monomial exponent vectors are congruent modulo 2 coordinatewise. In particular, every multilinear homogeneous polynomial is covered. For odd degree, and for multilinear forms, the mean is zero under unconditional symmetry, so the source paper's Proposition 1.1 gives dimension-free small-ball and Fourier decay as well.

## Scope

This is not a full solution of Conjecture 1.4. The unsolved part is exactly the same-parity cancellation regime, where sign averaging no longer diagonalizes the second moment. That regime includes the symmetric even-degree polynomial families the source identifies as the main obstruction.

## Files

- `source_paper.pdf`: arXiv:2603.22664.
- `solution_packet.pdf`: expert-facing proof packet.

Ledger: `runs/fa_banach_001/ledger/results/2603.22664_parity_separated_unconditional_l2_lower_bound.json`.
