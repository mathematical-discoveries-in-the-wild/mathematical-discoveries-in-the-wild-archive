# General multi-norm Littlewood--Paley families admit Calderón duals

Result type: `full`

Status: candidate full solution of the tensor-free Calderón-family question,
likely valid pending human review.

Source paper:

- Agnieszka Hejna, Alexander Nagel, and Fulvio Ricci,
  “Littlewood-Paley square functions and the local Hardy space for Multi-Norm
  Structures on R^d,” arXiv:2507.09399v1 (2025).
- The open question is Section 13, item 4, page 63.
- Local source PDF: `source_paper.pdf`.
- Evidence crop: `figures/open_problem_crop.png`.

## Claimed contribution

The source asks whether the tensor-product assumption in Section 4.2 can be
removed while retaining uniform Schwartz bounds, the coordinate cancellation
conditions, and the Littlewood--Paley reproducing identity.

The packet proves that every such family has an associated Calderón family.
More strongly, the dual functions may be chosen with compact Fourier support
away from every marked coordinate hyperplane, so they have cancellation of
all orders in every required variable.

The construction is an exact localized frame inverse. Smooth cutoffs retain
only atoms whose enlarged frequency tubes meet the frequency point. The
partition identity and an off-tube tail estimate give a uniformly positive
localized frame symbol

`A(xi) = sum_L theta_L(xi) |hat(Psi_L)(2^{-L}xi)|^2`.

Dividing by `A` yields the duals. Fixed-overlap geometry makes the normalized
dual symbols uniformly compactly supported and uniformly smooth.

## Scope

This settles the intrinsic tensor-free statement from Section 4.2: existence
of an associated Calderón reproducing family. The tensor-specific rectangular
partial-sum formula involving `Phi_L` is not a statement about an arbitrary
family and is not claimed. The broader question in the next sentence of item
4---a simple class of mutually L^1-equivalent square functions containing both
tensor and convolution types---is also not claimed here.

## Files

- `main.tex`: self-contained proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: original arXiv PDF.
- `figures/open_problem_crop.png`: full-width crop of Section 13, item 4.
- `tmp/`: build products and the rendered source page used for cropping.

## Verification and reviewer focus

The algebraic identity is exact after defining the localized frame symbol.
The main point for expert review is the adapted tail lemma: uniform Schwartz
bounds plus cancellation in the marked variables imply summable geometric
decay outside fixed enlargements of the multi-norm tubes. The proof reduces it
to geometric series after partitioning the index set by marked partitions and
using the scale relations already proved in the source paper.

No numerical computation is part of the proof.

## Bounded novelty check

On 2026-07-21, searches were run for the exact question sentence, the title
and arXiv id, “multi-norm Calderón reproducing formula non-tensor,” “multi-norm
Littlewood-Paley family,” and the author/topic combinations Hejna--Calderón and
Ricci--multi-norm. The searches returned arXiv:2507.09399 and general adjacent
Littlewood--Paley literature, but no later paper or revision answering this
question. Novelty confidence is therefore moderate, not definitive.

