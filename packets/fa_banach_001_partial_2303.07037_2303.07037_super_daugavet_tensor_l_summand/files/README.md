# Partial Result: Super Daugavet Tensor Transfer

Run: `fa_banach_001`

Source paper: Rainis Haller, Johann Langemets, Yoel Perreau, and Triinu
Veeorg, "Unconditional bases and Daugavet renormings", arXiv:2303.07037.

Target: the Section 3 sentence asking whether super Daugavet points pass to
projective tensor products similarly to ordinary Daugavet points.

Status: strengthened partial packet. The general tensor-transfer question is
still open in this packet, but the earlier L-summand result is now absorbed
into a broader report with several positive subcases and a sharper obstruction.

## Main Claims

The packet records the following.

- The previous one-dimensional L-summand theorem is correct, but its core
  two-coordinate `ell_1` stability lemma is already known.
- Arbitrary `ell_1` sums preserve points assembled from super Daugavet
  coordinates.
- A later vector-valued `L_1` characterization implies that, if `x` is super
  Daugavet in `X`, then `x tensor g` is super Daugavet in
  `X \widehat{\otimes}_pi L_1(mu)` for every `g` in the unit sphere of
  `L_1(mu)`.
- If both factors are ccs Daugavet points, then their elementary tensor is a
  ccs Daugavet point, hence super Daugavet.
- For two super Daugavet points, the desired tensor conclusion holds locally
  in every weak neighborhood centered at an elementary tensor.

The remaining obstruction is the genuinely non-elementary case: a weakly open
subset of the projective tensor ball can be centered at a non-elementary tensor
and contain no elementary tensors.

## Packet Files

- `source_paper.pdf`: local copy of the arXiv source paper.
- `figures/open_problem_crop.png`: crop of the tensor-transfer open sentence.
- `main.tex`: active strengthened proof packet.
- `solution_packet.pdf`: rendered active proof packet.
- `history/previous_l_summand_packet_2026_06_16/`: previous narrower packet.
- `evidence/supplied_super_daugavet_tensor_report_2026_06_22/`: supplied
  report used to update the active packet.

## Human Review Recommendation

The earlier L-summand part is straightforward. The most important checks are
the arbitrary `ell_1`-sum net argument, the ccs tensor-transfer theorem, and
the local elementary-target theorem. Also verify the literature distinction:
the scalar `L_1` conclusion is recorded as a consequence of later published
work, while the ccs/local results are proposed here and should be reviewed as
new proof content.
