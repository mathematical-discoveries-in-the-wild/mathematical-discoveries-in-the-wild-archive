# Countable Spectral Extensions: One Positive Case and Empty-Interior Obstructions

Result type: `partial`

Status: candidate partial result, likely valid pending human review.

Source paper:

- Ryshard-Pavel Kostecki, "Vaĭnberg--Brègman relative entropy and
  quasinonexpansive operators", arXiv:2511.14873.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

Remark 4.21(iii) asks for examples of unitarily invariant
Euler--Legendre functions `f o lambda~` on suitable separable reflexive
compact-operator ideals, and asks in particular whether the countable
extensions of the finite spectral examples in Proposition 4.17 work.

This packet gives a direct yes/no classification for the most literal
countable extensions of the Proposition 4.17 list in infinite dimension:

- the full-domain norm-power example extends positively to Schatten
  `S_p`, `1 < p < infinity`;
- the positive-cone and operator-interval entropy examples have empty
  norm interior in every infinite-dimensional compact-operator ideal, so
  they cannot satisfy Proposition 4.20's nonempty-interior hypotheses.

This includes the Kullback--Leibler, Burg/Pinsker, Fermi--Dirac, and
Tsallis/power positive-domain examples. The broad problem of finding
new non-`Psi_varphi` examples remains open.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: crop of Remark 4.21(iii), page 67.
- `tmp/`: LaTeX build intermediates.

## Human Review Notes

The positive case is the standard Legendre geometry of
`(1/p)||x||_p^p` on `ell_p` and `S_p`, transported through the spectral
map. The negative cases are elementary but important for target triage:
in an infinite-dimensional Hilbert space, every positive compact operator
has spectrum accumulating at zero. A tiny negative rank-one perturbation
can therefore be made arbitrarily small in any compact ideal norm while
leaving the positive cone. Hence the positive cone, strictly positive
compact cone, and compact operator interval have empty norm interior.

The result does not rule out full-domain countable examples, nor more
subtle renormalised domains/topologies. The main examples problem remains
open.
