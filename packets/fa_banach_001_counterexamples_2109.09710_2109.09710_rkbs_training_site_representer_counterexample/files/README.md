# Counterexample packet: RKBS representers need not use training-site atoms

Status: likely valid counterexample to the classical RKHS-style training-site strengthening.

Source target: Francesca Bartolucci, Ernesto De Vito, Lorenzo Rosasco, and Stefano Vigogna, "Understanding neural networks with reproducing kernel Banach spaces", arXiv:2109.09710v2.

The source asks how Hilbert-space representer theorems extend to Banach spaces and later notes that its RKBS representer theorem gives atoms `K_{x'_i}` with `x'_i` not necessarily in the training set. This packet gives a finite three-point RKBS where that caveat is sharp: the regularized ERM problem has a unique minimizer, and its representing atom is the middle point, while the training set consists only of the two endpoints.

Main construction:

- Let `X={-1,0,1}` and define the positive definite kernel matrix
  `[[1,3/5,0],[3/5,1,3/5],[0,3/5,1]]`.
- Use the RKBS `B={f_mu: mu in M(X)}` with the total-variation quotient norm. Since the kernel matrix is invertible, this is just `ell_1^3` through the representing measure.
- Train only at `x=-1` and `x=1`, with labels `1,1` and loss `L(y,z)=3|y-z|`.
- The unique minimizer is represented by `(5/3) delta_0`; it has no training-site atom.
- Any representation supported only on the training points has strictly larger objective value.

Files:

- `main.tex`: proof packet source.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: local copy of the source arXiv PDF.
- `figures/natural_question_crop.png`: crop of the source's motivating representer-theorem question.
- `figures/training_site_caveat_crop.png`: crop of the source's statement that atoms need not be training points.
- `code/finite_rkbs_training_site_check.py`: exact rational and numerical checks.
- `code/crop_source_passages.py`: reproducible crop script.

Novelty check:

- Local lightweight indexes were searched for `2109.09710`, `training point`, `training site`, `representer theorem`, and RKBS terms; no prior exact packet was found.
- Bounded web searches on 2026-06-28 for exact phrases around RKBS representer atoms/training-set points and `2109.09710` found no separate known answer beyond the source arXiv record.

Human-review recommendation: check that the finite positive definite kernel example is accepted as an RKBS instance under the paper's Example 3.8/RBF-kernel discussion. The proof is otherwise a two-variable `ell_1` minimization.
