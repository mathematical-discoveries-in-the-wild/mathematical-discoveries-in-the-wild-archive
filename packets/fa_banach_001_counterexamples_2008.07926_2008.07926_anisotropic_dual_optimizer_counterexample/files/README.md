# An anisotropic polynomial dual optimizer

Status: `candidate counterexample, likely valid pending expert review`

Source: Nikita A. Gladkov, Alexander V. Kolesnikov, and Alexander P. Zimin,
*The multistochastic Monge--Kantorovich problem*, arXiv:2008.07926v1.
The target is the uniqueness belief immediately following Example 2.20 on
PDF page 8.

## Result

Example 2.20 gives symmetric dual optimizers
`(f_A(x,y), f_A(x,z), f_A(y,z))` for the planar problem from Example 2.11
and says that the authors believe there are no other dual solutions.

Set `s=x+y+z`, take `A=1`, and define

```
h12(x,y) = (x-y)(x+y-1)^2,
h13(x,z) = x*z*(2*x+z-2),
h23(y,z) = -y*z*(2*y+z-2).
```

Then

```
h12(x,y)+h13(x,z)+h23(y,z) = (s-1)^2(x-y).
```

Consequently, the three pair potentials

```
g12 = f_1 + h12/12,
g13 = f_1 + h13/12,
g23 = f_1 + h23/12
```

satisfy the exact identity

```
xyz - g12(x,y) - g13(x,z) - g23(y,z)
    = (s-1)^2(2+x+3y+2z)/12 >= 0.
```

They therefore form a dual-feasible triple. Equality holds on the plane
`s=1`, which supports the primal measure, so the triple is dual optimal.
Its total sum is anisotropic and cannot agree identically with the total sum
of any symmetric `f_B` triple; gauge transformations do not change total
sums. Thus it is genuinely outside the displayed family.

## Scope caveat

This is a counterexample to the literal uniqueness belief in the arXiv v1
text. The sentence “We believe that there are no other dual solution” is
absent from the published 2022 JMAA version, although Example 2.20 and the
symmetric family remain. The packet does not claim to refute a theorem in the
published paper.

## Files

- `solution_packet.pdf`: rendered proof packet.
- `main.tex`: self-contained proof source.
- `source_paper.pdf`: arXiv v1 source paper.
- `figures/open_problem_crop.png`: Example 2.20 and the target sentence.
- `verification_report.md`: proof audit and scope notes.
- `code/verify_polynomials.py`: exact symbolic identity checker.
- `tmp/`: LaTeX and PDF-rendering intermediates.

## Novelty check

The run indexes were searched for the arXiv id, title, multistochastic
transport, dual uniqueness, and the planar `xyz` example. Bounded web searches
on July 23, 2026 used the exact source sentence, the displayed `f_A` notation,
the perturbation `(x+y+z-1)^2(x-y)`, the authors, and Example 2.20. No explicit
matching construction or later answer was found. Novelty confidence is
moderate-to-low because the journal version silently removes the uniqueness
sentence.

## Human review focus

Check the three-term polynomial decomposition, the sign of the exact dual
gap, and whether the source intended “no other” modulo the standard gauge
freedom. The last issue does not affect the construction: gauge changes leave
the total sum fixed, while the new total sum is not any symmetric `f_B` sum.
