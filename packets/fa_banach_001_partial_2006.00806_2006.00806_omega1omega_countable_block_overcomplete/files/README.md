# Partial Result: countable-block ordinal interval

Status: `candidate_partial_result_likely_valid`

Source paper: Piotr Koszmider, *On the existence of overcomplete sets in some
classical nonseparable Banach spaces*, arXiv:2006.00806.

Target question: Question 48 asks whether ZFC proves that `C([0, xi])` admits
an overcomplete set for every ordinal `xi < omega_2`.

Claim proved in this packet: in ZFC, `C([0, omega_1 * omega])` admits an
overcomplete set.

This is the first countable-block case not covered by the earlier lane-16
partial packet for all `xi < omega_1 * omega`.

## Proof Mechanism

The proof identifies `C([0, omega_1 * omega])` with

```text
R plus c0(N, C([0, omega_1])).
```

It then builds an `omega_1`-family whose evaluations under any fixed functional
become a single analytic function on an uncountable subfamily. Each countable
block is assigned its own sparse set of Taylor exponents, so coefficient
comparison prevents cancellation between different block functionals. An
endpoint-detector series with unbounded coefficients kills the endpoint mass
inside each copy of `C([0, omega_1])`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of arXiv:2006.00806.
- `figures/open_problem_crop.png`: crop of Question 48 from the source paper.

## Verification

Rendered with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=tmp main.tex
```

Human review should focus on the disjoint Taylor-support coefficient
comparison, normal convergence of the analytic series, simultaneous
stabilization over all countably many block measures, and the Banach-space
identification of `C([0, omega_1 * omega])` with the scalar plus countable
`c0`-sum model.
