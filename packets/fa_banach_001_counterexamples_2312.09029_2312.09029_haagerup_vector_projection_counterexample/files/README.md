# Counterexample packet: Haagerup's vector need not be cbF-optimal

Status: `counterexample_likely_valid` (new full negative answer, pending human review)

Source: Erik Christensen, *Some points of view on Grothendieck's
inequalities*, arXiv:2312.09029, especially the introduction and Section 3,
pp. 11-12 of the arXiv PDF.

## Result

The paper asks whether Haagerup's constructive vector always produces the
optimal cbF/operator factorization of a complex matrix, and says that the
authors expect a negative answer but have no definite result.  This packet
gives an explicit negative answer.

Let

\[
A=\begin{pmatrix}
1&0\\0&1\\2^{-1/2}&2^{-1/2}\\2^{-1/2}&i2^{-1/2}
\end{pmatrix},\qquad
X=P=A(A^*A)^{-1}A^*.
\]

Thus \(P\) is the orthogonal projection onto

\[
L=\{(a,b,(a+b)/\sqrt2,(a+ib)/\sqrt2):a,b\in\mathbb C\}.
\]

The optimal cbF factorization vector is uniquely
\((1/2,1/2,1/2,1/2)\), whereas every Haagerup vector for \(P\) is
nonuniform.  Consequently Haagerup's factorization is strictly suboptimal.

The proof is exact and elementary.  It rewrites the squared cbF optimization
as the diagonal semidefinite program

\[
\|X\|_{cbF}^2=\min\{\operatorname{Tr}D:D\text{ diagonal},\ D\ge X^*X\}.
\]

The matrix \(Q=AA^*\) has diagonal \(1\), range \(L\), and \(PQ=Q\).
It certifies that the SDP optimum is \(D=I_4\), uniquely.  On the other hand,
\(L\) contains no unimodular vector.  This forces the Haagerup probability
weights arising from any maximizing unimodular vector to differ from
\((1/4,1/4,1/4,1/4)\).

## Packet contents

- `main.tex` and `solution_packet.pdf`: self-contained proof and review packet.
- `source_paper.pdf`: the original arXiv PDF.
- `figures/open_problem_crop_page11.png` and
  `figures/open_problem_crop_page12.png`: full-width source crops spanning the
  open-problem statement.
- `code/verify_projection.py`: exact symbolic identities and a numerical
  phase-optimization sanity check.
- `code/make_open_problem_crops.py`: reproducible crop definitions.
- `verification_report.md`: commands, results, and proof-versus-computation
  boundary.

## Verification

From the repository root:

```bash
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python \
  runs/fa_banach_001/solutions/counterexamples/2312.09029_haagerup_vector_projection_counterexample/code/verify_projection.py
```

The exact part checks \(P=P^*=P^2\), the ranks, \(\operatorname{diag}Q=1\),
\(PQ=Q\), and \(\operatorname{Tr}(PQ)=4\).  The proof that \(L\) has no
unimodular vector and the SDP dual-witness argument are written out in the
packet; the numerical optimization is only a sanity check.

## Novelty check and review recommendation

A bounded search was performed on 2026-07-21 using the exact open-question
phrasing, `Haagerup vector`, `optimal cbF-factorization`, the paper title, and
arXiv:2312.09029.  The search found the source/published paper and unrelated
Grothendieck material, but no later answer or matching projection
counterexample.  This is not an exhaustive priority search, so novelty
confidence is **moderate**.

Recommended human review focus: (1) the diagonal-SDP equivalence with the
source's cbF convention; (2) uniqueness of \(D=I_4\) from the witness
\(Q=AA^*\); and (3) the final implication from uniform Haagerup weights to a
unimodular vector in \(L\).
