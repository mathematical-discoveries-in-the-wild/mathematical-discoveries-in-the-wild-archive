# Attempt log

Target: the question after Definition 4.1 of arXiv:2404.16338 asking whether
the integral-representation space is generally the completion of the algebraic
tensor product for the displayed seminorms.

## Route selection

The paper-level queue signal first exposed an introductory open problem that
the same paper answers.  That signal was discarded.  A separate live question
appears on page 22 and was selected because it asks for a general topological
identification, so a single explicit function-space counterexample suffices.

## Construction

The factor space was chosen as a concrete step-function realization of
`ell_infinity`.  Independent Rademacher coordinates then give the correlation
kernel `delta_mn`, which belongs to the integral-representation space with
cost one.

## Repaired false start

The first separation idea associated a sampled kernel to an operator from
`ell_1` to `ell_infinity`: algebraic projective tensors yield nuclear, hence
compact, operators, while the diagonal kernel yields the noncompact canonical
inclusion.  This only excludes completion in the Banach projective norm and is
not enough, because Definition 4.1 allows arbitrary integral representations
when defining its seminorm on algebraic tensors.

The argument was repaired without comparing tensor norms.  The seminorm in
Definition 4.1 directly dominates pointwise sup norm for the chosen factors.
Every algebraic tensor samples to a finite-rank matrix, and finite-rank matrices
stay at uniform distance at least `1/2` from the infinite identity matrix.
This proves separation in the exact seminorm named by the source question.

## Outcome

Candidate full negative answer, likely valid.  No computational dependency or
unproved lemma remains.

