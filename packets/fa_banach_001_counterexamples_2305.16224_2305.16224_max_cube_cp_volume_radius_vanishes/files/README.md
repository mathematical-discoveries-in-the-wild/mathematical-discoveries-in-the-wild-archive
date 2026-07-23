# Max-cube CP volume radius vanishes

Status: candidate full negative answer, likely valid pending expert review.

Klep, Štrekelj, and Zalar ask in Remark 1.5(1) of arXiv:2305.16224
whether the portion of the max-norm unit ball occupied by completely positive
matrices stays large as the matrix size grows. In the nontrivial normalized
volume-radius interpretation used in the surrounding discussion, the answer is
no. In fact, even the larger positive-semidefinite cone occupies max-cube
volume radius `O(n^{-1/2})`.

The proof disintegrates the PSD part of the max cube over its diagonal. Each
fiber is a diagonally scaled copy of the correlation elliptope. Schur
complements bound the volume of the `n`-dimensional elliptope by the product of
the Euclidean unit-ball volumes in dimensions `1,...,n-1`, whose normalized
product decays as `n^{-1/2}`.

Files:

- `solution_packet.pdf`: complete review packet.
- `source_paper.pdf`: source/open-problem paper.
- `figures/open_problem_crop_page4.png` and
  `figures/open_problem_crop_page5.png`: the two-page source passage.
- `verification.md`: proof audit and review focus.
- `code/verify_volume_bound.py`: numerical evaluation of the proved bound.
- `code/crop_source.py`: reproducible source-page rendering and crops.

Human review recommendation: verify the change of variables from PSD matrices
to diagonal variables plus a correlation matrix, and confirm that “does not
get arbitrarily small” is intended in the normalized volume-radius sense. The
literal unnormalized probability already tends to zero from
`CP_n subset NN_n`; the theorem proves the stronger and mathematically
substantive normalized statement also tends to zero.
