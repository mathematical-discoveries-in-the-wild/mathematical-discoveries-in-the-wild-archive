# Two partial results on extreme projective tensors

Status: `candidate_partial_result_likely_valid`

Source: Luis C. García-Lirola, Guillaume Grelier, Gonzalo
Martínez-Cervantes, and Abraham Rueda Zoca, *Extremal structure of
projective tensor products*, arXiv:2211.13559, Questions 3.9 and 3.10.

## Result

For real Banach spaces (X,Y):

1. If (x\in S_X) is strongly exposed and (y\in S_Y) is a preserved
   extreme point, then (x\otimes y) is a preserved extreme point of
   (B_{X\widehat\otimes_\pi Y}). The same holds with the factors reversed.
   No approximation property or compact-operator assumption is used.
2. If an extreme point (z\in B_{X\widehat\otimes_\pi Y}) attains its
   projective norm through a nuclear representation, then (z) is a basic
   tensor. Consequently any non-basic example sought in Question 3.10 must be
   non-norm-attaining.

The first proof identifies the bidual face of a tensor functional when one
factor functional strongly exposes its point. Near equality forces every
elementary tensor to concentrate, up to the simultaneous sign ambiguity, near
the one-dimensional tensor fiber (x\otimes B_Y). Goldstine's theorem lifts
this concentration to the bidual face, where preserved extremality of (y)
finishes the argument.

## Scope

This does not answer either source question in full. Question 3.9 remains open
when neither factor is strongly exposed. Question 3.10 remains open for
non-norm-attaining tensors.

A bounded arXiv search used the exact question phrases and the keywords
`preserved extreme`, `denting`, `strongly exposed`, `basic tensor`, and
`projective tensor`. It found arXiv:2510.21234, which gives a different positive
subcase under (L(X,Y^*)=K(X,Y^*)) and an approximation-property hypothesis,
and explicitly leaves the general question open. No source stating either
result above was located. Novelty confidence is therefore bounded, not
definitive.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem statements and complete proofs.
- `source_paper.pdf`: arXiv:2211.13559.
- `figures/open_problem_crop.png`: Questions 3.9 and 3.10 on source PDF page 13.
- `VERIFICATION.md`: proof and rendering checks.

Human review should focus on the tensor-face concentration lemma and the use of
Goldstine's theorem to identify the weak-star face with the bidual tensor
fiber.
