# Partial Result Packet: Coordinate-Commensurable Subspaces

Run: `fa_banach_001`

Result type: `partial`

Status: likely valid. This packet records a general coordinate-subspace
heredity theorem for norming Markushevich bases and combines it with the
previous finite-codimensional invariance packet.

## Source Problem

- Petr Hajek and Tommaso Russo, *Norming Markushevich bases: recent results
  and open problems*, arXiv:2402.18442.
- Local source inspected:
  `data/parsed/arxiv_sources/2402.18442/manuscript.tex`.
- Open problem: Problem 6.1, parsed source `manuscript.tex:685--691`,
  PDF page 24.

Problem 6.1 asks whether every subspace of a Banach space with a norming
M-basis again admits a norming M-basis.

## Result

Let `X` have a `lambda`-norming M-basis `{e_gamma; phi_gamma}_{gamma in Gamma}`.
For every `A subset Gamma`,

```text
X_A = closure span{e_gamma : gamma in A}
```

has the restricted `lambda`-norming M-basis

```text
{e_gamma; phi_gamma|_{X_A}}_{gamma in A}.
```

Consequently, if a closed subspace `Z subset X` is finite-dimensionally
commensurable with such a coordinate subspace, meaning that for some `A`

```text
V = Z cap X_A
```

has finite codimension in both `Z` and `X_A`, then `Z` admits a norming
M-basis.

This unifies two positive zones in the current work:

- `A = Gamma` gives the finite-codimensional heredity subcase.
- `Z = X_A` gives coordinate-generated subspaces of any norming-M-basis space,
  including the HRST coordinate subspaces.

## Proof Idea

The coordinate-subspace theorem is immediate but powerful. If `x` lies in the
closed span of `{e_gamma : gamma in A}`, then every coordinate functional
`phi_eta` with `eta notin A` vanishes on `x`, because it vanishes on the dense
linear span. Thus the full ambient norming coordinate span restricts exactly
to the span of the coordinates indexed by `A`.

For the commensurable-subspace corollary, pass from `X_A` to
`V = Z cap X_A` by finite-codimensional heredity, then pass from `V` to `Z`
by adjoining finitely many vectors and functionals on a finite-dimensional
complement.

## Scope And Limitations

- This does not solve the full arbitrary-subspace problem.
- The theorem covers subspaces aligned with a chosen ambient M-basis up to
  finite-dimensional error.
- A counterexample, if it exists, must be infinite-dimensionally skew relative
  to every norming M-basis of its ambient space.

## Evidence

- `source_paper.pdf`: arXiv:2402.18442.
- `main.tex` / `solution_packet.pdf`: formal statement and proof.
- Uses previous local packet:
  `runs/fa_banach_001/solutions/partial/2402.18442_finite_codim_heredity_norming_mbasis/`.

## Human Review Recommendation

Review as a broad partial theorem for Problem 6.1. The coordinate part is a
short direct proof; the commensurable corollary depends on the previous
finite-codimensional invariance packet.
