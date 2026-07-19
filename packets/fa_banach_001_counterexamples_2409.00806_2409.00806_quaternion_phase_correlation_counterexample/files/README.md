# Quaternion phase-correlation counterexample

**Status:** candidate counterexample, likely valid; independent human review required.

This packet gives a negative answer to Question 3.7 of Farhangi and
Tucker-Drob, arXiv:2409.00806v3. The counterexample already violates property
(i) in the question. It works for the countably infinite amenable group
`Q8 x Z`, so it is not an artifact of allowing finite groups.

## Result in one paragraph

Use the defining two-dimensional representation of the quaternion group and a
unit vector whose Bloch vector is `(1,1,1)/sqrt(3)`. Four quaternion translates
of this vector give an extreme `4 x 4` complex correlation matrix of rank two:
the four associated rank-one projectors span all Hermitian `2 x 2` matrices.
If the coefficient function of the representation were the correlation of a
circle-valued observable, the same matrix would be an average of rank-one
phase correlation matrices. Extremality would force those rank-one matrices
to equal the rank-two matrix, which is impossible.

## Packet contents

- `solution_packet.pdf`: self-contained statement, proof, source evidence,
  verification notes, limitations, and references.
- `main.tex`: LaTeX source for the packet.
- `source_paper.pdf`: local copy of arXiv:2409.00806v3.
- `figures/open_problem_crop.png`: source crop of Question 3.7 on PDF page 18.
- `code/verify_quaternion_elliptope.py`: deterministic numerical checks of the
  group, Bloch-vector, spanning determinant, and Gram-matrix identities.
- `code/make_source_crop.py`: reproducible source-crop renderer.
- `verification.md`: concise verifier report and novelty-search bounds.

## Reproduce the checks

From the repository root:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2409.00806_quaternion_phase_correlation_counterexample/code/verify_quaternion_elliptope.py
```

The numerical script is only a sanity check. The proof in the PDF establishes
the relevant determinant and rank statements exactly.

## Human-review focus

The most valuable independent check is the short passage converting a
circle-valued realization into a barycenter of rank-one phase matrices. A
second reviewer should also check the left/right convention in
`phi(g_j^{-1} g_i) = <q_i xi, q_j xi>`; the packet declares the source paper's
linear-in-the-first-variable convention explicitly.

The bounded search found the standard extreme-correlation-matrix criterion,
but no paper applying this quaternion example to Question 3.7. That does not
establish publication-level novelty.
