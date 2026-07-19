# Counterexample: Milman Moduli and Quasi-Orthogonality

## Source Question

- Source paper: Grigory Ivanov and Horst Martini, *New Moduli for Banach Spaces*, arXiv:1609.01587.
- Location: Section 6, "Some open questions", Conjecture 3.
- Question: whether in Milman's moduli it is enough to restrict to pairs
  `y` quasi-orthogonal to `x`, giving
  `zeta^-_X(epsilon) - 1 = beta^-_X(epsilon)` and
  `zeta^+_X(epsilon) - 1 = beta^+_X(epsilon)`.

## Counterexample

The first equality is false. In the real space `X = l_4^2` at
`epsilon = 1/2`,

```text
zeta^-_X(1/2) - 1 < beta^-_X(1/2).
```

The packet proves the exact lower value
`beta^-_X(epsilon) + 1 = (1 + epsilon^4)^{1/4}` for `l_4^2`, and gives an
explicit quasi-orthogonal unit pair whose one-sided `zeta^-` value is strictly
below `(17/16)^{1/4}`.

## Files

- `main.tex`: full counterexample packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of the source conjecture.
- `code/check_l4_counterexample.py`: exact rational and numerical check.

## Review Focus

Review should check the orientation of quasi-orthogonality against the source
definition. The packet uses the source convention: `y` is quasi-orthogonal to
`x` iff some norming functional at `x` annihilates `y`. The result disproves
only the `zeta^-`/`beta^-` equality; it does not address the `zeta^+` equality
or the other conjectures in the source paper.
