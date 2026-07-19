# Counterexample: a Banach-space affine isometry with no escape-direction limit

status: counterexample_likely_valid

source: Andres Navas, *Some examples of affine isometries of Banach spaces
arising from 1-D dynamics*, arXiv:2501.12120.

packet: `runs/fa_banach_001/solutions/counterexamples/2501.12120_l1_bilateral_shift_no_escape_direction/`

ledger: `runs/fa_banach_001/ledger/results/2501.12120_l1_bilateral_shift_no_escape_direction.json`

## Claim

There is a surjective affine isometry `I` of a Banach space and a vector `v`
such that the normalized orbit `I^n(v)/n` does not converge in norm.

The example is on `ell_1(Z)`. Let `S(e_k)=e_{k+1}` be the bilateral shift and
define

```text
I(x) = Sx + e_0.
```

Then `I` is a surjective affine isometry, but

```text
I^n(0)/n = (e_0 + ... + e_{n-1})/n
```

is not Cauchy, since the distance between the `n` and `2n` terms is exactly
`1`.

## Source Target

After discussing the finite-dimensional fixed-point/nonzero-drift dichotomy,
the source paper notes that vector convergence of `I^n(v)/n` is known in
Hilbert and reflexive settings, gives a non-surjective `ell_1` isometric-map
example, and then says that the corresponding situation for Banach-space
isometries is unclear.

This packet supplies a genuine surjective affine isometry example.

## Files

- `main.tex`: full counterexample note.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:2501.12120 source paper.

No crop is included because local Poppler tools (`pdftotext`, `pdftoppm`,
`pdfinfo`) were unavailable; the packet gives the exact source section and
transcribed passage.
