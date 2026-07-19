# Partial Result: Order-Unit Minorization Forces Nonempty Spectrum

Run: `fa_banach_001`

Agent: `agent_super_01`

Status: `partial_result_likely_valid`

## Source Problem

Daniel Daners, Jochen Glueck, and James B. Kennedy, *Eventually Positive
Semigroups of Linear Operators*, arXiv:1511.09020.

In Section 6, after proving non-emptiness of the generator spectrum for
uniformly eventually strongly positive semigroups on `C(K)`, the source
remarks that it is unclear whether `sigma(A) != empty` holds for uniformly or
individually eventually positive semigroups on `C(K)` in general.

## Result

This packet proves a partial positive answer. Let `(T(t))_{t >= 0}` be a real
individually eventually positive `C_0`-semigroup on `C(K)` with generator `A`.
If, for some `t_1 > 0`, the operator `T(t_1)` is positive and either

```text
T(t_1) u >= eps u
```

for some `u >> 0` and `eps > 0`, or dually

```text
T(t_1)' phi >= eps phi
```

for some nonzero positive functional `phi`, then `sigma(A)` is nonempty.

In particular, a uniformly eventually positive semigroup has nonempty
spectrum whenever one sufficiently late operator minorizes an order unit.

## Method

The minorization gives a finite lower bound on the growth bound:
`||T(n t_1)|| >= eps^n` for all `n`. Hence `omega_0(A) > -infty`. The source
Theorem 6.4 proves `s(A)=omega_0(A)` for real individually eventually positive
semigroups on `C(K)`. Therefore `s(A)` is finite, which is impossible if the
spectrum were empty.

## Scope

This does not solve the full source question. It leaves open uniformly
eventually positive semigroups for which no positive tail operator admits such
a primal or dual lower minorization.

## Files

- `main.tex`: proof note.
- `solution_packet.pdf`: rendered proof note.
- `source_paper.pdf`: arXiv:1511.09020.
