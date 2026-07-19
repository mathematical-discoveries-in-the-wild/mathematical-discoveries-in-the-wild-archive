# Partial Packet: `c0(Gamma)` Projective Tensor WLD Subcase

Run: `fa_banach_001`

Status: candidate partial result, likely valid.

Source paper: A. Aviles, G. Martinez-Cervantes, J. Rodriguez,
A. Rueda Zoca, *Topological properties in tensor products of Banach spaces*,
arXiv:2202.00371.

## Target

Question 8(b) asks whether `X \hat\otimes_\pi Y` is WLD whenever `X` and `Y`
are WLD and one of them has the Dunford-Pettis property.

## Result

For every index set `Gamma` and every WLD Banach space `Y`,

```text
c0(Gamma) \hat\otimes_\pi Y
```

is WLD. Since `c0(Gamma)` is WLD and has the Dunford-Pettis property, this is a
positive subcase of Question 8(b).

## Key Point

Every operator from a WLD Banach space into `ell_1(Gamma)` has separable
range. Indeed, the range closure is again WLD, while every nonseparable
subspace of `ell_1(Gamma)` contains `ell_1(omega_1)`, which fails Corson's
property (C). This also handles operators `c0(Gamma) -> Y*` after applying the
source paper's WLD weak-star-to-norm separability lemma.

## Contents

- `source_paper.pdf`: local copy of arXiv:2202.00371.
- `figures/open_question_page28.png`: rendered source page containing the open
  questions.
- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.

## Limitations

This does not solve Question 8(b) in ZFC for arbitrary WLD spaces with the
Dunford-Pettis property. It proves the important canonical nonseparable
Dunford-Pettis factor `c0(Gamma)`. A later lane-10 packet records a
complementary CH counterexample via `L1(mu)` factors:
`solutions/counterexamples/2202.00371_ch_l1_bochner_wld_dpp_counterexample/`.

## Human Review Recommendation

Review as a likely valid partial result. The main proof point to check is the
standard lemma that every nonseparable subspace of `ell_1(Gamma)` contains an
isomorphic copy of `ell_1(omega_1)`.
