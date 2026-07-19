# Candidate Partial Result: Block Partitions Give Weighted Lower Semi-Frames

Source paper: E. Zikkos, *The Gaussian Gabor system at the critical
density is a weighted lower semi frame*, arXiv:2606.00764.

Supporting conjecture source: P. Balazs, M. Corso, and D. T. Stoeva,
*Weighted frames, weighted lower semi frames and unconditionally
convergent multipliers*, arXiv:2310.18957.

Result type: `partial`

Status: candidate partial result, likely valid, pending human review.

## Open Question

Conjecture 1.1 in arXiv:2606.00764, quoted from Conjecture 3.1 of
arXiv:2310.18957, asks whether every complete family in a separable
Hilbert space is a weighted lower semi-frame.

The source paper explicitly marks the conjecture as only partially
answered by its complete-minimal subfamily criterion, and singles out the
remaining infinite-excess case. It also asks whether the Muntz family
`{t^{lambda_n}}` in `L^2(0,1)`, with `sum 1/lambda_n = infinity`, is a
weighted lower semi-frame.

## Candidate Contribution

If a complete sequence `(f_n)` in a separable Hilbert space admits a
partition of the index set into countably many disjoint blocks
`I_j` such that each subfamily `(f_n)_{n in I_j}` is complete, then
`(f_n)` is a weighted lower semi-frame.

More precisely, for every lower bound `A > 0` one can choose positive
weights so that

```text
sum_n |<f, omega_n f_n>|^2 = infinity
```

for every nonzero vector `f`. Under the lower semi-frame convention in
the cited papers, this implies the lower frame inequality with bound
`A`.

As an application, the Muntz family example from arXiv:2606.00764 is a
weighted lower semi-frame whenever `sum 1/lambda_n = infinity`: partition
the divergent positive series into countably many divergent subseries,
use the Muntz-Szasz theorem to make each block complete, and apply the
block-partition criterion.

## Why This Is Only Partial

This does not prove the full Balazs-Corso-Stoeva conjecture. The proof
requires a countable partition into complete subfamilies, or equivalently
enough disjoint complete blocks to build finite-dimensional projections
converging strongly to the identity. The source paper's remaining
infinite-excess case does not automatically provide such a partition.

The result is full for the Muntz-family example highlighted in the
source paper, but partial relative to the general complete-family
conjecture.

## Files

- `source_paper.pdf`: arXiv:2606.00764 PDF.
- `supporting_paper_2310.18957.pdf`: arXiv:2310.18957 PDF.
- `figures/open_problem_crop.png`: crop of the conjecture and Muntz
  example from the source paper.
- `main.tex`: solution packet source.
- `solution_packet.pdf`: rendered packet.
- `tmp/`: LaTeX and source-rendering intermediates.

## Verification Notes

The proof is purely analytic. The key checks are:

- finite spanning families give positive lower frame constants on their
  finite-dimensional spans;
- finite spans chosen from complete blocks yield orthogonal projections
  converging strongly to the identity;
- the cited lower semi-frame definitions allow the coefficient sum to be
  infinite, which trivially satisfies any finite lower bound.

## Human Review

Recommended check: verify the lower semi-frame convention and the exact
Muntz-Szasz completeness criterion used in arXiv:2606.00764. The packet
should not be promoted to `full` unless the block-partition hypothesis is
removed or proved for all complete families in the remaining case.
