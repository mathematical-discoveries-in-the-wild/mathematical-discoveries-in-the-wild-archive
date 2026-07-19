# Counterexample Packet: finite-p order continuity fails for a closed subspace

Run: `fa_banach_001`

Source paper: Youssef Azouzi and Wassim Dhifaoui, "Order denseness in free
Banach lattices", arXiv:2508.11648v1.

Status: `candidate_counterexample_likely_valid`

## Classification

The supplied report is not merely the existing complemented-subspace partial
result.  It contains a candidate counterexample to the remaining finite-`p`
closed-subspace question from arXiv:2508.11648.

For `F` equal to the closed span of the Rademacher functions in `L_1[0,1]`,
so that `F` is isomorphic to `ell_2`, the inclusion-induced lattice
homomorphism

```text
FBL^(p)[F] -> FBL^(p)[L_1[0,1]]
```

is not order continuous for every `1 <= p < infinity`.  The source theorem
gives the positive result at `p = infinity`, so the packet records a sharp
finite-versus-infinite dichotomy.

## Upgrade History

The earlier packet for this arXiv id proved the complemented-range subcase.
That partial result is mathematically sound, but it is already the part of
the Oikhberg--Taylor--Tradacete--Troitsky argument retained by the corrigendum.
It has been moved out of the active `solutions/partial/` tree and preserved at:

```text
history/packets/partial_packet_2508.11648_fblp_complemented_subspace_order_continuity_2026_06_13/
```

## Evidence

- `evidence/2026_06_22_free_banach_lattice_order_continuity/free_banach_lattice_order_continuity.tex`
- `evidence/2026_06_22_free_banach_lattice_order_continuity/free_banach_lattice_order_continuity.pdf`
- `source_paper.pdf`
- `figures/open_problem_crop.png`

## Human Review Focus

Check the source-zero proposition for the block sequence in `ell_2`, the
Rademacher finite-join estimate in `FBL^(p)[L_1]`, the functorial orientation
of the inclusion map, and the nonzero lower-bound argument using evaluation
at `r_0`.  These are the genuine moving parts of the counterexample.
