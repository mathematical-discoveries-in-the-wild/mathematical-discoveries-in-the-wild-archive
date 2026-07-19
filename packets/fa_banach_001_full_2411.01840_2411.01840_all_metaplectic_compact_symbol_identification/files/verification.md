# Verification report

Verdict: `full_solution_likely_valid`.

## Formal audit

1. **Exact source scope.** The source's Theorem 5.11 assumes simultaneous diagonalizability of two matrices in a symplectic decomposition.  Remark 5.14 explicitly suggests relaxing that hypothesis.  The candidate theorem keeps the same compact-symbol class and Gaussian window and proves the conclusion for every symplectic matrix.

2. **Uniform logarithm branch.** Compactness of (K) permits one (\varepsilon>0) for which every (e^{\varepsilon t^TCe_j}) remains in the disk (|w-1|<r<1).  The Taylor series for (\log w) therefore converges uniformly.  Its partial sums are polynomials in the lattice exponential (w), so every linear form (t^TCe_j) is in the uniform closure.  Invertibility of (C) recovers every real coordinate.

3. **Stone--Weierstrass use.** Once all real coordinate functions are in the closed exponential algebra, it contains the restrictions of all complex polynomials in those coordinates.  This self-adjoint polynomial algebra contains constants and separates points of arbitrary compact (K\subset\mathbb R^m), hence is uniformly dense in (C(K)).  Continuous functions are dense in (L^2(K)).

4. **Metaplectic Gaussian form.** The three standard metaplectic generators preserve the class (c e^{-\pi t^TZt}) with (Z=Z^T) and (\operatorname{Re}Z>0): chirps add a purely imaginary symmetric part, real dilations act by congruence, and Fourier transform sends (Z) to (Z^{-1}).  The source states that these generators generate the symplectic group.

5. **Invertibility of the orbit matrix.** With symplectic first block column \(\binom PR\), the orbit coefficient is (C=ZP+iR) (a harmless sign change may occur under another modulation convention).  If (Cu=0), multiplication by ((Pu)^*), positivity of (\operatorname{Re}Z), and symmetry of (P^TR) give (Pu=0).  Then (Ru=0), and the full column rank of \(\binom PR\) gives (u=0).  Thus (C\in GL_m(\mathbb C)).

6. **Identification transfer.** If all diagonal Gaussian measurements of (T\in\mathcal P_{\mathcal A,K}) vanish, then (\sigma_T^{\mathcal A}\) is orthogonal in (L^2(K)) to a dense metaplectic Gaussian lattice.  Hence (\sigma_T^{\mathcal A}=0), so (T=0).

## Computational sanity check

`code/sanity_check.py` generated 250 random symplectic matrices in dimensions 1 through 6 and random complex symmetric (Z) with positive-definite real part.  The smallest sampled singular value of (ZP+iR) was

```text
1.727867e-01
```

It also tested the logarithm-series coordinate recovery for a random invertible (4\times4) complex matrix on 4000 points.  At Taylor order 60, the maximum coordinate error was

```text
2.851971e-14
```

These computations are not part of the proof.

## Bounded novelty check

Searched on 2026-07-19:

- the run's `registry_index.tsv`, `solutions/index.tsv`, `attempts/index.tsv`, and `proof_gaps/index.tsv` for arXiv:2411.01840, “metaplectic”, “operator identification”, and close variants;
- exact-title and exact-phrase web/arXiv searches for “Metaplectic Quantum Time--Frequency Analysis”, “simultaneously diagonalisable”, “metaplectic operator identification compactly supported symbols Gaussian lattice”, and complex exponential lattice density;
- the source paper's theorem, proof, final remark, and bibliography.

No later paper or pre-existing result removing Theorem 5.11's diagonalization hypothesis was found in this bounded search.  The source paper itself is the only exact hit.  The density argument may well be independently known as a special exponential approximation observation, so novelty confidence is high for the exact theorem upgrade but not asserted as exhaustive literature priority.

## Limitations

- The lattice depends on the symplectic matrix and on the compact set.
- The theorem proves injectivity/identifiability, not a stable sampling inequality or an explicit reconstruction frame.
- It does not contradict the impossibility of lattice identification for unrestricted Hilbert--Schmidt operators.

Human verifier focus: check the metaplectic block convention in the formula for (ZP+iR).  Either sign before (iR) yields the same invertibility proof.
