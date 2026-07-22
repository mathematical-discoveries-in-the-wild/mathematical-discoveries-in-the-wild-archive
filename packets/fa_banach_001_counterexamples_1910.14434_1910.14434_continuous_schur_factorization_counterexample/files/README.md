# Continuous Schur factorization counterexample

Result type: `counterexample` (full negative answer)

Status: candidate full counterexample, likely valid pending expert review.

## Source problem

Steen, Todorov, and Turowska, Question 4.13(i) in *Local Operator Multipliers
and Positivity* (arXiv:1206.3889), ask whether a continuous Schur multiplier
always admits continuous bounded `ell^2` factors. Arhancet's
*Dilations of Markovian Semigroups of Measurable Schur Multipliers*
(arXiv:1910.14434) answers the positive version and predicts a negative answer
to part (i).

## Claimed contribution

The packet gives a negative answer on the compact metric space
`X = N union {infinity}` equipped with the full-support probability measure
`mu({n}) = 2^{-n}`. Partition `N` into blocks of size `2^k` and put a
normalized Sylvester Hadamard matrix on each diagonal block, with zero entries
between blocks and at infinity.

The entries tend uniformly to zero, so the kernel is continuous. Every block
has Schur multiplier norm exactly one. If continuous factors existed,
subtracting their values at infinity would make both factors tend uniformly
to zero on late blocks, forcing those block norms to tend to zero. This is the
contradiction.

## Files

- `main.tex`: complete proof source.
- `solution_packet.pdf`: compiled proof packet.
- `source_paper.pdf`: Arhancet's source paper, arXiv:1910.14434.
- `question_source.pdf`: Steen--Todorov--Turowska, arXiv:1206.3889.
- `figures/question_4_13_crop.png`: source evidence for the exact question.
- `code/verify_hadamard_blocks.py`: finite-block algebra sanity checks.
- `verification.md`: independent checklist, command, and review focus.
- `tmp/pdfs/`: rendered pages used for visual QA.

## Novelty check

Bounded searches on July 22, 2026 used the exact question, the source remark,
and combinations of continuous Schur multipliers with Hadamard blocks,
one-point compactifications, and continuous Hilbert factorizations. They found
the two source papers and adjacent factorization literature, but no published
negative solution. Novelty confidence is moderate pending specialist review.

## Human review focus

- Confirm the standard identification between the atomic integral-kernel
  multiplier and entrywise multiplication on matrices; the proof explains why
  the atom weights cancel.
- Confirm that the factorization estimate is for the ordinary operator norm,
  not only the completely bounded norm.
- Check the centering step at infinity and the uniform convergence on the
  moving finite blocks.
