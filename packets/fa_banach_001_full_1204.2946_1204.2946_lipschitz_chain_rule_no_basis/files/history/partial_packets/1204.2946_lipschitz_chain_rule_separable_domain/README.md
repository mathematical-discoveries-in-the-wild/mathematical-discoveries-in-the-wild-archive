# Historical partial packet: separable-domain Lipschitz chain rule

Status: `superseded_by_full_packet`

Parent packet:
`runs/fa_banach_001/solutions/full/1204.2946_lipschitz_chain_rule_no_basis/`.

This folder preserves the immediately preceding partial result for
arXiv:1204.2946.  It proved the Lipschitz Malliavin chain-rule membership
statement for arbitrary Banach domains and the full `T_F` operator-factor
conclusion for separable domains.  The parent packet supersedes it by removing
the separability restriction.

## Historical Result

For arbitrary Banach `E_0`, UMD `E_1`, `p in (1,infty)`, Lipschitz
`phi:E_0 -> E_1`, and `F in D^{1,p}(E_0)`, the historical packet proved
`phi(F) in D^{1,p}(E_1)` and the pointwise estimate

```text
||D phi(F)(omega)||_{gamma(H,E_1)}
  <= Lip(phi) ||DF(omega)||_{gamma(H,E_0)}.
```

It then proved the operator-factor conclusion

```text
T_F: gamma(H,E_0) -> L^infty(Omega; gamma(H,E_1))
```

when `E_0` is separable, using a measurable norming-functional selector on
`gamma(H,E_0)`.

## Supersession Note

The full packet keeps the same finite-dimensional approximation and Mazur
lemma core, but replaces the separable-domain norming-functional step by a
scalar `L^infty` extension argument on the separable essential range of `DF`.
Thus this historical packet is retained only to show the route by which the
full proof was found.

## Files

- `main.tex` and `solution_packet.pdf`: reconstructed predecessor packet.
- `source_paper.pdf`: source arXiv paper.
- `figures/open_problem_crop.png`: crop of Remark 3.11.
