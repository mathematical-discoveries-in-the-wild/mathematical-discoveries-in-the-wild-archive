# Weak-L4 endpoint obstruction for empirical covariance

Status: `candidate_counterexample_likely_valid`

Source: Olivier Guedon, Alexander E. Litvak, Alain Pajor, and Nicole
Tomczak-Jaegermann, *On the interval of fluctuation of the singular values of
random matrices*, arXiv:1509.02322.

## Result

The natural square-root endpoint extension of the source's covariance bound
is false under its weak tail hypothesis `H(t^4)`.  For every sufficiently
large sample size `N`, there is a centered isotropic real random variable `X`
such that

```text
P(|X|>=t) <= t^(-4)  for every t>0,
```

but for independent copies `X_1,...,X_N`, with probability at least `1/76`,

```text
|N^(-1) sum_i (X_i^2-1)| >= (1/4)sqrt(log(N)/N),
```

while deterministically

```text
max_i X_i^2/N <= N^(-1/2).
```

Consequently, no universal constant can give a high-probability bound

```text
S <= C(max_i |X_i|^2/N + sqrt(n/N))
```

at `p=4`, even in dimension `n=1`.  The logarithmic loss is already forced by
scalar second-moment fluctuations.

## Mechanism

Take `Z` to be a Pareto variable of tail exponent two, truncated at
`sqrt(N)`, and put `X=epsilon sqrt(Z/EZ)` with an independent random sign.
The weak fourth-tail condition is exact.  Meanwhile `Var(Z)` is of order
`log N`, so Paley--Zygmund gives a constant-probability fluctuation of order
`sqrt(log(N)/N)`.  Truncation keeps the maximum-column correction at only
`N^(-1/2)`.

## Scope

This is a complete negative answer to the square-root endpoint formulation
under the source's `H(t^4)` hypothesis.  It does not rule out a slower endpoint
rate, and it does not answer the stronger finite-fourth-moment problem with a
uniform `L4-L2` constant.  The construction is a nonasymptotic triangular
array: the distribution may depend on `N`, as permitted by a universal
finite-`N` theorem.

## Packet contents

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: packet source.
- `verification.md`: independent hypothesis and constant audit.
- `source_paper.pdf`: original arXiv paper.
- `figures/p4_endpoint_crop.png`: source page 6 endpoint statement.
- `figures/sqrt_rate_question_crop.png`: source page 20 rate question and bound.

Human review should focus on the scope match between the source's broad
`p=4` sentence and the precise square-root endpoint formulation disproved
here.  The probability calculation itself is elementary and explicit.
