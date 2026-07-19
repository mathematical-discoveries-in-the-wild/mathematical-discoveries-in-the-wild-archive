# Full Result: Fixed-ONB Banded Operator Algebra

Status: `full_solution_likely_valid` for Remark 1.92, Question 2 only.

Source: Palle Jorgensen and Feng Tian, "Noncommutative analysis,
Multivariable spectral theory for operators in Hilbert space, Probability,
and Unitary Representations", arXiv:1408.1164.

## Question Addressed

Remark 1.92 asks two open questions about banded operators/matrices. This
packet answers the second one: after fixing an ONB `(e_i)` and the dense common
domain `D = span{e_i}`, identify the `*`-algebra of unbounded operators whose
matrix is banded with respect to that ONB.

The first question, asking for an intrinsic geometric characterization of
operators which admit some banding ONB, is not addressed.

## Result

The maximal common-core `*`-algebra is exactly the finite-propagation algebra
with respect to the fixed ONB:

```text
A_band(D) = { A:D -> D : there is r >= 0 such that
              <e_i, A e_j> = 0 whenever |i-j| > r }.
```

Every other common-domain `*`-algebra all of whose elements are banded is just
a `*`-subalgebra of this maximal algebra. Thus the source question has a
unique answer only after this natural maximality convention is made explicit.

## Verification

- Source open-question crop: `figures/open_problem_crop.png` and
  `figures/open_problem_crop_2.png` from PDF pages 73--74.
- The proof is algebraic: bandwidth is preserved by adjoint and adds under
  products.
- A small finite-matrix sanity check is included in
  `code/verify_bandwidth_arithmetic.py`.
- Bounded novelty check: local run indexes were searched for the arXiv id and
  core phrases (`banded operator`, `finite propagation`, `finite band`,
  `band-dominated`, `common domain`). Web search on 2026-07-03 found adjacent
  band-dominated-operator literature but no exact packet or local duplicate
  for this fixed-ONB common-core question. The result is elementary and should
  be treated as likely folklore, but it appears to answer the literal source
  question.

## Files

- `main.tex`: proof packet.
- `solution_packet.pdf`: rendered proof packet.
- `source_paper.pdf`: arXiv PDF.
- `figures/`: source evidence crops.
- `code/verify_bandwidth_arithmetic.py`: arithmetic sanity check.

