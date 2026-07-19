# Verification report

**Verdict:** candidate counterexample, likely valid; human review needed.

## Exact checks in the proof

1. `Q8 = {+/-I, +/-iX, +/-iY, +/-iZ}` is a group of unitary matrices, and
   `G = Q8 x Z` is countably infinite and amenable.
2. The displayed vector `xi` has norm one and Bloch coordinates
   `(1,1,1)/sqrt(3)`.
3. Conjugating its rank-one projector by `I,iX,iY,iZ` gives the four displayed
   Pauli-coordinate rows. Their determinant is `-16/(3 sqrt(3))`, so the
   projectors span `Herm(2)` over the reals.
4. The resulting Gram matrix is an extreme point of the complex correlation
   elliptope by the proved spanning lemma.
5. Its rank is two (equivalently, its spectrum is `0,0,2,2`).
6. A circle-valued realization would express this matrix as a barycenter of
   rank-one phase correlation matrices. Since the matrix is extreme in the
   larger correlation elliptope, every matrix in such a barycenter must equal
   it, contradicting the ranks.

No unproved lemma, scalar inequality, or computational assumption is used.

## Computational sanity check

Command:

```sh
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2409.00806_quaternion_phase_correlation_counterexample/code/verify_quaternion_elliptope.py
```

The script checks all 64 products in the eight-element matrix model of `Q8`,
the vector normalization, the four Bloch coordinates, the exact determinant
formula to floating-point tolerance, the projector span rank, the explicit
Gram matrix, and its eigenvalues and rank. These checks guard against signs and
convention errors; they are not used as proof.

## Bounded novelty and duplicate search (2026-07-19)

- Searched the run registry, solution index, and cheap local full-text indexes
  for arXiv `2409.00806` and the core terms `circle-valued`, `positive
  definite`, `phase correlation`, `quaternion`, and `extreme correlation`.
- Searched the web/arXiv using the exact title, the exact question phrase,
  both authors with `Question 3.7`, and close combinations involving
  `circle-valued`, `positive definite`, and `extreme correlation matrix`.
- Checked later/citing-result search surfaces exposed by arXiv and searched for
  a later paper explicitly answering the question.
- Located Li--Tam's standard 1994 background on extreme correlation matrices,
  but no source applying the obstruction here or explicitly answering
  Farhangi--Tucker-Drob Question 3.7.

This was a bounded search, not a systematic citation review. It supports only
`no duplicate found`, not a claim of publication-level novelty.

## Recommended human review

Review the coefficient/Koopman convention and the extreme-point barycenter
step first. If those pass, the proof is a complete negative answer to the
question as stated, including its intended countably infinite amenable scope.
