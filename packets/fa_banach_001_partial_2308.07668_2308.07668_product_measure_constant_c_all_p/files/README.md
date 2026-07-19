# Product-Measure Lp Constants

Status: `partial` result for arXiv:2308.07668.

This packet extends the earlier `p=2` packet for the source paper's Proposition 55 question. It proves the exact limiting constant `c = sup_n c_n` for every `1 < p < infinity` and proves the exact finite constants `c_n` for `p >= 2`.

## Claims

For the constants `c_n` and `c` in Proposition 55 of the source paper:

```text
c = 2^(1/p)       for 1 < p <= 2,
c = 2^(1-1/p)     for 2 <= p < infinity.
```

Moreover, for every `n >= 1` and every `p >= 2`,

```text
c_n = 2^(1-1/p).
```

For `1 < p < 2`, the packet proves the quantitative bounds

```text
2 - (4 - 2^p)/2^n <= c_n^p <= 2,
```

so `c_n -> 2^(1/p)`. The exact finite value of `c_n` for `1 < p < 2` is not claimed as solved here.

## Evidence

- Source paper: `source_paper.pdf`.
- Open-question crop: `figures/open_problem_crop.png`, page 25 of the arXiv PDF.
- Packet PDF: `solution_packet.pdf`.
- Numerical finite-atom probe: `code/check_finite_atom_conjecture.py`.

## Method

The proof reduces each overlap pattern in the source definition to conditionally iid real random variables. A sharp iid moment inequality gives the upper bound:

```text
E|U-V|^p <= 2 E|U|^p             for 1 < p <= 2,
E|U-V|^p <= 2^(p-1) E|U|^p       for 2 <= p < infinity.
```

Sharpness for `c` comes from rare spikes when `p < 2` and Rademacher variables when `p >= 2`.

## Remaining Finite Problem

For `1 < p < 2`, numerical optimization supports the stronger formula

```text
c_n^p = 2 - (4 - 2^p)/2^n,
```

attained by a function taking values `+a`, `-a`, and `0` on the finite cube. This would settle the finite `c_n` problem, but the packet records it only as a conjectural finite-atom extremal inequality.

## Human Review Recommendation

Check the two iid moment inequalities and the conditioning step from the paper's overlap definition. The packet is suitable as a partial result: exact `c` for all `p`, exact `c_n` for `p >= 2`, and asymptotically sharp bounds for `1 < p < 2`.
