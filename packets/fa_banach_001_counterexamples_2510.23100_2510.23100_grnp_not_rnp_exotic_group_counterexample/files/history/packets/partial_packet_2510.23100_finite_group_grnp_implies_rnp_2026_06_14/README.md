# Finite-Group `G`-RNP Implies RNP

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Sheldon Dantas, Michal Doucha, Mingu Jung, Tomas Raunig, "Group
  equivariant Radon-Nikodym Property and its characterizations",
  arXiv:2510.23100.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper asks in Problem 8.2 whether the dotted implications in its
summary diagram hold. This packet proves one finite-group subcase of the
dotted implication

```text
G-RNP => RNP.
```

If `G` is a finite Hausdorff topological group acting by linear isometries on
a Banach space `X`, then `X` having the `G`-RNP forces `X` to have the
classical RNP.

The proof induces an arbitrary vector measure `m` on `(Omega,Sigma,mu)` to a
`G`-equivariant vector measure on the finite disjoint union `G x Omega`.
The `G`-RNP gives a density on the union; restricting the density to any
single positive-measure sheet `{g} x Omega` recovers a Radon-Nikodym density
for `m`.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of Problem 8.2 on page 34.
- `tmp/`: LaTeX build intermediates and disposable files.

## Human Review Notes

The proof is narrow but checkable. The finite-group hypothesis is essential to
the written argument because singleton sheets have positive measure. The packet
does not settle the same implication for infinite compact or general
topological groups.

No external literature search was performed for this partial subcase; the run
indexes and the source-paper neighborhood were checked for duplicates and for
same-paper resolution.
