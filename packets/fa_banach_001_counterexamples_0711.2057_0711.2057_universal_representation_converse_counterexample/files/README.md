# Counterexample: cyclic-universal need not be small-universal

Status: candidate counterexample, likely valid.

Source paper: Matthias Neufang and Volker Runde, *Column and row operator
spaces over QSL_p-spaces and their use in abstract harmonic analysis*,
arXiv:0711.2057.

Targeted remark: after Definition 3.7, the source notes that every
`p`-universal representation in the paper's stronger sense is `p`-universal
in the older sense of Runde's Definition 4.5, and says that the converse was
not known.

Result: the converse is false. For the trivial locally compact group
`G={e}`, the one-dimensional trivial representation on `C` contains every
cyclic representation in the older sense, because cyclicity for `L_1(G)=C`
forces the representation space to be one-dimensional. However, it does not
contain the small representation on `ell_p^2`, which is a `QSL_p`-space of the
allowed cardinality.

Files:

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:0711.2057 source paper.
- `supporting_paper_0402018.pdf`: Runde's paper containing the older
  cyclic-universal definition.
- `figures/open_problem_crop.png`: crop of Definition 3.7 and the target
  remark from page 13 of the source PDF.

Scope limitation: this answers only the first definitional converse question
in the paper. It does not address the later questions about Herz--Schur
multipliers, completely bounded inclusions, or complete isometries for
amenable groups.
