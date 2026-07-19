# Updated Partial Report: Smooth Non-Complete Norms

Status: `partial_known_c0_with_new_reductions_likely_valid`

Source paper: Daniel Azagra, Tadeusz Dobrowolski, Miguel Garcia-Bravo,
*Smooth approximations without critical points of continuous mappings between
Banach spaces, and diffeomorphic extractions of sets*, arXiv:1811.07587.

Source question: On page 13, immediately before Lemma 2.10, the authors write
that it is not known whether every infinite-dimensional Banach space with a
`C^1` equivalent norm possesses a `C^1` smooth non-complete norm.

Current conclusion:

- The full `C^1` question is still not solved here.
- The separable compact-operator proof is correct.
- The `c0(Gamma)`-injectable / M-basis theorem is correct, but it is not new:
  the supplied audit identifies it with Dobrowolski's 1979 condition (L),
  Proposition 5.1.
- The packet now records additional partial reductions, especially the
  quotient-extension result and a reflexive-subspace route marked for careful
  human review.
- The packet also records failed full-proof routes, including the failure of
  the actual-normal lemma.

Human-review priority:

1. Check the Dobrowolski condition (L) identification.
2. Check the quotient-extension partial theorem.
3. Check the reflexive-subspace infimal-convolution smoothness step.
4. Do not promote this to full unless the general `C^1` question is closed by
   an additional argument.

Files:

- `main.tex`: updated proof/investigation packet.
- `solution_packet.pdf`: rendered packet.
- `source_paper.pdf`: arXiv:1811.07587.
- `figures/open_question_crop.png`: crop of the source question on page 13.
- `history/packet_before_literature_correction_2026_06_19/`: previous active
  packet before this literature correction.
- `provenance/superseded_packets/1811.07587_separable_smooth_noncomplete_norm/`:
  earlier separable-only packet retained as provenance.
- `evidence/extended_audit_2026_06_19/`: summary of the external audit that
  triggered this correction.
