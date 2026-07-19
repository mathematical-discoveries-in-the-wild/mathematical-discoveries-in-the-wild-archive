# FDI Fell Algebras Have the Expected BCP Criterion

Status: likely valid partial result, superseded by the stronger packet
`2311.14257_fell_separable_irrep_bcp`.

Source target: arXiv:2311.14257, Question 3, asking for a noncommutative
version of the commutative `C(K)` BCP/UBCP criterion.

## Result

Let `A` be a Fell C*-algebra all of whose irreducible representations are
finite dimensional. Then

```text
A has BCP  <=>  A has UBCP  <=>  Prim(A) has a countable pi-basis.
```

This covers the finite-dimensional-irrep Fell/FDI side, including
subhomogeneous Fell algebras, without requiring the spectrum to be Hausdorff.

Note: the later atomic multiplier chart packet proves the same conclusion for
all Fell algebras with separable irreducible representations. This packet is
kept as a simpler finite-dimensional-fibre subcase.

## Key Idea

The previous local compact-chart criterion proves UBCP once `A` has a
countable primitive pi-basis of open charts on which every ambient element is a
norm-continuous compact-operator field.

FDI Fell algebras satisfy that chart hypothesis:

- Fell spectra are locally Hausdorff.
- On a Hausdorff open patch, the corresponding Fell ideal has continuous trace.
- Since irreducible representations are finite dimensional, local fibres are
  matrix algebras.
- For matrix fibres, multiplier fields are ordinary bounded norm-continuous
  matrix fields, so the multiplier obstruction disappears.

Thus the local chart theorem applies.

## Why It Matters

This pushes the positive theory past global continuous trace and past
finite-dimensional quotients. It gives a broad non-Hausdorff type-I/Fell
family where the expected BCP criterion is true.

It also sharpens the remaining obstruction: the unresolved Fell case is not
local Hausdorffness, but infinite-dimensional compact-operator fibres, where
ambient multiplier fields may be strict-continuous rather than norm-continuous.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: compiled PDF.
- `source_paper.pdf`: source paper.
- `supporting_paper_1207.2540.pdf`: Clark--an Huef--Raeburn Fell reference.
- `supporting_packet_local_compact_chart.pdf`: earlier local chart criterion.
- `figures/open_problem_crop.png`: crop of the source question.

## Review Focus

Please check:

- the refinement from countable pi-base plus locally Hausdorff spectrum to a
  countable pi-basis of Hausdorff continuous-trace trivialization patches;
- the use of finite-dimensionality to identify local multiplier fields with
  norm-continuous matrix-valued functions;
- the norm recovery of ambient elements through the local ideal multiplier
  representation.

If these pass review, the next target is the infinite-dimensional separable
irrep Fell case.
