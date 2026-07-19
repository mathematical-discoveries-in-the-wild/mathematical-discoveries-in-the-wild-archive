# Self-adjoint/Hermitian implications fail on complex ell_4^2

Status: `counterexample_likely_valid`

Source paper: Mohammed Shameem and Deepesh K. P., *On properties of
normal operators and self-adjoint operators on smooth Banach spaces*,
arXiv:2605.15898.

## Result

The packet answers the first open question from the source paper in the
negative at the level of bare implications: on complex smooth Banach spaces,
García-Pacheco self-adjointness and the paper's Hermitian condition do not
imply one another.

On `X = (C^2, ||.||_4)`, the coordinate swap

```text
U(z_1,z_2) = (z_2,z_1)
```

is self-adjoint, unitary, and normal in the source definitions, but it is not
Hermitian.  For `x=(1,2i)`, the normalized duality map gives
`Jx(Ux) = -6i/sqrt(17)`, which is not real.  Thus even a unitary normal
self-adjoint operator can fail to be Hermitian.  For the unit vector
`x/||x||_4`, the numerical range contains `-6i/17`, so the same example also
shows that the numerical range of a self-adjoint/unitary/normal operator in
this Banach-space framework need not be real.

Conversely, the diagonal operator

```text
D(z_1,z_2) = (z_1,2z_2)
```

is Hermitian and positive, since `Jx(Dx)` is always real and nonnegative, but
it is not self-adjoint.  At `x=(1,1)`, `D'Jx=(1,2)/sqrt(2)` whereas
`J(Dx)=(1,8)/sqrt(17)`.

## Files

- `main.tex`: self-contained counterexample packet.
- `solution_packet.pdf`: rendered review packet.
- `source_paper.pdf`: arXiv source paper PDF.
- `figures/open_problem_crop.png`: source page with the open questions.
- `figures/source_example_crop.png`: source page containing the coordinate
  swap example.
- `code/check_l4_examples.py`: arithmetic check for the displayed values.

## Novelty Check

Cheap run indexes were searched for `2605.15898`, the source title, normal
operators, self-adjoint operators, Hermitian operators, and smooth Banach
spaces.  No prior packet for this source or question was found.  Bounded web
search for the source title, García-Pacheco self-adjointness, Hermitian
operators, smooth Banach spaces, and `l^4` found the source paper and general
background on duality-map self-adjointness, but no separate answer to the
source's first open question.

## Human Review

Recommended verdict: likely valid counterexample/partial answer.  Reviewers
should mainly check the complex-dual pairing convention.  With the standard
linear-dual identification of `(ell_4^2)^*` with `ell_{4/3}^2`, the functional
represented by the vector `(|z_j|^2 z_j)/||z||_4^2` acts by conjugating that
representing vector, which is exactly the calculation in the packet.
