# 1203.5498: removing the Kato-Beurling `z^K` factor

Result type: `full`

Status: candidate full solution, likely valid pending human review.

Source paper:

- Stephan Fackler, "Regularity of Semigroups via the Asymptotic Behaviour at Zero", arXiv:1203.5498.
- Local source PDF: `source_paper.pdf`
- Open-question evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Fackler's Corollary 2.5(b) proves that a holomorphic `C_0`-semigroup satisfies

```text
limsup_{t downarrow 0} ||(T(t)-Id)^N T(t)^K||^{1/N} < 2
```

for large `N` after adding a large smoothing factor `T(t)^K`. Remark 2.6 asks
whether this extra factor can be omitted in general.

This packet proves that it can. For every holomorphic `C_0`-semigroup on an
arbitrary Banach space, there is `N` such that

```text
limsup_{t downarrow 0} ||(T(t)-Id)^N||^{1/N} < 2.
```

The proof first treats bounded holomorphic semigroups by a sectorial contour
estimate for `f_N(z)=(e^{-z}-1)^N`, obtaining a uniform bound of the form
`1 + C log(N) q^N` with `q<2`. A standard exponential rescaling transfers the
estimate to general holomorphic semigroups.

## Files

- `main.tex`: self-contained LaTeX proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of Corollary 2.5 and Remark 2.6 from page 4.
- `code/render_open_problem_crop.py`: script used to regenerate the crop.
- `tmp/`: LaTeX build intermediates.

## Literature Check

Local duplicate checks covered `1203.5498`, `additional factor`, `z^K`,
`Kato-Beurling`, and the finite-difference expressions in the run registry,
solutions, attempts, and proof-gap indexes.

A bounded web search on July 18, 2026 used exact phrases around
`additional factor z^K Kato-Beurling`, the displayed limsup with `T(t)^K`,
Pazy/Kato finite-difference terminology, and the source paper title. It found
adjacent work on Besov calculi and quantitative estimates for bounded
holomorphic semigroups, but no later paper explicitly answering Fackler's
Remark 2.6.

## Human Review Notes

The main review points are:

- verify the sectorial functional-calculus estimate for bounded holomorphic
  semigroups, especially the handling of the finite limit at infinity;
- check the scalar bound for `(1-e^{-re^{i psi}})^N-1` on the tail of the
  contour;
- confirm the exponential-rescaling step from general holomorphic semigroups
  to bounded holomorphic semigroups on a smaller sector.
