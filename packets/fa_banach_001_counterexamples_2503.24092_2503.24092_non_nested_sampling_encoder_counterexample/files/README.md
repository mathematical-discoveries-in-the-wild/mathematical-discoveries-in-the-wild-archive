# Non-nested sampling encoders: counterexample to the literal question and repaired theorem

Status: candidate counterexample likely valid, with positive repair.

Source: Janek Goedeke and Pascal Fernsel, *New universal operator approximation theorem for encoder-decoder architectures (Preprint)*, arXiv:2503.24092.

## Open question

After Theorem 3.20, the source asks whether the theorem still holds when the sampling points for the sampling encoder are not nested/refining:

> If, more generally, individual sampling points `{y_1^(n), ..., y_k(n)^(n)}` are chosen for each `n`, it remains an open question whether the previous theorem still holds.

Theorem 3.20 assumes a compact metric space `Omega` without isolated points, a Schauder basis of `C(Omega,K)`, and an unbounded dimension sequence `k(n)`. Its conclusion is that some `f` separates the sampling encoder from the first `k(n)` basis-coefficient encoder for all sufficiently large `n`.

## Result

The literal non-nested version is false if `k(n)` is only assumed unbounded.

Take `Omega=[0,1]` and a classical Faber-Schauder basis of `C([0,1],K)` ordered so that the first coefficient functional is evaluation at `0`. Let

```text
k(n)=1 for odd n,   k(n)=n for even n.
```

For every odd `n`, choose the one sampling point `y_1^(n)=0`. Then the sampling encoder is exactly the first basis encoder for every `f`, at infinitely many arbitrarily large odd indices. Therefore no single `f` can separate the two encoders for all sufficiently large `n`.

There is also a repaired positive theorem: if the non-nested dimensions satisfy `k(n) -> infinity`, then the conclusion of Theorem 3.20 does hold. The proof uses the source's Theorem B.2 plus Baire category.

## Proof intuition

The counterexample exploits a loophole in "unbounded": the sequence can keep returning to dimension one. If the first basis coefficient is a point evaluation, those repeated one-dimensional sampling encoders can agree exactly with the first basis encoder forever.

The repair explains why this is the only obstruction of this type. If `k(n)->infinity` and exact agreement occurred infinitely often as operators, every fixed Schauder coefficient functional would eventually be forced to be an evaluation functional. The source's Theorem B.2 says that no Schauder basis of `C_b(Omega,K)` can have all coefficients given by sampling at a sequence of points when `Omega` has no isolated points. Hence only finitely many exact operator agreements remain. A Baire category argument then chooses one function outside all the remaining equality kernels.

## Verification

- Cheap indexes showed no prior packet for `2503.24092` or this sampling-encoder question.
- Source TeX was inspected around Theorem 3.20, the open-question sentence, and Appendix Theorem B.2.
- Bounded web searches for exact phrases from the open question found only arXiv:2503.24092 and no later answer.
- The source PDF is included as `source_paper.pdf`; the open-question crop is in `figures/open_problem_crop.png`.

## Human review recommendation

Review as a counterexample to the literal non-nested/unbounded formulation, with the repaired `k(n)->infinity` theorem as useful context. If the authors intended only `1/n`-covering sampling schemes, the repaired theorem is the directly relevant answer.
