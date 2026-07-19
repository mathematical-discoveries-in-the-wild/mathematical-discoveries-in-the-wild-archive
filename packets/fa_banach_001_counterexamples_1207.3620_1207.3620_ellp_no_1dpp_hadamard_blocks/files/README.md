# Counterexample Packet: Hadamard Blocks Show `ell_p` Has No `1`-DPP

- status: candidate counterexample, likely valid
- run: `fa_banach_001`
- source arXiv id: `1207.3620`
- source paper: A. K. Karn and D. P. Sinha, *An operator summability of sequences in Banach spaces*
- target passage: PDF page 11 / source lines 405--413, where the authors state that they were unable to settle whether `ell_p` has the `1`-DPP for `1<p<infty`.

## Claim

For every `1<p<infty`, the space `ell_p` does not have the `1`-Dunford-Pettis property.

Equivalently, there is a bounded operator

```text
T : ell_p -> ell_1
```

which is not absolutely `1`-summing.

## Construction

Use Sylvester Hadamard matrices `H_N`, `N=2^j`, as operators
`ell_p^N -> ell_1^N`. They satisfy

```text
||H_N|| <= N                      if 1<p<=2
||H_N|| <= N^(3/2-1/p)            if 2<=p<infty
pi_1(H_N) >= N^(2-1/p).
```

Thus `pi_1(H_N)/||H_N||` grows at least like `N^(1/p')` for `p<=2` and at least
like `N^(1/2)` for `p>=2`. After scaling each block so the block norms form an
`ell_{p'}` sequence while the block `pi_1` norms tend to infinity, the
block-diagonal operator from `(sum ell_p^N)_p` to `(sum ell_1^N)_1` is bounded
but cannot be absolutely `1`-summing.

## Files

- `main.tex`: full proof packet
- `solution_packet.pdf`: rendered packet
- `source_paper.pdf`: local copy of arXiv:1207.3620
- `figures/open_problem_crop.png`: crop of the source passage
- `code/verify_hadamard_bounds.py`: small sanity check for the Hadamard estimates

## Novelty Check

Before promotion, the agent searched the run indexes for `1207.3620`, the
source title, `operator p-summability`, `1-DPP`, `Pi_1(ell_p,ell_1)`, and
related `ell_p` Dunford-Pettis phrases. No prior packet or attempt addressed
this endpoint.

The local parsed arXiv corpus was searched for later citations to Karn-Sinha
and for exact phrases around `1-DPP`, `ell_p`, and absolutely `1`-summing
operators into `ell_1`. Several related papers cite the source, but none found
in this bounded pass explicitly resolves this note. External web searches for
the exact phrases `ell_p 1-DPP`, `l_p 1-DPP An operator summability`,
`Pi_1 ell_p ell_1 1-summing`, and `absolutely 1-summing ell_p ell_1` likewise
found no explicit later answer.

Human review should focus on the finite-dimensional estimate
`pi_1(H_N) >= N^(2-1/p)`, the operator-norm upper bound
`||H_N x||_1 <= N ||x||_2`, and the block-diagonal passage from unbounded
finite ratios to a bounded non-`1`-summing operator.
