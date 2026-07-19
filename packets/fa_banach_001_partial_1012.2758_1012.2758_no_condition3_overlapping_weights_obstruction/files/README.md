# Partial packet: condition-(3)-free overlapping weights obstruction

Status: `partial_result_likely_valid`

Source: S. A. Argyros and G. Petsoulas, *A c_0 saturated Banach space with tight structure*, arXiv:1012.2758.

## Result

The packet records a sharp obstruction for the variant of the norming set obtained by deleting condition (3) from the definition of `G_0`.

In the condition-(3)-free core, for every finite number of different even weights there is a unit basis vector `e_t` and functionals of those pairwise different weights, all supported on the same coordinate, which evaluate `e_t` above any prescribed sufficiently small odd-level threshold. Thus bounded `G_0^-` norm alone does not forbid high-multiplicity overlapping different-weight families.

## Scope

This does not solve whether the original space `X_0` is strictly quasi-prime, and it does not disprove all further tight properties of the condition-(3)-free variant. It does rule out the most direct no-overlap repair of the proof of the key averaging proposition: after removing condition (3), the remaining even operations only combine successive functionals and cannot justify the Hilbertian combination of overlapping different-weight functionals used in the source proof.

## Files

- `main.tex`: review note with theorem, proof, limitations, and source citation.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: source paper PDF.
- `figures/open_problem_crop.png`: crop of the source passage saying condition (3) is critical and the variant is not understood.
- `code/make_open_problem_crop.py`: reproducible crop script.
