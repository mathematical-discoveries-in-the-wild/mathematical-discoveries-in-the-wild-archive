# Sharp perturbation dichotomy for independent-island phase retrieval

Status: `sharp_dichotomy_likely_valid`

Source: W. Alharbi, D. Freeman, D. Ghoreishi, C. Lois, and S. Sebastian,
*Stable phase retrieval and perturbations of frames*, arXiv:2212.13681.
The paragraph on PDF page 3 asks how perturbations affect stable recovery when
signals have separated islands and relative phases between islands are
intentionally ignored.

## Claimed contribution

There is a sharp distinction between arbitrary and structure-preserving
perturbations.

### Negative half: cross-island perturbations

The unrestricted perturbation principle is false, already for two
one-dimensional islands over either the real or complex scalars.

Let `H=F^2`, let `X=(e1,e2)`, and identify two signals when their two
coordinate magnitudes agree (equivalently, allow an independent unimodular
phase on each coordinate). The quotient metric is

```text
d_I(x,y)^2 = (|x1|-|y1|)^2 + (|x2|-|y2|)^2.
```

The magnitude analysis map of `X` is an exact isometry for this metric, so
`X` does 1-stable phase retrieval modulo independent island phases.

For any `epsilon>0`, perturb only the first frame vector:

```text
Y_epsilon = (e1 + epsilon e2, e2).
```

The squared perturbation size is exactly `epsilon^2`, and `Y_epsilon` remains
a basis. Nevertheless, for

```text
x = e2,                 z = -2 epsilon e1 + e2,
```

the two magnitude measurement vectors are both `(epsilon,1)`, while
`d_I(x,z)=2 epsilon>0`. Thus the perturbed frame is not even injective modulo
the enlarged equivalence relation. No positive stability constant survives.

The same construction embeds into any number of separated orthogonal islands
at least two.

### Positive half: island-preserving perturbations

Let a finite-dimensional Hilbert space have an orthogonal decomposition
`H=direct_sum H_k`, and partition the frame measurements so that the vectors
indexed by `J_k` lie in `H_k`. Suppose the frame has bounds `A,B` and does
`C`-stable retrieval modulo one independent phase on each island. If the
perturbed vector indexed by `J_k` remains in `H_k` and

```text
sum_j ||x_j-y_j||^2 < nu < 1/(16 C^4 B),
```

then the perturbed frame does stable independent-island retrieval with

```text
C_nu = C (1-4 C^2 sqrt(nu B))^(-1/2).
```

It also has the standard perturbed frame bounds

```text
A(1-sqrt(nu/A))^2,     B(1+sqrt(nu/B))^2.
```

The proof restricts the original inequality to each island, applies the source
perturbation theorem blockwise, and recombines the squared estimates using
orthogonality. There is no dimension or number-of-islands loss.

## Interpretation and scope

Together the two theorems answer the basic orthogonal-island perturbation
question sharply. The obstruction in the negative half is geometric:
the original measurement map is invariant under independent island phases,
whereas an arbitrarily small cross-island component destroys compatibility
between that fixed quotient and the measurement fibers.

Island localization is also exactly sufficient: every sufficiently small
localization-preserving perturbation obeys the explicit positive theorem
above. The remaining scope consists of different models—approximately
separated islands, signal-dependent decompositions, changing equivalence
relations, or additional mixed measurements—not the formal orthogonal-block
model settled here.

## Verification

The exact checker verifies the perturbation size, both measurement vectors,
the positive quotient distance, and the frame determinant:

```bash
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2212.13681_independent_island_phase_instability_under_cross_perturbations/code/verify_counterexample.py
```

## Novelty check

A bounded search on 2026-07-22 checked the four lightweight run indexes and
current arXiv searches for combinations of `independent phases`, `componentwise
phase`, `separated islands`, `frame perturbation`, and `phase retrieval`.
It found the source paper, block-based phase retrieval, and the established
separated-island stability literature, but no matching perturbative dichotomy.
This is evidence, not a guarantee, of novelty.

Files:

- `main.tex`, `solution_packet.pdf`: proof packet.
- `source_paper.pdf`: arXiv:2212.13681.
- `figures/open_problem_crop.png`: source PDF page 3.
- `code/verify_counterexample.py`: exact arithmetic check.
