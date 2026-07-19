# Verification report

Verdict: `candidate counterexample - likely valid`

## Hypothesis audit

- The coordinates use the source order `(12,13,14,23,24,34)`.
- Both proposed bivectors obey the Plucker relation
  `z12*z34-z13*z24+z14*z23=0`.
- Their Euclidean squared norms are
  `a^2+b^2+4t^2=(a+b)^2=1`, so they are unit simple bivectors.
- The associated unoriented planes are distinct: two unit simple
  representatives of one plane differ only by sign, while `x!=+/-y` for
  `a!=b` and `t>0`.
- For every `p>1`, the ell-p norm is positive and differentiable at these
  nonzero bivectors, so the source's `B_G` formula applies.
- The two bivectors have the same multiset of absolute coordinates, so the
  omitted ell-p normalization is a common positive scalar and cannot alter
  the kernel.

## Algebra audit

Writing `K(z)` for the skew matrix of a bivector and
`phi_p(z_ij)=sign(z_ij)|z_ij|^(p-1)`, the source formula is

```text
B_p(z)=K(phi_p(z))*K(z)^T / ||z||_p^(p-1).
```

Direct symbolic multiplication produces the two matrices printed in the proof.
Their equal average is symmetric with diagonal `d_p` and signed off-diagonal
entries of magnitude `c_p`.  Its characteristic polynomial is

```text
((lambda-d_p)^2-2*c_p^2)^2.
```

Thus the eigenvalues and multiplicities stated in the packet are exact.

At the continuous endpoint `p=1`, the smaller unnormalized eigenvalue is

```text
1/2+2t-sqrt(2)(t+1/2)<0,
```

because `t<1/(2sqrt(2))`.  At `p=2` it equals
`1/2-sqrt(ab)>0`.  A root therefore lies strictly inside `(1,2)`.
At a root, `d_p=sqrt(2)c_p>0`, so the average has exactly two zero and two
strictly positive eigenvalues.  The non-Dirac two-atom measure violates (AC2).

## Computational check

Run:

```text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/counterexamples/2011.09922_lp_plucker_atomic_condition_counterexample/code/verify_counterexample.py
```

The script checks the Plucker/norm identities, derives both matrices and their
characteristic polynomial symbolically, and bisects the concrete
`a=4/5,b=1/5` root.  This code is a transcription/error check; the proof is the
symbolic calculation and intermediate-value argument in `main.tex`.

## Literature and scope audit

On 2026-07-19, the run's registry, solution, attempt, and proof-gap indexes had
no match for arXiv:2011.09922 or the core scalar-atomic/Plucker ell-p terms.
Bounded primary-source web searches used the phrases `scalar atomic condition`,
`uniform scalar atomic condition`, `Plucker atomic condition`, and the source
title/authors.  The only exact hit was the source paper.  Two later relevant
primary sources were inspected:

- arXiv:2401.10858v2 proves that (AC) implies strict polyconvexity, but does not
  settle the Plucker ell-p family;
- arXiv:2601.10647v2 treats codimension-one ell-p anisotropies in a different
  Michael-Simon theorem and does not address this `G(4,2)` claim.

No prior proof or counterexample to Remark 6.4 was found in this bounded
search.  This is not an exhaustive novelty guarantee.

## Human-review focus

1. Check the index placement in `K(phi_p(z))*K(z)^T` against equation (6.2) of
   the source.
2. Check the signs in the displayed `B_p(x)` and `B_p(y)` matrices.
3. Confirm that the source's (AC2) uses kernel dimension `n=2` for `G(4,2)`.
