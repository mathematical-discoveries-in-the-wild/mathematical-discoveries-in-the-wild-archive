# 2007.15623 W2 equals tilde W2

Status: `full_solution_likely_valid`

Source: Weinan E and Stephan Wojtowytsch, *On the Banach spaces associated with multi-layer ReLU networks: Function representation, approximation theory and gradient descent dynamics*, arXiv:2007.15623.

## Result

The packet proves that for every compact `K subset R^d`,

```text
W^2(K) = tilde W^2(K) = X_{(0,1),(0,1),{0,...,d};K}.
```

This answers the source paper's Section 4.3 question asking whether the restriction to first-layer functions representable through a single separable `Y_pi` reduces expressivity.

## Idea

A single `W^2` function is represented by one finite outer Radon measure on the Barron unit ball. Select one norm-one first-layer representing measure for each inner Barron function used by that outer measure. Averaging their total variations produces one probability `pi` that dominates almost every selected inner representation. Hence the outer measure is concentrated on `Y_pi`, so the same function lies in `tilde W^2`.

## Scope

This settles the two-hidden-layer `L^1` indexed expressivity question. It does not settle the separate Hilbert-weight/RKHS subspace question for `W_{L^1,L^1,pi^0}(K)`.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of arXiv:2007.15623.
- `figures/open_problem_crop.png`: rendered source page containing the open question.

## Review Focus

Check the measurable-selection step for norm-attaining first-layer Barron representations and the use of Radon-Nikodym domination to build the common distribution `pi`.
