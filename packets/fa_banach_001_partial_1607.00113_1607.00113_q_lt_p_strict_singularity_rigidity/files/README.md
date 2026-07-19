# Partial packet: strict-singularity rigidity for `H^p -> H^q`, `q < p`

Source paper: arXiv:1607.00113, *Rigidity of composition operators on the
Hardy space `H^p`*.

Result type: partial answer to Problem 4.3(1).

## Target

Problem 4.3(1) asks whether there are analogues of the paper's main rigidity
theorems for composition operators

```text
C_phi : H^p -> H^q
```

when `p != q`.

## Packet Result

For every `1 <= q < p < infinity` and every analytic self-map `phi` of the
unit disk, the following are equivalent:

- `C_phi : H^p -> H^q` is compact;
- `C_phi : H^p -> H^q` is strictly singular;
- `C_phi : H^p -> H^q` is `ell^2`-singular;
- `m(E_phi)=0`, where `E_phi` is the boundary contact set.

Equivalently, if `C_phi : H^p -> H^q` is noncompact in the `q < p` regime,
then it fixes an isomorphic copy of `ell^2`.  More concretely, there is a
lacunary sequence `(n_k)` such that

```text
span{z^{n_k}} is isomorphic to ell^2 in H^p
```

and `C_phi` is bounded below on that subspace as an operator into `H^q`.

## Files

- `solution_packet.pdf`: human-readable proof packet.
- `main.tex`: LaTeX source.
- `source_paper.pdf`: original arXiv source paper.
- `figures/open_problem_crop.png`: rendered page containing Problem 4.3.

## Status

This is a partial result only.  It settles the `q < p` branch of the first open
problem in the finite-exponent range, but it does not address the harder
integrability-improving case `p < q`.
