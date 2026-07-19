# Exact Aubin-Talenti dimension threshold

Status: `full_solution_likely_valid` (candidate full solution; human review required)

Model: `GPT5.6`

Source: Souptik Chakraborty, Diksha Gupta, Shammi Malhotra, and Konijeti
Sreenadh, *Global Compactness Result for a Brezis-Nirenberg-Type Problem
Involving Mixed Local Nonlocal Operator*, arXiv:2504.15968v2 (2025).

## Result

Remark 1.1(1) asks for the threshold dimension beyond which the localized
Aubin-Talenti family in (1.7) has mixed Rayleigh energy below
`2^(2/N) S_N`. The packet gives an exact Gamma-function formula for the
obstruction

`Q_(N,s) = [U]_s^2 / ||grad U||_2^2`

and proves that the source's strict large-cutoff inequality holds if and only
if `Q_(N,s) < 2^(2/N)-1`. It also proves that the normalized obstruction
decreases under `N -> N+2` for every `N>=7`. Consequently, the exact eventual
threshold is obtained by evaluating the explicit formula until two consecutive
dimensions succeed; no later dimension can fail.

Illustrative evaluations from the included 80-digit checker give
`N_th(1/4)=19`, `N_th(1/2)=19`, and `N_th(3/4)=20`.

## Main mechanism

For `U(x)=(1+|x|^2)^(-(N-2)/2)`, its unitary Fourier transform is an explicit
multiple of `|xi|^(-1) K_1(|xi|)`. The Mellin integral of `K_1^2` evaluates the
unnormalized Gagliardo seminorm exactly. This replaces the source paper's
upper estimate by an equality and turns the dimension issue into a scalar
Gamma inequality.

## Verification and novelty

- The exact `N -> N+2` quotient was checked against independent Gamma
  evaluations for dimensions 7 through 81 and representative values of `s`.
- Direct Bessel quadrature spot checks agree with the closed formula.
- The `s -> 1` limit reproduces the Bourgain-Brezis-Mironescu normalization
  constant for the paper's unnormalized seminorm.
- A bounded search on 2026-07-19 used the exact arXiv id, the quoted question,
  `localized Aubin-Talenti bubbles`, `mixed local nonlocal`, and the critical
  level `2^(2/N) S_N`. It found the source paper and related mixed-operator
  papers, but no later paper resolving this exact threshold question. This is
  not an exhaustive novelty guarantee.

Human review should focus on the Fourier/Gagliardo normalization constant and
the interpretation of the source's uniform cutoff convergence. See
`verification.md` and `solution_packet.pdf`.

Ledger: `runs/fa_banach_001/ledger/results/2504.15968_exact_aubin_talenti_dimension_threshold.json`

