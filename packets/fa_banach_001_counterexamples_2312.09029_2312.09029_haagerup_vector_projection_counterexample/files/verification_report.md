# Verification report

Packet: `2312.09029_haagerup_vector_projection_counterexample`

Date: 2026-07-21

Verdict: `counterexample_likely_valid`, suitable for human review.

## Exact verification

Command run from the repository root:

```bash
/opt/homebrew/Caskroom/miniforge/base/envs/sandbox/bin/python \
  runs/fa_banach_001/solutions/counterexamples/2312.09029_haagerup_vector_projection_counterexample/code/verify_projection.py
```

Exact output summary:

```text
EXACT CHECKS: PASS
rank(P) = 2
diag(Q) = [1, 1, 1, 1]
P*Q == Q and Tr(P*Q) = 4
```

The script constructs

\[
A=\begin{pmatrix}
1&0\\0&1\\2^{-1/2}&2^{-1/2}\\2^{-1/2}&i2^{-1/2}
\end{pmatrix},\quad
Q=AA^*,\quad P=A(A^*A)^{-1}A^*,
\]

using exact SymPy arithmetic.  It asserts:

- \(P=P^*\) and \(P^2=P\);
- \(I-P\) is also a Hermitian idempotent;
- \(\operatorname{rank}P=\operatorname{rank}Q=2\);
- every diagonal entry of \(Q\) is exactly \(1\);
- \(PQ=Q\);
- \(\operatorname{Tr}(PQ)=4\).

These are all computationally checkable algebraic identities used by the
formal proof.

## Numerical sanity check

The same script fixes the irrelevant global phase, applies BFGS from two
structured and 32 deterministic pseudorandom starting points, and maximizes
\(u^*Pu\) over the three remaining phases.  It reports:

```text
optimizer success = True
F^2 approximately = 3.930567311133
phases approximately = [0, -pi/4, -pi/8, pi/8]
Haagerup lambda approximately =
  [0.21677275, 0.21677275, 0.28322725, 0.28322725]
max imaginary residual in lambda = 3.13e-17
Haagerup candidate squared norm approximately = 4.367919805265
exact optimum squared cbF norm = 4
NUMERICAL CHECKS: PASS
```

The numerical values are not part of the proof and do not certify global
optimality of the phase search.  They independently agree with the exact
conclusion that the Haagerup vector is nonuniform and strictly suboptimal.

## Proof-only steps

Two decisive steps are proved in `main.tex` rather than delegated to code:

1. The range
   \(L=\{(a,b,(a+b)/\sqrt2,(a+ib)/\sqrt2)\}\) contains no unimodular
   vector, because the last two modulus equations force both the real and
   imaginary parts of \(a\overline b\) to vanish while
   \(|a\overline b|=1\).
2. If a feasible diagonal \(D\ge P\) has trace \(4\), then
   \(\operatorname{Tr}((D-P)Q)=0\).  Positivity makes \(D-P\) annihilate
   \(\operatorname{ran}Q=L\), and coordinatewise action on \(L\) forces
   \(D=I_4\).  Thus the cbF optimizer is unique.

## Reproducibility and review focus

The source question crops are reproducible with
`code/make_open_problem_crops.py` after rendering source PDF pages 11 and 12
at 180 dpi as `tmp/pdfs/source-11.png` and `source-12.png`.

Recommended review focus:

- match the packet's diagonal SDP lemma to the source's normalization of the
  cbF norm;
- check the equality case for two positive semidefinite matrices with zero
  trace product;
- check that uniform Haagerup weights imply
  \(Pu=(\|P\|_F^2/4)u\), which is impossible for the constructed range.
