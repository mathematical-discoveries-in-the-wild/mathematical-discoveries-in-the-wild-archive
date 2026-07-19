# Literature-Already-Answered Packet: Complex Hilbert Plane Strict Inequality

Run: `fa_banach_001`

Result type: `literature_already_answered`

## Original Problem Source

- Ruidong Wang, Xujian Huang, Dongni Tan, *On the numerical radius of
  Lipschitz operators in Banach spaces*, arXiv:1211.5753.
- Local source archive: `source_1211.5753.tex.gz`.

The final problem in Section 4 asks whether there is a Banach space `X` such
that

```text
n_L(X) < n(X).
```

The question is stated for real or complex Banach spaces under the paper's
Lipschitz numerical range definition.

## Supporting Answer Source

- Antonio Perez-Hernandez, *Lipschitz vs Linear Numerical Index in certain
  Banach spaces*, arXiv:2507.18208.
- Local source archive: `supporting_source_2507.18208.tar.gz`.

## Status

The 2012 problem is answered affirmatively in the complex case by
arXiv:2507.18208.

The later paper explicitly says that the answer depends on the scalar field.
For the complex Hilbert plane `X = C^2` with its usual Euclidean norm, it
recalls the classical value

```text
n(C^2) = 1/2
```

and exhibits the real-linear Lipschitz map

```text
F(z_1,z_2) = (conj(z_2), -conj(z_1)).
```

This map has Lipschitz norm `1`, but its Lipschitz numerical range is `{0}`:
for a unit vector `y=(w_1,w_2)`, the unique norming complex-linear functional
is `x*(z_1,z_2)=conj(w_1)z_1+conj(w_2)z_2`, and then

```text
x*(F(y)) = conj(w_1)conj(w_2) - conj(w_2)conj(w_1) = 0.
```

Hence `n_L(C^2)=0`, so

```text
n_L(C^2) = 0 < 1/2 = n(C^2).
```

## Verification Notes

- The definitions match the 2012 source: the 2025 paper uses unit functionals
  norming `x_1-x_2`, which is equivalent to the 2012 denominator
  `||x_1-x_2||^2` formulation with `(x_1-x_2)^* in D(x_1-x_2)`.
- The map is not complex-linear, but the 2012 Lipschitz operator algebra
  consists of all Lipschitz maps fixing the origin, not only complex-linear
  maps. Thus it is admissible for `n_L`.
- The same 2025 source says that in the real case no example was known there,
  and proves equality for real separable spaces and real dual spaces. This
  packet records only the complex affirmative answer to the original broad
  question.

## Search Bounds

- Checked the cheap run indexes for `1211.5753`, the title, and core phrases
  including `Lipschitz numerical index`, `n_L(X)<n(X)`, and `numerical radius`.
- Relevant local hits were later partial packets for the real 2025 equality
  question and a 2021 absolute-sum Lipschitz numerical index packet; neither
  was an exact prior packet for arXiv:1211.5753.
- Read the original problem in `data/parsed/arxiv_sources/1211.5753/source.tex`
  and the complex-case passage in
  `data/parsed/arxiv_sources/2507.18208/main_MJM.tex`.
- Web/literature search found the published Choi--Jung--Tag 2025 Collectanea
  Mathematica paper on the Lipschitz numerical index, cited by the 2025
  source, and local source search found the decisive arXiv:2507.18208 passage.

## Files

- `README.md`: this packet summary.
- `main.tex`: compact literature-status note.
- `solution_packet.pdf`: rendered status note, if LaTeX rendering succeeds.
- `source_1211.5753.tex.gz`: original arXiv source archive.
- `supporting_source_2507.18208.tar.gz`: later arXiv source archive.
- `tmp/`: LaTeX build output.

## Human Review Recommendation

Verify that the scalar-field convention in the 2012 source allows real-linear
Lipschitz self maps on a complex Banach space, as its definition of
`Lip_0(X)` indicates. Under that convention the complex Hilbert plane is a
literal affirmative answer.
