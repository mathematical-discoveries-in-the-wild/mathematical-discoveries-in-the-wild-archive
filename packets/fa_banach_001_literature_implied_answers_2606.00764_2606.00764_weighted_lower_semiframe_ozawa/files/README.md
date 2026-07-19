# Literature-Implied Answer Packet: Complete Sequences Are Weighted Lower Semi-Frames

Status: literature-implied answer. This packet records a literature
theorem that directly answers the complete-family weighted lower
semi-frame conjecture quoted in arXiv:2606.00764 after identifying the
conjecture with a lower frame inequality for total sequences. Ozawa's
paper does not explicitly claim to solve the Balazs-Corso-Stoeva or
Zikkos formulation; it states the result as a solution to a MathOverflow
exercise. This packet is not an original proof by this pipeline.

Original source paper:
- E. Zikkos, *The Gaussian Gabor system at the critical density is a
  weighted lower semi frame*, arXiv:2606.00764.
- Local copy: `source_paper.pdf`.

Conjecture source:
- P. Balazs, M. Corso, and D. T. Stoeva, *Weighted frames, weighted
  lower semi frames and unconditionally convergent multipliers*,
  arXiv:2310.18957.
- Local copy: `supporting_paper_2310.18957.pdf`.

Supporting answer:
- N. Ozawa, *Total sequences and the lower frame inequality*,
  arXiv:2507.04899.
- Local copy: `supporting_paper_2507.04899.pdf`.
- Extracted source: `tmp/ozawa_lower_frame.tex`.
- Web status thread: <https://mathoverflow.net/questions/496725/can-any-complete-sequence-be-scaled-to-be-a-lower-frame>.

## Open Problem Closed

Conjecture 1.1 in arXiv:2606.00764, quoted from Conjecture 3.1 of
arXiv:2310.18957, asks whether every complete family in a separable
Hilbert space is a weighted lower semi-frame.

The source paper proves this for families containing a complete minimal
subfamily, and explicitly leaves open the case in which every complete
subfamily has infinite excess. It also singles out the Muntz family
`{t^{lambda_n}}` in `L^2(0,1)`, with `sum 1/lambda_n = infinity`, as an
unknown example.

## Literature-Implied Match

Ozawa proves that every total sequence `(v_n)` in a Hilbert space admits
positive numbers `lambda_n` such that

```text
||x||^2 <= sum_n lambda_n |<x, v_n>|^2
```

for every `x`, with the right-hand side allowed to be infinite. Setting
`omega_n = sqrt(lambda_n)` gives exactly the lower semi-frame inequality
for `(omega_n v_n)` with lower bound `1`. Multiplying all `lambda_n` by
any prescribed `A > 0` gives the Balazs-Corso-Stoeva formulation with
bound `A`.

Therefore the complete-family conjecture is fully answered
affirmatively by arXiv:2507.04899 after this direct reformulation. The
Muntz-family example in arXiv:2606.00764 is covered as a special case.

## Relation To The Partial Packet

The packet
`solutions/partial/2606.00764_complete_families_block_partition/`
remains a valid pipeline-derived partial criterion: countably many
complete blocks imply a weighted lower semi-frame. This
literature-implied packet supersedes it for the full conjecture because
Ozawa's theorem removes the block-partition hypothesis.

## Files

- `source_paper.pdf`: arXiv:2606.00764 PDF.
- `supporting_paper_2310.18957.pdf`: arXiv:2310.18957 PDF.
- `supporting_paper_2507.04899.pdf`: arXiv:2507.04899 PDF.
- `figures/open_problem_crop.png`: crop of the conjecture and Muntz
  example from the source paper.
- `main.tex`: human-readable status packet.
- `solution_packet.pdf`: compiled packet.
- `tmp/`: LaTeX, source, and rendering scratch files.

## Human Review

Recommended check: confirm that the word "complete" in the source
paper is used in the countable sequence/family sense of the BCS paper.
Under the cited definitions, Ozawa's theorem is an exact match.
