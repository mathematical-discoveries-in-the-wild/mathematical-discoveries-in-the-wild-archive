# Non-Uniform Besselian Crossnorm Preserving Unconditional Bases

Result type: `partial`

Status: literature-implied partial answer, source-backed and suitable for
human review.

Source paper:

- Rafik Karkri and Samir Kabbaj, "A New Crossnorm That Preserves
  Unconditional Bases in Banach Spaces", arXiv:2506.22522.
- Local source PDF: `source_paper.pdf`
- Open-problem evidence crop: `figures/open_problem_crop.png`

## Claimed Contribution

The source paper asks whether there is a tensor norm, equivalently a
uniform reasonable crossnorm on all algebraic tensor products of Banach
spaces, that preserves unconditional Schauder bases.

This packet records the source paper's strong non-uniform partial answer:
for each fixed pair of Banach spaces with chosen unconditional Schauder
bases, the paper constructs a basis-dependent Besselian reasonable
crossnorm `alpha^{Bess}` such that the square-ordered tensor product
sequence is again an unconditional Schauder basis in the completed tensor
product.

The packet does not claim the original uniform tensor-norm question is
settled. The source explicitly states that the constructed crossnorm is
generally non-uniform and that the original uniform tensor-norm existence
problem remains open.

## Files

- `main.tex`: self-contained LaTeX packet source.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: local copy of the original arXiv PDF.
- `figures/open_problem_crop.png`: screenshot crop from page 1 showing
  the open question and the non-uniform construction claim.
- `tmp/`: LaTeX build intermediates and disposable render outputs.
- `code/README.md`: notes that no computation was used.

## Human Review Notes

The main verification points are source-theoretic rather than
computational:

- Proposition `New-crossnorm` proves that the Besselian norm is a
  reasonable crossnorm for the equivalent Besselian renormings.
- Theorem `tensor.bess.is.bess` proves that, for USBs, the tensor product
  sequence is a USB in the corresponding completed tensor product.
- A later remark and example show that the crossnorm is generally not
  uniform, so the result is only a non-uniform partial answer.
