# Verification report

Verdict: `full_solution_likely_valid`

## Formal audit

1. For \(Z=(A^{1/2}BA^{1/2})^{1/2}\), the aligned factors
   \(G=A^{1/2}\) and \(M=A^{-1/2}Z\) satisfy \(GG^*=A\),
   \(MM^*=B\), and \(G^*M=Z\).
2. The source's exact formula becomes
   \(W_2^2=2\operatorname{tr}(S-Q_\varepsilon^{1/2})\), with
   \(S=X+Y\), \(X=A\), \(Y=ZA^{-1}Z\), and
   \(Q_\varepsilon=X^2+Y^2+Xf_\varepsilon(Z)Y+Yf_\varepsilon(Z)X\).
3. The expansion \(f_\varepsilon(Z)=I-(\varepsilon/2)Z^{-1}+O(\varepsilon^2)\)
   is uniform because \(Z\succ0\) is finite dimensional.
4. The two noncommutative terms simplify exactly:
   \(XZ^{-1}Y=YZ^{-1}X=Z\). Hence
   \(Q_\varepsilon=S^2-\varepsilon Z+O(\varepsilon^2)\).
5. Trace-square-root differentiation gives the asserted exact limit
   \(\operatorname{tr}(S^{-1}Z)\).
6. The identity
   \(S-2Z=(X-Z)X^{-1}(X-Z)\succeq0\) yields the sharp bound \(d/2\).
7. Equality forces \(X=Z\), equivalently \(A=B\); conversely \(A=B\)
   attains \(d/2\).

No unproved mathematical dependency remains beyond the exact formula already proved in the source paper.

## Computational sanity check

`code/numerical_check.py` uses a fixed random seed and tests five independent covariance pairs in each dimension \(1,2,5,10\). It directly evaluates the source formula for \(\varepsilon=10^{-3},3\cdot10^{-4},10^{-4}\), compares against the closed limit, verifies the \(d/2\) bound, checks the positive-semidefinite AM--GM identity numerically, and tests equality when \(A=B\).

The script passes. These computations only guard against sign, order, and factor-of-two mistakes; they are not proof.

## Bounded novelty/literature check

Performed 21 July 2026:

- Local indexes searched: `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, `proof_gaps/index.tsv`.
- Local keys: `2512.19457`, `spectral shrinkage`, `Gaussian entropic optimal transport`, `universal bounds`.
- Web/arXiv keys: exact title plus `Universal Bounds`; `Wasserstein Gaussian entropic coupling d/2`; `Gaussian entropic optimal transport coupling convergence sharp constant`; and an arXiv-restricted variant.
- The current arXiv version still states Conjecture 3.1.
- No separate primary paper claiming this exact formula or the sharp constant \(C_d=d/2\) was located.

This is a bounded search and does not establish novelty conclusively.

## Human-review focus

Check the parameter normalization and exact-matrix formula in source Theorem 3.10. In particular, verify that its \(f_\varepsilon\) is the function used here and that the positive-definite aligned factor is \(M=A^{-1/2}Z\). After that, the remainder is a short self-contained matrix argument.
