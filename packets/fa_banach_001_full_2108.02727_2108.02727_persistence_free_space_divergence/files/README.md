# Full solution: an explicit flux model for persistence diagrams

status: full_solution_likely_valid

source: Chad Giusti and Darrick Lee, *Signatures, Lipschitz-free spaces, and
paths of persistence diagrams*, arXiv:2108.02727.

target: The conclusion (p. 26) asks for an explicit description of the
Lipschitz-free space of the quotient metric space of a metric pair and asks
whether known representations of `F(R^N)` can be adapted to persistence
diagrams.

packet: `runs/fa_banach_001/solutions/full/2108.02727_persistence_free_space_divergence/`

ledger: `runs/fa_banach_001/ledger/results/2108.02727_persistence_free_space_divergence.json`

## Result

For every metric space `X` and nonempty closed `A`, collapsing `A` commutes
isometrically with forming the Lipschitz-free space:

```text
F(X/A) = F(X) / closure(span{delta(a): a in A}).
```

For ordinary persistence diagrams, rotate the birth-death half-plane to
`H = R x (0,infinity)` so that the diagonal is its boundary. Then

```text
F(cl(H)/boundary(H)) = L1(H;R^2) / {g : div(g)=0 in H}.
```

Thus, if `D,E` are finite diagrams and `nu_D,nu_E` their counting measures in
`H`,

```text
partial_W1(D,E) = inf ||g||_1 over div(g) = nu_E - nu_D in H.
```

This is an exact Beckmann/flux representation. Flux can exit through the
collapsed diagonal, which is why the divergence condition is imposed only in
the open half-plane.

## Main idea

A Lipschitz function on `X/A` is exactly a Lipschitz function on `X` that
vanishes on `A`, with the same Lipschitz constant. Duality gives the general
quotient identity. Applying the Cuth-Kalenda-Kaplicky representation for a
convex Euclidean domain shows that the new kernel is the annihilator of
zero-boundary Lipschitz functions. On a half-plane, this annihilator is exactly
the space of vector fields with zero distributional divergence in the
interior.

## Verification and novelty

- The source quotient metric and p. 26 question were checked directly.
- Theorem 1.1 of arXiv:1610.03966 was checked directly, including its
  zero-extension boundary convention.
- The collapsed-boundary kernel is proved separately in the packet.
- Exact and structural literature searches found the ambient Euclidean
  representation but no collapsed-diagonal or persistence-diagram flux
  formula.
- The general quotient identity may be folklore; novelty confidence is
  moderate. Proof confidence is high.

## Scope

The result is an exact infinite-dimensional quotient representation, not a
unique or finite-dimensional coordinate system. It addresses the `p=1`
geometry linearized by Lipschitz-free spaces, not `p>1` Wasserstein metrics.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: compiled and visually verified packet.
- `source_paper.pdf`: arXiv:2108.02727.
- `supporting_paper_1610.03966.pdf`: the decisive Euclidean representation.
- `figures/open_problem_crop.png`: source question from p. 26.
